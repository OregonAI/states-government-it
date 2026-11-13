#!/usr/bin/env python3
"""Authority references: what the documents we hold say enables them, against what we hold.

  python3 src/authority_refs.py                 # write _meta/eval/authority-refs.json
  python3 src/authority_refs.py --check         # exit 1 if the committed JSON is not what the documents give
  python3 src/authority_refs.py --table         # per-state table (add --state oregon for one state)

Policies and standards cite the rules and statutes that enable them; rules cite statutes. This reads every
document's "## Full text", extracts the citations to THAT STATE'S OWN statutes, administrative rules and
executive orders (the forms are in src/authority_forms.py, derived per state from the documents), and
resolves each against the state's seed file (_meta/sources/<state>.yml):

  HELD      a document's own citation or section range covers it
  STUB      a seed entry with `stub: true` covers it (no document yet)
  LEFT OUT  the state's `left_out` record names it (the recorded reason is kept)
  NOT HELD  none of the above: a candidate for the owner to approve for the seed list

Read-only: it fetches nothing and edits no document. Federal citations (U.S.C., C.F.R., NIST, FIPS,
FedRAMP, Pub. L.) are counted per state and are never candidates.
"""
from __future__ import annotations

import argparse
import dataclasses
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))   # run as `python3 src/authority_refs.py`
from src.authority_forms import FORMS, Code, StateForms

YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)   # same result as safe_load, several times faster
ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "_meta" / "sources"
OUT = ROOT / "_meta" / "eval" / "authority-refs.json"
CONTENT = ("statutes", "rules", "executive-orders", "policies", "standards")
DOC_KIND = {"statutes": "statute", "rules": "rule", "executive-orders": "executive_order",
            "policies": "policy", "standards": "standard"}
QUOTE_WORDS = 40
LAYOUT = r"\s{0,30}"
DASH = "[-\u2010-\u2015]"


def X(rx: str) -> str:
    """Expand `~` (a dash, doubled or spaced, then optional layout whitespace)."""
    return rx.replace("~", r"\s{0,3}" + DASH + "{1,2}" + LAYOUT)


# ---- citations ---------------------------------------------------------------------------------------

@dataclass(frozen=True)
class Cite:
    kind: str            # statute | rule | eo
    code: str            # Code.id, or "EO" / "AO" / "ED"
    level: str           # section | chapter
    sec: str             # canonical token (qualifier/section), or the chapter key
    end: str | None      # end of a range, canonical
    start: int = -1
    stop: int = -1
    year: str | None = None
    raw: str | None = None   # an order number as printed ("2005-22"), for display


def canon(s: str) -> str:
    s = re.sub(r"\s+", "", s)
    return re.sub(DASH + "+", "-", s)


def sortkey(tok: str):
    """Order of section numbers inside a code: digit runs numerically, letter runs after."""
    return tuple((0, int(p)) if p.isdigit() else (1, p.lower()) for p in re.findall(r"\d+|[A-Za-z]+", tok))


def split_q(tok: str):
    return tok.split("/", 1) if "/" in tok else (None, tok)


DES = re.compile(r"(?i:(?P<ch>chapters?|ch\.?|chap\.?|articles?|art\.?|parts?|subchapters?|subch\.?|"
                 r"division|div\.?)|(?P<ti>titles?|tit\.?)|(?P<sc>§§?|sections?|secs?\.?|ss?\.|subsections?))\s*,?\s*")
MID = re.compile(r"[ \t,:;]*(?:\.[ \t]*(?!\n|$))?[ \t,:;]*(?:\n[ \t]*)?[ \t,:.;]*(?:\([A-Za-z&.]{2,8}\)[ \t,:.;]*)?")
SUB = re.compile(r"(?:\s*\(\s?[\w.]{1,8}\s?\)|\s+(?:and|or)\s+\(\s?[\w.]{1,8}\s?\))*")
SECSYM = re.compile(r"(?:(?<!§)§§?|(?<![\w§])(?i:sections?|secs?\.|ss?\.))\s*")
CHAPWORD = re.compile(r"(?<![\w])(?i:chapters?|ch\.)\s*")


AUDIT_NEXT = (r"[ \t,:.;§]+(?:§§?|(?i:sections?|chapters?|ch\.?|articles?|art\.|parts?|subchapters?|titles?|division))?[ \t]*,?[ \t]*"
              r"(?=(?!(?:19|20)\d\d(?![\d.\-]))(?:\d|R\d|[A-Z][a-z]{1,4}\s?\d))")


class Compiled:
    def __init__(self, code: Code):
        self.code = code
        self.prefix = re.compile(r"(?<![\w.])(?:" + X(code.prefix) + ")")
        self.sec = re.compile("(?:" + X(code.sec) + r")(?!\d)")
        self.chap = re.compile("(?:" + X(code.chap) + r")(?![\dA-Za-z.]\d|\d|[A-Za-z])") if code.chap else None
        self.short = re.compile(r"\d{1,6}[A-Za-z]?(?:\.\d+)*") if code.short else None
        self.range_end = re.compile(r"\d{1,6}[A-Za-z]{0,2}(?:\.\d+)?")
        self.suffix = re.compile(r"[ \t,)\]]*(?:\n[ \t]*)?(?:of\s+the\s+|of\s+)?(?:" + X(code.suffix) + ")") if code.suffix else None
        self.suffix_name = re.compile(X(code.suffix)) if code.suffix else None   # a quick "is the code named at all" test
        self.anchor = re.compile(r"(?<![\w.])(?:" + X(code.prefix) + ")" + AUDIT_NEXT)   # audit: a code name followed by a number
        self.suffix_anchor = (re.compile(r"(?<=\d)[ \t,)\]]*(?:\n[ \t]*)?(?:of\s+the\s+|of\s+)?(?P<n>" + X(code.suffix) + ")")
                              if code.suffix else None)
        rep = (r"(?:" + X(code.prefix) + r")(?:[ \t,:;]|\.(?![ \t]*(?:\n|$)))*(?:\n[ \t]*)?(?:§§?|(?i:sections?))?\s*")
        self.sep = re.compile(r"\s*(?:(?P<r>\bto\b|\bthrough\.?|\bthru\b|" + DASH + r")|(?P<l>,|;|&|\band\b|\bor\b))\s*"
                              r"(?:(?:and|or)\s+)?(?P<sw>(?:§§?|(?i:sections?|secs?\.|ss?\.))\s*)?(?P<rp>" + rep + r")?")


def _expand_end(start: str, end: str, rx_full, code: Code) -> str:
    qs, s = split_q(start)
    end = canon(end)
    if rx_full.fullmatch(end) or not s:
        return end
    idx = max(s.rfind(c) for c in ".-:")
    if idx < 0:
        return end
    return (f"{qs}/" if qs else "") + s[: idx + 1] + end


def _sep_qual(m: re.Match, code: Code) -> str | None:
    """The qualifier a repeated code name carries inside a list ("62 O.S. §34.11.1 and 74 O.S. §85.5": 74)."""
    q = next((v for k, v in m.groupdict().items() if k.startswith("q") and v), None)
    if not q:
        return None
    q = re.sub(r"\s+", " ", q).strip()
    return code.qnorm(q) if code.qnorm else q.replace(" ", "").upper()


def parse_list(text: str, pos: int, cc: Compiled, level: str, q: str | None):
    """Section (or chapter) tokens listed from `pos`: [(tok, end_or_None)], and where the list stopped."""
    code = cc.code
    rx = cc.chap if level == "chapter" else cc.sec
    m = rx.match(text, pos)
    if not m:
        return [], pos
    fix = str.upper if level == "chapter" else (code.tokfix or (lambda t: t))
    out = [[fix(canon(m.group())), None, q]]
    p = SUB.match(text, m.end()).end()
    last = p
    first_tok = out[0][0]
    while True:
        s = cc.sep.match(text, p)
        if not s:
            break
        q2 = s.end()
        if level == "chapter" and s.group("sw"):     # "chapter 15 and section 901": the section is not another chapter
            break
        if s.group("rp") and cc.suffix and re.search(r"(?:§|(?i:sections?))\s*$", s.group("rp")):   # "..., 60203, Government Code; section 102235, Health ...":
            break                                           # the repeated name closes the list; it does not open the next
        nq = _sep_qual(s, code) if s.group("rp") else None
        if s.group("r"):
            if out[-1][1] is not None:
                break
            m2 = rx.match(text, q2) or (None if s.group("rp") else cc.range_end.match(text, q2))
            if not m2:
                break
            end = _expand_end(out[-1][0], m2.group(), rx, code)
            lo = out[-1][0]
            if level == "section" and sortkey(split_q(end)[1]) < sortkey(split_q(lo)[1]):
                # a "range" that runs backwards: "74 O.S. § 840-8.1" is one hyphenated section, and a source's own typo
                # ("7923.75-7923.55") is two sections, not a range
                if re.fullmatch(r"\d+", split_q(lo)[1]) and "." in m2.group():
                    out[-1][0] = lo + "-" + canon(m2.group())
                else:
                    out.append([fix(canon(m2.group())), None, nq or q])
            else:
                out[-1][1] = end
        else:
            m2 = rx.match(text, q2)
            if m2:
                tok = canon(m2.group())
                if level == "section" and re.fullmatch(r"\d{1,2}", tok) and re.match(r"\.\s+[A-Z]", text[m2.end():m2.end() + 4]):
                    break    # "Civil Code Section 1798.24; 6. If the form ...": a list number, not a section
                out.append([fix(tok), None, nq or q])
            elif cc.short:
                m2 = cc.short.match(text, q2)
                if not m2:
                    break
                lead = first_tok.split(code.short)[0] + code.short
                out.append([lead + canon(m2.group()), None, nq or q])
            else:
                break
        if nq:
            q = nq
        p = SUB.match(text, m2.end()).end()
        last = p
    qual = lambda t, qq: f"{qq}/{t}" if qq and t else t
    return [(qual(a, qq), qual(b, qq) if b else None) for a, b, qq in out], last


