"""Washington: RCW pages. Hooks are described in src/states/__init__.py."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line, _decode


def rcw_html_to_text(raw: bytes) -> str:
    """The Legislature's RCW page (app.leg.wa.gov), either a whole chapter (`&full=true`) or one
    section. Only the title block and the section content are the law: the site menu, the
    chapter's section list, the PDF buttons and the footer are not. Output: the citation and
    title, then for each section its `RCW x.y.z` line, caption, one line per paragraph, the
    session-law history line and any NOTES, with a blank line before each section. Nothing
    inside a section is dropped."""
    page = _decode(raw)
    block = re.search(r'id="ContentPlaceHolder1_pnlTitleBlock"(.*?)</div>\s*</div>|id="ContentPlaceHolder1_pnlTitleBlock"(.*?)</h2>',
                      page, flags=re.S)
    heads = re.findall(r"<h[12][^>]*>(.*?)</h[12]>", (block.group(0) if block else ""), flags=re.S)
    body_start = page.find('id="ContentPlaceHolder1_dlSectionContent"')
    if body_start < 0:                                  # a one-section page
        body_start = page.find("id='contentWrapper'")
    if not heads or body_start < 0:
        raise ValueError("RCW page has no content region: the page layout changed")
    end = page.find('id="ContentPlaceHolder1_pnlExpanded"', body_start)
    end = page.rfind("<", 0, end) if end >= 0 else end
    chapter = 'id="ContentPlaceHolder1_dlSectionContent"' in page[body_start:body_start + 60]
    if not chapter and end < 0:
        end = len(page)
    start = page.index(">", body_start) + 1               # after the opening tag
    region = page[start:] if chapter else page[start:end]
    if chapter:
        foot = region.find('<div class="block-dark-green">')       # the Legislature's page footer
        region = region[:foot] if foot >= 0 else region
        region = re.sub(r"<span>\s*<br>\s*<hr>", "\n\x00", region)
    head = [_clean_line(re.sub(r"<!--.*?-->|<[^>]+>", "", g)) for g in heads]
    region = re.sub(r"<!--.*?-->", "", region, flags=re.S)
    region = re.sub(r"<a class=\"btn[^>]*>.*?</a>", "", region, flags=re.S)       # PDF buttons
    region = re.sub(r"<(/?)(div|h[1-6]|p|tr)\b[^>]*>|<br\s*/?>|<hr\s*/?>", "\n", region, flags=re.I)
    region = re.sub(r"<[^>]+>", "", region)
    out = [line for line in head if line]
    for raw_line in region.split("\n"):
        marked = raw_line.startswith("\x00")
        line = _clean_line(raw_line.replace("\x00", ""))
        if marked and out:
            out.append("")
        if line:
            out.append(line)
    return "\n".join(out) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute":
        return rcw_html_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if src["doc_type"] == "statute" and src["jurisdiction"] == "washington":
        cite = src["citation"].replace("RCW chapter ", "Chapter ", 1)
        want = f"{cite} RCW" if cite.startswith("Chapter ") else cite
        if not text.strip() or text.splitlines()[0] != want:
            raise ValueError(f"{src['id']}: page is not {src['citation']} (title/chapter mismatch)")
        return True
    return False


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and src["jurisdiction"] == "washington":
        return ("Text taken from the Legislature's RCW page: the citation and title, then each "
                "section's caption, paragraphs, session-law history and notes, one line per "
                "paragraph. Site menu, PDF buttons, the page's section list and footer removed.")
    return None
