"""New Mexico: statute articles cut from the Compilation Commission's whole-chapter PDF (nmonesource.com), rules from
the DoIT's own NMAC PDFs and the State Records Center and Archives' Word-HTML pages, and DoIT policy, standard and
order PDFs. Hooks are described in src/states/__init__.py.

The statute source serves a whole chapter as one PDF (Chapter 9 is 476 pages), so an entry is a slice: `snapshot`
reads the chapter with pdftotext, keeps the pages from the article's heading line to the next article's heading
line, and stores them as a JSON bundle (page text, page range, the chapter PDF's sha256); `to_text` cuts the
article out of the bundle's pages. Nothing in the slice is edited: annotations and history lines stay.

A rule PDF opens with a Register header line or with the TITLE/CHAPTER/PART lines; the shared check looks for the
seed title in upper or lower case anywhere, so the part heading is read here instead. A standard prints its code in
its own spelling ("NDT-STD008.001" for N-STD-008), so the code is compared by kind and number. An executive order
is a scan read by OCR: its heading line must carry the number, a mention of it in the body does not count.

A statute entry is one of two slices of a chapter PDF. `slice: {article: "27"}` is a whole article (Chapter 9). `slice:
{section_start, section_end_before}` (the shared section-range shape, used for Chapter 14) is the run of sections from
the heading of `section_start` to the heading of `section_end_before`, which is not in it: the heading is the printed
line `14-15-1. Short title.`, and a line that merely begins with a section number (a cross reference in an annotation,
`14-3-15.2 NMSA 1978.`) is not one. The bundle keeps the pages that hold the range; `to_text` cuts the lines."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

from src.ingest_common import _LIGATURES, _squash, paragraph_html_to_text
from src.states import UNHANDLED

_FORMAT = "nmos-chapter-slice/1"
_FORMAT_SECTIONS = "nmos-section-slice/1"
_ARTICLE = re.compile(r"^ARTICLE \d+[A-Z]?$")
_SECTION_HEAD = re.compile(r"^(\d+[A-Z]?-\d+[A-Z]?-\d+(?:\.\d+)?[A-Za-z]?)\. (?=\S)")
_TITLE_BLOCK = 1500
_RULE_BLOCK = 700


# ---- statute slices ---------------------------------------------------------------------------

def _pdf_pages(raw: bytes) -> list[str]:
    """`pdftotext -layout` of the chapter PDF, one string per page."""
    text = subprocess.run(["pdftotext", "-layout", "-", "-"], input=raw, capture_output=True,
                          check=True).stdout.decode("utf-8", "replace")
    pages = text.split("\f")
    if len(pages) > 1 and not pages[-1].strip():
        pages.pop()
    return pages


def _heading_page(pages: list[str], heading: str, start: int = 0) -> int:
    for n in range(start, len(pages)):
        if heading in (l.rstrip() for l in pages[n].splitlines()):
            return n
    return -1


def slice_bundle(pages: list[str], article: str, url: str, chapter_sha256: str) -> bytes:
    """The pages of the chapter that hold `article`, as the JSON bundle that becomes the snapshot."""
    first = _heading_page(pages, f"ARTICLE {article}")
    if first < 0:
        raise ValueError(f"no heading 'ARTICLE {article}' in the chapter PDF")
    last = len(pages) - 1
    for n in range(first, len(pages)):
        lines = [l.rstrip() for l in pages[n].splitlines()]
        idx = lines.index(f"ARTICLE {article}") if n == first else -1
        if any(_ARTICLE.match(l) and l != f"ARTICLE {article}" for l in lines[idx + 1:]):
            last = n
            break
    doc = {"format": _FORMAT, "url": url, "chapter_sha256": chapter_sha256, "chapter_pages": len(pages),
           "article": article, "first_page": first + 1, "last_page": last + 1, "pages": pages[first:last + 1]}
    return (json.dumps(doc, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def _section_heads(lines: list[str]) -> list[tuple[int, str]]:
    """(line index, printed section number) of every line that is a section heading `14-15-1. Short title.`"""
    return [(i, m.group(1)) for i, l in enumerate(lines) if (m := _SECTION_HEAD.match(l))]


def _section_range(lines: list[str], start: str, end_before: str) -> tuple[int, int]:
    """Line indexes [first, stop) of the sections from `start` to the heading of `end_before`."""
    heads = _section_heads(lines)
    firsts = [i for i, num in heads if num == start]
    if len(firsts) != 1:
        raise ValueError(f"section {start} is printed {len(firsts)} times as a heading in the chapter PDF "
                         f"(the layout changed, the section was renumbered, or the slice is wrong)")
    stop = next((i for i, num in heads if num == end_before and i > firsts[0]), None)
    if stop is None:
        raise ValueError(f"heading {end_before} does not follow section {start} in the chapter PDF: "
                         f"the slice would be a guess")
    return firsts[0], stop


def slice_bundle_sections(pages: list[str], start: str, end_before: str, url: str, chapter_sha256: str) -> bytes:
    """The pages of the chapter that hold the sections from `start` to the heading of `end_before`, as the JSON
    bundle that becomes the snapshot."""
    lines_of = [[l.rstrip() for l in p.splitlines()] for p in pages]
    flat = [l for ls in lines_of for l in ls]
    first_line, stop_line = _section_range(flat, start, end_before)
    first = last = None
    seen = 0
    for n, ls in enumerate(lines_of):
        if first is None and seen + len(ls) > first_line:
            first = n
        if seen + len(ls) > stop_line:
            last = n
            break
        seen += len(ls)
    doc = {"format": _FORMAT_SECTIONS, "url": url, "chapter_sha256": chapter_sha256, "chapter_pages": len(pages),
           "section_start": start, "section_end_before": end_before, "first_page": first + 1,
           "last_page": last + 1, "pages": pages[first:last + 1]}
    return (json.dumps(doc, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def snapshot(src, fetcher, dest: Path, refetch):
    if src["doc_type"] != "statute":
        return None
    if dest.is_file() and not refetch:
        return dest.read_bytes(), False
    raw = fetcher.get(src["url"]).body
    if not raw.startswith(b"%PDF"):
        raise ValueError(f"{src['id']}: the chapter source did not serve a PDF")
    sha, pages = hashlib.sha256(raw).hexdigest(), _pdf_pages(raw)
    sl = src["slice"]
    if "section_start" in sl:
        bundle = slice_bundle_sections(pages, sl["section_start"], sl["section_end_before"], src["url"], sha)
    else:
        bundle = slice_bundle(pages, sl["article"], src["url"], sha)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(bundle)
    return bundle, True


def _sections_to_text(doc: dict, slice_: dict | None) -> str:
    start = (slice_ or {}).get("section_start") or doc["section_start"]
    end_before = (slice_ or {}).get("section_end_before") or doc["section_end_before"]
    lines = [l.rstrip() for l in "\n".join(doc["pages"]).translate(str.maketrans(_LIGATURES)).replace("\f", "\n").split("\n")]
    first, stop = _section_range(lines, start, end_before)
    cut = lines[first:stop]
    while cut and not cut[-1].strip():
        cut.pop()
    # the heading of the next article (`ARTICLE 16` and its caption) is printed just before that article's first section
    tail = [i for i, l in enumerate(cut) if _ARTICLE.match(l)]
    if tail and all(l.strip() for l in cut[tail[-1]:]) and len(cut) - tail[-1] <= 2:
        cut = cut[:tail[-1]]
    while cut and not cut[-1].strip():
        cut.pop()
    return re.sub(r"\n{3,}", "\n\n", "\n".join(cut)).strip("\n") + "\n"


def _bundle_to_text(raw: bytes, slice_: dict | None) -> str:
    doc = json.loads(raw)
    if doc.get("format") == _FORMAT_SECTIONS:
        return _sections_to_text(doc, slice_)
    if doc.get("format") != _FORMAT:
        raise ValueError("not a New Mexico slice bundle")
    article = (slice_ or {}).get("article") or doc["article"]
    lines = "\n".join(doc["pages"]).split("\n")
    lines = [l.rstrip() for l in lines]
    start = lines.index(f"ARTICLE {article}") if f"ARTICLE {article}" in lines else -1
    if start < 0:
        raise ValueError(f"no heading 'ARTICLE {article}' in the bundle")
    end = next((i for i in range(start + 1, len(lines)) if _ARTICLE.match(lines[i])), len(lines))
    text = "\n".join(lines[start:end]).translate(str.maketrans(_LIGATURES)).replace("\f", "\n")
    return re.sub(r"\n{3,}", "\n\n", text).strip("\n") + "\n"


# ---- hooks ------------------------------------------------------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "json" and doc_type == "statute":
        return _bundle_to_text(raw, slice_)
    if fmt == "html" and doc_type == "rule":
        return paragraph_html_to_text(raw)          # the SRCA's NMAC pages are Word-exported HTML
    return None


def _fail(src, what_is, msg):
    raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {msg}")


_SEC_CITATION = re.compile(r"NMSA 1978, (\d+[A-Z]?-\d+[A-Z]?-\d+(?:\.\d+)?[A-Za-z]?)"
                           r"(?: to (\d+[A-Z]?-\d+[A-Z]?-\d+(?:\.\d+)?[A-Za-z]?))?")


def _check_sections(src, text):
    """A section slice is the cited one when it opens on the heading of the first cited section and the last
    section heading it holds is the last cited one; for one section its printed caption is the seed title."""
    cite = _SEC_CITATION.fullmatch(src["citation"])
    if not cite:
        raise ValueError(f"{src['id']}: citation {src['citation']!r} is not 'NMSA 1978, n-n-n' or "
                         f"'NMSA 1978, n-n-n to n-n-n'")
    first, last = cite.group(1), cite.group(2) or cite.group(1)
    lines = text.splitlines()
    heads = [(m.group(1), l) for l in lines if (m := _SECTION_HEAD.match(l))]
    if not heads or heads[0][0] != first or heads[-1][0] != last:
        got = (heads[0][0], heads[-1][0]) if heads else None
        raise ValueError(f"{src['id']}: page is not {src['citation']} (its first and last section headings are {got})")
    if first == last:
        caption = _SECTION_HEAD.sub("", heads[0][1]).rstrip(".")
        if _squash(src["title"]).casefold().rstrip(".") != _squash(caption).casefold():
            raise ValueError(f"{src['id']}: the section's printed caption {caption!r} is not the seed title "
                             f"{src['title']!r} (title mismatch)")
    return True


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "new-mexico":
        return False
    kind = src["doc_type"]
    if kind == "statute" and "section_start" in (src.get("slice") or {}):
        return _check_sections(src, text)
    if kind == "statute":
        art = re.search(r"article\s+(\d+[A-Z]?)\b", src["citation"], flags=re.I)
        lines = text.splitlines()
        if not art or lines[:1] != [f"ARTICLE {art.group(1)}"]:
            raise ValueError(f"{src['id']}: page is not {src['citation']} (it opens {lines[:1]!r})")
        if _squash(src["title"]).casefold() != _squash(lines[1] if len(lines) > 1 else "").casefold():
            raise ValueError(f"{src['id']}: the article's printed title {lines[1:2]!r} is not the seed title "
                             f"{src['title']!r} (title mismatch)")
        return True
    if kind == "rule":
        m = re.fullmatch(r"1\.12\.(\d+) NMAC", src["citation"])
        block = _squash(text[:_RULE_BLOCK]).casefold()
        if not m:
            raise ValueError(f"{src['id']}: citation {src['citation']!r} is not 'n.n.n NMAC'")
        want = _squash(f"PART {m.group(1)} {src['title']}").casefold()
        if _squash(f"TITLE 1 ").casefold() not in block or want not in block:
            _fail(src, what_is, f"{src['citation']} 'PART {m.group(1)}' with the title {src['title']!r} (title) "
                                f"is not in its heading lines")
        return True
    if kind == "executive_order":
        m = re.search(r"\d{4}-\d{2,3}", src["citation"])
        found = re.search(r"^[ \t]*EXECUTIVE ORDER[ \t]+(?:NO\.?[ \t]*)?(\d{4}-\d{2,3})[ \t]*$", text[:800],
                          flags=re.I | re.M)       # the first whole heading line only
        if not m or not found or found.group(1) != m.group(0):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: 'Executive Order "
                             f"{m and m.group(0)}' is not in its heading line")
        return True
    if kind in ("policy", "standard"):
        block = text[:_TITLE_BLOCK]
        code = re.match(r"([A-Z])-([A-Z]+)-?(\d+)$", src["citation"])
        phrase = src.get("identity_text") or src["title"]
        if _squash(phrase).casefold() not in _squash(block).casefold():
            _fail(src, what_is, f"{phrase!r} is not in its title block")
        if code:
            compact = block.replace("-", "")
            if not re.search(rf"{code.group(2)}\s*{code.group(3)}", compact):
                _fail(src, what_is, f"{src['citation']} is not in its title block")
        return True
    return False


_SIGNED = re.compile(r"DONE AND ORDERED THIS\s+(\d{1,2})(?:st|nd|rd|th)\s+DAY OF\s+([A-Z]+),?\s+(\d{4})", re.I)
_MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
           "november", "december"]


def effective_date(text, doc_type):
    m = _SIGNED.search(text)
    if doc_type == "policy" and m and m.group(2).lower() in _MONTHS:
        return f"{int(m.group(3)):04d}-{_MONTHS.index(m.group(2).lower()) + 1:02d}-{int(m.group(1)):02d}"
    return UNHANDLED


_VERSION = re.compile(r"\bVersion\s+(\d+(?:\.\d+)*)\s*\((\d{1,2}/\d{4})\)")


def source_version(text, doc_type, fmt):
    m = _VERSION.search(text[:_TITLE_BLOCK]) if doc_type in ("policy", "standard") else None
    return f"Version {m.group(1)} ({m.group(2)})" if m else None


def notes(src, fmt, text):
    if fmt == "json" and src["doc_type"] == "statute":
        sections = "section_start" in (src.get("slice") or {})
        found = re.match(r"NMSA 1978, (\d+)", src["citation"]) if sections else re.search(r"chapter (\d+)", src["citation"])
        chapter = found.group(1) if found else "9"          # the article slices are all of Chapter 9
        cut = ("cut at the heading line of the first section and the heading line of the section that follows the "
               "last one" if sections else "cut at the article's heading line and the next article's heading line")
        return (f"Text taken from the whole-chapter PDF of Chapter {chapter} of the New Mexico Statutes Annotated 1978 that the "
                f"New Mexico Compilation Commission publishes on NMOneSource.com, {cut}. The Commission's annotations (effective dates, temporary "
                "provisions, cross references) and each section's history line are printed with the sections and "
                "kept as printed. The chapter PDF prints no page headers or footers and no edition date.")
    if fmt == "html" and src["doc_type"] == "rule":
        return (f"Text taken from the page of the State Records Center and Archives (srca.nm.gov), which publishes "
                f"the New Mexico Administrative Code, for {src['citation']}: one line per paragraph of the "
                f"Word-exported page, with the page's styles and markup removed. The page is a copy of the part as filed.")
    return None


def extra_notes(src, fmt, text, eff, version):
    if "Ư" in text:
        return (" The PDF's text layer prints the 'ff' ligature as the stray letter Ư (for example "
                "'eƯiciency' for 'efficiency'); the text is kept as extracted, so a keyword search for such "
                "words must allow for it.")
    return ""
