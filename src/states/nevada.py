"""Nevada: NRS and NAC chapter pages (Legislative Counsel Bureau, leg.state.nv.us). Hooks are described in
src/states/__init__.py. Nevada's policy library is PDF and Word, which the shared readers handle."""
from __future__ import annotations

import re

from src.ingest_common import _squash, paragraph_html_to_text

# The glyph the LCB prints for a sentence that continues after a list is the character 0xCA set in the
# Wingdings 3 font (a hanging arrow); read as text it is "Ê", which is not in the law.
_WINGDINGS = re.compile(rb"""<span\s+style=['"]font-family:\s*"?Wingdings 3"?['"]>.*?</span>""", flags=re.S | re.I)

_CHAPTER = re.compile(r"\b(NRS|NAC)\s+ch\.\s+(\w+)", flags=re.I)


def lcb_html_to_text(raw: bytes) -> str:
    """The LCB's Word-exported chapter page: one line per source paragraph (the shared paragraph reader),
    with the Wingdings continuation glyph removed first. The revision stamp, the chapter's table of
    contents, every section and its history line stay."""
    return paragraph_html_to_text(_WINGDINGS.sub(b"", raw))


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type in ("statute", "rule"):
        return lcb_html_to_text(raw)
    return None


# A policy or standard prints its own number and title in its heading block (policy 100's title page; the
# `Document ID / Title` row of a standard); other documents of the security library cite it in their text.
# The security library's files (ids nv-sec-*) head within six non-blank lines (measured on all 38 committed
# texts: line 1 or 4); a standard's scope paragraph, which cites policy 100, starts after that. The GTO
# governance files (a memo, bylaws, guidelines) print a letterhead first, so they get twenty.
_HEADING_LINES = {"nv-sec-": 6}
_HEADING_DEFAULT = 20


def _heading_identity(src, text, what_is):
    """The identity phrase must stand in the first lines of the text, not anywhere in it: the phrase
    'State Information Security Program Policy' is printed in the body of dozens of other library files.
    Returns False after this check so the shared `default_identity` still runs over the whole text."""
    phrase = src.get("identity_text") or src["title"]
    n = next((v for k, v in _HEADING_LINES.items() if src["id"].startswith(k)), _HEADING_DEFAULT)
    lines = [l for l in text.splitlines() if l.strip()][:n]
    # a title can wrap onto the next line, so the head is squashed as a whole
    if _squash(phrase) not in _squash("\n".join(lines)):
        raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {phrase!r} "
                         f"is not in its heading (first {n} lines)")
    return False


def check_identity(src, text, what_is):
    """A chapter page prints `CHAPTER <n> - <TITLE>` as its first or second line."""
    if src["jurisdiction"] != "nevada":
        return False
    if src["doc_type"] in ("policy", "standard"):
        return _heading_identity(src, text, what_is)
    if src["doc_type"] not in ("statute", "rule"):
        return False
    m = _CHAPTER.search(src["citation"])
    head = text.splitlines()[:3]
    if not m or not any(re.match(rf"CHAPTER {re.escape(m.group(2))} - ", l) for l in head):
        raise ValueError(f"{src['id']}: page is not {src['citation']} (title/chapter mismatch)")
    if src["doc_type"] == "rule" and src["title"] not in text:
        raise ValueError(f"{src['id']}: page does not carry the seed title {src['title']!r}")
    return True


def notes(src, fmt, text):
    if src["doc_type"] in ("statute", "rule"):
        kind = "NRS" if src["doc_type"] == "statute" else "NAC"
        return (f"HTML paragraphs unwrapped to one line per source paragraph; markup, spacing paragraphs and "
                f"non-breaking spaces removed, and the Wingdings 3 continuation glyph the Legislative Counsel Bureau "
                f"prints after a list (read as the letter E-circumflex) dropped. The source serves the whole {kind} "
                f"chapter as one page, so this document is the whole chapter: its revision stamp, its table of "
                f"contents, every section and the history line under each.")
    return None


def extra_notes(src, fmt, text, eff, version):
    if src.get("scan_layer"):
        return (" The PDF is a scan of a signed paper original; the text read here is the text layer the publisher "
                "embedded when it scanned the page (Adobe Paper Capture or a copier's recognition), a machine "
                "reading that can carry recognition errors in words and figures (a letterhead may read "
                "'Informatio11', the letters AI may read 'Al'). It is committed as served and is not human-verified: "
                "check any word or number against the PDF before relying on it.")
    return ""
