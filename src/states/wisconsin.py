"""Wisconsin: the Legislature's statute and administrative-code pages (docs.legis.wisconsin.gov).
Hooks are described in src/states/__init__.py.

A statute page is not one section: the site serves a window of neighbouring sections around the one
asked for. The page names the section it was asked for in its `<title>` ("Wisconsin Legislature: 16.971"),
and only the elements the page itself tags with that section are the text (a seed entry needs no `slice`,
which the shared seed check does not allow for this state). An administrative-code page is the whole chapter."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line, _decode
from src.states import UNHANDLED

_SEGMENT = re.compile(r'(?=<div class="qs)')
_DATA_SECTION = re.compile(r'data-section="([^"]*)"')


_PAGE_FURNITURE = re.compile(r"<div class='navigation'|<div class=\"hidden\"|<div class=\"container\"")


def _line(html: str) -> str:
    """One element's text. The page prints a hidden reference label (a link or a span with class
    `reference`) in front of every element; it is not the law. Inline links stay in the sentence."""
    html = re.sub(r'<a class="reference"[^>]*>.*?</a>|<span class="reference">.*?</span>', "", html, flags=re.S)
    return _clean_line(re.sub(r"<[^>]+>", "", html))


def _document_region(page: str) -> str:
    start = page.find('id="document"')
    if start < 0:
        raise ValueError("Wisconsin Legislature page has no document region: the page layout changed")
    region = page[page.index(">", start) + 1:]
    ends = [at for at in (region.find(m) for m in ('<div id="tools"', '<div id="pulltab"', 'id="disclaimerFrame"'))
            if at >= 0]
    return region[:min(ends)] if ends else region      # what follows the text is the page's own footer


def _certification(page: str) -> str:
    """The Legislature's own line under every page: for statutes the edition and publication date,
    for the administrative code the publication statement."""
    at = page.find('id="disclaimerFrame"')
    if at < 0:
        return ""
    frame = page[page.index(">", at) + 1:]
    return _line(frame[:frame.find("<script")] if "<script" in frame else frame)


def requested_section(page: str) -> str:
    """The section a statute page was asked for, from its title. A page for a whole subchapter or
    chapter has no such title and is refused: it is a window of sections with no edges."""
    m = re.search(r"<title>Wisconsin Legislature: (\d+\.\d+[a-z]*)</title>", page)
    if not m:
        raise ValueError("Wisconsin statute page is not titled for one section: it is a window of sections")
    return m.group(1)


def _is_history(seg: str) -> bool:
    return seg.lstrip().startswith('<div class="qsnote_history"')


def _at_window_end(segments: list[str], section: str) -> bool:
    """The window is cut where its element budget runs out, in the middle of a section as readily as
    between two: the requested section is then the last thing on the page and may be incomplete."""
    tag = _DATA_SECTION.search(segments[-1][:700]) if segments else None
    return bool(tag and tag.group(1) == section)


def legis_html_to_text(raw: bytes, doc_type: str) -> str:
    page = _decode(raw)
    region = _document_region(page)
    section = requested_section(page) if doc_type == "statute" else None
    lines = []
    segments = [_PAGE_FURNITURE.split(seg)[0] for seg in _SEGMENT.split(region)[1:]]
    for seg in segments:       # the last element runs on into the page's navigation and hidden metadata
        tag = _DATA_SECTION.search(seg[:700])
        if section and (not tag or tag.group(1) != section):
            continue
        if not section and doc_type == "rule" and "pulltab" in seg[:60]:
            continue
        if line := _line(seg):
            lines.append(line)
    if not lines or (section and not lines[0].startswith(f"{section} ")):
        raise ValueError(f"Wisconsin page does not hold section {section!r} as a section of its own"
                         if section else "Wisconsin page holds no text in its document region")
    if section and _at_window_end(segments, section) and not _is_history(segments[-1]):
        raise ValueError(f"Wisconsin statute page for {section!r} ends at the end of the window, inside the "
                         "section (no history line): the page holds only part of the section")
    if cert := _certification(page):
        lines.append(cert)
    return "\n".join(lines) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type in ("statute", "rule"):
        return legis_html_to_text(raw, doc_type)
    return None


def check_identity(src, text, what_is):
    cite = src["citation"]
    if src["doc_type"] == "statute":
        number = re.search(r"s\.\s*([\d.]+)\s*$", cite)
        if not number or not text.startswith(f"{number.group(1)} "):
            raise ValueError(f"{src['id']}: {what_is} is not {cite} (section number mismatch)")
        return True
    if src["doc_type"] == "rule":
        chapter = re.search(r"ch\.\s*(Adm \d+)\s*$", cite)
        if not chapter or not text.startswith(f"Chapter {chapter.group(1)}\n"):
            raise ValueError(f"{src['id']}: {what_is} is not {cite} (chapter mismatch)")
        title = re.sub(r"^Chapter Adm \d+\s*-\s*", "", src["title"])    # the page prints the title in capitals
        if " ".join(title.upper().split()) not in " ".join(text.upper().split()):
            raise ValueError(f"{src['id']}: {what_is} does not carry the seed title {title!r}")
        return True
    return False


def effective_date(text, doc_type):
    return None if doc_type in ("statute", "rule") else UNHANDLED


_REVISION_DATE = re.compile(r"^\s*Revision Date:\s*(\d{1,2}/\d{1,2}/\d{4})\s*$", re.M)
_ISSUANCE_ROW = re.compile(r"^\s*(\d{1,2}-\d{1,2}-\d{2})\s{2,}(\d+(?:\.\d+)+)\s*(\[DRAFT\])?\s{2,}\S", re.M)


def source_version(text, doc_type, fmt):
    """The Legislature's publication date for a statute; a DET policy or standard prints a revision
    date on its cover, or ends with an issuance table whose last row is the current version."""
    if doc_type == "statute":
        m = re.search(r"\(Published (\d{1,2}-\d{1,2}-\d{2})\)\s*$", text.rstrip())
        if m:
            return f"Published {m.group(1)}"
    if doc_type in ("policy", "standard") and fmt == "pdf":
        if m := _REVISION_DATE.search(text):
            return f"Revision Date {m.group(1)}"
        rows = _ISSUANCE_ROW.findall(text)
        if rows:
            date, version, draft = rows[-1]
            return f"Version {version}{' [DRAFT]' if draft else ''}, issued {date}"
    return None


def notes(src, fmt, text):
    if src["doc_type"] == "statute":
        return ("Text taken from the Legislature's statute page. The page serves a window of neighbouring "
                f"sections; only the elements it tags as the section it was asked for are kept, one line per "
                "element: the section heading, each subsection and paragraph, the history line and any "
                "annotations. Site menu, reference labels and the other sections of the window removed. The "
                "last line is the Legislature's own certification line for the edition.")
    if src["doc_type"] == "rule":
        return ("Text taken from the Legislature's administrative-code chapter page: chapter number and "
                "title, the chapter's section list, each section with its history line and any notes, one line "
                "per element, then the Legislature's publication statement. Site menu and reference labels removed.")
    return None
