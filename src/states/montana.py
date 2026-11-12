"""Montana: the Legislature's Montana Code Annotated section pages and the Governor's executive orders. Hooks are
described in src/states/__init__.py. The Department of Administration's PDFs (the Information Technology Board's
operating procedures) and the Governor's executive-order PDFs are read by the shared PDF reader; a scanned order goes
through the shared OCR procedure.

Statutes (`mca.legmt.gov/bills/mca`, the Legislature's static HTML tree): the site serves one section per page, so a
document is a bundle of the sections its seed entry lists (`sections:`), built by `snapshot` from the content block of
each page (`<div class="mca-content">`, the page's own title lines, section text and history; the navigation bar,
breadcrumb, footer disclaimer and the host's injected script are not kept). A section page's address is built from its
number (`section_url`); the bundle's identity check requires every listed section's number to be printed, in order.
Executive orders: the shared PDF reader gives the text; the order's own heading line ("EXECUTIVE ORDER No. 3-2025",
zero-padded in some orders) is what identifies it."""
from __future__ import annotations

import html as html_mod
import re
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

import httpx
from corpus_toolkit.sources.fetch import FetchError

from src.states import UNHANDLED

SECTION_MARK = "<!-- section "
_BASE = "https://mca.legmt.gov/bills/mca/"
_EDITION = re.compile(r"^Montana Code Annotated \d{4}$")


def section_url(number: str) -> str:
    """The page of a section of the Montana Code Annotated: `2-17-511` is title 2, chapter 17, part 5, section 11 and
    sits at title_0020/chapter_0170/part_0050/section_0110/0020-0170-0050-0110.html (the index pages print the same
    paths; the bundle's identity check confirms the page printed the number asked for)."""
    m = re.fullmatch(r"(\d+)-(\d+)-(\d+)", number)
    if not m:
        raise ValueError(f"not a Montana Code Annotated section number: {number!r}")
    title, chapter, rest = (int(g) for g in m.groups())
    part, sec = divmod(rest, 100)
    t, c, p, s = (f"{n * 10:04d}" for n in (title, chapter, part, sec))
    return f"{_BASE}title_{t}/chapter_{c}/part_{p}/section_{s}/{t}-{c}-{p}-{s}.html"


def _decode(raw: bytes) -> str:
    return raw.decode("utf-8", errors="replace").lstrip("﻿")


def section_fragment(page: bytes) -> bytes | None:
    """The content block of a section page, or None when the page is not a section page."""
    text = _decode(page)
    start = text.find('<div class="mca-content')
    end = text.find("<footer", start) if start >= 0 else -1
    if start < 0 or end < 0 or 'class="section-content"' not in text[start:end]:
        return None
    return text[start:end].rstrip().encode("utf-8")


def build_bundle(parts: list[tuple[str, bytes]]) -> bytes:
    """The snapshot of a statute document: each section's content block exactly as the site served it, after a
    comment line naming the page it came from."""
    return b"".join(f"{SECTION_MARK}{url} -->\n".encode() + frag + b"\n" for url, frag in parts)


def snapshot(src, fetcher, dest: Path, refetch):
    """A statute document is fetched section by section (`sections:` in the seed entry); any other entry is one GET
    of the url (None: the shared flow does it). A section the site does not serve is an error: nothing is written."""
    if not src.get("sections"):
        return None
    if dest.is_file() and not refetch:
        return dest.read_bytes(), False
    parts = []
    for number in src["sections"]:
        url = section_url(number)
        try:
            page = fetcher.get(url).body
        except (httpx.HTTPError, FetchError) as e:
            raise ValueError(f"{src['id']}: the Legislature's site did not serve section {number} ({url}): {e}") from e
        frag = section_fragment(page)
        if frag is None:
            raise ValueError(f"{src['id']}: the page for section {number} ({url}) is not a section page")
        parts.append((url, frag))
    bundle = build_bundle(parts)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(bundle)
    return bundle, True


# ---- statute text ---------------------------------------------------------------------------

