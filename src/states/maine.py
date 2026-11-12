"""Maine: the maine.gov web pages that are themselves instruments (the Governor's order page, MaineIT's Prohibited
Technologies and Digital Signatures pages, the Bureau of Human Resources' policy page), and the identity of the
statute chapters, rules and executive orders. Hooks are described in src/states/__init__.py.

The Revisor of Statutes serves each chapter of the Maine Revised Statutes as a Word file (`title5ch164.docx`), the
Secretary of State serves each rule chapter as a Word file, and MaineIT serves its policies as PDFs: all three are read
by the shared readers. A chapter file opens `CHAPTER 164`, then the chapter title, and ends with the Revisor's
copyright notice and the sentence "current through <date>"."""
from __future__ import annotations

import re
from html.parser import HTMLParser

from src.ingest_common import _decode, _squash
from src.states import UNHANDLED

_HEADING_LINES = 6      # letterhead lines plus a heading that wraps, in an order PDF
_SKIP = {"script", "style", "svg", "noscript", "nav", "form", "button", "iframe"}      # elements with an end tag; `img` has none and carries no text
_BLOCK = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "table", "section", "article", "blockquote", "br"}


class _Page(HTMLParser):
    """The text between a page's `h1` and its `footer`, one line per block, list items marked."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lines: list[str] = []
        self.buf: list[str] = []
        self.skip = 0
        self.on = False
        self.done = False
        self.lists: list[list] = []        # [kind, next number]
        self.indent = ""

    def _flush(self):
        raw = "".join(self.buf).replace("\xa0", " ").replace("\u202f", " ")
        self.buf = []
        text = " ".join(raw.split())
        if text:
            self.lines.append(self.indent + text)
        self.indent = ""

    def handle_starttag(self, tag, attrs):
        if self.done:
            return
        if tag == "footer":
            self._flush()
            self.done = True
            return
        if tag == "h1" and not self.on:
            self.on = True
        if not self.on:
            return
        if tag in _SKIP:
            self.skip += 1
            return
        if tag in ("ol", "ul"):
            self._flush()
            self.lists.append([tag, 1])
        elif tag == "li":
            self._flush()
            if self.lists:
                kind, n = self.lists[-1]
                indent = "  " * (len(self.lists) - 1)
                self.buf.append(f"{n}. " if kind == "ol" else "• ")
                self.indent = indent
                self.lists[-1][1] = n + 1
        elif tag == "td" or tag == "th":
            if self.buf and "".join(self.buf).strip():
                self.buf.append(" | ")
        elif tag in _BLOCK:
            self._flush()

    def handle_endtag(self, tag):
        if self.done or not self.on:
            return
        if tag in _SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if tag in ("ol", "ul"):
            self._flush()
            if self.lists:
                self.lists.pop()
        elif tag in _BLOCK or tag == "li":
            self._flush()

    def handle_data(self, data):
        if self.on and not self.done and not self.skip:
            self.buf.append(data)


def page_to_text(raw: bytes) -> str:
    """A maine.gov (Drupal) page that is itself the instrument. Everything from the page's `h1` to its `footer`,
    one line per paragraph, heading, list item and table row; links, images, menus and forms are not read."""
    page = _decode(raw)
    page = re.sub(r"<!--.*?-->", "", page, flags=re.S)
    parser = _Page()
    parser.feed(page)
    parser._flush()
    if not parser.lines:
        raise ValueError("Maine page has no h1 heading with text after it: the page layout changed")
    return "\n".join(parser.lines) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type in ("policy", "standard", "executive_order"):
        return page_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "maine":
        return False
    doc_type = src["doc_type"]
    if doc_type == "statute":
        ch = re.search(r"\bch\.\s*(\d+(?:-[A-Z])?)\b", src["citation"])
        first = text.strip().splitlines()[0].strip() if text.strip() else ""
        if not ch or first != f"CHAPTER {ch.group(1)}":
            raise ValueError(f"{src['id']}: file is not {src['citation']} (it opens {first[:60]!r})")
        return True
    if doc_type == "rule":
        m = re.match(r"(\d\d-\d{3}) C\.M\.R\. ch\. (\d+)$", src["citation"])
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        ok = bool(m) and len(lines) > 1 and lines[0].startswith(m.group(1) + " ") \
            and lines[1].startswith(f"Chapter {m.group(2)}:") and src["title"].upper() in lines[1].upper()
        if not ok:
            raise ValueError(f"{src['id']}: file is not the cited rule {src['citation']} ({src['title']!r})")
        return True
    if doc_type == "executive_order":
        want = src.get("identity_text")
        if not want:
            raise ValueError(f"{src['id']}: an executive order entry needs `identity_text`, the order's own heading")
        # The order's own heading, not a mention: a web page opens with it (first line); a PDF letterhead gives a few
        # lines (office, number, date) and then the heading, which may wrap over two lines.
        lines = [l for l in text.splitlines() if l.strip()]
        head = lines[:1] if src.get("format") == "html" else lines[:_HEADING_LINES]
        if _squash(want) not in _squash(" ".join(head)):
            raise ValueError(f"{src['id']}: document is not the cited order: {want!r} is not in its opening heading")
        return True
    if doc_type in ("policy", "standard") and what_is == "page":
        first = text.strip().splitlines()[0] if text.strip() else ""
        want = src.get("identity_text") or src["title"]
        if first != want:
            raise ValueError(f"{src['id']}: page is not {want!r} (it opens {first[:60]!r})")
        return True
    return False


def notes(src, fmt, text):
    if fmt != "html":
        return None
    return ("Text taken from the page on maine.gov (a Drupal site run by the issuing office): the page's heading, then "
            "everything up to the site footer, one line per paragraph, heading, list item and table row. The site "
            "header, menus, images (a signature or letterhead image is not text), social-media links and footer were "
            "removed, as were the targets of links. Items of a numbered list are numbered 1., 2., ... within their list "
            "(nested lists indented two spaces), as a browser numbers a plain ordered list; the page sets no other "
            "numbering style. Bullets are written as a bullet character. The page prints no revision history.")


_MONTH = r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\.?"
_PRINTED_DATE = (rf"(?:{_MONTH}\s+\d{{1,2}},?\s+\d{{4}}"          # May 29, 2026
                 rf"|\d{{1,2}},?\s+{_MONTH},?\s+\d{{4}}"          # 21 August 2026, 15, July 2025
                 rf"|\d{{1,2}}/\d{{1,2}}/\d{{4}}"                  # 10/17/2025
                 rf"|{_MONTH}\s+\d{{4}})")                        # JANUARY 2024
# The label as the file prints it: `Latest Revision Date:`, `Last Revision Date:`, `Latest Revision:`, `Latest Revision`,
# `Current Revision Date (Version 3.1):`, then the date; trailing prose ("- To update Document Information.") is dropped.
_REVISION = re.compile(rf"^\s*(?:\d+(?:\.\d+)*\.?\s+)?((?:Latest|Last|Current) Revision(?: Date)?(?: \([^)\n]*\))?)\s*:?\s*({_PRINTED_DATE})(?![\w/])", re.M | re.I)
_REVISED = re.compile(rf"^\s*(REVISED)\s+({_PRINTED_DATE})\s*$", re.M | re.I)
_CURRENT = re.compile(r"reflects changes made through the (.+?) of the (\d+\w+) Maine Legislature and is current through\s+(.+?)\s*\.\s+The text is subject", re.S)


def source_version(text, doc_type, fmt):
    """A MaineIT policy PDF prints its revision date in its document information (`Latest Revision Date:`, `Last Revision Date:`,
    `Latest Revision:`, `Current Revision Date (Version n):` or a line `REVISED <Month year>`; the label is kept as printed); a statute chapter's Word file prints the session it reflects and the date it is current through."""
    if doc_type == "statute":
        m = _CURRENT.search(" ".join(text.split()))
        if m:
            session = m.group(1)
            return f"Current through {m.group(3)} ({session} of the {m.group(2)} Maine Legislature)"
        return None
    if doc_type in ("policy", "standard") and fmt == "pdf":
        m = _REVISION.search(text)
        if m:
            return f"{m.group(1)}: {m.group(2)}"
        m = _REVISED.search(text)
        if m:
            return f"{m.group(1)} {m.group(2)}"
    return None


def extra_notes(src, fmt, text, eff, version):
    if src["id"] == "me-eo-25-fy-20-21":
        return (" The PDF is a scan (full-page images); the text here is the recognised-text layer the publisher embedded in "
                "it, taken as is: it was not corrected and was not checked by a person, so it carries recognition errors "
                "(for example 'Govermnent' for 'Government', 'Chieflnformation Officer' for 'Chief Information Officer', and "
                "a stray symbol line) that are not the Governor's words.")
    return ""


def effective_date(text, doc_type):
    return UNHANDLED
