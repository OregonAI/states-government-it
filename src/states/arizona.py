"""Arizona: the Legislature's per-section statute pages. Hooks are described in src/states/__init__.py.

The Arizona Revised Statutes are served one section per static page (`www.azleg.gov/ars/<title>/<nnnnn>.htm`): a
`<TITLE>` element, HTML comment lines (`Creation Date`, `Author`, `Typist`), then one `<p>` per paragraph. The first
paragraph is the number and caption, set in two font tags; an empty `&nbsp;` paragraph ends the body. The
Governor's executive orders are read from the Governor's order pages (azgovernor.gov): a heading, the title, the
issue date and the order's body in separate page panes. The agencies' policy libraries and the Administrative Code
answer the Fetcher with a Cloudflare challenge (see the seed list)."""
from __future__ import annotations

import re

from src.ingest_common import BlockParser, _decode, _LONG_DATE, _MONTHS, paragraph_html_to_text
from src.states import UNHANDLED, _squash

_FIRST = re.compile(r"^(?P<num>\d+-\d+(?:\.\d+)?)\.\s+(?P<caption>.+)$")


def section_html_to_text(raw: bytes) -> str:
    """One section page to text: one line per source paragraph (the number and caption first), markup, the TITLE
    element and the comment lines left out, entities resolved, the empty paragraph dropped."""
    text = paragraph_html_to_text(raw)
    first = text.splitlines()[0] if text.strip() else ""
    if not _FIRST.match(first):
        raise ValueError("no statute text: the page does not open with a section number and caption (the layout "
                         "changed, or this is not a section page)")
    return text


class _OrderParser(BlockParser):
    """The order's lists as the page's own HTML has them, with one repair: the page ends the order with a separate
    top-level `<ol>` that carries no `start`, which a browser prints as "1." though it is section 9. A top-level
    ordered list with no `start` continues the count of the one before it."""

    def __init__(self):
        super().__init__()
        self.next_top: int | None = None

    def handle_starttag(self, tag, attrs):
        if tag == "ol" and not self.lists and self.next_top and not dict(attrs).get("start"):
            attrs = [*attrs, ("start", str(self.next_top))]
        super().handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag == "ol" and len(self.lists) == 1:
            self.next_top = self.lists[-1][1]
        super().handle_endtag(tag)


def _pane(page: str, pattern: str) -> str | None:
    m = re.search(pattern, page, re.S)
    return " ".join(re.sub(r"<[^>]+>", " ", m.group(1)).split()) if m else None


def order_html_to_text(raw: bytes) -> str:
    """One Governor's order page to text: the heading line ("Executive Order 2023-10"; the page prints the words
    twice in its category heading and the first is dropped), the title, the issue date, then the body, one line per
    paragraph and per list item, numbered as the page's lists number. The page's menus, footer, the download link
    and its scripts are not the order."""
    page = _decode(raw)
    heading = _pane(page, r'<h3 class="category">(.*?)</h3>')
    title = _pane(page, r"<h1>(.*?)</h1>")
    issued = _pane(page, r'<span\s+class="date-display-single">(.*?)</span>')
    body = re.search(r'field-name-body[^>]*><div class="field-items"><div class="field-item even">(.*?)</div></div></div>',
                     page, re.S)
    if not (heading and title and issued and body):
        raise ValueError("no order text: the page's heading, title, date or body pane is missing (the layout "
                         "changed, or this is not an executive order page)")
    heading = re.sub(r"^(?:Executive Order\s+)+(?=Executive Order)", "", heading)
    html = re.sub(r"<li[^>]*>\s*<p[^>]*>", "<li>", body.group(1))      # the marker and the text on one line
    html = re.sub(r"</p>\s*</li>", "</li>", html)
    parser = _OrderParser()
    parser.feed(html)
    parser._flush()
    return "\n".join([heading, title, issued, *parser.lines]) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute":
        return section_html_to_text(raw)
    if fmt == "html" and doc_type == "executive_order":
        return order_html_to_text(raw)
    return None


def check_identity(src, text, what_is):
    """The page's first line is the cited section: its number is the citation's and its caption is the seed title's
    (`<number> - <caption>`; the page's TITLE element is not used: it holds a control character for the hyphen in 18-422's "third-party")."""
    if src["jurisdiction"] != "arizona":
        return False
    if src["doc_type"] == "executive_order":
        number = re.search(r"\d{2,4}-\d{2}", src["citation"])
        head = [_squash(l) for l in text.splitlines()[:4]]
        # the order's own heading is a line of its own near the top: a mention of the number in a later order must not pass
        if not number or _squash(f"executive order {number.group(0)}") not in head or _squash(src["title"]) not in head:
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: the heading 'Executive Order "
                             f"{number and number.group(0)}' and the title {src['title']!r} are not lines of their "
                             f"own in the opening lines of its text")
        return True
    if src["doc_type"] != "statute":
        return False
    first = _FIRST.match(text.splitlines()[0]) if text.strip() else None
    number = src["citation"].removeprefix("A.R.S.").strip()
    ok = bool(first) and first.group("num") == number and _squash(src["title"]) == _squash(f"{number} - {first.group('caption')}")
    if not ok:
        raise ValueError(f"{src['id']}: page is not {src['citation']} (section number or caption mismatch)")
    return True


def effective_date(text, doc_type):
    """An order says it takes effect on signature; the page prints the order's date on its third line."""
    if doc_type != "executive_order":
        return UNHANDLED
    lines = text.splitlines()
    m = _LONG_DATE.fullmatch(lines[2]) if len(lines) > 2 else None
    if not m:
        return None
    return f"{m.group(3)}-{_MONTHS.split('|').index(m.group(1)) + 1:02d}-{int(m.group(2)):02d}"


def notes(src, fmt, text):
    if src["doc_type"] == "executive_order" and src["jurisdiction"] == "arizona":
        return ("Text taken from the Governor's order page: the page's heading line, the order's title, the date "
                "the page prints, then the body, one line per paragraph and list item. The page's menus, footer "
                "and download link removed. The page's lists carry their numbering in HTML list markup; list "
                "numbering follows the page's lists, except that the page's final list (section 9) carries no "
                "start and a browser would print it as 1., so it continues the count. The signature and seal "
                "block is not on the page. The page's date is the order's date: the order takes effect on signature.")
    if src["doc_type"] == "statute" and src["jurisdiction"] == "arizona":
        return ("Text taken from the Legislature's static section page: the section number and caption, then each "
                "paragraph of the section, one line per paragraph. The page's TITLE element, its HTML comment lines "
                "(Creation Date, Author, Typist) and its font and underline tags removed; the page's Creation Date "
                "is not the section's effective date, which the page does not print.")
    return None
