"""Oklahoma: the Office of Management and Enterprise Services' (OMES) standards and policies are PDFs, which the shared
reader handles. They print `Effective date: 03/06/2025` and `Last revised: 07/29/2026` as month/day/year: the shared label
reader takes the effective date, and this module keeps the revision as the document's version.

The statutes are not read here: the Legislature serves each title as one PDF (Title 62 is 687 pages) and the shared seed check
and the drift detector have no PDF slice; see the seed file's stubs and docs/research/oklahoma-statutes.md.
Hooks are described in src/states/__init__.py."""
from __future__ import annotations

import re

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
    return f" {note}" if note else ""
