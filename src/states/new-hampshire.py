"""New Hampshire: the General Court's RSA pages (`gc.nh.gov/rsa/html/<title>/<chapter>/<chapter>-mrg.htm`, the whole
chapter, or `<chapter>-<section>.htm`, one section). Hooks are described in src/states/__init__.py.

A page is plain HTML: a hidden metadata comment, a TITLE and chapter heading (`<h1>`, `<h2>`, each with a `<br>`),
then for each section a `<h3>` banner ("Section 21-R:4"), a bold heading line ("21-R:4 Duties of the Commissioner. &#150;"),
the text in `<codesect>` with a `<br>` before each paragraph, and a `<sourcenote>` ("Source. 2008, 335:1, eff. ...").
Subdivision headings ("Open Standards") are `<h2>` elements between sections. The pages are cp1252 (the dash is the
numeric reference &#150;, read as an en dash). The administrative-rule pages and the nh.gov sites (DoIT, the Governor,
the Secretary of State) are not read here: the latter refuse the Fetcher (see the seed list)."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line

_COMMENT = re.compile(r"<!--.*?-->", re.S)
_HEADING = re.compile(r"<h([12])[^>]*>(.*?)</h\1>", re.S | re.I)
_BANNER = re.compile(r"<center>\s*<h3>.*?</h3>\s*</center>", re.S | re.I)
_SECTION_LINE = re.compile(r"^(\d+(?:-[A-Z])?:\d+(?:-[a-z])?) ")
_CHAPTER_LINE = re.compile(r"^CHAPTER (\S+) ", re.I)


def statute_html_to_text(raw: bytes) -> str:
    """One RSA page (a chapter or a section) to text: heading lines, then each section's bold heading line (after a
    blank line), one line per paragraph, and its Source line."""
    page = raw.decode("cp1252", errors="replace")
    body = page[page.lower().find("<body"):]
    body = _COMMENT.sub("", body)
    body = _BANNER.sub("", body)
    # a heading's own <br> joins its two halves ("TITLE I<br>THE STATE ...")
    body = _HEADING.sub(lambda m: "\n" + re.sub(r"<br\s*/?>", " ", m.group(2), flags=re.I) + "\n", body)
    body = re.sub(r"(&nbsp;)+\s*<b>", "\n\x00<b>", body)         # a section's bold heading line starts after a blank line
    body = re.sub(r"<br\s*/?>|</?p>|</?codesect>|</?sourcenote>", "\n", body, flags=re.I)
    out: list[str] = []
    for chunk in body.split("\n"):
        marked = chunk.startswith("\x00")
        line = _clean_line(re.sub(r"<[^>]+>", "", chunk.replace("\x00", "")))
        if not line:
            continue
        if marked and out:
            out.append("")
        out.append(line)
    if not any(_SECTION_LINE.match(l) for l in out):
        raise ValueError("no statute text: no section heading line")
    return "\n".join(out) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute":
        return statute_html_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "new-hampshire" or src["doc_type"] != "statute":
        return False
    cite = src["citation"]
    lines = text.splitlines()
    sec = re.fullmatch(r"RSA (\d+(?:-[A-Z])?:\d+(?:-[a-z])?)", cite)
    if sec:
        if not any(l.startswith(f"{sec.group(1)} ") for l in lines):
            raise ValueError(f"{src['id']}: {what_is} is not {cite} (no section heading line)")
        return True
    ch = re.fullmatch(r"RSA Chapter (\d+(?:-[A-Z])?)", cite)
    got = {m.group(1) for l in lines[:6] if (m := _CHAPTER_LINE.match(l))}
    if not ch or ch.group(1) not in got:
        raise ValueError(f"{src['id']}: {what_is} is not {cite} (chapter heading mismatch)")
    return True


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and src["jurisdiction"] == "new-hampshire":
        return ("Text taken from the General Court's RSA page on gc.nh.gov: the title and chapter heading lines, then "
                "each section's number and catch line, one line per paragraph, and its Source line (the session-law "
                "history). The page's hidden metadata comment and its repeated section banners are removed; a "
                "subdivision heading is kept where the page prints it. A blank line precedes each section.")
    return None
