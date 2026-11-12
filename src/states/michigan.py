"""Michigan: the executive orders the Legislature archives at www.legislature.mi.gov/Home/GetObject (older
orders are Word- or Vignette-made HTML pages; newer ones PDFs, which the shared reader handles) and the identity
checks for those orders and for the per-act statute PDFs (www.legislature.mi.gov/documents/mcl/pdf/). Hooks are
described in src/states/__init__.py."""
from __future__ import annotations

import html as html_mod
import re

_BLOCK = re.compile(r"</?(?:p|div|br|tr|td|th|table|tbody|hr|h[1-6]|li|ul|ol|blockquote|center)\b[^>]*>", re.I)
_FURNITURE = (re.compile(r"^www\.michigan\.gov$", re.I),
              re.compile(r"^\(To Print: use your browser's print function\)$", re.I),
              re.compile(r"^Copyright © \d{4} State of Michigan$", re.I))


def _decode(raw: bytes) -> str:
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252", errors="replace")


def eo_html_to_text(raw: bytes) -> str:
    """An executive order as the Legislature archives it: a Word-exported page or a Vignette print page. The
    head (title, style block, scripts), comments and tags go; each paragraph, heading line, line break and table
    cell is one line, wrapped source lines are joined, entities are decoded. The print bar (`www.michigan.gov`,
    `(To Print: ...)`) and the `Copyright (c) <year> State of Michigan` footer are page furniture and go; the
    page's `Release Date` and `Last Update` lines stay."""
    page = _decode(raw)
    page = re.sub(r"<!--.*?-->", "", page, flags=re.S)
    page = re.sub(r"<(head|script|style)\b.*?</\1>", "", page, flags=re.S | re.I)
    page = _BLOCK.sub("\x00", page)                 # a block tag ends a line; a newline in the source does not
    page = re.sub(r"<[^>]+>", "", page)
    page = html_mod.unescape(page).replace("\xa0", " ")
    out = []
    for line in page.split("\x00"):
        line = " ".join(line.split())
        if line and not any(p.match(line) for p in _FURNITURE):
            out.append(line)
    return "\n".join(out) + "\n"


def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "executive_order":
        return eo_html_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "michigan":
        return False
    head = " ".join(text[:600].split())
    if src["doc_type"] == "executive_order":
        m = re.search(r"(\d{4})\s*-\s*0*(\d+)", src["citation"])
        if not m:
            raise ValueError(f"{src['id']}: citation {src['citation']!r} has no order number")
        # The order's own heading is the FIRST 'EXECUTIVE ORDER' in the text, and the number must follow it
        # directly (the 'No. n' line is next, or the same line). A later mention of another order (a rescission,
        # a transfer) is never the heading, however near the top it falls.
        flat = " ".join(text.split())
        first = re.search(r"EXECUTIVE\s+ORDER\b", flat, re.I)
        own = re.compile(rf"\s*(?:NO\.?)?\s*{m.group(1)}\s*[-–]\s*0*{m.group(2)}\b", re.I)
        if not (first and own.match(flat, first.end())):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: its first 'Executive Order' "
                             f"heading is not 'Executive Order No. {m.group(1)}-{m.group(2)}'")
        return True
    if src["doc_type"] == "statute":
        m = re.match(r"Act (\d+) of (\d{4})", src["citation"])
        if not m or f"Act {m.group(1)} of {m.group(2)}" not in head:
            raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: the head of the text does not "
                             f"carry 'Act {m and m.group(1)} of {m and m.group(2)}'")
        return True
    return False


def notes(src, fmt, text):
    if fmt != "html":
        return None
    return ("Text taken from the archive copy of the order on the Michigan Legislature's website "
            "(www.legislature.mi.gov), a Word- or Vignette-made HTML page: each paragraph, heading line and table "
            "cell is one line, lines the source wrapped are joined, and entities are decoded. The page's style "
            "block, the print bar (www.michigan.gov, the print hint) and the copyright footer were removed; "
            "its Release Date and Last Update lines are kept as printed. The Legislature marks its executive "
            "order documents as presented for archival purposes.")
