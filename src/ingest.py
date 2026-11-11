#!/usr/bin/env python3
"""The ingester for this corpus: official state sources in, documents at <type>/<state>/<id>.md out.

  python3 src/ingest.py                    # every seed entry (all states) that is not a stub or watch-only
  python3 src/ingest.py --state washington # one state
  python3 src/ingest.py --refetch          # ignore cached snapshots
  python3 src/ingest.py --limit 3          # first three, while shaping it
  python3 src/ingest.py --check            # offline: committed text and documents are current

Built from the toolkit's ingest primitives (corpus-toolkit ADR-0016): `Fetcher` fetches with
the toolkit's honest User-Agent and per-host rate limit, `record_snapshot` writes the
snapshot, both hashes and the drift baseline, `write_document` validates before it writes.
This file is the shared flow: which entries (the seed list), the document and its notes, `--check`.
How bytes become text, and what a state's pages print, is each state's module in `src/states/`
(discovered by name, see its `__init__`); PDFs, Word files and scans are shared (`ingest_common`,
`ingest_docx`, `ingest_ocr`).

A refusal, a scan with no text layer, or a page that is not the cited instrument is reported
and the entry is skipped: the seed entry is then marked a stub by hand, with the reason.
"""
from __future__ import annotations

import argparse
import hashlib
import inspect
import subprocess
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))   # `python3 src/ingest.py` finds `src.*`

from corpus_toolkit import config as config_mod
from corpus_toolkit.documents import DocumentError, write_document
from corpus_toolkit.repo import hash_snapshot, parse_frontmatter
from corpus_toolkit.sources.fetch import UNSUPPORTED, FetchError, Fetcher, sniff
from corpus_toolkit.sources.snapshots import record_snapshot, retrieved_date

from src import states
from src.ingest_common import CONFIG, ROOT, _printed_version
from src.ingest_docx import same_words
from src.ingest_ocr import _ocr_warning, check_ocr, load_ocr_report, ocr_notes, ocr_scan, with_ocr, write_ocr_snapshot
from src.states import check_identity, effective_date, source_version, to_text

# ---- the document -----------------------------------------------------------------------

def doc_path(src: dict, config=CONFIG) -> Path:
    root = config.expected_root_for(src["doc_type"])
    if root is None:
        raise ValueError(f"{src['id']}: no content root for doc_type {src['doc_type']!r}")
    return config.root / root.path / src["jurisdiction"] / f"{src['id']}.md"


def conversion_notes(src: dict, fmt: str, text: str) -> str:
    notes = _conversion_notes(src, fmt, text)
    if src.get("_ocr"):
        return notes
    state = src["jurisdiction"]
    if h := states.hook(state, "extra_notes"):
        notes += h(src, fmt, text, effective_date(text, src["doc_type"], state),
                   source_version(text, src["doc_type"], state, fmt))
    if fmt == "docx" and _printed_version(text) and source_version(text, src["doc_type"], src["jurisdiction"], fmt) == _printed_version(text):
        notes += (" source_version is the date the Word file prints about itself, as printed (a review date, a "
                  "cover date or the last row of its revision history); it prints no effective date.")
    return notes


def _conversion_notes(src: dict, fmt: str, text: str) -> str:
    if src.get("_ocr"):
        return ocr_notes(src["_ocr"])
    if fmt == "docx":
        return ("Text extracted from the Word file (.docx) with pandoc's docx reader, tracked changes accepted "
                "and the result rendered one line per paragraph, heading, list item and table row (a table "
                "row's cells are joined by ' | '; list markers are written out as the file numbers them, bullets "
                "as a bullet character; footnotes follow the text as [n]). Running headers and footers, "
                "pictures and the text inside text boxes (such as a cover-page title) are not read. Headings "
                "carry no markup.")
    if fmt == "pdf":
        pages = sorted(set(src.get("no_text_pages") or ()))
        return ("Text extracted with pdftotext -layout (page headers, footers and column layout "
                "kept as extracted; form feeds and trailing spaces removed; ligature glyphs such "
                "as fi and fl written as their letters)."
                + (f" Pages {', '.join(str(n) for n in pages)} of the PDF have no text layer "
                   f"(figures, blank pages or scanned forms) and add no text here." if pages else ""))
    if h := states.hook(src["jurisdiction"], "notes"):
        if (text_ := h(src, fmt, text)) is not None:
            return text_
    raise ValueError(f"{src['id']}: no conversion notes for format {fmt!r}, doc_type {src['doc_type']!r}, "
                     f"state {src['jurisdiction']!r}: add a `notes` hook to src/states/{src['jurisdiction']}.py")


