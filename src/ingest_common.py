"""Helpers every state's ingester shares: bytes to text for PDFs, the date patterns, and the paths and
configuration. Nothing here is one state's: a state's cleanup lives in `src/states/<state>.py`."""
from __future__ import annotations

import html as html_mod
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path

from corpus_toolkit import config as config_mod


ROOT = Path(__file__).resolve().parent.parent


CONFIG = config_mod.load(ROOT / "_meta" / "corpus.yml")


MIN_PDF_WORDS = 30   # below this a PDF is a scan (or an image-only page), not a text document


# ---- bytes to text: one function per source format --------------------------------------

def _decode(raw: bytes) -> str:
    m = re.search(rb"charset=([\w-]+)", raw[:4096])
    return raw.decode(m.group(1).decode() if m else "utf-8", errors="replace")


def _clean_line(s: str) -> str:
    return " ".join(html_mod.unescape(s).replace("\xa0", " ").split())


def paragraph_html_to_text(raw: bytes) -> str:
    """The Legislative Counsel's ORS chapter page (Word-exported HTML): one source paragraph
    per <p>, wrapped across several HTML lines and indented with &nbsp; runs. Each paragraph
    becomes one line; empty paragraphs (spacing) are dropped. Nothing else is removed."""
    body = _decode(raw)
    body = body[body.lower().find("<body"):]
    lines = []
    for p in re.findall(r"<p[^>]*>(.*?)</p>", body, flags=re.S | re.I):
        line = _clean_line(re.sub(r"<[^>]+>", "", p))
        if line:
            lines.append(line)
    return "\n".join(lines) + "\n"


# pdftotext emits a typographic ligature glyph where a PDF used one ("conﬁgured"). It is the
# same letters, but keyword search cannot match "conﬁgured" against "configured".
_LIGATURES = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi",
              "\ufb04": "ffl", "\ufb05": "st", "\ufb06": "st"}


