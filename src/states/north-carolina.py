"""North Carolina: the General Assembly's article pages, the Office of Administrative Hearings' subchapter pages and
NCDIT's own web pages. Hooks are described in src/states/__init__.py.

Statutes are served one article per static page (`/EnactedLegislation/Statutes/HTML/ByArticle/Chapter_<c>/Article_<n>.html`,
the link the General Assembly's own section lists print): Word-exported HTML with the article number and title as
the first two paragraphs, then each section as a bold `§ n. Caption.` paragraph followed by its subsections. The
page prints no chapter line (only the `<title>` does), so the chapter is checked on the first section number.
Rules are served by OAH (`reports.oah.state.nc.us`, HTTP only) as one Windows-1252 Word-HTML file per subchapter.
NCDIT's pages are Drupal pages: the instrument is the `<article>` element. PDFs and Word files are shared."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line, _decode, paragraph_html_to_text

_SECTION = re.compile(r"^§ \S+\.\s")
_RULE = re.compile(r"^09 NCAC \d+\w+ \.\d+")


def _blocks(raw: bytes) -> list[str]:
    """The page's paragraphs and headings (the Part headings are <h6>, which the shared paragraph reader skips),
    each squeezed to one line; empty ones (spacing) dropped."""
    page = _decode(raw)
    body = page[page.lower().find("<body"):]
    return [l for l in (_clean_line(re.sub(r"<[^>]+>", "", m.group(2)))
                        for m in re.finditer(r"<(p|h[1-6])\b[^>]*>(.*?)</\1>", body, flags=re.S | re.I)) if l]


def statute_html_to_text(raw: bytes) -> str:
    """One article page to text: one line per source paragraph, then a blank line before each section and each
    part heading, nothing inside a section dropped (repealed-section lines and the session-law history stay)."""
    lines = _blocks(raw)
    if not lines or not re.match(r"^Article \w+\.$", lines[0]) or not any(_SECTION.match(l) for l in lines):
        raise ValueError("no statute text: the page has no article heading and sections (the layout changed, "
                         "or this is not an article page)")
    out: list[str] = []
    for i, line in enumerate(lines):
        if i > 1 and (_SECTION.match(line) or re.match(r"^Part \w+\. ", line)):
            out.append("")
        out.append(line)
    return "\n".join(out) + "\n"


def rule_html_to_text(raw: bytes) -> str:
    """One OAH subchapter page to text: the subchapter and section lines as printed, then each rule (its number and
    caption, text, history note), one line per source paragraph, with a blank line before each rule. Repealed and
    expired rules print their caption and history note and are kept as published."""
    lines = paragraph_html_to_text(raw).splitlines()
    if not lines or not lines[0].lower().startswith("subchapter ") or not any(_RULE.match(l) for l in lines):
        raise ValueError("no rule text: the page has no subchapter heading and rules (the layout changed, "
                         "or this is not a subchapter page)")
    out: list[str] = []
    for line in lines:
        if _RULE.match(line):
            out.append("")
        out.append(line)
    return "\n".join(out).lstrip("\n") + "\n"


def article_html_to_text(raw: bytes) -> str:
    """NCDIT's Drupal page: the `<article>` element (title, then the body), scripts and styles removed, one line
    per block element. The menus, the breadcrumb, the page's side navigation and the footer sit outside it."""
    page = _decode(raw)
    start = page.find("<article")
    end = page.find("</article>", start)
    if start < 0 or end < 0:
        raise ValueError("no article region: the page layout changed")
    region = re.sub(r"<(script|style)\b.*?</\1>|<!--.*?-->", "", page[start:end], flags=re.S | re.I)
    region = re.sub(r"<(/?)(p|div|li|ul|ol|h[1-6]|tr|table|header|section|article|br)\b[^>]*>", "\n", region, flags=re.I)
    lines = [l for l in (_clean_line(re.sub(r"<[^>]+>", "", x)) for x in region.split("\n")) if l]
    if len(lines) < 3:
        raise ValueError("no article region: the page has no body text")
    return "\n".join(lines) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt != "html":
        return None
    if doc_type == "statute":
        return statute_html_to_text(raw)
    if doc_type == "rule":
        return rule_html_to_text(raw)
    if doc_type == "policy" and host.endswith("it.nc.gov"):
        return article_html_to_text(raw)
    return None


_ARTICLE = re.compile(r"^G\.S\. (?P<ch>\w+), Article (?P<art>\w+)$")
_SUBCHAPTER = re.compile(r"Subchapter (?P<sub>\w+)$", re.I)


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "north-carolina":
        return False
    if src["doc_type"] == "statute":
        m = _ARTICLE.match(src["citation"])
        lines = text.splitlines()
        first = next((l for l in lines if _SECTION.match(l)), "")
        if not m or not lines or lines[0] != f"Article {m.group('art')}." \
                or not first.startswith(f"§ {m.group('ch')}-"):
            raise ValueError(f"{src['id']}: page is not {src['citation']} (article or chapter mismatch)")
        return True
    if src["doc_type"] == "rule":
        m = _SUBCHAPTER.search(src["citation"])
        if not m or not text.lower().startswith(f"subchapter {m.group('sub').lower()} "):
            raise ValueError(f"{src['id']}: page is not {src['citation']} (subchapter mismatch)")
        return True
    if src["doc_type"] == "executive_order":
        m = re.search(r"Executive Order No\. (\d+)$", src["citation"])
        if not m or not re.search(rf"executive\s+order\s+no\.?\s*{m.group(1)}(?!\d)", text, flags=re.I):
            raise ValueError(f"{src['id']}: PDF is not the cited instrument: '{src['citation']}' does not appear "
                             f"in its text")
        return True
    return False


def notes(src, fmt, text):
    if src["jurisdiction"] != "north-carolina":
        return None
    if src["doc_type"] == "statute":
        return ("Text taken from the General Assembly's article page: the article number and title, then each "
                "section's caption, subsections and session-law history, one line per paragraph. The page's head "
                "and style sheet removed. A blank line precedes each section and each part heading. Sections "
                "printed as repealed keep their line as published.")
    if src["doc_type"] == "rule":
        return ("Text taken from the Office of Administrative Hearings' page for the subchapter (Windows-1252 "
                "Word HTML): the subchapter and section lines as printed, then each rule's number and caption, "
                "text and history note, one line per paragraph, with a blank line before each rule. The page's "
                "style sheet removed. Repealed and expired rules print their caption and history note and are "
                "kept as published.")
    if src["doc_type"] == "policy":
        return ("Text taken from NCDIT's web page: the page title and the body of its article region, one line per "
                "paragraph, list item or heading. The site menus, breadcrumb, side navigation, scripts and footer "
                "removed; link addresses are not part of the text.")
    return None
