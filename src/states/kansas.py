"""Kansas: the Revisor of Statutes' section pages (www.ksrevisor.gov/statutes/chapters/chNN/NNN_NNN_NNNN.html).
Hooks are described in src/states/__init__.py.

The Revisor serves one statute section per static page, inside `<div id="print">`: a paragraph holding the section
number and caption in spans followed by the first paragraph of text, one `<p class="ksa_stat">` per further paragraph,
a `<p class="ksa_stat_hist">` history line, then (outside the print division but before the Previous/Next links) the
Revisor's Notes and "Cross References to Related Sections" paragraphs. Everything the page prints in that region is
kept: the notes tell a reader that a later amendment exists. The navigation, the print link and the right-hand
column (Legislative Coordinating Council notices) are not part of the section and are dropped.

The Secretary of State's session-law pages (sos.ks.gov/publications/sessionlaws/YYYY/Chapter-NN-BB-NNNN.html) serve
an Act whole: each section is a paragraph of class `session-laws-bill-section` ("Sec. 4. K.S.A. 2025 Supp. 75-413 is
hereby amended to read as follows: 75-413. ..."), new text in <em> and struck text in <s>. Where the Revisor's section page
has not yet caught up with a session, the in-force section is cut from the Act: struck text dropped, new text kept.

The Administrative Regulations (rules.ks.gov) are a script-rendered application with no static text, and the executive
policy library (ebit.ks.gov) refuses the toolkit Fetcher: see the seed list."""
from __future__ import annotations

import html as html_mod
import re

from src.ingest_common import _clean_line

_START = re.compile(r'<div[^>]*\bid="print"[^>]*>', re.I)
_END = re.compile(r'<a[^>]*\bid="prev2"', re.I)
_PARA = re.compile(r"<p\b[^>]*>(.*?)</p>", re.S | re.I)
_NUMBER = re.compile(r"^(\d+[a-z]?-\d+[a-z]?\d*[a-z]?(?:,\d+[a-z]?)?)\.\s")
_CITE_NUMBER = re.compile(r"K\.S\.A\.\s+(\S+)$")


def section_html_to_text(raw: bytes) -> str:
    """One section page to text: one line per source paragraph, tags and link markup removed, runs of spaces
    squeezed to one. The section number, its caption and the first paragraph share a line, as the page prints them."""
    page = raw.decode("utf-8", errors="replace").lstrip("﻿")
    start = _START.search(page)
    if not start:
        raise ValueError("no statute text: the page has no print division (the layout changed, or this is not a section page)")
    end = _END.search(page, start.end())
    region = page[start.end():end.start() if end else len(page)]
    out: list[str] = []
    for p in _PARA.findall(region):
        line = _clean_line(re.sub(r"<[^>]+>", " ", p))
        line = re.sub(r"\s+([.,;:)])", r"\1", line)            # a link's own spaces before punctuation
        line = re.sub(r"\(\s+", "(", line)
        if line:
            out.append(line)
    if not out or not _NUMBER.match(out[0]):
        raise ValueError("no statute text: the page does not open with a section number (the layout changed, "
                         "or this is not a section page)")
    return "\n".join(out) + "\n"


_SL_START = re.compile(r"^(New Section \d+|New Sec\. \d+|Sec\. \d+)\.\s*")
_SL_AMENDED = re.compile(r"^.*? is hereby amended to read as follows:\s*", re.S)
_P_ANY = re.compile(r"<p\b([^>]*)>(.*?)</p>", re.S | re.I)
_STRUCK = re.compile(r"<s>.*?</s>", re.S | re.I)
_APPROVED = re.compile(r"Approved ([A-Z][a-z]+ \d{1,2}, \d{4})\.")


def _squeeze(fragment: str) -> str:
    line = _clean_line(re.sub(r"<[^>]+>", " ", html_mod.unescape(fragment)))
    line = re.sub(r"\s+([.,;:)])", r"\1", line)
    return re.sub(r"\(\s+", "(", line)


