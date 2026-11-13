"""Oregon: ORS and OAR pages, and the Governor's orders. Hooks are described in src/states/__init__.py."""
from __future__ import annotations

import datetime
import re

from src.ingest_common import _clean_line, _decode, _squash, paragraph_html_to_text


def oar_html_to_text(raw: bytes) -> str:
    """The Secretary of State's OAR division page. Only the `#content` region is text of the
    rules: the site navigation, footer and scripts around it are not. One line per block
    element or <br>; a blank line before each rule."""
    page = _decode(raw)
    start = page.find('id="content"')
    end = page.find("sos-footer-wrapper")
    if start < 0 or end < start:
        raise ValueError("OAR page has no #content region: the page layout changed")
    start = page.index(">", start) + 1               # after the opening tag
    end = page.rindex("<", 0, end)                   # before the footer's opening tag
    region = re.sub(r"<(script|style).*?</\1>", " ", page[start:end], flags=re.S | re.I)
    region = re.sub(r"<div class='rule_div'>", "\n\x00", region)
    region = re.sub(r"<br\s*/?>|</?(p|div|h[1-6])\b[^>]*>", "\n", region, flags=re.I)
    region = re.sub(r"<[^>]+>", "", region)
    out: list[str] = []
    for raw_line in region.split("\n"):
        marked = raw_line.startswith("\x00")
        line = _clean_line(raw_line.replace("\x00", ""))
        if marked and out:
            out.append("")
        if line:
            out.append(line)
    return "\n".join(out) + "\n"


# ---- statutes: one provision of a chapter page ---------------------------------------------
# The Legislative Counsel serves a whole chapter per page. A document may be the provision, not the chapter:
# `slice: {section_start, section_end_before}`, printed section numbers; the end section is not in it.

_HEADING = re.compile(r"^(\d{1,3}[A-Z]?\.\d{3}[A-Z]?)(?: |$)")
_RULE = re.compile(r"^_{5,}$")              # the page's closing rule, after the last section of the chapter


def _body_headings(lines: list[str]) -> list[tuple[int, str]]:
    """(line index, section number) of every heading in the chapter's body. The page prints a contents list first, whose
    entries are `291.034 Title` with nothing after the title; the body prints the same number and title, then `.` and the
    text. A bracketed entry (`291.035 [2014 c.77 ...; renumbered 276A.223 in 2017]`) is in the body only, and is a heading
    too: it ends the section above it."""
    heads = [(i, m.group(1)) for i, line in enumerate(lines) if (m := _HEADING.match(line))]
    return [(i, num) for i, num in heads
            if not any(later.startswith(lines[i] + ".") for later in lines[i + 1:])]


def slice_chapter(text: str, start: str, end_before: str) -> str:
    """The lines from the heading of section `start` to the line before the heading of the first `end_before` section after it."""
    lines = text.splitlines()
    heads = _body_headings(lines)
    first = [i for i, num in heads if num == start]
    if len(first) != 1:
        raise ValueError(f"section {start} is printed {len(first)} times as a heading in the chapter page "
                         f"(the layout changed, the section was renumbered, or the slice is wrong)")
    stop = next((i for i, num in heads if num == end_before and i > first[0]), None)
    if stop is None:
        raise ValueError(f"heading {end_before} does not follow section {start} in the chapter page: "
                         f"the slice would be a guess")
    return "\n".join(lines[first[0]:stop]) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute":
        text = paragraph_html_to_text(raw)
        return slice_chapter(text, slice_["section_start"], slice_["section_end_before"]) if slice_ else text
    if fmt == "html" and doc_type == "rule":
        return oar_html_to_text(raw)
    return None


_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December"]
_OPERATIVE = re.compile(r"\b(?:operative|effective|takes effect)\b[^.\[\]]{0,40}?\b(" + "|".join(_MONTHS)
                        + r")\s+(\d{1,2}),\s+(\d{4})", flags=re.I)
