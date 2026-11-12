"""Pennsylvania: statute PDFs from the General Assembly (palegis.us) and executive-order, management-directive and
IT-policy PDFs from the Office of Administration (pa.gov). Every source is a PDF the shared reader handles; only the
identity check differs. Hooks are described in src/states/__init__.py.

A statute PDF opens with the act's title and "Act of <date>, P.L. n, No. n", not with a "Chapter n" line, so the
shared statute check (which expects a chapter page) cannot be used. An executive-order PDF prints its number in a
two-column title block ("Number: 2016-06, As Amended"), or in its heading ("Executive Order 2023-19"), and the shared
check looks only for the heading form.

A policy or directive (Management Directive or IT Policy) is told apart by a phrase in its title block, the first
_TITLE_BLOCK characters. The shared check accepts the phrase anywhere, and these PDFs cross-reference one another
('Data Classification Policy', 'IT Policy Governance', 'MD 205.34'), so a wrong file would pass it."""
from __future__ import annotations

import re

from src.ingest_common import _squash

_ACT_NUMBER = re.compile(r"\bNo\.\s*(\d+)\b")
_ORDER_NUMBER = re.compile(r"\d{4}-\d{2}")
_TITLE_BLOCK = 800


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "pennsylvania":
        return False
    if src["doc_type"] == "statute":
        head = _squash(text[:1500]).casefold()
        number = _ACT_NUMBER.search(src["citation"])
        phrase = _squash(src.get("identity_text") or src["title"]).casefold()
        if not number or phrase not in head or f"no. {number.group(1)} " not in head + " ":
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: the title {src['title']!r} and "
                             f"'No. {number and number.group(1)}' do not both open its text")
        return True
    if src["doc_type"] == "executive_order":
        m = _ORDER_NUMBER.search(src["citation"])
        found = bool(m) and re.search(rf"(?<![\d-]){re.escape(m.group(0))}(?![\d-])", text[:3000]) \
            and "executive order" in text[:3000].casefold()
        if not found:
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: 'Executive Order "
                             f"{m and m.group(0)}' is not in its title block")
        return True
    if src["doc_type"] == "policy" and what_is == "PDF":
        phrase = _squash(src.get("identity_text") or src["title"]).casefold()
        if phrase not in _squash(text[:_TITLE_BLOCK]).casefold():
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {phrase!r} is not in its title "
                             f"block (the first {_TITLE_BLOCK} characters)")
        return True
    return False