def _qual(m: re.Match, code: Code) -> str | None:
    d = m.groupdict()
    q = next((v for k, v in d.items() if k.startswith("q") and v), None)
    if not q:
        return code.q_default
    q = re.sub(r"\s+", " ", q).strip()
    return code.qnorm(q) if code.qnorm else q.replace(" ", "").upper()


FED_GUARD = {   # a cheap substring test before each federal pattern runs over a whole document
    "usc": ("U.S.C", "USC", "U. S. C", "U.S. C", "U. S.C"), "cfr": ("C.F.R", "CFR", "C. F. R", "C.F. R"),
    "nist": ("NIST", "FIPS"), "fedramp": ("FedRAMP",), "eo_federal": ("Executive Order",),
    "publ": ("Pub. L", "Pub L", "Public Law", "Pub.L", "P.L.", "PL "),
}


def _federal(text: str, mask: bool):
    out, counts = text, {}
    for k, rx in FED_RX.items():
        if not any(g in text for g in FED_GUARD[k]):
            continue
        if mask:
            out, n = rx.subn(lambda m: re.sub(r"[^\n]", " ", m.group()), out)
        else:
            n = len(rx.findall(text))
        if n:
            counts[k] = n
    return out, counts


def mask_federal(text: str) -> str:
    return _federal(text, True)[0]


FED_RX = {
    "usc": re.compile(r"\b\d{1,2}\s*U\.?\s?S\.?\s?C\.?(?:A\.)?\s*(?:§§?|Sec(?:tion)?s?\.?)?\s*[\w.\-()]*"),
    "cfr": re.compile(r"\b\d{1,2}\s*C\.?\s?F\.?\s?R\.?\s*(?:Parts?|§§?)?\s*[\w.\-()]*"),
    "nist": re.compile(r"\bNIST\s*(?:SP|Special\s+Publication|FIPS|IR|CSF)?\s*[\d][\w.\-]*|\bFIPS\s*(?:PUB\s*)?\d+[\w\-]*"),
    "fedramp": re.compile(r"\bFedRAMP\b"),
    "eo_federal": re.compile(r"(?:\bU\.S\.|\bPresidential|\bFederal)\s+Executive\s+Order\s*(?:No\.\s*)?\d+|\bExecutive\s+Order\s*(?:No\.\s*)?\d{5}\b"),
    "publ": re.compile(r"\bPub(?:lic)?\.?\s*L(?:aw)?\.?\s*(?:No\.\s*)?\d{2,3}-\d+"),
}


def count_federal(text: str) -> dict:
    return _federal(text, False)[1]


EO_KINDS = {"executive order": "EO", "executive directive": "ED", "exec. order": "EO", "ex. ord.": "EO",
            "e.o.": "EO", "eo": "EO", "administrative order": "AO"}
EO_HEAD = re.compile(r"(?<![\w])(?P<kind>Executive\s+Orders?|Executive\s+Directives?|Exec\.\s*Order|Ex\.\s*Ord\.|E\.\s?O\.|EO|"
                     r"Administrative\s+Orders?)(?:\s*(?:No\.?|Number|\#)\s*|\s+|\s*:\s*)")
DEFAULT_EO_NUM = r"(?:[A-Z]{1,3}-)?\d{1,4}(?:-\s?\d{1,4}){0,3}[A-Z]?(?![\d]|,\d{3})"
EO_YEAR = re.compile(r"\s*\(\s*(?:[A-Za-z.\- ]+,\s*)?(\d{4})\s*\)")


def norm_eo(num: str) -> str:
    s = re.sub(r"\s+", "-", num.strip()) if re.match(r"[A-Z]{1,3}\s", num) else re.sub(r"\s+", "", num)
    parts = s.upper().split("-")
    out = []
    for i, p in enumerate(parts):
        m = re.fullmatch(r"(\d+)([A-Z]*)", p)
        if m:
            n = m.group(1)
            if len(parts) > 1 and re.fullmatch(r"(19|20)\d\d", n):
                n = n[2:]
            p = str(int(n)) + m.group(2)
        out.append(p)
    return "-".join(out)


_FORMS_CACHE: dict[str, tuple] = {}


def _compiled(state: str):
    if state not in _FORMS_CACHE:
        f = FORMS[state]
        eo_num = re.compile(X(f.eo_num or DEFAULT_EO_NUM)) if f.eo else None
        _FORMS_CACHE[state] = (f, [Compiled(c) for c in f.codes], eo_num)
    return _FORMS_CACHE[state]


FOOTER = re.compile(r"(?m)^[ \t]*" + DASH + r"[ \t]*\d{1,3}[ \t]*" + DASH + r"[ \t]*$")


def _norm_text(text: str) -> str:
    """Same length as the original: zero-width and non-breaking spaces become spaces, and a page-number line
    ("-2-") is blanked, so it can never be read as the end of a range."""
    text = text.replace("\u200b", " ").replace("\xa0", " ")
    return FOOTER.sub(lambda m: " " * len(m.group()), text)


def prepare(text: str) -> str:
    """Text with federal citations blanked out (same length, so offsets still index the original)."""
    return mask_federal(_norm_text(text))


def _eo_kind(raw: str) -> str:
    k = re.sub(r"\s+", " ", raw.lower())
    return EO_KINDS[k.rstrip("s") if k.endswith("s") and not k.endswith("ss") else k]


def _after_prefix(text: str, cc: Compiled, found: list) -> None:
    """Citations that open with the code's name: "ORS 276A.300 to 276A.318", "Gov. Code §§ 11545, 11546"."""
    code = cc.code
    for pm in cc.prefix.finditer(text):
        q = _qual(pm, code)
        pos = MID.match(text, pm.end()).end()
        if code.q_join:
            m = cc.chap.match(text, pos) if q else None
            if m:
                found.append(Cite(code.kind, ns_of(code), "chapter", f"{q}{code.q_join}{canon(m.group())}", None, pm.start(), m.end()))
            continue
        if pos == pm.end() and pos < len(text) and text[pos].isdigit() and pm.end() > pm.start() and text[pm.end() - 1].isalnum():
            continue   # "HRS0094" in a URL is not a citation
        dm = DES.match(text, pos)
        level = "section"
        if dm and dm.group("sc"):       # "Sections § 11145": a word, then the symbol
            dm2 = DES.match(text, dm.end())
            if dm2 and dm2.group("sc"):
                dm = dm2
        if dm:
            if dm.group("ti"):
                continue     # "Title 1, Chapter 206": a title is not the chapter that follows it
            if dm.group("ch"):
                if not cc.chap or (code.chap_words and not re.match(code.chap_words, dm.group("ch"), re.I)):
                    continue
                level = "chapter"
            pos = dm.end()
        toks, end = parse_list(text, pos, cc, level, q if not code.q_is_chapter else None)
        if level == "chapter" and toks and code.chapter is None and not code.q_is_chapter:
            sm = re.compile(r"\s*,\s*(?:§§?|(?i:sections?))\s*").match(text, end)   # "1 MRSA, Chapter 14, §533"
            if sm:                                                                        # the section is the citation
                level = "section"
                toks, end = parse_list(text, sm.end(), cc, "section", q)
        if not toks and level == "chapter":     # "Iowa Code Chapter 8A.201" is a section
            level = "section"
            toks, end = parse_list(text, pos, cc, "section", q if not code.q_is_chapter else None)
        if not toks and level == "section" and cc.chap and code.chap_bare:
            level = "chapter"
            toks, end = parse_list(text, pos, cc, "chapter", q)
        if not toks:
            if code.q_is_chapter and q:      # "M.G.L. c. 66A" with no section: the chapter itself
                found.append(Cite(code.kind, ns_of(code), "chapter", q, None, pm.start(), pm.end()))
            continue
        for a, b in toks:
            if code.q_is_chapter and q and level == "section":
                a = f"{q}/{a}"
                b = f"{q}/{b}" if b else None
            found.append(Cite(code.kind, ns_of(code), level, a, b, pm.start(), end))


