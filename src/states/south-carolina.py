"""South Carolina: the General Assembly's Code of Laws pages. Hooks are described in src/states/__init__.py.

Statutes are served one chapter per page (`/code/t<title>c<chapter>.php`, the link the General Assembly's title
pages print): a PHP page whose law sits in `<div id="contentsection">`, written as lines separated by `<br />`:
the title line, the chapter number and name, article number and name lines, then each section as a bold
`SECTION n-n-n.` line, its caption, its paragraphs and a `HISTORY:` line, with editor's, code commissioner's and
amendment notes between sections. The page declares ISO-8859-1 but is UTF-8 (a byte order mark leads it).
Menus, scripts, the breadcrumb and the footer sit outside the content section. PDFs and Word files are shared; the Governor's orders print their heading as `Executive Order No. 2017-08`
(the default check looks for the words without `No.`), so the hook reads the heading line."""
from __future__ import annotations

import datetime
import re

from src.ingest_common import _clean_line, pdf_to_text
from src.states import UNHANDLED

_START = '<div id="contentsection">'
_END = "<!-- mainwidepanel -->"
_HEADING = re.compile(r"^(SECTION \d+-\d+-\d+(?:\.\d+)?\.(?: |$)|ARTICLE \d+\w*$|SUBARTICLE \d+\w*$)")
_ORDER_HEADING = re.compile(r"^executive\s+order\s+(?:no\.?)?\s*(\d{4}-\d+)\s*$", re.I)
_ORDER_CITATION = re.compile(r"Executive Order No\. (\d{4}-\d+)$")
_CITATION = re.compile(r"Title (?P<t>\d+\w*), Chapter (?P<c>\d+\w*)$")
_SECTION_CITATION = re.compile(r"S\.C\. Code §§? (?P<a>\d+-\d+-\d+(?:\.\d+)?)(?: to (?P<b>\d+-\d+-\d+(?:\.\d+)?))?$")


def _decode(raw: bytes) -> str:
    try:
        return raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        return raw.decode("cp1252", errors="replace")


def statute_html_to_text(raw: bytes) -> str:
    """One chapter page to text: the content section, one line per source line, a blank line before each article and
    section line (the section's number and caption are one line, as printed). Nothing inside it is dropped."""
    page = _decode(raw)
    start = page.find(_START)
    end = page.find(_END, start)
    if start < 0 or end < 0:
        raise ValueError("no statute text: the page has no content section (the layout changed, or this is not "
                         "a Code of Laws chapter page)")
    region = page[start + len(_START):end]
    region = re.sub(r"<(script|style)\b.*?</\1>|<!--.*?-->", "", region, flags=re.S | re.I)
    region = re.sub(r"<br\s*/?>|</?div\b[^>]*>", "\n", region, flags=re.I)
    lines = [l for l in (_clean_line(re.sub(r"<[^>]+>", "", x)) for x in region.split("\n")) if l]
    if (len(lines) < 4 or not re.match(r"^Title \d+\w* - ", lines[0]) or not re.match(r"^CHAPTER \d+\w*$", lines[1])
            or not any(l.startswith("SECTION ") for l in lines)):
        raise ValueError("no statute text: the page has no title, chapter and sections (the layout changed, or "
                         "this is not a Code of Laws chapter page)")
    out: list[str] = []
    for i, line in enumerate(lines):
        if i >= 2 and _HEADING.match(line):
            out.append("")
        out.append(line)
    return "\n".join(out) + "\n"


# ---- section slices of a chapter page ----------------------------------------------------------------------
# The General Assembly serves a chapter per page, so a provision inside a chapter that is not itself IT law is a slice
# `{section_start, section_end_before}` (printed section numbers; the end section is not in it).

_SECTION_LINE = re.compile(r"^SECTION (\d+-\d+-\d+(?:\.\d+)?)\.(?: |$)")
_DIVIDER = re.compile(r"^(?:ARTICLE|SUBARTICLE) \w+$", re.I)
_SECTION_NUMBER = re.compile(r"\d+-\d+-\d+(?:\.\d+)?")
_MONTHS = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
           "november", "december")
_EFFECTIVE_ON = re.compile(r"\beff(?:ective|\.)?\s+(" + "|".join(m.capitalize() for m in _MONTHS) +
                           r")\s+(\d{1,2}),\s+(\d{4})")


