"""One module per state, found by name: adding a state adds `src/states/<state>.py` and edits nothing.

A state module is named for its `jurisdiction` (`oregon.py`, `washington.py`) and defines only the
hooks it needs. Every hook is optional; a state whose sources are all PDFs and Word files needs none.

    to_text(raw, fmt, doc_type, slice_, host) -> str | None
        Bytes to the text committed as `<id>.txt`, for the formats this state's sources need beyond
        PDF and Word (those are shared). None: the state has no cleanup for this combination.
        Also called for a PDF source that carries a `slice` (a document that is part of a title
        PDF); None there is a refusal.
    check_identity(src, text, what_is) -> bool
        True when the state checked that the text is the instrument the seed entry cites (raise
        ValueError when it is not). False: use `default_identity`.
    effective_date(text, doc_type) -> str | None | UNHANDLED
        The date the state's sources print. UNHANDLED: use the shared `Effective:` label reader.
    source_version(text, doc_type, fmt) -> str | None
        The version the state's sources print. None: use the shared reader.
    notes(src, fmt, text) -> str | None
        The curator-notes paragraph describing how this state's html (or json) pages were read.
    extra_notes(src, fmt, text, eff, version) -> str
        Sentences appended to the conversion notes (`eff` and `version` are the dates the ingester
        derived from the text).
    snapshot(src, fetcher, dest, refetch) -> (bytes, fresh)
        Fetching that is not one GET of the entry's url (California's bulk download slices).

A state module imports from `src.ingest_common`, `src.ingest_docx` and `src.ingest_ocr`, never from
another state and never from `src.ingest`. Cleanup two states need goes into `src.ingest_common`.
Tests for a state live in `tests/<state>/`, its fixtures in `tests/fixtures/<state>/`.
"""
from __future__ import annotations

import importlib
import pkgutil
import re

from src.ingest_common import (_DATED, _EFFECTIVE_LABEL, _LONG_DATE, _MONTHS, _POLICY_NUMBER, _US_DATE,
                               _printed_version, _squash, pdf_to_text)
from src.ingest_docx import docx_to_text

UNHANDLED = object()      # an `effective_date` hook's answer for "not mine: read the label"

_modules: dict | None = None


def modules(refresh: bool = False) -> dict:
    """{state: module} for every `src/states/<state>.py`."""
    global _modules
    if _modules is None or refresh:
        _modules = {name: importlib.import_module(f"{__name__}.{name}")
                    for _, name, _ in pkgutil.iter_modules(__path__)}
    return _modules


def hook(state: str, name: str):
    """The state's hook of that name, or None."""
    return getattr(modules().get(state), name, None)


def to_text(raw: bytes, fmt: str, doc_type: str, jurisdiction: str = "oregon",
            slice_: dict | None = None, host: str = "", no_text_pages=()) -> str:
    """Bytes to the text committed as `<id>.txt` and hashed. A source this corpus has no
    cleanup for is refused: a generic tag-strip would commit navigation as law."""
    if fmt == "pdf" and slice_:
        # A document that is one slice of a title PDF (Oklahoma's statutes): only the state can cut it.
        h = hook(jurisdiction, "to_text")
        text = h(raw, fmt, doc_type, slice_, host) if h else None
        if text is None:
            raise ValueError(f"no PDF slice for doc_type {doc_type!r} ({jurisdiction!r}): "
                             f"a slice would be ignored and the whole PDF committed")
        return text
    if fmt == "pdf":
        return pdf_to_text(raw, no_text_pages)
    if fmt == "docx":
        return docx_to_text(raw)
    h = hook(jurisdiction, "to_text")
    text = h(raw, fmt, doc_type, slice_, host) if h else None
    if text is not None and slice_ and fmt == "html":
        # A hook that never reads the slice returns the whole page for a sliced entry. Whole means the
        # same text without the slice (or a hook that cannot read the page unsliced, which is one that
        # needs the slice): refuse the former, so a slice is never silently dropped.
        try:
            whole = h(raw, fmt, doc_type, None, host)
        except ValueError:
            whole = None
        if whole == text:
            raise ValueError(f"no HTML slice for doc_type {doc_type!r} ({jurisdiction!r}): "
                             f"the state's to_text ignores the slice and would commit the whole page")
    if text is None:
        raise ValueError(f"no to_text for format {fmt!r} with doc_type {doc_type!r}"
                         + ("" if h else f" ({jurisdiction!r} has no module in src/states/)"))
    return text