def _after_designator(text: str, cc: Compiled, found: list) -> None:
    """Citations that name the code after the list ("section 24-37.5-105, C.R.S.") or, for a code whose section
    numbers are distinctive, not at all ("§ 2.2-2009")."""
    code = cc.code
    if not ((cc.suffix and cc.suffix_name.search(text)) or code.bare):
        return
    marks = list(SECSYM.finditer(text)) + (list(CHAPWORD.finditer(text)) if code.suffix else [])
    for dm in marks:
        level = "chapter" if CHAPWORD.match(text, dm.start()) and not SECSYM.match(text, dm.start()) else "section"
        if level == "chapter" and not cc.chap:
            continue
        toks, end = parse_list(text, dm.end(), cc, level, code.q_default)
        if code.bare_sec and level == "section" and not (cc.suffix and cc.suffix.match(text, end)):
            toks = [(a, b) for a, b in toks if re.fullmatch(code.bare_sec, split_q(a)[1])
                    and (b is None or re.fullmatch(code.bare_sec, split_q(b)[1]))]
        if not toks:
            continue
        sm = cc.suffix.match(text, end) if cc.suffix else None
        if sm:
            stop = sm.end()
        elif code.bare and level == "section":
            stop = end
        else:
            continue
        for a, b in toks:
            found.append(Cite(code.kind, ns_of(code), level, a, b, dm.start(), stop))


def _distinctive(text: str, cc: Compiled, found: list) -> None:
    """A number of a shape no other text prints ("5-11-405") is a citation with no section sign and no code name."""
    code = cc.code
    if not code.bare_any:
        return
    rx = re.compile(r"(?<![\w.\-§/])" + X(code.bare_any) + r"(?![\w\-]|\.\d)")
    for m in rx.finditer(text):
        toks, end = parse_list(text, m.start(), cc, "section", code.q_default)
        for a, b in toks:
            found.append(Cite(code.kind, ns_of(code), "section", a, b, m.start(), end))


def _section_before_name(text: str, cc: Compiled, found: list) -> None:
    """"2-17-505, MCA": a section number straight before the code name, no "section" word."""
    code = cc.code
    if not (cc.suffix and code.sfx_bare and cc.suffix_name.search(text)):
        return
    for m in cc.sec.finditer(text):
        if m.start() and re.match(r"[\w.\-]", text[m.start() - 1]):
            continue
        toks, end = parse_list(text, m.start(), cc, "section", code.q_default)
        sm = cc.suffix.match(text, end) if toks else None
        if sm:
            for a, b in toks:
                found.append(Cite(code.kind, ns_of(code), "section", a, b, m.start(), sm.end()))


def _orders(text: str, f: StateForms, eo_num, found: list) -> None:
    """Executive orders (and administrative orders or directives where the state uses them), by number."""
    allowed = set(f.eo_kinds)
    for hm in EO_HEAD.finditer(text):
        kind = _eo_kind(hm.group("kind"))
        if kind not in allowed:
            continue
        m = eo_num.match(text, hm.end())
        if not m:
            continue
        nums, end = [m.group()], m.end()
        while True:
            sm = re.compile(r"\s*(?:,|and|&)\s*(?:Executive\s+Orders?\s*)?").match(text, end)
            if not sm:
                break
            m2 = eo_num.match(text, sm.end())
            if not m2 or not re.search(r"[-A-Z]", m2.group()):
                break
            nums.append(m2.group())
            end = m2.end()
        ym = EO_YEAR.match(text, end)
        year = ym.group(1) if ym and len(nums) == 1 else None
        for n in nums:
            found.append(Cite("eo", kind, "section", norm_eo(n), None, hm.start(), end, year, re.sub(r"\s+", "", n)))


COMPILED_BEFORE = re.compile(r"(?i)\bExecutive\s+Orders?\s+(?:No\.?\s*)?[\w-]+(?:,\s*as\s+amended)?,?\s*(?:being\s+)?(?:Section\s+)?$")


def _unglue(text: str, c: Cite) -> Cite:
    """A footnote mark run into a section number ("10 MRSA § 13471"): when the document's own footnote URL names
    the shorter section ("title10sec1347.html") and never the longer one, the last digit is the footnote's."""
    q, sec = split_q(c.sec)
    if c.level != "section" or c.end or not re.fullmatch(r"\d{4,6}", sec):
        return c
    if re.search(r"sec" + sec[:-1] + r"(?!\d)", text, re.I) and not re.search(r"sec" + sec + r"(?!\d)", text, re.I):
        return dataclasses.replace(c, sec=(f"{q}/" if q else "") + sec[:-1])
    return c


def extract(state: str, text: str, masked: str | None = None) -> list[Cite]:
    """Citations in `text` to `state`'s own statutes, rules and executive orders, in text order.
    `masked` is `prepare(text)`, when the caller already has it."""
    return extract_ignoring(state, text, masked)[0]


def extract_ignoring(state: str, text: str, masked: str | None = None):
    """(citations, spans the reader recognised and set aside: where an order is compiled, an old number of an order)."""
    f, ccs, eo_num = _compiled(state)
    ignored: list = []
    text = masked if masked is not None else prepare(text)
    found: list[Cite] = []
    custom: list[Cite] = []
    for cc in ccs:
        _after_prefix(text, cc, found)
        _after_designator(text, cc, found)
    for cc in ccs:
        if cc.code.custom:
            rx, fn = cc.code.custom
            for m in re.finditer(rx, text):
                for level, tok in fn(m):
                    custom.append(Cite(cc.code.kind, ns_of(cc.code), level, tok, None, m.start(), m.end()))
    for cc in ccs:
        _section_before_name(text, cc, found)
        _distinctive(text, cc, found)
    if custom:   # a printed form the list grammar cannot read wins over the list reading of the same words
        found = [c for c in found if not any(c.start < k.stop and k.start < c.stop for k in custom)] + custom
    if f.eo:
        _orders(text, f, eo_num, found)
    if f.eo_compiled:   # "Executive Order 2002-14, MCL 18.62": where an order is compiled, not a statute
        ignored += [(c.start, c.stop) for c in found
                    if c.kind == "statute" and COMPILED_BEFORE.search(text[max(0, c.start - 90):c.start])]
        found = [c for c in found if c.kind != "statute" or not COMPILED_BEFORE.search(text[max(0, c.start - 90):c.start])]
    superseded = [c for c in found if re.match(r"(?:,\s*[A-Za-z ]{0,40})?\s*[\[(]\s*now\s", text[c.stop:c.stop + 60])]
    if superseded:      # "1 NMAC 3.3.20 [now 1.24.20 NMAC]": the old number of the rule named beside it
        ignored += [(c.start, c.stop) for c in superseded]
        found = [c for c in found if c not in superseded]
    if f.unglue:
        found = [_unglue(text, c) if c.kind == "statute" else c for c in found]
    found.sort(key=lambda c: (c.start, -c.stop))
    out, edge = [], -1
    for c in found:
        if c.start < edge and not (out and out[-1].start == c.start and out[-1].stop == c.stop):
            continue
        out.append(c)
        edge = max(edge, c.stop)
    return out, ignored


# ---- the seed: what the corpus holds ------------------------------------------------------------------

HELD, STUB, LEFT_OUT, NOT_HELD = "HELD", "STUB", "LEFT_OUT", "NOT_HELD"
WORSE = {HELD: 0, STUB: 1, LEFT_OUT: 2, NOT_HELD: 3}
PARTIAL_UNIT = re.compile(r"\b(?:article|art\.|part|subchapter|subch\.)\s*[IVX\d]", re.I)


def ns_of(code: Code) -> str:
    return code.ns or code.id


def code_of(state: str, code_id: str) -> Code:
    for c in FORMS[state].codes:
        if ns_of(c) == code_id:
            return c
    raise KeyError(code_id)


def chapter_of(code: Code, tok: str) -> str | None:
    """The instrument a section token belongs to (a chapter, article, rule chapter), or None when the
    token does not reveal it."""
    q, s = split_q(tok)
    if code.q_is_chapter:
        return q
    if code.chapter is None:
        return None
    try:
        r = code.chapter(s)
    except (AttributeError, IndexError, ValueError):
        return None
    if r is None:
        return None
    return f"{q}/{r}" if q else r


@dataclass
class Holding:
    status: str
    seed_id: str | None
    citation: str
    reason: str = ""
    chapters: set = None        # {(code, chapter key)}: the whole instrument is covered
    sections: set = None        # {(code, token)}
    ranges: list = None         # [(code, lo, hi)]
    harvested: set = None       # {(code, token)} read from the held document's own section headings
    eos: set = None             # {(code, number, year)}

    def __post_init__(self):
        self.chapters, self.sections, self.harvested, self.eos = set(), set(), set(), set()
        self.ranges = []


@dataclass
class Seed:
    state: str
    holdings: list
    unparsed: list          # held statutes, rules and orders whose citation the table cannot read (a defect)
    n_watch: int = 0
    indexes: list = None    # stubs of an index page (no instrument number to cite)
    uncitable: list = None  # instruments cited by date or session-law chapter, not by a form this tool reads
    history_map: dict = None       # {(namespace, old token): (namespace, token now held)} from the held documents' history lines
    history_ids: dict = None       # {(namespace, old token): held document id}