_ORS_CITATION = re.compile(r"ORS (\d{1,3}[A-Z]?\.\d{3}[A-Z]?)(?: to (\d{1,3}[A-Z]?\.\d{3}[A-Z]?))?")


def _not_yet_operative(text: str, today: datetime.date | None = None) -> list[str]:
    """ISO dates after `today` that the text prints as the day a provision becomes operative or effective."""
    today = today or datetime.date.today()
    out = []
    for mon, day, year in _OPERATIVE.findall(" ".join(text.split())):
        try:
            d = datetime.date(int(year), _MONTHS.index(mon.capitalize()) + 1, int(day))
        except ValueError:
            continue
        if d > today:
            out.append(d.isoformat())
    return out


def _check_statute_slice(src, text, what_is):
    """A slice is the cited provision when it opens on the heading of the first cited section, its last heading is the
    last cited section (bracketed entries for renumbered or repealed sections are not sections), the first heading is not a
    repeal or renumbering entry, and no date after today is printed as the day it becomes operative."""
    cite = _ORS_CITATION.fullmatch(src["citation"])
    lines = text.splitlines()
    if not cite or not lines:
        raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: no usable citation or no text")
    first, last = cite.group(1), cite.group(2) or cite.group(1)
    if lines[0].startswith(first + " ["):       # the page prints a repealed or renumbered section as its history only
        raise ValueError(f"{src['id']}: {src['citation']} is printed as repealed or renumbered: not in force")
    heads = [(i, n) for i, n in _body_headings(lines) if not re.match(rf"^{re.escape(n)} \[", lines[i])]
    sl = src.get("slice") or {}
    if sl.get("section_start") != first or not lines[0].startswith(first + " ") or not heads or heads[-1][1] != last:
        raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: the slice opens on "
                         f"{lines[0].split(' ')[0]!r} and its last section is {heads[-1][1] if heads else None!r}")
    if later := _not_yet_operative(text):
        raise ValueError(f"{src['id']}: {what_is} prints a date after today as the day it becomes operative "
                         f"({', '.join(sorted(set(later)))}): its text is not shown to be the law in force")
    return True


def check_identity(src, text, what_is):
    if src["doc_type"] == "statute" and src["jurisdiction"] == "oregon" and src.get("slice"):
        return _check_statute_slice(src, text, what_is)
    if src["doc_type"] == "executive_order" and src["jurisdiction"] == "oregon":
        # the Governor's order prints its heading as the first line of its own, "EXECUTIVE ORDER NO. 23-26"
        # (a scan may read it with its spacing and punctuation slightly off); an order that cites it
        # further down is not it
        number = re.search(r"\d{2,4}-\d{2}", src["citation"])
        head = [_squash(l) for l in text.splitlines() if l.strip()][:8]
        if not number or not any(re.fullmatch(rf"executive order (?:no[.,]? ?)?{number.group(0)}", l) for l in head):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: "
                             f"{src['citation']!r} is not the order's heading line (its first lines)")
        return True
    return False


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and src.get("slice"):
        sl = src["slice"]
        return (f"The source serves the whole chapter as one page; this document is the provision {src['citation']}, "
                f"the lines from the heading of section {sl['section_start']} to the line before the heading of section "
                f"{sl['section_end_before']}, as the page prints them: heading, text, history note and any Note lines under it. "
                "HTML paragraphs unwrapped to one line per source paragraph; markup, spacing paragraphs and non-breaking "
                "spaces removed.")
    if src["doc_type"] == "statute":
        return ("HTML paragraphs unwrapped to one line per source paragraph; markup, spacing "
                "paragraphs and non-breaking spaces removed. The source serves the whole "
                "chapter as one page, so this document is the whole chapter.")
    if src["doc_type"] == "rule":
        return ("Rule text taken from the page's rule region; site navigation, footer and scripts "
                "removed. One line per source line; a blank line before each rule number.")
    return None
