"""California: the Legislature's bulk download, the Secretary of State's CCR pages, DGS's State Administrative
Manual, the Department of Technology's pages and letters, and the Governor's archive orders. Hooks are described
in src/states/__init__.py."""
from __future__ import annotations

import html as html_mod
import io
import json
import re
import urllib.parse
import weakref
import zipfile
from html.parser import HTMLParser
from pathlib import Path

import httpx
from corpus_toolkit.sources.fetch import Challenge, FetchError, Fetcher, Refused

from src.ingest_common import _MONTHS, BlockParser, _clean_line, _decode, _printed_version, _squash
from src.states import UNHANDLED


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
    parser = BlockParser()
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
    parser = BlockParser()
    parser.feed(page[head.start():tail.end()])
    parser._flush()
    return "\n".join(parser.lines) + "\n"


# ---- California Department of Technology: Technology Letters and SIMM pages --------------
#
# www.cdt.ca.gov answers the toolkit's httpx client with a Cloudflare managed challenge and answers
# system curl, sending the same User-Agent, with HTTP 200 (the Fetcher's opt-in curl transport,
# see `make_fetcher`). Its letters and SIMM sections are WordPress pages built with Divi: the
# instrument is the page from its <h1> to the department's footer section, minus the side and
# "On this page" navigation (<nav>) and the print button.

class _CdtParser(BlockParser):
    """The text of a CDT page region. Block elements start a line (as in the SAM parser); a table
    row is one line with its cells joined by ` | `; <nav> elements and the print button are
    not text of the instrument."""

    def __init__(self):
        super().__init__()
        self.nav = 0
        self.print_button = False
        self.cells = 0

    def _flush(self):
        """As the SAM parser, except that spaces the page's markup puts before a line are not
        indentation: only a nested list item (a bullet or a number) is indented."""
        raw = "".join(self.cur)
        self.cur = []
        line = " ".join(raw.split())
        if line:
            lead = len(raw) - len(raw.lstrip(" "))
            self.lines.append(" " * lead + line if lead and re.match(r"(\u2022|\d+\.|[a-z]+\.) ", line) else line)

    def handle_starttag(self, tag, attrs):
        if tag == "nav":
            self._flush()
            self.nav += 1
            return
        if self.nav:
            return
        if tag == "span" and dict(attrs).get("id") == "printbutton":
            self.print_button = True
            return
        if tag in ("td", "th"):
            if self.cells:
                self.cur.append(" | ")
            self.cells += 1
            return
        if tag == "tr":
            self.cells = 0
        super().handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag == "nav":
            self.nav = max(self.nav - 1, 0)
            return
        if self.nav:
            return
        if tag == "span" and self.print_button:
            self.print_button = False
            return
        if tag in ("td", "th"):
            return
        super().handle_endtag(tag)

    def handle_data(self, data):
        if not self.nav and not self.print_button:
            super().handle_data(data)


def cdt_html_to_text(raw: bytes) -> str:
    """A Department of Technology page (`www.cdt.ca.gov`): the page's <h1> to the start of the
    footer section (the Divi section that holds the `footer-heading` headings), one line per
    paragraph, heading, list item and table row. The site menu, the side navigation, the page's
    contents list ("On this page"), the print button, scripts and the footer are not the instrument."""
    page = _decode(raw)
    start = page.find("<h1")
    foot = page.find("footer-heading")
    end = page.rfind('<div class="et_pb_section', 0, foot) if foot >= 0 else -1
    if start < 0 or end <= start:
        raise ValueError("no CDT page region (heading to footer section): the page layout changed")
    parser = _CdtParser()
    parser.feed(page[start:end])
    parser._flush()
    return re.sub(r"\n{3,}", "\n\n", "\n".join(parser.lines)).strip("\n") + "\n"


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
    parser = BlockParser(paren_classes=True)
    parser.feed(page[start:end])
    parser._flush()
    return "\n".join(parser.lines) + "\n"


# What California letters and orders print instead of an effective date (read from the text as
# `derive` makes it): an ITPL or letter PDF prints `DATE ISSUED:` with a date (a day, or only a
# month and year) a few lines on, in its second column; a Technology Letter web page prints its
# month and year as line 2; a SIMM page's heading says `Revised May 2023`; a SIMM PDF's cover prints its month under the title; an executive order
# prints `this 30th day of March 2026` where the Governor signs. A day is an effective_date; a
# month alone is a source_version, never a day made up.
_CA_ISSUED = re.compile(r"DATE\s+ISSUED:", flags=re.I)


_CA_WIN = 150


_CA_FULL = re.compile(rf"\b({_MONTHS})\s+(\d{{1,2}}),\s+(\d{{4}})\b", flags=re.I)