def slice_sections(text: str, start: str, end_before: str) -> str:
    """The lines from the heading of section `start` to the line before the heading of section `end_before`, from
    the text `statute_html_to_text` makes. The page's title and chapter lines must be the ones the section numbers
    name. Article and subarticle headings (with their name line) that stand between the last section and the end
    section belong to the next section and are dropped; nothing else is."""
    for n in (start, end_before):
        if not _SECTION_NUMBER.fullmatch(n):
            raise ValueError(f"{n!r} is not a section number (as in 11-35-820)")
    lines = text.splitlines()
    title, chapter = start.split("-")[:2]
    if (not re.match(rf"^Title {title} - ", lines[0]) or lines[1] != f"CHAPTER {chapter}"
            or end_before.split("-")[:2] != [title, chapter]):
        raise ValueError(f"the page is not Title {title}, Chapter {chapter}: a slice from {start} to {end_before} "
                         f"cannot be cut from it")
    heads = [(i, m.group(1)) for i, l in enumerate(lines) if (m := _SECTION_LINE.match(l))]
    first = [i for i, n in heads if n == start]
    if len(first) != 1:
        raise ValueError(f"section {start} is printed {len(first)} times as a heading on the page "
                         f"(the layout changed, the section was renumbered, or the slice is wrong)")
    stop = next((i for i, n in heads if n == end_before and i > first[0]), None)
    if stop is None:
        raise ValueError(f"heading {end_before} does not follow section {start} on the page: "
                         f"the slice would be a guess")
    cut = lines[first[0]:stop]
    while True:
        while cut and not cut[-1].strip():
            cut.pop()
        if len(cut) >= 2 and _DIVIDER.match(cut[-2]):
            del cut[-2:]
        elif cut and _DIVIDER.match(cut[-1]):
            cut.pop()
        else:
            break
    return "\n".join(cut) + "\n"


def _not_yet_in_effect(text: str, today: datetime.date | None = None) -> list[str]:
    """ISO dates after `today` that the page prints as an effective date (`Section effective January 1, 2027.`,
    `eff June 30, 2026`). The Code prints a section once, as it will read, when an act takes effect later."""
    today = today or datetime.date.today()
    out = []
    for mon, day, year in _EFFECTIVE_ON.findall(text):
        try:
            d = datetime.date(int(year), _MONTHS.index(mon.lower()) + 1, int(day))
        except ValueError:
            continue
        if d > today:
            out.append(d.isoformat())
    return out


# A rule or a proviso is cut from a PDF the General Assembly serves whole: the Code of Regulations chapter
# (`19\u2013445.2027.   Electronic Commerce.`, body headings start the line, the contents' entries are indented) and
# Part IB of the Appropriations Act (`   117.106. (GP: Statewide ...)`, with a running page header line).
_REG_HEADING = re.compile(r"^(\d+)[\u2013-](\d+\.\d+)\.\s+\S")
_PROVISO_HEADING = re.compile(r"^\s*(\d+[A-Z]?\.\d+)\.\s+(?:\(|DELETED\b)")
_PROVISO_HEADER = re.compile(r"^SECTION \d+[A-Z]? - \S+ - .+\s{2,}PAGE \d+\s*$|^\s*PAGE \d+\s*$")


def _pdf_heading(line: str, doc_type: str) -> str | None:
    if doc_type == "rule":
        m = _REG_HEADING.match(line)
        return f"{m.group(1)}-{m.group(2)}" if m else None
    m = _PROVISO_HEADING.match(line)
    return m.group(1) if m else None


