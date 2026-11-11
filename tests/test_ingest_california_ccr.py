"""Seam: src.ingest.to_text for the Secretary of State's California Code of Regulations chapters.
The Secretary of State's stylesheet (www-specific.css, fetched 2026-11-11) hides the browser's list
markers on these lists (`#main ol.alphaLwr ... {list-style:none!important}`) and draws its own with
::before, e.g. `ol.alphaLwr li:before{content:'(' counter(item, lower-alpha) ') '}`. So the page
shows (a), (1), (A), (i), the form the regulations cite ("section 22003(a)")."""
from pathlib import Path

import pytest

from src import ingest as ing

SNAP = Path(__file__).resolve().parent.parent / "_meta" / "snapshots"
CH10 = (SNAP / "ca-ccr-2-div-7-ch-10.html").read_bytes()
CH15 = (SNAP / "ca-ccr-2-div-7-ch-15.html").read_bytes()


def ccr(raw):
    return ing.to_text(raw, "html", "rule", "california")


def page(lists: bytes) -> bytes:
    return (b'<html><body><main id="main"><div id="main-content-normal"><h1>Title 2.</h1>'
            + lists + b'</div><div> </div><div id="left-sidebar"></div></main></body></html>')


def test_ccr_chapter_10_definitions_use_the_parenthesized_designators_the_page_draws():
    t = ccr(CH10).splitlines()
    # section 22000's first list has no class in the page's markup, so a browser prints its own "a."
    assert t[11] == "a. For purposes of this chapter, and unless the context expressly indicates otherwise"
    assert any(l.startswith("(a) For a digital signature to be valid") for l in t)
    assert any(l.startswith("  (1) “Digitally signed communication” is a message") for l in t)
    assert any(l.startswith("  (2) “Message” means") for l in t)
    assert any(l.startswith("    (B) “Certificate” means") or l.startswith("  (B) “Certificate” means")
               for l in t)


def test_ccr_text_has_no_dotted_list_markers():
    import re
    for raw in (CH10, CH15):
        bad = [l for l in ccr(raw).splitlines() if re.match(r"\s*([a-zA-Z]|\d+|[ivxIVX]+)\. [\u201c\w]", l)
               and not re.match(r"\s*\d{5}\. ", l)
               and not l.startswith("a. For purposes of this chapter")]   # the one unclassed list
        assert bad == [], bad[:3]


@pytest.mark.parametrize("cls,items,want", [
    ("alphaLwr", 2, ["(a) x", "(b) x"]),
    ("alphaLwrInline", 2, ["(a) x", "(b) x"]),
    ("numPrnthsis", 2, ["(1) x", "(2) x"]),
    ("numPrnthsisInline", 2, ["(1) x", "(2) x"]),
    ("alphaUppr", 2, ["(A) x", "(B) x"]),
    ("romanLwr", 4, ["(i) x", "(ii) x", "(iii) x", "(iv) x"]),
    ("romanUppr", 2, ["(I) x", "(II) x"]),
])
def test_ccr_list_classes_map_to_the_stylesheets_markers(cls, items, want):
    lis = b"<li>x</li>" * items
    got = ccr(page(b'<ol class="%s">%s</ol>' % (cls.encode(), lis)))
    assert got.splitlines()[1:] == want


def test_ccr_class_wins_over_the_inline_style_and_nested_lists_indent():
    got = ccr(page(b'<ol class="alphaLwr" style="list-style-type: lower-alpha;"><li>a<ol class="numPrnthsis">'
                   b'<li>b</li></ol></li></ol>'))
    assert got.splitlines()[1:] == ["(a) a", "  (1) b"]


def test_ccr_list_without_a_class_keeps_the_browsers_marker():
    got = ccr(page(b'<ol start="1" style="list-style-type: lower-alpha;"><li>x</li></ol>'))
    assert got.splitlines()[1:] == ["a. x"]


def test_ccr_conversion_notes_do_not_claim_dotted_markers():
    src = {"id": "x", "doc_type": "rule", "jurisdiction": "california"}
    n = ing.conversion_notes(src, "html", "x")
    assert "(a)" in n and "(1., a., i.)" not in n
