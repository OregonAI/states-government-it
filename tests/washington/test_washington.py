"""Seam: src.ingest for Washington: RCW pages (app.leg.wa.gov), the identity of its statutes and orders.
Fixtures are real pages the Legislature served on 2026-11-10, trimmed to the page body."""
from pathlib import Path

import pytest

from src import ingest as ing

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "washington"

# ---- Washington RCW pages (app.leg.wa.gov) ----------------------------------------------
# Fixtures are real pages the Legislature served on 2026-11-10, trimmed to the page body.
RCW_CH = (FIX / "rcw-40-26-chapter.html").read_bytes()
RCW_SEC = (FIX / "rcw-39-26-340-section.html").read_bytes()


def test_rcw_chapter_text_has_chapter_title_then_each_section_in_source_order():
    t = ing.to_text(RCW_CH, "html", "statute", "washington")
    lines = t.splitlines()
    assert lines[0] == "Chapter 40.26 RCW"
    assert lines[1] == "BIOMETRIC IDENTIFIERS"
    assert lines.index("RCW 40.26.010") < lines.index("RCW 40.26.020")
    assert lines[lines.index("RCW 40.26.010") + 1] == "Finding."
    assert ("The legislature finds that the collection and use of personal information has been "
            "a practice of virtually all state agencies and programs.") in t


def test_rcw_chapter_text_keeps_history_and_notes_and_drops_page_furniture():
    t = ing.to_text(RCW_CH, "html", "statute", "washington")
    assert "[ 2017 c 306 s 1.]" in t               # the session-law history line of 40.26.010
    assert "NOTES:" in t and "Effective date—2017 2nd sp.s. c 1:" in t
    assert "<" not in t and "&amp;" not in t and "\xa0" not in t
    for furniture in ("PDF", "Chapter listing", "Sections"):
        assert furniture not in t.splitlines()


def test_rcw_section_page_text_is_citation_caption_body_history():
    t = ing.to_text(RCW_SEC, "html", "statute", "washington")
    lines = t.splitlines()
    assert lines[0] == "RCW 39.26.340"
    assert lines[1] == "Data-sharing agreements—When required."
    assert lines[2].startswith("(1) Before an agency shares with a contractor category 3 or higher data")
    assert "RCW 43.105.054" in lines[2]              # link text kept inside the sentence, spaces squashed
    assert lines[-1] == "[ 2021 c 291 s 5.]"


def test_rcw_page_without_a_content_region_is_refused():
    with pytest.raises(ValueError, match="content region"):
        ing.to_text(b"<html><body><p>Not found</p></body></html>", "html", "statute", "washington")


# ---- identity of Washington statutes and executive orders; no chapter-wide effective date ----

WA_CH = {"id": "wa-rcw-40-26", "doc_type": "statute", "jurisdiction": "washington",
         "citation": "RCW chapter 40.26", "title": "Chapter 40.26 RCW - Biometric identifiers"}
WA_SEC = dict(WA_CH, id="wa-rcw-39-26-340", citation="RCW 39.26.340", title="RCW 39.26.340 - x")
WA_EO = {"id": "wa-eo-24-01", "doc_type": "executive_order", "jurisdiction": "washington",
         "citation": "Executive Order No. 24-01", "title": "Artificial Intelligence"}


def test_wa_statute_chapter_page_must_be_the_cited_chapter():
    ing.check_identity(WA_CH, ing.to_text(RCW_CH, "html", "statute", "washington"))
    with pytest.raises(ValueError, match="not RCW chapter 43.105"):
        ing.check_identity(dict(WA_CH, citation="RCW chapter 43.105"),
                           ing.to_text(RCW_CH, "html", "statute", "washington"))


def test_wa_statute_section_page_must_be_the_cited_section():
    ing.check_identity(WA_SEC, ing.to_text(RCW_SEC, "html", "statute", "washington"))
    with pytest.raises(ValueError, match="not RCW 42.56.590"):
        ing.check_identity(dict(WA_SEC, citation="RCW 42.56.590"),
                           ing.to_text(RCW_SEC, "html", "statute", "washington"))


def test_wa_statute_citation_that_is_a_truncation_of_the_real_section_is_refused():
    text = ing.to_text(RCW_SEC, "html", "statute", "washington")     # opens "RCW 39.26.340"
    with pytest.raises(ValueError, match="not RCW 39.26.34"):
        ing.check_identity(dict(WA_SEC, citation="RCW 39.26.34"), text)
    chapter = ing.to_text(RCW_CH, "html", "statute", "washington")    # opens "Chapter 40.26 RCW"
    with pytest.raises(ValueError, match="not RCW chapter 40.2"):
        ing.check_identity(dict(WA_CH, citation="RCW chapter 40.2"), chapter)


def test_executive_order_must_print_its_own_number():
    ing.check_identity(WA_EO, "EXECUTIVE ORDER 24-01\nARTIFICIAL INTELLIGENCE\n")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity(WA_EO, "EXECUTIVE ORDER 24-02\nWSP INVESTIGATIONS\n")


def test_statute_gets_no_effective_date_from_a_session_law_note():
    # 40.26's NOTES print "Effective date—2017 2nd sp.s. c 1: ... [July 23, 2017]", the date of one
    # amending act, not of the chapter.
    text = ing.to_text(RCW_CH, "html", "statute", "washington")
    assert "[July 23, 2017]" in text
    assert ing.effective_date(text, "statute") is None
    assert ing.effective_date("Effective Date: March 5, 2020\n", "policy") == "2020-03-05"


def test_wa_statute_conversion_notes_describe_the_rcw_page_not_the_ors_page():
    notes = ing.conversion_notes(WA_CH, "html", "")
    assert "RCW" in notes and "section list" in notes and "history" in notes
    assert "whole chapter as one page" not in notes      # that sentence is about ORS


def test_rcw_text_stops_before_the_page_footer():
    for page in (RCW_CH, RCW_SEC):
        t = ing.to_text(page, "html", "statute", "washington")
        assert "Legislative Hotline" not in t and "TTY" not in t and "Disclaimer" not in t
