"""Vermont: the Legislature's full-chapter statute pages (`legislature.vermont.gov/statutes/fullchapter/<title>/<chapter>`,
one GET per chapter), the vermont.gov portal's web policy page, and the identity a Governor's order prints in its own
heading. Everything else Vermont holds is PDF or Word, which the shared readers handle. Hooks are described in
src/states/__init__.py.

A chapter page wraps the law in menus, a sidebar and a footer. The law runs from the `statute-title` and
`statute-chapter` headings to the sidebar: a list of sections (each `<li><p></p><div>` with a bold `§ n. Caption` line
and one `<p>` per paragraph), and, in a chapter with subchapters, a heading line for each subchapter between them."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line, _decode

_BLOCK = re.compile(r"</?(?:div|p|h[1-6]|li|ul|ol|tr|table|section|article|br|dt|dd|dl)\b[^>]*>", re.I)
_SECTION_OPEN = re.compile(r"<li><p></p><div>")
_SPLIT = re.compile(r"[\x00\x01]")


def _lines(fragment: str, section_marker: bool = False) -> list[str]:
    fragment = re.sub(r"<!--.*?-->", "", fragment, flags=re.S)
    fragment = re.sub(r"<(script|style|svg|noscript)\b.*?</\1>", "", fragment, flags=re.S | re.I)
    if section_marker:
        fragment = _SECTION_OPEN.sub("\x01", fragment)
    fragment = _BLOCK.sub("\x00", fragment)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    out: list[str] = []
    for chunk in re.split(r"(?=\x01)", fragment):
        blank = chunk.startswith("\x01")
        for line in (_clean_line(c) for c in _SPLIT.split(chunk)):
            if line:
                if blank and out:
                    out.append("")
                blank = False
                out.append(line)
    return out


def statute_to_text(raw: bytes) -> str:
    """`Title 3: Executive`, `Chapter 069: Division of Artificial Intelligence`, then each section (a blank line, its
    `§ n. Caption`, one line per paragraph) and, where the chapter has them, `Subchapter 001: General Provisions`."""
    page = _decode(raw)
    title = re.search(r'<h2 class="statute-title">(.*?)</h2>', page, re.S)
    start = page.find('<h3 class="statute-chapter">')
    end = page.find('<div class="sidebar">', start)
    if not title or start < 0 or end < 0 or "§" not in page[start:end]:
        raise ValueError("no chapter text on the page: it has no statute-title, statute-chapter and sidebar "
                         "(the layout changed, or this is not a full-chapter page)")
    return "\n".join(_lines(title.group(0)) + _lines(page[start:end], section_marker=True)) + "\n"


def web_page_to_text(raw: bytes) -> str:
    """A vermont.gov page that is itself the policy: the content of `<main id="main-content">`, one line per block (the
    page heading first). The page's styles, the menus and the footer sit outside it or are dropped."""
    page = _decode(raw)
    start = page.find('<main id="main-content"')
    end = page.find("</main>", start)
    if start < 0 or end < 0:
        raise ValueError("vermont.gov page has no main content region: the layout changed")
    out = _lines(page[start:end])
    if len(out) < 8:
        raise ValueError("vermont.gov page has no content: the layout changed")
    return "\n".join(out) + "\n"


# ---- hooks (see src/states/__init__.py) ------------------------------------------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt != "html":
        return None
    if doc_type == "statute":
        return statute_to_text(raw)
    if doc_type == "policy":
        return web_page_to_text(raw)
    return None


_CITED_CHAPTER = re.compile(r"(\d+[A-Za-z]*) V\.S\.A\. chapter (\w+)", re.I)
_TEXT_HEADS = re.compile(r"^Title (\w+)\s*: .*\nChapter (\w+)\s*: ", re.M)
_EO_CITED = re.compile(r"\b(\d{2})-(\d{2})\b")
_EO_HEADING = re.compile(r"^\s*EXECUTIVE ORDER NO\.? (\d{1,2})-(\d{2})\s*$", re.I | re.M)


def _norm(label: str) -> str:
    return label.lstrip("0").casefold() or "0"


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "vermont":
        return False
    cite = src["citation"]
    if src["doc_type"] == "statute":
        want, got = _CITED_CHAPTER.search(cite), _TEXT_HEADS.match(text)
        if not want or not got or (_norm(want.group(1)), _norm(want.group(2))) != (_norm(got.group(1)), _norm(got.group(2))):
            raise ValueError(f"{src['id']}: page is not {cite} (title/chapter mismatch)")
        return True
    if src["doc_type"] == "executive_order":
        want, heading = _EO_CITED.search(cite), _EO_HEADING.search(text)
        if not want or not heading or (int(want.group(1)), int(want.group(2))) != (int(heading.group(1)), int(heading.group(2))):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: 'Executive Order {want and want.group(0)}' "
                             f"is not the order's own heading line (the file's is {heading and heading.group(0).strip()!r})")
        return True
    return False


def notes(src, fmt, text):
    if src["jurisdiction"] != "vermont" or fmt != "html":
        return None
    if src["doc_type"] == "statute":
        return ("Text taken from the full-chapter page on legislature.vermont.gov: the title and chapter headings, then "
                "each section as its `§ n. Caption` line and one line per paragraph (and a line for each subchapter "
                "heading). Menus, sidebar, scripts and footer removed. The Legislature says its Vermont Statutes Online "
                "is an unofficial copy of the Vermont Statutes Annotated, provided as a convenience.")
    return ("Text taken from the vermont.gov page: the content of its main region, one line per block. Styles, menus "
            "and footer removed.")
