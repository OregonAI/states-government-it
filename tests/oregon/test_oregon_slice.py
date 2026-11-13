"""Seam: the Oregon ORS slice (`slice: {section_start, section_end_before}`) through src.ingest.to_text and
check_identity. The fixture is real bytes the Legislature served on 2026-11-13 for ORS chapter 291 (the
contents list, sections 291.030 to 291.044 and the last section, 291.990, with the page's own markup and
its closing rule), so the contents entries, the bracketed `renumbered` entries and the page furniture are real."""
import datetime
from pathlib import Path

import pytest

from src import ingest as ing
from src.states import oregon

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "oregon"
CH291 = (FIX / "ors-291-excerpt.html").read_bytes()


def cut(start, end):
    return ing.to_text(CH291, "html", "statute", "oregon", {"section_start": start, "section_end_before": end})


def test_slice_starts_at_the_first_heading_not_at_the_contents_entry():
    t = cut("291.034", "291.035")
    first = t.splitlines()[0]
    assert first.startswith("291.034 Providing technical services involving data processing. The State Chief")
    # the contents list prints the same number and title with no text after it
    assert t.count("291.034 Providing") == 1


def test_slice_includes_every_section_in_the_range_and_excludes_the_next():
    t = cut("291.040", "291.044")
    lines = t.splitlines()
    heads = [l.split(" ")[0] for l in lines if l[:3] == "291" and l[7:8] == " "]
    assert heads == ["291.040", "291.041", "291.042"]
    assert "291.044" not in t and "pay-line" not in t
    assert not t.startswith("291.035") and "291.034" not in t


def test_slice_keeps_the_notes_under_its_last_section_and_the_amendment_history():
    t = cut("291.042", "291.044")
    assert t.splitlines()[-1] == "Note: See note under 291.040."
    assert "[1979 c.740 §3; 1993 c.18 §56; 1995 c.452 §22; 2013 c.481 §1; 2015 c.807 §43]" in t
    assert "(a) May hold copyrights and obtain patents" in t     # subsections stay under the heading


def test_slice_of_the_last_section_drops_the_page_closing_rule():
    full = ing.to_text(CH291, "html", "statute", "oregon", None)
    assert full.rstrip().endswith("_______________")             # the whole-chapter text keeps it, as printed
    with pytest.raises(ValueError, match="does not follow"):      # no end heading: refuse, never guess
        cut("291.990", "291.995")


def test_slice_stops_before_the_bracketed_entry_of_a_renumbered_section():
    t = cut("291.034", "291.035")
    assert "291.035" not in t and "renumbered" not in t
    assert t.splitlines()[-1].endswith("[1965 c.365 §4; 2015 c.807 §40]")


def test_slice_has_no_markup_and_no_blank_lines():
    t = cut("291.030", "291.044")
    assert "<" not in t and "\xa0" not in t and "\n\n" not in t


def test_slice_is_refused_when_a_heading_is_missing_or_not_in_order():
    with pytest.raises(ValueError, match="printed 0 times"):
        cut("291.033", "291.035")
    with pytest.raises(ValueError, match="does not follow"):
        cut("291.042", "291.034")


def test_whole_chapter_text_is_unchanged_without_a_slice():
    full = ing.to_text(CH291, "html", "statute", "oregon", None)
    assert full.count("291.034 Providing technical services involving data processing") == 2   # contents and body


def src(cite, start, end, **kw):
    return {"id": "or-ors-291-034", "doc_type": "statute", "jurisdiction": "oregon", "citation": cite,
            "slice": {"section_start": start, "section_end_before": end}, **kw}


def test_identity_accepts_the_cited_section_and_refuses_another():
    s = src("ORS 291.034", "291.034", "291.035")
    assert oregon.check_identity(s, cut("291.034", "291.035"), "html") is True
    with pytest.raises(ValueError, match="not ORS 291.034"):
        oregon.check_identity(s, cut("291.042", "291.044"), "html")


def test_identity_refuses_a_slice_that_opens_on_a_repealed_or_renumbered_entry():
    s = src("ORS 291.035", "291.035", "291.036")
    with pytest.raises(ValueError, match="repealed or renumbered"):
        oregon.check_identity(s, cut("291.035", "291.036"), "html")


def test_identity_refuses_text_that_prints_a_later_operative_date():
    s = src("ORS 291.034", "291.034", "291.035")
    later = ("291.034 Providing technical services. Text.\n"
             "Note: The amendments to 291.034 by section 5, chapter 1, Oregon Laws 2027, become operative "
             "July 1, 2999.\n")
    with pytest.raises(ValueError, match="2999-07-01"):
        oregon.check_identity(s, later, "html")
    past = later.replace("2999", "2001")
    assert oregon.check_identity(s, past, "html") is True


def test_identity_for_a_range_requires_the_last_cited_section_to_be_the_last_body_heading():
    s = src("ORS 291.030 to 291.034", "291.030", "291.035")
    assert oregon.check_identity(s, cut("291.030", "291.035"), "html") is True
    bad = src("ORS 291.030 to 291.032", "291.030", "291.035")
    with pytest.raises(ValueError, match="not ORS 291.030 to 291.032"):
        oregon.check_identity(bad, cut("291.030", "291.035"), "html")


def test_whole_chapter_entries_are_not_touched_by_the_statute_identity_check():
    whole = {"id": "or-ors-276a", "doc_type": "statute", "jurisdiction": "oregon", "citation": "ORS chapter 276A"}
    assert oregon.check_identity(whole, "Chapter 276A\n", "html") is False


def test_notes_say_a_slice_is_a_slice_and_a_chapter_is_a_chapter():
    s = src("ORS 291.034", "291.034", "291.035")
    n = oregon.notes(s, "html", "")
    assert "291.034" in n and "291.035" in n and "whole chapter" in n and "this document is the whole chapter" not in n
    assert "this document is the whole chapter" in oregon.notes(
        {"doc_type": "statute", "jurisdiction": "oregon"}, "html", "")
