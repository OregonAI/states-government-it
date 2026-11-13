"""Nevada: NRS and NAC chapter pages (Legislative Counsel Bureau, leg.state.nv.us). Hooks are described in
src/states/__init__.py. Nevada's policy library is PDF and Word, which the shared readers handle."""
from __future__ import annotations

import re

from src.ingest_common import _squash, paragraph_html_to_text

# The glyph the LCB prints for a sentence that continues after a list is the character 0xCA set in the
# Wingdings 3 font (a hanging arrow); read as text it is "Ê", which is not in the law.
_WINGDINGS = re.compile(rb"""<span\s+style=['"]font-family:\s*"?Wingdings 3"?['"]>.*?</span>""", flags=re.S | re.I)

_CHAPTER = re.compile(r"\b(NRS|NAC)\s+ch\.\s+(\w+)", flags=re.I)
_SECTION_CITE = re.compile(r"NRS (\d+[A-Z]?\.\d+[A-Z]?)(?: to (\d+[A-Z]?\.\d+[A-Z]?))?")
_EFFECTIVE_MARK = re.compile(r"\[Effective\b|\bnot yet effective\b", flags=re.I)


def lcb_html_to_text(raw: bytes) -> str:
    """The LCB's Word-exported chapter page: one line per source paragraph (the shared paragraph reader),
    with the Wingdings continuation glyph removed first. The revision stamp, the chapter's table of
    contents, every section and its history line stay."""
    return paragraph_html_to_text(_WINGDINGS.sub(b"", raw))


# ---- a section of a whole-chapter NRS page ---------------------------------------
# The LCB serves a whole chapter per page: the revision stamp, the title and chapter lines, a table of contents
# (one `NRS 281.195 Title` line per section, with the group headings between them), then the body, where each
# section's heading line is followed by its text and a history line. A document may be one section of it
# (`slice: {section_start, section_end_before}`, README of the seed list): from the section's body heading to the
# line before the next section's body heading, less the group heading (`USE OF COMPUTERS`) that the page prints
# between two sections and that belongs to the next.

_HEADING = re.compile(r"^NRS (\d+[A-Z]?)\.(\d+[A-Z]?)(?:\s|$)")
_GROUP_HEADING = re.compile(r"^[A-Z][A-Z0-9 ,;:'’&()/.\-]+$")
_CHAPTER_LINE = re.compile(r"^CHAPTER (\d+[A-Z]?) - ")


def _body_headings(lines: list[str]) -> list[tuple[int, str]]:
    """(line index, section number) of every section heading of the chapter body. The contents list every
    section in the same form, so the body begins at the second time the first heading is printed."""
    chapter = next((m.group(1) for l in lines[:6] if (m := _CHAPTER_LINE.match(l))), None)
    if chapter is None:
        raise ValueError("the page does not print `CHAPTER n - ` at its head: it is not an NRS chapter page")
    heads = [(i, f"{m.group(1)}.{m.group(2)}") for i, l in enumerate(lines)
             if (m := _HEADING.match(l)) and m.group(1) == chapter]
    if not heads:
        raise ValueError(f"the page prints no section heading of chapter {chapter}")
    again = [k for k, (_, num) in enumerate(heads) if num == heads[0][1]]
    if len(again) < 2:
        raise ValueError("the page's table of contents and body are not both there: the layout changed")
    return heads[again[1]:]


