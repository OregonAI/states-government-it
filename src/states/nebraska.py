"""Nebraska: the Legislature's whole-chapter statute pages. Hooks are described in src/states/__init__.py.

`https://nebraskalegislature.gov/laws/display-chapters.php?chapter=N` (the "View Print Friendly" link beside each
chapter on browse-statutes.php) serves one chapter as a run of `<div class="printwidth">` blocks, one per section:
a bold `number.` and caption, one `<p>` per paragraph, then a `source` div (the session laws, and an
`Operative Date:` line when a later act sets one). A document is a run of sections of that page, named in the seed
entry as `slice: {article: <first section>, part: <last section>}` (the seed check allows only the keys `article`
and `part`; here they are the first and the last section number, inclusive). The policy library (nitc.nebraska.gov)
serves PDFs, which the shared reader handles."""
from __future__ import annotations

import re

from src import states
from src.ingest_common import BlockParser, _decode

_BLOCK = '<div class="printwidth">'
_NUMBER = r"\d+-\d+(?:[.,]\d+)?"
_HEAD = re.compile(rf"<strong>\s*({_NUMBER})\.")


def _sections(page: str) -> list[tuple[str, str]]:
    """[(section number, the block's html)] in page order."""
    starts = [m.start() for m in re.finditer(re.escape(_BLOCK), page)]
    end = page.lower().rfind("</body>")
    blocks = [page[a:b] for a, b in zip(starts, starts[1:] + [end if end > 0 else len(page)])]
    out = []
    for b in blocks:
        m = _HEAD.search(b)
        if m:
            out.append((m.group(1), b))
    return out


def _block_lines(block: str) -> list[str]:
    parser = BlockParser()
    # the page pads the "Source:" label with a 0.05in margin, which a browser draws as a space
    parser.feed(block.replace("Source:</strong></span>", "Source:</strong></span> "))
    parser._flush()
    return parser.lines


def statute_html_to_text(raw: bytes, slice_: dict | None) -> str:
    """The slice's sections to text: one line per paragraph, the heading (number and caption) on one line, the
    `Source:` line and the `Operative Date:` line kept, a blank line before each section after the first. Nothing
    inside a section is dropped; links, markup and the page's style sheet are."""
    if not slice_ or not slice_.get("article") or not slice_.get("part"):
        raise ValueError("a Nebraska statute entry needs a slice: {article: <first section>, part: <last section>}")
    secs = _sections(_decode(raw))
    if not secs:
        raise ValueError("no statute text: the page holds no section blocks (the layout changed, or this is not a "
                         "chapter page)")
    numbers = [n for n, _ in secs]
    first, last = slice_["article"], slice_["part"]
    for want in (first, last):
        if numbers.count(want) != 1:
            raise ValueError(f"the page holds section {want} {numbers.count(want)} times: the slice would be a guess")
    a, b = numbers.index(first), numbers.index(last)
    if a > b:
        raise ValueError(f"slice runs backwards: {first} comes after {last}")
    lines: list[str] = []
    for _, block in secs[a:b + 1]:
        if lines:
            lines.append("")
        lines += _block_lines(block)
    return "\n".join(lines) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute":
        return statute_html_to_text(raw, slice_)
    return None


def _check_executive_order(src, text, what_is):
    """The Governor's PDFs print `EXECUTIVE ORDER NO. 25-04` (or `No. 23-05`) as a heading line of their own, so the
    default reader's `Executive Order 25-04` never matches. A line that is that heading, with the cited number
    exactly, is required; a mention of the number in another order's text is not an identity."""
    cited = re.search(r"\b\d{2}-\d{2}\b", src["citation"])
    heading = re.compile(r"^\s*EXECUTIVE ORDER\s+(?:NO\.?\s*)?(\d{2}-\d{2})\s*$", flags=re.M | re.I)
    printed = heading.findall(text)
    if not cited or cited.group(0) not in printed:
        raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: no heading line "
                         f"'EXECUTIVE ORDER NO. {cited and cited.group(0)}' (headings found: {printed})")
    return True


def check_identity(src, text, what_is):
    """A statute's text opens with the first section the citation names and ends with the last one named; an
    executive order carries its own heading line."""
    if src["jurisdiction"] != "nebraska":
        return False
    if src["doc_type"] == "executive_order":
        return _check_executive_order(src, text, what_is)
    if src["doc_type"] != "statute":
        return False
    cited = re.findall(_NUMBER, src["citation"])
    if not cited:
        raise ValueError(f"{src['id']}: citation {src['citation']!r} names no section")
    heads = [m.group(1) for m in re.finditer(rf"^({_NUMBER})\. ", text, flags=re.M)]
    if not heads or heads[0] != cited[0] or heads[-1] != cited[-1]:
        raise ValueError(f"{src['id']}: page is not {src['citation']}: the text runs from section "
                         f"{heads[:1]} to {heads[-1:]} (the instrument is not the cited one)")
    return True


_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December"]
_MONTH_RE = "|".join(_MONTHS)
_SIGNED = re.compile(rf"\bthis\s+(\d{{1,2}})(?:st|nd|rd|th)?\s+day\s+of\s+({_MONTH_RE}),?\s+(\d{{4}})", re.I)
_LONG = re.compile(rf"\b({_MONTH_RE})\s+(\d{{1,2}}),\s+(\d{{4}})")
_HISTORY = re.compile(r"^\s*History:(.*?)(?=^\s*URL:|\n\s*\n|\Z)", re.M | re.S)


def effective_date(text, doc_type):
    """An executive order prints no effective-date label; it prints the day the Governor signed it ('this 5th day of
    March, 2025'), which is its date. Everything else goes to the shared reader."""
    if doc_type != "executive_order":
        return states.UNHANDLED
    m = _SIGNED.search(text)
    if not m:
        return states.UNHANDLED
    return f"{int(m.group(3)):04d}-{_MONTHS.index(m.group(2).capitalize()) + 1:02d}-{int(m.group(1)):02d}"


def _history_dates(text):
    m = _HISTORY.search(text)
    if not m:
        return []
    return sorted((int(y), _MONTHS.index(mo) + 1, int(d)) for mo, d, y in _LONG.findall(m.group(1)))


def source_version(text, doc_type, fmt):
    """Every NITC section ends in 'History: Adopted on ... Amended on ...'. The latest date on that line is the
    version of the text; adoption is not read as an effective date (the section does not say when it takes effect)."""
    if doc_type not in ("policy", "standard"):
        return None
    dates = _history_dates(text)
    if not dates:
        return None
    y, mo, d = dates[-1]
    return f"History through {_MONTHS[mo - 1]} {d}, {y}"


def extra_notes(src, fmt, text, eff, version):
    out = ""
    if src["doc_type"] == "executive_order" and eff:
        out += " effective_date is the day the Governor signed the order, as its closing line prints it (this Nth day of Month, Year)."
    if version:
        out += (" source_version is the latest date on the section's History line (adoption, renumbering or amendment); "
                "the section prints no separate effective date, so effective_date stays empty.")
    return out


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and src["jurisdiction"] == "nebraska":
        return ("Text taken from the Legislature's print-friendly chapter page, cut to the sections the citation names "
                "(first and last inclusive): each section's number and caption, its paragraphs, its session-law source "
                "line and any Operative Date line, one line per paragraph. Links, markup and the page's style sheet "
                "removed. A blank line precedes each section after the first. A section the page prints as repealed "
                "stays as printed.")
    return None
