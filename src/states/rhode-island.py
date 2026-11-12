"""Rhode Island: the General Laws on webserver.rilegislature.gov (one page per section; a chapter is bundled here from
its index page and its section pages, a single section is one page), the Governor's executive order PDF, and the dates
the Division of Enterprise Technology Strategy and Services (ETSS) policies print. The policy library is PDF, which
the shared reader handles. Hooks are described in src/states/__init__.py."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line, _decode, _squash
from src.states import UNHANDLED

# ---- General Laws -------------------------------------------------------------------------------------------------

_MARK = b"<!-- RI-PAGE "
_SECTION_LINK = re.compile(r'href="([^"/]+\.htm)"', re.I)
_BLOCK = re.compile(r"</?(?:div|p|h[1-6]|li|ul|ol|tr|table|center|br)\b[^>]*>", re.I)
_BODY = re.compile(r"<body[^>]*>(.*)</body>", re.S | re.I)


def _is_chapter(src: dict) -> bool:
    return src["doc_type"] == "statute" and src["url"].lower().endswith("/index.htm")


def chapter_bundle(fetcher, url: str) -> bytes:
    """The chapter's index page, then each section page it links, in its order, each preceded by a marker line
    naming its url."""
    base = url.rsplit("/", 1)[0]
    index = fetcher.get(url).body
    links = list(dict.fromkeys(l for l in _SECTION_LINK.findall(_decode(index)) if l.lower() != "index.htm"))
    if not links:
        raise ValueError(f"{url}: the chapter index links no sections: the layout changed")
    out = [_MARK + url.encode() + b" -->\n" + index]
    for name in links:
        u = f"{base}/{name}"
        out.append(_MARK + u.encode() + b" -->\n" + fetcher.get(u).body)
    return b"\n".join(out)


def snapshot(src, fetcher, dest, refetch):
    if not _is_chapter(src):
        return None
    if dest.is_file() and not refetch:
        return dest.read_bytes(), False
    raw = chapter_bundle(fetcher, src["url"])
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    return raw, True


def _lines(fragment: str) -> list[str]:
    fragment = re.sub(r"<!--.*?-->", "", fragment, flags=re.S)
    fragment = re.sub(r"<(script|style)\b.*?</\1>", "", fragment, flags=re.S | re.I)
    fragment = re.sub(r"\s+", " ", fragment)          # a source paragraph is wrapped across several lines
    # a heading's <br> only separates its number from its name (`Chapter 11<br>Department of Administration`)
    fragment = re.sub(r"<h([12])\b.*?</h\1>", lambda m: re.sub(r"<br\s*/?>", " ", m.group(0), flags=re.I),
                      fragment, flags=re.S | re.I)
    fragment = _BLOCK.sub("\n", fragment)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    return [c for c in (_clean_line(l) for l in fragment.split("\n")) if c]


def _body(page: str) -> str:
    m = _BODY.search(page)
    if not m:
        raise ValueError("a General Laws page has no body: the layout changed")
    return m.group(1)


def _section_lines(page: str, with_head: bool) -> list[str]:
    """A section page: `Title n Name`, `Chapter n Name`, `R.I. Gen. Laws § n` (kept when the page is the document),
    then the section's paragraphs, one line each, ending with its History of Section."""
    lines = _lines(_body(page))
    at = next((i for i, l in enumerate(lines) if l.startswith("§ ")), None)
    if at is None or not any(l.startswith("R.I. Gen. Laws §") for l in lines[:at]):
        raise ValueError("a General Laws section page has no section heading: the layout changed")
    return lines if with_head else lines[at:]


def statute_to_text(raw: bytes) -> str:
    if raw.startswith(_MARK):
        parts = raw.split(_MARK)[1:]
        pages = [_decode(p.split(b" -->\n", 1)[1]) for p in parts]
        head = _lines(_body(pages[0]))
        if not head or not head[0].startswith("Chapter "):
            raise ValueError("a General Laws chapter index has no chapter heading: the layout changed")
        out = [head[0]]
        for page in pages[1:]:
            out += [""] + _section_lines(page, False)
        return "\n".join(out) + "\n"
    return "\n".join(_section_lines(_decode(raw), True)) + "\n"


def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute":
        return statute_to_text(raw)
    return None


# ---- identity ------------------------------------------------------------------------------------------------------

_EO_NO = re.compile(r"\d{2}-\d{2}")


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "rhode-island":
        return False
    cite = src["citation"]
    if src["doc_type"] == "statute":
        if "ch. " in cite:
            number = cite.split("ch. ", 1)[1].strip()
            ok = text.startswith(f"Chapter {number.rsplit('-', 1)[-1]} ") and f"§ {number}-" in text
        else:
            ok = bool(re.search(rf"^R\.I\. Gen\. Laws {re.escape(cite.split('Laws ', 1)[-1])}$", text, re.M))
        if not ok:
            raise ValueError(f"{src['id']}: {what_is} is not {cite} (chapter or section mismatch)")
        return True
    if src["doc_type"] == "executive_order":
        number = _EO_NO.search(cite)
        # the order's own heading is the line `EXECUTIVE ORDER` followed by its number line; a number the body
        # mentions ("amends Executive Order 24-06") is not it
        heading = re.search(r"^\s*EXECUTIVE ORDER\s*\n\s*(\d{2}-\d{2})\s*$", text, re.M | re.I)
        if not number or not heading or heading.group(1) != number.group(0):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {number and number.group(0)} is not "
                             f"the number under the order's own heading (the file's is {heading and heading.group(1)})")
        return True
    return False


# ---- dates ---------------------------------------------------------------------------------------------------------

_MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December")
_DAY_FIRST = re.compile(rf"Effective Date:\s*(\d{{1,2}})\s+({'|'.join(_MONTHS)})\s+(\d{{4}})\b")
_VERSION = re.compile(r"^[ \t]*(?:Last Review|Last Revision Date|Last Revision|Date of Last Revision)\b[: ]\s*\S.*$", re.M)


def effective_date(text, doc_type):
    """ETSS policies print `Effective Date: 23 June 2026`, day first, which the shared reader does not take; a
    numeric date (`7/29/2026`) is left to it."""
    m = _DAY_FIRST.search(text)
    if not m:
        return UNHANDLED
    d, mon, y = int(m.group(1)), _MONTHS.index(m.group(2)) + 1, int(m.group(3))
    return f"{y:04d}-{mon:02d}-{d:02d}" if 1 <= d <= 31 else UNHANDLED


def source_version(text, doc_type, fmt):
    """The revision line a policy prints about itself, as printed: `Last Review: 22 June 2026`, `Last Revision Date:
    07/29/2026`, `Last Revision: 4/21/2025` or `Date of Last Revision 04/01/2016`."""
    m = _VERSION.search(text)
    if not m:
        return None
    return _clean_line(re.split(r"\s{3,}", m.group(0).strip())[0])


def notes(src, fmt, text):
    if src["jurisdiction"] != "rhode-island" or fmt != "html":
        return None
    if src["doc_type"] == "statute":
        return ("Text taken from the General Laws pages on webserver.rilegislature.gov, which the Legislature serves one "
                "section per page. A chapter is the chapter heading from its index page, then each section page the "
                "index links, in its order, one line per paragraph, ending with each section's History of Section. A "
                "single section keeps the page's title, chapter and citation lines. The link list, markup and "
                "non-breaking spaces removed.")
    return None