def add_cover(h: Holding, state: str, c: Cite):
    if c.kind == "eo":
        h.eos.add((c.code, c.sec, c.year))
        return
    code = code_of(state, c.code)
    if c.level == "chapter":
        h.chapters.add((c.code, c.sec))
    elif c.end:
        h.ranges.append((c.code, c.sec, c.end))
    elif chapter_of(code, c.sec) == c.sec:
        h.chapters.add((c.code, c.sec))        # the token is itself the instrument ("8 CCR 1501-5")
    elif code.whole and re.search(code.whole + "$", c.sec) and chapter_of(code, c.sec):
        h.chapters.add((c.code, chapter_of(code, c.sec)))     # "801 CMR 3.00" names regulation 3 whole
    else:
        h.sections.add((c.code, c.sec))


def harvest_sections(state: str, code: Code, qual: str | None, text: str, chapter: str | None = None) -> set:
    """The section numbers a held document prints as its own headings. A heading opens a line; where the document
    marks its headings with the section sign, only those lines count (a History line such as "73 Del. Laws, c. 86"
    also opens with a number and is not a heading). With `chapter`, only tokens of that chapter are kept."""
    has_q = bool(re.search(r"\(\?P<q", code.prefix))
    pre = f"{qual}/" if has_q and qual else ""

    def heads(rx):
        return {(ns_of(code), pre + canon(m.group(1))) for m in re.finditer(rx, text)}
    sym = heads(r"(?m)^[ \t]*§+\s*(" + X(code.sec) + r")(?=[.\s:])")
    got = sym or heads(r"(?m)^[ \t]*(" + X(code.sec) + r")(?=[.\s:])")
    if chapter is not None:    # a heading of another chapter is a cross-reference; a code that cannot tell keeps all
        got = {t for t in got if chapter_of(code, t[1]) in (chapter, None)}
    return got


def history_pairs(state: str, ns: str, rx: str, text: str, h: "Holding | None" = None) -> list:
    """[(old token, current token)] from a held document's history lines: each old number a line prints
    ("[Formerly 291.037]", "C2014, §8B.21") belongs to the last section heading above it."""
    code = code_of(state, ns)
    cc = Compiled(code)
    heads = [(m.start(), canon(m.group(1))) for m in re.finditer(r"(?m)^[ \t]*(?:§+\s*)?(" + X(code.sec) + r")(?=[.\s:])", text)]
    if h is not None:    # only the headings of the section(s) or chapter(s) this entry holds, not a cross-reference opening a line
        declared = {t for c, t in h.sections if c == ns} | {t for c, lo, hi in h.ranges if c == ns for t in (lo, hi)}
        chs = {k for c, k in h.chapters if c == ns}
        if declared and not chs:      # a section-held entry: its own sections, not a cross-reference opening a line
            heads = [(pos, t) for pos, t in heads if t in declared]
        elif chs:
            heads = [(pos, t) for pos, t in heads if chapter_of(code, t) in chs]
    out = []
    for m in re.finditer(rx, text):
        above = [t for pos, t in heads if pos < m.start()]
        if not above:
            continue
        for old in cc.sec.finditer(m.group(1)):
            out.append((canon(old.group()), above[-1]))
    return out


def bare_cites(state: str, text: str, cites: list) -> list:
    """Instruments a left_out record names by bare number, in the state's own shapes ("24-72 (Colorado Open Records
    Act)", "Left out: 61.934", "JML 25-103", "No. 628"): the code, title and kind come from the nearest citation before
    it in the item. Used for the seed's own prose only, where a number is a record of what was read and set aside."""
    f, ccs, eo_num = _compiled(state)
    stat = [cc for cc in ccs if cc.code.kind == "statute" and cc.code.prefix != "(?!)"]
    spans = [(c.start, c.stop) for c in cites]
    free = lambda a, b: not any(a < y and x < b for x, y in spans)
    out = []
    by_ns = {}
    for cc in sorted(stat, key=lambda c: bool(re.search(r"\(\?P<q", c.code.prefix))):   # a code with no qualifier first
        by_ns.setdefault(ns_of(cc.code), cc)
    only = next(iter(by_ns.values())) if len(by_ns) == 1 else None

    def context(pos):
        prior = [c for c in cites if c.stop <= pos and c.kind == "statute"]
        if not prior:
            return only, None
        c = prior[-1]
        return by_ns.get(c.code), split_q(c.sec)[0]

    def take(cc, q, start, stop_to, level):
        toks, end = parse_list(text, start, cc, level, q or cc.code.q_default)
        if toks:
            for a, b in toks:
                out.append(Cite("statute", ns_of(cc.code), level, a, b, start, end))
            spans.append((start, end))
        return end
    q_rx = r"(?<![\w.\-§/])"
    seen = set()
    for pos_cc in stat:       # structured numbers, anywhere in the prose
        for m in re.finditer(q_rx + "(?:" + X(pos_cc.code.bare_sec or pos_cc.code.sec) + r")(?![\w\-]|\.\d)", text):
            cc, q = context(m.start())
            if cc is None or m.start() in seen or not free(m.start(), m.end()):
                continue
            tok = canon(m.group())
            if not re.search(r"[-.:]", tok) or len(re.sub(r"\D", "", tok)) < 4:
                continue
            if cc.code.q_is_chapter or (re.search(r"\(\?P<q", cc.code.prefix) and not (q or cc.code.q_default)):
                continue
            seen.add(m.start())
            take(cc, q, m.start(), None, "section")
        if pos_cc.chap and pos_cc.code.chap_bare:          # "24-72", "24-71.3": an article or chapter number
            for m in re.finditer(q_rx + "(?:" + X(pos_cc.code.chap) + r")(?![\w\-]|\.\d)", text):
                tok = canon(m.group())
                if m.start() in seen or not free(m.start(), m.end()) or not re.search(r"[-.]", tok) or pos_cc.code.q_is_chapter:
                    continue
                if len(re.sub(r"\D", "", tok)) < 3:
                    continue
                cc, q = context(m.start())
                if cc is None or ns_of(cc.code) != ns_of(pos_cc.code):
                    continue
                seen.add(m.start())
                take(cc, q, m.start(), None, "chapter")
    for cc in stat:           # "section 901" after "22 V.S.A.": a plain number the item's nearest title makes a section
        if not re.search(r"\(\?P<q", cc.code.prefix):
            continue
        for m in re.finditer(r"(?<![\w§])(?i:sections?|§§?)\s*(\d{1,5}[a-z]?)\b", text):
            c2, q = context(m.start())
            if c2 is None or ns_of(c2.code) != ns_of(cc.code) or not q or not free(m.start(), m.end()):
                continue
            if m.start(1) in seen:
                continue
            seen.add(m.start(1))
            out.append(Cite("statute", ns_of(cc.code), "section", f"{q}/{m.group(1)}", None, m.start(), m.end()))
            spans.append((m.start(), m.end()))
    for rx, fn in f.leftout_custom:    # "Chapter 15 Article 1C (Information Technology Management Act ...)"
        for m in re.finditer(rx, text):
            if free(m.start(), m.end()):
                for ns, level, tok in fn(m):
                    out.append(Cite("statute", ns, level, tok, None, m.start(), m.end()))
                spans.append((m.start(), m.end()))
    if f.leftout_plain_chapters:
        for cc in stat:       # "Statute chapters seen and left out: 205A (...), 239 (Public Records: not IT)"
            for m in re.finditer(r"(?<![\w.\-§/])(" + X(cc.code.chap or r"(?!)") + r")(?=\s*\()", text):
                if free(m.start(), m.end()) and re.search(r"(?i)\bchapters?\b", text[max(0, m.start() - 500):m.start()]):
                    out.append(Cite("statute", ns_of(cc.code), "chapter", canon(m.group(1)).upper(), None, m.start(), m.end()))
                    spans.append((m.start(), m.end()))
    if f.eo:                  # orders: "JML 25-103", "19-22", "01.01.2021.11", and "No. 628" where the state numbers plainly
        yr = re.compile(r"(?:19|20)\d\d-(?:19|20)\d\d")
        for m in eo_num.finditer(text):
            tok = m.group()
            if m.start() and re.match(r"[\w.\-§/]", text[m.start() - 1]) and not re.match(r"[A-Z]{1,3}\s", tok):
                continue
            if re.match(r"[\w\-]", text[m.end():m.end() + 1] or " ") or re.match(r"\.\d", text[m.end():m.end() + 2]):
                continue
            if not free(m.start(), m.end()) or yr.fullmatch(tok):
                continue
            structured = bool(re.search(r"[-.]", tok))
            if not structured:
                near = text[max(0, m.start() - 80):m.start()]
                if not (f.leftout_plain_orders and re.search(r"(?i)\bno\.?\s*$|(?:orders?|:|,)\s*$", near)
                        and re.match(r"\s*\(", text[m.end():m.end() + 3])):
                    continue
            for kind in f.eo_kinds:
                out.append(Cite("eo", kind, "section", norm_eo(tok), None, m.start(), m.end(), None, re.sub(r"\s+", "", tok)))
            spans.append((m.start(), m.end()))
    return out


