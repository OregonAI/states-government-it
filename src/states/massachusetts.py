"""Massachusetts: the General Laws on malegislature.gov (served one section per page, bundled here one chapter at a
time), the executive order, directive and policy pages on mass.gov, and the identity and dates its documents print.
Everything else Massachusetts holds is PDF, which the shared reader handles. Hooks are described in
src/states/__init__.py."""
from __future__ import annotations

import re

from src.ingest_common import _clean_line, _decode, _squash
from src.states import UNHANDLED

# ---- General Laws: one chapter = its table-of-contents page + every section page -------------------------------

_MARK = b"<!-- MA-PAGE "
_SECTION_LINK = re.compile(r'href="(/Laws/GeneralLaws/[^"]*?/Chapter\w+/Section\w+)"')
_HEADING = re.compile(r'<h2 id="skipTo" class="h3 genLawHeading[^"]*">(.*?)</h2>', re.S)
_BLOCK = re.compile(r"</?(?:div|p|h[1-6]|li|ul|ol|tr|table|section|article|br|dt|dd|dl)\b[^>]*>", re.I)


def chapter_bundle(fetcher, url: str) -> bytes:
    """The chapter's table-of-contents page, then each section page it links, in its order, each preceded by a
    marker line naming its url."""
    base = re.match(r"https?://[^/]+", url).group(0)
    toc = fetcher.get(url).body
    links = list(dict.fromkeys(_SECTION_LINK.findall(_decode(toc))))
    if not links:
        raise ValueError(f"{url}: the chapter page links no sections: the layout changed")
    out = [_MARK + url.encode() + b" -->\n" + toc]
    for path in links:
        u = base + path
        out.append(_MARK + u.encode() + b" -->\n" + fetcher.get(u).body)
    return b"\n".join(out)


def _pages(raw: bytes) -> list[tuple[str, str]]:
    parts = raw.split(_MARK)[1:]
    if not parts:
        raise ValueError("not a chapter bundle: no page markers")
    return [(p.split(b" -->\n", 1)[0].decode(), _decode(p.split(b" -->\n", 1)[1])) for p in parts]


def _lines(fragment: str) -> list[str]:
    fragment = re.sub(r"<!--.*?-->", "", fragment, flags=re.S)
    fragment = re.sub(r"<(script|style|svg|noscript)\b.*?</\1>", "", fragment, flags=re.S | re.I)
    fragment = _BLOCK.sub("\n", fragment)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    return [c for c in (_clean_line(l) for l in fragment.split("\n")) if c]


def _heading(page: str) -> tuple[str, str, int]:
    """(`Chapter 7D` or `Section 2`, caption, offset just after the heading)."""
    m = _HEADING.search(page)
    if not m:
        raise ValueError("no section heading (genLawHeading) on a General Laws page: the layout changed")
    label, _, cap = m.group(1).partition("<small>")
    return _clean_line(re.sub(r"<[^>]+>", "", label)).rstrip(":"), _clean_line(re.sub(r"<[^>]+>", "", cap)), m.end()


_VERSION_NOTE = re.compile(r"\[Text of section\b.*\beffective\b", re.I)


def statute_bundle_to_text(raw: bytes) -> str:
    """`Chapter 7D CAPTION`, then each section: a blank line, `Section n: caption`, and the section's paragraphs, one
    line each. The page's menus, search form, buttons and footer are not the law."""
    pages = _pages(raw)
    label, cap, _ = _heading(pages[0][1])
    out = [f"{label} {cap}"]
    for _url, page in pages[1:]:
        label, cap, end = _heading(page)
        stop = page.find('<script src="/bundles/enhancedInteractions', end)
        body = _lines(page[end:stop if stop > 0 else len(page)])
        if re.match(r"repealed\b", cap, re.I):      # the site prints a repeal in the heading caption and leaves the body empty
            raise ValueError(f"{label}: the section is repealed ({cap})")
        if body and _VERSION_NOTE.match(body[0]):
            raise ValueError(f"{label}: the page announces a version with its own effective date ({body[0][:120]}): "
                             "not yet in force, or two versions; review by hand")
        if not body:
            raise ValueError(f"{label}: no law text on the page: the layout changed")
        out += ["", f"{label}: {cap}"] + body
    return "\n".join(out) + "\n"


