"""Hawaii: the Legislature's one-file-per-section HRS pages (data.capitol.hawaii.gov/hrscurrent/) and the ETS library's
WordPress pages. The fixtures are real bytes with their page furniture (title, Previous/Next links, analytics script,
site menus and footer): section 27-43.5 (bracketed number, one Word paragraph broken across source lines), 27G-3 (the
number split across bold runs), 27-46 (a Revision-free section with definitions) and ETS Doc No. 508.01 (a table)."""
from pathlib import Path

import pytest

from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "hawaii"
S2743_5 = (FIX / "hrs-27-43.5.htm").read_bytes()
S27G3 = (FIX / "hrs-27g-3.htm").read_bytes()
S2746 = (FIX / "hrs-27-46.htm").read_bytes()
ETS508 = (FIX / "ets-508-01.html").read_bytes()
HOST = "data.capitol.hawaii.gov"


def stat(raw):
    return states.to_text(raw, "html", "statute", "hawaii", None, HOST)


def src(cite, **kw):
    return {"id": "hi-test", "jurisdiction": "hawaii", "doc_type": "statute", "format": "html",
            "citation": cite, "title": "t", **kw}


def test_the_state_is_found_by_name():
    assert "hawaii" in states.modules(refresh=True)


def test_a_section_page_becomes_one_line_per_paragraph_with_the_source_line_breaks_joined():
    lines = stat(S2743_5).splitlines()
    assert lines[0].startswith("[§27-43.5] Additional duties of the chief information officer relating to security of "
                               "government information. (a) The chief information officer shall provide for periodic "
                               "security audits of all executive branch departments and agencies")
    assert lines[1].startswith("(b) Security audits may include on-site audits")
    assert lines[-1].startswith("(c) This section shall not infringe") and lines[-1].endswith("[L 2013, c 265, §2]")


def test_text_runs_split_across_bold_tags_are_joined_without_inventing_spaces():
    first = stat(S27G3).splitlines()[0]
    assert first.startswith("§27G-3 Access Hawaii committee; establishment; membership; chairperson. (a) There is")


def test_the_page_furniture_is_not_text():
    for raw in (S2743_5, S27G3, S2746):
        text = stat(raw)
        for junk in ("Previous", "Vol01_Ch0001-0042F", "cloudflare", "pageLink", "hrs.css", "&nbsp;"):
            assert junk not in text
        assert "\xa0" not in text and text.endswith("\n") and "\n\n" not in text


def test_a_wordpress_library_page_becomes_its_title_header_and_table_rows():
    text = states.to_text(ETS508, "html", "standard", "hawaii", None, "ets.hawaii.gov")
    lines = text.splitlines()
    assert lines[0] == "ETS DOC NO. 508.01: SECURE DEVICE STANDARDS"
    assert "Policy No. 508.01" in text and "Revision No./Date: September 18, 2018" in text
    assert "Category | Minimum Standard | Comments" in lines
    assert "Device passwords | Desktop/Laptop: 14 characters; Mobile device: 6 characters; All passwords must be unique |" in lines
    assert "Skip to Content" not in text and "Powered by eHawaii.gov" not in text


def test_a_page_that_is_neither_a_section_nor_a_library_page_is_refused():
    with pytest.raises(ValueError):
        stat(b"<html><body><p>Not found</p></body></html>")


@pytest.mark.parametrize("cite,raw", [("Hawaii Revised Statutes section 27-43.5", S2743_5),
                                      ("Hawaii Revised Statutes section 27G-3", S27G3),
                                      ("Hawaii Revised Statutes section 27-46", S2746)])
def test_identity_accepts_the_cited_section_whatever_the_brackets_and_spacing(cite, raw):
    states.check_identity(src(cite), stat(raw))


def test_identity_refuses_a_different_section():
    with pytest.raises(ValueError):
        states.check_identity(src("Hawaii Revised Statutes section 27-43"), stat(S2743_5))
    with pytest.raises(ValueError):          # 27-46 must not match 27-460 or 27-4
        states.check_identity(src("Hawaii Revised Statutes section 27-4"), stat(S2746))


S128B1 = (FIX / "hrs-128b-1.htm").read_bytes()


def test_a_section_of_a_lettered_chapter_with_a_long_catch_line_is_read_and_identified():
    text = stat(S128B1)
    assert text.splitlines()[0].startswith("§128B-1 Cybersecurity, economic, education, and infrastructure security coordinator")
    assert "The coordinator shall be placed within the department of law enforcement." in text
    states.check_identity(src("Hawaii Revised Statutes section 128B-1"), text)


def test_statute_notes_say_the_compilation_predates_the_2026_session_laws():
    note = states.hook("hawaii", "notes")(src("Hawaii Revised Statutes section 27-43"), "html", "x")
    assert "January 2026" in note and "before the 2026 session laws" in note
    assert "not reflected" in note


# ---- sections of chapters outside chapter 27 (owner decision 2026-11-13: a section whose own focus is IT governance) ----
S941_2 = (FIX / "hrs-94-1.2.htm").read_bytes()
S103D1006 = (FIX / "hrs-103d-1006.htm").read_bytes()
S103D215 = (FIX / "hrs-103d-215.htm").read_bytes()


def test_a_section_of_chapter_94_keeps_its_numbered_list_and_drops_the_furniture():
    lines = stat(S941_2).splitlines()
    assert lines[0].startswith("[§94-1.2] The state archivist. The department of accounting and general services shall")
    assert lines[1].startswith("(1) Administer the state archives, records management, and digital archives programs")
    assert any(l.startswith("(3) Issue guidelines and standards, including those applicable to computer hardware") for l in lines)
    assert lines[-1].startswith("(5) Request and obtain an electronic copy") and lines[-1].endswith("[L 2013, c 88, pt of §1]")
    for junk in ("Previous", "Next", "cloudflare", "&nbsp;"):
        assert junk not in stat(S941_2)


def test_a_section_of_the_procurement_code_is_one_document_with_a_letter_in_its_chapter_number():
    lines = stat(S103D1006).splitlines()
    assert lines[0].startswith("§103D-1006 Software development businesses. (a) In any expenditure of public funds for software development")
    assert lines[-1].startswith("(b) This section shall not apply when precluded by federal requirements")
    assert len(lines) == 2


def test_the_procurement_automation_fund_section_is_one_document_with_its_fund_purpose_words():
    lines = stat(S103D215).splitlines()
    assert lines[0].startswith("[§103D-215] State procurement automation system special fund; transaction fee. (a) There is established")
    assert lines[-1].startswith("(b) The state procurement automation special fund shall be expended")
    assert "administration, management, operation, maintenance, and upgrade of the procurement automation system" in lines[-1]
    states.check_identity(src("Hawaii Revised Statutes section 103D-215"), stat(S103D215))


def test_the_identity_check_reads_chapter_numbers_with_a_letter_or_a_decimal_section():
    for cite, text in (("Hawaii Revised Statutes section 103D-1006", stat(S103D1006)),
                       ("Hawaii Revised Statutes section 94-1.2", stat(S941_2))):
        states.check_identity(src(cite), text)
    with pytest.raises(ValueError):
        states.check_identity(src("Hawaii Revised Statutes section 94-1.1"), stat(S941_2), "the page")
