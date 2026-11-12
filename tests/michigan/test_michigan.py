"""Seam: src.states (to_text, check_identity, notes) for Michigan. Michigan's statutes are the Legislature's
per-act PDFs (shared reader); its executive orders are the Legislature's archive copies: older ones are
Word- or Vignette-made HTML pages, newer ones PDFs. Fixtures are the bytes the Legislature served on
2026-11-12, whole files, page furniture included, nothing re-typed."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "michigan"
EO94 = (FIX / "eo-1994-15-telecom.html").read_bytes()          # bare Word HTML, no page furniture
EO05 = (FIX / "eo-2005-2-public-safety-comms.html").read_bytes()  # Vignette print page with a style block and tables
EO09 = (FIX / "eo-2009-55-dtmb.html").read_bytes()             # Vignette print page: www.michigan.gov bar, release dates, copyright
EO16 = (FIX / "eo-2016-24-eim.pdf").read_bytes()               # a scan with a machine-OCR text layer: only the heading logic is tested
EO22 = (FIX / "eo-2022-11-data-analytics.pdf").read_bytes()
ACT132 = (FIX / "mcl-act-132-of-2017.pdf").read_bytes()


def eo(raw):
    return ing.to_text(raw, "html", "executive_order", "michigan")


def src(**kw):
    base = {"id": "x", "jurisdiction": "michigan", "doc_type": "executive_order", "format": "html",
            "citation": "Executive Order No. 2009-55", "title": "t"}
    base.update(kw)
    return base


def test_eo_text_is_one_line_per_paragraph_with_the_heading_lines_first():
    lines = eo(EO09).splitlines()
    assert "EXECUTIVE ORDER No. 2009 - 55" in lines
    i = lines.index("EXECUTIVE ORDER No. 2009 - 55")
    assert lines[i + 1] == "DEPARTMENT OF INFORMATION TECHNOLOGY"
    assert any(l.startswith("WHEREAS, Section 1 of Article V of the Michigan Constitution of 1963 vests") for l in lines)
    assert any("effective March 21, 2010" in l for l in lines)


def test_eo_text_drops_the_style_block_print_bar_and_copyright_but_keeps_release_dates():
    for raw in (EO05, EO09):
        t = eo(raw)
        assert "10pt" not in t and "sans-serif" not in t
        assert "font-family" not in t.lower()
        assert "To Print" not in t and "www.michigan.gov" not in t
        assert "Copyright" not in t
        assert "<" not in t and "&nbsp;" not in t and "\xa0" not in t
    assert "Release Date: December 30, 2009" in eo(EO09)


def test_eo_text_of_a_bare_word_page_joins_wrapped_lines_into_their_paragraph():
    lines = eo(EO94).splitlines()
    assert lines[0] == "EXECUTIVE ORDER"
    assert lines[1] == "No. 1994 - 15"
    assert any(l.startswith("WHEREAS, Section 271 of Act No. 431") and "establish,manage, and operate" in l for l in lines)


def test_identity_accepts_the_orders_own_heading_and_refuses_another_order_that_only_mentions_it():
    states.check_identity(src(), eo(EO09), "html")
    states.check_identity(src(id="a", citation="Executive Order No. 1994-15"), eo(EO94), "html")
    with pytest.raises(ValueError):
        states.check_identity(src(citation="Executive Order No. 2001-3"), eo(EO09), "html")   # 2009-55 mentions "Executive Order 2001-3"


def test_identity_reads_a_pdf_order_whose_heading_has_no_number_sign_label_on_the_same_line():
    text = ing.to_text(EO22, "pdf", "executive_order", "michigan")
    states.check_identity(src(citation="Executive Order No. 2022-11", format="pdf"), text, "pdf")
    with pytest.raises(ValueError):
        states.check_identity(src(citation="Executive Order No. 2016-24", format="pdf"), text, "pdf")


def test_identity_reads_only_the_first_heading_so_an_order_that_rescinds_another_is_not_that_order():
    text = ing.to_text(EO16, "pdf", "executive_order", "michigan")
    assert "2009-18" in text                       # the order names the one it rescinds
    states.check_identity(src(citation="Executive Order No. 2016-24", format="pdf"), text, "pdf")
    with pytest.raises(ValueError):
        states.check_identity(src(citation="Executive Order No. 2009-18", format="pdf"), text, "pdf")


def test_identity_does_not_widen_with_a_longer_head_of_text():
    padded = "\n".join(["STATE OF MICHIGAN"] * 80) + "\n" + eo(EO09)
    states.check_identity(src(), padded, "html")                       # the order's own heading, far down
    with pytest.raises(ValueError):
        states.check_identity(src(citation="Executive Order No. 2001-3"), padded, "html")


def test_statute_identity_needs_the_act_citation_in_the_head_of_the_text():
    text = ing.to_text(ACT132, "pdf", "statute", "michigan")
    cite = dict(doc_type="statute", format="pdf", citation="Act 132 of 2017 (MCL 18.221 to 18.229)")
    states.check_identity(src(**cite), text, "pdf")
    with pytest.raises(ValueError):
        states.check_identity(src(**{**cite, "citation": "Act 431 of 1984 (MCL 18.1101 to 18.1594)"}), text, "pdf")


def test_html_notes_say_what_was_removed():
    n = states.hook("michigan", "notes")(src(), "html", eo(EO09))
    assert "Release Date" in n and "removed" in n
