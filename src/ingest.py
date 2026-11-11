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
This file owns what is this domain's: which entries (the seed list), how bytes become text
(`to_text`, one function per source format), and what the document says.

A refusal, a scan with no text layer, or a page that is not the cited instrument is reported
and the entry is skipped: the seed entry is then marked a stub by hand, with the reason.
"""
from __future__ import annotations

import argparse
import html as html_mod
import re
import subprocess
import sys
from pathlib import Path

from corpus_toolkit import config as config_mod
from corpus_toolkit.documents import DocumentError, write_document
from corpus_toolkit.repo import parse_frontmatter
from corpus_toolkit.sources.fetch import UNSUPPORTED, FetchError, Fetcher, sniff
from corpus_toolkit.sources.snapshots import record_snapshot, retrieved_date

ROOT = Path(__file__).resolve().parent.parent
CONFIG = config_mod.load(ROOT / "_meta" / "corpus.yml")

MIN_PDF_WORDS = 30   # below this a PDF is a scan (or an image-only page), not a text document


# ---- bytes to text: one function per source format --------------------------------------

def _decode(raw: bytes) -> str:
    m = re.search(rb"charset=([\w-]+)", raw[:4096])
    return raw.decode(m.group(1).decode() if m else "utf-8", errors="replace")


def _clean_line(s: str) -> str:
    return " ".join(html_mod.unescape(s).replace("\xa0", " ").split())


def ors_html_to_text(raw: bytes) -> str:
    """The Legislative Counsel's ORS chapter page (Word-exported HTML): one source paragraph
    per <p>, wrapped across several HTML lines and indented with &nbsp; runs. Each paragraph
    becomes one line; empty paragraphs (spacing) are dropped. Nothing else is removed."""
    body = _decode(raw)
    body = body[body.lower().find("<body"):]
    lines = []
    for p in re.findall(r"<p[^>]*>(.*?)</p>", body, flags=re.S | re.I):
        line = _clean_line(re.sub(r"<[^>]+>", "", p))
        if line:
            lines.append(line)
    return "\n".join(lines) + "\n"


def oar_html_to_text(raw: bytes) -> str:
    """The Secretary of State's OAR division page. Only the `#content` region is text of the
    rules: the site navigation, footer and scripts around it are not. One line per block
    element or <br>; a blank line before each rule."""
    page = _decode(raw)
    start = page.find('id="content"')
    end = page.find("sos-footer-wrapper")
    if start < 0 or end < start:
        raise ValueError("OAR page has no #content region: the page layout changed")
    start = page.index(">", start) + 1               # after the opening tag
    end = page.rindex("<", 0, end)                   # before the footer's opening tag
    region = re.sub(r"<(script|style).*?</\1>", " ", page[start:end], flags=re.S | re.I)
    region = re.sub(r"<div class='rule_div'>", "\n\x00", region)
    region = re.sub(r"<br\s*/?>|</?(p|div|h[1-6])\b[^>]*>", "\n", region, flags=re.I)
    region = re.sub(r"<[^>]+>", "", region)
    out: list[str] = []
    for raw_line in region.split("\n"):
        marked = raw_line.startswith("\x00")
        line = _clean_line(raw_line.replace("\x00", ""))
        if marked and out:
            out.append("")
        if line:
            out.append(line)
    return "\n".join(out) + "\n"


def rcw_html_to_text(raw: bytes) -> str:
    """The Legislature's RCW page (app.leg.wa.gov), either a whole chapter (`&full=true`) or one
    section. Only the title block and the section content are the law: the site menu, the
    chapter's section list, the PDF buttons and the footer are not. Output: the citation and
    title, then for each section its `RCW x.y.z` line, caption, one line per paragraph, the
    session-law history line and any NOTES, with a blank line before each section. Nothing
    inside a section is dropped."""
    page = _decode(raw)
    block = re.search(r'id="ContentPlaceHolder1_pnlTitleBlock"(.*?)</div>\s*</div>|id="ContentPlaceHolder1_pnlTitleBlock"(.*?)</h2>',
                      page, flags=re.S)
    heads = re.findall(r"<h[12][^>]*>(.*?)</h[12]>", (block.group(0) if block else ""), flags=re.S)
    body_start = page.find('id="ContentPlaceHolder1_dlSectionContent"')
    if body_start < 0:                                  # a one-section page
        body_start = page.find("id='contentWrapper'")
    if not heads or body_start < 0:
        raise ValueError("RCW page has no content region: the page layout changed")
    end = page.find('id="ContentPlaceHolder1_pnlExpanded"', body_start)
    end = page.rfind("<", 0, end) if end >= 0 else end
    chapter = 'id="ContentPlaceHolder1_dlSectionContent"' in page[body_start:body_start + 60]
    if not chapter and end < 0:
        end = len(page)
    start = page.index(">", body_start) + 1               # after the opening tag
    region = page[start:] if chapter else page[start:end]
    if chapter:
        foot = region.find('<div class="block-dark-green">')       # the Legislature's page footer
        region = region[:foot] if foot >= 0 else region
        region = re.sub(r"<span>\s*<br>\s*<hr>", "\n\x00", region)
    head = [_clean_line(re.sub(r"<!--.*?-->|<[^>]+>", "", g)) for g in heads]
    region = re.sub(r"<!--.*?-->", "", region, flags=re.S)
    region = re.sub(r"<a class=\"btn[^>]*>.*?</a>", "", region, flags=re.S)       # PDF buttons
    region = re.sub(r"<(/?)(div|h[1-6]|p|tr)\b[^>]*>|<br\s*/?>|<hr\s*/?>", "\n", region, flags=re.I)
    region = re.sub(r"<[^>]+>", "", region)
    out = [line for line in head if line]
    for raw_line in region.split("\n"):
        marked = raw_line.startswith("\x00")
        line = _clean_line(raw_line.replace("\x00", ""))
        if marked and out:
            out.append("")
        if line:
            out.append(line)
    return "\n".join(out) + "\n"


# pdftotext emits a typographic ligature glyph where a PDF used one ("conﬁgured"). It is the
# same letters, but keyword search cannot match "conﬁgured" against "configured".
_LIGATURES = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi",
              "\ufb04": "ffl", "\ufb05": "st", "\ufb06": "st"}


def pdf_to_text(raw: bytes) -> str:
    """`pdftotext -layout`, as the drift detector reads PDFs, with form feeds and trailing
    space removed and ligature glyphs written as their letters. Page headers, footers and
    column layout are kept: removing furniture per document would be editing the instrument."""
    text = subprocess.run(["pdftotext", "-layout", "-", "-"], input=raw, capture_output=True,
                          check=True).stdout.decode("utf-8", "replace")
    text = text.translate(str.maketrans(_LIGATURES))
    text = "\n".join(line.rstrip() for line in text.replace("\f", "\n").split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", text).strip("\n") + "\n"
    if len(text.split()) < MIN_PDF_WORDS:
        raise ValueError("PDF has no text layer (a scan): needs OCR, make the entry a stub")
    return text


_CRS_ARTICLE = re.compile(r"ARTICLE \d+(\.\d+)?")
_CRS_PART = re.compile(r"PART \d+(\.\d+)?")


def _only(lines: list[str], want: str, what: str) -> int:
    hits = [i for i, line in enumerate(lines) if line == want]
    if not hits:
        raise ValueError(f"CRS file has no {what}: the file layout changed or the slice is wrong")
    if len(hits) > 1:
        raise ValueError(f"CRS file has {what} more than once: the slice would be a guess")
    return hits[0]


def crs_html_to_text(raw: bytes, slice_: dict | None) -> str:
    """The Office of Legislative Legal Services' C.R.S. title file (Word-exported HTML, one file
    per title, so the same paragraph handling as the ORS page). A document is one slice of it:
    `{article: "73"}` runs from the line `ARTICLE 73` to the next `ARTICLE n` heading line, and
    `{article: "33.5", part: "19"}` runs from the body line `PART 19` inside that article to the
    next `PART n` body line. (The article's caption list prints `PART 19 COLORADO CYBERSECURITY`
    on one line; only the body heading is a line of its own.) Nothing inside a slice is dropped:
    caption lists, section text, source notes, editor's notes and annotations all stay."""
    if not slice_ or not slice_.get("article"):
        raise ValueError("a Colorado statute entry needs a slice: {article: ...} or "
                         "{article: ..., part: ...}")
    lines = ors_html_to_text(raw).splitlines()
    start = _only(lines, f"ARTICLE {slice_['article']}", f"article {slice_['article']}")
    end = next((i for i in range(start + 1, len(lines)) if _CRS_ARTICLE.fullmatch(lines[i])),
               len(lines))
    lines = lines[start:end]
    if slice_.get("part"):
        start = _only(lines, f"PART {slice_['part']}", f"part {slice_['part']}")
        end = next((i for i in range(start + 1, len(lines)) if _CRS_PART.fullmatch(lines[i])),
                   len(lines))
        lines = lines[start:end]
    return "\n".join(lines) + "\n"


