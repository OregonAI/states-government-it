"""Per-state citation forms for src/authority_refs.py.

One entry per state in _meta/sources/. Each form was derived by READING that state's documents
(statutes cite themselves and one another, rules print "Authority:" lines, policies say "pursuant to"):
what a state's documents print is the table, not what the state's code is officially abbreviated.

A `Code` is one statute code or one rule code of one state: how its citations begin (`prefix`), what a
section looks like (`sec`), what a chapter looks like (`chap`), how to find the instrument (chapter, article,
rule chapter) a section belongs to (`chapter`), and at what grain this corpus holds it (`grain`).

Regex notes: `~` stands for "a dash, then optional layout whitespace" (PDF text breaks "125-800-" / "0020"
across lines); a prefix may carry one named group, `q`, a qualifier (a title or chapter number printed
before the code name) that becomes part of the token as "q/sec".
"""
from __future__ import annotations

import dataclasses
import re
from dataclasses import dataclass, field
from typing import Callable, Optional


@dataclass(frozen=True)
class Code:
    id: str                      # token namespace within the state ("Gov", "ORS")
    kind: str                    # "statute" | "rule"
    prefix: str                  # regex that opens a citation
    sec: str                     # regex of one section token
    label: str = ""              # display name ("ORS"); defaults to id
    chap: Optional[str] = None   # regex of a chapter-level token ("279A")
    chap_bare: bool = False      # "AS 36.30" with no "chapter" word is a chapter-level citation
    suffix: Optional[str] = None  # regex naming the code after the list: "section 24-37.5-105, C.R.S."
    bare: bool = False           # "§ 2.2-2009" alone is this code (the section shape is distinctive)
    chapter: Optional[Callable[[str], Optional[str]]] = None  # section -> instrument it belongs to
    grain: str = "chapter"       # "chapter": the corpus holds whole chapters; "section": sections or ranges;
    #                              "law": a whole named law is the unit (candidate = the law)
    short: Optional[str] = None  # list items may omit the part up to this char ("R.S. 39:199, 200")
    q_default: Optional[str] = None  # qualifier assumed when the text omits it (and why, in the state's notes)
    q_is_chapter: bool = False   # the qualifier is itself the chapter ("M.G.L. c. 66A, § 1")
    unit_word: str = ""          # "chapter", "article": printed before the key of a chapter-grain candidate
    ns: Optional[str] = None     # token namespace when two forms of one code share holdings (defaults to id)
    q_join: Optional[str] = None  # prefix carries "Title 24 Article 37.5": chapter key = q + q_join + token
    whole: Optional[str] = None  # regex ending a held token that denotes the whole unit ("3.00" in "801 CMR 3.00")
    custom: Optional[tuple] = None  # (regex, fn(match) -> [(level, token)]) for a printed form the list grammar cannot read
    sfx_bare: bool = False       # a section number straight before the code name is a citation ("2-17-505, MCA")
    qnorm: Optional[Callable[[str], str]] = None  # canonical form of the qualifier ("Technology Law" -> "State Technology Law")


@dataclass(frozen=True)
class StateForms:
    codes: tuple
    eo: bool = True              # executive orders are cited by number
    eo_kinds: tuple = ("EO",)    # "EO", plus "AO" (administrative order) or "ED" (executive directive)
    eo_num: Optional[str] = None   # regex override for an order number
    eo_ambiguous: bool = False   # numbering restarts with each governor; matched on number and year when printed
    held_extra: tuple = ()       # (regex over a seed citation, fn(match) -> list of (kind, code, level, sec, end))
    notes: str = ""              # what this state's table cannot do, in words
    uncitable: tuple = ()        # ((seed id, why), ...): held instruments no later document can cite by form
    renumber: Optional[Callable[[str, str], Optional[str]]] = None   # (namespace, old token) -> token now held
    renumber_evidence: str = ""  # where the corpus itself records that renumbering
    audit_ignore: Optional[str] = None   # lines that look like a citation to the audit and are page furniture
    unreliable: tuple = ()       # kinds ("statute", "rule", "eo") whose extraction the audit shows cannot be trusted


# ---- chapter functions -------------------------------------------------------------------------------

def dot0(s):          # "276A.300" -> "276A"
    return s.split(".")[0]


def dash_n(n):        # "24-37.5-105" -> first n dash groups
    def f(s):
        parts = re.split(r"[-]", s)
        return "-".join(parts[:n]) if len(parts) >= n else None
    return f


def colon0(s):        # "39:15.1" -> "39"
    return s.split(":")[0] if ":" in s else None


def dot_n(n):
    def f(s):
        parts = s.split(".")
        return ".".join(parts[:n]) if len(parts) >= n else None
    return f


def digits_article(s):   # K.S.A. 75-4701 -> "75-47" (chapter, article = all but the last two digits)
    m = re.match(r"(\d+)-(\d+)", s)
    if not m:
        return None
    n = m.group(2)
    return f"{m.group(1)}-{n[:-2] or n}"


def none(_s):
    return None


# ---- shared regex pieces -----------------------------------------------------------------------------

NUM_DASH = r"(?:[A-Z]{1,3}[-\s]?)?\d{1,4}(?:~\d{1,4}){0,3}[A-Z]?"


def S(*codes, **kw):
    return StateForms(codes=tuple(codes), **kw)


def C(id, kind, prefix, sec, **kw):
    return Code(id=id, kind=kind, prefix=prefix, sec=sec, **kw)


FORMS: dict[str, StateForms] = {}

