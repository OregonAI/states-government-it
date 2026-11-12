"""Florida: the Legislature's chapter page (leg.state.fl.us). The fixture is real bytes: the 2026 chapter 282 page with its
page furniture (menus, footer) and the chapter cut to five sections: 282.003, 282.00515, 282.31855 (a footnote marker in the
text and an editors' Note), 282.3186, and 282.319 whose tail carries the Part II heading and its contents list."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states
from src.states import florida

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "florida"
CH282 = (FIX / "ch-282-cut.html").read_bytes()
SRC = {"id": "fl-st-282", "jurisdiction": "florida", "doc_type": "statute",
       "citation": "Chapter 282, Florida Statutes", "title": "Chapter 282. Communications and Data Processing"}


def test_the_state_is_found_by_name():
    assert "florida" in states.modules(refresh=True)


def test_a_chapter_page_becomes_the_edition_the_title_and_chapter_lines_then_one_line_per_paragraph():
    text = florida.statute_html_to_text(CH282)
    lines = text.splitlines()
    assert [l for l in lines if l][:4] == ["The 2026 Florida Statutes", "Title XIX PUBLIC BUSINESS",
                         "CHAPTER 282 COMMUNICATIONS AND DATA PROCESSING", "PART I INFORMATION TECHNOLOGY MANAGEMENT"]
    assert ("282.003 Short title. — This part may be cited as the “Information Technology Management Act.”"
            in lines)
    assert "History. — s. 8, ch. 87-137; s. 1, ch. 92-98; s. 93, ch. 92-142; s. 4, ch. 96-390; s. 7, ch. 97-286; s. 45, ch. 99-13; s. 4, ch. 2008-116; s. 5, ch. 2009-80; s. 7, ch. 2019-118." in lines


def test_subsections_paragraphs_and_subparagraphs_each_keep_their_number_and_their_own_line():
    lines = florida.statute_html_to_text(CH282).splitlines()
    assert any(l.startswith("(1) ") for l in lines)
    assert any(l.startswith("(a) ") for l in lines)
    assert any(l.startswith("1. ") for l in lines)


def test_the_contents_lists_are_page_furniture_and_do_not_repeat_the_sections():
    text = florida.statute_html_to_text(CH282)
    assert text.count("282.003 Short title.") == 1
    assert "(ss. 282.003-282.319)" not in text


def test_a_footnote_marker_and_the_editors_note_it_points_to_are_kept():
    text = florida.statute_html_to_text(CH282)
    assert "detection [1]of, prevention [1]of" in text
    assert "[1] Note. — The word “of” was inserted by the editors to conform to context." in text


def test_later_part_headings_are_kept_in_their_place():
    lines = florida.statute_html_to_text(CH282).splitlines()
    assert "PART II ACCESSIBILITY OF INFORMATION AND TECHNOLOGY" in lines


def test_each_section_is_set_off_by_a_blank_line_and_no_markup_or_furniture_leaks():
    text = florida.statute_html_to_text(CH282)
    assert "\n\n282.00515 " in text
    for leak in ("<", ">", "xml:space", "&#x", "&amp;", " ", "Online Sunshine", "Privacy Statement", "Copyright",
                 "Search Statutes", "\t"):
        assert leak not in text


def test_a_page_with_no_statute_body_is_refused_not_committed():
    with pytest.raises(ValueError, match="no statute text"):
        florida.statute_html_to_text(b"<html><body><h1>Not Found</h1></body></html>")


def test_the_shared_flow_reaches_this_reader_for_html_statutes_and_no_other_combination():
    assert ing.to_text(CH282, "html", "statute", "florida").startswith("The 2026 Florida Statutes\n")
    with pytest.raises(ValueError, match="no to_text"):
        ing.to_text(CH282, "html", "rule", "florida")


def test_the_identity_check_accepts_the_cited_chapter_and_refuses_another():
    text = florida.statute_html_to_text(CH282)
    assert florida.check_identity(SRC, text, "") is True
    with pytest.raises(ValueError, match="not Chapter 119"):
        florida.check_identity({**SRC, "citation": "Chapter 119, Florida Statutes"}, text, "")
    assert florida.check_identity({**SRC, "doc_type": "policy"}, "x", "") is False


def test_the_version_is_the_edition_the_page_prints():
    text = florida.statute_html_to_text(CH282)
    assert florida.source_version(text, "statute", "html") == "2026 Florida Statutes"
    assert florida.source_version("x", "policy", "pdf") is None


EO = {"id": "fl-eo-22-216", "jurisdiction": "florida", "doc_type": "executive_order", "citation": "Executive Order 22-216",
      "title": "Strengthening Florida Cybersecurity Against Foreign Adversaries",
      "identity_text": "EXECUTIVE ORDER NUMBER 22-216"}
EO_PAGE_ONE = "STATE OF FLORIDA\nOFFICE OF THE GOVERNOR\nEXECUTIVE ORDER NUMBER 22-216\n(Strengthening Florida Cybersecurity Against Foreign Adversaries)\n"


def test_an_order_is_identified_by_the_number_line_the_order_prints_not_by_the_citations_wording():
    # the shared check wants "Executive Order 22-216"; Florida's orders print "EXECUTIVE ORDER NUMBER 22-216"
    assert florida.check_identity(EO, EO_PAGE_ONE, "PDF") is True
    with pytest.raises(ValueError, match="not the cited instrument"):
        florida.check_identity(EO, EO_PAGE_ONE.replace("22-216", "22-217"), "PDF")
    with pytest.raises(ValueError, match="not the cited instrument"):
        florida.check_identity({k: v for k, v in EO.items() if k != "identity_text"}, EO_PAGE_ONE, "PDF")