def open_ended(text: str, c: Cite):
    """The upper end of "147-33.72 and following" or "1798.80 et seq.": the same article, any later section."""
    if c.kind == "eo" or c.level != "section" or c.end:
        return None
    if not re.match(r"\s*(?:,\s*)?(?:and\s+following\b|et\s+seq\b)", text[c.stop:c.stop + 30]):
        return None
    m = re.match(r"(.*[.\-])\d+[A-Za-z]?$", c.sec)
    return m.group(1) + "999999" if m and "." in c.sec.rsplit("/", 1)[-1] else None


def _excerpt(item: str, pos: int, stop: int, before: int = 300, after: int = 450) -> str:
    """The recorded reason around a citation in a left_out item: its bullet (or paragraph), narrowed to a window of
    about `before` characters before and `after` after the citation, cut at sentence ends. A verbatim substring."""
    bullet = re.compile(r"(?m)^\s*-\s")
    para = item.rfind("\n\n", 0, pos)
    lo = max([m.start() for m in bullet.finditer(item, 0, pos + 1)] + [para + 2 if para >= 0 else 0])
    ends = [m.start() for m in bullet.finditer(item, stop)]
    para_end = item.find("\n\n", stop)
    hi = min(ends + [para_end if para_end >= 0 else len(item)])
    a = max(lo, pos - before)
    if a > lo:
        k = item.rfind(". ", a, pos)
        sp = item.find(" ", a)
        a = k + 2 if k >= 0 else (sp + 1 if 0 <= sp < pos else a)
    b = min(hi, stop + after)
    if b < hi:
        k = item.find(". ", stop, b)
        sp = item.rfind(" ", stop, b)
        b = k + 1 if k >= 0 else (sp if sp > stop else b)
    return item[a:b].strip()


def load_seed(state: str, docs: dict | None = None) -> Seed:
    """Holdings of one state from its seed file. `docs` maps document id -> full text (for section headings)."""
    data = yaml.load((SOURCES / f"{state}.yml").read_text(encoding="utf-8"), Loader=YAML_LOADER)
    forms = FORMS[state]
    holdings, unparsed, n_watch, indexes = [], [], 0, []
    history_map, history_ids = {}, {}
    uncitable = [i for i, _ in forms.uncitable]
    for e in data.get("sources") or []:
        if e.get("watch_only"):
            n_watch += 1
            continue
        if e.get("doc_type") not in ("statute", "rule", "executive_order"):
            continue
        status = STUB if e.get("stub") else HELD
        cit = str(e.get("citation") or "")
        h = Holding(status, e["id"], cit, reason=str(e.get("stub_reason") or "").strip())
        cites = extract(state, cit)
        for rx, fn in forms.held_extra:
            for m in rx.finditer(cit):
                cites += [Cite(k, code, lvl, sec, end) for k, code, lvl, sec, end in fn(m)]
        # a seed citation is not prose: only the kind the entry declares counts
        want = {"statute": "statute", "rule": "rule", "executive_order": "eo"}[e["doc_type"]]
        cites = [c for c in cites if c.kind == want]
        for c in cites:
            add_cover(h, state, c)
        if not (h.chapters or h.sections or h.ranges or h.eos):
            if e["id"] in uncitable:
                continue
            (indexes if status == STUB and not re.search(r"\d", cit) else unparsed).append(e["id"])
            continue
        if status == HELD and docs and e["id"] in docs and want in ("statute", "rule"):
            for code_id, key in list(h.chapters):
                code = code_of(state, code_id)
                # "chapter 9, article 27" is a whole instrument where the code's unit is the article
                partial = any(not (code.unit_word and w.group().lower().startswith(code.unit_word[:3].lower()))
                              for w in PARTIAL_UNIT.finditer(cit))
                qual = split_q(key)[0]
                got = harvest_sections(state, code, qual, docs[e["id"]], key)
                h.harvested |= got
                if partial and got:
                    h.chapters.discard((code_id, key))
                    toks = sorted((t for _, t in got), key=sortkey)
                    h.ranges.append((code_id, toks[0], toks[-1]))
        if status == HELD and docs and e["id"] in docs:
            for ns, rx in forms.history_rx:
                for old, new in history_pairs(state, ns, rx, docs[e["id"]], h):
                    history_map.setdefault((ns, old), (ns, new))
                    history_ids.setdefault((ns, old), e["id"])
        holdings.append(h)
    for item in data.get("left_out") or []:
        text = str(item.get("text") or "")
        printed = extract(state, text)
        sect_chaps = {(c.code, chapter_of(code_of(state, c.code), c.sec)) for c in printed
                      if c.kind != "eo" and c.level == "section"}
        cites = sorted(printed + bare_cites(state, text, printed), key=lambda c: (c.start, -c.stop))
        cites = [dataclasses.replace(c, end=open_ended(text, c)) if open_ended(text, c) else c for c in cites]
        for c in cites:
            if c.kind != "eo" and c.level == "chapter" and (c.code, c.sec) in sect_chaps:
                continue    # "AS 44.21 sections left out: 44.21.010 ..." names sections, not the chapter
            h = Holding(LEFT_OUT, None, text[c.start:c.stop], reason=_excerpt(text, c.start, c.stop))
            add_cover(h, state, c)
            holdings.append(h)
    return Seed(state, holdings, unparsed, n_watch, indexes, uncitable, history_map, history_ids)


# ---- resolution --------------------------------------------------------------------------------------

@dataclass
class Resolution:
    cite: Cite
    status: str
    instrument: str
    kind: str
    chapter: str | None = None
    seed_ids: list = None
    reason: str = ""
    partial_ids: list = None
    key: str = ""             # identity of the instrument, for grouping citations of it


def display(state: str, code: Code, key: str, level: str) -> str:
    """Label of an instrument at the grain the corpus holds it."""
    q, rest = split_q(key)
    if code.grain == "law":
        return q or code.label
    if code.q_is_chapter:
        return f"{code.label} c. {q if '/' in key else key}" + (f", § {rest}" if level == "section" and "/" in key else "")
    head = f"{q} {code.label}" if q else code.label
    if level == "chapter" and code.kind == "statute":
        return f"{head} {code.unit_word or 'chapter'} {rest}"
    return f"{head} {rest}"


def _covers(h: Holding, code: Code, tok: str, forms: StateForms) -> bool:
    sk = sortkey(split_q(tok)[1])
    q = split_q(tok)[0]
    ch = chapter_of(code, tok)
    if ch is not None and (ns_of(code), ch) in h.chapters:
        return True
    if (ns_of(code), tok) in h.sections or (ns_of(code), tok) in h.harvested:
        return True
    for cid, lo, hi in h.ranges:
        if cid != ns_of(code):
            continue
        ql, lo_s = split_q(lo)
        if ql != q:
            continue
        if sortkey(lo_s) <= sk <= sortkey(split_q(hi)[1]):
            return True
    return False


def _touches(h: Holding, code: Code, chapter: str) -> bool:
    for cid, ch in h.chapters:
        if cid == ns_of(code) and ch == chapter:
            return True
    for cid, tok in list(h.sections) + list(h.harvested):
        if cid == ns_of(code) and chapter_of(code, tok) == chapter:
            return True
    for cid, lo, hi in h.ranges:
        if cid == ns_of(code) and chapter_of(code, lo) == chapter:
            return True
    return False


