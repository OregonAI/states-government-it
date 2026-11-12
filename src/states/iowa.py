"""Iowa: the policy portal's HTML policy pages (policies.iowa.gov/dom/policy/<slug>/), and the identity and
version checks of the Legislature's per-section Code PDFs, the Iowa Administrative Code chapter PDFs and the
executive orders (scans, read by the shared OCR procedure). Hooks are described in src/states/__init__.py.
The OCIO standards and every other PDF are read by the shared reader."""
from __future__ import annotations

import html as html_mod
import re
from html.parser import HTMLParser

from src.ingest_common import _clean_line, _decode, _squash

_BLOCK = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "li", "ul", "ol", "tr", "table", "br", "section", "blockquote"}
_SKIP = {"script", "style", "svg", "noscript"}


class _Body(HTMLParser):
    """The text inside the one <div class="policy-content ..."> of a policy page, one line per block."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0          # div depth inside the policy body; 0 = not inside
        self.skip = 0
        self.lines: list[str] = []
        self.cur: list[str] = []
        self.cells = False

    def _flush(self):
        line = _clean_line("".join(self.cur))
        if line:
            self.lines.append(line)
        self.cur = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.depth == 0:
            if tag == "div" and "policy-content" in (a.get("class") or "").split():
                self.depth = 1
            return
        if tag in _SKIP:
            self.skip += 1
        elif tag == "div":
            self.depth += 1
            self._flush()
        elif tag == "li":
            self._flush()
            self.cur.append("- ")
        elif tag in ("td", "th"):
            if self.cells:
                self.cur.append(" | ")
            self.cells = True
        elif tag == "tr":
            self._flush()
            self.cells = False
        elif tag in _BLOCK:
            self._flush()

    def handle_endtag(self, tag):
        if self.depth == 0:
            return
        if tag in _SKIP:
            self.skip -= 1
        elif tag == "div":
            self._flush()
            self.depth -= 1
        elif tag in _BLOCK:
            self._flush()

    def handle_data(self, data):
        if self.depth and not self.skip:
            self.cur.append(data)


def policy_html_to_text(raw: bytes) -> str:
    """A policy page of the State of Iowa's policy portal. Output: the page's title, one line with the
    published and updated dates and the version the page prints (when it prints one), then the policy body, one line per paragraph,
    list item and table row (cells joined by ' | '). The portal's machine-written 'Quick Summary', menus,
    breadcrumb and footer are not the policy and are not read."""
    page = _decode(raw)
    parser = _Body()
    parser.feed(page)
    parser._flush()
    if not parser.lines:
        raise ValueError("policy page has no policy-content body: the portal's layout changed")
    h1 = re.search(r"<h1\b[^>]*>(.*?)</h1>", page, flags=re.S)
    if not h1:
        raise ValueError("policy page has no title")
    head = [_clean_line(re.sub(r"<[^>]+>", "", h1.group(1)))]
    dates = [_clean_line(re.sub(r"<[^>]+>", "", d)) for d in re.findall(r"<time\b[^>]*>(.*?)</time>", page, flags=re.S)]
    ver = re.search(r'data-testid="document-version-number"[^>]*>\s*([^<]+?)\s*<', page)
    if not ver:
        # Some pages print the version as 'document-version-name' ('1.0'); on others that field holds the policy's
        # number (ADMN.303.02.E), which is not a version and is not taken for one.
        ver = re.search(r'data-testid="document-version-name"[^>]*>\s*(v?\d+(?:\.\d+)*)\s*<', page)
    meta = dates[:2] + ([_clean_line(ver.group(1))] if ver else [])
    if meta:
        head.append(" | ".join(meta))
    return "\n".join(head + parser.lines) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "html" and doc_type == "policy" and host == "policies.iowa.gov":
        return policy_html_to_text(raw)
    return None


def _lines(text: str) -> list[str]:
    return [_squash(l) for l in text.splitlines() if l.strip()]


def _prints_heading(lines: list[str], want: str) -> bool:
    """Some run of up to three consecutive lines (a wrapped title) is exactly `want`, or one line begins with
    `want` and then ends or prints only a defined term in parentheses ('Title ("Standard")', as the standards
    do) or goes on with something other than the punctuation of running text, as 'Policy Number: X' does. 'the Taxonomy ("Taxonomy"). In ...' inside a sentence does not count."""
    for i in range(len(lines)):
        if lines[i].startswith(want):
            rest = lines[i][len(want):].strip()
            if not rest or re.fullmatch(r"\(.{1,40}\)", rest) or rest[0] not in "(,;.)\"'\u201c\u201d":
                return True
        joined = lines[i]
        for j in range(i + 1, min(i + 3, len(lines))):
            joined = _squash(joined + " " + lines[j])
            if joined == want:
                return True
    return False


def check_identity(src, text, what_is):
    """A Code section, a rule chapter, an executive order, a standard or a policy must print its own heading: a
    line that begins with `identity_text` (a wrapped title counts, see _prints_heading); for a chapter, a line
    that is `identity_text` ('CHAPTER 8') and one that is `identity_title`; an order's whole heading line. A
    mention of the title or number inside another line does not count (playbook lesson f)."""
    if src["jurisdiction"] != "iowa" or src["doc_type"] not in ("statute", "rule", "executive_order", "standard", "policy"):
        return False
    phrase = src.get("identity_text")
    if not phrase:
        raise ValueError(f"{src['id']}: an Iowa {src['doc_type']} entry needs identity_text")
    lines = _lines(text)
    want = _squash(phrase)
    if src["doc_type"] == "executive_order" or src["doc_type"] == "rule":
        ok = any(l == want for l in lines)
    elif src["doc_type"] == "statute":
        ok = any(l.startswith(want) for l in lines)
    else:
        ok = _prints_heading(lines, want)
    if ok and src.get("identity_title"):
        ok = _squash(src["identity_title"]) in lines
    if not ok:
        raise ValueError(f"{src['id']}: {what_is} is not the cited instrument: no line of its text is "
                         f"{phrase!r}" + (f" and {src['identity_title']!r}" if src.get("identity_title") else ""))
    return True


def source_version(text, doc_type, fmt):
    """The edition a Code section's footer prints ('Iowa Code 2026, Section 8.77'), or the date a rule chapter's
    running header prints ('IAC 2/5/25'). Nothing else here prints a version."""
    if doc_type == "statute":
        m = re.search(r"Iowa Code (\d{4}), (?:Section|Chapter) ", text)
        return f"Iowa Code {m.group(1)}" if m else ""
    if doc_type == "rule":
        m = re.search(r"^IAC (\d{1,2}/\d{1,2}/\d{2})\b", text, flags=re.M)
        return f"IAC {m.group(1)}" if m else ""
    return ""


def notes(src, fmt, text):
    if fmt != "html":
        return None
    second = text.splitlines()[1] if len(text.splitlines()) > 1 else ""
    has_version = second.count(" | ") >= 2
    kept = ("The page's title, its published and updated dates and its version are kept on the first two lines; "
            if has_version else
            "The page's title and its published and updated dates are kept on the first two lines (the page prints "
            "no version number); ")
    return ("Text taken from the policy page on the State of Iowa's policy portal (policies.iowa.gov), not from the "
            "page's PDF version, which the portal generates anew on every request and so never hashes the same twice. "
            + kept + "the policy body follows, one line per paragraph, list item and table row (cells joined by ' | '). The "
            "portal's machine-written 'Quick Summary' box, menus, breadcrumb and footer, and the links' targets, "
            "were not read.")
