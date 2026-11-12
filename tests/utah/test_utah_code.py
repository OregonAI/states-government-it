"""Seam: src.states.to_text / check_identity for Utah Code chapters, the Legislature's per-chapter XML
download (le.utah.gov/xcode/Title<t>/Chapter<n>/C<t>-<n>_<version>.xml).

Fixtures are real bytes: the whole of chapter 63C-27 (carries a sunset marker) and Part 11 of chapter
63A-16 (whole <part>, wrapped in the chapter's own opening tags and a closing tag)."""
from pathlib import Path

import pytest

from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "utah"
CYBER_COMMISSION = (FIX / "c63c-27-cybersecurity-commission.xml").read_bytes()
CYBER_CENTER = (FIX / "c63a-16-part-11-cyber-center.xml").read_bytes()


def text(raw):
    return states.to_text(raw, "xml", "statute", "utah")


def test_chapter_opens_with_number_title_effective_date_and_sunset():
    lines = text(CYBER_COMMISSION).splitlines()
    assert lines[0] == "Chapter 63C-27 Cybersecurity Commission"
    assert lines[1] == "Effective 5/4/2022"
    assert lines[2] == "Repeal date 7/1/2032 (Section 63I-1-263)"


def test_sections_nest_subsections_by_depth_and_inline_cross_references_read_as_text():
    out = text(CYBER_CENTER)
    assert "Part 63A-16-11 Utah Cyber Center" in out
    assert "63A-16-1101 Definitions." in out
    assert '  (1) "Cyber Center" means the Utah Cyber Center created in Section 63A-16-1102.' in out
    assert '  (2) "Data breach" means the unauthorized access, acquisition, disclosure, loss of access, or destruction of:' in out
    assert "    (a) personal data affecting 500 or more individuals; or" in out


def test_amendment_history_is_kept_after_the_section():
    out = text(CYBER_CENTER).splitlines()
    i = out.index("63A-16-1101 Definitions.")
    assert "Amended by Chapter 60, 2026 General Session" in out[i + 1:i + 40]
    assert not any("modchap" in line or "<" in line for line in out)


def test_every_section_of_the_source_is_present():
    out = text(CYBER_COMMISSION)
    for n in ("101", "201", "202", "203", "204", "205", "206"):
        assert f"63C-27-{n} " in out


def test_unknown_markup_is_refused_not_dropped():
    bad = CYBER_COMMISSION.replace(b"<tab/>", b"<table/>", 1)
    with pytest.raises(ValueError, match="table"):
        text(bad)


def test_a_page_that_is_not_the_chapter_xml_is_refused():
    with pytest.raises(ValueError):
        text(b"<html><body>Utah Code</body></html>")


SRC = {"id": "ut-code-63c-27", "doc_type": "statute", "jurisdiction": "utah",
       "citation": "Utah Code chapter 63C-27", "title": "Cybersecurity Commission"}


def test_identity_accepts_the_cited_chapter_and_refuses_another():
    states.check_identity(SRC, text(CYBER_COMMISSION), "xml")
    with pytest.raises(ValueError, match="63A-16"):
        states.check_identity({**SRC, "citation": "Utah Code chapter 63A-16"}, text(CYBER_COMMISSION), "xml")


FUTURE = (FIX / "c63a-16-section-216-future-effective.xml").read_bytes()


def test_a_section_that_takes_effect_later_says_so_under_its_heading():
    lines = text(FUTURE).splitlines()
    i = lines.index("63A-16-216 Government websites and applications.")
    assert lines[i + 1] == "Effective 1/1/2027"


LEGAL_PERSONHOOD = (FIX / "c63g-32-legal-personhood-no-parts.xml").read_bytes()  # whole chapter file; sections sit directly in <chapter>


def test_sections_that_are_direct_children_of_the_chapter_are_rendered():
    out = text(LEGAL_PERSONHOOD)
    assert "63G-32-101 Definitions." in out
    assert "63G-32-102 " in out
    assert "artificial intelligence" in out


def test_a_chapter_that_renders_no_section_is_refused():
    with pytest.raises(ValueError, match="no section"):
        text(b'<chapter number="63G-32"><effdate>5/1/2024</effdate><catchline>Legal Personhood</catchline></chapter>')