def to_text(raw: bytes, fmt: str, doc_type: str, jurisdiction: str = "oregon",
            slice_: dict | None = None) -> str:
    """Bytes to the text committed as `<id>.txt` and hashed. A source this corpus has no
    cleanup for is refused: a generic tag-strip would commit navigation as law."""
    if fmt == "pdf":
        return pdf_to_text(raw)
    if fmt == "html" and doc_type == "statute" and jurisdiction == "washington":
        return rcw_html_to_text(raw)
    if fmt == "html" and doc_type == "statute" and jurisdiction == "colorado":
        return crs_html_to_text(raw, slice_)
    if fmt == "html" and doc_type == "statute":
        return ors_html_to_text(raw)
    if fmt == "html" and doc_type == "rule":
        return oar_html_to_text(raw)
    raise ValueError(f"no to_text for format {fmt!r} with doc_type {doc_type!r}")


# ---- what the page itself states --------------------------------------------------------

_MONTHS = ("January|February|March|April|May|June|July|August|September|October|November|"
           "December")
_LONG_DATE = re.compile(rf"\b({_MONTHS})\s+(\d{{1,2}}),\s+(\d{{4}})\b")
_US_DATE = re.compile(r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{4})\b")   # 1/1/2010 or 01-01-2010
_EFFECTIVE_LABEL = re.compile(r"effective\s+date|\beffective\s*:", flags=re.I)


