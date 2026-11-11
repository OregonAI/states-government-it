"""Colorado: the OLLS title files, OIT's web pages and instrument PDFs, and the Code of Colorado Regulations.
Hooks are described in src/states/__init__.py."""
from __future__ import annotations

import re
import urllib.parse

from src.ingest_common import _MONTHS, BlockParser, _decode, _squash, paragraph_html_to_text


# ---- Colorado Office of Information Technology: pages on oit.colorado.gov ---------------------
#
# oit.colorado.gov is a Drupal site behind colorado.gov's shared firewall, which answers the toolkit's
# crawler-form User-Agent (toolkit ADR-0019) and refused the earlier one. A page that states an instrument
# is its <h1> (in the header region) and the page body (`field--name-body`), up to the end of the content
# column; the breadcrumb and side navigation, which list the neighbouring pages, are not the page.

def oit_html_to_text(raw: bytes) -> str:
    page = _decode(raw)
    heading = re.search(r"<h1[^>]*>\s*(.*?)\s*</h1>", page, flags=re.S)
    region = page.find("region-content")           # an earlier field--name-body is the language selector
    start = page.find("field--name-body", region) if region >= 0 else -1
    start = page.rfind("<div", 0, start) if start >= 0 else -1
    end = page.find("</section>", start) if start >= 0 else -1
    if not heading or start < 0 or end < 0:
        raise ValueError("page has no heading and body region: the page layout changed")
    parser = BlockParser()
    parser.feed(f"<h1>{heading.group(1)}</h1>" + page[start:end])
    parser._flush()
    return "\n".join(parser.lines) + "\n"


_CRS_ARTICLE = re.compile(r"ARTICLE \d+(\.\d+)?")


_CRS_PART = re.compile(r"PART \d+(\.\d+)?")


def _only(lines: list[str], want: str, what: str) -> int:
    hits = [i for i, line in enumerate(lines) if line == want]
    if not hits:
        raise ValueError(f"CRS file has no {what}: the file layout changed or the slice is wrong")
    if len(hits) > 1:
        raise ValueError(f"CRS file has {what} more than once: the slice would be a guess")
    return hits[0]


def crs_html_to_text(raw: bytes, slice_: dict | None) -> str:
    """The Office of Legislative Legal Services' C.R.S. title file (Word-exported HTML, one file
    per title, so the same paragraph handling as the ORS page). A document is one slice of it:
    `{article: "73"}` runs from the line `ARTICLE 73` to the next `ARTICLE n` heading line (or to
    the title-level group heading printed before it, which belongs to neither article), and
    `{article: "33.5", part: "19"}` runs from the body line `PART 19` inside that article to the
    next `PART n` body line. (The article's caption list prints `PART 19 COLORADO CYBERSECURITY`
    on one line; only the body heading is a line of its own.) Nothing inside a slice is dropped:
    caption lists, section text, source notes, editor's notes and annotations all stay."""
    if not slice_ or not slice_.get("article"):
        raise ValueError("a Colorado statute entry needs a slice: {article: ...} or "
                         "{article: ..., part: ...}")
    all_lines = paragraph_html_to_text(raw).splitlines()
    lines = all_lines
    start = _only(lines, f"ARTICLE {slice_['article']}", f"article {slice_['article']}")
    end = next((i for i in range(start + 1, len(lines)) if _CRS_ARTICLE.fullmatch(lines[i])),
               len(lines))
    # The file prints a title-level group heading (LIBRARIES, STATE FUNDS, ...) between the last
    # article of one group and the next ARTICLE line, so a slice would take it as its own last
    # line. The contents list at the top of the file names every group heading (an all-caps
    # line followed by `Art. n` lines); an article ends before the first one of them.
    groups = {line for i, line in enumerate(all_lines[:-1])
              if line == line.upper() and line != line.lower()
              and all_lines[i + 1].startswith("Art. ")}
    lines = all_lines[start:end]
    cut = next((i for i, line in enumerate(lines) if i and line in groups), len(lines))
    lines = lines[:cut]
    if slice_.get("part"):
        start = _only(lines, f"PART {slice_['part']}", f"part {slice_['part']}")
        end = next((i for i in range(start + 1, len(lines)) if _CRS_PART.fullmatch(lines[i])),
                   len(lines))
        lines = lines[start:end]
    return "\n".join(lines) + "\n"


# Colorado. A Code of Colorado Regulations PDF ends with `Editor's Notes / History` lines such as `New rule eff.
# 04/14/2024.` and `Entire rule eff. 06/30/2025.`: the rule in force is the one the last `eff.` line dates
# (a `repealed eff.` line is a repeal, which `check_identity` refuses). An OIT policy PDF prints a
# `Effective Date: Nov. 30, 2018` label (month abbreviated, with a full stop) or, when it prints none, an
# `Updated: Feb 23, 2026` or `Published January 2020` line, which is a source_version (a month or a
# revision stamp, not an effective date).
_CO_EFF = re.compile(r"^(?!.*repealed).*\beff\.\s+(\d{2})/(\d{2})/(\d{4})", flags=re.M | re.I)


