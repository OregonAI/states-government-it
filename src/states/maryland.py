"""Maryland: DoIT's SharePoint policy pages, the Division of State Documents' COMAR and executive-order pages, and the
General Assembly's statute section pages. Hooks are described in src/states/__init__.py. DoIT's PDFs are shared.

DoIT pages (`doit.maryland.gov`): the page's `<main id="mdgovMain">` holds an `<h1>` and one rich-text field; the
menus, header and footer are outside it. COMAR and executive orders (`raw.githubusercontent.com/maryland-dsd/law-html`,
the Division of State Documents' own bulk publication): the `<article class="content">` of each file.
Statutes (`mgaleg.maryland.gov/mgawebsite/Laws/StatuteText`): the site serves one section per page, so a document is a
bundle of the sections its seed entry lists, built by `snapshot` from the `StatuteText` fragment of each page."""
from __future__ import annotations

import html as html_mod
import re
from html.parser import HTMLParser
from pathlib import Path

from src.ingest_common import _squash
from src.states import UNHANDLED

_ZERO_WIDTH = dict.fromkeys(map(ord, "​‌‍﻿"), None)
_SKIP = {"script", "style", "noscript", "button", "svg", "select", "form"}
_VOID = {"img", "input", "br", "hr", "wbr", "meta", "link", "area", "base", "col", "embed", "source", "track"}
_BLOCK = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "div", "li", "ul", "ol", "table", "summary", "details",
          "section", "aside", "article", "blockquote", "br"}


class _Blocks(HTMLParser):
    """One output line per block element; a list item carries its marker (a bullet, or `n.` in an ordered list) and
    is indented two spaces per nesting level; a table row is one line with its cells joined by ' | '; text inside a
    cell runs together; elements hidden with `display:none` and scripts, styles, buttons and pictures are not read."""

    def __init__(self, indent_classes: bool = False):
        super().__init__(convert_charrefs=True)
        self.lines: list[str] = []
        self.cur: list[str] = []
        self.lists: list[list] = []        # [ordered, next number]
        self.prefix = ""                   # the pending list marker, written before the next text
        self.indent = ""                   # indentation from a `text-indent-N` class (COMAR)
        self.skip: list[str] = []          # stack of hidden tags
        self.in_row = False
        self.cells: list[str] = []
        self.indent_classes = indent_classes

    def _flush(self):
        line = " ".join("".join(self.cur).translate(_ZERO_WIDTH).replace("\xa0", " ").split())
        self.cur = []
        if line:
            self.lines.append(self.indent + self.prefix + line)
            self.prefix = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in _VOID:
            # a void element has no end tag, so it must never be pushed on the skip stack; a picture or a field
            # shows no text of its own, and `br` still ends a line
            if not self.skip and tag == "br":
                if self.in_row:
                    self.cur.append(" ")
                else:
                    self._flush()
            return
        if self.skip:
            if tag == self.skip[-1]:
                self.skip.append(tag)
            return
        if tag in _SKIP or "display:none" in (a.get("style") or "").replace(" ", "") or "hidden" in a:
            self.skip.append(tag)
            return
        if tag == "tr":
            self._flush()
            self.in_row, self.cells = True, []
            return
        if tag in ("td", "th"):
            self.cur = []
            return
        if self.in_row:
            self.cur.append(" ")
            return
        if tag in ("ul", "ol"):
            self._flush()
            self.lists.append([tag == "ol", 1])
            return
        if tag in _BLOCK:
            self._flush()
        if tag == "li" and self.lists:
            ordered, n = self.lists[-1]
            self.prefix = "  " * (len(self.lists) - 1) + (f"{n}. " if ordered else "• ")
            self.lists[-1][1] = n + 1
        if self.indent_classes and tag == "p":
            m = re.search(r"text-indent-(\d+)", a.get("class") or "")
            self.indent = "  " * (int(m.group(1)) - 1) if m else ""

    def handle_endtag(self, tag):
        if self.skip:
            if tag == self.skip[-1]:
                self.skip.pop()
            return
        if tag in ("td", "th") and self.in_row:
            self.cells.append(" ".join("".join(self.cur).translate(_ZERO_WIDTH).replace("\xa0", " ").split()))
            self.cur = []
            return
        if tag == "tr" and self.in_row:
            self.in_row = False
            if any(self.cells):
                self.lines.append(" | ".join(self.cells))
            self.cells, self.cur = [], []
            return
        if self.in_row:
            return
        if tag in ("ul", "ol"):
            self._flush()
            if self.lists:
                self.lists.pop()
            return
        if tag in _BLOCK:
            self._flush()
        if tag == "p":
            self.indent = ""

    def handle_data(self, data):
        if not self.skip:
            self.cur.append(data)