def body_for(src: dict, text: str, notes: str, config=CONFIG) -> str:
    return (f"> **{config.disclaimer_marker}.** This is a convenience copy for machine reading. "
            f"The official text is published at the source URL above. Verify at source before "
            f"relying on it.\n\n" + (_ocr_warning(src["_ocr"]) if src.get("_ocr") else "") +
            f"# {src['title']} ({src['citation']})\n\n"
            f"## At a glance\n\n{src['why_relevant'].strip()}\n\n"
            f"## Full text\n\n{text.rstrip()}\n\n"
            f"## Curator notes\n\n{notes}\n")


def ingestable(src: dict, state: str | None) -> bool:
    """A seed entry that becomes a document: not a stub, not watch-only, in `state` (every state
    when none is named, so `--check` in the gate covers every state's documents)."""
    return (isinstance(src, dict) and (state is None or src.get("jurisdiction") == state)
            and not src.get("stub") and not src.get("watch_only"))


def derive(src: dict, raw: bytes) -> tuple[str, str]:
    """Raw bytes to (format, text), with the identity check: the one place bytes become the
    text that is committed, shared by `ingest` and `--check`."""
    declared = src.get("format") or "html"
    fmt = sniff(raw, declared)                       # the bytes decide, the manifest is corrected
    if fmt in UNSUPPORTED - {"docx"}:
        raise ValueError(f"{fmt} is not a format this corpus can read")
    if fmt != declared:
        print(f"  {src['id']}: manifest says {declared}, bytes say {fmt} -- correct the manifest")
    text = to_text(raw, fmt, src["doc_type"], src["jurisdiction"], src.get("slice"),
                   urllib.parse.urlsplit(src.get("url") or "").hostname or "",
                   src.get("no_text_pages") or ())
    check_identity(src, text, fmt)
    return fmt, text


def doc_dates(src: dict, text: str) -> tuple[str | None, str]:
    """(effective_date, source_version) the text prints. A scan read by OCR gets neither: a date
    read from an image is a machine's reading of digits, not a transcription."""
    if src.get("_ocr"):
        return None, ""
    return (effective_date(text, src["doc_type"], src["jurisdiction"]),
            source_version(text, src["doc_type"], src["jurisdiction"], src.get("format") or ""))


def frontmatter_for(src: dict, fmt: str, text: str, snap, path: Path, config=CONFIG) -> dict:
    """The document's frontmatter: everything the seed entry, the snapshot and the text determine."""
    eff, version = doc_dates(src, text)
    fm = {
        "id": src["id"],
        "jurisdiction": src["jurisdiction"],
        "title": src["title"],
        "doc_type": src["doc_type"],
        "citation": src["citation"],
        "authority_level": src.get("authority_level", ""),
        "issuing_body": src["issuing_body"] if src.get("issuing_body") else "",
        "source_url": src["url"],
        "source_format": fmt,
        "retrieved": retrieved_date(snap.fresh, path, snap.raw_path),
        "source_sha256": snap.sha256,
        "effective_date": eff,
        "source_version": version,
        "status": "current",
        "content_mode": "verbatim",
        "conversion_notes": conversion_notes(src, fmt, text),
        "maintainer": src.get("maintainer", ""),
        "relationships": {"implements": [], "implemented_by": [],
                          "references_external": [], "related": [], "supersedes": []},
        "tags": list(src["tags"]),
    }
    if src.get("_ocr"):
        fm["text_source"] = "ocr"       # extra_document_fields in corpus.yml lets the server show it
    return fm