def effective_date(text: str, doc_type: str = "", jurisdiction: str = "") -> str | None:
    """An ISO date, only when the source labels it `EFFECTIVE DATE` or `Effective:` and prints
    it with a month name or a four-digit year (slashes or hyphens). `09-08-08` is not guessed
    at; a memo's `Date:` is not an effective date; "effective immediately" is prose, not a
    label. The first date within 200 characters after the first label is taken. A statute never
    gets one: a chapter is many sections, and the "Effective date" notes printed under them
    (RCW) belong to the amending acts, not to the document. A state whose sources print their
    dates another way reads them in its own `effective_date` hook."""
    if doc_type == "statute":
        return None
    h = hook(jurisdiction, "effective_date")
    if h and (printed := h(text, doc_type)) is not UNHANDLED:
        return printed
    m = _EFFECTIVE_LABEL.search(text)
    if not m:
        return None
    window = text[m.end():m.end() + 200]
    long_ = _LONG_DATE.search(window)
    us = _US_DATE.search(window)
    hits = [h for h in (long_, us) if h]
    if not hits:
        return None
    h = min(hits, key=lambda x: x.start())
    if h is long_:
        mon = _MONTHS.split("|").index(h.group(1)) + 1
        d, y = int(h.group(2)), int(h.group(3))
    else:
        mon, d, y = int(h.group(1)), int(h.group(2)), int(h.group(3))
    if not (1 <= mon <= 12 and 1 <= d <= 31):
        return None
    return f"{y:04d}-{mon:02d}-{d:02d}"


def source_version(text: str, doc_type: str, jurisdiction: str = "", fmt: str = "") -> str:
    """ORS pages print their edition ("2025 EDITION"); a state's own sources may print another
    version (its `source_version` hook); a Word file may print a review date, a cover date or a
    revision history (`_printed_version`, only when `fmt` is "docx": a web page's or PDF's revision
    table is not read as its version); nothing else here prints a version."""
    if doc_type == "statute":
        m = re.search(r"^(\d{4}) EDITION$", text, flags=re.M)
        if m:
            return f"{m.group(1)} Edition"
    h = hook(jurisdiction, "source_version")
    if h and (version := h(text, doc_type, fmt)) is not None:
        return version
    return _printed_version(text) if fmt == "docx" else ""


def check_identity(src: dict, text: str, fmt: str | None = None) -> None:
    """The fetched bytes must be the instrument the seed entry cites, or nothing is written.
    The state's `check_identity` hook goes first; what it does not claim is checked by
    `default_identity`. `fmt` words the refusal ("PDF" or "page"); it defaults to the seed
    entry's declared format."""
    fmt = fmt or src.get("format") or "html"
    what_is = {"pdf": "PDF", "docx": "Word file"}.get(fmt, "page")
    h = hook(src["jurisdiction"], "check_identity")
    if h and h(src, text, what_is):
        return
    default_identity(src, text, what_is)


def default_identity(src: dict, text: str, what_is: str) -> None:
    """A statute page opens with its chapter, a rule page carries the division title, and a
    policy or standard PDF carries the seed entry's `identity_text` (a phrase the document
    prints, for when its printed title differs from the seed title), else the citation's policy
    number (107-004-190 for 107-004-190_PR), else, when the citation has none, the seed title."""
    if src["doc_type"] in ("policy", "standard"):
        number = _POLICY_NUMBER.search(src["citation"])
        if src.get("identity_text"):
            what = repr(src["identity_text"])
            found = _squash(src["identity_text"]) in _squash(text)
        elif number:
            what = number.group(0)
            found = what in text
        else:
            what = repr(src["title"])
            found = _squash(src["title"]) in _squash(text)
        if not found:
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {what} "
                             f"does not appear in its text")
    if src["doc_type"] == "rule" and src["title"] not in text:
        raise ValueError(f"{src['id']}: page does not carry the seed title {src['title']!r}")
    if src["doc_type"] == "executive_order":
        number = re.search(r"\d{2,4}-\d{2}", src["citation"])
        if not number or _squash(f"executive order {number.group(0)}") not in _squash(text):
            raise ValueError(f"{src['id']}: PDF is not the cited instrument: "
                             f"'Executive Order {number and number.group(0)}' does not appear in its text")
    if src["doc_type"] == "statute":
        chapter = re.search(r"chapter\s+(\w+)", src["citation"], flags=re.I)
        if not chapter or not text.startswith(f"Chapter {chapter.group(1)} "):
            raise ValueError(f"{src['id']}: page is not {src['citation']} (title/chapter mismatch)")
