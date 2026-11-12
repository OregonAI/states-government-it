"""Minnesota: the Revisor of Statutes' full-chapter pages for statutes (revisor.mn.gov/statutes/cite/<chapter>/full)
and rules (revisor.mn.gov/rules/<chapter>/full), and the identity of statute pages. Hooks are described in
src/states/__init__.py. MNIT's policies and standards and the executive orders are PDFs, which the shared
reader handles."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line, _decode, _squash

_BLOCK = re.compile(r"<(?:/?)(?:div|p|h[1-6]|li|ul|ol|tr|table|section|article|br)\b[^>]*>", re.I)
_END = "Official Publication of the State of Minnesota"


def _lines(fragment: str) -> list[str]:
    fragment = re.sub(r"<!--.*?-->", "", fragment, flags=re.S)
    fragment = re.sub(r"<(script|style|svg|noscript)\b.*?</\1>", "", fragment, flags=re.S | re.I)
    fragment = _BLOCK.sub("\n", fragment)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    return [c for c in (_clean_line(l) for l in fragment.split("\n")) if c]


def revisor_html_to_text(raw: bytes) -> str:
    """A Revisor full-chapter page, statute or rule. Only the `xtend` region is the law: the legislature's menus,
    the resource box, the footer and the 'Official Publication' line are not, nor is the table of sections (or of
    parts) that precedes the text and repeats its headings. Output: the chapter heading (and, for a rule, its
    agency), then each section (part) with a blank line before it: its heading, each subdivision's number and
    headnote on one line, one line per paragraph, the history line. A repealed section or part is kept as the
    page prints it. Nothing inside a section is dropped; the permalink marks (§) are."""
    page = _decode(raw)
    start = page.find('id="xtend"')
    end = page.find(_END, start)
    if start < 0 or end < 0:
        raise ValueError("Revisor page has no xtend text region: the page layout changed")
    region = page[page.index(">", start) + 1:end]
    region = re.sub(r'<div id="chapter_analysis">.*?</table>\s*</div>', "", region, flags=re.S)
    region = re.sub(r'<a [^>]*class="permalink"[^>]*>.*?</a>', "", region, flags=re.S)
    region = re.sub(r'<span class="headnote">', " ", region)
    region = re.sub(r'</h2>\s*<h2 class="headnote">', " ", region)
    region = re.sub(r'<(div class="(?:section|sr|sr_by_subd|part)"|h1 class="fgh")',
                    lambda m: "<p>\x00</p>" + m.group(0), region)       # a blank line before each section, part and group heading
    out: list[str] = []
    gap = False
    for line in _lines(region):
        if line == "\x00":
            gap = True
            continue
        if gap and out:
            out.append("")
        gap = False
        out.append(line)
    if not out:
        raise ValueError("Revisor page has no text in its xtend region")
    return "\n".join(out) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type in ("statute", "rule"):
        return revisor_html_to_text(raw)
    return None


_BODY_START = re.compile(r"^\s*(?:Purpose|Policy Statement|Standard Statement)\b")


def _title_block(text: str) -> str:
    """The lines a MNIT policy or standard prints before its body ('Purpose', 'Policy Statement' or 'Standard
    Statement'), at most 15. Each line is cut at its first run of two or more spaces, so the left column alone is
    read: the Supply Chain Risk Management Policy prints its title in that column on lines 1 and 3, beside
    'Date Issued' and 'Authority', with a right-column line (indented) between them."""
    block = []
    for line in text.splitlines()[:15]:
        if _BODY_START.match(line):
            break
        if line[:1].isspace():      # a right-column line (the policy's 'Revised Date') has no left column
            continue
        block.append(re.split(r"\s{2,}", line.rstrip())[0])
    return " ".join(block)


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "minnesota":
        return False
    if src["doc_type"] in ("policy", "standard"):
        # MNIT documents name each other in their Related Information lists, so the phrase must be in the title block
        phrase = src.get("identity_text") or src["title"]
        if _squash(phrase) not in _squash(_title_block(text)):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {phrase!r} is not in its title block")
        return True
    if src["doc_type"] != "statute":
        return False
    ch = re.search(r"\bch\.\s*(\w+)", src["citation"])
    first = text.strip().splitlines()[0] if text.strip() else ""
    if not ch or not re.match(rf"CHAPTER {re.escape(ch.group(1))}\. ", first):
        raise ValueError(f"{src['id']}: page is not {src['citation']} (it opens {first[:60]!r})")
    return True


def notes(src, fmt, text):
    if fmt != "html":
        return None
    what = "chapter of Minnesota Statutes" if src["doc_type"] == "statute" else "chapter of Minnesota Rules"
    return (f"Text taken from the Revisor of Statutes' full-chapter page (www.revisor.mn.gov), the official publication "
            f"of the State of Minnesota: the {what}'s heading, then each {'section' if src['doc_type'] == 'statute' else 'part'} "
            f"with its subdivisions, one line per paragraph, and the history line. Repealed and expired "
            f"{'sections' if src['doc_type'] == 'statute' else 'parts'} appear as the page prints them. The legislature's "
            f"menus, the resource box, the footer and the Table of Sections (Table of Parts for a rule), which repeats "
            f"the headings, were removed, as were the links' targets. The page prints no effective date for the chapter.")
