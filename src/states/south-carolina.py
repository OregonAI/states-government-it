"""South Carolina: the General Assembly's Code of Laws pages. Hooks are described in src/states/__init__.py.

Statutes are served one chapter per page (`/code/t<title>c<chapter>.php`, the link the General Assembly's title
pages print): a PHP page whose law sits in `<div id="contentsection">`, written as lines separated by `<br />`:
the title line, the chapter number and name, article number and name lines, then each section as a bold
`SECTION n-n-n.` line, its caption, its paragraphs and a `HISTORY:` line, with editor's, code commissioner's and
amendment notes between sections. The page declares ISO-8859-1 but is UTF-8 (a byte order mark leads it).
Menus, scripts, the breadcrumb and the footer sit outside the content section. PDFs and Word files are shared; the Governor's orders print their heading as `Executive Order No. 2017-08`
(the default check looks for the words without `No.`), so the hook reads the heading line."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line
from src.states import UNHANDLED

_START = '<div id="contentsection">'
_END = "<!-- mainwidepanel -->"
_HEADING = re.compile(r"^(SECTION \d+-\d+-\d+(?:\.\d+)?\.(?: |$)|ARTICLE \d+\w*$|SUBARTICLE \d+\w*$)")
_ORDER_HEADING = re.compile(r"^executive\s+order\s+(?:no\.?)?\s*(\d{4}-\d+)\s*$", re.I)
_ORDER_CITATION = re.compile(r"Executive Order No\. (\d{4}-\d+)$")
_CITATION = re.compile(r"Title (?P<t>\d+\w*), Chapter (?P<c>\d+\w*)$")


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


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute":
        return statute_html_to_text(raw)
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
    if src["doc_type"] != "statute":
        return False
    m = _CITATION.search(src["citation"])
    lines = text.splitlines()
    if (not m or len(lines) < 2 or not re.match(rf"^Title {m.group('t')} - ", lines[0])
            or lines[1] != f"CHAPTER {m.group('c')}"):
        raise ValueError(f"{src['id']}: page is not {src['citation']} (title/chapter mismatch)")
    return True


def notes(src, fmt, text):
    if src["jurisdiction"] != "south-carolina":
        return None
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


def extra_notes(src, fmt, text, eff, version):
    notes = ""
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
