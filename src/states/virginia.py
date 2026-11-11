"""Virginia: the Code of Virginia pages (law.lis.virginia.gov), VITA's web-page policies
(vita.virginia.gov), and the identity of statutes and executive orders. Hooks are described in
src/states/__init__.py. Everything else Virginia holds is PDF, which the shared reader handles."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line, _decode
from src.states import UNHANDLED

_BLOCK = re.compile(r"<(?:/?)(?:div|p|h[1-6]|li|ul|ol|tr|table|section|article|button|br|b)\b[^>]*>|<br\s*/?>", re.I)


def _text_lines(fragment: str) -> list[str]:
    """HTML to lines: comments, scripts, styles and svg dropped, one line per block, tags removed."""
    fragment = re.sub(r"<!--.*?-->", "", fragment, flags=re.S)
    fragment = re.sub(r"<(script|style|svg|noscript)\b.*?</\1>", "", fragment, flags=re.S | re.I)
    fragment = _BLOCK.sub("\n", fragment)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    return [c for c in (_clean_line(l) for l in fragment.split("\n")) if c]


def code_html_to_text(raw: bytes) -> str:
    """A Code of Virginia page, a whole chapter (`/vacodefull/title/chapter/`) or one section. Only the
    `va_code` region is the law: the menus, the report form, the print header with its date and the
    site's note under a section are not. Output: the chapter heading (a section page: the section
    heading), then each section's heading with a blank line before it (and before an article
    heading), one line per paragraph, the history line. Nothing inside a section is dropped."""
    page = _decode(raw)
    start = page.find("id='va_code'")
    if start < 0:
        start = page.find('id="va_code"')
    end = page.find("</article>", start)
    if start < 0 or end < 0:
        raise ValueError("Code of Virginia page has no va_code region: the page layout changed")
    region = page[page.index(">", start) + 1:end]
    region = re.sub(r"<input\b[^>]*>", "", region)
    region = re.sub(r"<(h3|b)\b", lambda m: "\n\x00" + m.group(0), region)           # a blank line before an article or section heading
    out: list[str] = []
    for chunk in region.split("\n"):
        marked = chunk.startswith("\x00")
        lines = _text_lines(chunk.replace("\x00", ""))
        if marked and out and lines:
            out.append("")
        out.extend(lines)
    if not out:
        raise ValueError("Code of Virginia page has no text in its va_code region")
    return "\n".join(out) + "\n"


def vita_html_to_text(raw: bytes) -> str:
    """A VITA web page that is itself the instrument (the Cloud Third Party Use Policy, VITA Rules).
    The page title (its `h1`) then everything in `<main>`, one line per block, hidden accordion
    panels included. The site header, navigation, breadcrumb and footer are not read."""
    page = _decode(raw)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", page, flags=re.S)
    m_start = re.search(r"<main\b[^>]*>", page)
    m_end = page.rfind("</main>")
    if not h1 or not m_start or m_end < 0:
        raise ValueError("VITA page has no h1 or main region: the page layout changed")
    out = _text_lines(h1.group(1)) + _text_lines(page[m_start.end():m_end])
    return "\n".join(out) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt != "html":
        return None
    if doc_type == "statute":
        return code_html_to_text(raw)
    if doc_type in ("policy", "standard"):
        return vita_html_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "virginia":
        return False
    first = text.strip().splitlines()[0] if text.strip() else ""
    if src["doc_type"] == "statute":
        ch = re.search(r"\bch\.\s*([\d.]+\w*)", src["citation"])
        sec = re.search(r"§\s*([\d.:\-]+\w*)", src["citation"])
        want = f"Chapter {ch.group(1)}." if ch else f"§ {sec.group(1)}." if sec else None
        if not want or not first.startswith(want):
            raise ValueError(f"{src['id']}: page is not {src['citation']} (it opens {first[:60]!r})")
        return True
    if src["doc_type"] == "executive_order":
        want = src.get("identity_text")
        if not want or " ".join(want.split()).casefold() not in " ".join(text.split()).casefold():
            raise ValueError(f"{src['id']}: PDF is not the cited instrument: {want!r} does not appear in its text")
        return True
    if src["doc_type"] in ("policy", "standard") and what_is == "page":
        if first != src["title"]:
            raise ValueError(f"{src['id']}: page is not {src['title']!r} (it opens {first[:60]!r})")
        return True
    return False


def notes(src, fmt, text):
    if fmt != "html":
        return None
    if src["doc_type"] == "statute":
        return ("Text taken from the Code of Virginia page on law.lis.virginia.gov (the Division of Legislative "
                "Automated Systems' Virginia Law portal): the chapter or section heading, then each section's "
                "heading, paragraphs and history line, one line per paragraph. Menus, the report form, the "
                "print header (which carries the day the page was fetched) and the site's note on the history "
                "line were removed. The page prints no effective date for the chapter or section.")
    if src["doc_type"] in ("policy", "standard"):
        return ("Text taken from the agency's web page (vita.virginia.gov): the page title, then the content of "
                "its main region, one line per paragraph, heading, list item and accordion panel. The site "
                "header, navigation, breadcrumb and footer were removed, as were the targets of links. "
                "The page prints no effective date.")
    return None


_PLACEHOLDER_DATE = re.compile(r"Effective Date[^\n]*\n[^\n]{0,60}\b[A-Z][a-z]+ x,", re.M)


def effective_date(text, doc_type):
    """ITRM documents print an `Effective Date` row in their publication-designation table and the shared
    label reader takes it. Two shapes are not one date and give none: a placeholder date in the row
    ('January x, 2023' beside the real date, GOV 101-04), and a list of dated milestones headed
    'Effective Dates:' (the Legacy IT Solutions report)."""
    if doc_type == "statute" or re.search(r"^\s*Effective Dates:", text, flags=re.M) or _PLACEHOLDER_DATE.search(text):
        return None
    return UNHANDLED
