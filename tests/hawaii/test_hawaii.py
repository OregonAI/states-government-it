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