def effective_date(text: str, doc_type: str = "") -> str | None:
    """An ISO date, only when the source labels it `EFFECTIVE DATE` or `Effective:` and prints
    it with a month name or a four-digit year (slashes or hyphens). `09-08-08` is not guessed
    at; a memo's `Date:` is not an effective date; "effective immediately" is prose, not a
    label. The first date within 200 characters after the first label is taken. A statute never
    gets one: a chapter is many sections, and the "Effective date" notes printed under them
    (RCW) belong to the amending acts, not to the document."""
    if doc_type == "statute":
        return None
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


def source_version(text: str, doc_type: str) -> str:
    """ORS pages print their edition ("2025 EDITION"); nothing else here prints a version."""
    if doc_type == "statute":
        m = re.search(r"^(\d{4}) EDITION$", text, flags=re.M)
        if m:
            return f"{m.group(1)} Edition"
    return ""


_POLICY_NUMBER = re.compile(r"(?<!\d)\d{3}-\d{3}-\d{3}(?!\d)")   # 107-004-190, also before _PR


def _squash(s: str) -> str:
    """Whitespace, case and typographic apostrophes/dashes normalised, for phrase matching."""
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u2013", "-").replace("\u2014", "-")
    return " ".join(s.split()).casefold()


def check_identity(src: dict, text: str) -> None:
    """The fetched bytes must be the instrument the seed entry cites, or nothing is written.
    A statute page opens with its chapter, a rule page carries the division title, and a
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
            raise ValueError(f"{src['id']}: PDF is not the cited instrument: {what} "
                             f"does not appear in its text")
    if src["doc_type"] == "rule" and src["title"] not in text:
        raise ValueError(f"{src['id']}: page does not carry the seed title {src['title']!r}")
    if src["doc_type"] == "executive_order":
        number = re.search(r"\d{2,4}-\d{2}", src["citation"])
        if not number or _squash(f"executive order {number.group(0)}") not in _squash(text):
            raise ValueError(f"{src['id']}: PDF is not the cited instrument: "
                             f"'Executive Order {number and number.group(0)}' does not appear in its text")
    if src["doc_type"] == "statute" and src["jurisdiction"] == "washington":
        cite = src["citation"].replace("RCW chapter ", "Chapter ", 1)
        want = f"{cite} RCW" if cite.startswith("Chapter ") else cite
        if not text.strip() or text.splitlines()[0] != want:
            raise ValueError(f"{src['id']}: page is not {src['citation']} (title/chapter mismatch)")
        return
    if src["doc_type"] == "statute" and src["jurisdiction"] == "colorado":
        cite = re.fullmatch(r"C\.R\.S\. title \d+, article ([\d.]+)(?:, part (\d+))?", src["citation"])
        sl = src.get("slice") or {}
        lines = text.splitlines()
        heading = f"PART {sl['part']}" if sl.get("part") else f"ARTICLE {sl.get('article')}"
        if (not cite or cite.group(1) != sl.get("article") or cite.group(2) != sl.get("part")
                or not lines or lines[0] != heading):
            raise ValueError(f"{src['id']}: page is not {src['citation']} (article/part mismatch)")
        if len(lines) < 2 or lines[1].casefold() not in src["title"].casefold():
            raise ValueError(f"{src['id']}: slice title {lines[1] if len(lines) > 1 else ''!r} "
                             f"is not in the seed title {src['title']!r}")
        return
    if src["doc_type"] == "statute":
        chapter = re.search(r"chapter\s+(\w+)", src["citation"], flags=re.I)
        if not chapter or not text.startswith(f"Chapter {chapter.group(1)} "):
            raise ValueError(f"{src['id']}: page is not {src['citation']} (title/chapter mismatch)")


# ---- the document -----------------------------------------------------------------------

def doc_path(src: dict, config=CONFIG) -> Path:
    root = config.expected_root_for(src["doc_type"])
    if root is None:
        raise ValueError(f"{src['id']}: no content root for doc_type {src['doc_type']!r}")
    return config.root / root.path / src["jurisdiction"] / f"{src['id']}.md"


def conversion_notes(src: dict, fmt: str, text: str) -> str:
    if fmt == "pdf":
        return ("Text extracted with pdftotext -layout (page headers, footers and column layout "
                "kept as extracted; form feeds and trailing spaces removed; ligature glyphs such "
                "as fi and fl written as their letters).")
    if src["doc_type"] == "statute" and src["jurisdiction"] == "colorado":
        return ("The source is the Office of Legislative Legal Services' title file (one file for the whole of "
                "the title); this document is the one article (or part) named in the citation, "
                "from its ARTICLE (or PART) heading line to the next one, one line per source "
                "paragraph, with markup, spacing paragraphs and non-breaking spaces removed. "
                "Caption lists, source notes, editor's notes and annotations are kept.")
    if src["doc_type"] == "statute" and src["jurisdiction"] == "washington":
        return ("Text taken from the Legislature's RCW page: the citation and title, then each "
                "section's caption, paragraphs, session-law history and notes, one line per "
                "paragraph. Site menu, PDF buttons, the page's section list and footer removed.")
    if src["doc_type"] == "statute":
        return ("HTML paragraphs unwrapped to one line per source paragraph; markup, spacing "
                "paragraphs and non-breaking spaces removed. The source serves the whole "
                "chapter as one page, so this document is the whole chapter.")
    return ("Rule text taken from the page's rule region; site navigation, footer and scripts "
            "removed. One line per source line; a blank line before each rule number.")


def body_for(src: dict, text: str, notes: str, config=CONFIG) -> str:
    return (f"> **{config.disclaimer_marker}.** This is a convenience copy for machine reading. "
            f"The official text is published at the source URL above. Verify at source before "
            f"relying on it.\n\n# {src['title']} ({src['citation']})\n\n"
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
    if fmt in UNSUPPORTED:
        raise ValueError(f"{fmt} is not a format this corpus can read")
    if fmt != declared:
        print(f"  {src['id']}: manifest says {declared}, bytes say {fmt} -- correct the manifest")
    text = to_text(raw, fmt, src["doc_type"], src["jurisdiction"], src.get("slice"))
    check_identity(src, text)
    return fmt, text


def ingest(src: dict, fetcher: Fetcher, refetch: bool, config=CONFIG) -> Path:
    sid = src["id"]
    declared = src.get("format") or "html"
    snap_path = config.snapshot_dir / f"{sid}.{declared}"
    raw, fresh = fetcher.snapshot(src["url"], snap_path, refetch=refetch)
    try:
        fmt, text = derive(src, raw)
    except ValueError:
        if fresh:                                    # leave no snapshot for a source we refuse
            snap_path.unlink(missing_ok=True)
        raise
    snap = record_snapshot(config, sid, raw, fmt, text)
    path = doc_path(src, config)
    frontmatter = {
        "id": sid,
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
        "effective_date": effective_date(text, src["doc_type"]),
        "source_version": source_version(text, src["doc_type"]),
        "status": "current",
        "content_mode": "verbatim",
        "conversion_notes": conversion_notes(src, fmt, text),
        "maintainer": src.get("maintainer", ""),
        "relationships": {"implements": [], "implemented_by": [],
                          "references_external": [], "related": [], "supersedes": []},
        "tags": list(src["tags"]),
    }
    return write_document(config, path, frontmatter,
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
        try:
            fmt, text = derive(src, raw_path.read_bytes())
        except (ValueError, subprocess.CalledProcessError) as e:
            problems.append(f"{sid}: cannot re-derive text from the snapshot: {e}")
            continue
        if not txt_path.is_file():
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
        for key, want in (("effective_date", effective_date(text, src["doc_type"])),
                          ("source_version", source_version(text, src["doc_type"])),
                          ("source_format", fmt), ("conversion_notes", notes)):
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
    with Fetcher(CONFIG) as fetcher:
        done, failed = run(sources, fetcher, args.refetch)
    print(f"{len(done)} ingested, {len(failed)} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