def _blocks(fragment: str, indent_classes: bool = False) -> list[str]:
    p = _Blocks(indent_classes)
    p.feed(fragment)
    p.close()
    p._flush()
    return p.lines


def _decode(raw: bytes) -> str:
    return raw.decode("utf-8", errors="replace").lstrip("﻿")


# ---- DoIT policy pages ------------------------------------------------------------------------

def doit_page_to_text(raw: bytes) -> str:
    """A DoIT page to text: the page's main content only (its title and its rich-text field), one line per block."""
    page = _decode(raw)
    start = page.find('<main id="mdgovMain"')
    end = page.find("</main>", start) if start >= 0 else -1
    lines = _blocks(page[start:end]) if end > start else []
    if not lines:
        raise ValueError("no policy text: the page has no main content (the layout changed, or this is not a DoIT "
                         "policy page)")
    return "\n".join(lines) + "\n"


# ---- COMAR and executive orders --------------------------------------------------------------

def comar_to_text(raw: bytes) -> str:
    """A COMAR or executive-order file to text: the `<article class="content">` (heading, paragraphs with their
    numbering, the annotations and cross references), one line per paragraph, indented two spaces per level."""
    page = _decode(raw)
    start = page.find('<article class="content"')
    end = page.find("</article>", start) if start >= 0 else -1
    lines = _blocks(page[start:end], indent_classes=True) if end > start else []
    if not lines:
        raise ValueError("no COMAR text: the page has no document article (the layout changed, or this is not a "
                         "COMAR or executive-order file)")
    return "\n".join(lines) + "\n"


# ---- statutes -------------------------------------------------------------------------------

SECTION_MARK = "<!-- section "
_FRAGMENT = re.compile(r'id="StatuteText">\s*(<html>.*?</html>)', re.S)


def statute_url(article: str, section: str) -> str:
    return (f"https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article={article}"
            f"&section={section}&enactments=true")


def section_url(src, section: str) -> str:
    """The page of one section of a seed entry: the entry's own url with the section swapped, so an entry keeps the
    view it was read in. The first seven documents carry `enactments=true` ('in effect as of October 1st'); that view
    answered File Not Found for every section from 2026-11-12, and the default view prints the same law, so entries
    added after that carry no flag."""
    url = src.get("url") or ""
    if "section=" not in url:
        return statute_url(src["article"], section)
    return re.sub(r"(section=)[^&]+", lambda m: m.group(1) + section, url, count=1)


def section_fragment(page: bytes) -> bytes | None:
    """The `StatuteText` fragment of a section page, or None when the site answers `File Not Found`."""
    m = _FRAGMENT.search(_decode(page))
    return m.group(1).encode("utf-8") if m else None


def build_bundle(parts: list[tuple[str, bytes]]) -> bytes:
    """The snapshot of a statute document: each section's fragment exactly as the site served it, after a comment
    line naming the page it came from."""
    return b"".join(f"{SECTION_MARK}{url} -->\n".encode() + frag + b"\n" for url, frag in parts)


