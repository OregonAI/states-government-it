"""Alaska: the Legislature's print view of the Alaska Statutes and Administrative Code, and the Governor's order pages.
Hooks are described in src/states/__init__.py.

Statutes and rules: `statutes.asp?media=print&secStart=<n>&secEnd=<n>` and `aac.asp?media=print&...` are the print
links the Legislature's own pages offer for any run of sections; the seed list cites one run per document. The page
is bare (no menus): a `<div class="statute">` holding each section as an anchor `<a name="44.21.150">`, the heading,
and the text with `<BR>` between lines, in Windows-1252 bytes. Orders: gov.alaska.gov WordPress pages; the order is
the `post_content` module (title in `<h1 class="entry-title">`), the rest of the page is menus, a sidebar of
governors and a footer. Nothing here reads Alaska's PDF sources (shared reader)."""
from __future__ import annotations

import html as html_mod
import re

_SECTION = re.compile(r"\d+\.\d+\.\d+")
_AAC_NUMBER = re.compile(r"\d+\s+AAC\s+\d+\.\d+")


def _decode(raw: bytes) -> str:
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252")


def _lines(fragment: str) -> list[str]:
    """Markup to lines: `<br>` and block ends break a line, other tags vanish, entities and spaces are normalised."""
    fragment = re.sub(r"<br\s*/?>|</p>|</div>|</h\d>|</tr>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"<(?:p|h\d|div|tr)\b[^>]*>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    return [" ".join(html_mod.unescape(l).replace("\xa0", " ").split()) for l in fragment.split("\n")]


def _join(lines: list[str]) -> str:
    out: list[str] = []
    for l in lines:
        if l:
            out.append(l)
        elif out and out[-1] != "":
            out.append("")
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def print_view_to_text(raw: bytes, what: str) -> str:
    """A print-view page of a run of sections to text: a blank line before each section, then its heading line and one
    line per subsection, paragraph and subparagraph."""
    page = _decode(raw)
    start = page.find('<div class="statute">')
    if start == -1 or '<a name="' not in page[start:]:
        raise ValueError(f"no text of record: the page has no statute block with sections (the layout changed, "
                         f"or this is not a print view of {what})")
    body = page[start:]
    body = re.sub(r'<a name="[^"]*">', lambda m: "<br><br>" + m.group(0), body)
    lines = _lines(body)
    while lines and (not lines[-1] or re.match(r"Article \d+\. ", lines[-1])):
        lines.pop()          # the heading of the next Article, which the page prints after the last section
    return _join(lines)


def order_page_to_text(raw: bytes) -> str:
    """An order page to text: the order's own heading, then one line per paragraph, heading and list item (numbered
    as the page numbers an ordered list, a bullet for an unordered one). Menus, sidebar and footer are not read."""
    page = _decode(raw)
    title = re.search(r'<h1 class="entry-title">(.*?)</h1>', page, flags=re.S)
    start = page.find('class="et_pb_module et_pb_post_content')
    if not title or start == -1:
        raise ValueError("no text of record: the page has no order title and post content (the layout changed, "
                         "or this is not an administrative order page)")
    start = page.find(">", start) + 1
    end = page.find('<div class="et_pb_column', start)
    body = page[start:end if end != -1 else len(page)]
    counters: list[int | None] = []
    parts = re.split(r"(</?(?:ol|ul|li)\b[^>]*>)", body)
    out = []
    for part in parts:
        m = re.match(r"<(/?)(ol|ul|li)\b", part)
        if not m:
            out.append(part)
        elif m.group(2) in ("ol", "ul"):
            if m.group(1):
                if counters:
                    counters.pop()
            else:
                counters.append(0 if m.group(2) == "ol" else None)
            out.append("<br>")
        elif not m.group(1):
            if counters and counters[-1] is not None:
                counters[-1] += 1
                out.append(f"<br>{counters[-1]}. ")
            else:
                out.append("<br>• ")
        else:
            out.append("<br>")
    lines = [" ".join(html_mod.unescape(re.sub(r"<[^>]+>", "", title.group(1))).split()), ""] + _lines("".join(out))
    return _join(lines)


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt != "html":
        return None
    if doc_type == "statute":
        return print_view_to_text(raw, "the Alaska Statutes")
    if doc_type == "rule":
        return print_view_to_text(raw, "the Alaska Administrative Code")
    if doc_type == "executive_order":
        return order_page_to_text(raw)
    return None


def _headings(text: str) -> set[str]:
    heads = set()
    for line in text.splitlines():
        m = re.match(r"Sec\. (\d+\.\d+\.\d+)\.", line) or re.match(r"(\d+ AAC \d+\.\d+)\.\s", line)
        if m:
            heads.add(m.group(1))
    return heads


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "alaska":
        return False
    kind = src["doc_type"]
    if kind == "executive_order":
        want = src["citation"]
        first = text.split("\n", 1)[0]
        if not re.fullmatch(r"Administrative Order No\. \d+", want) or first != want:
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: its heading is {first!r}, "
                             f"the seed entry cites {want!r}")
        return True
    if kind not in ("statute", "rule"):
        return False
    cited = _SECTION.findall(src["citation"]) if kind == "statute" else [
        re.sub(r"\s+", " ", m) for m in _AAC_NUMBER.findall(src["citation"])]
    heads = _headings(text)
    if not cited or any(c not in heads for c in (cited[0], cited[-1])):
        raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {src['citation']!r} "
                         f"does not open and close with section headings in its text")
    return True


def notes(src, fmt, text):
    if src["jurisdiction"] != "alaska" or fmt != "html":
        return None
    if src["doc_type"] in ("statute", "rule"):
        code = "Alaska Statutes" if src["doc_type"] == "statute" else "Alaska Administrative Code"
        return (f"Text taken from the Alaska Legislature's print view of the {code} (the page's print link, for the run of "
                "sections cited): a blank line before each section, then its heading line and one line per subsection, "
                "paragraph and subparagraph, as the page prints them. The page prints no menus or footer, no edition "
                "line and no history lines; sections the page marks repealed or renumbered are printed as marked. The "
                "page's own links are plain text here. A heading of the next Article that the page prints after the last "
                "section of the run is dropped.")
    if src["doc_type"] == "executive_order":
        return ("Text taken from the order's page on the Governor's site (gov.alaska.gov): the order's own heading, then one "
                "line per paragraph, heading and list item, a numbered list numbered as the page numbers it and an "
                "unordered list with a bullet. The page's menus, the list of orders by Governor and the footer are removed.")
    return None