def slice_pdf(text: str, doc_type: str, start: str, end_before: str) -> str:
    """The lines from the body heading of `start` to the line before the heading of `end_before`. Rules: headings
    start in column 0 (the contents lists every regulation indented). Provisos: the running page header line is
    dropped wherever it falls (it is page furniture, not part of any proviso), and the leading indent of the
    heading line is cut. Nothing else is changed."""
    lines = text.splitlines()
    heads = [(i, n) for i, l in enumerate(lines) if (n := _pdf_heading(l, doc_type))]
    first = [i for i, n in heads if n == start]
    if len(first) != 1:
        raise ValueError(f"{start} is printed {len(first)} times as a heading in the PDF "
                         f"(the layout changed, it was renumbered, or the slice is wrong)")
    stop = next((i for i, n in heads if n == end_before and i > first[0]), None)
    if stop is None:
        raise ValueError(f"heading {end_before} does not follow {start} in the PDF: the slice would be a guess")
    cut = lines[first[0]:stop]
    if doc_type != "rule":
        kept: list[str] = []
        skip_blank = False
        for l in cut:
            if _PROVISO_HEADER.match(l):                  # the page break's blank lines go with the header
                while kept and not kept[-1].strip():
                    kept.pop()
                skip_blank = True
            elif skip_blank and not l.strip():
                continue
            else:
                skip_blank = False
                kept.append(l)
        cut = kept
    cut[0] = cut[0].lstrip()
    while cut and not cut[-1].strip():
        cut.pop()
    return "\n".join(cut) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "pdf" and doc_type in ("statute", "rule") and slice_:
        return slice_pdf(pdf_to_text(raw), doc_type, slice_["section_start"], slice_["section_end_before"])
    if fmt == "html" and doc_type == "statute":
        text = statute_html_to_text(raw)
        if slice_:
            return slice_sections(text, slice_["section_start"], slice_["section_end_before"])
        return text
    return None


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "south-carolina":
        return False
    if src["doc_type"] == "executive_order":
        m = _ORDER_CITATION.search(src["citation"])
        first = next((l.strip() for l in text.splitlines() if l.strip()), "")
        h = _ORDER_HEADING.match(first)
        if not m or not h or h.group(1) != m.group(1):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: its heading line is not "
                             f"'Executive Order No. {m and m.group(1)}'")
        return True
    if src["doc_type"] == "rule" and src.get("slice"):
        return _check_slice_identity(src, text, text.splitlines(), what_is)
    if src["doc_type"] != "statute":
        return False
    lines = text.splitlines()
    if src.get("slice"):
        return _check_slice_identity(src, text, lines, what_is)
    m = _CITATION.search(src["citation"])
    if (not m or len(lines) < 2 or not re.match(rf"^Title {m.group('t')} - ", lines[0])
            or lines[1] != f"CHAPTER {m.group('c')}"):
        raise ValueError(f"{src['id']}: page is not {src['citation']} (title/chapter mismatch)")
    return True


_RULE_CITATION = re.compile(r"S\.C\. Code Regs\. (?P<a>\d+-\d+\.\d+)(?: to (?P<b>\d+-\d+\.\d+))?$")
_PROVISO_CITATION = re.compile(r".*, Proviso (?P<a>\d+[A-Z]?\.\d+)(?: to (?P<b>\d+[A-Z]?\.\d+))?$")


def _check_slice_identity(src, text, lines, what_is):
    """A slice is the cited one when it opens on the heading of the first cited section, its last heading is the last
    cited section, it is not a single section printed as repealed, deleted or recodified, and it prints no
    effective date after today (the text would not be the law in force)."""
    kind = ("rule" if src["doc_type"] == "rule" else "proviso" if src.get("format") == "pdf" else "section")
    cite = {"rule": _RULE_CITATION, "proviso": _PROVISO_CITATION, "section": _SECTION_CITATION}[kind]
    sl = src["slice"]
    m = cite.fullmatch(src["citation"])
    if kind == "section":
        heads = [x.group(1) for l in lines if (x := _SECTION_LINE.match(l))]
    else:
        heads = [n for l in lines if (n := _pdf_heading(l, src["doc_type"]))]
    if not m or not heads:
        raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: no usable citation or no section text")
    first, last = m.group("a"), m.group("b") or m.group("a")
    if (sl.get("section_start") != first or heads[0] != first or heads[-1] != last
            or (kind == "section" and not _SECTION_LINE.match(lines[0]))
            or (kind != "section" and _pdf_heading(lines[0], src["doc_type"]) != first)):
        raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: the slice opens on {heads[0]!r} and its "
                         f"last heading is {heads[-1]!r}")
    if later := _not_yet_in_effect(text):
        raise ValueError(f"{src['id']}: {what_is} prints an effective date after today "
                         f"({', '.join(sorted(set(later)))}): its text is not shown to be the law in force")
    if not m.group("b") and re.match(r"(Repealed|Recodified|DELETED)\b", re.sub(r"^(SECTION )?\S+?\.\s+", "", lines[0])):
        raise ValueError(f"{src['id']}: {src['citation']} is printed as repealed, deleted or recodified: not in force")
    return True


def notes(src, fmt, text):
    if src["jurisdiction"] != "south-carolina":
        return None
    if src["doc_type"] == "statute" and src.get("slice"):
        sl = src["slice"]
        title, chapter = sl["section_start"].split("-")[:2]
        return (f"Text taken from the General Assembly's Code of Laws page for Title {title}, Chapter {chapter} (the "
                f"unannotated code), which serves the whole chapter; this document is the sections from the heading of "
                f"section {sl['section_start']} to the line before the heading of section {sl['section_end_before']}, "
                f"as the page prints them: each section's number and caption line and paragraphs with its history "
                f"line, one line per paragraph, with editor's, code commissioner's and effect-of-amendment notes as "
                f"the page prints them. The chapter's other sections, the title and chapter lines, menus, scripts, "
                f"breadcrumb and footer are not part of it.")
    if src["doc_type"] == "statute":
        return ("Text taken from the General Assembly's Code of Laws page for the chapter (the unannotated "
                "code): the title line, the chapter number and name, article headings, then each section's number and "
                "caption line and paragraphs with its history line, one line per paragraph, with editor's, code "
                "commissioner's and effect-of-amendment notes as the page prints them between sections. A blank "
                "line precedes each article and section heading. The page's menus, scripts, breadcrumb and footer "
                "removed. Sections printed as repealed or reserved keep their line as published.")
    return None