_CO_LABEL = re.compile(r"Effective\s+Date:\s*([A-Za-z]{3,9})\.?\s+(\d{1,2}),\s+(\d{4})")


_CO_STAMP = re.compile(rf"^\s*((?:Updated:\s*[A-Za-z]{{3,9}}\.?\s+\d{{1,2}},\s+\d{{4}})"
                       rf"|(?:Published\s+(?:{_MONTHS})\s+\d{{4}}))", flags=re.M)


_CO_HEAD = 2500   # OIT's instrument PDFs print their header table at the top


_CO_ROW_DATE = re.compile(r"^[ \t]*Effective Date[ \t]{2,}(\d{1,2})[/-](\d{1,2})[/-](\d{4})[ \t]*$", flags=re.M)


_CO_ROW_VERSION = re.compile(r"^[ \t]*Version[ \t]{2,}(\S.*?)[ \t]*$", flags=re.M)


_CO_ROW_UPDATED = re.compile(r"^[ \t]*Last Updated[ \t]{2,}(\d{1,2}[/-]\d{1,2}[/-]\d{4})[ \t]*$", flags=re.M)


def _co_effective_date(text: str, doc_type: str) -> str | None:
    if doc_type == "rule":
        history = text[text.rfind("History"):] if "History" in text else ""
        hits = _CO_EFF.findall(history)
        if not hits:
            return None
        mon, day, year = hits[-1]
        return f"{year}-{mon}-{day}" if 1 <= int(mon) <= 12 and 1 <= int(day) <= 31 else None
    row = _CO_ROW_DATE.search(text[:_CO_HEAD])
    if row:         # the header table of a TS-/CISP-/POL- PDF: 'Effective Date   11/19/2015' (or 07-01-2026)
        mon, day, year = row.groups()
        return f"{year}-{int(mon):02d}-{int(day):02d}" if 1 <= int(mon) <= 12 and 1 <= int(day) <= 31 else None
    m = _CO_LABEL.search(text)
    if not m:
        return None
    months = [x[:3].casefold() for x in _MONTHS.split("|")]
    if m.group(1)[:3].casefold() not in months or not 1 <= int(m.group(2)) <= 31:
        return None
    return f"{int(m.group(3)):04d}-{months.index(m.group(1)[:3].casefold()) + 1:02d}-{int(m.group(2)):02d}"


def _check_co_rule_identity(src: dict, text: str, what_is: str) -> None:
    """A Code of Colorado Regulations PDF prints the department, the agency, the rule's title and its
    number (`8 CCR 1501-9`) on its cover, before the first rule. The cover must carry the cited number
    on a line of its own and the seed title (whitespace and case do not matter: the cover wraps and
    capitalises it), and must not be a repeal notice: the Secretary of State keeps a repealed rule's
    number, with a one-page PDF whose cover says `REPEALED EFF.`, as its current version."""
    cover = [" ".join(l.split()) for l in text.splitlines() if l.strip()][:30]
    head = _squash(" ".join(cover))
    if (not re.fullmatch(r"\d+ CCR \d+-\d+", src["citation"]) or src["citation"] not in cover
            or _squash(src["title"]) not in head):
        raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {src['citation']!r} and "
                         f"{src['title']!r} are not both on the rule's cover")
    if re.search(r"repealed eff\.", head):
        raise ValueError(f"{src['id']}: {src['citation']} is repealed (its cover says so): not in force")


_OIT = re.compile(r"\bOIT\b|Office of Information Technology")


def _check_co_policy_identity(src: dict, text: str, what_is: str) -> None:
    """An OIT policy PDF prints its own title in its head (the first 1,500 characters), which a document
    that only cites the policy further down does not, and names OIT (or the Office of Information
    Technology) somewhere: the files are found through OIT's page, so the file must say whose it is."""
    phrase = src.get("identity_text") or src["title"]
    if _squash(phrase) not in _squash(text[:1500]):
        raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {phrase!r} "
                         f"is not in the first 1,500 characters of its text")
    if not _OIT.search(text):
        raise ValueError(f"{src['id']}: {what_is} never names OIT or the Office of Information Technology: "
                         f"not shown to be OIT's")
    if src.get("document_id"):
        # An OIT instrument PDF opens with a header table: Document ID, Title, Issuing Authority, Version.
        head = text[:_CO_HEAD]
        ident = re.search(r"^[ \t]*Document ID[ \t]+(\S+)[ \t]*$", head, flags=re.M)
        if not ident or ident.group(1) != src["document_id"]:
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: its header prints Document ID "
                             f"{ident.group(1) if ident else None!r}, the seed entry cites {src['document_id']!r}")
        issuer = re.search(r"^[ \t]*Issuing Authority[ \t]+(\S.*)$", head, flags=re.M)
        if not issuer or not _OIT.search(issuer.group(1)):
            raise ValueError(f"{src['id']}: {what_is} has no Issuing Authority line naming OIT in its header "
                             f"(it prints {issuer.group(1) if issuer else None!r})")
        ver = _CO_ROW_VERSION.search(head)
        if ver and re.search(r"draft", ver.group(1), flags=re.I):
            raise ValueError(f"{src['id']}: {what_is} prints its version as {ver.group(1)!r}: a Draft is not "
                             f"shown to be in force")
        # A header table that calls the file a draft on its Last Updated row says the same (TS-DBS-001).
        upd = re.search(r"^[ \t]*Last Updated[ \t]{2,}(\S.*?)[ \t]*$", head, flags=re.M)
        if upd and re.search(r"draft", upd.group(1), flags=re.I):
            raise ValueError(f"{src['id']}: {what_is} prints its Last Updated row as {upd.group(1)!r}: a Draft "
                             f"is not shown to be in force")


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type in ("policy", "standard") and host == "oit.colorado.gov":
        return oit_html_to_text(raw)
    if fmt == "html" and doc_type == "statute":
        return crs_html_to_text(raw, slice_)
    return None


