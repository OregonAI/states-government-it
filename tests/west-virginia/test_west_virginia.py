"""West Virginia: the Legislature's section pages (code.wvlegislature.gov), the Office of Technology's policy PDFs
(Google Drive downloads, whose text carries zero-width spaces) and Google Doc exports, and the Secretary of State's
legislative rules as Word files. Fixtures are the real bytes the sources served on 2026-11-12, page furniture included."""
import importlib
from pathlib import Path

import pytest

from src import states
from src.ingest_docx import docx_to_text
from src.ingest_common import pdf_to_text

FX = Path(__file__).resolve().parent.parent / "fixtures" / "west-virginia"
J = "west-virginia"


def text_of(name, doc_type, fmt):
    raw = (FX / name).read_bytes()
    return states.to_text(raw, fmt, doc_type, J)


def section(name):
    return text_of(name, "statute", "html")


def test_the_state_is_found_by_name():
    assert J in states.modules(refresh=True)


# ---- statute section pages -------------------------------------------------------------------

def test_a_section_page_becomes_its_heading_then_one_line_per_paragraph():
    lines = section("5a-6-4.html").splitlines()
    assert lines[0] == "§5A-6-4. Powers and duties of the Chief Information Officer generally."
    assert lines[1].startswith("(a) With respect to all state spending units")
    assert "(12) Promulgate legislative rules, in accordance with the provisions of §29A-3-1 et seq. as may be necessary to standardize and make effective the administration of the provisions of this article." in lines
    assert "(b) With respect to executive agencies, the Chief Information Officer may:" in lines


def test_inline_emphasis_runs_on_and_entities_are_decoded():
    assert "(A) Identifies the certification authority issuing it;" in section("39a-3-1.html")
    assert '(1) "Certificate" means a computer-based record that:' in section("39a-3-1.html")
    assert ": Provided, That executive agencies communicate such requirements." in section("5a-6-4.html")


def test_page_furniture_and_the_neighbouring_sections_are_not_text():
    text = section("5A-6-7.html".lower())
    assert text == ("§5A-6-7. Biannual report.\n"
                    "The Chief Information Officer shall report biannually to the Legislative Joint Committee "
                    "on Government and Finance on the activities of his or her office.\n")
    for leak in ("Facebook", "Search in all Chapters", "Bill History", "Previous", "Next", "Copyright",
                 "CHAPTER 1. THE STATE", "Loading Articles", "<", "&quot;"):
        assert leak not in section("5a-6-4.html")


def test_a_repealed_section_is_refused_because_only_law_in_force_is_held():
    with pytest.raises(ValueError, match="repealed"):
        section("5a-6-4a-repealed.html")


def test_an_article_contents_page_is_not_a_section_and_is_refused():
    with pytest.raises(ValueError, match="no statute text"):
        section("5a-6-article-page.html")


def test_a_section_page_must_be_the_cited_section():
    src = {"id": "wv-code-5a-6-7", "jurisdiction": J, "doc_type": "statute", "citation": "W. Va. Code § 5A-6-7",
           "title": "§5A-6-7. Biannual report.", "format": "html"}
    states.check_identity(src, section("5a-6-7.html"))
    with pytest.raises(ValueError, match="5A-6-7"):
        states.check_identity(src, section("5a-6-4.html"))


def test_a_section_with_a_lowercase_letter_is_matched_by_its_printed_number():
    src = {"id": "x", "jurisdiction": J, "doc_type": "statute", "citation": "W. Va. Code § 5A-6-4b",
           "title": "t", "format": "html"}
    with pytest.raises(ValueError):
        states.check_identity(src, section("5a-6-4.html"))


def test_the_notes_say_what_was_taken_and_what_was_removed():
    src = {"jurisdiction": J, "doc_type": "statute"}
    n = states.hook(J, "notes")(src, "html", section("5a-6-7.html"))
    assert "code.wvlegislature.gov" in n and "Previous" in n and "no effective date" in n


def test_a_statute_gets_no_effective_date_or_version():
    t = section("5a-6-7.html")
    assert states.effective_date(t, "statute", J) is None
    assert states.source_version(t, "statute", J, "html") == ""


# ---- policy PDFs with zero-width spaces ---------------------------------------------------------

def pdf(name):
    return pdf_to_text((FX / name).read_bytes())


def test_a_policy_is_the_cited_one_when_it_prints_its_number_even_between_zero_width_spaces():
    src = {"id": "wv-wvot-po1013", "jurisdiction": J, "doc_type": "policy", "citation": "WVOT-PO1013",
           "title": "Data Protection and Backup Policy", "format": "pdf"}
    states.check_identity(src, pdf("wvot-po1013.pdf"))
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({**src, "citation": "WVOT-PO1099"}, pdf("wvot-po1013.pdf"))
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({**src, "citation": "WVOT-PO101"}, pdf("wvot-po1018.pdf"))


def test_a_policy_is_matched_by_the_identity_phrase_when_one_is_given():
    src = {"id": "wv-wvot-po2005", "jurisdiction": J, "doc_type": "policy", "citation": "WVOT-PO2005",
           "title": "Memorandum of Understanding(MOU) Policy", "format": "pdf", "identity_text": "WVOT-P02005"}
    states.check_identity(src, pdf("wvot-po2005.pdf"))
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({**src, "identity_text": "WVOT-P09999"}, pdf("wvot-po2005.pdf"))


