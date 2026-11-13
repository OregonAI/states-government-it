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


# ---- section slices of a chapter page: {section_start, section_end_before} (owner decision 2026-11-13) ----------------
# Fixtures are real bytes fetched on 2026-11-13 through the toolkit Fetcher: Title 26 chapter 6 and Title 30 chapter 1
# whole, Title 11 chapter 35 cut to its head, sections 11-35-810 to 11-35-840 and its footer.
T11C35 = (FIX / "title-11-chapter-35-cut.html").read_bytes()
T26C6 = (FIX / "title-26-chapter-6.html").read_bytes()
T30C1 = (FIX / "title-30-chapter-1.html").read_bytes()


def cut(raw, start, end, host="www.scstatehouse.gov"):
    return ing.to_text(raw, "html", "statute", SC, {"section_start": start, "section_end_before": end}, host)


def headings(t):
    return [l.split(".")[0] for l in t.splitlines() if l.startswith("SECTION ")]


def test_a_slice_starts_at_the_first_section_heading_not_the_title_line():
    t = cut(T11C35, "11-35-820", "11-35-830")
    assert t.startswith("SECTION 11-35-820. Creation of Information Technology Management Office.\nThere is created")


def test_a_one_section_slice_excludes_the_next_section_and_the_previous_one():
    t = cut(T11C35, "11-35-820", "11-35-830")
    assert headings(t) == ["SECTION 11-35-820"]
    assert "Materials Management" not in t.replace("Information Technology management Office", "")
    assert "State Engineer" not in t and "Subarticle" not in t


def test_a_slice_keeps_the_history_and_amendment_notes_under_its_last_section():
    t = cut(T11C35, "11-35-820", "11-35-830")
    assert "HISTORY: 1981 Act No. 148, SECTION 1; 1997 Act No. 153" in t
    assert t.rstrip().endswith("by specific reference to the Information Technology management Office\" at the end.")


def test_a_range_slice_includes_every_section_in_range_and_stops_before_the_end_section():
    t = cut(T26C6, "26-6-170", "26-6-210")
    assert headings(t) == ["SECTION 26-6-170", "SECTION 26-6-180", "SECTION 26-6-190", "SECTION 26-6-195"]
    assert "Applicability of Computer Crime Act" not in t and "26-6-160" not in t.split("\n")[0]
    assert t.rstrip().endswith("effective July 1, 2015.")


def test_a_one_section_slice_of_the_records_chapter_starts_at_30_1_90_and_stops_before_30_1_100():
    t = cut(T30C1, "30-1-90", "30-1-100")
    assert headings(t) == ["SECTION 30-1-90"]
    assert t.startswith("SECTION 30-1-90")
    assert "stored electronically" in t
    assert "Records management program" not in t and "30-1-100" not in t
    states.check_identity(slice_seed("S.C. Code § 30-1-90", "30-1-90", "30-1-100"), t, "html")
    with pytest.raises(ValueError):
        states.check_identity(slice_seed("S.C. Code § 30-1-80", "30-1-90", "30-1-100"), t, "html")


def test_a_slice_carries_no_page_furniture():
    for t in (cut(T11C35, "11-35-820", "11-35-830"), cut(T26C6, "26-6-170", "26-6-210"),
              cut(T30C1, "30-1-80", "30-1-100")):
        for leak in ("<", ">", "&quot;", "&#39;", "&nbsp;", "\t", "DOCTYPE", "223 Blatt Building", "Staff Portal",
                     "jQuery", "Disclaimer", "Photo Credits", "Title 26 - ", "CHAPTER "):
            assert leak not in t, leak


def test_a_slice_that_ends_at_the_end_of_the_chapter_page_needs_the_end_section_to_exist():
    with pytest.raises(ValueError):
        cut(T26C6, "26-6-170", "26-6-999")
    with pytest.raises(ValueError):
        cut(T26C6, "26-6-999", "26-6-210")


def test_a_slice_whose_end_section_comes_before_its_start_is_refused():
    with pytest.raises(ValueError):
        cut(T26C6, "26-6-190", "26-6-170")


def test_a_slice_from_another_chapter_than_the_page_is_refused():
    with pytest.raises(ValueError):
        cut(T26C6, "30-1-80", "30-1-100")