def write_ocr_document(src: dict, config=CONFIG, fresh: bool = True) -> Path:
    """The document for a scan whose OCR snapshot is written (see `write_ocr_snapshot`)."""
    src = with_ocr(src, config)
    txt = config.snapshot_dir / f"{src['id']}.txt"
    text = txt.read_text(encoding="utf-8")
    path = doc_path(src, config)
    raw_path = config.snapshot_dir / f"{src['id']}.pdf"
    snap = type("Snap", (), {"fresh": fresh, "raw_path": raw_path,
                             "sha256": hash_snapshot(src["id"], "pdf", config.snapshot_dir)})
    notes = conversion_notes(src, "pdf", text)
    return write_document(config, path, frontmatter_for(src, "pdf", text, snap, path, config),
                          body_for(src, text, notes, config))


def ingest(src: dict, fetcher: Fetcher, refetch: bool, config=CONFIG) -> Path:
    sid = src["id"]
    declared = src.get("format") or "html"
    snap_path = config.snapshot_dir / f"{sid}.{declared}"
    custom = states.hook(src["jurisdiction"], "snapshot")      # fetching that is not one GET of the url
    got = custom(src, fetcher, snap_path, refetch) if custom else None
    raw, fresh = got if got is not None else fetcher.snapshot(src["url"], snap_path, refetch=refetch)
    if src.get("ocr"):
        try:
            prior = load_ocr_report(config, sid)
            if not (prior and prior["pdf_sha256"] == hashlib.sha256(raw).hexdigest() and not refetch):
                text, report = ocr_scan(src, raw, config)
                snap = write_ocr_snapshot(config, src, raw, text, report)
                return write_ocr_document(src, config, snap.fresh)
        except ValueError:
            if fresh:
                snap_path.unlink(missing_ok=True)
            raise
        return write_ocr_document(src, config, False)
    try:
        fmt, text = derive(src, raw)
    except ValueError:
        if fresh:                                    # leave no snapshot for a source we refuse
            snap_path.unlink(missing_ok=True)
        raise
    snap = record_snapshot(config, sid, raw, fmt, text)
    path = doc_path(src, config)
    return write_document(config, path, frontmatter_for(src, fmt, text, snap, path, config),
                          body_for(src, text, conversion_notes(src, fmt, text), config))


def check(sources, config=CONFIG) -> list[str]:
    """Offline: re-derive each committed snapshot's text and document from its raw bytes and
    report every file that differs. Catches a changed `to_text`, and a `.txt` (with its hash)
    or a document edited by hand. Returns problem strings; empty means current."""
    problems: list[str] = []
    for src in sources:
        sid = src["id"]
        declared = src.get("format") or "html"
        raw_path = next((p for p in [config.snapshot_dir / f"{sid}.{declared}"]
                         + sorted(config.snapshot_dir.glob(f"{sid}.*"))
                         if p.suffix != ".txt" and p.is_file()), None)
        txt_path = config.snapshot_dir / f"{sid}.txt"
        doc = doc_path(src, config)
        if raw_path is None:
            problems.append(f"{sid}: raw snapshot missing in {config.snapshot_dir.name}/")
            continue
        if src.get("ocr"):
            fmt = "pdf"
            text, ocr_problems = check_ocr(src, raw_path.read_bytes(), config)
            problems += ocr_problems
            if text is None:
                continue
            src = with_ocr(src, config)
        else:
            try:
                fmt, text = derive(src, raw_path.read_bytes())
            except (ValueError, subprocess.CalledProcessError) as e:
                problems.append(f"{sid}: cannot re-derive text from the snapshot: {e}")
                continue
        if fmt == "docx" and txt_path.is_file() and same_words(txt_path.read_text(encoding="utf-8"), text):
            # The committed text was made by the maintainer's pandoc; CI's is another release and may lay
            # the same words out differently. The same words in the same order are current; any other
            # difference is reported below. The document is then compared with the committed text.
            text = txt_path.read_text(encoding="utf-8")
        if src.get("_ocr"):
            pass                                     # check_ocr compared the committed text already
        elif not txt_path.is_file():
            problems.append(f"{sid}: {sid}.txt missing")
        elif txt_path.read_text(encoding="utf-8") != text:
            problems.append(f"{sid}: {sid}.txt differs from to_text(raw snapshot)")
        if not doc.is_file():
            problems.append(f"{sid}: document {doc.relative_to(config.root)} missing")
            continue
        fm, body = parse_frontmatter(doc)
        notes = conversion_notes(src, fmt, text)
        if body.strip() != body_for(src, text, notes, config).strip():
            problems.append(f"{sid}: document body differs from what the ingester derives "
                            f"from the snapshot and seed entry")
        eff, version = doc_dates(src, text)
        for key, want in (("effective_date", eff), ("source_version", version),
                          ("source_format", fmt), ("conversion_notes", notes),
                          *((("text_source", "ocr"),) if src.get("_ocr") else ())):
            if fm.get(key) != want:
                problems.append(f"{sid}: document frontmatter {key} is {fm.get(key)!r}, "
                                f"the ingester derives {want!r}")
    return problems