class _Paragraphs(HTMLParser):
    """The `<p>` paragraphs of a section (text, then history) and the page's title lines."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.paras: list[str] = []
        self.heads: dict[str, str] = {}
        self._cur: list[str] | None = None
        self._tag: str | None = None
        self._head: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "p" and "line-indent" in (a.get("class") or ""):
            self._cur = []
        elif tag in ("h1", "h2", "h3", "h4"):
            self._tag, self._head = tag, []

    def handle_endtag(self, tag):
        if tag == "p" and self._cur is not None:
            line = " ".join("".join(self._cur).split())
            if line:
                self.paras.append(line)
            self._cur = None
        elif tag == self._tag:
            self.heads.setdefault(tag + ("-code" if tag == "h1" and "Montana Code" in "".join(self._head) else ""),
                                  " ".join("".join(self._head).split()))
            self._tag = None

    def handle_data(self, data):
        if self._cur is not None:
            self._cur.append(data)
        elif self._tag:
            self._head.append(data)


def statute_to_text(raw: bytes) -> str:
    """A bundle to text: the code's edition line and the title, chapter and part lines once, then each section (its
    catchline and text paragraphs, then its history line), a blank line before each section."""
    pieces = _decode(raw).split(SECTION_MARK)[1:]
    if not pieces:
        raise ValueError("no statute text: the snapshot has no section fragments")
    header: list[str] | None = None
    out: list[str] = []
    for piece in pieces:
        p = _Paragraphs()
        p.feed(piece.split("-->", 1)[1])
        p.close()
        this = [p.heads.get(k, "") for k in ("h1-code", "h4", "h3", "h2")]
        if not all(this) or not p.paras:
            raise ValueError("no statute text: a section fragment has no edition, title, chapter and part lines "
                             "and section text")
        if header is None:
            header = this
            out.extend(this)
        elif this != header:
            raise ValueError(f"no statute text: the sections sit under more than one part ({header[3]!r} and "
                             f"{this[3]!r}): split the seed entry")
        out.append("")
        out.extend(p.paras)
    return "\n".join(out) + "\n"


# ---- hooks (see src/states/__init__.py) ------------------------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute" and host == "mca.legmt.gov":
        return statute_to_text(raw)
    return None


_SECTION_LINE = re.compile(r"^(\d+-\d+-\d+)\.\s")
_ORDER_HEADING = re.compile(r"^\s*EXECUTIVE ORDER\s+NO\.?\s*0*(\d+)-(\d{4})\s*$", re.I)


def _statute_identity(src, text, what_is):
    sid = src["id"]
    blocks = text.split("\n\n")[1:]
    printed = [m.group(1) for b in blocks if (m := _SECTION_LINE.match(b))]
    listed = list(src["sections"])
    for n in listed:
        if n not in printed:
            raise ValueError(f"{sid}: {what_is} is not the cited instrument: section {n} does not appear in its text")
    extra = [n for n in printed if n not in listed]
    if extra:
        raise ValueError(f"{sid}: {what_is} holds {', '.join(extra)}, which the seed entry does not list in its "
                         f"sections: the bundle and the seed list have drifted apart")
    if printed != listed:
        raise ValueError(f"{sid}: {what_is} holds the listed sections in another order than the seed entry "
                         f"(bundle order {printed}, listed order {listed})")


def _order_identity(src, text, what_is):
    want = re.search(r"(\d+)-(\d{4})", src["citation"])
    heads = [m for line in text.splitlines()[:25] if (m := _ORDER_HEADING.match(line))]
    if not want or not any((int(m.group(1)), m.group(2)) == (int(want.group(1)), want.group(2)) for m in heads):
        raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: 'EXECUTIVE ORDER NO. "
                         f"{want and '-'.join(want.groups())}' is not its heading line")


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "montana":
        return False
    if src.get("sections"):
        _statute_identity(src, text, what_is)
        return True
    if src["doc_type"] == "executive_order":
        _order_identity(src, text, what_is)
        return True
    return False


def effective_date(text, doc_type):
    """An order prints `shall take effect on July 1, 2025`; one that is effective immediately prints no date."""
    if doc_type != "executive_order":
        return UNHANDLED
    m = re.search(r"take\s+effect\s+on\s+([A-Z][a-z]+)\s+(\d{1,2}),\s+(\d{4})", text)
    if not m:
        return UNHANDLED
    try:
        return datetime.strptime(" ".join(m.groups()), "%B %d %Y").date().isoformat()
    except ValueError:
        return UNHANDLED


def source_version(text, doc_type, fmt):
    first = text.split("\n", 1)[0]
    return first if doc_type == "statute" and _EDITION.match(first) else None


def notes(src, fmt, text):
    if src["jurisdiction"] != "montana" or fmt != "html" or not src.get("sections"):
        return None
    return ("Text taken from the Legislature's Montana Code Annotated pages (mca.legmt.gov): the site serves one "
            "section per page, so each listed section's text and history line were taken from its page and the "
            "sections are joined in order, a blank line before each. The edition line, title, chapter and part "
            "lines the pages print are given once at the top. The pages' navigation, breadcrumb, footer "
            "disclaimer and links are not read; a cross reference is written as its text. The snapshot keeps each "
            "page's content block as served.")
