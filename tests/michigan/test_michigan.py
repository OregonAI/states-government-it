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
ACT116 = (FIX / "mcl-act-116-of-1992.pdf").read_bytes()        # Records Reproduction Act: 24.401 to 24.406 with 24.402a, a page break inside 24.404
SEC2503 = (FIX / "mcl-333-2503.html").read_bytes()             # one MCL section page, site navigation included
SEC2505 = (FIX / "mcl-333-2505.html").read_bytes()
EO9413 = (FIX / "eo-1994-13-computer-programming.html").read_bytes()


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


# ---- statutes: a slice of an act PDF, and one MCL section page ------------------------------

def slice_(start, end):
    return {"section_start": start, "section_end_before": end}


def act116(start, end):
    return ing.to_text(ACT116, "pdf", "statute", "michigan", slice_(start, end))


def sec(raw):
    return ing.to_text(raw, "html", "statute", "michigan")


def stat(citation, **kw):
    return src(doc_type="statute", format=kw.pop("format", "html"), citation=citation, **kw)


def test_slice_starts_at_the_first_heading_not_the_act_title_block():
    t = act116("24.401", "24.402a")
    assert t.splitlines()[0].strip() == "24.401 Short title; definitions."
    assert "AN ACT to designate" not in t and "The People of the State of Michigan enact" not in t


def test_slice_includes_every_section_in_range_and_excludes_the_end_section_and_the_next():
    t = act116("24.401", "24.402a")
    assert "24.402 Reproduction of record by governmental entity" in t
    assert "(5) The department may enter into a pilot agreement" in t     # the last paragraph of 24.402
    assert "Admin Rule: R 24.401 et seq." in t
    assert "24.402a" not in t and "construction document" not in t
    assert "24.403" not in t and "24.404" not in t


def test_slice_of_one_section_keeps_the_text_after_a_page_break_and_drops_page_furniture():
    t = act116("24.404", "24.405")
    lines = t.splitlines()
    assert lines[0].strip() == "24.404 Proposed technical standard."
    assert any(l.strip().startswith("(2) Before submitting a proposed technical standard") for l in lines)
    assert any(l.strip().startswith("(3) Proposed and final technical standards shall be published") for l in lines)
    assert "24.405" not in t and "Optical disc" not in t
    for gone in ("Rendered", "Page 3 of 4", "Courtesy of legislature.mi.gov", "Complete Through PA"):
        assert gone not in t


def test_slice_refuses_a_heading_the_act_does_not_print_or_an_end_that_does_not_follow():
    with pytest.raises(ValueError):
        act116("24.499", "24.405")
    with pytest.raises(ValueError):
        act116("24.404", "24.499")
    with pytest.raises(ValueError):
        act116("24.404", "24.402")        # the end section precedes the start


def test_slice_identity_needs_the_cited_first_and_last_section():
    t = act116("24.401", "24.402a")
    cite = "MCL 24.401 to 24.402 (Records Reproduction Act, Act 116 of 1992)"
    s = stat(cite, format="pdf", slice=slice_("24.401", "24.402a"))
    states.check_identity(s, t, "pdf")
    with pytest.raises(ValueError):
        states.check_identity({**s, "citation": "MCL 24.401 to 24.404"}, t, "pdf")   # the slice stops at 24.402
    with pytest.raises(ValueError):
        states.check_identity({**s, "slice": slice_("24.402", "24.402a")}, t, "pdf")
    one = act116("24.404", "24.405")
    states.check_identity(stat("MCL 24.404 (Records Reproduction Act)", format="pdf", slice=slice_("24.404", "24.405")), one, "pdf")


def test_identity_refuses_text_that_prints_an_amendment_taking_effect_after_today():
    future = "24.404 Proposed technical standard.\nSec. 4.\n(1) x\nHistory: Am. 2099, Act 1, Eff. Jan. 1, 2099\n"
    s = stat("MCL 24.404", format="pdf", slice=slice_("24.404", "24.405"))
    with pytest.raises(ValueError):
        states.check_identity(s, future, "pdf")


def test_section_page_text_is_the_section_alone_without_site_navigation():
    t = sec(SEC2503)
    lines = t.splitlines()
    assert lines[:2] == ["PUBLIC HEALTH CODE (EXCERPT)", "Act 368 of 1978"]
    assert lines[2].startswith("333.2503 Health information technology commission; creation;")
    assert lines[3] == "Sec. 2503."
    assert any(l.startswith("(1) The health information technology commission is created within the department") for l in lines)
    assert any(l.startswith("History: Add. 2006, Act 137, Imd. Eff. May 12, 2006") for l in lines)
    assert any(l.startswith("Compiler's Notes:") and "E.R.O. No. 2025-2" in l for l in lines)
    for gone in ("Skip to content", "Previous Section", "Next Section", "Download Section", "Senate adjourned",
                 "Acceptable Use Policy", "368-1978-2", "<", "&nbsp;", "\xa0"):
        assert gone not in t
    assert "333.2505" not in t


def test_section_page_identity_is_the_cited_section_and_not_a_repealed_one():
    t = sec(SEC2505)
    states.check_identity(stat("MCL 333.2505 (Public Health Code)"), t, "html")
    with pytest.raises(ValueError):
        states.check_identity(stat("MCL 333.2503"), t, "html")
    repealed = t.replace("333.2505 Commission; duties; strategic plan.", "333.2505 Repealed. 2020, Act 1.")
    with pytest.raises(ValueError):
        states.check_identity(stat("MCL 333.2505"), repealed, "html")


def test_section_page_that_is_not_a_section_page_is_refused():
    with pytest.raises(ValueError):
        ing.to_text(b"<html><body><main>nothing here</main></body></html>", "html", "statute", "michigan")


def test_executive_order_1994_13_is_read_by_its_own_heading():
    t = eo(EO9413)
    assert t.splitlines()[:2] == ["EXECUTIVE ORDER", "No. 1994 - 13"]
    states.check_identity(src(citation="Executive Order No. 1994-13"), t, "html")
    with pytest.raises(ValueError):
        states.check_identity(src(citation="Executive Order No. 1994-15"), t, "html")


def test_extra_notes_describe_the_slice_and_carry_the_currency_note():
    s = stat("MCL 24.404", format="pdf", slice=slice_("24.404", "24.405"), currency_note="checked today")
    n = states.hook("michigan", "extra_notes")(s, "pdf", "", None, "")
    assert "24.404" in n and "24.405" in n and "page furniture" in n and n.endswith("checked today")
    assert states.hook("michigan", "extra_notes")(stat("MCL 333.2503"), "html", "", None, "") == ""
