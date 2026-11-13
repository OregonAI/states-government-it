"""Hawaii: the Legislature's current statutes (`data.capitol.hawaii.gov/hrscurrent/`, one Word-made HTML file per
section) and the pages of the Office of Enterprise Technology Services' policy library that carry the instrument as
a web table (ETS Doc No. 508.01). Hooks are described in src/states/__init__.py.

A section file is page furniture around one `<div class="WordSection1">`: the section number and catch line (in bold
runs, so the number can arrive split across tags: `§</b><b>27G-</b><b>3`), then one `<p>` per paragraph, each wrapped
at about 80 columns by the Word export, then empty `&nbsp;` paragraphs. The Previous/Next links and the analytics
script follow the block and are dropped with the rest of the page. A section is one document: the seed list names the
sections of chapters 27, 27G, 94, 103D, 128B, 487J, 487N and 487R it holds (chapters 94 and 103D are outside the IT chapters:
one section of each whose own focus is IT governance, by the owner decision of 2026-11-13); the PDFs of the library need nothing here."""
from __future__ import annotations

import html
import re

_SECTION_BLOCK = re.compile(r'<div class="WordSection1">(.*?)</div>', re.S)
_PARAGRAPH = re.compile(r"<p\b[^>]*>(.*?)</p>", re.S)
_WP_BLOCK = re.compile(r'<div class="primary-content">(.*?)<!-- #content -->', re.S)
_WP_TITLE = re.compile(r'<div class="pagetitle">\s*<h2>(.*?)</h2>', re.S)
_ROW = re.compile(r"<tr\b[^>]*>(.*?)</tr>", re.S)
_CELL = re.compile(r"<t[hd]\b[^>]*>(.*?)</t[hd]>", re.S)
_BREAK = re.compile(r"<br\s*/?>", re.I)
_TAG = re.compile(r"<[^>]+>")
_SECTION_NO = re.compile(r"^\W*§\s*(\d+[A-Z]?)\s*-\s*(\d+(?:\.\d+)?)")
_CITE = re.compile(r"^Hawaii Revised Statutes section (\d+[A-Z]?-\d+(?:\.\d+)?)$")


def _clean(fragment: str) -> str:
    """Tags dropped without inventing spaces (the Word export splits one word across bold runs), entities decoded,
    the no-break spaces the export pads with turned into spaces, whitespace collapsed."""
    text = html.unescape(_TAG.sub("", fragment)).replace("\xa0", " ")
    return " ".join(text.split())


def section_html_to_text(raw: bytes) -> str:
    """One HRS section file to text: one line per non-empty paragraph, the Word line wraps joined."""
    page = raw.decode("utf-8", errors="replace").lstrip("﻿")
    block = _SECTION_BLOCK.search(page)
    lines = [l for p in _PARAGRAPH.findall(block.group(1) if block else "") if (l := _clean(_BREAK.sub(" ", p)))]
    if not lines or "§" not in lines[0] and not any("§" in l for l in lines[:2]):
        raise ValueError("no statute text: the page has no WordSection1 block with a section heading "
                         "(the layout changed, or this is not an HRS section file)")
    return "\n".join(lines) + "\n"


def library_page_to_text(raw: bytes) -> str:
    """An ETS library page to text: the page title, each paragraph (a `<br>` is a line break) and each table row as
    its cells joined by ` | ` (a cell's own line breaks by `; `). A paragraph that is only a link is navigation."""
    page = raw.decode("utf-8", errors="replace").lstrip("﻿")
    block, title = _WP_BLOCK.search(page), _WP_TITLE.search(page)
    if not block or not title:
        raise ValueError("no library text: the page has no primary-content block with a title")
    body = block.group(1)
    lines = [_clean(title.group(1))]
    for chunk in re.split(r"(<table\b.*?</table>)", body, flags=re.S):
        if chunk.startswith("<table"):
            for row in _ROW.findall(chunk):
                cells = ["; ".join(c for c in (_clean(x) for x in _BREAK.split(cell)) if c) for cell in _CELL.findall(row)]
                lines.append(" | ".join(cells).strip())
            continue
        for p in _PARAGRAPH.findall(chunk):
            if re.fullmatch(r"\s*<a\b[^>]*>[^<]*</a>\s*", p):
                continue
            lines += [l for l in (_clean(x) for x in _BREAK.split(p)) if l]
    return "\n".join(lines) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt != "html":
        return None
    if doc_type == "statute":
        return section_html_to_text(raw)
    if doc_type in ("policy", "standard") and host == "ets.hawaii.gov":
        return library_page_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "hawaii" or src["doc_type"] != "statute":
        return False
    cite = _CITE.match(src["citation"])
    first = next((l for l in text.splitlines() if "§" in l), "")
    printed = _SECTION_NO.match(first)
    if not cite or not printed or f"{printed.group(1)}-{printed.group(2)}" != cite.group(1):
        raise ValueError(f"{src['id']}: {what_is} is not {src['citation']} (section heading mismatch)")
    return True


def notes(src, fmt, text):
    if src["jurisdiction"] != "hawaii" or fmt != "html":
        return None
    if src["doc_type"] == "statute":
        return ("Text taken from the section's own file in the Legislature's current Hawaii Revised Statutes "
                "(data.capitol.hawaii.gov/hrscurrent/): the section number, catch line and text, one line per "
                "paragraph, with the History line and any Note or Revision Note the file prints under it. Square "
                "brackets around a number or heading are kept as the file prints them. The file's Previous and "
                "Next links and page script are removed; the Word export's line wraps are joined. The Legislature's "
                "hrscurrent compilation is dated January 2026 (its directory listings show 1/5/2026 to 1/6/2026), before "
                "the 2026 session laws: amendments made by 2026 acts are not reflected until the Legislature "
                "republishes the section.")
    return ("Text taken from the library page the Office of Enterprise Technology Services lists for this document: "
            "the page title, the header block and each table row (cells separated by ' | '). The page's menus, "
            "footer and the link to a PDF copy are removed.")