def pdf_to_text(raw: bytes, no_text_pages=()) -> str:
    """`pdftotext -layout`, as the drift detector reads PDFs, with form feeds and trailing
    space removed and ligature glyphs written as their letters. Page headers, footers and
    column layout are kept: removing furniture per document would be editing the instrument.
    A page with no words (a scanned page) makes the whole PDF a refusal, because the text
    would silently lack that page; only pages the seed entry lists in `no_text_pages` (a
    figure, a blank page or a scanned form it has looked at) are let through, and a listed page
    that does have text is refused too, so the list stays true."""
    text = subprocess.run(["pdftotext", "-layout", "-", "-"], input=raw, capture_output=True,
                          check=True).stdout.decode("utf-8", "replace")
    pages = text.split("\f")
    if len(pages) > 1 and not pages[-1].strip():
        pages.pop()
    empty = [n for n, page in enumerate(pages, 1) if not page.split()]
    listed = sorted(set(no_text_pages))
    if [n for n in empty if n not in listed]:
        raise ValueError(f"PDF page(s) {', '.join(str(n) for n in empty if n not in listed)} "
                         f"have no text layer (a scan): needs OCR, make the entry a stub, or list the "
                         f"page as no_text_pages if it is a figure or blank")
    if [n for n in listed if n not in empty]:
        raise ValueError(f"seed entry lists page(s) {', '.join(str(n) for n in listed if n not in empty)} "
                         f"as no_text_pages but the PDF has text there")
    text = text.translate(str.maketrans(_LIGATURES))
    text = "\n".join(line.rstrip() for line in text.replace("\f", "\n").split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", text).strip("\n") + "\n"
    if len(text.split()) < MIN_PDF_WORDS:
        raise ValueError("PDF has no text layer (a scan): needs OCR, make the entry a stub")
    return text


class BlockParser(HTMLParser):
    """Collects the text of the State Administrative Manual's chapter view (dgs.ca.gov). Block
    elements start a new line, inline elements (span, a, strong, em, sup) run on inside the
    sentence, `<hr>` between sections gives a blank line. List markers are printed the way a
    browser prints them (the page styles them with CSS): `1.` for an ordered list, `a.` for
    `lower-alpha`, `i.` for `lower-roman`, a bullet for an unordered list; a nested list is
    indented two spaces per level."""

    BLOCK = {"p", "div", "h1", "h2", "h3", "h4", "li", "ol", "ul", "br", "tr"}
    # CSS `list-style-type` values a browser prints as letters or numbers; `lower-latin` is
    # `lower-alpha` under another name. Any other value is an error, never a silent decimal.
    STYLES = {"decimal": "decimal", "lower-alpha": "lower-alpha", "lower-latin": "lower-alpha",
              "upper-alpha": "upper-alpha", "upper-latin": "upper-alpha",
              "lower-roman": "lower-roman", "upper-roman": "upper-roman"}
    # The Secretary of State's stylesheet hides the browser marker on these list classes and
    # draws `(a)`, `(1)`, `(A)`, `(i)`, `(I)` itself: class -> counter style. Used only when
    # `paren_classes` is set (the CCR pages); a list with none of these classes keeps its style.
    PAREN_CLASSES = {"alphaLwr": "lower-alpha", "alphaLwrInline": "lower-alpha",
                     "numPrnthsis": "decimal", "numPrnthsisInline": "decimal",
                     "alphaUppr": "upper-alpha", "romanLwr": "lower-roman", "romanUppr": "upper-roman"}

    def __init__(self, paren_classes: bool = False):
        super().__init__(convert_charrefs=True)
        self.lines: list[str] = []
        self.cur: list[str] = []
        self.lists: list[list] = []          # [style, next number, parenthesized]
        self.skip = 0                         # inside <style> or <script>
        self.paren_classes = paren_classes

    def _flush(self):
        raw = "".join(self.cur)
        self.cur = []
        line = " ".join(raw.split())
        if line:
            self.lines.append(" " * (len(raw) - len(raw.lstrip(" "))) + line)

    @staticmethod
    def _marker(style: str, n: int, paren: bool = False) -> str:
        if style in ("lower-alpha", "upper-alpha"):
            letters = "abcdefghijklmnopqrstuvwxyz"
            out = letters[(n - 1) % 26]
            out = out if style == "lower-alpha" else out.upper()
        elif style in ("lower-roman", "upper-roman"):
            out, rest = "", n
            for v, r in ((10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")):
                while rest >= v:
                    out, rest = out + r, rest - v
            out = out if style == "lower-roman" else out.upper()
        elif style == "decimal":
            out = str(n)
        else:
            raise ValueError(f"list style {style!r} is not one the ingester knows: add it with a test")
        return f"({out})" if paren else f"{out}."

    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script"):
            self.skip += 1
            return
        if tag in ("ol", "ul"):
            self._flush()
            a = dict(attrs)
            paren = False
            if tag == "ul":
                kind = "bullet"
            else:
                classes = (a.get("class") or "").split()
                drawn = [self.PAREN_CLASSES[c] for c in classes if c in self.PAREN_CLASSES] \
                    if self.paren_classes else []
                found = re.search(r"list-style-type:\s*([a-z-]+)", a.get("style") or "")
                if drawn:
                    kind, paren = drawn[0], True
                elif found:
                    if found.group(1) not in self.STYLES:
                        raise ValueError(f"list style {found.group(1)!r} is not one the ingester "
                                         f"knows: add it with a test")
                    kind = self.STYLES[found.group(1)]
                else:
                    kind = "decimal"
            start = a.get("start")
            self.lists.append([kind, int(start) if start and start.isdigit() else 1, paren])
        elif tag == "li":
            self._flush()
            kind, n, paren = self.lists[-1] if self.lists else ("bullet", 1, False)
            mark = "\u2022" if kind == "bullet" else self._marker(kind, n, paren)
            if self.lists:
                self.lists[-1][1] += 1
            self.cur.append("  " * max(len(self.lists) - 1, 0) + mark + " ")
        elif tag == "hr":
            self._flush()
            self.lines.append("")
        elif tag in self.BLOCK:
            self._flush()

    def handle_endtag(self, tag):
        if tag in ("style", "script"):
            self.skip -= 1
        elif tag in ("ol", "ul") and self.lists:
            self._flush()
            self.lists.pop()
        elif tag in self.BLOCK:
            self._flush()

    def handle_data(self, data):
        if not self.skip:
            self.cur.append(data)


# ---- what the page itself states --------------------------------------------------------

_MONTHS = ("January|February|March|April|May|June|July|August|September|October|November|"
           "December")


_LONG_DATE = re.compile(rf"\b({_MONTHS})\s+(\d{{1,2}}),\s+(\d{{4}})\b")


_US_DATE = re.compile(r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{4})\b")   # 1/1/2010 or 01-01-2010


_EFFECTIVE_LABEL = re.compile(r"effective\s+date|\beffective\s*:", flags=re.I)


_DATED = re.compile(rf"^Dated\s+((?:{_MONTHS})\s+\d{{1,2}},\s+\d{{4}})\s*$", flags=re.M)


_LAST_REVIEW = re.compile(rf"^Last Review Date \| ((?:{_MONTHS})\s+\d{{4}})\s*$", flags=re.M)


_REVISION_ROW = re.compile(rf"^([^|\n]+?) \| ((?:{_MONTHS})\s+(?:\d{{1,2}},\s+)?\d{{4}})(?: \|.*)?$")


def _printed_version(text: str) -> str:
    """The date a Word file prints about itself where it prints no effective date: a front-table
    `Last Review Date | July 2024` row, a cover line `Dated April 1, 2025`, or the last row of a
    `Revision History` table headed `Version | Date`. Transcribed as printed; empty when none is."""
    if m := _LAST_REVIEW.search(text):
        return f"Last Review Date: {m.group(1)}"
    if m := _DATED.search(text):
        return f"Dated {m.group(1)}"
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().casefold() == "revision history":
            head = next((n for n in range(i + 1, min(i + 4, len(lines))) if lines[n].strip()), None)
            if head is None or not re.match(r"Version \| Date\b", lines[head]):
                continue
            rows = []
            for row in lines[head + 1:]:
                if not row.strip():
                    break
                if m := _REVISION_ROW.match(row):
                    rows.append(m.groups())
            if rows:
                return f"Version {rows[-1][0].strip()}, {rows[-1][1]}"
    return ""


_POLICY_NUMBER = re.compile(r"(?<!\d)\d{3}-\d{3}-\d{3}(?!\d)")   # 107-004-190, also before _PR


def _squash(s: str) -> str:
    """Whitespace, case and typographic apostrophes/dashes normalised, for phrase matching."""
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u2013", "-").replace("\u2014", "-")
    return " ".join(s.split()).casefold()
