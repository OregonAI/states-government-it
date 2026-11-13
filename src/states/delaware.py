"""Delaware: the Delaware Code Online (delcode.delaware.gov), DTI's policy and standard PDFs, and the Public Archives'
scanned executive orders. Hooks are described in src/states/__init__.py. PDFs and scans are shared.

Statutes (`delcode.delaware.gov/title<T>/c<CCC>/[sc<NN>/]index.html`): the page is a chapter, or one subchapter of a
chapter, built by an XSLT. Inside `<div id="TitleHead">` are the title, chapter and subchapter heads (h1-h4); inside
`<div id="CodeBody">` each `<div class="Section">` holds a `SectionHead`, its paragraphs (`<p class="subsection">`,
`indent-2`, `indent-3`, ...) and, outside any paragraph, the section's history citations and any repeal note. After
the last section the page prints that section's first history citation once more, outside the section; that
repeat is not read. The menus, the breadcrumb, the section index at the top (`ul.chaptersections`) and the footer are not read."""
from __future__ import annotations

import datetime
import re
from html.parser import HTMLParser

from src.ingest_common import _squash

_ZERO_WIDTH = dict.fromkeys(map(ord, "​‌‍﻿"), None)
_VOID = {"img", "input", "br", "hr", "wbr", "meta", "link", "area", "base", "col", "embed", "source", "track"}
_HEADS = {"h1", "h2", "h3", "h4"}
_INDENT = re.compile(r"indent-(\d+)")


def _norm(s: str) -> str:
    return " ".join(s.translate(_ZERO_WIDTH).replace("\xa0", " ").split())


