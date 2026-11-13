"""New York: State Technology Law articles from the Senate's Open Legislation API, ITS's page of its NYCRR
part, and the Governor's executive orders. Hooks are described in src/states/__init__.py.

The API needs a free key. It is read at run time from NY_OPENLEG_KEY, else from the owner-only file named by
NY_OPENLEG_KEY_FILE (default ~/.config/oregonai/ny_openleg_key), added to the request URL here and nowhere
else: seed-entry urls are keyless, the snapshot never holds it, and an error that quotes the request is
scrubbed of it before it is raised."""
from __future__ import annotations

import json
import os
import re
import urllib.parse
from pathlib import Path

from src.ingest_common import _clean_line, _decode, _squash

API_HOST = "legislation.nysenate.gov"
LAW = "STT"                    # the State Technology Law: the only law this state holds; the seed slice names the article
KEY_FILE = "~/.config/oregonai/ny_openleg_key"
# Laws outside the State Technology Law from which one section is seeded (owner decision 2026-11-13: a provision whose
# own focus is the governance of state IT); lawId -> the name the citation uses
SECTION_LAWS = {"EXC": "Executive Law"}
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}


def api_key() -> str:
    key = os.environ.get("NY_OPENLEG_KEY", "").strip()
    if not key:
        path = Path(os.environ.get("NY_OPENLEG_KEY_FILE", KEY_FILE)).expanduser()
        key = path.read_text().strip() if path.is_file() else ""
    if not key:
        raise ValueError("no Open Legislation API key: set NY_OPENLEG_KEY or put it in "
                         f"{os.environ.get('NY_OPENLEG_KEY_FILE', KEY_FILE)}")
    return key


def law_tree_to_text(raw: bytes, slice_: dict | None) -> str:
    """One article of a consolidated law from the API's law tree (`laws/<law>?full=true&fromLocation=<loc>
    &toLocation=<loc>`): the article's own text, then each section's text in source order. The API stores a
    line break as the two characters backslash and n; they become line breaks. Nothing else is changed."""
    slice_ = slice_ or {}
    if "section_start" in slice_:
        return section_to_text(raw, slice_)
    try:
        tree = json.loads(raw)
        root = tree["result"]["documents"]
        law = tree["result"]["info"]["lawId"]
    except (ValueError, KeyError, TypeError):
        raise ValueError("not a law tree: the API did not answer with the article's document tree") from None
    if law != LAW or root.get("locationId") != slice_.get("article"):
        raise ValueError(f"not the article the seed entry cites ({LAW} {slice_.get('article')}): "
                         f"the API answered {law} {root.get('locationId')}")
    parts = [root.get("text") or ""] + [c.get("text") or "" for c in (root.get("documents") or {}).get("items", [])]
    blocks = []
    for part in parts:
        lines = [l.rstrip() for l in part.replace("\\n", "\n").split("\n")]
        block = "\n".join(lines).strip("\n")
        if block.strip():
            blocks.append(block)
    if len(blocks) < 2:
        raise ValueError("not a law tree: the article has no section text")
    return "\n\n".join(blocks) + "\n"


def section_to_text(raw: bytes, slice_: dict) -> str:
    """One section of a consolidated law from the API's law tree (`laws/<law>?full=true&fromLocation=<section>
    &toLocation=<section>`): the section's own text, and nothing before or after it. The slice names the section
    (`section_start`) and the section that follows it (`section_end_before`, which is not in the text). The API stores
    a line break as the two characters backslash and n; they become line breaks."""
    try:
        tree = json.loads(raw)
        root = tree["result"]["documents"]
        law = tree["result"]["info"]["lawId"]
        text = root["text"]
    except (ValueError, KeyError, TypeError):
        raise ValueError("not a law tree: the API did not answer with the section's document tree") from None
    want = slice_["section_start"]
    if law not in SECTION_LAWS or root.get("docType") != "SECTION" or \
            str(root.get("locationId", "")).upper() != want.upper() or (root.get("documents") or {}).get("items"):
        raise ValueError(f"not the section the seed entry cites ({want}): the API answered {law} "
                         f"{root.get('docType')} {root.get('locationId')}")
    if root.get("repealed"):
        raise ValueError(f"section {want} is marked repealed by the API: not in force")
    lines = [l.rstrip() for l in text.replace("\\n", "\n").split("\n")]
    out = "\n".join(lines).strip("\n")
    if not out.strip():
        raise ValueError("not a law tree: the section has no text")
    return out + "\n"


def its_page_to_text(raw: bytes) -> str:
    """An ITS page that prints a NYCRR part (its.ny.gov): the page title, then the body area. The site
    navigation, footer and scripts around them are not text of the rule."""
    page = _decode(raw)
    start = page.find('<div class="page-body">')
    h1 = re.search(r'<div class="title-page">\s*<h1[^>]*>(.*?)</h1>', page, flags=re.S)
    end = page.find("</main>", start)
    if not h1 or start < 0 or end < 0:
        raise ValueError("ITS page has no body region: the page layout changed")
    region = re.sub(r"<(script|style).*?</\1>", " ", page[start:end], flags=re.S | re.I)
    region = re.sub(r"<br\s*/?>|</?(p|div|h[1-6]|li|ul|ol|tr)\b[^>]*>", "\n", region, flags=re.I)
    region = re.sub(r"<[^>]+>", "", region)
    out = [_clean_line(re.sub(r"<[^>]+>", "", h1.group(1)))]
    for raw_line in region.split("\n"):
        line = _clean_line(raw_line)
        if line:
            out.append(line)
    return "\n".join(out) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "json" and doc_type == "statute":
        return law_tree_to_text(raw, slice_)
    if fmt == "html" and doc_type in ("rule", "executive_order"):
        return its_page_to_text(raw)
    return None


