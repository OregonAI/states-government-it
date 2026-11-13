"""Wyoming: the Legislature's per-title statute PDFs (sliced). The Department of Enterprise Technology Services'
policy library is PDFs served from Google Drive, which the shared PDF reader handles. Hooks are described in
src/states/__init__.py."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

from src.ingest_common import _MONTHS, _squash, pdf_to_text
from src.states import UNHANDLED


# ---- Statutes: one slice of the title PDF ------------------------------------------------------
#
# wyoleg.gov serves each title of the Wyoming Statutes as one PDF (title 9 is 892 pages) and the shared PDF
# reader cannot slice. The snapshot hook therefore reads the PDF once, cuts the slice out of its extracted
# text and commits the slice as a JSON bundle (the PDF's address and sha256 are in it, so the slice can be
# checked against the title file). A slice is the entry's `cut: {from: <heading line>, to: <heading line>}` (the shared
# seed check accepts only Colorado's and California's `slice` keys, and it treats entries with one url as duplicates, so
# the key is `cut` and each entry's url ends in a #fragment that names its slice; the fragment is not sent). It runs from the
# line that is `from` up to, not including, the line that is `to`. Each heading must be a line of its own that
# occurs exactly once in the title; a heading that is missing or repeated is a refusal, never a guess.

def _only(lines: list[str], want: str, what: str) -> int:
    hits = [i for i, line in enumerate(lines) if _squash(line) == _squash(want)]
    if not hits:
        raise ValueError(f"title PDF has no line {want!r} ({what}): the layout changed or the slice is wrong")
    if len(hits) > 1:
        raise ValueError(f"title PDF has the line {want!r} ({what}) {len(hits)} times: the slice would be a guess")
    return hits[0]


def slice_title_text(text: str, slice_: dict) -> str:
    if not slice_ or not slice_.get("from") or not slice_.get("to"):
        raise ValueError("a Wyoming statute entry needs cut: {from: <heading line>, to: <heading line>}")
    lines = text.splitlines()
    start = _only(lines, slice_["from"], "start of the slice")
    end = _only(lines, slice_["to"], "end of the slice")
    if end <= start:
        raise ValueError(f"the end heading {slice_['to']!r} comes before the start heading {slice_['from']!r}")
    body = lines[start:end]
    while body and not body[-1].strip():
        body.pop()
    return "\n".join(body) + "\n"


_STRUCTURE = re.compile(r"^\s*(?:TITLE|CHAPTER|ARTICLE)\s+\d+\S*\s+-\s")


def _section_heading_lines(lines: list[str], number: str) -> list[int]:
    """Lines that open section `number` as a heading: the printed number, a full stop, then the section's name on the
    same line. A cross-reference that wraps so that '40-21-119.' starts a line has nothing after the stop."""
    head = re.compile(rf"^\s*{re.escape(number)}\.\s+\S")
    return [i for i, line in enumerate(lines) if head.match(line)]


def slice_sections(text: str, start: str, end_before: str) -> str:
    """The section-range slice `{section_start, section_end_before}` of a title's text: from the heading line of
    section `start` up to, not including, the heading line of section `end_before`. Each heading must be there exactly
    once and the end must follow the start; anything else is a refusal, never a guess. When the end section opens a new
    chapter or article, the structure heading that sits between the two sections (`CHAPTER 22 - ...`) is not part of
    the slice and is dropped with the blank lines around it."""
    lines = text.splitlines()
    first = _section_heading_lines(lines, start)
    if len(first) != 1:
        raise ValueError(f"title PDF has section {start} as a heading line {len(first)} times (the layout changed, "
                         f"the section was renumbered, or the slice is wrong): the slice would be a guess")
    stops = [i for i in _section_heading_lines(lines, end_before)]
    if len(stops) != 1:
        raise ValueError(f"title PDF has section {end_before} as a heading line {len(stops)} times: the slice "
                         f"would be a guess")
    if stops[0] <= first[0]:
        raise ValueError(f"section {end_before} (the end) does not follow section {start} (the start) in the title PDF")
    body = lines[first[0]:stops[0]]
    while body and not body[-1].strip():
        body.pop()
    # the structure heading of the chapter or article that the end section opens (one line, or wrapped)
    block = len(body)
    while block and body[block - 1].strip():
        block -= 1
    if block < len(body) and _STRUCTURE.match(body[block]):
        body = body[:block]
        while body and not body[-1].strip():
            body.pop()
    return "\n".join(body) + "\n"


def _pdf_moddate(raw: bytes) -> str:
    out = subprocess.run(["pdfinfo", "-"], input=raw, capture_output=True, check=True).stdout.decode("utf-8", "replace")
    m = re.search(r"^ModDate:\s*(.+)$", out, flags=re.M)
    return m.group(1).strip() if m else ""


def wy_snapshot(src: dict, fetcher, dest: Path, refetch: bool) -> tuple[bytes, bool]:
    """Like Fetcher.snapshot, for a statute slice: reuse the committed bundle unless `refetch`, else read the
    title PDF (once per fetcher: entries of one title share it) and cut the slice."""
    if dest.is_file() and not refetch:
        return dest.read_bytes(), False
    url = src["url"].split("#", 1)[0]
    cache = fetcher.__dict__.setdefault("_wyoming_title_pdfs", {})
    if url not in cache:
        cache[url] = fetcher.get(url).body
    pdf = cache[url]
    if src.get("slice"):
        key, how = "slice", src["slice"]
        text = slice_sections(pdf_to_text(pdf), how["section_start"], how["section_end_before"])
    else:
        key, how = "cut", src.get("cut")
        text = slice_title_text(pdf_to_text(pdf), how)
    bundle = json.dumps({"source": url, "pdf_sha256": hashlib.sha256(pdf).hexdigest(),
                         "pdf_moddate": _pdf_moddate(pdf), key: how, "text": text},
                        ensure_ascii=False, indent=1).encode("utf-8")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(bundle)
    return bundle, True


def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "json" and doc_type == "statute":
        return json.loads(raw)["text"]
    return None


_SECTION = re.compile(r"\d+-\d+-\d+")


def _check_order_identity(src: dict, text: str, what_is: str) -> bool:
    """The Governor's order prints 'EXECUTIVE ORDER', then on its own line 'Order 2023-02'. The number must be
    that heading line, not a mention of it in the body."""
    number = re.search(r"\d{4}-\d{2}", src["citation"])
    heading = re.search(r"(?im)^\s*executive order\s*\n+\s*order\s+(\d{4}-\d{2})\s*$", text)
    if not number or not heading or heading.group(1) != number.group(0):
        raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: its heading is "
                         f"'Order {heading.group(1) if heading else '(none found)'}', not "
                         f"'Order {number.group(0) if number else src['citation']}'")
    return True


def check_identity(src, text, what_is):
    if src["doc_type"] == "executive_order":
        return _check_order_identity(src, text, what_is)
    if src["doc_type"] != "statute":
        return False
    sections = _SECTION.findall(src["citation"])
    if not sections or not re.search(rf"(?m)^\s*{re.escape(sections[0])}\.", text):
        raise ValueError(f"{src['id']}: slice is not {src['citation']}: section "
                         f"{sections[0] if sections else '(none cited)'} is not printed in it")
    if src.get("slice"):
        return _check_section_slice(src, text, sections)
    if _squash(text.splitlines()[0]) != _squash(src["cut"]["from"]):
        raise ValueError(f"{src['id']}: slice does not open with its start heading")
    return True


def _check_section_slice(src: dict, text: str, sections: list[str]) -> bool:
    """A section-range slice is the cited one when it opens on the heading of `section_start` (the first cited
    section), its last heading is the last cited section, it does not hold the end section, and the first section is
    not printed as repealed or renumbered."""
    sl = src["slice"]
    lines = text.splitlines()
    heads = [m.group(1) for line in lines if (m := re.match(r"^\s*(\d+-\d+-\d+)\.\s+\S", line))]
    first, last = sections[0], sections[-1]
    if sl["section_start"] != first or not heads or heads[0] != first or not re.match(rf"\s*{re.escape(first)}\.", lines[0]):
        raise ValueError(f"{src['id']}: slice is not {src['citation']}: it opens on "
                         f"{heads[0] if heads else None!r}, and section_start is {sl['section_start']!r}")
    if heads[-1] != last:
        raise ValueError(f"{src['id']}: slice is not {src['citation']}: its last section heading is {heads[-1]!r}")
    if sl["section_end_before"] in heads:
        raise ValueError(f"{src['id']}: slice holds section {sl['section_end_before']}, which ends it")
    if re.search(r"\b(Repealed|Renumbered)\b", lines[0]) or re.search(r"(?m)^\s*\d+-\d+-\d+\.\s+(Repealed|Renumbered)\b", text):
        raise ValueError(f"{src['id']}: {src['citation']} prints a section as repealed or renumbered: not in force")
    return True


def notes(src, fmt, text):
    if fmt == "json" and src["doc_type"] == "statute" and src.get("slice"):
        sl = src["slice"]
        return (f"The source is the Legislature's PDF of the whole title (the url above); this document is the sections "
                f"of it from the heading line of section {sl['section_start']} to the line before the heading of "
                f"section {sl['section_end_before']} (that section, and the chapter heading that opens it, are not in "
                f"it), as the PDF prints them: pdftotext -layout, page breaks removed, line breaks and indentation as "
                f"extracted. The section is a provision of a chapter that is not about state IT as a whole; it is "
                f"mirrored because the provision itself governs state IT (owner decision 2026-11-13). The snapshot is "
                f"the JSON bundle of the slice with the title PDF's sha256 and its PDF ModDate, not the PDF.")
    if fmt == "json" and src["doc_type"] == "statute":
        return ("The source is the Legislature's PDF of the whole title (the url above); this document is the one "
                "slice named in the citation, from its heading line to the line before the next heading, as the PDF "
                "prints it: pdftotext -layout, page breaks removed, line breaks and indentation as extracted, "
                "nothing inside the slice dropped (section notes such as an effective date for a later section, and "
                "repealed-section lines, stay). The snapshot is the JSON bundle of the slice with the title PDF's "
                "sha256 and its PDF ModDate, not the PDF.")
    return None


def snapshot(src, fetcher, dest, refetch):
    if src["doc_type"] == "statute":
        return wy_snapshot(src, fetcher, dest, refetch)
    return None


# ---- Dates the policy files print -----------------------------------------------------------------------------
#
# The 2xxx files and WyIT 3023 open with a header table whose rows are `Effective Date`, `Next Review Date` and
# `Policy Version` (or `Document Version`); a cell can be empty (WyIT 3023, 2001 and 2002 print an empty Effective
# Date cell), and the shared label reader would then take the next row's date, the next review date. WyIT 2003 prints
# an abbreviated month ('Nov 4, 2026'). The date is read only from the same line as the label. The 1xxx and 3xxx files have a document-history table instead and are left to the
# shared reader.

_MONTH_NAMES = _MONTHS.split("|")
_HEADER_EFFECTIVE = re.compile(rf"(?m)^[ \t]*Effective Date(?:[ \t]+(?P<d>(?:{_MONTHS}|{'|'.join(m[:3] for m in _MONTH_NAMES)})\.?\s+\d{{1,2}},\s+\d{{4}}))?[ \t]*$")
_HEADER_VERSION = re.compile(r"(?m)^[ \t]*(?:Policy|Document) Version(?:[ \t]+(?P<v>\S+))?[ \t]*$")


def effective_date(text, doc_type):
    m = _HEADER_EFFECTIVE.search(text)
    if not m:
        return UNHANDLED
    if not m.group("d"):
        return None
    month, day, year = re.match(r"([A-Za-z]+)\.?\s+(\d{1,2}),\s+(\d{4})", m.group("d")).groups()
    return f"{int(year):04d}-{[n[:3] for n in _MONTH_NAMES].index(month[:3]) + 1:02d}-{int(day):02d}"


def source_version(text, doc_type, fmt):
    m = _HEADER_VERSION.search(text)
    return m.group("v") if m and m.group("v") else None


def extra_notes(src, fmt, text, eff, version):
    out = ""
    if eff:
        out += " effective_date is the Effective Date cell of the file's header table, as printed."
    if version:
        out += " source_version is the Policy Version (or Document Version) cell of the header table, as printed."
    return out
