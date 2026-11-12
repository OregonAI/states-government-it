"""Louisiana: the Legislature's one-section law pages, the Office of Technology Services' own policy pages and the
Division of Administration's policy pages. Hooks are described in src/states/__init__.py.

Statutes are served one section per page (`legis.la.gov/legis/Law.aspx?d=<id>`, the link the Legislature's own
title tables of contents print): the page's label ("RS 39:15.3") and then the section as Word-style paragraphs
inside one span, with the site's menus, previous/next buttons and footer around it.
OTS (`ots.la.gov`) serves each policy as a web page whose title, summary line and body carry `data-prop`
attributes; the DOA's own site (`doa.la.gov`) is an Umbraco site whose policy body is its `doa-RTE` blocks.
PDFs and Word files are shared."""
from __future__ import annotations

import re
from html.parser import HTMLParser

from src.ingest_common import _clean_line, _decode, _squash

_BLOCK = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "caption", "div", "br"}
_VOID = {"br", "img", "hr", "input", "meta", "link"}


class _Capture(HTMLParser):
    """Collects the text of the regions `starts(tag, attrs)` opens, one line per block (paragraph, heading, list
    item, table row), until that element closes. Scripts and styles never count."""

    def __init__(self, starts, regions=None):
        super().__init__(convert_charrefs=True)
        self.starts, self.lines, self.buf = starts, [], []
        self.cap_tag, self.depth = None, 0
        self.lists: list[list] = []           # [kind, counter]
        self.cell, self.row = False, None
        self.skip = 0
        self.pending_marker = ""

    def flush(self):
        line = _clean_line("".join(self.buf))
        self.buf = []
        if line:
            self.lines.append(self.pending_marker_for_line(line))

    def pending_marker_for_line(self, line):
        marker, self.pending_marker = self.pending_marker, ""
        return marker + line if marker else line

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.cap_tag is None:
            if self.starts(tag, a):
                self.cap_tag, self.depth = tag, 1
                self.flush()
            return
        if tag in _VOID:
            if tag == "br" and not self.cell:
                self.buf.append(" ")
            return
        if tag == self.cap_tag:
            self.depth += 1
        if tag in ("script", "style"):
            self.skip += 1
        elif tag in ("ul", "ol"):
            self.flush()
            n = int(a["start"]) - 1 if a.get("start", "").isdigit() else 0
            self.lists.append([tag, n])
        elif tag == "li":
            self.flush()
            kind = self.lists[-1] if self.lists else ["ul", 0]
            kind[1] += 1
            indent = "  " * max(len(self.lists) - 1, 0)
            self.pending_marker = indent + (f"{kind[1]}. " if kind[0] == "ol" else "- ")
        elif tag == "tr":
            self.flush()
            self.row = []
        elif tag in ("td", "th"):
            self.cell = True
            self.buf = []
        elif tag in _BLOCK and not self.cell:
            self.flush()

    def handle_endtag(self, tag):
        if self.cap_tag is None:
            return
        if tag in ("script", "style"):
            self.skip = max(self.skip - 1, 0)
        elif tag in ("td", "th") and self.row is not None:
            self.row.append(_clean_line("".join(self.buf)))
            self.buf, self.cell = [], False
        elif tag == "tr" and self.row is not None:
            if any(self.row):
                self.lines.append(" | ".join(self.row))
            self.row = None
        elif tag in ("ul", "ol"):
            self.flush()
            if self.lists:
                self.lists.pop()
        elif tag in _BLOCK and not self.cell:
            self.flush()
        if tag == self.cap_tag:
            self.depth -= 1
            if self.depth == 0:
                self.flush()
                self.cap_tag = None

    def handle_data(self, data):
        if self.cap_tag is not None and not self.skip:
            self.buf.append(data)


def _capture(raw: bytes, starts) -> list[str]:
    p = _Capture(starts)
    p.feed(_decode(raw))
    p.close()
    p.flush()
    return p.lines


# ---- the Legislature's law pages ------------------------------------------------------------

_LABEL = "ctl00_PageBody_LabelName"
_DOC = "ctl00_PageBody_LabelDocument"
_SECTION = re.compile(r"^§\S+\.\s")


def law_html_to_text(raw: bytes) -> str:
    """One section page to text: the page's label, then one line per source paragraph. Nothing inside the section is
    dropped (a repealed section prints its one line, the session-law history stays)."""
    lines = _capture(raw, lambda tag, a: a.get("id") in (_LABEL, _DOC))
    if not lines or not re.match(r"^RS \S+$", lines[0]) or not any(_SECTION.match(l) for l in lines[1:6]):
        raise ValueError("no statute text: the page has no section label and section line (the layout "
                         "changed, an error page was served, or this is not a law page)")
    return "\n".join(lines) + "\n"


# ---- OTS and DOA policy pages -------------------------------------------------------------------