class Resolver:
    def __init__(self, state: str, seed: Seed):
        self.state, self.seed = state, seed
        self.forms = FORMS[state]
        self.renumbered = Counter()   # (old token, token now held) -> citations resolved through the renumbering
        self.history = Counter()      # the same, where the held documents' own history lines give the new number
        self.rolled = Counter()       # chapter citations resolved because the chapter is held section by section
        self.history_chapters = {}    # (namespace, old chapter) -> held document ids that took its sections
        for (ns, old), (_ns2, _new) in (seed.history_map or {}).items():
            ch = chapter_of(code_of(state, ns), old)
            if ch is not None:
                self.history_chapters.setdefault((ns, ch), set()).add(seed.history_ids[(ns, old)])

    def _tried(self, code: Code, tok: str, level: str):
        """Other numbers the same provision is known by: (code, token, level, where the corpus says so, counter)."""
        f, ns = self.forms, ns_of(code)
        if level == "section":
            new = f.renumber(ns, tok) if f.renumber else None
            if new:
                yield code, new, level, f.renumber_evidence, self.renumbered
            for mns, wrong, right, why in f.misprints:
                if (mns, wrong) == (ns, tok):
                    yield code, right, level, why, self.renumbered
            hit = (self.seed.history_map or {}).get((ns, tok))
            if hit:
                yield code_of(self.state, hit[0]), hit[1], level, (
                    f"the held {self.seed.history_ids[(ns, tok)]} prints it as its own history line"), self.history
        ch = tok if level == "chapter" else chapter_of(code, tok)
        for ans, old, now, why in f.aliases:
            if ans == ns and old == ch:
                yield code, now, "chapter", why, self.renumbered

    def _token(self, code: Code, tok: str, level: str) -> Resolution:
        for c2, new, lv2, why, counter in self._tried(code, tok, level):
            r = self._plain(c2, new, lv2)
            if r.status in (HELD, STUB):
                if r.status == HELD:
                    r.reason = why
                counter[(tok, new)] += 1
                return r
        if level == "chapter":
            ids = (self.history_chapters.get((ns_of(code), tok)) or set()) if ns_of(code) in self.forms.history_whole else set()
            if ids:
                self.history[(tok, "held under another chapter")] += 1
                return Resolution(None, HELD, display(self.state, code, tok, "chapter"), code.kind, tok, sorted(ids),
                                  "its sections are held under a new chapter number, and the held documents print the old one as history lines",
                                  None, f"{ns_of(code)}:{tok}")
        return self._plain(code, tok, level)

    def _plain(self, code: Code, tok: str, level: str) -> Resolution:
        best = None
        for status in (HELD, STUB, "ROLLUP", LEFT_OUT):
            if status == "ROLLUP":     # a chapter cited as a whole, where the corpus holds this code section by section
                hits = ([h for h in self.seed.holdings if h.status == HELD and _touches(h, code, tok)]
                        if level == "chapter" and code.grain == "section" else [])
                if hits:
                    self.rolled[tok] += 1
                    best = (HELD, hits)
                    break
                continue
            hits = [h for h in self.seed.holdings if h.status == status and self._holds(h, code, tok, level)]
            if hits:
                best = (status, hits)
                break
        ch = chapter_of(code, tok) if level == "section" else tok
        unit_level = "chapter" if (level == "chapter" or (code.grain != "section" and ch is not None)) else "section"
        key = ch if unit_level == "chapter" else tok
        label = display(self.state, code, key, unit_level)
        ident = f"{ns_of(code)}:{key}"
        if best:
            status, hits = best
            return Resolution(None, status, label, code.kind, ch, [h.seed_id for h in hits if h.seed_id],
                              hits[0].reason, None, ident)
        partial = []
        if ch is not None:
            partial = [h.seed_id for h in self.seed.holdings if h.status == HELD and h.seed_id and _touches(h, code, ch)]
        return Resolution(None, NOT_HELD, label, code.kind, ch, [], "", partial, ident)

    def _holds(self, h: Holding, code: Code, tok: str, level: str) -> bool:
        if level == "chapter":
            return (ns_of(code), tok) in h.chapters
        return _covers(h, code, tok, self.forms)

    def resolve(self, c: Cite) -> Resolution:
        if c.kind == "eo":
            word = {"EO": "Executive Order", "AO": "Administrative Order", "ED": "Executive Directive"}[c.code]
            label = f"{word} {c.raw or c.sec}" + (f" ({c.year})" if c.year else "")
            ident = f"{c.code}:{c.sec}" + (f"@{c.year}" if c.year and self.forms.eo_ambiguous else "")
            for status in (HELD, STUB, LEFT_OUT):
                hits = [h for h in self.seed.holdings if h.status == status and any(
                    code == c.code and num == c.sec and (not self.forms.eo_ambiguous or not c.year or not y or y == c.year)
                    for code, num, y in h.eos)]
                if hits:
                    return Resolution(c, status, label, "eo", None, [h.seed_id for h in hits if h.seed_id], hits[0].reason, None, ident)
            if self.forms.eo_glue and re.fullmatch(r"\d{3,}", c.sec):   # "No. 1171": order 117 and a footnote mark
                r = self.resolve(dataclasses.replace(c, sec=c.sec[:-1], raw=(c.raw or c.sec)[:-1]))
                if r.status == HELD:
                    r.cite = c
                    r.reason = "a footnote mark is run into the order number in the printed text"
                    return r
            return Resolution(c, NOT_HELD, label, "eo", None, [], "", [], ident)
        code = code_of(self.state, c.code)
        toks = [c.sec] + ([c.end] if c.end else [])
        rs = [self._token(code, t, c.level) for t in toks]
        r = max(rs, key=lambda x: WORSE[x.status])
        r.cite = c
        if (c.end and r.status != HELD and (code.grain == "section" or r.chapter is None)
                and rs[0].key != rs[-1].key and rs[0].status == rs[-1].status):
            r.instrument = f"{rs[0].instrument} to {split_q(c.end)[1]}"
            r.key = f"{rs[0].key}-{split_q(c.end)[1]}"
        return r


def resolve_text(state: str, text: str) -> list[Resolution]:
    """Extract and resolve every citation in `text` against `state`'s real seed file."""
    rv = Resolver(state, load_seed(state, load_texts()))
    return [rv.resolve(c) for c in extract(state, text)]


# ---- context and quotes ------------------------------------------------------------------------------

CUE = re.compile(r"(?i)\b(?:pursuant\s+to|under|authority|authorized\s+by|as\s+required\s+by|required\s+by|in\s+accordance\s+with|"
                 r"accordance\s+with|established\s+(?:by|in|under)|implement\w*|enabling|mandated\s+by|"
                 r"adopted\s+(?:under|pursuant)|promulgated|references?|applicab\w+|statutory)\b")
HEADING = re.compile(r"(?i)^\W*(?:\d+(?:\.\d+)*\.?\s*)?(?:statutory\s+|legal\s+|other\s+|compliance\s+|statutes?/other\s+)?"
                     r"(?:authority|authorities|references?|related\s+(?:documents?|policies|standards|laws|statutes|references|information)|"
                     r"applicability|statutes?\s+implemented|law\s+implemented|legal\s+basis)\b[^.]{0,40}$")
NUMBERED_HEADING = re.compile(r"^\W*\d+(?:\.\d+)*\.?\s+[A-Z][A-Za-z ,&/-]{2,50}$")
BRACKET_OPEN = re.compile(r"\[\s*(?:Source:?\s*)?$")
SENTENCE_END = re.compile(r"[.!?][\"')\]]*\s+(?=[A-Z(\[\d\"\u201c])|\n\s*\n")


def in_authority_context(text: str, pos: int) -> bool:
    """True when the citation at `pos` sits where a document says what enables it (a line or heading such as
    Authority, Reference, Applicability, or a phrase such as "pursuant to", "under", "as required by")."""
    back = text[max(0, pos - 300):pos]
    ends = list(SENTENCE_END.finditer(back))
    seg = back[ends[-1].end():] if ends else back
    if CUE.search(seg):
        return True
    ls = text.rfind("\n", 0, pos) + 1
    if HEADING.match(text[ls:pos].strip() or "x") and len(text[ls:pos].strip()) < 60 and CUE.search(text[ls:pos]):
        return True
    if BRACKET_OPEN.search(text[ls:pos]):      # "[Neb. Rev. Stat. § 81-1120.27(1)]": a source note in brackets
        return True
    lines = [ln for ln in text[max(0, ls - 3000):ls].split("\n") if ln.strip()]
    for ln in reversed(lines[-40:]):            # a reference block runs to a heading or to prose, however long the list
        s = ln.strip()
        if HEADING.match(s):
            return True
        if len(s.split()) >= 22 or NUMBERED_HEADING.match(s):
            return False
    return False


HISTORY_BEFORE = re.compile(r"(?i)\b(?:formerly|former|renumbered(?:\s+from)?|recodified(?:\s+from)?|repealed(?:\s+by)?|"
                            r"redesignated\s+from|derived\s+from|supersed\w+|rescission\s+of|rescinded\s+by)\W{0,3}(?:[A-Za-z.]+\s+){0,2}$")
SESSION_LAW_BEFORE = re.compile(r"(?:\b(?:19|20)\d\d,?\s+(?:cc?\.|ch\.|c)\s*\d+[\w,;.\s]{0,40}\(?|\bCode\s+(?:19|20)\d\d,?\s*)$")
HISTORY_LINE = re.compile(r"(?i)^\s*\W*(?:history|source|derived\s+from|formerly)\b")
RULE_HISTORY_LINE = re.compile(r"^\s*\[\s*\d[\d.]*\s+[A-Z]+\s*-")   # "[1.12.1.1 NMAC - Rp/E, 1 NMAC 12.1.1, 12/02/2005]"


def is_history_reference(doc_type: str, text: str, pos: int) -> bool:
    """A citation that names an instrument in a history note ("Formerly RCW 42.17.31922", "1976, c. 597, § 2.1-377",
    a statute's own "Source:" line): the number is old, or a session law's, not a pointer to what enables the text."""
    ls = text.rfind("\n", 0, pos) + 1
    before = text[ls:pos]
    if HISTORY_BEFORE.search(before[-60:]) or SESSION_LAW_BEFORE.search(before[-90:]):
        return True
    le = text.find("\n", pos)
    if RULE_HISTORY_LINE.match(text[ls:len(text) if le < 0 else le]):
        return True
    return doc_type == "statute" and bool(HISTORY_LINE.match(text[ls:pos + 1]))


