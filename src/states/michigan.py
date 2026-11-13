"""Michigan: the executive orders the Legislature archives at www.legislature.mi.gov/Home/GetObject (older
orders are Word- or Vignette-made HTML pages; newer ones PDFs, which the shared reader handles) and the identity
checks for those orders and for the per-act statute PDFs (www.legislature.mi.gov/documents/mcl/pdf/). Hooks are
described in src/states/__init__.py."""
from __future__ import annotations

import datetime
import html as html_mod
import re

from src.ingest_common import pdf_to_text

_BLOCK = re.compile(r"</?(?:p|div|br|tr|td|th|table|tbody|hr|h[1-6]|li|ul|ol|blockquote|center)\b[^>]*>", re.I)
_FURNITURE = (re.compile(r"^www\.michigan\.gov$", re.I),
              re.compile(r"^\(To Print: use your browser's print function\)$", re.I),
              re.compile(r"^Copyright © \d{4} State of Michigan$", re.I))


def _decode(raw: bytes) -> str:
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252", errors="replace")


def eo_html_to_text(raw: bytes) -> str:
    """An executive order as the Legislature archives it: a Word-exported page or a Vignette print page. The
    head (title, style block, scripts), comments and tags go; each paragraph, heading line, line break and table
    cell is one line, wrapped source lines are joined, entities are decoded. The print bar (`www.michigan.gov`,
    `(To Print: ...)`) and the `Copyright (c) <year> State of Michigan` footer are page furniture and go; the
    page's `Release Date` and `Last Update` lines stay."""
    page = _decode(raw)
    page = re.sub(r"<!--.*?-->", "", page, flags=re.S)
    page = re.sub(r"<(head|script|style)\b.*?</\1>", "", page, flags=re.S | re.I)
    page = _BLOCK.sub("\x00", page)                 # a block tag ends a line; a newline in the source does not
    page = re.sub(r"<[^>]+>", "", page)
    page = html_mod.unescape(page).replace("\xa0", " ")
    out = []
    for line in page.split("\x00"):
        line = " ".join(line.split())
        if line and not any(p.match(line) for p in _FURNITURE):
            out.append(line)
    return "\n".join(out) + "\n"


# ---- statutes: a slice of an act PDF, and one MCL section page --------------------------------

_HEADING = re.compile(r"^\s*(\d+\.\d+[a-z]*)\s+\S")
_SEC_LINE = re.compile(r"^\s*Sec\.\s+\d+[a-z]*\.")
# the page furniture the Legislature's PDF prints at each page break: the render date and page count, the
# "complete through" banner and the courtesy line (the render date changes on every download)
_PDF_FURNITURE = (re.compile(r"^\s*Rendered \w+, \w+ \d{1,2}, \d{4}\s+Page \d+ of \d+\s+Courtesy of legislature\.mi\.gov\s*$"),
                  re.compile(r"^\s*Michigan Compiled Laws Complete Through .*$"))


def _headings(lines):
    """(line index, section number) of every section heading of an act PDF: `24.404 Proposed technical standard.`
    with the `Sec. 4.` line within the next three lines (a long title wraps). A cross-reference that starts a
    line is not followed by one."""
    out = []
    for i, line in enumerate(lines):
        m = _HEADING.match(line)
        if m and any(_SEC_LINE.match(f) for f in lines[i + 1:i + 4]):
            out.append((i, m.group(1)))
    return out


def slice_act(text: str, start: str, end_before: str) -> str:
    """The lines from the heading of section `start` to the line before the heading of the next `end_before`
    section, without the page furniture; the act's title block (before the first heading) is not part of it."""
    lines = text.splitlines()
    heads = _headings(lines)
    first = [i for i, n in heads if n == start]
    if len(first) != 1:
        raise ValueError(f"section {start} is printed {len(first)} times as a heading in the act PDF "
                         f"(the layout changed, the section was repealed or renumbered, or the slice is wrong)")
    stop = next((i for i, n in heads if n == end_before and i > first[0]), None)
    if stop is None:
        raise ValueError(f"heading {end_before} does not follow section {start} in the act PDF: the slice would be a guess")
    cut = [l for l in lines[first[0]:stop] if not any(p.match(l) for p in _PDF_FURNITURE)]
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(l.rstrip() for l in cut))
    return text.strip("\n") + "\n"


def section_page_to_text(raw: bytes) -> str:
    """One section of the Michigan Compiled Laws as www.legislature.mi.gov/Laws/MCL?objectName=mcl-<n>-<n> serves
    it: the `sectionWrapper` block (act name, section heading, `Sec. n.`, paragraphs, History, Compiler's Notes,
    Popular Name). The site's navigation, banner (complete-through and adjournment lines), the chapter, act and
    division links, the previous and next links and the footer are not part of the section and go."""
    page = _decode(raw)
    start = page.find('<div class="sectionWrapper">')
    if start < 0:
        raise ValueError("the page has no sectionWrapper block: it is not an MCL section page")
    end = page.find("</main>", start)
    block = page[start:end if end > 0 else len(page)]
    block = re.sub(r"<!--.*?-->", "", block, flags=re.S)
    block = re.sub(r"</?(?:p|div|br|h[1-6]|tr|td|li)\b[^>]*>", "\x00", block, flags=re.I)
    block = re.sub(r"<[^>]+>", "", block)
    block = html_mod.unescape(block).replace("\xa0", " ")
    out = [l for l in (" ".join(l.split()) for l in block.split("\x00")) if l]
    if not out:
        raise ValueError("the section block is empty")
    return "\n".join(out) + "\n"


_MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
_EFF = re.compile(r"\bEff\.\s+([A-Za-z]+)\.?\s+(\d{1,2}),\s+(\d{4})")


