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
    text = slice_title_text(pdf_to_text(pdf), src.get("cut"))
    bundle = json.dumps({"source": url, "pdf_sha256": hashlib.sha256(pdf).hexdigest(),
                         "pdf_moddate": _pdf_moddate(pdf), "cut": src["cut"], "text": text},
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
    first = _SECTION.search(src["citation"])
    if not first or not re.search(rf"(?m)^\s*{re.escape(first.group(0))}\.", text):
        raise ValueError(f"{src['id']}: slice is not {src['citation']}: section "
                         f"{first.group(0) if first else '(none cited)'} is not printed in it")
    if _squash(text.splitlines()[0]) != _squash(src["cut"]["from"]):
        raise ValueError(f"{src['id']}: slice does not open with its start heading")
    return True


def notes(src, fmt, text):
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