def statute_to_text(raw: bytes) -> str:
    """A bundle to text: the article line once, then each section (its number line, then one line per paragraph, the
    source's &nbsp; indentation kept as two spaces per level), a blank line before each section."""
    body = _decode(raw)
    pieces = [p for p in body.split(SECTION_MARK)[1:]]
    if not pieces:
        raise ValueError("no statute text: the snapshot has no section fragments")
    out: list[str] = []
    for piece in pieces:
        frag = piece.split("-->", 1)[1]
        frag = re.sub(r'<div class="row">.*?</div></div>', "", frag, flags=re.S)       # Previous / Next buttons
        lines = []
        for chunk in re.split(r"<br\s*/?>", re.sub(r"</?html>", "", frag)):
            m = re.match(r"((?:&nbsp;)*)(.*)", chunk, flags=re.S)
            level = len(re.findall("&nbsp;", m.group(1))) // 4
            text = " ".join(html_mod.unescape(re.sub(r"<[^>]+>", "", m.group(2))).replace("\xa0", " ").split())
            if text:
                lines.append(("  " * max(level - 1, 0)) + text)
        if not lines or not lines[0].startswith("Article - ") or len(lines) < 2:
            raise ValueError("no statute text: a section fragment has no article line and section text")
        if not out:
            out.append(lines[0])
        for heading_and_body in _versions_in_effect(lines[1:]):
            out.append("")
            out.extend(heading_and_body)
    return "\n".join(out) + "\n"


_HEADING = re.compile(r"§\S+\.(\s|$)")


def _versions_in_effect(lines: list[str]) -> list[list[str]]:
    """A page prints a section once, or twice when a later act replaces it: '§3.5–309. IN EFFECT' and then
    '§3.5–309. // EFFECTIVE JUNE 30, 2031 PER CHAPTERS 436 AND 437 OF 2026 //' with the text that takes over then.
    Only the version marked IN EFFECT is the law now; the snapshot keeps both. Returns one [heading, text...] list."""
    groups: list[list[str]] = []
    for line in lines:
        if _HEADING.match(line):
            groups.append([line])
        elif groups:
            groups[-1].append(line)
        else:
            raise ValueError("no statute text: a section fragment's text has no section number line")
    if len(groups) > 1:
        current = [g for g in groups if re.search(r"\bIN EFFECT\b", g[0])]
        if len(current) != 1:
            raise ValueError(f"a page prints {len(groups)} versions of {groups[0][0].split()[0]} and "
                             f"{len(current)} of them are marked IN EFFECT: which one is in effect is not clear")
        return current
    return groups


def snapshot(src, fetcher, dest: Path, refetch):
    """A statute document is fetched section by section (`sections:` in the seed entry, `article:` its code); other
    entries are one GET of the url (None: the shared flow does it). A section the site does not have is an error:
    the seed lists only sections read in the run that wrote it."""
    if not src.get("sections"):
        return None
    if dest.is_file() and not refetch:
        return dest.read_bytes(), False
    parts = []
    for section in src["sections"]:
        url = section_url(src, section)
        frag = section_fragment(fetcher.get(url).body)
        if frag is None:
            raise ValueError(f"{src['id']}: the General Assembly's site has no section {section} (File Not Found)")
        parts.append((url, frag))
    bundle = build_bundle(parts)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(bundle)
    return bundle, True


# ---- hooks (see src/states/__init__.py) ------------------------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt != "html":
        return None
    if doc_type == "statute" and host == "mgaleg.maryland.gov":
        return statute_to_text(raw)
    if doc_type in ("policy", "standard") and host.endswith("doit.maryland.gov"):
        return doit_page_to_text(raw)
    if doc_type in ("rule", "executive_order") and host == "raw.githubusercontent.com":
        return comar_to_text(raw)
    return None