def _not_yet_in_effect(text: str, today: datetime.date | None = None) -> list[str]:
    """ISO dates after `today` that an amendment note (`Imd. Eff. Jan. 3, 2005`, `Eff. Jan. 1, 2027`) prints: the
    Legislature codifies an act that takes effect later as the section's text, which is not the law in force."""
    today = today or datetime.date.today()
    out = []
    for mon, day, year in _EFF.findall(" ".join(text.split())):
        if mon[:3].lower() not in _MONTHS:
            continue
        try:
            d = datetime.date(int(year), _MONTHS.index(mon[:3].lower()) + 1, int(day))
        except ValueError:
            continue
        if d > today:
            out.append(d.isoformat())
    return out


def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "executive_order":
        return eo_html_to_text(raw)
    if fmt == "html" and doc_type == "statute" and not slice_:
        return section_page_to_text(raw)
    if fmt == "pdf" and doc_type == "statute" and slice_:
        return slice_act(pdf_to_text(raw), slice_["section_start"], slice_["section_end_before"])
    return None


_SECTION_CITE = re.compile(r"MCL (\d+\.\d+[a-z]*)(?: to (\d+\.\d+[a-z]*))?(?:\s|\(|$)")


def _check_section_identity(src, text, what_is):
    cite = _SECTION_CITE.match(src["citation"])
    lines = text.splitlines()
    sl = src.get("slice") or {}
    if not cite:
        raise ValueError(f"{src['id']}: citation {src['citation']!r} is not an 'MCL <section>' citation")
    first, last = cite.group(1), cite.group(2) or cite.group(1)
    heads = _headings(lines)
    if sl and sl.get("section_start") != first:
        raise ValueError(f"{src['id']}: the slice starts at {sl.get('section_start')!r}, the citation at {first!r}")
    if not heads or heads[0][1] != first or heads[-1][1] != last:
        raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: the text opens on "
                         f"{heads[0][1] if heads else None!r} and its last heading is {heads[-1][1] if heads else None!r}")
    if not sl and len(heads) != 1:
        raise ValueError(f"{src['id']}: {what_is} holds {len(heads)} section headings, not the one section cited")
    if later := _not_yet_in_effect(text):
        raise ValueError(f"{src['id']}: {what_is} prints an amendment taking effect {', '.join(sorted(set(later)))}, "
                         f"after today: its text is not shown to be the law in force")
    if not cite.group(2) and re.search(r"\b(Repealed|Renumbered)\b", lines[heads[0][0]]):
        raise ValueError(f"{src['id']}: {src['citation']} is printed as repealed or renumbered: not in force")
    return True


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "michigan":
        return False
    head = " ".join(text[:600].split())
    if src["doc_type"] == "executive_order":
        m = re.search(r"(\d{4})\s*-\s*0*(\d+)", src["citation"])
        if not m:
            raise ValueError(f"{src['id']}: citation {src['citation']!r} has no order number")
        # The order's own heading is the FIRST 'EXECUTIVE ORDER' in the text, and the number must follow it
        # directly (the 'No. n' line is next, or the same line). A later mention of another order (a rescission,
        # a transfer) is never the heading, however near the top it falls.
        flat = " ".join(text.split())
        first = re.search(r"EXECUTIVE\s+ORDER\b", flat, re.I)
        own = re.compile(rf"\s*(?:NO\.?)?\s*{m.group(1)}\s*[-–]\s*0*{m.group(2)}\b", re.I)
        if not (first and own.match(flat, first.end())):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: its first 'Executive Order' "
                             f"heading is not 'Executive Order No. {m.group(1)}-{m.group(2)}'")
        return True
    if src["doc_type"] == "statute" and src["citation"].startswith("MCL "):
        return _check_section_identity(src, text, what_is)
    if src["doc_type"] == "statute":
        m = re.match(r"Act (\d+) of (\d{4})", src["citation"])
        if not m or f"Act {m.group(1)} of {m.group(2)}" not in head:
            raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: the head of the text does not "
                             f"carry 'Act {m and m.group(1)} of {m and m.group(2)}'")
        return True
    return False


def extra_notes(src, fmt, text, eff, version):
    """A seed entry's `currency_note`, and for a slice what the document is of the act's PDF."""
    note = (src.get("currency_note") or "").strip()
    sl = src.get("slice")
    slice_note = ""
    if sl and src["doc_type"] == "statute":
        slice_note = (f" The source is the Legislature's file for the whole act (the PDF is the snapshot); this document is the "
                      f"sections from the heading of section {sl['section_start']} to the line before the heading of section "
                      f"{sl['section_end_before']}, as the PDF prints them: section headings, text, History, Compiler's Notes and "
                      f"Admin Rule lines. The page furniture (render date, page count, complete-through banner, courtesy line) "
                      f"was removed.")
    return (slice_note + (f" {note}" if note else "")) or ""


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and src["citation"].startswith("MCL "):
        return ("Text taken from the section's own page on the Michigan Legislature's website (www.legislature.mi.gov, "
                "Laws/MCL): the act name, the section heading and text, and the History, Compiler's Notes and Popular Name "
                "lines, one per line. The site navigation, the banner, the chapter and act links and the footer were removed.")
    if fmt != "html":
        return None
    return ("Text taken from the archive copy of the order on the Michigan Legislature's website "
            "(www.legislature.mi.gov), a Word- or Vignette-made HTML page: each paragraph, heading line and table "
            "cell is one line, lines the source wrapped are joined, and entities are decoded. The page's style "
            "block, the print bar (www.michigan.gov, the print hint) and the copyright footer were removed; "
            "its Release Date and Last Update lines are kept as printed. The Legislature marks its executive "
            "order documents as presented for archival purposes.")
