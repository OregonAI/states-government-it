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
import io
import json
import re
import subprocess
import sys
import urllib.parse
import weakref
import zipfile
from html.parser import HTMLParser
from pathlib import Path

from corpus_toolkit import config as config_mod
from corpus_toolkit.documents import DocumentError, write_document
from corpus_toolkit.repo import parse_frontmatter
import httpx

from corpus_toolkit.sources.fetch import UNSUPPORTED, Challenge, FetchError, Fetcher, Refused, sniff
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


class _SamParser(HTMLParser):
    """Collects the text of the State Administrative Manual's chapter view (dgs.ca.gov). Block
    elements start a new line, inline elements (span, a, strong, em, sup) run on inside the
    sentence, `<hr>` between sections gives a blank line. List markers are printed the way a
    browser prints them (the page styles them with CSS): `1.` for an ordered list, `a.` for
    `lower-alpha`, `i.` for `lower-roman`, a bullet for an unordered list; a nested list is
    indented two spaces per level."""

    BLOCK = {"p", "div", "h1", "h2", "h3", "h4", "li", "ol", "ul", "br", "tr"}
    # CSS `list-style-type` values a browser prints as letters or numbers; `lower-latin` is
    # `lower-alpha` under another name. Any other value is an error, never a silent decimal.
    STYLES = {"decimal": "decimal", "lower-alpha": "lower-alpha", "lower-latin": "lower-alpha",
              "upper-alpha": "upper-alpha", "upper-latin": "upper-alpha",
              "lower-roman": "lower-roman", "upper-roman": "upper-roman"}
    # The Secretary of State's stylesheet hides the browser marker on these list classes and
    # draws `(a)`, `(1)`, `(A)`, `(i)`, `(I)` itself: class -> counter style. Used only when
    # `paren_classes` is set (the CCR pages); a list with none of these classes keeps its style.
    PAREN_CLASSES = {"alphaLwr": "lower-alpha", "alphaLwrInline": "lower-alpha",
                     "numPrnthsis": "decimal", "numPrnthsisInline": "decimal",
                     "alphaUppr": "upper-alpha", "romanLwr": "lower-roman", "romanUppr": "upper-roman"}

    def __init__(self, paren_classes: bool = False):
        super().__init__(convert_charrefs=True)
        self.lines: list[str] = []
        self.cur: list[str] = []
        self.lists: list[list] = []          # [style, next number, parenthesized]
        self.skip = 0                         # inside <style> or <script>
        self.paren_classes = paren_classes

    def _flush(self):
        raw = "".join(self.cur)
        self.cur = []
        line = " ".join(raw.split())
        if line:
            self.lines.append(" " * (len(raw) - len(raw.lstrip(" "))) + line)

    @staticmethod
    def _marker(style: str, n: int, paren: bool = False) -> str:
        if style in ("lower-alpha", "upper-alpha"):
            letters = "abcdefghijklmnopqrstuvwxyz"
            out = letters[(n - 1) % 26]
            out = out if style == "lower-alpha" else out.upper()
        elif style in ("lower-roman", "upper-roman"):
            out, rest = "", n
            for v, r in ((10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")):
                while rest >= v:
                    out, rest = out + r, rest - v
            out = out if style == "lower-roman" else out.upper()
        elif style == "decimal":
            out = str(n)
        else:
            raise ValueError(f"list style {style!r} is not one the ingester knows: add it with a test")
        return f"({out})" if paren else f"{out}."

    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script"):
            self.skip += 1
            return
        if tag in ("ol", "ul"):
            self._flush()
            a = dict(attrs)
            paren = False
            if tag == "ul":
                kind = "bullet"
            else:
                classes = (a.get("class") or "").split()
                drawn = [self.PAREN_CLASSES[c] for c in classes if c in self.PAREN_CLASSES] \
                    if self.paren_classes else []
                found = re.search(r"list-style-type:\s*([a-z-]+)", a.get("style") or "")
                if drawn:
                    kind, paren = drawn[0], True
                elif found:
                    if found.group(1) not in self.STYLES:
                        raise ValueError(f"list style {found.group(1)!r} is not one the ingester "
                                         f"knows: add it with a test")
                    kind = self.STYLES[found.group(1)]
                else:
                    kind = "decimal"
            start = a.get("start")
            self.lists.append([kind, int(start) if start and start.isdigit() else 1, paren])
        elif tag == "li":
            self._flush()
            kind, n, paren = self.lists[-1] if self.lists else ("bullet", 1, False)
            mark = "\u2022" if kind == "bullet" else self._marker(kind, n, paren)
            if self.lists:
                self.lists[-1][1] += 1
            self.cur.append("  " * max(len(self.lists) - 1, 0) + mark + " ")
        elif tag == "hr":
            self._flush()
            self.lines.append("")
        elif tag in self.BLOCK:
            self._flush()

    def handle_endtag(self, tag):
        if tag in ("style", "script"):
            self.skip -= 1
        elif tag in ("ol", "ul") and self.lists:
            self._flush()
            self.lists.pop()
        elif tag in self.BLOCK:
            self._flush()

    def handle_data(self, data):
        if not self.skip:
            self.cur.append(data)


def sam_toc_titles(raw: bytes) -> dict[str, str]:
    """The manual's contents page (`/Resources/SAM/TOC`): chapter number -> the title it prints
    in its link. Not a document; it is what a test checks the seed titles against."""
    page = _decode(raw)
    return {n: " ".join(html_mod.unescape(t).split()) for n, t in
            re.findall(r'<a href="/Resources/SAM/TOC/(\d+)">([^<]+)</a>', page)}


def sam_html_to_text(raw: bytes) -> str:
    """The Department of General Services' State Administrative Manual chapter view
    (`/Resources/SAM/TOC/<chapter>/Chapter-View`): the page prints the whole chapter. The text is
    the page's `Chapter nnnn - Chapter-View` line, then every section from the first section
    heading to the end of the last one, each as its heading line (`SUBJECT - number`), its
    revision line and its paragraphs. The site menu, the print button, the contents table (it
    repeats the section headings), the loading message and the scripts are not the manual."""
    page = _decode(raw)
    chapter = re.search(r"<h1>(Chapter \d+ - Chapter-View)</h1>", page)
    marker = "We are generating the manual..."
    start = page.find(marker)
    if not chapter or start < 0 or '<div class="row">' not in page[start:]:
        raise ValueError("SAM page has no chapter view region: the page layout changed")
    start = page.index('<div class="row">', start)
    last_hr = page.rfind("<hr />")
    end = page.find("<script", last_hr if last_hr > start else start)
    parser = _SamParser()
    parser.feed(page[start:end if end > 0 else len(page)])
    parser._flush()
    lines = [chapter.group(1)] + parser.lines
    text = "\n".join(lines)
    return re.sub(r"\n{3,}", "\n\n", text).strip("\n") + "\n"


def archive_eo_html_to_text(raw: bytes) -> str:
    """A California executive order printed in full inside a press-release page of the Governor's
    archive site (`www.archive.gov.ca.gov/archive/...`): the region from the centred
    `EXECUTIVE ORDER <number>` heading to the attestation (`ATTEST:` and the Secretary of State's
    name and title). The press release above it, the pointer to the PDF copy below it, the site
    menu and the news list are not the order."""
    page = _decode(raw)
    head = re.search(r"<p[^>]*>\s*<strong>\s*EXECUTIVE ORDER [A-Z]-\d+-\d+\s*</strong>\s*</p>", page)
    attest = page.find("ATTEST:", head.end()) if head else -1
    tail = re.compile(r"Secretary of State\s*</p>").search(page, attest) if attest > 0 else None
    if not head or not tail:
        raise ValueError("page has no executive order region (heading to attestation): "
                         "the page layout changed")
    parser = _SamParser()
    parser.feed(page[head.start():tail.end()])
    parser._flush()
    return "\n".join(parser.lines) + "\n"


# ---- California statutes: the Legislature's official bulk download ------------------------
#
# leginfo.legislature.ca.gov answers the toolkit's Fetcher with a Cloudflare challenge, so the
# per-section web pages cannot be fetched. The Legislature's own bulk download
# (downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip, the 2025-26 session's law tables) can:
# it is a zip of three tab-separated tables (the table of contents, its section list, the
# sections) and one small file of marked-up text (CAML) per section version. The zip is 1.2 GB,
# so it is read by HTTP range requests (its directory, the three tables, the section files
# of one slice) with the Fetcher's own client, headers and rate limit, and the snapshot is a
# JSON bundle of the raw rows and raw section files of one slice, not the zip.

CA_CODES = {"Gov.": "GOV", "Civ.": "CIV", "Pub. Contract": "PCC"}
_CA_TABLES = ("LAW_TOC_TBL.dat", "LAW_TOC_SECTIONS_TBL.dat", "LAW_SECTION_TBL.dat")
_CA_BLOCK = 4 << 20          # one range request reads this much; neighbouring members share it


def _ca_fields(line: str) -> list[str | None]:
    """One row of a pubinfo table: tab-separated, text values in backticks, NULL for empty."""
    return [None if f == "NULL" else (f[1:-1] if f.startswith("`") and f.endswith("`") else f)
            for f in line.rstrip("\n").split("\t")]


class CaZip(io.RawIOBase):
    """A read-only, seekable view of the remote bulk zip, for zipfile. Reads in aligned blocks
    (a few kept), one range request per block, each through the Fetcher's client, headers and
    per-host rate limit."""

    def __init__(self, fetcher: Fetcher, url: str):
        self.fetcher, self.url, self.pos = fetcher, url, 0
        self.blocks: dict[int, bytes] = {}
        r = self._range_get("bytes=0-0")
        if r.status_code != 206:
            raise FetchError(f"{url}: no range support (HTTP {r.status_code})")
        self.size = int(r.headers["Content-Range"].rsplit("/", 1)[1])
        self.last_modified = r.headers.get("Last-Modified", "")

    def _range_get(self, rng: str) -> httpx.Response:
        """One ranged GET with what `Fetcher.get` does for a plain one: the per-host rate limit, a 429
        waited out (`Retry-After`, else the Fetcher's backoff steps) and retried, then `Refused`; a
        401/403 is `Refused`, or `Challenge` under Cloudflare's `cf-mitigated`; a connection dropped
        without an answer is `Refused`. (The toolkit has no ranged get yet; when it does, this goes.)"""
        f, host = self.fetcher, urllib.parse.urlsplit(self.url).netloc
        for attempt in range(len(f.backoff) + 1):
            f._throttle(self.url)
            try:
                r = f.client().get(self.url, headers={"Range": rng})
            except httpx.RemoteProtocolError as e:
                raise Refused(f"{self.url}: connection closed without a response ({e})") from e
            code = r.status_code
            if code == 429 and attempt < len(f.backoff):
                try:
                    wait = float(r.headers.get("Retry-After", ""))
                except ValueError:
                    wait = f.backoff[attempt]
                f._log(f"    429 from {host} -- backing off {wait:g}s (attempt {attempt + 1}/{len(f.backoff)})")
                f._sleep(wait)
                continue
            if code in (401, 403, 429):
                mitigated = r.headers.get("cf-mitigated", "")
                raise (Challenge if mitigated == "challenge" else Refused)(
                    f"{self.url}: HTTP {code} on range {rng}"
                    f"{' (Cloudflare managed challenge)' if mitigated else ''}")
            return r
        raise FetchError(f"{self.url}: unreachable after backoff")   # pragma: no cover

    def seekable(self): return True
    def readable(self): return True
    def tell(self): return self.pos

    def seek(self, offset, whence=0):
        self.pos = {0: offset, 1: self.pos + offset, 2: self.size + offset}[whence]
        return self.pos

    def _block(self, n: int) -> bytes:
        if n not in self.blocks:
            if len(self.blocks) >= 4:
                self.blocks.pop(next(iter(self.blocks)))
            start, end = n * _CA_BLOCK, min((n + 1) * _CA_BLOCK, self.size) - 1
            r = self._range_get(f"bytes={start}-{end}")
            if r.status_code != 206:
                raise FetchError(f"{self.url}: range {start}-{end} answered HTTP {r.status_code}")
            self.blocks[n] = r.content
        return self.blocks[n]

    def read(self, size=-1):
        if size is None or size < 0 or self.pos + size > self.size:
            size = self.size - self.pos
        out = []
        while size > 0:
            n, off = divmod(self.pos, _CA_BLOCK)
            chunk = self._block(n)[off:off + size]
            if not chunk:
                break
            out.append(chunk)
            self.pos += len(chunk)
            size -= len(chunk)
        return b"".join(out)

    def readinto(self, b):
        data = self.read(len(b))
        b[:len(data)] = data
        return len(data)


_CA_OPEN: dict[int, tuple] = {}      # id(fetcher) -> (fetcher, zipfile, CaZip): the directory is read once


def ca_open(fetcher: Fetcher, url: str):
    held = _CA_OPEN.get(id(fetcher))
    if held and held[0] is fetcher:
        return held[1], held[2]
    raw = CaZip(fetcher, url)
    zf = zipfile.ZipFile(io.BufferedReader(raw, buffer_size=1 << 16))
    _CA_OPEN[id(fetcher)] = (fetcher, zf, raw)
    return zf, raw


_CA_ROWS: "weakref.WeakKeyDictionary" = weakref.WeakKeyDictionary()   # zip -> {table: [(line, fields)]}


def _ca_table(zf, name: str) -> list[tuple[str, list]]:
    """A table of the zip, parsed once per open zip (the section table alone is 43 MB)."""
    tables = _CA_ROWS.setdefault(zf, {})
    if name not in tables:
        tables[name] = [(l, _ca_fields(l)) for l in zf.read(name).decode("utf-8").splitlines()]
    return tables[name]


def ca_bundle(zf, slice_: dict, url: str, last_modified: str = "") -> bytes:
    """The raw rows and section files of one slice, as JSON. A slice is `{code, path}` (a
    table-of-contents node: every section under it) or `{code, section}` (one section number).
    Kept: the node's ancestors' and descendants' table-of-contents rows, and for each section its
    section-list row, its section row and its section file, all as the download holds them. When
    a section number has several versions in the list (an amendment operative on a later date),
    every version is kept."""
    code, path, number = slice_.get("code"), slice_.get("path"), slice_.get("section")
    if not code or bool(path) == bool(number):
        raise ValueError("a California statute slice needs a code and exactly one of path or section")
    toc = [(l, f) for l, f in _ca_table(zf, "LAW_TOC_TBL.dat") if f[0] == code]
    sec_list = [(l, f) for l, f in _ca_table(zf, "LAW_TOC_SECTIONS_TBL.dat") if f[1] == code]
    if number:
        want = [(l, f) for l, f in sec_list if (f[3] or "").rstrip(".") == number.rstrip(".")]
        if not want:
            raise ValueError(f"no section {code} {number} in the download")
        paths = {f[2] for _, f in want}
        if len(paths) != 1:
            raise ValueError(f"section {code} {number} sits under more than one node: the slice is a guess")
        path = paths.pop()
        nodes = [(l, f) for l, f in toc if f[13] == path or path.startswith((f[13] or "?") + ".")]
    else:
        nodes = [(l, f) for l, f in toc
                 if f[13] == path or (f[13] or "").startswith(path + ".") or path.startswith((f[13] or "?") + ".")]
        if not any(f[13] == path for _, f in nodes):
            raise ValueError(f"no table of contents node {code} {path} in the download")
        keep = {f[13] for _, f in nodes if f[13] == path or f[13].startswith(path + ".")}
        want = [(l, f) for l, f in sec_list if f[2] in keep]
        if not want:
            raise ValueError(f"no section under {code} {path} in the download")
    nodes.sort(key=lambda lf: int(lf[1][10]))
    by_version = {}
    versions = {w[1][11] for w in want}
    for l, f in _ca_table(zf, "LAW_SECTION_TBL.dat"):
        if f[1] == code and f[7] in versions:
            by_version[f[7]] = (l, f)
    sections = []
    order = {n[1][13]: int(n[1][10]) for n in nodes}
    for l, f in sorted(want, key=lambda lf: (order.get(lf[1][2], 0), int(lf[1][4]))):
        if f[11] not in by_version:
            raise ValueError(f"section {f[3]}: no row in LAW_SECTION_TBL.dat for version {f[11]}")
        row, rf = by_version[f[11]]
        member = rf[14]
        sections.append({"toc_section_row": l, "law_section_row": row, "lob_member": member,
                         "lob": zf.read(member).decode("utf-8")})
    doc = {"format": "leginfo-pubinfo-slice/1", "source": url, "zip_last_modified": last_modified,
           "slice": slice_, "toc_rows": [l for l, _ in nodes], "sections": sections}
    return (json.dumps(doc, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


class _CamlParser(HTMLParser):
    """One section's marked-up text (CAML): a line per paragraph or table cell paragraph, inline
    markup (italics, the thin and en space marks) folded into the line."""

    BLOCK = {"p", "tr", "td", "br", "table"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lines: list[str] = []
        self.cur: list[str] = []

    def _flush(self):
        line = " ".join("".join(self.cur).split())
        self.cur = []
        if line:
            self.lines.append(line)

    def handle_starttag(self, tag, attrs):
        if tag == "span":
            self.cur.append(" ")
        elif tag in self.BLOCK:
            self._flush()

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag in self.BLOCK:
            self._flush()

    def handle_data(self, data):
        self.cur.append(data)


def caml_to_lines(caml: str) -> list[str]:
    parser = _CamlParser()
    parser.feed(caml)
    parser._flush()
    return parser.lines


def ca_bundle_to_text(raw: bytes) -> str:
    """The slice's text: the headings from the title down to the node (and any article headings
    inside it, each with the history note the table prints under it), then each section as its
    number and first paragraph on one line, the following paragraphs one per line, and the
    section's history line as the download holds it. Order is the download's: node sequence, then
    section order."""
    doc = json.loads(raw)
    if doc.get("format") != "leginfo-pubinfo-slice/1":
        raise ValueError("not a California slice bundle")
    nodes = sorted((_ca_fields(r) for r in doc["toc_rows"]), key=lambda f: int(f[10]))
    sections: dict[str, list[dict]] = {}
    for s in doc["sections"]:
        sections.setdefault(_ca_fields(s["toc_section_row"])[2], []).append(s)
    out: list[str] = []
    for f in nodes:
        out.append(_clean_line(f[6]))
        note = _clean_line(f[15] or "")
        if note:
            out.append(note)
        for s in sections.get(f[13], []):
            number = _ca_fields(s["toc_section_row"])[3]
            body = caml_to_lines(s["lob"])
            if not body:
                raise ValueError(f"section {number} has no text in its section file")
            out.append(f"{number} {body[0]}")
            out.extend(body[1:])
            history = _clean_line(_ca_fields(s["law_section_row"])[13] or "")
            if history:
                out.append(history)
    return "\n".join(out) + "\n"


def ca_snapshot(src: dict, fetcher: Fetcher, dest: Path, refetch: bool) -> tuple[bytes, bool]:
    """Like Fetcher.snapshot, for a California statute slice: reuse the committed bundle unless
    `refetch`, else build it from the bulk download."""
    if dest.is_file() and not refetch:
        return dest.read_bytes(), False
    zf, raw = ca_open(fetcher, src["url"])
    bundle = ca_bundle(zf, src["slice"], src["url"], raw.last_modified)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(bundle)
    return bundle, True


def sos_html_to_text(raw: bytes) -> str:
    """A California Code of Regulations chapter as the Secretary of State publishes it
    (sos.ca.gov/administration/regulations/...): the page's `Title`, `Division` and `Chapter`
    headings, the chapter's contents list and every regulation with its note. The region is the
    page's content column (a page may print a `California Code of Regulations` line above the
    headings); text the page keeps inside an HTML comment is not shown and not taken; the site menu,
    breadcrumb, side navigation and footer are not the regulations. The page's stylesheet hides the
    browser's list markers on its `alphaLwr`, `numPrnthsis`, `alphaUppr`, `romanLwr` (and `Inline`
    and `romanUppr`) lists and draws `(a)`, `(1)`, `(A)`, `(i)` with `::before`; those lists are
    written that way, the form the regulations cite their subdivisions in."""
    page = _decode(raw)
    start = page.find('id="main-content-normal"')
    side = page.find('id="left-sidebar"', start) if start >= 0 else -1
    if start < 0 or side < 0 or "Title " not in page[start:side]:
        raise ValueError("page has no regulation region (content column with a Title heading): "
                         "the page layout changed")
    start = page.index(">", start) + 1
    end = page.rindex("<div", 0, side)
    parser = _SamParser(paren_classes=True)
    parser.feed(page[start:end])
    parser._flush()
    return "\n".join(parser.lines) + "\n"


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
    `{article: "73"}` runs from the line `ARTICLE 73` to the next `ARTICLE n` heading line (or to
    the title-level group heading printed before it, which belongs to neither article), and
    `{article: "33.5", part: "19"}` runs from the body line `PART 19` inside that article to the
    next `PART n` body line. (The article's caption list prints `PART 19 COLORADO CYBERSECURITY`
    on one line; only the body heading is a line of its own.) Nothing inside a slice is dropped:
    caption lists, section text, source notes, editor's notes and annotations all stay."""
    if not slice_ or not slice_.get("article"):
        raise ValueError("a Colorado statute entry needs a slice: {article: ...} or "
                         "{article: ..., part: ...}")
    all_lines = ors_html_to_text(raw).splitlines()
    lines = all_lines
    start = _only(lines, f"ARTICLE {slice_['article']}", f"article {slice_['article']}")
    end = next((i for i in range(start + 1, len(lines)) if _CRS_ARTICLE.fullmatch(lines[i])),
               len(lines))
    # The file prints a title-level group heading (LIBRARIES, STATE FUNDS, ...) between the last
    # article of one group and the next ARTICLE line, so a slice would take it as its own last
    # line. The contents list at the top of the file names every group heading (an all-caps
    # line followed by `Art. n` lines); an article ends before the first one of them.
    groups = {line for i, line in enumerate(all_lines[:-1])
              if line == line.upper() and line != line.lower()
              and all_lines[i + 1].startswith("Art. ")}
    lines = all_lines[start:end]
    cut = next((i for i, line in enumerate(lines) if i and line in groups), len(lines))
    lines = lines[:cut]
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
    if fmt == "json" and doc_type == "statute" and jurisdiction == "california":
        return ca_bundle_to_text(raw)
    if fmt == "html" and doc_type == "rule" and jurisdiction == "california":
        return sos_html_to_text(raw)
    if fmt == "html" and doc_type == "policy" and jurisdiction == "california":
        return sam_html_to_text(raw)
    if fmt == "html" and doc_type == "executive_order" and jurisdiction == "california":
        return archive_eo_html_to_text(raw)
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
    if src["doc_type"] == "policy" and src["jurisdiction"] == "california":
        chapter = re.fullmatch(r"SAM chapter (\d+)", src["citation"])
        if not chapter or not text.startswith(f"Chapter {chapter.group(1)} - Chapter-View\n"):
            raise ValueError(f"{src['id']}: page is not the cited instrument: "
                             f"{src['citation']!r} does not match the chapter view's first line")
        # the chapter view does not print the chapter's title; the seed title must be the form built
        # from the manual's contents page (a test compares every seed title with a fetched copy of it)
        prefix = f"State Administrative Manual chapter {chapter.group(1)}: "
        if not src["title"].startswith(prefix) or not src["title"][len(prefix):].strip():
            raise ValueError(f"{src['id']}: seed title {src['title']!r} is not "
                             f"{prefix!r} followed by the chapter's title in the manual's contents page")
        return
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
    if src["doc_type"] == "rule" and src["jurisdiction"] == "california":
        cite = re.fullmatch(r"Cal\. Code Regs\., tit\. (\d+), div\. (\d+), ch\. ([\d.]+)", src["citation"])
        want = [f"Title {cite.group(1)}.", f"Division {cite.group(2)}.", f"Chapter {cite.group(3)}."] if cite else None
        head = text.splitlines()[:5]
        got = [next((l for l in head if l.startswith(w.split(" ")[0] + " ")), "") for w in (want or ["", "", ""])]
        if (not cite or [" ".join(l.split(" ")[:2]) for l in got] != want
                or got[2][len(want[2]) + 1:] != src["title"]):
            raise ValueError(f"{src['id']}: page is not the cited instrument: {src['citation']!r} "
                             f"does not match the page's title, division and chapter headings")
        return
    if src["doc_type"] == "rule" and src["title"] not in text:
        raise ValueError(f"{src['id']}: page does not carry the seed title {src['title']!r}")
    if src["doc_type"] == "executive_order" and src["jurisdiction"] == "california":
        cite = re.fullmatch(r"Executive Order ([A-Z]-\d{1,2}-\d{2})", src["citation"])
        if not cite or text.splitlines()[:1] != [f"EXECUTIVE ORDER {cite.group(1)}"]:
            raise ValueError(f"{src['id']}: page is not the cited instrument: {src['citation']!r} "
                             f"does not match the order's heading line")
        return
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
    if src["doc_type"] == "statute" and src["jurisdiction"] == "california":
        cite = re.fullmatch(r"Cal\. (Gov\.|Civ\.|Pub\. Contract) Code \u00a7\u00a7? ([\d.]+[a-z]?)(?:-([\d.]+[a-z]?))?",
                            src["citation"])
        sl = src.get("slice") or {}
        # a section line is its number, then its first paragraph, e.g. `11549.64. As used in ...`
        nums = [l.split(" ", 1)[0].rstrip(".") for l in text.splitlines()
                if re.match(r"\d+(\.\d+)*[a-z]?\. ", l)]
        if (not cite or CA_CODES.get(cite.group(1)) != sl.get("code") or not nums
                or (nums[0], nums[-1]) != (cite.group(2).rstrip("."), (cite.group(3) or cite.group(2)).rstrip("."))
                or (sl.get("section") and set(nums) != {sl["section"].rstrip(".")})):
            raise ValueError(f"{src['id']}: page is not {src['citation']} (code or section range mismatch)")
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
    if src["doc_type"] == "rule" and src["jurisdiction"] == "california":
        return ("Text taken from the Secretary of State's page for the chapter of the California Code of "
                "Regulations: the title, division and chapter headings, the chapter's contents list and each "
                "regulation with its note, one line per paragraph, with markup, the site menu, side "
                "navigation, footer and non-breaking spaces removed. The page's stylesheet draws each "
                "subdivision designator, so they are written as it shows them: (a), (1), (A), (i). A list with none of the "
                "stylesheet's classes keeps the browser's own marker (a.).")
    if src["doc_type"] == "executive_order" and src["jurisdiction"] == "california":
        return ("Text taken from the Governor's archive site page that prints the order in full: the heading "
                "line, the recitals (WHEREAS), the orders, the signature and the attestation, one line per "
                "paragraph, with markup and non-breaking spaces removed. The press release above the order, "
                "the pointer to the PDF copy below it, the site menu and the news list are not the order.")
    if src["doc_type"] == "policy" and src["jurisdiction"] == "california":
        return ("Text taken from the Department of General Services' State Administrative Manual chapter "
                "view page: the chapter line, then each section's heading, revision line and "
                "paragraphs, one line per paragraph, with markup, the site menu, the page's contents "
                "table, scripts and non-breaking spaces removed. List numbers and letters, which the "
                "page draws with style rules, are written out (1., a., i.); bullets are written as "
                "a bullet character.")
    if src["doc_type"] == "statute" and src["jurisdiction"] == "california":
        return ("The source is the Legislature's bulk download of the law tables (pubinfo_2025.zip), "
                "because the per-section pages refuse the Fetcher. This document is the one slice named "
                "in the citation: the table of contents' headings from the title down to the slice, "
                "then each section as its number and first paragraph, further paragraphs one per line, "
                "and the section's history line as the download holds it (the table's own note under "
                "a heading is kept). Section markup and spacing marks removed, one line per paragraph. "
                "The snapshot is the JSON bundle of the slice's raw rows and section files, not the zip.")
    if src["doc_type"] == "statute" and src["jurisdiction"] == "colorado":
        return ("The source is the Office of Legislative Legal Services' title file (one file for the whole of "
                "the title); this document is the one article (or part) named in the citation, "
                "from its ARTICLE (or PART) heading line to the next one (an article stops "
                "before the title-level group heading, such as LIBRARIES, that the file prints "
                "between articles), one line per source paragraph, with markup, spacing paragraphs and non-breaking spaces removed. "
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
    if src["doc_type"] == "statute" and src["jurisdiction"] == "california":
        raw, fresh = ca_snapshot(src, fetcher, snap_path, refetch)
    else:
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
