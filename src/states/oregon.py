"""Oregon: ORS and OAR pages, and the Governor's orders. Hooks are described in src/states/__init__.py."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line, _decode, _squash, paragraph_html_to_text


def oar_html_to_text(raw: bytes) -> str:
    """The Secretary of State's OAR division page. Only the `#content` region is text of the
    rules: the site navigation, footer and scripts around it are not. One line per block
    element or <br>; a blank line before each rule."""
    page = _decode(raw)
    start = page.find('id="content"')
    end = page.find("sos-footer-wrapper")
    if start < 0 or end < start:
        raise ValueError("OAR page has no #content region: the page layout changed")
    start = page.index(">", start) + 1               # after the opening tag
    end = page.rindex("<", 0, end)                   # before the footer's opening tag
    region = re.sub(r"<(script|style).*?</\1>", " ", page[start:end], flags=re.S | re.I)
    region = re.sub(r"<div class='rule_div'>", "\n\x00", region)
    region = re.sub(r"<br\s*/?>|</?(p|div|h[1-6])\b[^>]*>", "\n", region, flags=re.I)
    region = re.sub(r"<[^>]+>", "", region)
    out: list[str] = []
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
        return paragraph_html_to_text(raw)
    if fmt == "html" and doc_type == "rule":
        return oar_html_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if src["doc_type"] == "executive_order" and src["jurisdiction"] == "oregon":
        # the Governor's order prints its heading as the first line of its own, "EXECUTIVE ORDER NO. 23-26"
        # (a scan may read it with its spacing and punctuation slightly off); an order that cites it
        # further down is not it
        number = re.search(r"\d{2,4}-\d{2}", src["citation"])
        head = [_squash(l) for l in text.splitlines() if l.strip()][:8]
        if not number or not any(re.fullmatch(rf"executive order (?:no[.,]? ?)?{number.group(0)}", l) for l in head):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: "
                             f"{src['citation']!r} is not the order's heading line (its first lines)")
        return True
    return False


def notes(src, fmt, text):
    if src["doc_type"] == "statute":
        return ("HTML paragraphs unwrapped to one line per source paragraph; markup, spacing "
                "paragraphs and non-breaking spaces removed. The source serves the whole "
                "chapter as one page, so this document is the whole chapter.")
    if src["doc_type"] == "rule":
        return ("Rule text taken from the page's rule region; site navigation, footer and scripts "
                "removed. One line per source line; a blank line before each rule number.")
    return None