_CA_MONTH = re.compile(rf"\b({_MONTHS})\s+(\d{{4}})\b", flags=re.I)


_CA_SIGNED = re.compile(rf"\bthis\s+(\d{{1,2}})(?:st|nd|rd|th)\s+day\s+of\s+({_MONTHS})\s+(\d{{4}})\b")


_CA_REVISED = re.compile(rf"\b((?:Revised|Updated)\s+(?:{_MONTHS})\s+\d{{4}})\s*$")


def _iso(month: str, day: str, year: str) -> str | None:
    mon = [m.casefold() for m in _MONTHS.split("|")].index(month.casefold()) + 1
    return f"{int(year):04d}-{mon:02d}-{int(day):02d}" if 1 <= int(day) <= 31 else None


def _ca_dates(text: str, doc_type: str) -> tuple[str | None, str]:
    """(effective_date, source_version) as a California letter, page or order prints them."""
    if doc_type == "executive_order":
        m = _CA_SIGNED.search(" ".join(text.split()))
        return (_iso(m.group(2), m.group(1), m.group(3)) if m else None), ""
    lines = text.splitlines()
    m = _CA_ISSUED.search(text)
    if m:
        window = " ".join(text[m.end():m.end() + 4 * _CA_WIN].split())[:_CA_WIN]
        full, month = _CA_FULL.search(window), _CA_MONTH.search(window)
        if full and (not month or full.start() <= month.start()):
            return _iso(full.group(1), full.group(2), full.group(3)), ""
        if month:
            return None, f"{month.group(1).title()} {month.group(2)}"
    if len(lines) > 1 and re.fullmatch(rf"({_MONTHS}) \d{{4}}", lines[1].strip()):
        return None, lines[1].strip()
    if lines and (m := _CA_REVISED.search(lines[0])):
        return None, m.group(1)
    head = [l.strip() for l in lines if l.strip()][:15]
    if head and head[0].startswith("State of California"):      # a SIMM section's cover page
        m = re.search(rf"\b((?:Revised\s+|Updated\s+)?(?:{_MONTHS})\s+\d{{4}})\b", " ".join(head))
        if m:
            return None, m.group(1)
    return None, ""


def _is_cdt(src: dict) -> bool:
    return src["jurisdiction"] == "california" \
        and urllib.parse.urlsplit(src.get("url") or "").hostname == "www.cdt.ca.gov"


_COVER_NUMBER = re.compile(r"(?:statewide information management manual|\bsimm)\s*[\u2013-]?\s*(?:section\s+)?"
                           r"(\d+[a-z]?(?:-[a-z])?)(?![\w.-])", flags=re.I)


_CITED_NUMBER = re.compile(r"SIMM (\d+[A-Z]?(?:-[A-Z])?)(?![\w-])(?: Appendix ([A-Z]))?")   # 'SIMM 45 Appendix F' is section 45F


_LETTER = re.compile(r"^(TL|ITPL) ", flags=re.I)


