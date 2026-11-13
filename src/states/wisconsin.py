"""Wisconsin: the Legislature's statute and administrative-code pages (docs.legis.wisconsin.gov).
Hooks are described in src/states/__init__.py.

A statute page is not one section: the site serves a window of neighbouring sections around the one
asked for. The page names the section it was asked for in its `<title>` ("Wisconsin Legislature: 16.971"),
and only the elements the page itself tags with that section are the text (a seed entry needs no `slice`,
which the shared seed check does not allow for this state). An administrative-code page is the whole chapter.

A section whose page is cut off by the end of the window (s. 16.61) is a slice of the Legislature's chapter PDF
(/document/statutes/16.pdf, one file per chapter, two columns): `slice: {section_start, section_end_before}`, the
printed numbers of the first section and of the section whose heading ends the slice. The PDF is read in column order
(not `-layout`), the page header, footer and running head are dropped, and a word hyphenated at a line end is joined."""
from __future__ import annotations

import re
import subprocess

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


# ---- statutes: one slice of the Legislature's chapter PDF ------------------------------------

_HEADING = re.compile(r"^(\d+\.\d+[a-z]*) [A-Z\u201c]")      # "16.611 State public records"; not "16.611 (2)" or "16.61;"
_PAGE_HEADER = re.compile(r"^Updated (2023-24|23-24) Wis\. Stats\.")
_FOOTER_1 = re.compile(r"^\d{4}-\d{2} Wisconsin Statutes updated through ")
_FOOTER_2 = re.compile(r"^after .*, are designated by NOTES\. \(Published \d{1,2}-\d{1,2}-\d{2}\)$")


def slice_headings(lines: list[str]) -> list[tuple[int, str]]:
    """(line index, section number) of every line that opens a section: a number, a space and a capital."""
    return [(i, m.group(1)) for i, line in enumerate(lines) if (m := _HEADING.match(line))]


def _chapter_pdf_lines(raw: bytes) -> tuple[list[str], str]:
    """The chapter PDF's body lines in reading order, with the page furniture removed, and the Legislature's
    certification line (the page footer, which is the same on every page)."""
    proc = subprocess.run(["pdftotext", "-", "-"], input=raw, capture_output=True, check=False)
    if proc.returncode != 0:
        raise ValueError("pdftotext could not read the Wisconsin statute chapter PDF")
    text = proc.stdout.decode("utf-8", "replace").replace("\f", "\n")
    lines = [_clean_line(l) for l in text.splitlines()]
    lines = [l for l in lines if l]
    title = next((lines[i + 1] for i, l in enumerate(lines[:-1]) if re.fullmatch(r"CHAPTER \d+[A-Z]?", l)), "")
    body, cert = [], ""
    for line in lines:
        if _FOOTER_1.match(line):
            cert = cert or line
        elif _FOOTER_2.match(line):
            if cert and not cert.endswith(")"):
                cert = f"{cert} {line}"
        elif (_PAGE_HEADER.match(line) or re.fullmatch(r"\d{1,3}", line) or re.fullmatch(r"\d+\.\d+[a-z]*", line)
              or (title and line == title)):
            continue
        else:
            body.append(line)
    return body, cert


def slice_chapter(raw: bytes, start: str, end_before: str) -> str:
    """The lines from the heading of section `start` to the line before the heading of `end_before`, then the
    certification line. Both headings must be there, once each as a heading, and in that order."""
    lines, cert = _chapter_pdf_lines(raw)
    heads = slice_headings(lines)
    first = [i for i, num in heads if num == start]
    if len(first) != 1:
        raise ValueError(f"section {start} is printed {len(first)} times as a heading in the chapter PDF "
                         "(the layout changed, the section was renumbered, or the slice is wrong)")
    stop = next((i for i, num in heads if num == end_before and i > first[0]), None)
    if stop is None:
        raise ValueError(f"heading {end_before} does not follow section {start} in the chapter PDF: "
                         "the slice would be a guess")
    out: list[str] = []
    for line in lines[first[0]:stop]:
        if out and re.search(r"[a-z]-$", out[-1]) and re.match(r"[a-z]", line):
            out[-1] = out[-1][:-1] + line           # a word hyphenated at the end of a line
        else:
            out.append(line)
    if not cert:
        raise ValueError("the Wisconsin chapter PDF prints no certification line: the layout changed")
    return "\n".join(out + [cert]) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "pdf" and doc_type == "statute" and slice_:
        return slice_chapter(raw, slice_["section_start"], slice_["section_end_before"])
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
    if src["doc_type"] == "statute" and fmt == "pdf":
        return ("Text taken from the Legislature's chapter PDF, cut to this section: from its heading to the line "
                "before the next section's heading, read in column order (pdftotext, not -layout). Page headers, "
                "footers and running heads removed, and a word hyphenated at the end of a line joined. The last "
                "line is the Legislature's own certification line for the edition. The Legislature's page for "
                "this section serves it only in part (the page ends inside the section), so the chapter PDF is "
                "the text of record.")
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
