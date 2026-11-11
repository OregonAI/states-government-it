"""Texas: the Legislature's statute pages (tcss.legis.texas.gov). Fixtures are real bytes: the whole of Government
Code chapter 2060, and chapter 2054 cut to its title block plus its last three subchapters (which share a letter)."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states
from src.states import texas

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "texas"
CH2060 = (FIX / "gv-2060-chapter.htm").read_bytes()
CH2054 = (FIX / "gv-2054-subchapter-s.htm").read_bytes()
SRC = {"id": "tx-gv-2060", "jurisdiction": "texas", "doc_type": "statute",
       "citation": "Government Code chapter 2060", "title": "Government Code, Chapter 2060. Interagency Data Transparency Commission"}


def test_the_state_is_found_by_name():
    assert "texas" in states.modules(refresh=True)


def test_a_chapter_page_becomes_the_title_block_then_one_line_per_paragraph():
    text = texas.statute_html_to_text(CH2060)
    lines = text.splitlines()
    assert lines[:4] == ["GOVERNMENT CODE", "TITLE 10. GENERAL GOVERNMENT", "SUBTITLE B. INFORMATION AND PLANNING",
                         "CHAPTER 2060. INTERAGENCY DATA TRANSPARENCY COMMISSION"]
    assert 'Sec. 2060.001. DEFINITION. In this chapter, "commission" means the Interagency Data Transparency Commission.' in lines
    assert "(1) the current public data structure, classification, sharing, and reporting protocols for state agencies; and" in lines
    # the session-law history line under a section is kept, with its bill number
    assert "Added by Acts 2015, 84th Leg., R.S., Ch. 639 (S.B. 1844), Sec. 1, eff. September 1, 2015." in lines
    assert text.rstrip().endswith("to perform the commission's duties.\nAdded by Acts 2015, 84th Leg., R.S., Ch. 639 (S.B. 1844), Sec. 1, eff. September 1, 2015.")


def test_each_section_is_set_off_by_a_blank_line_and_no_markup_or_css_leaks():
    text = texas.statute_html_to_text(CH2060)
    assert "\n\nSec. 2060.002. COMMISSION CREATED." in text
    for leak in ("<", ">", "font-family", "statutes.capitol.texas.gov", "xml:space", "&nbsp;", "&amp;", "﻿", "\t"):
        assert leak not in text


def test_subchapters_with_the_same_letter_are_all_kept_and_set_off():
    text = texas.statute_html_to_text(CH2054)
    heads = [l for l in text.splitlines() if l.startswith("SUBCHAPTER S.")]
    assert heads == ["SUBCHAPTER S. MODERNIZATION OF STATE AGENCY INTERNET WEBSITES AND DIGITAL SERVICES",
                     "SUBCHAPTER S. ARTIFICIAL INTELLIGENCE DIVISION", "SUBCHAPTER S. ARTIFICIAL INTELLIGENCE"]
    assert "\n\nSUBCHAPTER S. ARTIFICIAL INTELLIGENCE DIVISION\n" in text
    assert text.rstrip().endswith("The department shall adopt rules to implement this subchapter.\n"
                                  "Added by Acts 2025, 89th Leg., R.S., Ch. 1148 (S.B. 1964), Sec. 5, eff. September 1, 2025.")


def test_a_page_with_no_statute_body_is_refused_not_committed():
    with pytest.raises(ValueError, match="no statute text"):
        texas.statute_html_to_text(b"<html><body><h1>Not Found</h1></body></html>")


def test_the_shared_flow_reaches_this_reader_for_html_statutes_and_no_other_combination():
    assert ing.to_text(CH2060, "html", "statute", "texas").startswith("GOVERNMENT CODE\n")
    with pytest.raises(ValueError, match="no to_text"):
        ing.to_text(CH2060, "html", "rule", "texas")


def test_identity_accepts_the_cited_chapter_and_refuses_another():
    text = texas.statute_html_to_text(CH2060)
    ing.check_identity(SRC, text)
    with pytest.raises(ValueError, match="not Government Code chapter 2059"):
        ing.check_identity({**SRC, "citation": "Government Code chapter 2059"}, text)
    with pytest.raises(ValueError, match="not Business and Commerce Code chapter 2060"):
        ing.check_identity({**SRC, "citation": "Business and Commerce Code chapter 2060"}, text)


def test_identity_does_not_take_a_chapter_number_from_a_section_cross_reference():
    text = "GOVERNMENT CODE\nCHAPTER 2054. INFORMATION RESOURCES\nSec. 2054.001. x. See Chapter 2059.\n"
    with pytest.raises(ValueError, match="chapter 2059"):
        ing.check_identity({**SRC, "citation": "Government Code chapter 2059"}, text)


def test_notes_describe_the_reading_and_name_the_hook_state():
    n = ing.conversion_notes(SRC, "html", texas.statute_html_to_text(CH2060))
    assert "Legislature" in n and "history" in n