def slice_section(text: str, start: str, end_before: str) -> str:
    lines = text.splitlines()
    heads = _body_headings(lines)
    first = [i for i, num in heads if num == start]
    if len(first) != 1:
        raise ValueError(f"section {start} is printed {len(first)} times as a heading in the chapter body "
                         f"(the layout changed, the section was repealed or renumbered, or the slice is wrong)")
    stop = next((i for i, num in heads if num == end_before and i > first[0]), None)
    if stop is None:
        raise ValueError(f"heading {end_before} does not follow section {start} in the chapter body: "
                         f"the slice would be a guess")
    cut = lines[first[0]:stop]
    while cut and (not cut[-1].strip() or _GROUP_HEADING.match(cut[-1])):
        cut.pop()
    return "\n".join(cut) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type in ("statute", "rule"):
        text = lcb_html_to_text(raw)
        if slice_ and doc_type == "statute":
            return slice_section(text, slice_["section_start"], slice_["section_end_before"])
        return text
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
    if src["doc_type"] == "statute" and src.get("slice"):
        return _slice_identity(src, text, what_is)
    m = _CHAPTER.search(src["citation"])
    head = text.splitlines()[:3]
    if not m or not any(re.match(rf"CHAPTER {re.escape(m.group(2))} - ", l) for l in head):
        raise ValueError(f"{src['id']}: page is not {src['citation']} (title/chapter mismatch)")
    if src["doc_type"] == "rule" and src["title"] not in text:
        raise ValueError(f"{src['id']}: page does not carry the seed title {src['title']!r}")
    return True


def _slice_identity(src, text, what_is):
    """A section slice is the cited one when its first line is the heading of the first cited section, its
    last heading is the last cited section, no heading is a repeal notice or an `[Effective ...]` version
    marker (the page prints a section in two versions, with the date each takes effect, as two headings)."""
    cite = _SECTION_CITE.fullmatch(src["citation"])
    sl = src["slice"]
    lines = [l for l in text.splitlines() if l.strip()]
    heads = [(l, f"{m.group(1)}.{m.group(2)}") for l in lines if (m := _HEADING.match(l))]
    first = cite.group(1) if cite else None
    last = (cite.group(2) or cite.group(1)) if cite else None
    if (not cite or not heads or sl.get("section_start") != first or heads[0] != (lines[0], first)
            or heads[-1][1] != last):
        raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: the slice opens on "
                         f"{heads[0][1] if heads else None!r} and its last heading is "
                         f"{heads[-1][1] if heads else None!r}")
    for line, num in heads:
        if re.search(r"\bRepealed\b", line) or _EFFECTIVE_MARK.search(line):
            raise ValueError(f"{src['id']}: section {num} is printed as repealed or in an `[Effective ...]` "
                             f"version: not shown to be the law in force ({line[:80]!r})")
    return True


def _slice_notes(src):
    sl = src["slice"]
    chapter = src["citation"].split()[1].split(".")[0]
    return (f"HTML paragraphs unwrapped to one line per source paragraph; markup, spacing paragraphs and "
            f"non-breaking spaces removed, and the Wingdings 3 continuation glyph the Legislative Counsel Bureau "
            f"prints after a list dropped. The source serves the whole NRS chapter {chapter} as one page (the page "
            f"is the snapshot); this document is the one provision cut from it: from the heading of section "
            f"{sl['section_start']} to the line before the heading of section {sl['section_end_before']}, with the "
            f"section's text and the history line under it. The page's revision stamp, the chapter's table of "
            f"contents, the group heading and the other sections of the chapter are not in it.")


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and src.get("slice"):
        return _slice_notes(src)
    if src["doc_type"] in ("statute", "rule"):
        kind = "NRS" if src["doc_type"] == "statute" else "NAC"
        return (f"HTML paragraphs unwrapped to one line per source paragraph; markup, spacing paragraphs and "
                f"non-breaking spaces removed, and the Wingdings 3 continuation glyph the Legislative Counsel Bureau "
                f"prints after a list (read as the letter E-circumflex) dropped. The source serves the whole {kind} "
                f"chapter as one page, so this document is the whole chapter: its revision stamp, its table of "
                f"contents, every section and the history line under each.")
    return None


def extra_notes(src, fmt, text, eff, version):
    note = (src.get("currency_note") or "").strip()
    if note:
        return f" {note}"
    if src.get("scan_layer"):
        return (" The PDF is a scan of a signed paper original; the text read here is the text layer the publisher "
                "embedded when it scanned the page (Adobe Paper Capture or a copier's recognition), a machine "
                "reading that can carry recognition errors in words and figures (a letterhead may read "
                "'Informatio11', the letters AI may read 'Al'). It is committed as served and is not human-verified: "
                "check any word or number against the PDF before relying on it.")
    return ""
