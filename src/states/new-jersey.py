"""New Jersey: the Legislature's bulk statutes file and the Governor's infobank order pages. The Office of
Information Technology's circulars and standards are PDFs, which the shared readers handle. Hooks are described
in src/states/__init__.py.

The Legislature publishes the whole of the general and permanent statutes as one plain-text file inside
`STATUTES-TEXT.zip` (https://pub.njleg.gov/statutes/, rebuilt every weekday): a two-line banner ("... UPDATED THROUGH
P.L.2026, c.50, and J.R.1"), a `TITLE n` line, then each section as a heading line at column 0 (`52:18A-227  Office of
Information Technology.`) followed by indented paragraphs and a history line. A statute document here is the sections
a seed entry names (its `sections` list; the shared seed check accepts a `slice` only for California and Colorado), cut out of that file; the snapshot is a JSON bundle of those raw section
chunks, not the 41 MB zip (the same arrangement as California's)."""
from __future__ import annotations

import io
import json
import re
import zipfile
from pathlib import Path

from src.ingest_common import BlockParser, _decode
from src.states import UNHANDLED

_FORMAT = "njleg-statutes-slice/1"
_HEADING = re.compile(r"^(\d+[A-Za-z]?:\d+[A-Za-z]?(?:-[\w.]+)?)\.?[ \t]{1,4}(\S.*)$", re.M)
_TITLE = re.compile(r"^TITLE[ \t]+\d+[A-Za-z]?\b.*$", re.M)
_UPDATED = re.compile(r"\(UPDATED THROUGH\s+(.+?)\)")


def _norm(number: str) -> str:
    return number.rstrip(".")


def statute_bundle(txt: str, slice_: dict, url: str, last_modified: str = "") -> bytes:
    """The raw chunks of the sections a slice names, with the file's banner and the title line each sits under.
    A section the file does not hold is an error, never a smaller document."""
    wanted = slice_.get("sections") or []
    if not wanted or len(set(wanted)) != len(wanted):
        raise ValueError("a New Jersey statute slice needs `sections`: a list of section numbers, each once")
    txt = txt.replace("\r\n", "\n")
    heads = [(m.start(), _norm(m.group(1))) for m in _HEADING.finditer(txt)]
    titles = [(m.start(), m.group(0).strip()) for m in _TITLE.finditer(txt)]
    updated = _UPDATED.search(txt[:400])
    chunks, title_line = {}, None
    for i, (start, number) in enumerate(heads):
        if number in wanted:
            if number in chunks:
                raise ValueError(f"section {number} appears twice in the file: the slice is a guess")
            end = heads[i + 1][0] if i + 1 < len(heads) else len(txt)
            chunks[number] = txt[start:end].rstrip() + "\n"
            under = [t for pos, t in titles if pos < start][-1:] or [None]
            if title_line not in (None, under[0]):
                raise ValueError(f"sections {wanted} sit under more than one title: split the slice")
            title_line = under[0]
    missing = [n for n in wanted if n not in chunks]
    if missing:
        raise ValueError(f"no section {', '.join(missing)} in the file")
    doc = {"format": _FORMAT, "source": url, "zip_last_modified": last_modified,
           "banner": [" ".join(l.split()) for l in txt.split("\n")[:2]], "updated_through": updated.group(1).strip() if updated else "",
           "title_line": " ".join((title_line or "").split()), "slice": slice_,
           "sections": [{"number": n, "chunk": chunks[n]} for n in wanted]}
    return (json.dumps(doc, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def statute_bundle_to_text(raw: bytes) -> str:
    """The file's two banner lines, the title line, then each section: its heading as `number. Caption`, then one line per paragraph with the file's
    tab and space indentation squeezed out, then the history line as printed. A blank line separates sections."""
    doc = json.loads(raw)
    if doc.get("format") != _FORMAT:
        raise ValueError("not a New Jersey statutes slice bundle")
    out = list(doc["banner"]) + ([doc["title_line"]] if doc.get("title_line") else [])
    for s in doc["sections"]:
        lines = [" ".join(l.split()) for l in s["chunk"].splitlines()]
        lines = [l for l in lines if l]
        m = _HEADING.match(s["chunk"].splitlines()[0])
        if not m or _norm(m.group(1)) != s["number"]:
            raise ValueError(f"section {s['number']}: the chunk does not open with its heading")
        out.append("")
        out.append(f"{s['number']}. {' '.join(m.group(2).split())}")
        out.extend(lines[1:])
    return "\n".join(out) + "\n"


_ZIPS: dict[int, tuple] = {}      # id(fetcher) -> (fetcher, text, last_modified): the zip is read once per run


def _statutes_file(fetcher, url: str) -> tuple[str, str]:
    held = _ZIPS.get(id(fetcher))
    if held and held[0] is fetcher and held[3] == url:
        return held[1], held[2]
    resp = fetcher.get_response(url)
    with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
        member = next(n for n in z.namelist() if n.upper().endswith(".TXT"))
        text = z.read(member).decode("latin-1")
    _ZIPS[id(fetcher)] = (fetcher, text, resp.headers.get("last-modified", ""), url)
    return text, resp.headers.get("last-modified", "")


# ---- the Governor's infobank order pages (an old Dreamweaver template) ----------------------------

def infobank_order_to_text(raw: bytes) -> str:
    """An order page: the number and governor heading and the order's text (its editable regions), one line per
    paragraph and list item with the list numbered as a browser numbers it. The index link, the page's scripts and
    the template around the regions are not the order."""
    page = _decode(raw)
    region = lambda name: re.search(rf'<!-- #BeginEditable "{name}" -->(.*?)<!-- #EndEditable -->', page, re.S)
    number, gov, body = region("EONumber"), region("GovernorName"), region("ExecOrderText")
    if not (number and gov and body):
        raise ValueError("no order text: the page's editable regions are missing (the layout changed)")
    parser = BlockParser()
    parser.feed(f"<p>Executive Order #{number.group(1).strip()}</p><p>{gov.group(1)}</p>{body.group(1)}")
    parser._flush()
    return "\n".join(parser.lines) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "json" and doc_type == "statute":
        return statute_bundle_to_text(raw)
    if fmt == "html" and doc_type == "executive_order":
        return infobank_order_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "new-jersey":
        return False
    if src["doc_type"] == "statute":
        have = {l.split(". ", 1)[0] for l in text.splitlines()}
        missing = [n for n in src["sections"] if n not in have]
        if missing:
            raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: section {', '.join(missing)} "
                             f"is not in its text")
        return True
    if src["doc_type"] == "executive_order":
        number = re.search(r"No\. (\d+)", src["citation"]).group(1)
        # the order's own heading is its first line: a later order or a policy that recites it must not pass
        if not re.match(rf"EXECUTIVE ORDER\s+(?:NO\.\s*|#)\s*{number}\b", text.lstrip(), re.I):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: 'Executive Order No. {number}' "
                             f"is not the heading that opens its text")
        return True
    return False


_MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December")
_UNITS = {w: i for i, w in enumerate("one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
                                     "fifteen sixteen seventeen eighteen nineteen".split(), 1)}
_TENS = {w: 10 * i for i, w in enumerate("twenty thirty forty fifty sixty seventy eighty ninety".split(), 2)}
_SIGNED = re.compile(rf"GIVEN, under my hand and seal this\s+(\d{{1,2}})(?:st|nd|rd|th)?\s+day\s+of\s+({'|'.join(_MONTHS)}),?\s+"
                     rf"Two\s+Thousand(?:\s+and)?\s+([A-Za-z\s-]+?),?\s+and\s+of\b", re.I)


def _year_words(words: str) -> int | None:
    """'Twenty- Three' or 'Six' (the part of 'Two Thousand and ...' after the thousands) as a number."""
    total = 0
    for w in re.split(r"[\s-]+", words.strip().lower()):
        if w in _TENS:
            total += _TENS[w]
        elif w in _UNITS:
            total += _UNITS[w]
        elif w:
            return None
    return 2000 + total if total else None


def effective_date(text, doc_type):
    """An executive order prints no effective-date label; it says it takes effect immediately and prints the day it was
    signed ('GIVEN, under my hand and seal this 1st day of November, Two Thousand and Eighteen'). That signing day
    is its date. Policies and circulars go to the shared reader."""
    if doc_type != "executive_order":
        return UNHANDLED
    m = _SIGNED.search(text)
    year = _year_words(m.group(3)) if m else None
    if not year:
        return UNHANDLED
    return f"{year:04d}-{_MONTHS.index(m.group(2).capitalize()) + 1:02d}-{int(m.group(1)):02d}"


def source_version(text, doc_type, fmt):
    """A statute prints how current the file is on its banner line: (UPDATED THROUGH P.L.2026, c.50, and J.R.1)."""
    m = _UPDATED.search(text[:400]) if doc_type == "statute" else None
    return f"Updated through {m.group(1).strip()}" if m else None


def extra_notes(src, fmt, text, eff, version):
    notes = ""
    if src["doc_type"] == "executive_order" and eff:
        notes += (" effective_date is the day the Governor signed the order, as its closing paragraph prints it (this Nth "
                  "day of Month, Two Thousand and ...); the order prints no other date and says it takes effect immediately.")
    if version:
        notes += " source_version is the update line of the Legislature's file when it was read: " + version + "."
    return notes


def notes(src, fmt, text):
    if src["doc_type"] == "statute":
        return ("The source is the Legislature's bulk file of the general and permanent statutes "
                "(STATUTES-TEXT.zip, one plain-text file, rebuilt every weekday). This document is the sections "
                "named in the citation, cut out of it: the title line, then each section's number and caption, "
                "its paragraphs one per line with the file's indentation removed, and the history line as the file "
                "prints it. The snapshot is the JSON bundle of those raw section chunks, not the zip.")
    if src["doc_type"] == "executive_order" and fmt == "html":
        return ("Text taken from the Governor's infobank page for the order: the order number and governor, then the "
                "order's paragraphs one per line, its list numbered as a browser numbers it, with the index link, "
                "page scripts and template removed.")
    return None


def snapshot(src, fetcher, dest: Path, refetch):
    if src["doc_type"] != "statute":
        return None
    if dest.is_file() and not refetch:
        return dest.read_bytes(), False
    url = src["url"].split("#", 1)[0]       # the fragment only keeps entries on one file distinct (see the seed list)
    txt, modified = _statutes_file(fetcher, url)
    bundle = statute_bundle(txt, {"sections": src["sections"]}, url, modified)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(bundle)
    return bundle, True