_SECTION_URL = re.compile(r"^(https?://.+/Chapter\w+)/Section(\w+)$")


def section_bundle(fetcher, url: str) -> bytes:
    """One section of a chapter: the chapter's table-of-contents page (it gives the chapter heading, and a section the
    chapter does not link is refused) and then the section's own page, each preceded by its marker line."""
    chapter, number = _SECTION_URL.match(url).groups()
    toc = fetcher.get(chapter).body
    if not any(l.endswith(f"/Section{number}") for l in _SECTION_LINK.findall(_decode(toc))):
        raise ValueError(f"{url}: the chapter page does not link Section {number}: renumbered or repealed")
    return _MARK + chapter.encode() + b" -->\n" + toc + b"\n" + _MARK + url.encode() + b" -->\n" + fetcher.get(url).body


def snapshot(src, fetcher, dest, refetch):
    if src["doc_type"] != "statute":
        return None
    if dest.is_file() and not refetch:
        return dest.read_bytes(), False
    raw = section_bundle(fetcher, src["url"]) if _SECTION_URL.match(src["url"]) else chapter_bundle(fetcher, src["url"])
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    return raw, True


# ---- mass.gov pages: orders, directives, policy advisories -----------------------------------------------------

_CHROME = {"Skip table of contents", "Table of Contents", "table of contents", "+", "Hide Table of contents", "×",
           "Show More", "Table of contents", "top", "You skipped the table of contents section.",
           "table of contents+", "Table of Contents Hide Table of contents×", "Show More Table of contents",
           "show moreshow less", "Table of Contents ×"}
_END = ('<section class="ma__contact-list', '<aside class="sidebar"', '<div class="post-content"', '<div class="ma__contact-us', "ma__mass-feedback-form",
        "<footer", "ma__footer-new", '<div class="ma__page-flipper', '<div class="ma__header-tags"')
_DOWNLOADS = re.compile(r'<section class="ma__form-downloads">.*?</section>', re.S)
_HIDDEN = re.compile(r'<span class="ma__visually-hidden">.*?</span>', re.S)
# Cells of a table the page printed on one line (a version table) are joined with " | ", as the Word reader does;
# a table with its cells on separate source lines (the header's Date and Issuer) keeps one cell per line.
_CELLS = re.compile(r"(</t[dh]>)(?=<t[dh]\b)", re.I)


def massgov_page_to_text(raw: bytes) -> str:
    """A mass.gov page that is itself the instrument: from the page header (its category, title, and the Date, Issuer,
    Organization, Referenced Sources, Mass Register and Rescinded-by lines it prints) to the end of the content
    column, one line per block. The handbook menu, the table-of-contents widget, the contact column, the feedback
    form and the footer are not read."""
    page = _decode(raw)
    start = page.find('<section class="ma__page-header')
    if start < 0:
        raise ValueError("mass.gov page has no page header: the layout changed")
    ends = [i for i in (page.find(m, start) for m in _END) if i > 0]
    if not ends:
        raise ValueError("mass.gov page has no end of content: the layout changed")
    body = _CELLS.sub(r"\1 | ", _HIDDEN.sub("", _DOWNLOADS.sub("", page[start:min(ends)])))
    out = [l for l in _lines(body) if l not in _CHROME]
    if len(out) < 8:
        raise ValueError("mass.gov page has no content: the layout changed")
    return "\n".join(out) + "\n"


