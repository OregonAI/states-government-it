"""Missouri through the shared seam (src.ingest / src.states): the Revisor of Statutes' one-section pages and the
Secretary of State's executive-order pages. Fixtures are real bytes fetched through the toolkit Fetcher on 2026-11-12,
whole, with the pages' menus, search form, scripts and footers: RSMo 37.110 and 37.1300 (a section the page marks with
an asterisk note), 407.1500 (a section of subsections, definitions and a soft-hyphen separator) and Executive Order
26-02 (a heading, whereas clauses, nested lettered lists and a scan link)."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "missouri"
S110 = (FIX / "rsmo-37-110.html").read_bytes()
S1300 = (FIX / "rsmo-37-1300.html").read_bytes()
S4071500 = (FIX / "rsmo-407-1500.html").read_bytes()
EO2 = (FIX / "eo-26-02.html").read_bytes()
EO0326 = (FIX / "eo-03-26.html").read_bytes()
MO = "missouri"


def text(raw, doc_type):
    return ing.to_text(raw, "html", doc_type, MO, None, "revisor.mo.gov" if doc_type == "statute" else "www.sos.mo.gov")


def src(doc_type, citation, title="t", **kw):
    return {"id": "mo-x", "jurisdiction": MO, "doc_type": doc_type, "citation": citation, "title": title, **kw}


def test_the_state_is_found_by_name():
    assert MO in states.modules(refresh=True)


# ---- statutes: one section per page ---------------------------------------------------------

def test_a_section_page_is_title_chapter_effective_line_the_section_its_history_and_the_end_line():
    lines = text(S110, "statute").splitlines()
    assert lines[:3] == ["Title IV EXECUTIVE BRANCH", "Chapter 37", "Effective - 28 Aug 2014, 2 histories"]
    assert lines[3].startswith("37.110. Information technology services division established. — The commissioner")
    assert lines[3].endswith("without the approval of this unit.")
    assert lines[4] == "(L. 1965 p. 141 § 5, A.L. 2014 H.B. 1299 Revision)"
    assert lines[5] == "---- end of effective 28 Aug 2014 ----"
    assert len(lines) == 6


def test_no_page_furniture_markup_or_soft_hyphen_leaks():
    for raw in (S110, S1300, S4071500):
        t = text(raw, "statute")
        for leak in ("<", ">", "Revisor of Missouri", "Do search", "ctl00", "Recent Sections", "\xad", "bookmark",
                     "All versions", "All rights reserved", "\t", "\xa0"):
            assert leak not in t
        assert "\n\n" not in t


def test_subsections_and_definitions_are_one_line_each_and_the_footnote_separator_is_dropped():
    t = text(S4071500, "statute")
    assert '(8) "Person", any individual, corporation, business trust, estate, trust, partnership' in t
    assert "governmental agency, governmental instrumentality, public corporation" in t
    assert "\n(L. 2009 H.B. 62)\n" in t
    assert "--------\n" not in t.replace("---- end of effective", "")


def test_an_asterisk_note_the_page_prints_stays():
    t = text(S1300, "statute")
    assert "*Section 37.1330 does not exist." in t
    assert t.splitlines()[2] == "Effective - 28 Aug 2026"


def test_the_robot_page_and_a_page_that_is_not_a_section_are_refused():
    bot = b"<html><body><p>Chapter, Title, etc. that does NOT exist.</p><p>The system thinks you are a roBOT</p></body></html>"
    with pytest.raises(ValueError, match="no statute text"):
        text(bot, "statute")


def test_identity_is_the_section_number_the_seed_cites():
    t = text(S110, "statute")
    ing.check_identity(src("statute", "Section 37.110, RSMo"), t)
    with pytest.raises(ValueError, match="not Section 37.920, RSMo"):
        ing.check_identity(src("statute", "Section 37.920, RSMo"), t)
    with pytest.raises(ValueError, match="not Section 37.11, RSMo"):         # a prefix of the number is not it
        ing.check_identity(src("statute", "Section 37.11, RSMo"), t)


def test_the_notes_describe_how_the_section_page_was_read():
    n = ing.conversion_notes(src("statute", "Section 37.110, RSMo"), "html", text(S110, "statute"))
    assert "Revisor of Statutes" in n and "one section" in n and "soft" in n


# ---- executive orders: the Secretary of State's text page --------------------------------------

def test_an_executive_order_page_is_the_heading_then_its_paragraphs_and_lists_as_printed():
    t = text(EO2, "executive_order")
    lines = t.splitlines()
    assert lines[0] == "EXECUTIVE ORDER 26-02"
    assert lines[1].startswith("WHEREAS, Artificial Intelligence (AI) represents a transformative")
    assert any(l.strip().startswith("a. Evaluate the AI Education and Training Ecosystem:") for l in lines)
    assert "MIKE KEHOE" in lines and "SECRETARY OF STATE" in lines
    assert lines[-1] == "DENNY HOSKINS" or lines[-1] == "SECRETARY OF STATE"
    for leak in ("Scan of Executive Order", "Business Search", "Internet Privacy Policy", "Skip to main content", "<"):
        assert leak not in t


def test_an_executive_order_identity_is_the_orders_own_heading_not_a_mention():
    t = text(EO2, "executive_order")
    ing.check_identity(src("executive_order", "Executive Order 26-02"), t)
    with pytest.raises(ValueError, match="26-03"):
        ing.check_identity(src("executive_order", "Executive Order 26-03"), t)
    mention = "EXECUTIVE ORDER 26-09\nWHEREAS this order extends Executive Order 26-02 until\n"
    with pytest.raises(ValueError, match="26-02"):
        ing.check_identity(src("executive_order", "Executive Order 26-02"), mention)


def test_a_page_with_no_order_text_is_refused():
    with pytest.raises(ValueError, match="no executive order text"):
        text(b"<html><body><div id='main'><p>Page not found</p></div></body></html>", "executive_order")


def test_the_notes_describe_how_the_order_page_was_read():
    n = ing.conversion_notes(src("executive_order", "Executive Order 26-02"), "html", text(EO2, "executive_order"))
    assert "Secretary of State" in n and "scan" in n.lower()


def test_an_older_order_page_has_its_heading_on_two_lines_and_ends_at_the_pdf_link():
    t = text(EO0326, "executive_order")
    lines = t.splitlines()
    assert lines[0] == "EXECUTIVE ORDER 03-26"                   # <h1>EXECUTIVE ORDER<br />03-26</h1>
    assert lines[1].startswith("WHEREAS, the State of Missouri recognizes the critical importance of technology")
    assert "Bob Holden" in lines and "Matt Blunt" in lines and lines[-1] == "Secretary of State"
    assert "State of Information Technology in Missouri" in t        # an underlined span stays inside its paragraph
    for leak in (".pdf version", "Business Search", "executiveorderssearch", "<"):
        assert leak not in t
    ing.check_identity(src("executive_order", "Executive Order 03-26"), t)
