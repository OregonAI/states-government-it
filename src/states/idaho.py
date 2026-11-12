"""Idaho: Idaho Code section pages (legislature.idaho.gov). Hooks are described in src/states/__init__.py.
Everything else Idaho holds is PDF (ITA policies, standards and guidelines, ITS policies, scanned
executive orders), which the shared readers handle."""
from __future__ import annotations

import re

from src.ingest_common import _LONG_DATE, _MONTHS, _US_DATE, _clean_line, _decode, _squash

_START = '<div class="pgbrk"'
_END = '<a href="/statutesrules/howcurrentisthislaw"'


def code_html_to_text(raw: bytes) -> str:
    """One Idaho Code section page. Only the code region is the law: it runs from the title heading
    to the "How current is this law?" link. The site menu, search forms, the print and chapter-PDF
    buttons, the generator stub (`pecnv.out`) and the footer are not. Output: the title and chapter
    headings, then the section (number, caption and first paragraph on one line, as the page prints
    it), one line per paragraph, the History line."""
    page = _decode(raw)
    start = page.find(_START)
    end = page.find(_END, start)
    if start < 0 or end < 0:
        raise ValueError("Idaho Code page has no code region: the page layout changed")
    region = re.sub(r"<!--.*?-->", "", page[start:end], flags=re.S)
    region = re.sub(r"<(script|style)\b.*?</\1>", "", region, flags=re.S | re.I)
    region = re.sub(r"</?(?:div|p|h[1-6]|tr|li)\b[^>]*>|<br\s*/?>", "\n", region, flags=re.I)
    region = re.sub(r"<[^>]+>", "", region)
    lines = [c for c in (_clean_line(l) for l in region.split("\n")) if c]
    if not any(re.match(r"^\d+-\d+(?:-\d+)?[A-Za-z]?\.", l) for l in lines):
        raise ValueError("Idaho Code page has no section in its code region")
    return "\n".join(lines) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute":
        return code_html_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if src["doc_type"] == "statute" and src["jurisdiction"] == "idaho":
        number = re.search(r"\d+-\d+(?:-\d+)?[A-Za-z]?\s*$", src["citation"])
        if not number or not any(l.startswith(f"{number.group(0)}.") for l in text.splitlines()):
            raise ValueError(f"{src['id']}: page is not {src['citation']} (section mismatch)")
        return True
    if src["doc_type"] == "executive_order" and src["jurisdiction"] == "idaho":
        # the Governor's order prints its heading as a line of its own, "EXECUTIVE ORDER NO. 2022-06" (a scan
        # may read it with its punctuation slightly off); an order that cites it further down is not it
        number = re.search(r"\d{2,4}-\d{2}", src["citation"])
        head = [_squash(l) for l in text.splitlines() if l.strip()][:12]
        if not number or not any(re.fullmatch(rf"executive order (?:no[.,]? ?)?{number.group(0)}", l) for l in head):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: "
                             f"{src['citation']!r} is not the order's heading line (its first lines)")
        return True
    return False


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and src["jurisdiction"] == "idaho":
        return ("Text taken from the Legislature's Idaho Code section page: the title and chapter headings, "
                "then the section and its history line, one line per paragraph. Site menu, search forms, "
                "print and PDF buttons and footer removed.")
    return None


# A PDF policy or standard prints its date on a line of its own: "Effective Date: May 5, 2026",
# "Effective date is August 25, 2011." or, under the version line of a data standard,
# "Effective July 20, 2023". The shared reader takes the first "Effective date" label anywhere, and
# the data standards carry data-dictionary rows ("Effective date of current map revision ... 7/7/2009")
# that are not the standard's date. Only a line that starts with the label and is followed by the date counts.
_DATE_LINE = re.compile(
    rf"^\s*Effective(?:\s+date)?\s*(?::|\bis\b)?\s+"
    rf"(?:(?P<long>(?:{_MONTHS})\s+\d{{1,2}},\s+\d{{4}})|(?P<us>\d{{1,2}}[/-]\d{{1,2}}[/-]\d{{4}}))", re.I)


def effective_date(text, doc_type):
    for line in text.splitlines():
        m = _DATE_LINE.match(line)
        if not m:
            continue
        if m.group("long"):
            h = _LONG_DATE.search(m.group("long"))
            mon, d, y = _MONTHS.split("|").index(h.group(1)) + 1, int(h.group(2)), int(h.group(3))
        else:
            h = _US_DATE.search(m.group("us"))
            mon, d, y = int(h.group(1)), int(h.group(2)), int(h.group(3))
        if 1 <= mon <= 12 and 1 <= d <= 31:
            return f"{y:04d}-{mon:02d}-{d:02d}"
    return None
