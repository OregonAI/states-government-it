"""Texas: the Legislature's statute pages. Hooks are described in src/states/__init__.py.

Statutes are served one chapter per static page (`<code>.<chapter>.htm`, `tcss.legis.texas.gov` and
`statutes.capitol.texas.gov`): the code, title, subtitle and chapter lines, then each section as a `<p>`
whose bold link carries `Sec. n.  CAPTION.` followed by its first paragraph, then the subdivisions and
the session-law history line, each a `<p>`. DIR's policy library serves PDFs and Word files, which the
shared readers handle; the Administrative Code has no static source (see the seed list)."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line
from src.states import UNHANDLED

_CHAPTER_LINE = re.compile(r"^CHAPTER (\w+)\.\s")


def statute_html_to_text(raw: bytes) -> str:
    """One chapter page to text: one line per source paragraph, tags, the inline style sheet, anchors and links
    removed (the link text is the section number and caption and stays), runs of spaces squeezed to one, and a blank
    line before each section and each subchapter heading. Nothing inside a section is dropped: the history line,
    bracketed notes and "Text of subsection as amended by" lines are law as published."""
    page = raw.decode("utf-8", errors="replace").lstrip("﻿")
    body = page[page.lower().find("<body"):]
    out: list[str] = []
    for p in re.findall(r"<p\b[^>]*>(.*?)</p>", body, flags=re.S | re.I):
        line = _clean_line(re.sub(r"<[^>]+>", "", p))
        if not line:
            continue                                   # the empty anchor paragraphs before each section
        if out and re.match(r"^(Sec\. \S+|SUBCHAPTER \S+|ARTICLE \S+)", line):
            out.append("")
        out.append(line)
    if not any(_CHAPTER_LINE.match(l) for l in out) or not any(l.startswith("Sec. ") for l in out):
        raise ValueError("no statute text: the page has no chapter heading and sections (the layout changed, "
                         "or this is not a chapter page)")
    return "\n".join(out) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute":
        return statute_html_to_text(raw)
    return None


_CITE = re.compile(r"^(?P<code>.+?) chapter (?P<ch>\w+)$")


def check_identity(src, text, what_is):
    if src["doc_type"] != "statute" or src["jurisdiction"] != "texas":
        return False
    m = _CITE.match(src["citation"])
    lines = text.splitlines()
    chapter = next((_CHAPTER_LINE.match(l).group(1) for l in lines[:8] if _CHAPTER_LINE.match(l)), None)
    code = lines[0] if lines else ""
    if not m or chapter != m.group("ch") or code.casefold() != m.group("code").casefold():
        raise ValueError(f"{src['id']}: page is not {src['citation']} (code or chapter mismatch)")
    return True


_MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December")
_ORDINAL_DATE = re.compile(rf"Effective Date:\s*({'|'.join(_MONTHS)})\s+(\d{{1,2}})(?:st|nd|rd|th),\s+(\d{{4}})")


def effective_date(text, doc_type):
    """DIR's Security Control Standards Catalog prints "Effective Date: August 28th, 2025"; the shared reader does
    not take an ordinal day suffix. Only that form, directly after the label, is read here; anything else is left
    to the shared reader."""
    m = _ORDINAL_DATE.search(text)
    if not m:
        return UNHANDLED
    mon, d, y = _MONTHS.index(m.group(1)) + 1, int(m.group(2)), int(m.group(3))
    return f"{y:04d}-{mon:02d}-{d:02d}" if 1 <= d <= 31 else UNHANDLED


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and src["jurisdiction"] == "texas":
        return ("Text taken from the Legislature's static chapter page: the code, title, subtitle and chapter lines, "
                "then each section's caption and paragraphs and its session-law history line, one line per paragraph. "
                "Anchors, links and the page's style sheet removed. A blank line precedes each section and each "
                "subchapter heading.")
    return None
