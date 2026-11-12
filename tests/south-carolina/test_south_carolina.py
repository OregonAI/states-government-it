"""South Carolina through the shared seam (src.ingest / src.states): the General Assembly's per-chapter Code of Laws
pages. Fixtures are real bytes fetched on 2026-11-12 through the toolkit Fetcher: Title 30 chapter 2 and Title 11
chapter 53 whole (head, menus, scripts and footer kept), and Title 1 chapter 11 cut after its first sections and
after sections 1-11-430 to 1-11-435 (head and footer kept). PDFs and Word files are shared and need no hook."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "south-carolina"
T30C2 = (FIX / "title-30-chapter-2.html").read_bytes()
T11C53 = (FIX / "title-11-chapter-53.html").read_bytes()
T1C11 = (FIX / "title-1-chapter-11-cut.html").read_bytes()
SC = "south-carolina"


def text(raw):
    return ing.to_text(raw, "html", "statute", SC, None, "www.scstatehouse.gov")


def test_the_state_is_found_by_its_hyphenated_name():
    assert SC in states.modules(refresh=True)


def test_a_chapter_page_opens_with_its_title_chapter_and_article_headings_as_printed():
    lines = text(T30C2).splitlines()
    assert lines[:4] == ["Title 30 - PUBLIC RECORDS", "CHAPTER 2",
                         "Family and Personal Identifying Information Privacy Protection", ""]
    assert lines[4:6] == ["ARTICLE 1", "The Family Privacy Protection Act"]


def test_each_section_is_a_blank_line_then_its_number_and_caption_line_as_printed():
    t = text(T30C2)
    assert ("\n\nSECTION 30-2-20. Privacy policies and procedures required of all state entities.\n"
            "All state agencies, boards, commissions") in t


def test_editor_notes_and_history_lines_stay_as_published():
    t = text(T30C2)
    assert 'redesignated as Article 1, Chapter 2, Title 30."' in t
    assert "HISTORY: 2002 Act No. 225, SECTION 1." in t
    assert t.rstrip().endswith("or local government agency to address the eligible requesting party's request.\"")


def test_no_markup_menu_script_or_footer_leaks_from_the_page():
    for raw in (T30C2, T11C53, T1C11):
        t = text(raw)
        for leak in ("<", ">", "&quot;", "&#39;", "&nbsp;", "\t", "\xa0", "DOCTYPE", "223 Blatt Building",
                     "Code of Laws\nUnannotated", "Staff Portal", "jQuery", "Disclaimer", "Photo Credits"):
            assert leak not in t, leak


def test_a_section_that_is_one_long_paragraph_keeps_its_subsection_lines_separate():
    t = text(T1C11)
    assert "\n\nSECTION 1-11-435. Protection of critical information technology infrastructure and data systems.\n" in t
    assert "\n\nSECTION 1-11-430. Supply and use of telecommunication systems for state Government.\n" in t


def test_a_utf8_page_that_declares_latin1_is_read_as_utf8():
    t = text(T1C11)
    assert "Department of Mental Health\u2014Bull Street Complex;" in t
    assert "\u00e2" not in t and "\ufeff" not in t


def test_a_page_that_is_not_a_chapter_is_refused():
    with pytest.raises(ValueError):
        text(b"<html><body><div id='contentsection'>nothing</div></body></html>")


def seed(citation, **kw):
    return {"id": "x", "jurisdiction": SC, "doc_type": "statute", "citation": citation, "title": "t", **kw}


def test_identity_accepts_the_cited_chapter_and_refuses_another():
    states.check_identity(seed("S.C. Code Title 30, Chapter 2"), text(T30C2), "html")
    with pytest.raises(ValueError):
        states.check_identity(seed("S.C. Code Title 30, Chapter 4"), text(T30C2), "html")
    with pytest.raises(ValueError):
        states.check_identity(seed("S.C. Code Title 11, Chapter 53"), text(T30C2), "html")
    states.check_identity(seed("S.C. Code Title 11, Chapter 53"), text(T11C53), "html")


def test_identity_does_not_claim_other_states_or_other_instrument_types():
    from src.states import hook
    h = hook(SC, "check_identity")
    assert h({**seed("x"), "jurisdiction": "oregon"}, "", "page") is False
    assert h({**seed("x"), "doc_type": "policy"}, "", "PDF") is False


# ---- executive orders: the PDF reader is shared, the heading is printed 'Executive Order No. 2017-08' -----------

EO0817 = (FIX / "executive-order-2017-08-text-alternative.pdf").read_bytes()


def eo_seed(citation):
    return {"id": "x", "jurisdiction": SC, "doc_type": "executive_order", "citation": citation, "title": "t",
            "format": "pdf"}


def test_identity_accepts_the_order_whose_heading_the_file_prints_and_refuses_another_number():
    t = ing.to_text(EO0817, "pdf", "executive_order", SC, None, "governor.sc.gov")
    assert t.startswith("Executive Order No. 2017-08\n")
    states.check_identity(eo_seed("Executive Order No. 2017-08"), t, "pdf")
    with pytest.raises(ValueError):
        states.check_identity(eo_seed("Executive Order No. 2017-09"), t, "pdf")


def test_a_mention_of_the_number_in_the_body_is_not_the_heading():
    body = "Executive Order No. 2017-05\n\nWHEREAS, see Executive Order No. 2017-08 of April 19, 2017.\n"
    with pytest.raises(ValueError):
        states.check_identity(eo_seed("Executive Order No. 2017-08"), body, "pdf")


# ---- printed dates, versions and the scanner text layer (real PDFs, fetched 2026-11-12) ---------------------

def pdf_text(name, doc_type="standard"):
    return ing.to_text((FIX / name).read_bytes(), "pdf", doc_type, SC, None, "www.admin.sc.gov")


def test_effective_date_is_read_from_a_day_month_name_year_label():
    t = pdf_text("scdis-501.pdf")
    assert "effective: 01-Jul-2016" in t
    assert states.effective_date(t, "standard", SC) == "2016-07-01"


def test_a_month_only_effective_label_is_not_made_into_a_date():
    t = pdf_text("mobile-device-protection-policy.pdf", "policy")
    assert "Effective 11/2018" in t
    assert states.effective_date(t, "policy", SC) is None


def test_other_labels_still_go_to_the_shared_reader():
    t = "Version 1.0\n            Effective: August 8, 2018\n"
    assert states.effective_date(t, "standard", SC) == "2018-08-08"


def test_source_version_is_the_cover_version_line_as_printed():
    assert states.source_version(pdf_text("scdis-501.pdf"), "standard", SC, "pdf") == "version: 1.0"
    assert states.source_version("   Version 2.5\n   Effective: October 4, 2019\n", "standard", SC, "pdf") == "Version 2.5"
    t = pdf_text("data-classification-schema-guidelines.pdf", "policy")
    assert states.source_version(t, "policy", SC, "pdf") == "V.2.0 (07.15.15)"


def test_a_version_mentioned_in_the_body_is_not_the_documents_version():
    body = "\n".join(["Title"] * 20) + "\nversion 1.2 of the module\nVersion 3.0\n"
    assert states.source_version(body, "standard", SC, "pdf") == ""


def test_a_document_that_prints_no_version_line_has_none():
    t = pdf_text("mobile-device-protection-policy.pdf", "policy")
    assert states.source_version(t, "policy", SC, "pdf") == ""


def note(src, t, fmt="pdf"):
    return ing.conversion_notes({"jurisdiction": SC, "doc_type": "policy", **src}, fmt, t)


def test_a_scanners_own_ocr_layer_is_declared_unverified_with_what_is_wrong_with_it():
    t = pdf_text("mobile-device-protection-policy.pdf", "policy")
    n = note({"text_layer": "scanner-ocr"}, t)
    assert "scanner" in n and "OCR" in n and "not been checked" in n
    assert "DEPARTMENT o ADMINISTRATION" in t      # the logo junk the note speaks of is really in the text
    assert "harolina Department" in t              # the dropped 'South C'
    assert "OCR" not in note({}, t)


def test_the_month_only_effective_line_is_explained_in_the_notes():
    t = pdf_text("mobile-device-protection-policy.pdf", "policy")
    assert "effective_date is left empty" in note({}, t)


def test_the_printed_dates_and_versions_are_explained_in_the_notes():
    t = pdf_text("scdis-501.pdf")
    n = note({"doc_type": "standard"}, t)
    assert "'effective: 01-Jul-2016'" in n and "source_version is the version line" in n
