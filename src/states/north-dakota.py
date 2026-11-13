"""North Dakota: the Legislative Council's chapter PDFs (Century Code, Administrative Code), NDIT's policy PDFs and the
Governor's order PDFs, all of which the shared readers handle. The only hook is the identity check: the shared one
reads the chapter number as its first digits (54 for 54-59.1), and its order check would accept a mention of the
number. Hooks are described in src/states/__init__.py.

A statute document may be one section or a run of sections of a chapter PDF (`slice: {section_start,
section_end_before}`, the printed section numbers): `to_text` cuts it, `check_identity` confirms it.

A chapter PDF opens with `CHAPTER 54-59` and the chapter title on the next line; an Administrative Code chapter PDF
carries `CHAPTER 113-02-01` after its article contents. An order opens with its own `EXECUTIVE ORDER 2026-06` line."""
from __future__ import annotations

import re

from src.ingest_common import pdf_to_text

_CHAPTER = re.compile(r"^\s*CHAPTER ([0-9.\-]+)\s*$", re.M)
_RISK_MATRIX = re.compile(r"^\s*AI Risk Matrix\s*$", re.M)
_ORDER = re.compile(r"^\s*EXECUTIVE ORDER ([0-9.\-]+)\s*$", re.M | re.I)


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "north-dakota":
        return False
    kind = src["doc_type"]
    if kind == "statute" and src.get("slice"):
        return _check_slice(src, text, what_is)
    if kind in ("statute", "rule"):
        cite = re.search(r"([0-9][0-9.\-]*[0-9])\s*$", src["citation"])
        if not cite or cite.group(1) not in _CHAPTER.findall(text):
            raise ValueError(f"{src['id']}: {what_is} is not {src['citation']} (no heading line "
                             f"'CHAPTER {cite and cite.group(1)}')")
        return True
    if kind == "policy":
        # The policy PDFs print Created/Revised/Reviewed, then the title centred on a line of its own. The shared
        # check only looks for the title anywhere, and the policies name one another.
        head = "\n".join(text.splitlines()[:15])
        if not re.search(rf"^\s*{re.escape(src['title'])}\s*$", head, re.M):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: no heading line "
                             f"{src['title']!r} at the top of its text")
        return True
    if kind == "executive_order":
        number = re.search(r"\d{4}-\d{2}(?:\.\d+)?", src["citation"])
        if not number or number.group(0) not in _ORDER.findall(text):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: no heading line "
                             f"'Executive Order {number and number.group(0)}' in its text")
        return True
    return False


def _slice_note(src):
    sl = src["slice"]
    chapter = sl["section_start"].rsplit("-", 1)[0]
    return (f" The source is the Legislative Council's file for the whole of chapter {chapter} (the PDF is the "
            f"snapshot); this document is the section or sections from the heading of {sl['section_start']} to the "
            f"line before the heading of {sl['section_end_before']}, as the PDF prints them. The page footer lines "
            f"('Page No. n') of the pages the text crosses are not copied.")


def extra_notes(src, fmt, text, eff, version):
    """A slice names itself. The AI Guideline's page 6 is the 'AI Risk Matrix', a picture (563 x 459, no text layer) under a heading that
    does have text. pdftotext reads only the heading and the footnote, so the matrix's wording is not in the text."""
    if src["doc_type"] == "statute" and src.get("slice"):
        return _slice_note(src)
    if src["doc_type"] == "policy" and fmt == "pdf" and _RISK_MATRIX.search(text):
        return (" Page 6 of the PDF carries the 'AI Risk Matrix' as an image (a matrix of use cases by risk of impact "
                "and risk of data breach) with no text layer: the heading and the note beneath it are in the text, "
                "the matrix's own wording is not mirrored here. Read it at the source URL.")
    return ""


# ---- statutes: sections cut from a Century Code chapter PDF -----------------------------------------------

_SECTION = r"\d+(?:\.\d+)?-\d+(?:\.\d+)?-\d+(?:\.\d+)?"
_HEADING = re.compile(rf"^\s*({_SECTION})\.\s")
_FOOTER = re.compile(r"^\s*Page No\. \d+\s*$")
_CITED = re.compile(rf"N\.D\.C\.C\. sections? ({_SECTION})(?: to ({_SECTION}))?")
_DEAD = re.compile(r"^\s*(Repealed|Expired|Superseded|Obsolete)\b", re.I)


def _headings(lines):
    """(line index, section number) of every section heading: a line that begins `23-12-19. `. The heading may wrap
    onto the next line; nothing else in a chapter PDF starts a line with a section number and a full stop."""
    return [(i, m.group(1)) for i, line in enumerate(lines) if (m := _HEADING.match(line))]


def slice_chapter(text, start, end_before):
    """The lines from the heading of section `start` to the line before the heading of `end_before` (which follows it),
    with the page footers (`Page No. 8`) of the pages the slice crosses removed: they are page furniture, not text of
    the provision."""
    lines = text.splitlines()
    heads = _headings(lines)
    first = [i for i, num in heads if num == start]
    if len(first) != 1:
        raise ValueError(f"section {start} is printed {len(first)} times as a heading in the chapter PDF "
                         f"(the layout changed, the section was renumbered or repealed, or the slice is wrong)")
    stop = next((i for i, num in heads if num == end_before and i > first[0]), None)
    if stop is None:
        raise ValueError(f"heading {end_before} does not follow section {start} in the chapter PDF: "
                         f"the slice would be a guess")
    cut = [line for line in lines[first[0]:stop] if not _FOOTER.match(line)]
    while cut and not cut[-1].strip():
        cut.pop()
    return "\n".join(cut) + "\n"


def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "pdf" and doc_type == "statute" and slice_:
        return slice_chapter(pdf_to_text(raw), slice_["section_start"], slice_["section_end_before"])
    return None


def _check_slice(src, text, what_is):
    """A slice is the cited section when it opens on the first cited heading, its last heading is the last cited one,
    and a single section is not a repeal or expiry notice."""
    cite = _CITED.fullmatch(src["citation"])
    lines = text.splitlines()
    heads = _headings(lines)
    first, last = (cite.group(1), cite.group(2) or cite.group(1)) if cite else (None, None)
    if (not cite or (src["slice"].get("section_start") != first) or not heads or heads[0] != (0, first)
            or heads[-1][1] != last):
        raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: the slice opens on "
                         f"{heads[0][1] if heads else None!r} and its last heading is "
                         f"{heads[-1][1] if heads else None!r}")
    if not cite.group(2) and any(_DEAD.match(line) for line in lines[1:3]):
        raise ValueError(f"{src['id']}: {src['citation']} is printed as repealed or expired: not in force")
    return True