def ots_page_to_text(raw: bytes) -> str:
    """An OTS policy page: its title, its summary line and its body (the `data-prop` regions), one line per block;
    the menus, the banner, the breadcrumb and the footer sit outside them."""
    lines = _capture(raw, lambda tag, a: a.get("data-prop") in ("title", "excerpt", "@content"))
    if len(lines) < 3:
        raise ValueError("no policy text: the page has no title, summary and body (the layout changed)")
    return "\n".join(lines) + "\n"


def doa_page_to_text(raw: bytes) -> str:
    """A DOA policy page: the `doa-RTE` blocks of the page's main region (title, number, dates, body, the note on
    the signed original). The staff directory menu, the contact box and the footer sit outside them."""
    page = _decode(raw)
    main = page[page.find("<main"):page.find("</main>")]
    lines = _capture(main.encode("utf-8"), lambda tag, a: "doa-RTE" in a.get("class", "").split())
    if len(lines) < 3:
        raise ValueError("no policy text: the page has no policy body (the layout changed)")
    return "\n".join(lines) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt != "html":
        return None
    if doc_type == "statute" and host.endswith("legis.la.gov"):
        return law_html_to_text(raw)
    if doc_type == "policy" and host.endswith("ots.la.gov"):
        return ots_page_to_text(raw)
    if doc_type == "policy" and host.endswith("doa.la.gov"):
        return doa_page_to_text(raw)
    return None


_CITED_SECTION = re.compile(r"^R\.S\. (?P<title>\d+):(?P<sec>\S+)$")
_DOA_NUMBER = re.compile(r"^DOA Policy No\. (?P<n>\d+)$")
_DOA_HEADING = re.compile(r"^Division of Administration (?:DOA )?Policy No\. (?P<n>\d+)$")
_EO_HEADING = re.compile(r"EXECUTIVE\s+ORDER\s+NUMBER\s+(?:JML\s+)?(?P<n>\d{2}-\d{3})\s*$", re.I)


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "louisiana":
        return False
    if src["doc_type"] == "statute":
        m = _CITED_SECTION.match(src["citation"])
        lines = text.splitlines()
        want = f"RS {m.group('title')}:{m.group('sec')}" if m else None
        first = next((l for l in lines if _SECTION.match(l)), "")
        if not m or not lines or lines[0] != want or not first.startswith(f"§{m.group('sec')}. "):
            raise ValueError(f"{src['id']}: page is not {src['citation']} (section mismatch)")
        return True
    if src["doc_type"] == "policy" and src.get("url", "").startswith(("https://doa.la.gov/doa/hr/", "https://www.doa.la.gov/doa/hr/")):
        m = _DOA_NUMBER.match(src["citation"])
        lines = text.splitlines()
        printed = next((h.group("n") for h in map(_DOA_HEADING.match, lines) if h), None)
        subject = next((l for l in lines if l.startswith("SUBJECT:")), "")
        if not m or printed != m.group("n") or _squash(src["title"]) not in _squash(subject):
            raise ValueError(f"{src['id']}: page is not {src['citation']} (policy number or subject mismatch)")
        return True
    if src["doc_type"] == "executive_order":
        m = re.search(r"(\d{2}-\d{3})$", src["citation"])
        heading = next((_EO_HEADING.search(l) for l in text.splitlines() if _EO_HEADING.search(l)), None)
        if not m or not heading or heading.group("n") != m.group(1):
            raise ValueError(f"{src['id']}: PDF is not the cited instrument: no heading line "
                             f"'EXECUTIVE ORDER NUMBER {src['citation'].split()[-1]}'")
        return True
    return False


def notes(src, fmt, text):
    if src["jurisdiction"] != "louisiana":
        return None
    if src["doc_type"] == "statute":
        return ("Text taken from the Legislature's page for the one section: the page's label, then the section's "
                "caption, subsections and session-law history, one line per paragraph. The site's menus, "
                "previous and next buttons, scripts and footer removed. A repealed section keeps its one line as "
                "published.")
    if src["doc_type"] == "policy":
        if src.get("url", "").startswith("https://ots.la.gov/"):
            return ("Text taken from the Office of Technology Services' web page: the page title, its summary line "
                    "and the body, one line per paragraph, heading, list item (marked '- ' or numbered, indented "
                    "by depth) or table row (cells separated by ' | '). The site menus, banner, breadcrumb, "
                    "footer and scripts removed; link addresses are not part of the text. Words are joined exactly as the "
                    "page's HTML joins them (a link followed by a word with no space between them prints as one "
                    "word), and an e-mail address the page hides behind Cloudflare prints as '[email protected]' in "
                    "the page itself.")
        return ("Text taken from the Division of Administration's web page: the policy body as the page prints it "
                "(title, policy number, dates, sections), one line per paragraph or list item. The site menus, "
                "the contact box, the footer and scripts removed; link addresses are not part of the text.")
    return None