# ---- printed dates and versions (the Department of Administration's PDFs) --------------------------------------

_DAY_MON_YEAR = re.compile(r"^\s*effective:\s*(\d{1,2})-([A-Za-z]{3})-(\d{4})\s*$", re.I | re.M)
_ABBREV = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")
_MONTH_ONLY = re.compile(r"^\s*Effective\s+(\d{1,2}/\d{4})\s*$", re.M)
_COVER_VERSION = re.compile(r"^\s*((?:version:?\s*\d+(?:\.\d+)*)|(?:V\.\d+(?:\.\d+)*\s*\(\d{2}\.\d{2}\.\d{2,4}\)))\s*$",
                            re.I)
_COVER_LINES = 20       # the version is a cover line; a "version 1.2" further in is the body talking about software


def effective_date(text, doc_type):
    """`effective: 01-Jul-2016` (SCDIS-501) is read here; every other label goes to the shared reader. A month
    with no day (`Effective 11/2018`, SWM-300) is not a date and stays empty."""
    m = _DAY_MON_YEAR.search(text)
    if m and m.group(2).lower() in _ABBREV:
        return f"{int(m.group(3)):04d}-{_ABBREV.index(m.group(2).lower()) + 1:02d}-{int(m.group(1)):02d}"
    return UNHANDLED


def source_version(text, doc_type, fmt):
    """The version line a policy prints among its first lines, as printed: `Version 2.5`, `version: 1.0`,
    `V.2.0 (07.15.15)`. None when it prints none (the shared reader then finds none for a PDF)."""
    cover = [l for l in text.splitlines() if l.strip()][:_COVER_LINES]
    for line in cover:
        m = _COVER_VERSION.match(line)
        if m:
            return re.sub(r"\s+", " ", m.group(1))
    return None


def _pdf_slice_notes(src) -> str:
    """What a rule or proviso slice of a whole-file PDF is, said after the shared pdftotext note."""
    sl = src["slice"]
    if src["doc_type"] == "rule":
        return (f" The source is the General Assembly's Code of Regulations file for Chapter 19 (one PDF for the whole "
                f"chapter, the unannotated code); this document is regulation {sl['section_start']}, from its body "
                f"heading to the line before the heading of {sl['section_end_before']}, as the PDF prints it, with its "
                f"HISTORY line. The chapter's contents list and its other regulations are not part of it.")
    return (f" The source is Part IB (the provisos) of the FY 2026-27 General Appropriations Act, H. 5126 as ratified by "
            f"the General Assembly on August 11, 2026, which the General Assembly serves as one PDF; this document is "
            f"proviso {sl['section_start']}, from its heading to the line before the heading of proviso "
            f"{sl['section_end_before']}, as the PDF prints it. Unlike the rest of the PDF's text, the running page "
            f"header line (section, agency code and page number) is dropped, with the blank lines a page break leaves "
            f"around it, and the heading line's indent is cut. A proviso is temporary law for the fiscal year of the "
            f"Act ('the current fiscal year').")


def extra_notes(src, fmt, text, eff, version):
    notes = ""
    if src.get("slice") and fmt == "pdf":
        notes += _pdf_slice_notes(src)
    if src.get("text_layer") == "scanner-ocr":
        notes += (" The PDF is a page image made by an office scanner, and its text layer is the scanner's own OCR: "
                  "it has not been checked against the page. It renders the logo as stray characters and can drop "
                  "words (the signature block's 'South C' is missing), so a quotation from this text must be checked "
                  "against the PDF.")
    if m := _DAY_MON_YEAR.search(text):
        if eff:
            notes += f" effective_date is the date the cover prints as '{m.group(0).strip()}'."
    elif (m := _MONTH_ONLY.search(text)) and not eff:
        notes += (f" The document prints 'Effective {m.group(1)}', a month with no day, so effective_date is left "
                  f"empty.")
    if version:
        notes += " source_version is the version line the document prints on its cover, as printed."
    return notes
