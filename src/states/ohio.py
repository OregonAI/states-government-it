"""Ohio: the Ohio Laws pages on codes.ohio.gov (the Legislative Service Commission's Revised Code and the
Joint Committee on Agency Rule Review's Administrative Code), the policy pages of the Department of
Administrative Services (das.ohio.gov) and the executive order pages of the Governor (governor.ohio.gov),
and the identity of those pages and of the IT standards (PDFs). Hooks are described in
src/states/__init__.py. Every other source Ohio holds is a PDF, which the shared reader handles."""
from __future__ import annotations

import re
from html.parser import HTMLParser

from src.ingest_common import _clean_line, _decode
from src.states import UNHANDLED

_VOID = {"br", "img", "input", "meta", "link", "hr", "area", "base", "col", "source", "wbr"}
_INLINE = {"a", "span", "strong", "b", "em", "i", "u", "sup", "sub", "small", "abbr", "font"}
# Page furniture inside the laws region: the breadcrumb trail, the previous/next pager, the expand/close
# buttons, every `no-print` element (the PDF link, the "View ... Version" links), the "Last updated" note
# (the day the site's editors touched the page, not part of the law), spacers and the table's header row.
_DROP_CLASSES = ("breadcrumbs", "profile-navigator", "global-content-controls", "no-print", "laws-notice",
                 "spacer-", "section-banner")
_DROP_TAGS = {"script", "style", "svg", "noscript", "th", "button", "form", "nav", "header", "footer"}


