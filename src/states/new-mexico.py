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
is a scan read by OCR: its heading line must carry the number, a mention of it in the body does not count."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

from src.ingest_common import _LIGATURES, _squash, paragraph_html_to_text
from src.states import UNHANDLED

_FORMAT = "nmos-chapter-slice/1"
_ARTICLE = re.compile(r"^ARTICLE \d+[A-Z]?$")
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


def snapshot(src, fetcher, dest: Path, refetch):
    if src["doc_type"] != "statute":
        return None
    if dest.is_file() and not refetch:
        return dest.read_bytes(), False
    raw = fetcher.get(src["url"]).body
    if not raw.startswith(b"%PDF"):
        raise ValueError(f"{src['id']}: the chapter source did not serve a PDF")
    bundle = slice_bundle(_pdf_pages(raw), src["slice"]["article"], src["url"], hashlib.sha256(raw).hexdigest())
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(bundle)
    return bundle, True


def _bundle_to_text(raw: bytes, slice_: dict | None) -> str:
    doc = json.loads(raw)
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


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "new-mexico":
        return False
    kind = src["doc_type"]
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
        return ("Text taken from the whole-chapter PDF of Chapter 9 of the New Mexico Statutes Annotated 1978 that the "
                "New Mexico Compilation Commission publishes on NMOneSource.com, cut at the article's heading line "
                "and the next article's heading line. The Commission's annotations (effective dates, temporary "
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
