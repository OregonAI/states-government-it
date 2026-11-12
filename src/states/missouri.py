"""Missouri: the Revisor of Statutes' one-section pages and the Secretary of State's executive-order text pages.
Hooks are described in src/states/__init__.py. Everything else Missouri seeds is a PDF, which the shared reader handles.

Statutes are served one section per page (`revisor.mo.gov/main/OneSection.aspx?section=<n>`): a header block with the
title line ("Title IV  EXECUTIVE BRANCH"), the chapter link and an `Effective - <date>` span, then the section as a
`<div class="norm">` of paragraphs (the bold lead-in carries the number and caption), a `foot` block holding the
session-law history after a soft-hyphen separator, and an `---- end of effective <date> ----` line. A section that does
not exist is answered with a page that begins "Chapter, Title, etc. that does NOT exist" and has no `norm` block.
Executive orders are served by the Secretary of State as a text page (`/library/reference/orders/<year>/eo<n>`): the
order is the content of `<div id="main">`, from an `<h1>EXECUTIVE ORDER nn-nn</h1>` (older pages break the heading after
"ORDER") to a link to the scan or the `.pdf version`, which is furniture. The page's lists are styled with `list-style-type`, which the shared block reader prints as a browser does."""
from __future__ import annotations

import re

from src.ingest_common import BlockParser, _clean_line, _squash

_TITLE = re.compile(r'<p[^>]*>\s*(Title\s+[IVXLC]+\s[^<]+?)\s*</p>', re.S)
_CHAPTER = re.compile(r'title="Return to section list for Chapter (\w+)"')
_EFFECTIVE = re.compile(r'<span id="effdt"[^>]*>(.*?)<span', re.S)
_END = re.compile(r'<p[^>]*>\s*(---- end of effective[^<]*----)\s*</p>', re.S)
_SECTION_LINE = re.compile(r"^(\d+\.\d+)\.\s")
_SEPARATOR = re.compile(r"^-{4,}$")


def _decode(raw: bytes) -> str:
    return raw.decode("utf-8", errors="replace").lstrip("﻿")


def _lines(region: str) -> list[str]:
    parser = BlockParser()
    parser.feed(region)
    parser._flush()
    out = []
    for line in parser.lines:
        line = re.sub(r"^ (?=\S)", "", line.replace("\xad", ""))     # soft hyphens; one space left after a <br>
        if line.strip() and not _SEPARATOR.match(line.strip()):
            out.append(line)
    return out


def statute_html_to_text(raw: bytes) -> str:
    """One section page to text: the title line, the chapter, the `Effective -` line, the section (one line per
    paragraph: number, caption and first paragraph, then each subsection, definition and list item), the
    session-law history and the `---- end of effective ----` line. Search form, menus, the page's version table,
    the notes and the footer are not the law and are not carried. The separator before the history, drawn as a
    row of hyphens between soft hyphens, is dropped."""
    page = _decode(raw)
    start = page.find('<div class="norm"')
    end = page.find("<hr>", start) if start >= 0 else -1
    title, chapter, eff = _TITLE.search(page), _CHAPTER.search(page), _EFFECTIVE.search(page)
    body = _lines(page[start:end]) if start >= 0 and end > start else []
    if not (title and chapter and body and _SECTION_LINE.match(body[0])):
        raise ValueError("no statute text: the page has no section (the layout changed, or the section does not "
                         "exist on the Revisor's site)")
    head = [_clean_line(title.group(1)), f"Chapter {chapter.group(1)}"]
    if eff:
        head.append(_clean_line(re.sub(r"<[^>]+>", "", eff.group(1))))
    tail = _END.search(page, end)
    return "\n".join(head + body + ([_clean_line(tail.group(1))] if tail else [])) + "\n"


def executive_order_html_to_text(raw: bytes) -> str:
    """One order page to text: the heading and every paragraph and list item of the order as the Secretary of State
    prints it, one line per paragraph, signature lines and attestation included. The link to the scan of the signed
    order, the site menus and the footer are not the order."""
    page = _decode(raw)
    start = page.find('<div id="main">')
    marks = [i for i in (page.find("Scan of", start), page.find(".pdf version", start)) if i > start] if start >= 0 else []
    end = page.rfind("<p>", start, min(marks)) if marks else -1
    lines = _lines(page[start:end]) if start >= 0 and end > start else []
    if len(lines) > 1 and lines[0] == "EXECUTIVE ORDER" and re.fullmatch(r"\d{2}-\d{2,3}", lines[1]):
        lines[:2] = [f"{lines[0]} {lines[1]}"]            # older pages break the heading after "ORDER"
    if not lines or not re.match(r"^EXECUTIVE ORDER \d{2}-\d{2,3}\b", lines[0]) or len(lines) < 3:
        raise ValueError("no executive order text: the page has no heading and paragraphs (the layout changed, or "
                         "this is not an order page)")
    return "\n".join(lines) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt != "html":
        return None
    if doc_type == "statute":
        return statute_html_to_text(raw)
    if doc_type == "executive_order":
        return executive_order_html_to_text(raw)
    return None


_SECTION_CITE = re.compile(r"Section (?P<n>\d+\.\d+), RSMo")
_ORDER_CITE = re.compile(r"Executive Order (?P<n>\d{2}-\d{2,3})$")


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "missouri":
        return False
    if src["doc_type"] == "statute":
        m = _SECTION_CITE.fullmatch(src["citation"])
        found = {x.group(1) for l in text.splitlines() if (x := _SECTION_LINE.match(l))}
        if not m or m.group("n") not in found:
            raise ValueError(f"{src['id']}: page is not {src['citation']} (section number mismatch)")
        return True
    if src["doc_type"] == "executive_order":
        m = _ORDER_CITE.fullmatch(src["citation"])
        heading = re.match(r"EXECUTIVE ORDER (\d{2}-\d{2,3})\b", text)
        if not m or not heading or heading.group(1) != m.group("n"):
            raise ValueError(f"{src['id']}: page is not '{src['citation']}': its heading is "
                             f"{heading.group(0) if heading else 'missing'!r}, not 'EXECUTIVE ORDER "
                             f"{m.group('n') if m else '?'}'")
        return True
    return False


def notes(src, fmt, text):
    if src["jurisdiction"] != "missouri":
        return None
    if src["doc_type"] == "statute":
        return ("Text taken from the Revisor of Statutes' page for the one section: the title and chapter lines, the "
                "`Effective -` line, the section as printed (number, caption, subsections and definitions, one line "
                "per paragraph), its session-law history and the closing `end of effective` line. The page's search "
                "form, menus, version table and footer removed; the soft-hyphen separator before the history "
                "dropped.")
    if src["doc_type"] == "executive_order":
        return ("Text taken from the Secretary of State's text page for the order: the heading, then each paragraph "
                "and list item as printed, with the signature and attestation lines. The link to the scan of the "
                "signed order, the site menus and the footer removed.")
    return None