def _printed_section(number: str) -> str:
    return "§" + number.replace("-", "–") + "."


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "maryland":
        return False
    sid, kind = src["id"], src["doc_type"]
    if src.get("sections"):
        listed = [_printed_section(n) for n in src["sections"]]
        printed = [m.group(1) for m in re.finditer(r"(?:^|\n)\n(§\S+?\.)(?:\s|\n|$)", text)]
        for number, mark in zip(src["sections"], listed):
            if mark not in printed:
                raise ValueError(f"{sid}: {what_is} is not the cited instrument: section {number} does not appear in its text")
        extra = [m for m in printed if m not in listed]
        if extra:
            raise ValueError(f"{sid}: {what_is} holds {', '.join(extra)}, which the seed entry does not list in its "
                             f"sections: the bundle and the seed list have drifted apart (section not listed)")
        if printed != listed:
            raise ValueError(f"{sid}: {what_is} holds the listed sections in another order than the seed entry "
                             f"(bundle order {printed}, listed order {listed})")
        return True
    if what_is != "page":
        return False                                   # PDFs: the shared check (identity_text, number, title)
    if kind == "executive_order":
        number = re.search(r"\d\d\.\d\d\.\d{4}\.\d+", src["citation"])
        if not number or not text.startswith(f"Executive Order {number.group(0)}\n"):
            raise ValueError(f"{sid}: {what_is} is not the cited instrument: 'Executive Order "
                             f"{number and number.group(0)}' is not its heading")
        return True
    if kind == "rule" and re.search(r"\d+\.\d+\.\d+\.\d+\s*$", src["citation"]):
        # a single regulation: its file prints only `.05 Heading.`, so the section number comes from the citation
        number = re.search(r"\.(\d+)\s*$", src["citation"]).group(1)
        first = text.split("\n", 1)[0]
        if not re.fullmatch(rf"\.{number} {re.escape(src['title'])}\.?", first):
            raise ValueError(f"{sid}: {what_is} is not the cited instrument: '.{number} {src['title']}' is not its "
                             f"heading (the file's first line is {first!r})")
        return True
    if kind == "rule":
        if not text.startswith(src["title"] + "\n"):
            raise ValueError(f"{sid}: {what_is} is not the cited instrument: {src['title']!r} is not its heading")
        return True
    if kind in ("policy", "standard"):
        want = src.get("identity_text") or src["title"]
        if _squash(want) not in _squash(text):
            raise ValueError(f"{sid}: {what_is} is not the cited instrument: {want!r} does not appear in its text")
        return True
    return False


def effective_date(text, doc_type):
    """An executive order prints one `Effective date:` in its administrative history, which the shared reader takes.
    A regulation file here is a whole subtitle: each chapter prints its own original effective date (and the
    amendments of its sections), so no one date is the document's and none is given."""
    return None if doc_type == "rule" else UNHANDLED


def notes(src, fmt, text):
    if src["jurisdiction"] != "maryland" or fmt != "html":
        return None
    if src.get("sections"):
        view = ("'in effect as of October 1st of this year' view" if "enactments=true" in src.get("url", "")
                else "site's default view")
        return ("Text taken from the General Assembly's statute pages (mgaleg.maryland.gov, Laws, Statutes, "
                + view + "): the site serves one section per page, so each "
                "listed section's text was taken from its page and the sections are joined in order, a blank line "
                "before each. The page's Previous and Next buttons are not read; the source's indentation is kept "
                "as two spaces per level. The article line is printed once. When a page prints two versions of a section "
                "(one marked IN EFFECT and one that takes effect later), only the version in effect is read; the "
                "snapshot keeps both.")
    if src["doc_type"] in ("rule", "executive_order"):
        return ("Text taken from the Division of State Documents' HTML publication of the Code of Maryland "
                "Regulations (the maryland-dsd/law-html repository, the bulk download the Library of Maryland "
                "Regulations site asks for in place of scraping): the document's article only, one line per "
                "paragraph, numbering as printed, two spaces of indentation per level, with the administrative "
                "history, authority and cross references the file prints. Links are written as their text; the "
                "page navigation, license notice and footer are not read.")
    return ("Text taken from the page's main content (title and rich-text field) as DoIT's SharePoint site serves "
            "it, one line per paragraph, heading, list item and table row (a table row's cells are joined by "
            "' | '; list items carry a bullet or their number). Links are written as their text, pictures and "
            "page navigation are not read, and an e-mail address the site obscures prints as '[email protected]'.")