def _check_cdt_identity(src: dict, text: str, what_is: str) -> None:
    """A Department of Technology document is the cited one when it prints the identity where its
    own heading is: a web page's first line (the h1) starts with the citation or `identity_text`
    and goes no further into a longer number (SIMM 40 is not the page headed SIMM 40A); a letter
    PDF (TL, ITPL) carries `identity_text` in its header block, before its SUBJECT and REFERENCES
    (a letter that cites another prints that number in its references); any other PDF or Word file (a SIMM
    section) carries `identity_text` or the seed title on its cover, the first 15 lines, and, when
    the cover prints a SIMM section number (`Statewide Information Management Manual - Section 19F`),
    it is the citation's (SIMM 19E.1 is section 19E)."""
    key = src.get("identity_text")
    fmt_pdf = what_is in ("PDF", "Word file")      # a Word file has a cover, as a PDF does
    lines = [l for l in text.splitlines() if l.strip()]

    def refuse(want: str):
        raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {want}")

    if not fmt_pdf:
        want = key or src["citation"]
        first = _squash(lines[0]) if lines else ""
        if not re.match(re.escape(_squash(want)) + r"(?![\w.-])", first):
            refuse(f"{want!r} is not what the page's first line starts with")
        return
    if what_is == "PDF" and _LETTER.match(src["citation"]) and key:
        header = re.split(r"SUBJECT:|REFERENCES:", " ".join(lines[:12]), maxsplit=1, flags=re.I)[0]
        if not re.search(r"(?<![\w-])" + re.escape(_squash(key)) + r"(?![\w-])", _squash(header)):
            refuse(f"{key!r} is not in the letter's header block (before SUBJECT and REFERENCES)")
        return
    want = key or src["title"]
    cover = " ".join(lines[:15])
    if _squash(want) not in _squash(cover):
        refuse(f"{want!r} is not on the cover (the first 15 lines)")
    printed, cited = _COVER_NUMBER.search(cover), _CITED_NUMBER.match(src["citation"])
    if printed and cited and printed.group(1).casefold() != (cited.group(1) + (cited.group(2) or "")).casefold():
        refuse(f"the cover prints SIMM section {printed.group(1)}, the citation is {src['citation']!r}")


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "json" and doc_type == "statute":
        return ca_bundle_to_text(raw)
    if fmt == "html" and doc_type == "rule":
        return sos_html_to_text(raw)
    if fmt == "html" and doc_type in ("policy", "standard") and host == "www.cdt.ca.gov":
        return cdt_html_to_text(raw)
    if fmt == "html" and doc_type == "policy":
        return sam_html_to_text(raw)
    if fmt == "html" and doc_type == "executive_order":
        return archive_eo_html_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if _is_cdt(src) and src["doc_type"] in ("policy", "standard"):
        _check_cdt_identity(src, text, what_is)
        return True
    if src["doc_type"] == "policy" and src["jurisdiction"] == "california" \
            and src["citation"].startswith("SAM chapter"):
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
        return True
    if src["doc_type"] == "rule" and src["jurisdiction"] == "california":
        cite = re.fullmatch(r"Cal\. Code Regs\., tit\. (\d+), div\. (\d+), ch\. ([\d.]+)", src["citation"])
        want = [f"Title {cite.group(1)}.", f"Division {cite.group(2)}.", f"Chapter {cite.group(3)}."] if cite else None
        head = text.splitlines()[:5]
        got = [next((l for l in head if l.startswith(w.split(" ")[0] + " ")), "") for w in (want or ["", "", ""])]
        if (not cite or [" ".join(l.split(" ")[:2]) for l in got] != want
                or got[2][len(want[2]) + 1:] != src["title"]):
            raise ValueError(f"{src['id']}: page is not the cited instrument: {src['citation']!r} "
                             f"does not match the page's title, division and chapter headings")
        return True
    if src["doc_type"] == "executive_order" and src["jurisdiction"] == "california":
        cite = re.fullmatch(r"Executive Order ([A-Z]-\d{1,2}-\d{2})", src["citation"])
        # the order prints its heading on a line of its own after the "EXECUTIVE DEPARTMENT / STATE OF
        # CALIFORNIA" letterhead (which pdftotext sometimes splits into odd words) and before the first
        # WHEREAS; a page prints it as its first line. A letter that cites the order has no WHEREAS.
        lines = [_squash(l) for l in text.splitlines() if l.strip()]
        first = next((i for i, l in enumerate(lines) if l.startswith("whereas")), None)
        head = lines[:first] if first is not None else []
        if not cite or f"executive order {cite.group(1).casefold()}" not in head[:8]:
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {src['citation']!r} "
                             f"does not match the order's heading line (the line after the letterhead, before "
                             f"the first WHEREAS)")
        return True
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
        return True
    return False


def effective_date(text, doc_type):
    return printed if (printed := _ca_dates(text, doc_type)[0]) else UNHANDLED


def source_version(text, doc_type, fmt):
    return _ca_dates(text, doc_type)[1] or (_printed_version(text) if fmt == "docx" else "")


def notes(src, fmt, text):
    if fmt == "html" and src["jurisdiction"] == "california" \
            and urllib.parse.urlsplit(src.get("url") or "").hostname == "www.cdt.ca.gov":
        return ("Text taken from the California Department of Technology's web page for the instrument: "
                "from the page heading to the end of the page's content, one line per paragraph, heading, "
                "list item and table row (a table row's cells are joined by ' | '), with markup, the site "
                "menu, the side navigation, the page's contents list ('On this page'), the print button, "
                "scripts, the footer and non-breaking spaces removed.")
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
    return None


def extra_notes(src, fmt, text, eff, version):
    notes = ""
    if src["doc_type"] == "executive_order" and eff:
        notes += (" effective_date is the date the Governor signed the order, as its closing paragraph "
                  "prints it (this Nth day of Month Year); the order prints no other date.")
    elif eff:
        notes += " effective_date is the date the letter prints as issued (DATE ISSUED)."
    if version:
        notes += (" source_version is the month, or the revision month, the document prints "
                  "(a month with no day is not made into a date).")
    return notes


def snapshot(src, fetcher, dest, refetch):
    if src["doc_type"] == "statute":
        return ca_snapshot(src, fetcher, dest, refetch)
    return None