def check_identity(src, text, what_is):
    if src["jurisdiction"] == "colorado" and src["doc_type"] == "rule":
        _check_co_rule_identity(src, text, what_is)
        return True
    if src["jurisdiction"] == "colorado" and src["doc_type"] in ("policy", "standard"):
        _check_co_policy_identity(src, text, what_is)
        return True
    if src["doc_type"] == "statute" and src["jurisdiction"] == "colorado":
        cite = re.fullmatch(r"C\.R\.S\. title \d+, article ([\d.]+)(?:, part (\d+))?", src["citation"])
        sl = src.get("slice") or {}
        lines = text.splitlines()
        heading = f"PART {sl['part']}" if sl.get("part") else f"ARTICLE {sl.get('article')}"
        if (not cite or cite.group(1) != sl.get("article") or cite.group(2) != sl.get("part")
                or not lines or lines[0] != heading):
            raise ValueError(f"{src['id']}: page is not {src['citation']} (article/part mismatch)")
        if len(lines) < 2 or lines[1].casefold() not in src["title"].casefold():
            raise ValueError(f"{src['id']}: slice title {lines[1] if len(lines) > 1 else ''!r} "
                             f"is not in the seed title {src['title']!r}")
        return True
    return False


def effective_date(text, doc_type):
    return _co_effective_date(text, doc_type)


def source_version(text, doc_type, fmt):
    if doc_type in ("policy", "standard"):
        m = _CO_STAMP.search(text)
        if m:
            return " ".join(m.group(1).split())
        head = text[:_CO_HEAD]
        ver, upd = _CO_ROW_VERSION.search(head), _CO_ROW_UPDATED.search(head)
        if ver:
            return ver.group(1) + (f", last updated {upd.group(1)}" if upd else "")
    return None


def notes(src, fmt, text):
    if fmt == "html" and src["jurisdiction"] == "colorado" \
            and urllib.parse.urlsplit(src.get("url") or "").hostname == "oit.colorado.gov":
        return ("Text taken from the Office of Information Technology's web page: the page heading, then the "
                "page body, one line per paragraph, heading and list item (list items marked with a bullet, "
                "nested lists indented), with markup, the site menu, breadcrumb, side navigation of the "
                "neighbouring guide pages, language selector, footer and scripts removed. The page prints no "
                "document number, version or effective date.")
    if src["doc_type"] == "statute" and src["jurisdiction"] == "colorado":
        return ("The source is the Office of Legislative Legal Services' title file (one file for the whole of "
                "the title); this document is the one article (or part) named in the citation, "
                "from its ARTICLE (or PART) heading line to the next one (an article stops "
                "before the title-level group heading, such as LIBRARIES, that the file prints "
                "between articles), one line per source paragraph, with markup, spacing paragraphs and non-breaking spaces removed. "
                "Caption lists, source notes, editor's notes and annotations are kept.")
    return None


def extra_notes(src, fmt, text, eff, version):
    notes = ""
    if src.get("oit_link"):
        notes += (f" OIT's page ({src.get('found_via', 'its index')}), where the list item reads "
                  f"{src.get('listed_as', 'its title')!r}, links this file as {src['oit_link']}; the text "
                  f"was fetched from Google Drive's direct-download form of the same file, {src['url']} (the source URL above).")
    if src["jurisdiction"] == "colorado" and src["doc_type"] == "rule":
        notes += (" The PDF is the copy the Secretary of State's page calls the official version of the rule "
                  "(it governs in all cases). Its cover's Secretary of State mark prints as a few scattered "
                  "letter fragments before the heading, kept as extracted. effective_date is the date of the "
                  "last `eff.` line of the rule's Editor's Notes History.")
    return notes