class _Code(HTMLParser):
    """The text of a delcode page: head lines, then a blank line and one block per section."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.head: list[str] = []          # TitleHead lines
        self.out: list[str] = []           # CodeBody lines
        self.cur: list[str] = []
        self.stack: list[tuple[str, str]] = []     # (tag, role) of the open elements that matter
        self.in_head = False
        self.in_body = False
        self.section_depth = 0             # nesting depth of div elements inside the open Section, 0 = outside
        self.in_section = False
        self.cur_indent = ""
        self.in_p = False
        self.in_sechead = False
        self.history: list[str] = []
        self.sections = 0

    # -- helpers
    def _flush(self, into: list[str], indent: str = ""):
        line = _norm("".join(self.cur))
        self.cur = []
        if line:
            into.append(indent + line)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class") or ""
        if tag in _VOID:
            return
        if tag == "div" and a.get("id") == "TitleHead":
            self.in_head, self.head_depth = True, 1
            return
        if tag == "div" and a.get("id") == "CodeBody":
            self.in_body, self.body_depth = True, 1
            return
        if self.in_head:
            if tag == "div":
                self.head_depth += 1
            if tag in _HEADS:
                self.cur = []
            return
        if not self.in_body:
            return
        if tag == "div":
            self.body_depth += 1
            if "Section" == cls and not self.in_section:
                self.in_section, self.section_depth = True, 1
                self.sections += 1
                if self.out:
                    self.out.append("")
                self.history = []
                return
            if self.in_section:
                self.section_depth += 1
                if cls == "SectionHead":
                    self.in_sechead = True
                    self.cur = []
            return
        if self.in_section and tag == "p":
            self.in_p = True
            self.cur = []
            m = _INDENT.search(cls)
            self.cur_indent = "  " * (int(m.group(1)) - 1) if m else ""

    def handle_endtag(self, tag):
        if tag in _VOID:
            return
        if self.in_head:
            if tag in _HEADS:
                self._flush(self.head)
            elif tag == "div":
                self.head_depth -= 1
                if self.head_depth == 0:
                    self.in_head = False
            return
        if not self.in_body:
            return
        if tag == "p" and self.in_p:
            self._flush(self.out, self.cur_indent)
            self.in_p = False
            return
        if tag == "div":
            self.body_depth -= 1
            if self.in_section:
                if self.in_sechead:
                    self._flush(self.out)
                    self.in_sechead = False
                self.section_depth -= 1
                if self.section_depth == 0:
                    self.in_section = False
                    self._flush(self.out)            # the history citations and any repeal note
            if self.body_depth == 0:
                self.in_body = False

    def handle_data(self, data):
        if self.in_head or (self.in_body and self.in_section):
            self.cur.append(data)


_SECTION_HEAD = re.compile(r"^§ (\d+[A-Z]?(?:-\d+[A-Z]?)?)\.")


def _cut(head: list[str], body: list[str], start: str, end_before: str) -> list[str]:
    """The sections from the heading of `start` up to, not including, the heading of `end_before`. `body` holds one
    section per blank-line-separated block, each opening on its `§ N.` heading. The page heads are kept."""
    blocks, cur = [], []
    for line in body + [""]:
        if line:
            cur.append(line)
        elif cur:
            blocks.append(cur)
            cur = []
    numbers = [(_SECTION_HEAD.match(b[0]) or [None, None])[1] for b in blocks]
    for n in (start, end_before):
        if n not in numbers:
            raise ValueError(f"slice: section {n} has no heading on the page (the page changed, the section was "
                             f"renumbered, or the slice is wrong)")
    i, j = numbers.index(start), numbers.index(end_before)
    if i >= j:
        raise ValueError(f"slice: section {start} does not come before section {end_before} on the page")
    out: list[str] = []
    for b in blocks[i:j]:
        out += ([""] if out else []) + b
    return head + [""] + out


def delcode_to_text(raw: bytes, slice_: dict | None = None) -> str:
    p = _Code()
    p.feed(raw.decode("utf-8", errors="replace"))
    p.close()
    if not p.sections or not p.out:
        raise ValueError("Delaware Code page has no code body: the page layout changed or this is not a code page")
    if slice_:
        return "\n".join(_cut(p.head, p.out, slice_["section_start"], slice_["section_end_before"])) + "\n"
    return "\n".join(p.head + [""] + p.out) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "statute":
        return delcode_to_text(raw, slice_)
    return None


_CITE = re.compile(r"^(\d+) Del\. C\. ch\. (\w+)(?:, subch\. ([IVX]+))?")
_SECTIONS = re.compile(r"(\d+) Del\. C\. (\d+[A-Z]?(?:-\d+[A-Z]?)?)(?: to (\d+[A-Z]?(?:-\d+[A-Z]?)?))?")
_HEAD_EFFECTIVE = re.compile(r"\[Effective ([A-Z][a-z]{2})[a-z]*\.? (\d{1,2}), (\d{4})\]")
_MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
_WORDS = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
          "seventeen eighteen nineteen").split()
_TENS = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}


def _number_words(n: int) -> str:
    if n < 20:
        return _WORDS[n]
    return _TENS[n // 10] + (f" {_WORDS[n % 10]}" if n % 10 else "")


def _check_sections(src, text, what_is, sec, today=None):
    """A section slice is the cited one when its title is the cited title, it opens on the first cited section's
    heading and its last heading is the last cited section, and no heading is a repeal or a not-yet-effective mark."""
    title, first, last = sec.group(1), sec.group(2), sec.group(3) or sec.group(2)
    lines = text.splitlines()
    heads = [m.group(1) for l in lines if (m := _SECTION_HEAD.match(l))]
    if f"TITLE {title}" not in lines or not heads or heads[0] != first or heads[-1] != last:
        raise ValueError(f"{src['id']}: {what_is} is not {src['citation']}: the slice opens on "
                         f"{heads[0] if heads else None!r} and its last heading is {heads[-1] if heads else None!r}")
    for l in lines:
        if _SECTION_HEAD.match(l) and "[Repealed]" in l:
            raise ValueError(f"{src['id']}: {l.split('.')[0]} is printed as repealed: not in force")
        if _SECTION_HEAD.match(l) and (e := _HEAD_EFFECTIVE.search(l)):
            d = datetime.date(int(e.group(3)), _MON.index(e.group(1)) + 1, int(e.group(2)))
            if d > (today or datetime.date.today()):
                raise ValueError(f"{src['id']}: {l.split('.')[0]} is not in force until {d.isoformat()}")
    return True


def check_identity(src, text, what_is):
    if src["jurisdiction"] != "delaware":
        return False
    if src["doc_type"] == "statute" and (sec := _SECTIONS.fullmatch(src["citation"])):
        return _check_sections(src, text, what_is, sec)
    if src["doc_type"] == "statute":
        m = _CITE.match(src["citation"])
        if not m:
            raise ValueError(f"{src['id']}: cannot read the title and chapter from the citation {src['citation']!r}")
        title, chapter, sub = m.groups()
        lines = text.splitlines()
        ok = (f"TITLE {title}" in lines
              and any(l.startswith(f"CHAPTER {chapter}. ") for l in lines)
              and (sub is None or any(l.startswith(f"Subchapter {sub}. ") for l in lines[:8])))
        if not ok:
            raise ValueError(f"{src['id']}: page is not {m.group(0)} (title, chapter or subchapter mismatch)")
        return True
    if src["doc_type"] == "executive_order":
        n = re.search(r"\bNo\.\s*(\d{1,2})\b", src["citation"])
        if not n:
            raise ValueError(f"{src['id']}: cannot read the order number from the citation {src['citation']!r}")
        words = _number_words(int(n.group(1)))
        heading = re.compile(r"^\W*EXECUTIVE\s+ORDER\s*\n?\s*NUMBER\s+" + r"[\s-]+".join(words.split()) + r"\W*$",
                             flags=re.I | re.M)
        if not heading.search(text):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: its heading 'Executive Order "
                             f"Number {words.title()}' does not appear")
        if src.get("identity_text") and _squash(src["identity_text"]) not in _squash(text):
            raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: {src['identity_text']!r} "
                             f"does not appear in its text")
        return True
    return False


_REVISION = re.compile(r"^\s*(?:.*?\s{2,})?Revision Number:\s*(\d+)\b", flags=re.M)
_REVIEWED = re.compile(r"^\s*Reviewed:\s*(\d{1,2}/\d{1,2}/\d{4})\b", flags=re.M)
_TITLE_BLOCK = 2500      # characters: the first page's title block, before the body text


def source_version(text, doc_type, fmt):
    """DTI's policy, standard and guideline PDFs print 'Revision Number: N' and 'Reviewed: M/D/YYYY' in the title
    block of the first page (and repeat the revision on every page head); the first page's are read."""
    if doc_type not in ("policy", "standard"):
        return None
    head = text[:_TITLE_BLOCK]
    rev = _REVISION.search(head)
    if not rev:
        return None
    rv = _REVIEWED.search(head)
    return f"Revision {rev.group(1)}" + (f" (reviewed {rv.group(1)})" if rv else "")


def notes(src, fmt, text):
    if fmt == "html" and src["doc_type"] == "statute":
        sl = src.get("slice") or {}
        cut = (f"This document is the sections from the heading of section {sl['section_start']} to the line before the "
               f"heading of section {sl['section_end_before']} of the page, cut here; the page's other sections are "
               f"not in it. " if sl else "")
        return cut + ("Text taken from the Delaware Code Online page on delcode.delaware.gov (the Division of Research of the "
                "General Assembly): the title, chapter and subchapter heads, then each section's heading, "
                "paragraphs, history citations and any repeal note, one line per paragraph, indented by the "
                "page's paragraph level. The menus, the breadcrumb, the section index at the top of the page and "
                "the footer were removed. The page prints the last section's first history citation a second time after the "
                "section; the repeat is not read. The page prints no effective date for the chapter.")
    return None
