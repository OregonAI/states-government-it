"""Florida: the Legislature's chapter page (`leg.state.fl.us/statutes/`, the "View Entire Chapter" link). Hooks are
described in src/states/__init__.py.

A section outside chapter 282 is read from its own page (`.../Sections/0112.22.html`), which wraps one `<div
class="Section">` in the same menus and footer; no slice is needed.

The page wraps the chapter in the site's menus and footer; the law is one `<div class="Chapters">` block: the chapter
heading, a Part contents list and a section contents list per Part (both repeat what follows and are dropped), then for
each Part its heading and each section as a `<div class="Section">` (number, catch line, an em dash, the text or its
subsections, paragraphs and subparagraphs as nested divs, the History line, and editors' Notes). The pages for rule
text (flrules.org) are legacy Word files and are stubs in the seed list; nothing here reads them."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line

_EDITION = re.compile(r"<h2>\s*The (\d{4}) Florida Statutes")
_TITLE = re.compile(r"<a href=\"[^\"]*Display_Index[^\"]*\">(Title [A-Z]+)</a></b><br>([^<]+)</center>")
_BREAK_BEFORE = re.compile(r'<div class="(ChapterTitle|PartTitle|Section|Subsection|Paragraph|SubParagraph|'
                           r'SubSubParagraph|SubSubSubParagraph|History|Note)">')
_CHAPTER_LINE = re.compile(r"^CHAPTER (\w+) ")
# a section's own page prints the chapter as a link and its title after it, not as a heading line
_PAGE_CHAPTER = re.compile(r"Display_Statute[^\"]*ContentsIndex\.html\">Chapter (\w+)</a>\s*</b><br>([^<]+)</center>")
_SECTION_LINE = re.compile(r"^(\d+\.\d+\w*) \S.* —(?: |$)")


def _drop_divs(html: str, cls: str) -> str:
    """Remove every `<div class="cls">...</div>` including nested divs."""
    start_tag = f'<div class="{cls}">'
    while (i := html.find(start_tag)) != -1:
        depth, pos = 0, i
        for m in re.finditer(r"<div\b|</div>", html[i:]):
            depth += 1 if m.group(0) != "</div>" else -1
            if depth == 0:
                pos = i + m.end()
                break
        else:
            raise ValueError("unbalanced div in the statute page")
        html = html[:i] + html[pos:]
    return html


def statute_html_to_text(raw: bytes) -> str:
    """One chapter page to text: the edition and title lines the page prints above the chapter, then one line per
    heading, section, subsection, paragraph, subparagraph, History line and Note, with a blank line before each section
    and each Part heading. A footnote marker is written `[n]` where the page prints it as a superscript. The two
    contents lists are dropped (they repeat the section numbers and catch lines that follow)."""
    page = raw.decode("utf-8", errors="replace").lstrip("﻿")
    start = page.find('<div class="Chapters">')
    one_section = start == -1 and page.count('<div class="Section">') == 1
    if one_section:                     # the page of a single section: the section block is the body
        start = page.find('<div class="Section">')
    if start == -1 or 'class="Section"' not in page:
        raise ValueError("no statute text: the page has no chapter block with sections (the layout changed, "
                         "or this is not a chapter page)")
    edition, title = _EDITION.search(page), _TITLE.search(page)
    body = page[start:page.find("</body>", start)]
    for cls in ("PartIndex", "CatchlineIndex"):
        body = _drop_divs(body, cls)
    body = re.sub(r"(</sup>)(<span class=\"NoteTitle\")", r"\1 \2", body)
    body = re.sub(r"<sup>\s*<a\b[^>]*>(\w+)</a>\s*</sup>", r"[\1]", body)
    body = re.sub(r'<span class="EmDash">.*?</span>', " — ", body)
    body = re.sub(r"<br\s*/?>", " ", body).replace("</div>", " </div>")
    body = _BREAK_BEFORE.sub(lambda m: ("\n\n" if m.group(1) in ("Section", "PartTitle") else "\n") + m.group(0), body)
    out: list[str] = []
    if edition:
        out.append(f"The {edition.group(1)} Florida Statutes")
    if title:
        out.append(f"{title.group(1)} {_clean_line(title.group(2))}")
    if one_section:
        chap = _PAGE_CHAPTER.search(page)
        if not chap:
            raise ValueError("no statute text: the section page does not name its chapter (the layout changed)")
        out.append(f"CHAPTER {chap.group(1)} {_clean_line(chap.group(2))}")
    for chunk in body.split("\n"):
        line = _clean_line(re.sub(r"<[^>]+>", "", chunk))
        if line:
            out.append(line)
        elif out and out[-1] != "":
            out.append("")
    # a blank line is wanted only before a Section or Part heading: the splits above insert "\n\n" there
    while out and out[-1] == "":
        out.pop()
    if not any(_CHAPTER_LINE.match(l) for l in out):
        raise ValueError("no statute text: no chapter heading line")
    return "\n".join(out) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute":
        return statute_html_to_text(raw)
    return None


_CITE = re.compile(r"^Chapter (\w+), Florida Statutes$")
_SECTION_CITE = re.compile(r"^Section (\d+\.\d+\w*), Florida Statutes$")


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "florida":
        return False
    if src["doc_type"] == "executive_order":
        # The Governor's orders print "EXECUTIVE ORDER NUMBER 22-216"; the shared check looks for "Executive Order 22-216".
        want = src.get("identity_text")
        if not want or " ".join(want.split()).casefold() not in " ".join(text.split()).casefold():
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {want!r} does not appear in its text")
        return True
    if src["doc_type"] != "statute":
        return False
    sec = _SECTION_CITE.match(src["citation"])
    if sec:                              # a section's own page: exactly one section, the cited one
        found = [m.group(1) for l in text.splitlines() if (m := _SECTION_LINE.match(l))]
        if found != [sec.group(1)]:
            raise ValueError(f"{src['id']}: page is not {src['citation']} (it holds sections {found})")
        return True
    m = _CITE.match(src["citation"])
    chapter = next((_CHAPTER_LINE.match(l).group(1) for l in text.splitlines()[:8] if _CHAPTER_LINE.match(l)), None)
    if not m or chapter != m.group(1):
        raise ValueError(f"{src['id']}: page is not {src['citation']} (chapter heading mismatch)")
    return True


def source_version(text, doc_type, fmt):
    if doc_type == "statute":
        m = re.match(r"The (\d{4}) Florida Statutes$", text.split("\n", 1)[0])
        if m:
            return f"{m.group(1)} Florida Statutes"
    return None


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and src["jurisdiction"] == "florida" and _SECTION_CITE.match(src["citation"]):
        return ("Text taken from the Legislature's page for this one section of the current Florida Statutes (the "
                "Legislature serves each section on its own page): the edition and title lines, the chapter heading, "
                "then the section's number, catch line and text, one line per subsection, paragraph and subparagraph, "
                "with its History line. The page's menus and footer are removed; a footnote marker the page prints as "
                "a superscript is written [n]. Only this section is mirrored; the rest of its chapter is not.")
    if src["doc_type"] == "statute" and src["jurisdiction"] == "florida":
        return ("Text taken from the Legislature's \"View Entire Chapter\" page for the current Florida Statutes: the "
                "edition and title lines, the chapter and Part headings, then each section's number, catch line and "
                "text, one line per subsection, paragraph and subparagraph, with its History line and any editors' "
                "Note. The page's menus and footer and its two contents lists are removed; a footnote marker the page "
                "prints as a superscript is written [n]. A blank line precedes each section and each Part heading.")
    return None