def quote(text: str, pos: int) -> str:
    """The line holding `pos`, verbatim, clipped around the citation to at most 40 words. A line of fewer
    than six words takes the line before it."""
    ls = text.rfind("\n", 0, pos) + 1
    le = text.find("\n", pos)
    le = len(text) if le < 0 else le
    line = text[ls:le]
    if len(line.split()) < 6 and ls > 0:
        ps = text.rfind("\n", 0, ls - 1) + 1
        if text[ps:ls - 1].strip():
            line = text[ps:le]
            ls = ps
    toks = list(re.finditer(r"\S+", line))
    if len(toks) <= QUOTE_WORDS:
        return line.strip()
    i = next((k for k, t in enumerate(toks) if t.end() > pos - ls), 0)
    lo = max(0, min(i - 12, len(toks) - QUOTE_WORDS))
    return line[toks[lo].start():toks[lo + QUOTE_WORDS - 1].end()]


# ---- documents ---------------------------------------------------------------------------------------

@dataclass
class Doc:
    id: str
    state: str
    doc_type: str
    text: str
    issuing_body: str = ""
    citation: str = ""
    title: str = ""


def load_docs() -> list[Doc]:
    out = []
    for folder in CONTENT:
        for path in sorted((ROOT / folder).rglob("*.md")):
            raw = path.read_text(encoding="utf-8")
            end = raw.find("\n---", 4)
            fm = yaml.load(raw[4:end], Loader=YAML_LOADER) if raw.startswith("---\n") and end > 0 else {}
            body = raw[end + 4:] if end > 0 else raw
            i = body.find("## Full text")
            body = body[i + len("## Full text"):] if i >= 0 else body
            j = body.find("\n## Curator notes")
            body = body[:j] if j >= 0 else body
            out.append(Doc(str(fm["id"]), str(fm["jurisdiction"]), str(fm["doc_type"]), body,
                           str(fm.get("issuing_body") or ""), str(fm.get("citation") or ""), str(fm.get("title") or "")))
    return out


_DOCS_CACHE: list | None = None


def docs() -> list[Doc]:
    global _DOCS_CACHE
    if _DOCS_CACHE is None:
        _DOCS_CACHE = load_docs()
    return _DOCS_CACHE


def load_texts() -> dict:
    return {d.id: d.text for d in docs()}


# ---- audit: how many probable citations did the table read? ------------------------------------------

def audit_text(state: str, text: str, cites: list[Cite], masked: str | None = None, ignored=()) -> list[int]:
    """Positions where this state's code name is followed by a number and no extracted citation starts there or
    spans it: the places the table may be failing."""
    f, ccs, _ = _compiled(state)
    t = masked if masked is not None else prepare(text)
    spans = [(c.start, c.stop) for c in cites] + list(ignored)
    ignore = re.compile(f.audit_ignore) if f.audit_ignore else None

    def skipped(pos):
        if not ignore:
            return False
        ls = t.rfind("\n", 0, pos) + 1
        le = t.find("\n", pos)
        return bool(ignore.search(t[ls:len(t) if le < 0 else le]))
    miss, probable = [], 0
    anchored = set()      # where each prefix anchor's number begins
    for cc in ccs:
        for m in cc.anchor.finditer(t):
            anchored.add(m.end())
            if skipped(m.start()):
                continue
            probable += 1
            if not any(a <= m.start() < b for a, b in spans):
                miss.append(m.start())
    # a statute number after a section sign or the word "section", whether or not a code name precedes it: this
    # anchor does not use the forms it audits, so a form the table cannot read at all still shows as missed
    for cc in ccs:
        code = cc.code
        if code.kind != "statute" or code.prefix == "(?!)":
            continue
        shape = code.bare_sec or code.sec
        for m in re.finditer(r"(?<![\w§])(?:§§?|(?i:sections?|secs?\.|ss?\.))\s*(?P<n>" + X(shape) + r")(?![\d\w])", t):
            pos = m.start("n")
            if pos in anchored or not re.search(r"[-.:]", m.group("n")) or len(re.sub(r"\D", "", m.group("n"))) < 3:
                continue
            if any(o.suffix_name and o.suffix_name.search(t[pos:pos + 60]) for o in ccs):
                continue
            if skipped(pos):
                continue
            anchored.add(pos)
            probable += 1
            if not any(a <= pos < b for a, b in spans):
                miss.append(pos)
    for cc in ccs:
        if cc.code.suffix and cc.suffix_name.search(t):
            for m in cc.suffix_anchor.finditer(t):
                pos = m.start("n")
                if skipped(pos):
                    continue
                probable += 1
                if not any(a <= pos < b + 10 for a, b in spans):
                    miss.append(pos)
    if f.eo:
        rx = re.compile(EO_HEAD.pattern + r"(?=[A-Z]{0,3}[-\s]?\d)")
        for m in rx.finditer(t):
            if _eo_kind(m.group("kind")) not in f.eo_kinds:
                continue
            probable += 1
            if not any(a <= m.start() < b for a, b in spans):
                miss.append(m.start())
    return [probable] + sorted(set(miss))


# ---- the report --------------------------------------------------------------------------------------

STATUS_KEY = {NOT_HELD: "not_held", STUB: "stub", LEFT_OUT: "left_out", HELD: "held"}


class Agg:
    def __init__(self, r: Resolution):
        self.r = r
        self.labels = Counter()
        self.authority_docs = set()
        self.docs, self.sections, self.bodies = set(), set(), set()
        self.total = self.auth = self.cross = self.passing = 0
        self.quotes = []     # (rank, document, authority, text)


def _merge(dst: Agg, src: Agg) -> None:
    dst.labels.update(src.labels)
    dst.authority_docs |= src.authority_docs
    dst.docs |= src.docs
    dst.sections |= src.sections
    dst.bodies |= src.bodies
    dst.total += src.total
    dst.auth += src.auth
    dst.cross += src.cross
    dst.passing += src.passing
    dst.quotes += src.quotes


def merge_same_instrument(state: str, aggs: dict) -> None:
    """One instrument must be one row: a section named inside a range the same state cites ("16-4-203" beside
    "16-4-201 to 16-4-205"), and an order cited both with and without its year, are merged into the longer citation."""
    for key in list(aggs):
        status, kind, ident = key
        if key not in aggs:
            continue
        g = aggs[key]
        c = g.r.cite
        if kind == "eo":
            if "@" in ident:
                continue
            years = [k for k in aggs if k[0] == status and k[1] == "eo" and k[2].startswith(ident + "@")]
            if len(years) == 1:
                _merge(aggs[years[0]], aggs.pop(key))
        elif c is not None and c.end and c.level == "section":
            code = code_of(state, c.code)
            ch = chapter_of(code, c.sec)
            if ch is None or ch != chapter_of(code, c.end):    # only a range inside one chapter names one instrument
                continue
            q = split_q(c.sec)[0]
            lo, hi = sortkey(split_q(c.sec)[1]), sortkey(split_q(c.end)[1])
            for k2 in list(aggs):
                g2 = aggs.get(k2)
                if k2 == key or g2 is None or k2[0] != status or k2[1] != "statute" or g2.r.cite is None:
                    continue
                c2 = g2.r.cite
                if c2.code != c.code or c2.end or c2.level != "section" or split_q(c2.sec)[0] != q:
                    continue
                if chapter_of(code, c2.sec) == ch and lo <= sortkey(split_q(c2.sec)[1]) <= hi:
                    _merge(g, aggs.pop(k2))


def _self_range(state: str, c: Cite, own: list) -> bool:
    """True when a statute cites a range that contains the statute's own section (its definitions clause)."""
    if c.level != "section":
        return False
    for o in own:
        if o.kind == "statute" and o.level == "section" and o.code == c.code and split_q(o.sec)[0] == split_q(c.sec)[0]:
            if sortkey(split_q(c.sec)[1]) <= sortkey(split_q(o.sec)[1]) <= sortkey(split_q(c.end)[1]):
                return True
    return False