FORMS["alaska"] = S(
    C("AS", "statute", r"AS|Alaska\s+Statutes?", r"\d{1,2}\.\d{2}\.\d{3}(?:\.\d+)?", label="AS",
      chap=r"\d{1,2}\.\d{2}", chap_bare=True, chapter=dot_n(2), grain="section"),
    C("AAC", "rule", r"(?P<q>\d{1,2})\s+AAC", r"\d{2}\.\d{3}(?:\.\d+)?", label="AAC",
      chap=r"\d{2}", chapter=dot0, grain="section"),
    eo_kinds=("EO", "AO"),
)
FORMS["arizona"] = S(
    C("ARS", "statute", r"A\.R\.S\.|ARS|Arizona\s+Revised\s+Statutes", r"\d{1,2}~\d{3,4}(?:\.\d{2})?",
      label="A.R.S.", chap=r"\d{1,2}", chapter=dash_n(1), grain="section"),
    C("AAC", "rule", r"A\.A\.C\.|Arizona\s+Administrative\s+Code", r"R\d{1,2}~\d{1,2}(?:~\d{3,4})?",
      label="A.A.C.", chapter=dash_n(2)),
)
_CA_SEC = r"\d{1,5}(?:\.\d{1,3}){0,2}"
FORMS["california"] = S(
    C("Gov", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Gov(?:ernment|\.|'t)?\s+Code,?", _CA_SEC,
      label="Gov. Code", suffix=r"Gov(?:ernment|\.|'t)?\s+Code", grain="section"),
    C("Civ", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Civ(?:il|\.)\s+Code,?", _CA_SEC,
      label="Civ. Code", suffix=r"Civ(?:il|\.)\s+Code", grain="section"),
    C("PCC", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Pub(?:lic|\.)\s+Contract\s+Code,?", _CA_SEC,
      label="Pub. Contract Code", suffix=r"Pub(?:lic|\.)\s+Contract\s+Code", grain="section"),
    C("Pen", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Pen(?:al|\.)\s+Code,?", _CA_SEC,
      label="Penal Code", suffix=r"Pen(?:al|\.)\s+Code", grain="section"),
    C("Edu", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Ed(?:ucation|uc\.)\s+Code,?", _CA_SEC,
      label="Educ. Code", suffix=r"Ed(?:ucation|uc\.)\s+Code", grain="section"),
    C("HSC", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Health\s+(?:and|&)\s+Safety\s+Code,?", _CA_SEC,
      label="Health & Safety Code", suffix=r"Health\s+(?:and|&)\s+Safety\s+Code", grain="section"),
    C("WIC", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Welf(?:are|\.)\s+(?:and|&)\s+Inst(?:itutions|\.)\s+Code,?", _CA_SEC,
      label="Welf. & Inst. Code", suffix=r"Welf(?:are|\.)\s+(?:and|&)\s+Inst(?:itutions|\.)\s+Code", grain="section"),
    C("BPC", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Bus(?:iness|\.)\s+(?:and|&)\s+Prof(?:essions|\.)\s+Code,?", _CA_SEC,
      label="Bus. & Prof. Code", suffix=r"Bus(?:iness|\.)\s+(?:and|&)\s+Prof(?:essions|\.)\s+Code", grain="section"),
    C("Elec", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Elec(?:tions|\.)\s+Code,?", _CA_SEC,
      label="Elec. Code", suffix=r"Elec(?:tions|\.)\s+Code", grain="section"),
    C("RTC", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Rev(?:enue|\.)\s+(?:and|&)\s+Tax(?:ation|\.)\s+Code,?", _CA_SEC,
      label="Rev. & Tax. Code", suffix=r"Rev(?:enue|\.)\s+(?:and|&)\s+Tax(?:ation|\.)\s+Code", grain="section"),
    C("PRC", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Pub(?:lic|\.)\s+Res(?:ources|\.)\s+Code,?", _CA_SEC,
      label="Pub. Resources Code", suffix=r"Pub(?:lic|\.)\s+Res(?:ources|\.)\s+Code", grain="section"),
    C("Lab", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Lab(?:or|\.)\s+Code,?", _CA_SEC,
      label="Labor Code", suffix=r"Lab(?:or|\.)\s+Code", grain="section"),
    C("Veh", "statute", r"(?:Cal(?:ifornia|\.)\s+)?Veh(?:icle|\.)\s+Code,?", _CA_SEC,
      label="Vehicle Code", suffix=r"Veh(?:icle|\.)\s+Code", grain="section"),
    C("CCR", "rule", r"(?:Cal\.\s+Code\s+Regs\.,?\s+tit(?:le|\.)\s+(?P<q>\d{1,2}),?|(?P<q2>\d{1,2})\s+CCR)",
      r"\d{1,5}(?:\.\d{1,3}){0,2}", label="Cal. Code Regs.", grain="section"),
    notes=("State Administrative Manual (SAM) and SIMM sections are policies in this corpus and are not "
           "extracted as statutes. Statutes are held as section ranges, so grain is the section."),
    held_extra=((re.compile(r"tit\.\s*(\d+),\s*div\.\s*(\d+),\s*ch\.\s*(\d+)"),
                 lambda m: [("rule", "CCR", "chapter", f"{m.group(1)}/div{m.group(2)}-ch{m.group(3)}", None)]),),
)
FORMS["colorado"] = S(
    C("CRS_T", "statute", r"(?:C\.R\.S\.|CRS|Colorado\s+Revised\s+Statutes),?\s*Title\s+(?P<q>\d{1,2}),?\s*Article\s+", r"\d{1,3}(?:\.\d)?",
      label="C.R.S.", ns="CRS", chap=r"\d{1,3}(?:\.\d)?", q_join="-", chapter=dash_n(2), unit_word="article"),
    C("CRS", "statute", r"C\.R\.S\.|CRS|Colorado\s+Revised\s+Statutes",
      r"\d{1,2}~\d{1,3}(?:\.\d)?~\d{1,4}(?:\.\d{1,2})?", label="C.R.S.", chap=r"\d{1,2}~\d{1,3}(?:\.\d)?",
      chap_bare=True, suffix=r"C\.R\.S\.|CRS", sfx_bare=True, chapter=dash_n(2), unit_word="article"),
    C("CRS_R", "statute", r"(?!)", r"(?!)", ns="CRS", label="C.R.S.", unit_word="article", chapter=dash_n(2),
      custom=(r"articles?\s+(\d{1,3}(?:\.\d)?)\s+of\s+title\s+(\d{1,2}),?\s*C\.R\.S\.", lambda m: [("chapter", f"{m.group(2)}-{m.group(1)}")])),
    C("CCR", "rule", r"(?:\d{1,2}\s+)?CCR", r"\d{3,4}~\d{1,3}(?:~\d+){0,3}", label="CCR", chapter=dash_n(2)),
    eo_num=r"[A-Z]\s\d{4}\s\d{3}|[A-Z]{1,2}[-\s]\d{4}[-\s]\d{3}|\d{4}[-\s]\d{2,3}",
    held_extra=(
        (re.compile(r"C\.R\.S\.\s*title\s+(\d+),\s*article\s+([\d.]+)"),
         lambda m: [("statute", "CRS", "chapter", f"{m.group(1)}-{m.group(2)}", None)]),
        (re.compile(r"^([A-Z])\s+(\d{4})\s+(\d{3})$"),
         lambda m: [("eo", "EO", "section", f"{m.group(1)}-{m.group(2)[2:]}-{int(m.group(3))}", None)]),
    ),
)
FORMS["delaware"] = S(
    C("DEL", "statute", r"(?:Title\s+)?(?P<q>\d{1,2})\s+Del\.?\s*C\.?|Delaware\s+Code,?|Del\.\s*C\.",
      r"\d{1,5}[A-Z]?(?:~\d{1,4})?(?:\.\d+)?", label="Del. C.", chap=r"\d{1,3}[A-Z]?", q_default="29",
      chapter=lambda s: (re.match(r"(\d+)-", s).group(1) if "-" in s else
                         (lambda m: (m.group(1)[:-2] or m.group(1)) + m.group(2))(re.match(r"(\d+)([A-Z]?)", s))),
      unit_word="chapter"),
    notes="A Delaware citation with no title number is read as Title 29, the title that holds the DTI statute.",
    held_extra=(
        (re.compile(r"(\d+)\s+Del\.\s*C\.\s*ch\.\s*(\d+[A-Z]?)"),
         lambda m: [("statute", "DEL", "chapter", f"{m.group(1)}/{m.group(2)}", None)]),
    ),
    eo_ambiguous=True,
)
FORMS["florida"] = S(
    C("FS", "statute", r"Florida\s+Statutes,?|F\.S\.,?|Fla\.\s*Stat\.", r"\d{1,3}\.\d{2,5}", label="F.S.",
      chap=r"\d{1,3}", suffix=r"Florida\s+Statutes|F\.S\.|Fla\.\s*Stat\.", chapter=dot0, unit_word="chapter"),
    C("FAC", "rule", r"(?:Rule(?:s)?\s+(?:Chapter\s+)?|Chapter\s+|Ch\.\s*)(?=\d{2}[A-Z]{1,3}-\d)",
      r"\d{2}[A-Z]{1,3}~\d{1,2}(?:\.\d{3,4})?", label="F.A.C.", chap=r"\d{2}[A-Z]{1,3}~\d{1,2}",
      chapter=dot0),
    held_extra=(),
)
FORMS["hawaii"] = S(
    C("HRS", "statute", r"HRS|H\.R\.S\.|Hawaii\s+Revised\s+Statutes", r"\d{1,3}[A-Z]?~\d+(?:\.\d+)?(?:-\d+)?",
      label="HRS", chap=r"\d{1,3}[A-Z]?", chap_bare=True, chapter=dash_n(1), grain="section"),
    C("HAR", "rule", r"HAR|Hawaii\s+Administrative\s+Rules", r"\d{1,2}~\d{1,3}(?:~\d+)?", label="HAR",
      chapter=dash_n(2)),
)
FORMS["idaho"] = S(
    C("IC", "statute", r"Idaho\s+Code|I\.C\.", r"\d{1,2}~(?:\d{2,3}~\d{3}|\d{3,4}[A-Z]?)", label="Idaho Code",
      chap=r"\d{1,2}~\d{1,3}", chap_bare=True, suffix=r"Idaho\s+Code", sfx_bare=True,
      chapter=lambda s: (s.rsplit("-", 1)[0] if s.count("-") == 2 else
                         (lambda m: f"{m.group(1)}-{m.group(2)[:-2] or m.group(2)}")(re.match(r"(\d+)-(\d+)", s))),
      grain="section"),
    C("ICCH", "statute", r"(?!)", r"(?!)", ns="IC", label="Idaho Code",
      custom=(r"chapters?\s+(\d{1,3}),\s*title\s+(\d{1,2}),?\s*Idaho\s+Code", lambda m: [("chapter", f"{m.group(2)}-{m.group(1)}")]),
      chapter=lambda s: None, unit_word="chapter"),
    C("IDAPA", "rule", r"IDAPA", r"\d{2}\.\d{2}\.\d{2}(?:\.\d{3})?", label="IDAPA",
      chapter=dot_n(3)),
)
FORMS["iowa"] = S(
    C("IC", "statute", r"Iowa\s+Code(?:\s+\d{4})?,?(?:\s+Chapter\s+\d+[A-Z]?,)?|Iowa\s+Code\s+Supp\.", r"\d{1,3}[A-Z]?\.\d{1,4}[A-Za-z]?",
      label="Iowa Code", chap=r"\d{1,3}[A-Za-z]?", chap_bare=True, suffix=r"Iowa\s+Code", chapter=dot0, grain="section"),
    C("ICSEC", "statute", r"(?!)", r"(?!)", ns="IC", label="Iowa Code", chapter=dot0,
      custom=(r"Iowa\s+Code\s+Chapter\s+(\d{1,3}[A-Z]?),\s*Section\s+(\d{1,4})\b", lambda m: [("section", f"{m.group(1)}.{m.group(2)}")]),
      grain="section"),
    C("IAC", "rule", r"IAC|Iowa\s+Admin(?:istrative|\.)\s+Code", r"\d{1,3}~\d{1,3}(?:\.\d+)?", label="IAC",
      chap=r"\d{1,3}~\d{1,3}", chapter=dot0),
    eo_ambiguous=True, audit_ignore=r"IAC\s+\d{1,2}/\d{1,2}/\d{2}",
    notes="Iowa Code section numbers are read after 'Iowa Code', with or without the edition year.",
)
FORMS["kansas"] = S(
    C("KSA", "statute", r"K\.S\.A\.(?:\s+(?:\d{4}\s+)?Supp\.)?|KSA", r"\d{1,2}~\d{1,4}(?:[a-z]\d{0,2})?",
      label="K.S.A.", chap=r"\d{1,2}~\d{1,3}", chapter=digits_article, grain="section"),
    C("KAR", "rule", r"K\.A\.R\.", r"\d{1,3}~\d{1,3}~\d{1,3}[a-z]?", label="K.A.R.", chapter=dash_n(2)),
)
FORMS["kentucky"] = S(
    C("KRS", "statute", r"KRS|Kentucky\s+Revised\s+Statutes", r"\d{1,3}[A-Z]?\.\d{3,4}", label="KRS",
      chap=r"\d{1,3}[A-Z]?", chap_bare=True, chapter=dot0, grain="section"),
    C("KAR", "rule", r"(?P<q>\d{1,3})\s+KAR", r"\d{1,3}:\d{3}", label="KAR", chapter=lambda s: s.split(":")[0]),
)
FORMS["louisiana"] = S(
    C("RS", "statute", r"(?:La\.\s*)?R\.S\.|LSA-R\.S\.|Louisiana\s+Revised\s+Statutes", r"\d{1,2}:\d{1,5}(?:\.\d+)*",
      label="R.S.", short=":", chapter=colon0, grain="section"),
    C("LAC", "rule", r"LAC|Louisiana\s+Administrative\s+Code", r"\d{1,2}:[IVXLC]+(?:\.\d+)?", label="LAC",
      chapter=lambda s: s.split(".")[0]),
    C("LAC_T", "rule", r"Louisiana\s+Administrative\s+Code,?\s*Title\s+(?P<q>\d{1,2})(?:\.|,)?\s*Part\s+", r"[IVXLC]+", label="LAC",
      ns="LAC", chap=r"[IVXLC]+", q_join=":", chapter=lambda s: s.split(".")[0]),
    eo_num=r"[A-Z]{1,3}\s\d{2}-\d{1,3}",
)
FORMS["maine"] = S(
    C("MRS", "statute", r"(?P<q>\d{1,2})\s+M\.?R\.?S\.?A?\.?", r"\d{1,5}(?:-[A-Z])?", label="M.R.S.",
      chap=r"\d{1,4}(?:-[A-Z])?", grain="section", chapter=None),
    C("CMR", "rule", r"(?P<q>\d{2}-\d{3})\s+C\.M\.R\.", r"(?:ch\.\s*)?\d{1,4}", label="C.M.R.", chap=r"\d{1,4}"),
    notes=("Maine section numbers do not reveal their chapter, so a held chapter covers the sections printed "
           "in its text and nothing else."),
    held_extra=((re.compile(r"(\d+)\s+M\.R\.S\.\s*ch\.\s*(\d+(?:-[A-Z])?)"),
                 lambda m: [("statute", "MRS", "chapter", f"{m.group(1)}/{m.group(2)}", None)]),),
    uncitable=(("me-eo-ai-task-force-2024-12", "an order cited by its date, not a number"),),
)
_MD_SEC = r"\d{1,2}(?:\.\d)?[A-Za-z]?~(?:\d[A-Za-z]?~)?\d{2,4}(?:\.\d+)?|\d{1,2}~\d{3,4}"
FORMS["maryland"] = S(
    C("SFP", "statute", r"(?:Md\.\s*Code(?:\s*Ann\.)?,?\s*)?(?:State\s+Fin(?:ance|\.)?\s*(?:and|&)\s*Proc(?:urement|\.)?"
      r"(?:\s+Article|\s+Code(?:\s+Ann\.)?)?|SF&P|SFP)\s*,?", _MD_SEC, label="State Fin. & Proc.", grain="section"),
    C("SG", "statute", r"(?:Md\.\s*Code(?:\s*Ann\.)?,?\s*)?State\s+Gov(?:ernment|'t|\.)?(?:\s+Article|\s+Code(?:\s+Ann\.)?)?\s*,?",
      _MD_SEC, label="State Gov't", grain="section"),
    C("GP", "statute", r"(?:Md\.\s*Code(?:\s*Ann\.)?,?\s*)?General\s+Provisions(?:\s+Article)?\s*,?",
      _MD_SEC, label="General Provisions", grain="section"),
    C("COMAR", "rule", r"COMAR", r"\d{2}[A-Z]?\.\d{2}(?:\.\d{2}(?:\.\d{2})?)?", label="COMAR", chapter=dot_n(2)),
    eo_num=r"\d{2}\.\d{2}\.\d{4}\.\d{2}",
    renumber=lambda ns, t: (m := re.fullmatch(r"3A-(30[1-9])", t)) and ns == "SFP" and "3.5-" + m.group(1) or None,
    renumber_evidence=("_meta/sources/maryland.yml, md-sfp-3-5-powers-and-duties-of-the-secretary: 'its older policies cite "
                       "the same duties as 'SF&P 3A-301-309''."),
    notes=("Section numbers are read as printed. Older Maryland policies cite the Department of IT's duties as "
           "'SF&P 3A-301 to 3A-309'; the seed entry md-sfp-3-5-powers-and-duties-of-the-secretary says they are the "
           "duties held as 3.5-301 to 3.5-309, so those citations resolve to the held text."),
)
FORMS["massachusetts"] = S(
    C("MGL", "statute", r"(?:M\.?\s?G\.?\s?L\.?|G\.L\.|Massachusetts\s+General\s+Laws)\s*(?:c\.|ch\.|Ch\.|chapter)\s*(?P<q>\d{1,3}[A-Za-z]?)(?:\s*,)?",
      r"\d{1,3}[A-Z]?(?:\s?\d)?", label="M.G.L.", q_is_chapter=True, chap=r"\d{1,3}[A-Z]?"),
    C("CMR", "rule", r"(?P<q>\d{1,3})\s+CMR", r"\d{1,3}(?:\.\d{1,2})?", label="CMR", chapter=dot0, whole=r"\.00"),
    notes="A chapter of the General Laws cited with no section is a chapter-level citation.",
)
FORMS["michigan"] = S(
    C("MCL", "statute", r"MCL|M\.C\.L\.|Michigan\s+Compiled\s+Laws", r"\d{1,3}[a-z]?\.\d{1,4}[a-z]{0,2}\d?",
      label="MCL", chapter=dot0, unit_word="chapter"),
    C("PA", "statute", r"(?:Public\s+)?Act(?=\s+\d+\s+of\s+\d{4})", r"\d{1,4}\s+of\s+\d{4}", label="Act",
      chapter=lambda s: s, unit_word=""),
    C("MAC", "rule", r"Admin\s+Rule:?|Mich(?:igan)?\.?\s+Admin(?:istrative)?\.?\s+Code,?", r"R\s?\d{1,3}\.\d{1,4}[a-z]?", label="Mich. Admin. Code",
      chapter=lambda s: "R" + re.match(r"R\s?(\d+)", s).group(1)),
    eo_num=r"\d{4}~\d{1,3}",
    notes="Public Acts are cited as 'Act 431 of 1984'; compiled-law sections as MCL; rules as 'Admin Rule: R 18.201'.",
)
FORMS["minnesota"] = S(
    C("MS", "statute", r"Minn(?:esota|\.)\s*Stat(?:utes|s)?\.?(?:\s+\d{4})?,?", r"\d{1,3}[A-Z]?\.\d{1,4}[a-z]?",
      label="Minn. Stat.", chap=r"\d{1,3}[A-Z]?", chapter=dot0, unit_word="chapter"),
    C("MR", "rule", r"Minn(?:esota|\.)\s*(?:Rules|R\.),?(?:\s+(?:parts?))?", r"\d{4}(?:\.\d{4})?", label="Minn. R.",
      chap=r"\d{4}", chapter=dot0),
)
FORMS["missouri"] = S(
    C("RSMo", "statute", r"RSMo|R\.S\.Mo\.|Revised\s+Statutes\s+of\s+Missouri", r"\d{1,3}\.\d{3,4}", label="RSMo",
      chap=r"\d{1,3}", suffix=r"RSMo|R\.S\.Mo\.", sfx_bare=True, chapter=dot0, grain="section"),
    C("CSR", "rule", r"(?P<q>\d{1,2})\s+CSR", r"\d{1,3}~\d{1,3}(?:\.\d+)?", label="CSR", chap=r"\d{1,3}~\d{1,3}",
      chapter=lambda s: s.split(".")[0]),
)
FORMS["montana"] = S(
    C("MCA", "statute", r"Mont\.\s*Code\s*Ann\.|Montana\s+Code\s+Annotated(?:\s+\d{4})?|MCA", r"\d{1,2}~\d{1,3}~\d{1,4}",
      label="MCA", suffix=r"MCA|Mont\.\s*Code\s*Ann\.", sfx_bare=True, chapter=dash_n(2), grain="section"),
    C("ARM", "rule", r"ARM", r"\d{1,2}\.\d{1,3}\.\d{1,4}", label="ARM", chapter=dot_n(2)),
    audit_ignore=r"Montana\s+Code\s+Annotated\s+\d{4}\s*$|MCA\s+\d{4}\b",
    held_extra=((re.compile(r"ARM\s+Title\s+(\d+),\s*chapter\s+(\d+)"),
                 lambda m: [("rule", "ARM", "chapter", f"{m.group(1)}.{m.group(2)}", None)]),),
)
FORMS["nebraska"] = S(
    C("NRS", "statute", r"Neb\.\s*Rev\.\s*Stat\.(?:\s+(?:Supp\.|Cum\.\s*Supp\.|Reissue)[^§\d]{0,15})?|R\.R\.S\.(?:\s*Neb\.)?|Nebraska\s+Revised\s+Statutes?",
      r"\d{1,3}~\d{1,4}(?:,\d{3})?(?:\.\d{1,3})?", label="Neb. Rev. Stat.", suffix=r"R\.R\.S\.(?:\s*Neb\.)?|Neb\.\s*Rev\.\s*Stat\.",
      chapter=dash_n(1), grain="section"),
    C("NAC", "rule", r"(?P<q>\d{1,3})\s+NAC", r"\d{1,3}", label="NAC", chapter=lambda s: s),
)
FORMS["nevada"] = S(
    C("NRS", "statute", r"NRS|Nevada\s+Revised\s+Statutes", r"\d{1,3}[A-Z]?\.\d{1,5}", label="NRS",
      chap=r"\d{1,3}[A-Z]?", chap_bare=True, chapter=dot0, unit_word="chapter"),
    C("NAC", "rule", r"NAC|Nevada\s+Administrative\s+Code", r"\d{1,3}[A-Z]?\.\d{1,5}", label="NAC",
      chap=r"\d{1,3}[A-Z]?", chapter=dot0),
)
FORMS["new-hampshire"] = S(
    C("RSA", "statute", r"RSA|Revised\s+Statutes\s+Annotated", r"\d{1,3}(?:-[A-Z])?:\d{1,3}(?:-[a-z]){0,2}", label="RSA",
      chap=r"\d{1,3}(?:-[A-Z])?", chapter=colon0, unit_word="chapter"),
    notes="New Hampshire administrative rules are cited by agency code (e.g. 'Saf-C 1000'); no such form was found in the held documents.",
)
FORMS["new-jersey"] = S(
    C("NJSA", "statute", r"N\.J\.S\.A\.(?:\s*C\.)?|NJSA", r"\d{1,2}[A-Z]?:\d{1,3}[A-Z]?(?:~\d{1,4}(?:\.\d{1,3})?)?", label="N.J.S.A.",
      chapter=lambda s: s.split("-")[0] if "-" in s else None, grain="section"),
    C("NJAC", "rule", r"N\.J\.A\.C\.", r"\d{1,2}:\d{1,3}[A-Z]?(?:~\d+(?:\.\d+)?)?", label="N.J.A.C.",
      chapter=lambda s: s.split("-")[0]),
    eo_ambiguous=True,
)
FORMS["new-mexico"] = S(
    C("NMSA", "statute", r"NMSA(?:\s+1978)?,?", r"\d{1,2}~\d{1,3}[A-Z]?~\d{1,3}(?:\.\d)?", label="NMSA 1978",
      suffix=r"NMSA(?:\s+1978)?", sfx_bare=True, chapter=dash_n(2), unit_word="article"),
    C("NMSA_ART", "statute", r"Chapter\s+(?P<q>\d{1,2}),\s*Article\s+", r"\d{1,3}[A-Z]?", label="NMSA 1978", ns="NMSA",
      chap=r"\d{1,3}[A-Z]?(?=\s+NMSA)", q_join="-", chapter=dash_n(2), unit_word="article"),
    C("NMAC", "rule", r"NMAC\s+|(?=\d{1,2}\.\d{1,3}\.\d{1,3}(?:\.\d{1,3})?\s+NMAC)", r"\d{1,2}\.\d{1,3}\.\d{1,3}(?:\.\d{1,3})?", label="NMAC",
      chapter=dot_n(3)),
    held_extra=((re.compile(r"NMSA\s+1978,\s*chapter\s+(\d+),\s*article\s+(\d+[A-Z]?)"),
                 lambda m: [("statute", "NMSA", "chapter", f"{m.group(1)}-{m.group(2)}", None)]),),
    audit_ignore=r"NMAC\s{5,}\d*\s*$",
)
_NY_NAMES = r"(?P<q>(?:State\s+)?(?:Technology|Public\s+Officers|Civil\s+Service|State\s+Finance|Executive|Education|General\s+Business|Public\s+Authorities|Penal|Labor|Retirement\s+and\s+Social\s+Security|General\s+Municipal|Public\s+Service|Arts\s+and\s+Cultural\s+Affairs|Public\s+Health|Social\s+Services|Legislative|State\s+Administrative\s+Procedure|Judiciary|Tax|Vehicle\s+and\s+Traffic|Insurance|Banking|Real\s+Property|Military|Correction|Mental\s+Hygiene|Environmental\s+Conservation|Highway|Transportation|Public\s+Buildings|State\s+Law)\s+Law)"
FORMS["new-york"] = S(
    C("NYL", "statute", _NY_NAMES + r"\s*,?", r"\d{1,4}(?:-[a-z])?", label="Law",
      chapter=lambda s: None, grain="law", qnorm=lambda q: re.sub(r"^(Technology Law)$", r"State \1", q)),
    C("NYCRR", "rule", r"(?:(?P<q>\d{1,2})\s+)?NYCRR\s+(?:Part\s+)?", r"\d{3}(?:\.\d+)?", label="NYCRR", chapter=dot0),
    eo_ambiguous=True, unreliable=("eo",),
    held_extra=((re.compile(r"State Technology Law, Article \d \(sections ([\d-]+[a-z]?)-([\d-]+[a-z]?)\)"),
                 lambda m: [("statute", "NYL", "section", "State Technology Law/" + m.group(1), "State Technology Law/" + m.group(2))]),),
    notes=("Executive Order numbers in the PDF text carry footnote marks ('Executive Order No. 117 1'); a "
           "footnote mark run into the number reads as a different order, so Executive Orders are unreliable. "
           "The State Technology Law is held by article (hundreds digit of the section)."),
)
FORMS["north-carolina"] = S(
    C("GS", "statute", r"N\.?C\.?G\.?S\.?|G\.S\.|N\.C\.\s*Gen\.\s*Stat\.|North\s+Carolina\s+General\s+Statutes",
      r"\d{1,3}[A-Za-z]?~\d{1,4}(?:\.\d{1,3})?[A-Z]?", label="G.S.", chap=r"\d{1,3}[A-Za-z]?", chap_bare=True, chapter=lambda s: dash_n(1)(s).upper()),
    C("NCAC", "rule", r"(?:\d{2}\s+)?NCAC", r"\d{2}[A-Za-z]\s?(?:\.\d{4})?", label="NCAC", chapter=lambda s: re.match(r"\d{2}[A-Za-z]", s).group().upper()),
    eo_ambiguous=True,
    held_extra=((re.compile(r"G\.S\.\s*(\d+[A-Z]?),\s*Article\s+(\d+)"),
                 lambda m: [("statute", "GS", "chapter", m.group(1), None)]),
                (re.compile(r"NCAC\s+Subchapter\s+(\d{2}[A-Z])"),
                 lambda m: [("rule", "NCAC", "chapter", m.group(1), None)]),),
)
FORMS["north-dakota"] = S(
    C("NDCC", "statute", r"N\.?D\.?C\.?C\.?|NDCC|North\s+Dakota\s+Century\s+Code|Century\s+Code", r"\d{1,2}(?:\.\d)?~\d{1,3}(?:\.\d)?~\d{1,3}(?:\.\d+)?",
      label="N.D.C.C.", chap=r"\d{1,2}(?:\.\d)?~\d{1,3}(?:\.\d)?", chap_bare=True, chapter=dash_n(2), unit_word="chapter"),
    C("NDAC", "rule", r"N\.D\.\s*Admin\.\s*Code|NDAC|N\.D\.A\.C\.", r"\d{1,3}~\d{2}~\d{2}(?:~\d{2})?", label="N.D. Admin. Code",
      chap=r"\d{1,3}~\d{2}~\d{2}", chapter=dash_n(3)),
)
FORMS["ohio"] = S(
    C("ORC", "statute", r"R\.C\.|ORC|O\.R\.C\.|(?:Ohio\s+)?Revised\s+Code", r"\d{1,4}\.\d{1,3}(?:\.\d+)?", label="R.C.",
      chap=r"\d{1,4}", suffix=r"(?:Ohio\s+)?Revised\s+Code|R\.C\.", chapter=dot0, grain="section"),
    C("OAC", "rule", r"OAC|Ohio\s+Adm(?:in)?\.\s*Code|Ohio\s+Administrative\s+Code", r"\d{1,4}[:-]\d{1,2}(?:-\d{1,3})?(?:-\d{2})?",
      label="OAC", chap=r"\d{1,4}[:-]\d{1,3}", chapter=lambda s: re.match(r"\d+[:-]\d+(?:-\d+)?", s).group()
      if s.count("-") + s.count(":") < 3 else re.match(r"\d+[:-]\d+-\d+", s).group()),
)
FORMS["oklahoma"] = S(
    C("OS", "statute", r"(?:Title\s+)?(?P<q>\d{1,3})\s+O\.S\.(?:\s+Supp\.\s*\d{4})?|(?<![\w.])O\.S\.", r"\d{1,4}[A-Z]?(?:\.\d{1,3}){0,2}[a-z]?",
      label="O.S.", chap=r"\d{1,4}", chapter=dot0, grain="section"),
    C("OAC", "rule", r"OAC|Oklahoma\s+Administrative\s+Code", r"\d{1,3}:\d{1,3}(?:-\d+(?:-\d+)?)?", label="OAC",
      chapter=lambda s: ":".join([s.split(":")[0], s.split(":")[1].split("-")[0]])),
)
FORMS["oregon"] = S(
    C("ORS", "statute", r"ORS|Oregon\s+Revised\s+Statutes", r"\d{1,3}[A-C]?\.\d{3,4}[a-z]?", label="ORS", chap=r"\d{1,3}[A-C]?",
      chap_bare=True, chapter=dot0, unit_word="chapter"),
    C("OAR", "rule", r"OAR|Oregon\s+Administrative\s+Rules?", r"\d{3}~\d{2,3}(?:~\d{3,4})?", label="OAR",
      chapter=lambda s: "-".join([s.split("-")[0], s.split("-")[1].zfill(3)])),
    held_extra=((re.compile(r"OAR\s+chapter\s+(\d+),\s*division\s+(\d+)"),
                 lambda m: [("rule", "OAR", "chapter", f"{m.group(1)}-{int(m.group(2)):03d}", None)]),),
    renumber=lambda ns, t: re.sub(r"^125-800", "128-030", t) if ns == "OAR" and t.startswith("125-800") else None,
    renumber_evidence=("_meta/sources/oregon.yml, or-oar-128-30: 'Government-wide information security rules ... "
                       "renumbered from OAR 125-800 effective 2026-05-01.'"),
)
FORMS["pennsylvania"] = S(
    C("PS", "statute", r"(?P<q>\d{1,3})\s+P\.S\.", r"\d{1,5}(?:\.\d{1,4})?[a-z]?", label="P.S.", chapter=lambda s: None, grain="section"),
    C("PACS", "statute", r"(?:(?P<q>\d{1,2})\s+)?Pa\.?\s?C\.S\.A?\.", r"\d{3,5}", label="Pa.C.S.", chapter=lambda s: None, grain="section"),
    C("ACT", "statute", r"Act\s+of\s+(?:[A-Z][a-z]+\.?\s+\d{1,2},\s+)?(?=\d{4},\s*P\.L\.)", r"\d{4},\s*P\.L\.\s*\d+,\s*No\.\s*\d+",
      label="Act", chapter=lambda s: s, grain="chapter"),
    C("PACODE", "rule", r"(?P<q>\d{1,2})\s+Pa\.?\s?Code", r"\d{1,4}\.\d{1,4}", label="Pa. Code", chapter=dot0),
    eo_num=r"\d{4}~\d{1,2}",
    notes="Management Directives and other Commonwealth policies are policies in this corpus, not extracted as instruments.",
)
FORMS["rhode-island"] = S(
    C("RIGL", "statute", r"R\.I\.\s*Gen\.\s*Laws|RIGL|Rhode\s+Island\s+General\s+Laws|G\.L\.\s*(?:1956)?", r"\d{1,2}~\d{1,3}(?:\.\d)?~\d{1,3}(?:\.\d+)?",
      label="R.I. Gen. Laws", chap=r"\d{1,2}~\d{1,3}(?:\.\d)?", chapter=dash_n(2), grain="section"),
    C("RICR", "rule", r"(?=\d{3}-RICR)", r"\d{3}~RICR~\d{2}~\d{2}~\d{1,2}(?:\.\d+)?", label="RICR", chapter=lambda s: "-".join(s.split("-")[:4])),
)
FORMS["south-carolina"] = S(
    C("SCC", "statute", r"S\.?C\.?\s*Code(?:\s+Ann\.)?(?:\s+of\s+Laws)?(?:,?\s*1976)?,?", r"\d{1,2}~\d{1,2}~\d{1,4}(?:\.\d+)?", label="S.C. Code",
      chap=r"\d{1,2}~\d{1,2}", suffix=r"(?:South\s+Carolina\s+)?(?:Code\s+of\s+Laws|1976\s+Code)", chapter=dash_n(2), unit_word="chapter"),
    C("SCR", "rule", r"S\.C\.\s*Code\s*Regs\.", r"\d{1,3}~\d{1,4}(?:\.\d+)?", label="S.C. Code Regs.", chapter=dash_n(1)),
    held_extra=((re.compile(r"S\.C\.\s*Code\s*Title\s+(\d+),\s*Chapter\s+(\d+)"),
                 lambda m: [("statute", "SCC", "chapter", f"{m.group(1)}-{m.group(2)}", None)]),),
)
FORMS["south-dakota"] = S(
    C("SDCL", "statute", r"SDCL,?", r"\d{1,2}~\d{1,2}[A-Z]?~\d{1,3}(?:\.\d+)?", label="SDCL", chap=r"\d{1,2}~\d{1,2}[A-Z]?",
      chapter=dash_n(2), grain="section"),
    C("ARSD", "rule", r"ARSD", r"\d{2}:\d{2}(?::\d{2}(?::\d{2}(?:\.\d+)?)?)?", label="ARSD",
      chapter=lambda s: ":".join(s.split(":")[:2])),
)
_TX_SEC = r"\d{1,4}\.\d{2,5}"
_TX = r"(?:Tex(?:as|\.)\s+)?"
FORMS["texas"] = S(
    C("Gov", "statute", _TX + r"Gov(?:ernment|'t|\.)\s+Code,?(?:\s+Subchapter\s+[A-Z0-9-]+,)?", _TX_SEC, label="Gov't Code", chap=r"\d{1,4}",
      suffix=_TX + r"Gov(?:ernment|'t|\.)\s+Code", chapter=dot0, unit_word="chapter"),
    C("BCC", "statute", _TX + r"Bus(?:iness|\.)\s+(?:and|&)\s+Com(?:merce|\.)\s+Code,?", _TX_SEC, label="Bus. & Com. Code", chap=r"\d{1,4}",
      suffix=_TX + r"Bus(?:iness|\.)\s+(?:and|&)\s+Com(?:merce|\.)\s+Code", chapter=dot0, unit_word="chapter"),
    C("HSC", "statute", _TX + r"Health\s+(?:and|&)\s+Safety\s+Code,?", _TX_SEC, label="Health & Safety Code", chap=r"\d{1,4}",
      suffix=_TX + r"Health\s+(?:and|&)\s+Safety\s+Code", chapter=dot0, unit_word="chapter"),
    C("Edu", "statute", _TX + r"Education\s+Code,?", _TX_SEC, label="Education Code", chap=r"\d{1,4}",
      suffix=_TX + r"Education\s+Code", chapter=dot0, unit_word="chapter"),
    C("Pen", "statute", _TX + r"Penal\s+Code,?", _TX_SEC, label="Penal Code", chap=r"\d{1,4}",
      suffix=_TX + r"Penal\s+Code", chapter=dot0, unit_word="chapter"),
    C("TACT", "rule", r"(?!)", r"(?!)", ns="TAC", label="TAC", chapter=dot0,
      custom=(r"Texas\s+Administrative\s+Code,?\s*Title\s+(\d{1,2}),?\s*(?:Part\s+\d+,?\s*)?Chapter\s+(\d{1,4})",
              lambda m: [("chapter", f"{m.group(1)}/{m.group(2)}")])),
    C("TAC", "rule", r"(?:(?P<q>\d{1,2})\s+)?(?:TAC|Tex\.\s*Admin\.\s*Code|Texas\s+Administrative\s+Code)", r"\d{1,4}(?:\.\d{1,4})?", label="TAC",
      chap=r"\d{1,4}", q_default="1", chapter=dot0),
    notes="A Texas Administrative Code citation with no title number is read as Title 1 (the Department of Information Resources).",
    held_extra=((re.compile(r"(\d+)\s+TAC\s+chapter\s+(\d+)"),
                 lambda m: [("rule", "TAC", "chapter", f"{m.group(1)}/{m.group(2)}", None)]),
                (re.compile(r"(Government|Business and Commerce)\s+Code\s+chapter\s+(\d+)"),
                 lambda m: [("statute", "Gov" if m.group(1) == "Government" else "BCC", "chapter", m.group(2), None)]),),
)
FORMS["utah"] = S(
    C("UC", "statute", r"Utah\s+Code(?:\s+Ann\.)?|UCA|U\.C\.A\.", r"\d{1,3}[A-Z]?~\d{1,3}[a-z]?~\d{1,4}(?:\.\d+)?", label="Utah Code",
      chap=r"\d{1,3}[A-Z]?~\d{1,3}[a-z]?", chap_bare=True, bare=True, chapter=dash_n(2), unit_word="chapter"),
    C("UAC", "rule", r"Utah\s+Admin(?:istrative|\.)\s+Code,?|UAC|Rule", r"R\d{3}~\d{1,2}(?:~\d{1,3})?", label="Utah Admin. Code", chapter=dash_n(2)),
    held_extra=((re.compile(r"Utah\s+Administrative\s+Code\s+(R\d{3}-\d{1,2})"),
                 lambda m: [("rule", "UAC", "chapter", m.group(1), None)]),),
    uncitable=(("ut-eo-2001-12-11-cio-security", "an order cited by its date, not a number"),),
)
FORMS["vermont"] = S(
    C("VSA", "statute", r"(?P<q>\d{1,2})\s+V\.S\.A\.|(?<![\d\s]\s)V\.S\.A\.", r"\d{1,5}[a-z]?(?:-[a-z])?", label="V.S.A.", chap=r"\d{1,3}",
      chapter=lambda s: None, grain="section"),
    notes="V.S.A. citations with no title number cannot be resolved to a title and are not extracted.",
    eo_ambiguous=True,
)
FORMS["virginia"] = S(
    C("VA", "statute", r"Code\s+of\s+Virginia,?(?:\s+\(1950\),?)?|Va\.\s*Code(?:\s+Ann\.)?,?", r"\d{1,2}(?:\.\d{1,2})?~\d{1,5}(?:\.\d{1,3})?(?::\d{1,3})?", label="Va. Code",
      suffix=r"Code\s+of\s+Virginia|Va\.\s*Code", bare=True, chapter=lambda s: None, grain="section"),
    C("VAC", "rule", r"(?=\d{1,2}\s?VAC\s?\d)", r"\d{1,2}\s?VAC\s?\d{1,3}~\d{1,3}(?:~\d+)?", label="VAC",
      chapter=lambda s: "-".join(s.replace(" ", "").split("VAC")[1].split("-")[:2])),
    eo_kinds=("EO", "ED"), eo_ambiguous=True,
    notes="Virginia section numbers do not reveal their chapter, so a held chapter covers the sections printed in its text.",
    held_extra=((re.compile(r"Va\.\s*Code\s*tit\.\s*([\d.]+),\s*ch\.\s*([\d.]+)"),
                 lambda m: [("statute", "VA", "chapter", f"{m.group(1)}/{m.group(2)}", None)]),),
)
FORMS["washington"] = S(
    C("RCW", "statute", r"RCW", r"\d{1,3}[A-Z]?\.\d{1,3}[A-Z]?\.\d{3,4}", label="RCW", chap=r"\d{1,3}[A-Z]?\.\d{1,3}[A-Z]?", chap_bare=True,
      suffix=r"RCW", chapter=dot_n(2), unit_word="chapter"),
    C("WAC", "rule", r"WAC", r"\d{2,3}~\d{2,3}(?:~\d{3,4}[A-Z]?)?", label="WAC", chap=r"\d{2,3}~\d{2,3}", suffix=r"WAC",
      chapter=dash_n(2)),
    uncitable=(("wa-law-2026-c167", "a session law, cited by chapter and year rather than by code section"),),
)
FORMS["west-virginia"] = S(
    C("WV", "statute", r"W\.?\s?Va\.\s*Code|WV\s+Code|West\s+Virginia\s+Code", r"\d{1,3}[A-Z]?~\d{1,3}[A-Z]?~\d{1,3}[a-z]?(?:[a-z]\d+)?", label="W. Va. Code",
      chap=r"\d{1,3}[A-Z]?~\d{1,3}[A-Z]?", chap_bare=True, chapter=dash_n(2), grain="section"),
    C("CSR", "rule", r"(?:W\.?\s?Va\.\s*)?CSR|Code\s+of\s+State\s+Rules", r"\d{1,3}~\d{1,3}(?:~\d+)?", label="W. Va. CSR", chapter=dash_n(2)),
    eo_ambiguous=True,
)
FORMS["wisconsin"] = S(
    C("WS", "statute", r"Wis(?:consin|\.)\s*Stat(?:utes|s)?\.?(?:\s+(?:20\d\d|updated\s+through\s+\d{4}))?,?", r"\d{1,3}\.\d{1,4}", label="Wis. Stat.",
      chap=r"\d{1,3}", chapter=dot0, grain="section"),
    C("WAC", "rule", r"Wis(?:consin|\.)\s*Admin(?:istrative|\.)\s*Code,?(?:\s+ch\.)?", r"[A-Z][a-z]{1,4}\s?\d{1,3}(?:\.\d{2,3})?", label="Wis. Admin. Code",
      chapter=lambda s: re.match(r"[A-Z][a-z]{1,4}\s?\d{1,3}", s).group()),
)
FORMS["wyoming"] = S(
    C("WS", "statute", r"W\.S\.(?:\s*[§S]\.?)?|Wyoming\s+Stat(?:utes|ute)\.?\s*(?:\.S\.)?|Wyo\.\s*Stat\.(?:\s*Ann\.)?", r"\d{1,2}~\d{1,2}~\d{1,4}", label="W.S.",
      chapter=dash_n(2), grain="section"),
)


# What each state's documents print that this table does not read (found by the audit in authority_refs.audit_text:
# a code name followed by a number with no extracted citation). Said once here so the JSON carries it per state.
EXTRA_NOTES = {
    "california": "Citations by structure alone ('Government Code, Title 2, Division 3, Part 1' or 'Section 7920.000) of Title 1 of the Government Code') are not read.",
    "virginia": "A chapter cited as 'Chapter 20.1 of Title 2.2' (chapter before title) is not read.",
    "maryland": "A statute cited by Article, Title and Subtitle with no section number ('State Government Article, Title 10, Subtitle 13') is not read.",
    "north-carolina": "'Article 3A of G.S. 150B' and 'Article 3D of Chapter 147 of the General Statutes' (article before chapter) are not read; old title numbers ('4 NCAC 21') are not read.",
    "south-carolina": "A chapter cited as 'Chapter 6, Title 26 of the 1976 Code' is not read.",
    "florida": "A list shorthand ('§§ 501.171, 812.081, 815.04, .045, Florida Statutes') stops at the shorthand, and subdivisions run into the number ('216.023(4)(a)10') end a list.",
    "new-mexico": "A whole chapter cited as 'Chapter 15 NMSA 1978' is not read (the corpus holds articles).",
    "iowa": "Administrative rules are read as chapter-level units ('11-25'); the parenthetical statute ('(8A)') that Iowa rules print after a rule number is not read as a citation.",
    "new-york": "A law cited by article only ('Public Officers Law, art. 6-A') is not read; a law is the unit for every law except the State Technology Law.",
}
for _k, _v in EXTRA_NOTES.items():
    FORMS[_k] = dataclasses.replace(FORMS[_k], notes=(FORMS[_k].notes + " " + _v).strip())