def test_the_version_is_the_revision_date_the_policy_prints_as_printed():
    v = lambda n: states.source_version(pdf(n), "policy", J, "pdf")
    assert v("wvot-po1013.pdf") == "Revised 10/01/2026"
    assert v("wvot-po1018.pdf") == "Revised 12/31/2023"
    assert v("wvot-po1034.pdf") == "Issued 10/07/2026"


def test_an_issue_date_footer_gives_the_version_when_the_policy_prints_no_revision_date():
    # 'Issue Date: 01/22/2026  Revised: New Policy' prints in every page footer of WVOT-PO2005
    assert states.source_version(pdf("wvot-po2005.pdf"), "policy", J, "pdf") == "Issued 01/22/2026"


def test_the_privacy_policies_print_dotted_dates_in_a_header_line_and_the_version_is_as_printed():
    v = lambda n: states.source_version(pdf(n), "policy", J, "pdf")
    assert v("wveb-p101.pdf") == "Revised 4.1.12"          # Issue Date: 1.30.09 ... Rev. Date: 4.1.12
    assert v("wveb-p101-2.pdf") == "Revised 11.16.23"
    assert v("wveb-p102.pdf") == "Issued 01/30/09"         # 'Rev. Date:' printed with no date
    assert v("wveb-p106-1.pdf") == "Issued 01/20/11"       # no revision field at all


def test_a_policy_with_no_printed_date_has_an_empty_version():
    assert states.source_version("A policy with no date.\n" * 30, "policy", J, "pdf") == ""


# ---- Word files ---------------------------------------------------------------------------------

def test_a_rule_is_the_cited_series_when_it_prints_its_section_marker_and_title():
    src = {"id": "wv-csr-163-2", "jurisdiction": J, "doc_type": "rule", "citation": "W. Va. CSR § 163-2",
           "title": "Chief Information Officer Review", "format": "docx"}
    t = docx_to_text((FX / "163-02.docx").read_bytes())
    states.check_identity(src, t)
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({**src, "citation": "W. Va. CSR § 163-3"}, t)
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({**src, "title": "Plan of Operation"}, t)


def test_a_rule_whose_index_title_differs_from_the_printed_one_uses_the_identity_phrase():
    src = {"id": "wv-csr-163-3", "jurisdiction": J, "doc_type": "rule", "citation": "W. Va. CSR § 163-3",
           "title": "Some Other Index Title", "format": "docx", "identity_text": "SERIES 3 CYBER REPORTING"}
    states.check_identity(src, docx_to_text((FX / "163-03.docx").read_bytes()))


def test_a_google_doc_without_a_printed_title_is_matched_by_a_phrase_the_body_prints():
    src = {"id": "wv-wvot-pr1013", "jurisdiction": J, "doc_type": "policy", "citation": "WVOT-PR1013",
           "title": "WVOT Patch Management", "format": "docx",
           "identity_text": "routine maintenance of its computing assets"}
    states.check_identity(src, docx_to_text((FX / "wvot-pr1013.docx").read_bytes()))


def test_a_sign_in_page_is_never_taken_for_a_policy():
    with pytest.raises(ValueError):
        states.to_text((FX / "drive-signin.html").read_bytes(), "html", "policy", J)


def test_the_notes_of_a_pdf_with_zero_width_spaces_say_they_are_kept():
    src = {"jurisdiction": J, "doc_type": "policy"}
    extra = states.hook(J, "extra_notes")
    t = pdf("wvot-po1013.pdf")
    assert "zero-width" in extra(src, "pdf", t, None, "Revised 10/01/2026")
    assert extra(src, "pdf", "plain text\n", None, "") == ""


def test_the_notes_claim_a_source_version_only_when_one_was_found():
    src = {"jurisdiction": J, "doc_type": "policy"}
    extra = states.hook(J, "extra_notes")
    t = pdf("wvot-po2005.pdf")
    assert "zero-width" in extra(src, "pdf", t, None, "")
    assert "source_version" not in extra(src, "pdf", t, None, "")
    assert "source_version" in extra(src, "pdf", t, None, "Issued 01/22/2026")


def test_a_privacy_procedure_is_told_from_its_parent_policy_by_the_identity_phrase():
    # WVEB-P101 is a prefix of WVEB-P101.2, so the citation alone would match both files
    src = {"id": "wv-wveb-p101", "jurisdiction": J, "doc_type": "policy", "citation": "WVEB-P101",
           "title": "Accountability Policy", "format": "pdf", "identity_text": "Policy No: WVEB-P101 Issue Date"}
    states.check_identity(src, pdf("wveb-p101.pdf"))
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(src, pdf("wveb-p101-2.pdf"))


def test_a_scanned_rule_is_matched_by_its_identity_phrase_because_ocr_misreads_its_section_marks():
    # the 163CSR1 scan prints '§ 163-1-1' and the OCR reads '§ 161-3-1'
    ocr_text = ("TITLE 163\nLEGISLATIVE RULE\nSERIES 1\nPROCEDURES FOR SANITIZATION, RETIREMENT, AND DISPOSITION\n"
                "§ 161-3-1 General.\n")
    src = {"id": "wv-csr-163-1", "jurisdiction": J, "doc_type": "rule", "citation": "W. Va. CSR § 163-1",
           "title": "Procedures for Sanitization, Retirement and Disposition of Information Technology Equipment",
           "format": "pdf", "ocr": True, "identity_text": "PROCEDURES FOR SANITIZATION, RETIREMENT"}
    states.check_identity(src, ocr_text)
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({**src, "identity_text": "CYBER REPORTING"}, ocr_text)
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({k: v for k, v in src.items() if k != "ocr"}, ocr_text)
