"""Oklahoma: the Office of Management and Enterprise Services' (OMES) standards and policies are PDFs, which the shared
reader handles. They print `Effective date: 03/06/2025` and `Last revised: 07/29/2026` as month/day/year: the shared label
reader takes the effective date, and this module keeps the revision as the document's version.

The statutes are the Legislature's per-title PDFs (Title 62 is 820 pages): the whole PDF is the snapshot and a document is
the sections from one printed heading to the next, cut here in `to_text` (the slice shape is `{section_start,
section_end_before}`, see _meta/sources/README.md and docs/research/oklahoma-statutes.md).
Hooks are described in src/states/__init__.py."""
from __future__ import annotations

import datetime
import re

from src.ingest_common import pdf_to_text
from src.states import UNHANDLED

_REVISED = re.compile(r"Last revised:\s*(\d{1,2}/\d{1,2}/\d{4})", flags=re.I)
_EFFECTIVE = re.compile(r"Effective date:\s*(\d{1,2})/(\d{1,2})/(\d{4})", flags=re.I)


def effective_date(text, doc_type):
    """The revision table's `Effective date: 07/30/2026`. The shared reader takes the first 'effective date' in the text, which in
    a standard's body can be a phrase ('before the effective date of this Standard'), so the table is read here."""
    m = _EFFECTIVE.search(text)
    if not m:
        return UNHANDLED
    mon, d, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return f"{y:04d}-{mon:02d}-{d:02d}" if 1 <= mon <= 12 and 1 <= d <= 31 else UNHANDLED


def source_version(text, doc_type, fmt):
    m = _REVISED.search(text)
    return f"Last revised {m.group(1)}" if m else None


def extra_notes(src, fmt, text, eff, version):
    """A seed entry's `currency_note` (what is and is not known about whether the text is current) is printed in the curator notes."""
    note = (src.get("currency_note") or "").strip()
    slice_note = notes_for_slice(src) if src.get("slice") and src["doc_type"] == "statute" else ""
    return f"{slice_note} {note}" if note and slice_note else (f" {note}" if note else slice_note)


# ---- statutes: one slice of a Legislature title PDF ------------------------------------------

_TITLE = re.compile(r"^\s*TITLE\s+(\d+[A-Z]?)\.", flags=re.I)
_LEADERS = re.compile(r"\.{5,}\s*\d*\s*$")
_FOOTER = re.compile(r"^Oklahoma Statutes - Title \d+[A-Z]?\. .*\bPage \d+$")


def _title_of(lines: list[str]) -> str:
    for line in lines[:10]:
        m = _TITLE.match(line)
        if m:
            return m.group(1)
    raise ValueError("the PDF does not print `TITLE n.` at its head: it is not an Oklahoma title file")


def _body_headings(lines: list[str], title: str) -> list[tuple[int, str]]:
    """(line index, section number) of every section heading `§62-34.43. Heading` that starts a line of the body.
    The contents lists every section too, in the same form; its entries are the ones with dot leaders and a page
    number, on the heading line or, when the entry wraps, on one of the next three lines."""
    head = re.compile(rf"^§{re.escape(title)}-(\S+?)\.(?:\s|$)")
    out = []
    for i, line in enumerate(lines):
        m = head.match(line)
        if not m:
            continue
        in_contents = False
        for follow in lines[i:i + 4]:
            if follow is not line and (not follow.strip() or head.match(follow)):
                break
            if _LEADERS.search(follow):
                in_contents = True
                break
        if not in_contents:
            out.append((i, m.group(1)))
    return out


def slice_title(text: str, start: str, end_before: str) -> str:
    """The lines from the heading of section `start` to the line before the heading of the next `end_before`
    section that follows it. A trailing page footer (the last page's furniture, which would be the end of the
    slice only because the next section starts a page) is dropped, and nothing else is."""
    lines = text.splitlines()
    heads = _body_headings(lines, _title_of(lines))
    first = [i for i, num in heads if num == start]
    if len(first) != 1:
        raise ValueError(f"section {start} is printed {len(first)} times as a heading in the title PDF "
                         f"(the layout changed, the section was renumbered, or the slice is wrong)")
    stop = next((i for i, num in heads if num == end_before and i > first[0]), None)
    if stop is None:
        raise ValueError(f"heading {end_before} does not follow section {start} in the title PDF: "
                         f"the slice would be a guess")
    cut = lines[first[0]:stop]
    while cut and (not cut[-1].strip() or _FOOTER.match(cut[-1])):
        cut.pop()
    return "\n".join(cut) + "\n"


def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "pdf" and doc_type == "statute" and slice_:
        return slice_title(pdf_to_text(raw), slice_["section_start"], slice_["section_end_before"])
    return None


_EFF_DATE = re.compile(r"\beff\.\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+(\d{1,2}),\s+(\d{4})")
_MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def _not_yet_in_effect(text: str, today: datetime.date | None = None) -> list[str]:
    """ISO dates after `today` that an amendment note (`Laws 2026, c. 445, § 131, eff. Jan. 1, 2027`) prints. The
    Legislature codifies an act that takes effect later as the section's text, so a PDF printed in November 2026 holds
    the January 2027 version of a section as its only text: it is not the law in force."""
    today = today or datetime.date.today()
    out = []
    for mon, day, year in _EFF_DATE.findall(" ".join(text.split())):
        try:
            d = datetime.date(int(year), _MON.index(mon) + 1, int(day))
        except ValueError:
            continue
        if d > today:
            out.append(d.isoformat())
    return out


_CITATION = re.compile(r"(\d+[A-Z]?) O\.S\. (\S+?)(?: to (\S+))?")


def check_identity(src, text, what_is):
    """A statute slice is the cited one when it opens on the heading of the first cited section, closes on the
    last heading it holds being the last cited section, and, for a single section, that heading is not a
    repeal or renumbering notice."""
    if src["doc_type"] != "statute" or src["jurisdiction"] != "oklahoma":
        return False
    cite = _CITATION.fullmatch(src["citation"])
    sl = src.get("slice") or {}
    lines = text.splitlines()
    if not cite or not lines:
        raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: no usable citation or no text")
    title, first, last = cite.group(1), cite.group(2), cite.group(3) or cite.group(2)
    heads = _body_headings(lines, title)
    if (sl.get("section_start") != first or not heads or heads[0] != (0, first)
            or heads[-1][1] != last):
        raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: the slice opens on "
                         f"{heads[0][1] if heads else None!r} and its last heading is "
                         f"{heads[-1][1] if heads else None!r}")
    if later := _not_yet_in_effect(text):
        raise ValueError(f"{src['id']}: {what_is} prints an amendment taking effect {', '.join(sorted(set(later)))}, "
                         f"after today: its text is not shown to be the law in force")
    if not cite.group(3) and re.search(r"\b(Repealed|Renumbered)\b", lines[0]):
        raise ValueError(f"{src['id']}: {src['citation']} is printed as repealed or renumbered: not in force")
    return True


def notes_for_slice(src) -> str:
    sl = src.get("slice") or {}
    return (f" The source is the Legislature's file for the whole of Title {src['citation'].split()[0]} (the PDF is the "
            f"snapshot); this document is the sections from the heading of section {sl.get('section_start')} to the "
            f"line before the heading of section {sl.get('section_end_before')}, as the PDF prints them: section "
            f"headings, text, the amendment notes under each section, and the page footer where a page break falls "
            f"inside a section. Where a section has more than one version, the Legislature prints a `See the "
            f"following versions` heading and each version with its own act and effective date; both are kept "
            f"as printed.")