def session_law_section_to_text(raw: bytes, section, number: str | None = None) -> str:
    """One section of an Act as the Secretary of State's page prints it, as text: struck text dropped, new text kept,
    one line per paragraph, then a bracketed line naming the session law and its approval date. `section` is the
    section number (4 for "Sec. 4.") or the page's own label for a new section ("New Section 1"). A new section carries
    no K.S.A. number in the Act (the Revisor assigns it): `number` is the one the 2026 Composite Listing gives."""
    page = raw.decode("utf-8", errors="replace").lstrip("﻿")
    label = f"Sec. {section}" if isinstance(section, int) else str(section)
    chapter = re.search(r'session-laws-bill-chapter">\s*CHAPTER (\d+)', page)
    heading = re.search(r'session-laws-bill-heading">(.*?)</p>', page, re.S)
    if not chapter or not heading:
        raise ValueError("no session law: the page has no chapter heading (the layout changed, or this is not a session-law page)")
    out: list[str] | None = None
    prev_struck_end = False          # the last paragraph read ended in struck text
    for attrs, inner in _P_ANY.findall(page):
        starts = "session-laws-bill-section" in attrs
        if starts:
            if out is not None:
                break
            m = _SL_START.match(_squeeze(re.sub(r"<[^>]+>", "", inner)))
            if not m or m.group(1) != label:
                continue
            out = []
        elif out is None:
            continue
        if inner.lower().count("<s>") != inner.lower().count("</s>"):
            raise ValueError("struck text runs across paragraphs (the layout changed)")
        line = _squeeze(_STRUCK.sub("", inner))
        struck_start = inner.lstrip().lower().startswith("<s>")
        joined = (not starts and out and prev_struck_end and struck_start and line
                  and not re.match(r"\(\w+\)\s", line))
        prev_struck_end = inner.rstrip().lower().endswith("</s>") or (prev_struck_end and not line)
        if joined:                   # a struck run took the paragraph break with it: the sentence goes on
            out[-1] = _squeeze(out[-1] + " " + line)
            continue
        if starts:
            line = _SL_START.sub("", line)
            if label.startswith("Sec"):
                if not _SL_AMENDED.match(line):
                    raise ValueError(f"{label}: not an amendment ('is hereby amended to read as follows' not found)")
                line = _SL_AMENDED.sub("", line)
            elif number:
                line = f"{number}. {line}"
        if line:
            out.append(line)
    if not out:
        raise ValueError(f"section {section} is not on the page")
    approved = _APPROVED.search(re.sub(r"<[^>]+>", " ", page))
    name = _squeeze(heading.group(1))
    out.append(f"[2026 Session Laws of Kansas, chapter {chapter.group(1)}, {name}, "
               f"{label.lower().replace('sec.', 'section')}."
               + (f" Approved {approved.group(1)}.]" if approved else "]"))
    return "\n".join(out) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute" and slice_ and "article" in slice_:
        sec = slice_["article"]
        return session_law_section_to_text(raw, int(sec) if sec.isdigit() else sec, slice_.get("part"))
    if fmt == "html" and doc_type == "statute":
        return section_html_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "kansas" or src["doc_type"] != "statute":
        return False
    m = _CITE_NUMBER.search(src["citation"])
    first = _NUMBER.match(text.splitlines()[0]) if text else None
    if not m or not first or first.group(1) != m.group(1):
        raise ValueError(f"{src['id']}: page is not {src['citation']} (section number mismatch)")
    return True


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and src["jurisdiction"] == "kansas":
        extra = ("\n\n" + src["curator_note"].strip()) if src.get("curator_note") else ""
        if src.get("slice") and src["slice"].get("part"):
            return ("Text cut from the Secretary of State's page for the 2026 session law named in the last line: a new "
                    "section that the Revisor of Statutes has not yet published, listed in the 2026 Composite Listing of New, "
                    "Amended and Repealed Statutes (K.S.A. Order, August 13, 2026) with effective date 7/1/2026. The Act "
                    "prints no K.S.A. number and no caption: the number is the Composite Listing's and the title is the Act's "
                    "own words. The section's paragraphs, one line per paragraph; the Act's 'New Section' label removed." + extra)
        if src.get("slice"):
            return ("Text cut from the Secretary of State's page for the 2026 session law named in the last line, because the "
                    "Revisor of Statutes' section page still printed the earlier text: the 2026 Composite Listing of New, Amended "
                    "and Repealed Statutes (K.S.A. Order, August 13, 2026) lists this section with effective date 7/1/2026. The "
                    "section's own paragraphs, one line per paragraph; struck text dropped, new text kept; the Act's section "
                    "heading ('is hereby amended to read as follows') removed. The Act prints no caption: the title is the "
                    "Revisor's caption for the section." + extra)
        return ("Text taken from the Revisor of Statutes' static section page (one section per page): the section number "
                "and caption with its first paragraph, each further paragraph, the history line, and any Revisor's Note "
                "and cross-reference lines the page prints, one line per paragraph. Links, the page's navigation, print "
                "link and right-hand column removed." + extra)
    return None
