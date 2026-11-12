"""West Virginia: the Legislature's section pages (`code.wvlegislature.gov/<section>/`), the Office of Technology's
policy PDFs and Google Docs (Google Drive downloads), and the Secretary of State's legislative rules (Word files, and
one scan read by OCR). Hooks are described in src/states/__init__.py.

The Code site serves one page per section and, for an article, only a contents list (its "Display all sections" link
loads the text by script, and is not used), so each statute entry is one section. A section page wraps the section in the
site's menus, a chapter selector, previous and next links and a bill-history widget; the law is one
`<div class='sectiontext'>`: an `<h4>` heading and one `<p>` per paragraph. The site does not mark a repealed section in
its contents list, only in the section's own text (`[Repealed]`), so a repealed section is refused here.

Google Drive's PDF downloads of the Office's newer policies put a zero-width space (U+200B) around every run of text.
The text is kept as extracted; only the identity and version checks look through them."""
from __future__ import annotations

import html as html_mod
import re

from src.ingest_common import _clean_line, _squash

_ZERO_WIDTH = dict.fromkeys(map(ord, "​‌‍﻿"))
_HYPHENS = dict.fromkeys(map(ord, "‐‑‒–"), "-")

_SECTIONTEXT = re.compile(r"<div class=['\"]sectiontext[^>]*>(.*?)</div>", re.S)
_BLOCKS = re.compile(r"<(h4|p)\b[^>]*>(.*?)</\1>", re.S)


def _plain(fragment: str) -> str:
    fragment = re.sub(r"<br\s*/?>", " ", fragment)
    return _clean_line(re.sub(r"<[^>]+>", "", fragment).translate(_ZERO_WIDTH))


def statute_section_to_text(raw: bytes) -> str:
    """One section page to text: the section's heading line, then one line per paragraph (a repealed section prints its notice in several headings). A repealed section, and a
    page that has no section text (an article's contents list, a layout change), are refused."""
    page = raw.decode("utf-8", errors="replace")
    m = _SECTIONTEXT.search(page)
    if not m:
        raise ValueError("no statute text: the page has no section text block (this is not a section page, "
                         "or the layout changed)")
    block = m.group(1)
    lines = [t for t in (_plain(b[1]) for b in _BLOCKS.findall(block)) if t]
    if not lines:
        raise ValueError("no statute text: the section text block is empty")
    if re.search(r"\[\s*Repealed", " ".join(lines)[:300], flags=re.I):
        raise ValueError(f"{lines[0][:40]!r} is repealed: only law in force is held")
    if len(lines) < 2:
        raise ValueError("no statute text: the section has a heading and no paragraphs")
    return "\n".join(lines) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute":
        return statute_section_to_text(raw)
    return None


def _refuse(src, what_is, what):
    raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {what} does not appear in its text")


_POLICY_ID = re.compile(r"[A-Z]+-[A-Z]*\d+(?:-\d+)*")
_CITED_SECTION = re.compile(r"§\s*(\S+)$")
_CITED_SERIES = re.compile(r"§\s*(163-\d+)$")


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "west-virginia":
        return False
    kind = src["doc_type"]
    if kind == "statute":
        m = _CITED_SECTION.search(src["citation"])
        first = text.split("\n", 1)[0]
        if not m or not first.startswith(f"§{m.group(1)}."):
            raise ValueError(f"{src['id']}: page is not {src['citation']} (the section heading line is "
                             f"{first[:60]!r})")
        return True
    plain = text.translate(_ZERO_WIDTH).translate(_HYPHENS)
    if kind == "rule":
        series = _CITED_SERIES.search(src["citation"])
        want = src.get("identity_text") or src["title"]
        # a scan's section marks are misread by OCR ('§ 161-3-1' for '§ 163-1-1'): its identity phrase is the check
        marked = bool(series) and (src.get("ocr") is True or re.search(rf"§\s*{re.escape(series.group(1))}-1\b", plain))
        if not marked or _squash(want) not in _squash(plain):
            _refuse(src, what_is, f"the section marker for {src['citation']} and {want!r}")
        return True
    if kind in ("policy", "standard"):
        if src.get("identity_text"):
            want = src["identity_text"]
            if _squash(want) not in _squash(plain):
                _refuse(src, what_is, repr(want))
            return True
        number = _POLICY_ID.search(src["citation"])
        if number:
            if not re.search(rf"(?<![\w-]){re.escape(number.group(0))}(?![\w])", plain):
                _refuse(src, what_is, number.group(0))
            return True
    return False


_REVISED = re.compile(r"Revised(?: Date)?:?\s+(\d{1,2}/\d{1,2}/\d{2,4})")
_ISSUED_ON = re.compile(r"Issued by the Chief Information Officer on\s+(\d{1,2}/\d{1,2}/\d{2,4})")
# the State Privacy Office's header line: 'Issue Date: 1.30.09 Effective Date: 8.1.09 Rev. Date: 4.1.12' (the revision field
# is sometimes printed empty); the Office's footer: 'Issue Date: 01/22/2026  Revised: New Policy'
_REV_DATE = re.compile(r"Rev\.?[ \t]*Date:?[ \t]*(\d{1,2}[./]\d{1,2}[./]\d{2,4})")
_ISSUE_DATE = re.compile(r"Issue Date:?[ \t]*(\d{1,2}[./]\d{1,2}[./]\d{2,4})")


def source_version(text, doc_type, fmt):
    if fmt != "pdf" or doc_type not in ("policy", "standard"):
        return None
    plain = text.translate(_ZERO_WIDTH)
    if m := _REVISED.search(plain):
        return f"Revised {m.group(1)}"
    if m := _REV_DATE.search(plain):
        return f"Revised {m.group(1)}"
    if m := _ISSUED_ON.search(plain):
        return f"Issued {m.group(1)}"
    if m := _ISSUE_DATE.search(plain):
        return f"Issued {m.group(1)}"
    return None


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and fmt == "html":
        return ("Text taken from the West Virginia Code page for the section (code.wvlegislature.gov): the section's "
                "heading, then each paragraph on its own line. The page's menus, chapter selector, Previous and Next "
                "links, bill-history list and footer were removed. The page prints no effective date.")
    return None


def extra_notes(src, fmt, text, eff, version):
    said = " source_version is the revision or issue date the policy prints, as printed." if version else ""
    if fmt == "pdf" and "​" in text:
        return (" Google Drive's PDF puts a zero-width space (U+200B) around runs of text; they are kept as "
                "extracted." + said)
    if fmt == "pdf":
        return said
    return ""