def test_a_trailing_subarticle_heading_before_the_end_section_does_not_ride_along():
    t = cut(T11C35, "11-35-810", "11-35-820")
    assert headings(t) == ["SECTION 11-35-810"]
    t2 = ing.to_text(T11C35.replace(b"<span style=\"font-weight: bold;\"> SECTION 11-35-830.",
                                    b"<div style=\"text-align: center;\">Subarticle 6</div>\n<div style=\"text-align: center;\">Other Offices</div><br />\n<span style=\"font-weight: bold;\"> SECTION 11-35-830."),
                     "html", "statute", SC, {"section_start": "11-35-820", "section_end_before": "11-35-830"}, None)
    assert "Subarticle 6" not in t2 and "Other Offices" not in t2


def slice_seed(citation, start, end):
    return seed(citation, format="html", slice={"section_start": start, "section_end_before": end})


def test_identity_accepts_the_cited_sections_and_refuses_another_slice():
    t = cut(T26C6, "26-6-170", "26-6-210")
    states.check_identity(slice_seed("S.C. Code §§ 26-6-170 to 26-6-195", "26-6-170", "26-6-210"), t, "html")
    with pytest.raises(ValueError):
        states.check_identity(slice_seed("S.C. Code §§ 26-6-170 to 26-6-180", "26-6-170", "26-6-190"), t, "html")
    with pytest.raises(ValueError):
        states.check_identity(slice_seed("S.C. Code §§ 26-6-180 to 26-6-195", "26-6-180", "26-6-210"), t, "html")
    one = cut(T11C35, "11-35-820", "11-35-830")
    states.check_identity(slice_seed("S.C. Code § 11-35-820", "11-35-820", "11-35-830"), one, "html")
    with pytest.raises(ValueError):
        states.check_identity(slice_seed("S.C. Code § 11-35-810", "11-35-810", "11-35-830"), one, "html")


def test_identity_refuses_a_single_section_that_is_printed_as_repealed():
    t = "SECTION 11-35-1580. Repealed.\nHISTORY: Former Section, titled Information technology procurements, had the following history: 1997 Act No. 153, SECTION 1. Repealed by 2019 Act No. 41, SECTION 77, eff May 13, 2019.\n"
    with pytest.raises(ValueError):
        states.check_identity(slice_seed("S.C. Code § 11-35-1580", "11-35-1580", "11-35-1590"), t, "html")


def test_identity_refuses_a_slice_with_an_amendment_not_yet_in_effect():
    t = ("SECTION 30-2-60. Removal of public records.\nBody.\nSection effective January 1, 2099.\n"
         "HISTORY: 2026 Act No. 214, SECTION 1.\n")
    with pytest.raises(ValueError):
        states.check_identity(slice_seed("S.C. Code § 30-2-60", "30-2-60", "30-2-70"), t, "html")
    past = t.replace("January 1, 2099", "January 1, 2026")
    states.check_identity(slice_seed("S.C. Code § 30-2-60", "30-2-60", "30-2-70"), past, "html")


def test_the_notes_say_the_document_is_a_slice_of_the_chapter_page():
    t = cut(T30C1, "30-1-80", "30-1-100")
    n = ing.conversion_notes(slice_seed("S.C. Code §§ 30-1-80 to 30-1-90", "30-1-80", "30-1-100"), "html", t)
    assert "30-1-80" in n and "30-1-100" in n and "Title 30, Chapter 1" in n


# ---- section slices of a PDF: the Code of Regulations chapter and the Appropriations Act's Part IB provisos ---------
# Fixtures are real pages of the PDFs fetched on 2026-11-13 through the toolkit Fetcher, cut out with poppler's
# pdfseparate and pdfunite (page 1, the contents page with the section index and the pages around the slices of
# Chapter 19; the pages holding provisos 93.9, 117.96 and 117.106 of Part IB with the pages between and after them).
REGS = (FIX / "ch19-regulations-pages.pdf").read_bytes()
BUDGET = (FIX / "appropriations-2026-27-part-1b-pages.pdf").read_bytes()


def pdf_cut(raw, doc_type, start, end):
    return ing.to_text(raw, "pdf", doc_type, SC, {"section_start": start, "section_end_before": end}, "www.scstatehouse.gov")


def test_a_regulation_slice_starts_at_the_body_heading_not_the_contents_entry():
    t = pdf_cut(REGS, "rule", "19-445.2027", "19-445.2030")
    assert t.startswith("19–445.2027.")
    assert t.splitlines()[0].split()[1:] == ["Electronic", "Commerce."]
    assert t.splitlines()[1].startswith("A. ")