def check_identity(src, text, what_is):
    kind = src["doc_type"]
    if kind == "statute" and (src.get("slice") or {}).get("section_start"):
        sec = src["slice"]["section_start"]
        first = next((l.strip() for l in text.splitlines() if l.strip()), "")
        law = re.search(r"/laws/([A-Z]+)\b", src.get("url") or "")
        name = SECTION_LAWS.get(law.group(1)) if law else None
        cited = re.fullmatch(rf"(.+?) section {re.escape(sec)}", src["citation"], flags=re.I)
        opens = re.match(rf"\*?\s*§ {re.escape(sec)}\.", first, flags=re.I)
        if not (name and cited and cited.group(1) == name and opens):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {src['citation']!r} is not "
                             f"the law and section the text opens with ({first[:60]!r})")
        return True
    if kind == "statute":
        m = re.search(r"\bArticle\s+(\d+)\b", src["citation"])
        first = next((l.strip() for l in text.splitlines() if l.strip()), "")
        if not m or re.sub(r"^\*\s*", "", first) != f"ARTICLE {ROMAN.get(int(m.group(1)), '?')}":
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {src['citation']!r} is not "
                             f"the article the text opens with ({first!r})")
        return True
    if kind == "rule":
        m = re.search(r"\bPart\s+(\d+)\b", src["citation"])
        if not m or not re.search(rf"^PART {m.group(1)}\.?$", text, flags=re.M):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: no 'PART "
                             f"{m and m.group(1)}' heading line in its text")
        return True
    if kind == "executive_order":
        m = re.search(r"\bNo\.?\s*(\d+(?:\.\d+)?)", src["citation"])
        head = [re.sub(r"\s+", "", _squash(l)) for l in text.splitlines() if l.strip()][:10]
        want = rf"executiveorder(?:no\.?)?{re.escape(m.group(1)) if m else '?'}\.?"
        if not m or not any(re.fullmatch(want, l) for l in head):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {src['citation']!r} is not "
                             f"a heading line of the order (its first lines)")
        return True
    return False


_HEADER_DATE = re.compile(r"\b(Updated|Issued|Released):\s*(\d{1,2}/\d{1,2}/\d{2}(?:\d{2})?)\b")


def source_version(text, doc_type, fmt):
    """The date the header block of an ITS policy or standard PDF prints about itself ('Updated:',
    'Issued:' or 'Released:' beside the number and owner), as printed. The header block is the first 40
    lines; a later 'Updated' in a revision table or the body is not read. 'Issued By:' has no date."""
    if fmt != "pdf" or doc_type not in ("policy", "standard"):
        return None
    for line in text.splitlines()[:40]:
        if m := _HEADER_DATE.search(line):
            return f"{m.group(1)}: {m.group(2)}"
    return None


def notes(src, fmt, text):
    if src["doc_type"] == "statute" and (src.get("slice") or {}).get("section_start"):
        return ("Text from the Senate's Open Legislation API (legislation.nysenate.gov/api/3/laws), one section of a "
                "consolidated law of a chapter that is not itself about information technology, seeded as a section "
                "because the section's own subject is the governance of state IT; exactly as the API returns it, "
                "with the API's line break (the two characters backslash and n) written as a line break and trailing "
                "spaces removed. The API needs a key; the key is added to the request only and is not in the "
                "snapshot or this document.")
    if src["doc_type"] == "statute":
        return ("Text from the Senate's Open Legislation API (legislation.nysenate.gov/api/3/laws), one article "
                "of the State Technology Law per document: the article's own text, then each section's text in "
                "order, exactly as the API returns it (its line breaks and indentation kept). The API stores each "
                "line break as the two characters backslash and n; they are written here as line breaks, and "
                "trailing spaces are removed. The API needs a key; the key is added to the request only and is "
                "not in the snapshot or this document. The snapshot also holds the API's version dates and "
                "per-section active and repealed fields.")
    if src["doc_type"] == "rule":
        return ("Text taken from the page's title and body area (the `page-body` block) on its.ny.gov, ITS's own "
                "publication of this Part of Title 9 NYCRR; site navigation, footer and scripts removed, one line "
                "per source paragraph, the section and subdivision labels kept as printed. The official NYCRR "
                "(govt.westlaw.com/nycrr) refused the Fetcher with a Cloudflare managed challenge (HTTP 403), "
                "so this agency copy is the text of record here.")
    if src["doc_type"] == "executive_order" and fmt == "html":
        return ("Text taken from the page's title and body area (the `page-body` block) on its.ny.gov, where ITS "
                "prints the order; site navigation, footer and scripts removed, one line per source paragraph. The "
                "Governor's own PDF of the order is a scan and did not pass the two-engine OCR gates (the engines "
                "agreed on 43% of its 14 figures, bar 90%), so this agency copy is the text of record here.")
    return None


def snapshot(src, fetcher, dest, refetch):
    """The API entries: one GET with the key on the request. Any other entry: None (one plain GET)."""
    if urllib.parse.urlsplit(src.get("url") or "").hostname != API_HOST:
        return None
    dest = Path(dest)
    if dest.is_file() and not refetch:
        return dest.read_bytes(), False
    key = api_key()
    url = src["url"] + ("&" if "?" in src["url"] else "?") + "key=" + urllib.parse.quote(key, safe="")
    try:
        body = fetcher.get(url).body
    except Exception as e:                       # the message may quote the request url
        raise ValueError(f"{src.get('id')}: Open Legislation API request failed: "
                         + str(e).replace(key, "<key>").replace(urllib.parse.quote(key, safe=""), "<key>")) from None
    for form in (key, urllib.parse.quote(key, safe="")):
        body = body.replace(form.encode(), b"")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(body)
    return body, True