def build_report() -> dict:
    all_docs = docs()
    by_state = defaultdict(list)
    for d in all_docs:
        by_state[d.state].append(d)
    texts = {d.id: d.text for d in all_docs}
    states = {}
    for state in sorted(FORMS):
        forms = FORMS[state]
        seed = load_seed(state, texts)
        rv = Resolver(state, seed)
        aggs: dict = {}
        counts = {k: Counter() for k in ("statute", "rule", "eo")}
        pairs = {k: defaultdict(set) for k in ("statute", "rule", "eo")}
        citing = set()
        instruments = defaultdict(set)      # status -> {(kind, instrument key)}: distinct instruments cited
        federal = Counter()
        probable = missed = history = self_ranges = 0
        missed_lines = []
        for d in by_state[state]:
            masked = prepare(d.text)
            cites, ignored = extract_ignoring(state, d.text, masked)
            federal.update(count_federal(d.text))
            a = audit_text(state, d.text, cites, masked, ignored)
            probable += a[0]
            missed += len(a) - 1
            for pos in a[1:]:
                if len(missed_lines) < 5:
                    missed_lines.append({"document": d.id, "text": quote(d.text, pos)})
            if cites:
                citing.add(d.id)
            own = extract(state, d.citation) if d.doc_type == "statute" and d.citation else []
            for c in cites:
                if is_history_reference(d.doc_type, d.text, c.start):
                    history += 1
                    continue
                if c.end and c.kind != "eo" and _self_range(state, c, own):
                    self_ranges += 1      # "As used in K.S.A. 75-7201 through 75-7212": the statute's own range
                    continue
                r = rv.resolve(c)
                instruments[r.status].add((r.kind, r.key))
                counts[r.kind][r.status] += 1
                pairs[r.kind][r.status].add((d.id, r.instrument))
                if r.status == HELD:
                    continue
                key = (r.status, r.kind, r.key)
                g = aggs.get(key)
                if g is None:
                    g = aggs[key] = Agg(r)
                auth = in_authority_context(d.text, c.start)
                from_statute = d.doc_type == "statute"
                g.docs.add(d.id)
                if d.issuing_body:
                    g.bodies.add(d.issuing_body)
                g.labels[r.instrument] += 1
                g.total += 1
                if from_statute:
                    g.cross += 1
                elif auth:
                    g.auth += 1
                    g.authority_docs.add(d.id)
                else:
                    g.passing += 1
                if c.kind != "eo" and c.level == "section":
                    g.sections.add(c.sec + (f"-{split_q(c.end)[1]}" if c.end else ""))
                g.quotes.append((from_statute, not auth, d.id, auth, quote(d.text, c.start)))
        merge_same_instrument(state, aggs)
        st = {
            "documents": len(by_state[state]),
            "documents_citing_state_instruments": len(citing),
            "forms": [{"form": c.label or c.id, "kind": c.kind,
                       "grain": ("the named law" if c.grain == "law" else "section or section range" if c.grain == "section"
                                 else (c.unit_word or "chapter") if c.kind == "statute" else "rule chapter")}
                      for c in forms.codes if not c.custom and c.prefix != "(?!)" and not c.ns]
                     + (([{"form": "Executive Order" + ("/Administrative Order" if "AO" in forms.eo_kinds else "")
                           + ("/Executive Directive" if "ED" in forms.eo_kinds else ""), "kind": "eo", "grain": "order number"}])
                        if forms.eo else []),
            "citations": {k: {STATUS_KEY[s]: counts[k][s] for s in (HELD, STUB, LEFT_OUT, NOT_HELD)} for k in counts},
            "distinct_instruments": {"cited": len(set().union(*instruments.values())) if instruments else 0,
                                     **{STATUS_KEY[k]: len(instruments[k]) for k in (HELD, STUB, LEFT_OUT, NOT_HELD)}},
            "document_instrument_pairs": {k: {STATUS_KEY[s]: len(pairs[k][s]) for s in (HELD, STUB, LEFT_OUT, NOT_HELD)} for k in pairs},
            "federal_citations": dict(sorted(federal.items())),
            "history_note_citations_excluded": history,
            "self_range_citations_excluded": self_ranges,
            "renumbered_citations": {"resolved": sum(rv.renumbered.values()),
                                     "evidence": forms.renumber_evidence} if rv.renumbered else {},
            "history_renumbered_citations": ({"resolved": sum(rv.history.values()),
                                              "evidence": "the held documents print the old number as a history line"}
                                             if rv.history else {}),
            "rolled_up_chapter_citations": sum(rv.rolled.values()),
            "extraction": {
                "probable_citations": probable,
                "read": probable - missed,
                "missed": missed,
                "share_read": round((probable - missed) / probable, 3) if probable else 1.0,
                "unreliable_kinds": list(forms.unreliable),
                "notes": forms.notes,
                "missed_examples": missed_lines,
            },
            "seed": {
                "held_instruments_with_a_citable_form": sum(1 for h in seed.holdings if h.status == HELD),
                "stub_instruments_with_a_citable_form": sum(1 for h in seed.holdings if h.status == STUB),
                "watch_only_entries": seed.n_watch,
                "index_stubs": sorted(seed.indexes),
                "uncitable": [{"id": i, "why": w} for i, w in forms.uncitable],
                "unparsed": sorted(seed.unparsed),
            },
        }
        for status, bucket in ((NOT_HELD, "not_held"), (STUB, "stub"), (LEFT_OUT, "left_out"), (NOT_HELD, "not_held_unverified")):
            items = []
            for (s, kind, _key), g in aggs.items():
                if s != status or (kind in forms.unreliable) != (bucket == "not_held_unverified"):
                    continue
                inst = sorted(g.labels.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
                qs, seen_q, seen_d = [], set(), set()
                for from_statute, passing, did, auth, text in sorted(g.quotes, key=lambda x: (x[0], x[1], x[2])):
                    if text in seen_q or (did in seen_d and len(qs) < len(seen_d)):
                        continue
                    seen_q.add(text)
                    seen_d.add(did)
                    qs.append({"document": did, "authority_context": auth, "text": text})
                    if len(qs) == 3:
                        break
                item = {
                    "instrument": inst, "kind": kind, "code": g.r.cite.code, "chapter": g.r.chapter,
                    "citing_documents": sorted(g.docs),
                    "citing_issuing_bodies": sorted(g.bodies)[:6],
                    "citations": g.total,
                    "authority_context_documents": len(g.authority_docs),
                    "authority_context_citations": g.auth,
                    "statute_cross_references": g.cross,
                    "passing_citations": g.passing,
                    "sections_cited": sorted(g.sections, key=lambda t: sortkey(split_q(t)[1]))[:12],
                    "quotes": qs,
                }
                if status == NOT_HELD and g.r.partial_ids:
                    item["held_in_same_chapter"] = sorted(set(g.r.partial_ids))
                if status == STUB:
                    item["seed_ids"] = sorted(set(g.r.seed_ids))
                if status in (STUB, LEFT_OUT):
                    item["reason"] = g.r.reason
                items.append(item)
            items.sort(key=lambda i: (-i["authority_context_documents"], -len(i["citing_documents"]),
                                      -i["authority_context_citations"], i["instrument"]))
            st[bucket] = items
        states[state] = st
    totals = {"states": len(states), "documents": sum(s["documents"] for s in states.values())}
    for k in ("statute", "rule", "eo"):
        totals[k] = {b: sum(s["citations"][k][b] for s in states.values()) for b in ("held", "stub", "left_out", "not_held")}
    for b in ("not_held", "not_held_unverified", "stub", "left_out"):
        totals[f"{b}_instruments"] = sum(len(s[b]) for s in states.values())
    return {
        "about": ("Citations in the held documents to their own state's statutes, administrative rules and executive "
                  "orders, resolved against each state's seed file. Generated by src/authority_refs.py; read-only. "
                  "not_held lists are CANDIDATES for the owner to judge, not approved seed entries."),
        "unverified": ("not_held_unverified lists instruments of a kind whose extraction the audit found unreliable for that "
                       "state (see extraction.notes); they are not candidates until a person reads the quotes."),
        "resolution": {"held": "a document's own citation or section range covers it", "stub": "a seed entry with stub: true",
                       "left_out": "named in the state's left_out record (reason kept)",
                       "not_held": "none of the above"},
        "totals": totals,
        "states": states,
    }


def render(report: dict) -> str:
    return json.dumps(report, ensure_ascii=False, indent=1, sort_keys=False) + "\n"


def check(path: Path = OUT) -> bool:
    if not path.exists():
        print(f"{path} is missing -- run: python3 src/authority_refs.py")
        return False
    if path.read_text(encoding="utf-8") != render(build_report()):
        print(f"{path} is stale -- run: python3 src/authority_refs.py")
        return False
    print(f"{path.relative_to(ROOT) if path.is_relative_to(ROOT) else path} is current.")
    return True


def table(report: dict, only: str | None = None) -> str:
    head = f"{'state':15} {'docs':>5} {'citing':>6} {'read%':>6}  {'statute H/S/L/N':>16} {'rule H/S/L/N':>14} {'order H/S/L/N':>14}  {'cand':>4} {'auth':>5}"
    rows = [head]
    for name, st in report["states"].items():
        if only and name != only:
            continue
        c = st["citations"]
        f = lambda k: "/".join(str(c[k][b]) for b in ("held", "stub", "left_out", "not_held"))
        auth = sum(i["authority_context_citations"] for i in st["not_held"])
        rows.append(f"{name:15} {st['documents']:5d} {st['documents_citing_state_instruments']:6d} "
                    f"{st['extraction']['share_read'] * 100:6.1f}  {f('statute'):>16} {f('rule'):>14} {f('eo'):>14}  "
                    f"{len(st['not_held']):4d} {auth:5d}")
    return "\n".join(rows)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="exit 1 if the committed JSON is stale")
    ap.add_argument("--table", action="store_true", help="print the per-state table")
    ap.add_argument("--state", help="with --table: one state")
    args = ap.parse_args(argv)
    if args.check:
        return 0 if check() else 1
    report = build_report()
    if args.table:
        print(table(report, args.state))
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(report), encoding="utf-8")
    t = report["totals"]
    print(f"wrote {OUT.relative_to(ROOT)}: {t['states']} states, {t['documents']} documents, "
          f"{t['not_held_instruments']} not-held, {t['stub_instruments']} stub, {t['left_out_instruments']} left-out instruments")
    return 0


if __name__ == "__main__":
    sys.exit(main())
