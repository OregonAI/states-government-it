"""Kentucky: the General Assembly serves each KRS section as its own one-page PDF (`statute.aspx?id=<n>`) and each
administrative regulation as a PDF (`/law/kar/downloads/docs/<n>/document.engrossed.pdf`, linked from the regulation's
page under "Download PDF"); the Commonwealth Office of Technology publishes its policies, standards and guidelines as
PDFs and its executive orders as scans (read by the shared two-engine OCR). Every one of those is a shared format, so
this module only identifies the instrument and reads the regulation's effective date. Hooks are described in
src/states/__init__.py.

A KRS section PDF opens with `42.724 Commonwealth Office of Technology.` (number, catchline) and ends with its
`Effective:` and `History:` lines; the section is the document, not the chapter. A regulation PDF prints
`200 KAR 1:016. Data breach notification forms.` and ends its history line with `eff. 1-3-2023.`. A policy PDF prints
its number with an en dash (`CIO–050`), which the shared identity check's squashing already treats as a hyphen. An
executive order's scan prints its number in the heading block, before the first "WHEREAS"; the orders recite one
another, so a mention after that point does not identify the instrument."""
from __future__ import annotations

import re

from src.ingest_common import _squash
from src.states import UNHANDLED

_SECTION_CITE = re.compile(r"^KRS (?P<n>\d+[A-Z]?\.\d+)$")
_RULE_CITE = re.compile(r"^(?P<n>\d+ KAR \d+:\d+)$")
_EO_CITE = re.compile(r"^Executive Order (?P<n>\d{4}-\d{2,4})$")
_EFF = re.compile(r"\beff\.\s+(\d{1,2})-(\d{1,2})-(\d{4})")


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "kentucky":
        return False
    kind = src["doc_type"]
    if kind == "statute":
        m = _SECTION_CITE.match(src["citation"])
        if not m or not re.match(rf"{re.escape(m.group('n'))}\s", text):
            raise ValueError(f"{src['id']}: {what_is} is not {src['citation']} (it does not open with the section number)")
        return True
    if kind == "rule":
        m = _RULE_CITE.match(src["citation"])
        want = f"{m.group('n')}. {src['title']}" if m else ""
        if not m or _squash(want) not in _squash(text):
            raise ValueError(f"{src['id']}: {what_is} is not {src['citation']} ({want!r} does not appear in its text)")
        return True
    if kind == "executive_order":
        m = _EO_CITE.match(src["citation"])
        head = re.split(r"whereas", text, maxsplit=1, flags=re.I)[0]
        a, b = (m.group("n").split("-") if m else ("", ""))
        if not m or not re.search(rf"(?<!\d){a}\s*-\s*{b}(?!\d)", head):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: '{src['citation']}' is not the "
                             f"number in the heading before the first 'whereas'")
        return True
    return False


def effective_date(text, doc_type):
    """A regulation's history line ends `eff. 1-3-2023.`; the last `eff.` date is the version in force."""
    if doc_type != "rule":
        return UNHANDLED
    dates = _EFF.findall(text)
    if not dates:
        return None
    mon, day, year = (int(x) for x in dates[-1])
    return f"{year:04d}-{mon:02d}-{day:02d}" if 1 <= mon <= 12 and 1 <= day <= 31 else None