class _Laws(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lines: list[str] = []
        self.cur: list[str] = []
        self.stack: list[tuple[str, bool]] = []     # (tag, drops its content)
        self.skip = 0
        self.seen_h1 = False

    def _flush(self, blank_before=False):
        line = _clean_line("".join(self.cur))
        self.cur = []
        if line:
            if blank_before and self.lines and self.lines[-1] != "":
                self.lines.append("")
            self.lines.append(line)

    def handle_starttag(self, tag, attrs):
        cls = dict(attrs).get("class") or ""
        if tag in _VOID:
            if tag == "br" and not self.skip and self.seen_h1:
                self._flush()
            return
        drop = tag in _DROP_TAGS or any(c in cls for c in _DROP_CLASSES)
        if tag == "h1":
            self.seen_h1 = True
        self.stack.append((tag, drop))
        if drop:
            self.skip += 1
            return
        if not self.seen_h1 or self.skip:
            return
        if "content-head-text" in cls or tag == "h2":
            self._flush()
            self.pending_blank = True
        if tag not in _INLINE:
            self._flush(blank_before=getattr(self, "pending_blank", False))
            self.pending_blank = False

    def handle_endtag(self, tag):
        if tag in _VOID:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                dropped = self.stack[i:]
                del self.stack[i:]
                for _, d in dropped:
                    if d:
                        self.skip -= 1
                break
        else:
            return
        if self.seen_h1 and not self.skip and tag not in _INLINE:
            self._flush(blank_before=getattr(self, "pending_blank", False))
            self.pending_blank = False

    def handle_data(self, data):
        if self.seen_h1 and not self.skip:
            self.cur.append(data)


def laws_html_to_text(raw: bytes) -> str:
    """A codes.ohio.gov page: a Revised Code section, a Revised Code chapter (every section of it, expanded),
    an Administrative Code chapter (every rule of it). Only what follows the page's `h1` inside `<main>` is read.
    Output: the heading (`Section 125.18 | Title`, `Chapter 1347 | Title`), then for each section or rule its
    heading (a blank line before it), the `Effective:` and `Latest Legislation:` / `Promulgated Under:` lines,
    one line per paragraph, and the history ("Available Versions of this Section", or a rule's "Supplemental
    Information"). The menus, search form, breadcrumb, pager, PDF and "View ... Version" links and the
    "Last updated" note are not read."""
    page = _decode(raw)
    start = page.find("<main")
    end = page.find("</main>")
    if start < 0 or end < 0 or "<h1" not in page[start:end] or "laws-body" not in page[start:end]:
        raise ValueError("codes.ohio.gov page has no laws region: the page layout changed")
    page = re.sub(r"<!--.*?-->", "", page[start:end], flags=re.S)
    p = _Laws()
    p.feed(page)
    p._flush()
    lines = _join_labels(p.lines)
    if not lines:
        raise ValueError("codes.ohio.gov page has no text in its laws region")
    return "\n".join(lines) + "\n"


_LABELS = {"Effective:", "Latest Legislation:", "Promulgated Under:"}


def _join_labels(lines: list[str]) -> list[str]:
    """The page prints a label and its value in two boxes; they are one line here."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i] in _LABELS and i + 1 < len(lines):
            out.append(f"{lines[i]} {lines[i + 1]}")
            i += 2
        else:
            out.append(lines[i])
            i += 1
    return out


# ---- das.ohio.gov policy pages and governor.ohio.gov executive order pages ----------------
# Both sites run the same portal: the page's `h1` (class odx-content__title) opens the content and an HTML
# comment (`./odx-content__body`) closes it; the menus, the CMS comments, the download box and the footer
# lie outside that region. The page's lists are numbered by style sheet (upper-roman, upper-alpha, `type`),
# so the numbers are written out here: the policies refer to their own sections ("refer to section F.").
_PORTAL_END = "<!-- ./odx-content__body -->"
_PORTAL_DROP = {"script", "style", "svg", "noscript", "button", "form"}


def _roman(n: int) -> str:
    out = ""
    for v, r in ((10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")):
        while n >= v:
            out, n = out + r, n - v
    return out


def _marker(style: str, n: int) -> str:
    if style == "A":
        return f"{chr(64 + n)}."
    if style == "a":
        return f"{chr(96 + n)}."
    if style == "I":
        return f"{_roman(n).upper()}."
    if style == "i":
        return f"{_roman(n)}."
    if style == "-":
        return "-"
    return f"{n}."


class _Portal(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lines: list[str] = []
        self.cur: list[str] = []
        self.skip = 0
        self.lists: list[list] = []          # [style, count]
        self.marker = ""                     # list marker waiting for the item's first text
        self.table_row: list[str] | None = None
        self.cell: list[str] | None = None
        self.blank_next = False

    def _flush(self):
        line = _clean_line("".join(self.cur))
        self.cur = []
        if not line:
            return
        if self.marker:
            line, self.marker = f"{self.marker} {line}", ""
        if self.blank_next and self.lines and self.lines[-1] != "":
            self.lines.append("")
        self.blank_next = False
        self.lines.append(line)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in _VOID and tag != "br":
            return
        if tag in _PORTAL_DROP:
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "br":
            if self.cell is not None:
                self.cell.append(" ")
            else:
                self._flush()
            return
        if self.cell is not None:
            if tag in ("td", "th"):
                self.cell = []
            return
        if tag in ("ol", "ul"):
            self._flush()
            cls, typ = a.get("class") or "", a.get("type") or ""
            style = ("-" if tag == "ul" else "I" if "romanH2" in cls else "A" if "alphaCapH3" in cls
                     else typ if typ in ("a", "A", "i", "I") else "1")
            self.lists.append([style, 0])
        elif tag == "li" and self.lists:
            self._flush()
            self.lists[-1][1] += 1
            self.marker = _marker(*self.lists[-1])
        elif tag == "tr":
            self._flush()
            self.table_row = []
        elif tag in ("td", "th") and self.table_row is not None:
            self.cell = []
        elif tag in ("h2", "h3", "h4"):
            self._flush()
            self.blank_next = True
        elif tag not in _INLINE:
            self._flush()

    def handle_endtag(self, tag):
        if tag in _VOID:
            return
        if tag in _PORTAL_DROP and self.skip:
            self.skip -= 1
            return
        if self.skip:
            return
        if tag in ("td", "th") and self.cell is not None:
            self.table_row.append(_clean_line("".join(self.cell)))
            self.cell = None
        elif tag == "tr" and self.table_row is not None and self.cell is None:
            cells = [c for c in self.table_row if c]
            if cells:
                self.cur = [" | ".join(cells)]
                self._flush()
            self.table_row = None
        elif tag in ("ol", "ul"):
            self._flush()
            if self.lists:
                self.lists.pop()
        elif tag not in _INLINE and self.cell is None and tag not in ("td", "th", "tr"):
            self._flush()

    def handle_data(self, data):
        if self.skip:
            return
        if self.cell is not None:
            self.cell.append(data)
        else:
            self.cur.append(data)


def portal_html_to_text(raw: bytes) -> str:
    """A das.ohio.gov policy page or a governor.ohio.gov executive order page. Output: the page heading
    (`IT-17 Use of Artificial Intelligence in State of Ohio Solutions`, `Executive Order 2022-07D`), then the
    content, one line per paragraph, list item (with its number as the page displays it) or table row (cells
    joined by ` | `, the header row included). The menus, scripts, style sheets, CMS comments, the download box
    (a PDF attachment of the order) and the footer are not read."""
    page = _decode(raw)
    start = page.find('<h1 class="odx-content__title">')
    end = page.find(_PORTAL_END)
    if start < 0 or end < start:
        raise ValueError("das.ohio.gov / governor.ohio.gov page has no content region: the page layout changed")
    p = _Portal()
    p.feed(re.sub(r"<!--.*?-->", "", page[start:end], flags=re.S))
    p._flush()
    if len(p.lines) < 3:
        raise ValueError("das.ohio.gov / governor.ohio.gov page has no text in its content region")
    return "\n".join(p.lines) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type in ("statute", "rule"):
        return laws_html_to_text(raw)
    if fmt == "html" and doc_type in ("policy", "standard", "executive_order"):
        return portal_html_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "ohio":
        return False
    first = text.strip().splitlines()[0] if text.strip() else ""
    cite = src["citation"]
    if src["doc_type"] in ("statute", "rule"):
        ch = re.search(r"\bch\.\s*([\w:.\-]+)", cite)
        sec = re.search(r"\b(?:R\.C\.|OAC)\s*([\d][\w:.\-]*)", cite)
        want = f"Chapter {ch.group(1)} | " if ch else f"Section {sec.group(1)} | " if sec else None
        if not want or not first.startswith(want):
            raise ValueError(f"{src['id']}: page is not {cite} (it opens {first[:60]!r})")
        return True
    if what_is == "page" and src["doc_type"] in ("policy", "standard"):
        # The page's own heading line: `IT-17 Use of Artificial Intelligence in State of Ohio Solutions`.
        if not re.match(rf"{re.escape(cite)}(\s|$)", first):
            raise ValueError(f"{src['id']}: page is not {cite} (it opens {first[:60]!r})")
        return False       # the shared check of the title follows
    if what_is == "page" and src["doc_type"] == "executive_order":
        # Only the heading line counts: an order's text may name another order.
        if first != cite:
            raise ValueError(f"{src['id']}: page is not {cite} (it opens {first[:60]!r})")
        return True
    if what_is == "PDF" and src["doc_type"] == "standard":
        if not re.search(rf"(?<![\w-]){re.escape(cite)}(?![\w-])", text):
            raise ValueError(f"{src['id']}: PDF is not {cite}: that number does not appear in its text")
        return False
    return False


def effective_date(text, doc_type):
    # A chapter page prints an `Effective:` line under every section or rule: none of them is the document's.
    if doc_type in ("statute", "rule", "executive_order"):
        return None
    return UNHANDLED


def notes(src, fmt, text):
    if fmt != "html":
        return None
    if src["doc_type"] in ("policy", "standard"):
        return ("Text taken from the policy page on das.ohio.gov (the Department of Administrative Services' web "
                "publication of the policy): the page heading, then the content below it, one line per paragraph, "
                "list item or table row. The page numbers its lists by style sheet; the list numbers (I., A., 1., a.) "
                "are written out as the page displays them, bullets as '-', and the cells of a table row are joined "
                "by ' | '. The portal's menus, scripts, style sheets, comments, download box and footer were removed.")
    if src["doc_type"] == "executive_order":
        return ("Text taken from the order's page on governor.ohio.gov (the Governor's web publication of the "
                "order): the page heading, then the order's text, one line per paragraph or list item, with list "
                "numbers written out as the page displays them. The portal's menus, scripts, comments, the download "
                "box for the signed PDF (a scanned copy that is not read) and the footer were removed. The order "
                "prints no effective-date label, so none is recorded.")
    return ("Text taken from the page on codes.ohio.gov (Ohio Laws): the heading, then for each section or rule its "
            "heading, the `Effective:` and `Latest Legislation:` (or `Promulgated Under:`) lines, the paragraphs "
            "and the version history or supplemental information, one line per paragraph. The menus, search form, "
            "breadcrumb, previous/next pager, the Download Authenticated PDF and View Version links and the "
            "site's 'Last updated' note were removed. The page prints an effective date for each section or rule, "
            "not for the document, so none is recorded for the document. Sections or rules marked repealed or "
            "expired ride along as the page prints them.")
