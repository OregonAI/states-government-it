"""North Dakota: the Legislative Council's chapter PDFs (Century Code, Administrative Code), NDIT's policy PDFs and the
Governor's order PDFs, all of which the shared readers handle. The only hook is the identity check: the shared one
reads the chapter number as its first digits (54 for 54-59.1), and its order check would accept a mention of the
number. Hooks are described in src/states/__init__.py.

A chapter PDF opens with `CHAPTER 54-59` and the chapter title on the next line; an Administrative Code chapter PDF
carries `CHAPTER 113-02-01` after its article contents. An order opens with its own `EXECUTIVE ORDER 2026-06` line."""
from __future__ import annotations

import re

_CHAPTER = re.compile(r"^\s*CHAPTER ([0-9.\-]+)\s*$", re.M)
_RISK_MATRIX = re.compile(r"^\s*AI Risk Matrix\s*$", re.M)
_ORDER = re.compile(r"^\s*EXECUTIVE ORDER ([0-9.\-]+)\s*$", re.M | re.I)


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "north-dakota":
        return False
    kind = src["doc_type"]
    if kind in ("statute", "rule"):
        cite = re.search(r"([0-9][0-9.\-]*[0-9])\s*$", src["citation"])
        if not cite or cite.group(1) not in _CHAPTER.findall(text):
            raise ValueError(f"{src['id']}: {what_is} is not {src['citation']} (no heading line "
                             f"'CHAPTER {cite and cite.group(1)}')")
        return True
    if kind == "policy":
        # The policy PDFs print Created/Revised/Reviewed, then the title centred on a line of its own. The shared
        # check only looks for the title anywhere, and the policies name one another.
        head = "\n".join(text.splitlines()[:15])
        if not re.search(rf"^\s*{re.escape(src['title'])}\s*$", head, re.M):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: no heading line "
                             f"{src['title']!r} at the top of its text")
        return True
    if kind == "executive_order":
        number = re.search(r"\d{4}-\d{2}(?:\.\d+)?", src["citation"])
        if not number or number.group(0) not in _ORDER.findall(text):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: no heading line "
                             f"'Executive Order {number and number.group(0)}' in its text")
        return True
    return False


def extra_notes(src, fmt, text, eff, version):
    """The AI Guideline's page 6 is the 'AI Risk Matrix', a picture (563 x 459, no text layer) under a heading that
    does have text. pdftotext reads only the heading and the footnote, so the matrix's wording is not in the text."""
    if src["doc_type"] == "policy" and fmt == "pdf" and _RISK_MATRIX.search(text):
        return (" Page 6 of the PDF carries the 'AI Risk Matrix' as an image (a matrix of use cases by risk of impact "
                "and risk of data breach) with no text layer: the heading and the note beneath it are in the text, "
                "the matrix's own wording is not mirrored here. Read it at the source URL.")
    return ""