def test_a_regulation_slice_includes_the_whole_regulation_and_excludes_the_next_one():
    t = pdf_cut(REGS, "rule", "19-445.2027", "19-445.2030")
    assert "B.     General." in t and "C. Submission of Offers by Electronic Commerce." in t
    assert t.rstrip().endswith("eff April 24, 2020.")
    assert "Competitive Sealed Bidding" not in t and "19–445.2030" not in t
    s = pdf_cut(REGS, "rule", "19-445.2115", "19-445.2120")
    assert s.rstrip().endswith("eff June 26, 2020.") and "Cost or Pricing Data" not in s
    assert "Software Licensing" in s


def test_a_slice_whose_start_is_only_in_the_contents_or_absent_is_refused():
    with pytest.raises(ValueError):
        pdf_cut(REGS, "rule", "19-445.2000", "19-445.2030")
    with pytest.raises(ValueError):
        pdf_cut(REGS, "rule", "19-445.2027", "19-445.2999")


def test_a_proviso_slice_starts_at_the_proviso_heading_and_stops_before_the_next_proviso():
    t = pdf_cut(BUDGET, "statute", "93.9", "93.10")
    assert t.startswith("93.9. (DOA: Cyber Security) All state agencies must adopt")
    assert t.rstrip().endswith("The Judicial and Legislative Branches are specifically exempt\nfrom the requirements set forth herein.")
    assert "Holidays" not in t and "Surplus Real Property" not in t


def test_a_proviso_slice_drops_the_running_page_header_and_keeps_every_other_line():
    t = pdf_cut(BUDGET, "statute", "93.9", "93.10")
    assert "PAGE 472" not in t and "DEPARTMENT OF ADMINISTRATION" not in t
    assert "to\nmonitor compliance with established cyber security policies" in t
    long = pdf_cut(BUDGET, "statute", "117.96", "117.97")
    assert "PAGE 53" not in long and "GENERAL PROVISIONS" not in long
    assert long.splitlines()[0].startswith("117.96. (GP: Data Breach Notification) (A) An agency of this State")
    assert "(D) For purposes of this proviso:" in long and "Remittance of Court Fee" not in long


def test_a_proviso_slice_of_117_106_has_all_seven_items_and_the_exempt_branches():
    t = pdf_cut(BUDGET, "statute", "117.106", "117.107")
    for n in range(1, 8):
        assert f"({n}) " in t
    assert t.rstrip().endswith("exempt from the\nrequirements as provided in this provision.")
    assert "Sentencing Reform" not in t


def reg_seed(citation, start, end, doc_type="rule"):
    return seed(citation, doc_type=doc_type, format="pdf", slice={"section_start": start, "section_end_before": end})


def test_identity_for_a_regulation_and_a_proviso_slice():
    t = pdf_cut(REGS, "rule", "19-445.2115", "19-445.2120")
    states.check_identity(reg_seed("S.C. Code Regs. 19-445.2115", "19-445.2115", "19-445.2120"), t, "pdf")
    with pytest.raises(ValueError):
        states.check_identity(reg_seed("S.C. Code Regs. 19-445.2027", "19-445.2027", "19-445.2030"), t, "pdf")
    p = pdf_cut(BUDGET, "statute", "117.106", "117.107")
    cite = "FY 2026-27 General Appropriations Act (H. 5126), Part IB, Proviso 117.106"
    states.check_identity(reg_seed(cite, "117.106", "117.107", "statute"), p, "pdf")
    with pytest.raises(ValueError):
        states.check_identity(reg_seed(cite.replace("117.106", "117.96"), "117.96", "117.107", "statute"), p, "pdf")


def test_a_proviso_slice_has_no_blank_line_where_a_page_break_fell():
    assert "\n\n" not in pdf_cut(BUDGET, "statute", "93.9", "93.10")
    assert "\n\n" not in pdf_cut(BUDGET, "statute", "117.96", "117.97")


def test_the_notes_of_a_pdf_slice_say_what_was_cut_and_what_was_dropped():
    p = pdf_cut(BUDGET, "statute", "117.106", "117.107")
    n = ing.conversion_notes(reg_seed("FY 2026-27 General Appropriations Act (H. 5126), Part IB, Proviso 117.106",
                                      "117.106", "117.107", "statute"), "pdf", p)
    assert "proviso 117.106" in n and "heading of proviso 117.107" in n and "page header" in n and "temporary law" in n
    r = pdf_cut(REGS, "rule", "19-445.2115", "19-445.2120")
    n = ing.conversion_notes(reg_seed("S.C. Code Regs. 19-445.2115", "19-445.2115", "19-445.2120"), "pdf", r)
    assert "regulation 19-445.2115" in n and "heading of 19-445.2120" in n and "Chapter 19" in n
