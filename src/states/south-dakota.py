"""South Dakota: the Legislature's per-section statute pages and the identity of the Governor's executive orders.
Hooks are described in src/states/__init__.py. The Bureau of Information and Technology's policy pages are a
ServiceNow portal that serves no text without its own script, so no policy is read here; the executive orders are
scans (the shared OCR procedure) and the PDFs are read by the shared reader.

The Legislature's chapter page (`/api/Statutes/1-33.html`, the documented keyless API of sdlegislature.gov) is only a
list of section numbers and captions; the law is on one page per section (`/api/Statutes/1-33-43.html`). A statute
document here is the sections a seed entry names (its `sections` list), each fetched once; the snapshot is a JSON
bundle of those raw pages, as New Jersey's and California's are."""
from __future__ import annotations

import json
import re
from pathlib import Path

from src.ingest_common import _decode, _squash, paragraph_html_to_text

_FORMAT = "sdlegislature-statute-sections/1"
_API = "https://sdlegislature.gov/api/Statutes/{}.html"
_DEAD = re.compile(r"^\S+\s+(?:Repealed|Superseded|Obsolete|Transferred|Executed)\b", re.I)


def _section_text(number: str, page: str) -> str:
    text = paragraph_html_to_text(page.encode("utf-8"))
    first = text.splitlines()[0] if text.strip() else ""
    if not first.startswith(f"{number}. ") and not first.startswith(f"{number} "):
        raise ValueError(f"section {number}: the page opens {first[:60]!r}, not the section")
    if _DEAD.match(first):
        raise ValueError(f"section {number} is marked Repealed (or superseded, transferred) on the Legislature's page: "
                         f"{first[:80]!r}; a section out of force is not in the document")
    return text


def statute_bundle(pages: dict, sections: list) -> bytes:
    """The raw pages of the sections a seed entry names, in the order it names them. A section that is
    repealed, or a page that is not the section, is an error, never a smaller document."""
    if not sections or len(set(sections)) != len(sections):
        raise ValueError("a South Dakota statute entry needs `sections`: a list of section numbers, each once")
    out = []
    for n in sections:
        page = _decode(pages[n])
        _section_text(n, page)
        out.append({"number": n, "url": _API.format(n), "page": page})
    return (json.dumps({"format": _FORMAT, "sections": out}, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def statute_bundle_to_text(raw: bytes) -> str:
    doc = json.loads(raw)
    if doc.get("format") != _FORMAT:
        raise ValueError("not a South Dakota statute-sections bundle")
    return "\n".join(_section_text(s["number"], s["page"]) for s in doc["sections"])


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "json" and doc_type == "statute":
        return statute_bundle_to_text(raw)
    return None


def snapshot(src, fetcher, dest: Path, refetch):
    if src["doc_type"] != "statute" or src.get("format") != "json":
        return None
    sections = src.get("sections")
    if not sections:
        raise ValueError(f"{src.get('id')}: a South Dakota json statute entry needs `sections`: a list of section numbers")
    if dest.is_file() and not refetch:
        return dest.read_bytes(), False
    pages = {}
    for n in sections:
        pages[n] = fetcher.get(_API.format(n)).body
    bundle = statute_bundle(pages, sections)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(bundle)
    return bundle, True


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "south-dakota":
        return False
    if src["doc_type"] == "statute":
        heads = [l.split(". ", 1)[0] for l in text.splitlines() if re.match(r"^\d+[A-Za-z]?-\d+[A-Za-z]?-[\d.]+\. ", l)]
        if heads != list(src["sections"]):
            missing = [n for n in src["sections"] if n not in heads]
            raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: its section headings are "
                             f"{heads}, the entry names {src['sections']}"
                             + (f" (no section {', '.join(missing)})" if missing else ""))
        return True
    if src["doc_type"] == "executive_order":
        number = re.search(r"\d{4}-\d{2}", src["citation"])
        # the order's own heading is a line of its own (EXECUTIVE ORDER 2022-10, with at most a stray mark of scan noise
        # beside it); a later order that recites it (2023-06 names 2022-10 in its first paragraph) must not pass
        heading = re.compile(rf"^(?:\S{{1,2}}\s+)?EXECUTIVE\s+ORDER\s+{number.group(0) if number else '-'}(?:\s+\S{{1,2}})?$", re.I)
        if not number or not any(heading.match(l.strip()) for l in text.splitlines()[:15]):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: 'EXECUTIVE ORDER "
                             f"{number and number.group(0)}' is not a heading line in its first lines")
        return True
    return False


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and fmt == "json":
        return ("Text taken from the South Dakota Legislature's keyless statute API (sdlegislature.gov/api/Statutes/<section>.html), "
                "one page per section, the sections named in the citation: each section's number and caption, its paragraphs "
                "one per line with the page's indentation removed, and its source (history) line as printed. The "
                "snapshot is the JSON bundle of those raw pages. A section the Legislature marks repealed is not included. "
                "The pages print no edition or effective date for the whole.")
    return None