def orphans(all_sources, config=CONFIG) -> list[str]:
    """Documents and seed entries must agree, over the whole seed list (not one state's): every
    .md under a content root belongs to a non-stub, non-watch-only entry, and a stub entry has no
    document ("a stub is a seed entry with no document file"; an entry removed from the list takes
    its document with it). Returns problem strings; empty means they agree."""
    problems: list[str] = []
    expected = {}
    for src in all_sources:
        if not isinstance(src, dict):
            continue
        try:
            path = doc_path(src, config)
        except (ValueError, KeyError):
            continue
        if ingestable(src, None):
            expected[path] = src["id"]
        elif src.get("stub") and path.is_file():
            problems.append(f"{src['id']}: stub entry has a document file "
                            f"{path.relative_to(config.root)}: remove the file or the stub flag")
    for root in config.content_roots:
        for md in sorted((config.root / root.path).rglob("*.md")):
            if md not in expected:
                problems.append(f"{md.relative_to(config.root)}: document has no ingestable seed "
                                f"entry (removed, or marked stub or watch-only)")
    return problems


def make_fetcher(config, cls=Fetcher):
    """The Fetcher, with the toolkit's curl transport (ADR-0018) when the pinned toolkit has it.
    cdt.ca.gov and gov.ca.gov challenge the Python client and answer system curl, with the same
    honest User-Agent, with HTTP 200; a corpus on a toolkit without `curl_on_challenge` (v1.36.4)
    gets the plain Fetcher and a challenged host stays a refusal. Passing the flag to a toolkit
    that lacks it would be a TypeError, so the signature is read first."""
    kwargs = {"curl_on_challenge": True} if "curl_on_challenge" in inspect.signature(cls.__init__).parameters else {}
    return cls(config, **kwargs)


def run(sources, fetcher, refetch, config=CONFIG):
    """Ingest every source; a failure is recorded and the rest still run."""
    done, failed = [], []
    for src in sources:
        try:
            out = ingest(src, fetcher, refetch, config)
            print(f"ok  {out.relative_to(config.root)}")
            done.append(out)
        except (FetchError, DocumentError, ValueError, subprocess.CalledProcessError) as e:
            print(f"FAILED {src.get('id')}: {type(e).__name__}: {e}", file=sys.stderr)
            failed.append((src.get("id"), e))
    return done, failed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--state", default=None, help="one state (default: every state in the seed list)")
    ap.add_argument("--refetch", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--check", action="store_true",
                    help="offline: re-derive every committed text and document from the "
                         "raw snapshots and fail if any differs")
    args = ap.parse_args()
    everything = [s for _, g in config_mod.load_source_manifest_group_files(CONFIG)
                  for s in (g.get("sources") or [])]
    sources = [s for s in everything if ingestable(s, args.state)][:args.limit]
    if args.check:
        problems = check(sources) + (orphans(everything) if args.state is None and args.limit is None else [])
        for m in problems:
            print(m)
        print(f"{len(problems)} ingest problem(s)" if problems
              else f"ingest current: {len(sources)} documents re-derived from their snapshots")
        return 1 if problems else 0
    with make_fetcher(CONFIG) as fetcher:
        done, failed = run(sources, fetcher, args.refetch)
    print(f"{len(done)} ingested, {len(failed)} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