# ---- hooks (see src/states/__init__.py) ------------------------------------------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt != "html":
        return None
    if doc_type == "statute":
        return statute_bundle_to_text(raw)
    if doc_type in ("executive_order", "policy", "standard"):
        return massgov_page_to_text(raw)
    return None


_RULE_NO = re.compile(r"\d+ CMR \d+\.\d+")
_EO_NO = re.compile(r"Executive Order No\. (\d+)")
_EO_TITLE = re.compile(r"^No\. (\d+):", re.M)


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "massachusetts":
        return False
    cite = src["citation"]
    if src["doc_type"] == "statute":
        chapter = re.search(r"c\.\s*(\w+)", cite)
        if not chapter or not text.startswith(f"Chapter {chapter.group(1)} "):
            raise ValueError(f"{src['id']}: page is not {cite} (chapter mismatch)")
        wanted = re.search(r"§\s*(\w+)", cite)
        if wanted:      # a one-section entry: the text must hold that section and no other
            found = re.findall(r"^Section (\w+): ", text, re.M)
            if found != [wanted.group(1)]:
                raise ValueError(f"{src['id']}: text is not {cite} (section mismatch: it holds sections {found})")
        return True
    if src["doc_type"] == "rule":
        number = _RULE_NO.search(cite)
        if not number or _squash(number.group(0)) not in _squash(text):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: "
                             f"{number and number.group(0)} does not appear in its text")
        return True
    if src["doc_type"] == "executive_order":
        number = _EO_NO.search(cite)
        title = _EO_TITLE.search(text)      # the order's own title line, `No. 614: ...`; a number the body mentions is not it
        if not number or not title or title.group(1) != number.group(1):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {number and number.group(0)} is not "
                             f"the order's own title line (the page's is {title and 'No. ' + title.group(1)})")
        return True
    return False


_MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December")
_ORDINAL_DATE = re.compile(rf"Effective Date:\s*({'|'.join(_MONTHS)})\s+(\d{{1,2}})(?:st|nd|rd|th),(?:\s+|[ \t]*\n[^\n]*?[ \t]{{2,}})(\d{{4}})\b")


def effective_date(text, doc_type):
    """EOTSS standards print "Effective Date: October 15th, 2018"; the shared reader does not take an ordinal day
    suffix, and one (IS.024) wraps so that the year starts the next line in the same column. Only those forms, directly after the label, are read here; the rest is left to the shared reader."""
    m = _ORDINAL_DATE.search(text)
    if not m:
        return UNHANDLED
    mon, d, y = _MONTHS.index(m.group(1)) + 1, int(m.group(2)), int(m.group(3))
    return f"{y:04d}-{mon:02d}-{d:02d}" if 1 <= d <= 31 else UNHANDLED


def notes(src, fmt, text):
    if src["jurisdiction"] != "massachusetts" or fmt != "html":
        return None
    if src["doc_type"] == "statute":
        tail = (" as `Section n: caption` and the section's paragraphs, one line each. Menus, search form, buttons and "
                "footer removed. The site says its General Laws are an unofficial version; the printed Official Edition "
                "governs.")
        if _SECTION_URL.match(src["url"]):
            return ("Text taken from the General Laws pages on malegislature.gov, which the Legislature serves one section "
                    "per page: the chapter page's heading and the one cited section page (the chapter's table of contents "
                    "was checked to link it; the other sections are not part of this document)," + tail)
        return ("Text taken from the General Laws pages on malegislature.gov, which the Legislature serves one section "
                "per page: the chapter page's heading, then each section page the chapter's table of contents links, in "
                "its order," + tail)
    return ("Text taken from the mass.gov page: from the page header (category, title, and the date, issuer, organization, "
            "referenced-sources, Mass Register and rescission lines it prints) to the end of its content column, one line "
            "per block; the cells of a version table are joined with ' | '. The table-of-contents widget, the visually "
            "hidden category label, the downloads widget, the repeated referenced-sources block, the contact column, the "
            "feedback form and the footer removed.")
