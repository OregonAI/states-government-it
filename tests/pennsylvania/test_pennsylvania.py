"""Pennsylvania: statute PDFs from the General Assembly's site and executive-order PDFs from the Office of
Administration. Fixtures are the first page of each file as the shared PDF reader prints it (pdftotext -layout), so
the title block and its two-column layout are real; the shared reader handles the PDFs themselves."""
from pathlib import Path

import pytest

from src import states
from src.states import pennsylvania

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "pennsylvania"
ACT94 = (FIX / "act-94-2005-first-page.txt").read_text()
ACT69 = (FIX / "act-69-1999-first-page.txt").read_text()
EO_2016_06 = (FIX / "eo-2016-06-first-page.txt").read_text()
EO_2023_19 = (FIX / "eo-2023-19-first-page.txt").read_text()
MD_205_43 = (FIX / "md-205-43-first-page.txt").read_text()
ITP_MOBILE_TEXT = (FIX / "itp-mobile-device-first-page.txt").read_text()

STATUTE = {"id": "pa-act-94-2005", "doc_type": "statute", "jurisdiction": "pennsylvania",
           "citation": "Act of Dec. 22, 2005, P.L. 474, No. 94", "title": "Breach of Personal Information Notification Act"}
EO = {"id": "pa-eo-2016-06", "doc_type": "executive_order", "jurisdiction": "pennsylvania",
      "citation": "Executive Order 2016-06", "title": "Enterprise Information Technology Governance"}


def test_the_state_is_found_by_name():
    assert "pennsylvania" in states.modules(refresh=True)


def test_a_statute_pdf_is_the_cited_act_when_it_prints_the_title_and_the_act_number():
    assert pennsylvania.check_identity(STATUTE, ACT94, "PDF") is True
    eta = dict(STATUTE, id="pa-act-69-1999", citation="Act of Dec. 16, 1999, P.L. 971, No. 69", title="Electronic Transactions Act")
    assert pennsylvania.check_identity(eta, ACT69, "PDF") is True


def test_a_statute_pdf_that_is_another_act_is_refused():
    with pytest.raises(ValueError, match="not the cited instrument"):
        pennsylvania.check_identity(STATUTE, ACT69, "PDF")
    wrong_number = dict(STATUTE, citation="Act of Dec. 22, 2005, P.L. 474, No. 95")
    with pytest.raises(ValueError, match="not the cited instrument"):
        pennsylvania.check_identity(wrong_number, ACT94, "PDF")


def test_an_order_that_prints_its_number_in_the_title_block_column_is_accepted():
    # the title block is two columns: "Enterprise Information Technology   2016-06, As Amended"; the shared
    # reader looks for "Executive Order 2016-06", which these PDFs do not print
    assert "Executive Order 2016-06" not in EO_2016_06[:600]    # only the page footer prints it
    assert pennsylvania.check_identity(EO, EO_2016_06, "PDF") is True


def test_an_order_that_prints_executive_order_and_the_number_in_its_heading_is_accepted():
    eo = dict(EO, id="pa-eo-2023-19", citation="Executive Order 2023-19")
    assert pennsylvania.check_identity(eo, EO_2023_19, "PDF") is True


def test_an_order_with_another_number_is_refused():
    with pytest.raises(ValueError, match="not the cited instrument"):
        pennsylvania.check_identity(dict(EO, citation="Executive Order 2016-07"), EO_2016_06, "PDF")
    with pytest.raises(ValueError, match="not the cited instrument"):
        pennsylvania.check_identity(dict(EO, citation="Executive Order 2023-19"), EO_2016_06, "PDF")


def test_a_number_inside_a_longer_number_does_not_count():
    eo = dict(EO, citation="Executive Order 2016-0")
    with pytest.raises(ValueError, match="not the cited instrument"):
        pennsylvania.check_identity(eo, EO_2016_06, "PDF")


MD = {"id": "pa-md-205-43", "doc_type": "policy", "jurisdiction": "pennsylvania", "citation": "Management Directive 205.43",
      "title": "Quality Assurance for Business Productivity Tools", "identity_text": "205.43"}
ITP_CLASSIFICATION = {"id": "pa-itp-data-classification-policy", "doc_type": "policy", "jurisdiction": "pennsylvania",
                      "citation": "Commonwealth of Pennsylvania IT Policy: Data Classification Policy",
                      "title": "Data Classification Policy", "identity_text": "Data Classification Policy"}
ITP_MOBILE = dict(ITP_CLASSIFICATION, id="pa-itp-mobile-device-policy", title="Mobile Device Policy",
                  citation="Commonwealth of Pennsylvania IT Policy: Mobile Device Policy",
                  identity_text="Mobile Device Policy")


def test_a_directive_is_the_cited_one_when_its_number_is_in_the_title_block():
    assert pennsylvania.check_identity(MD, MD_205_43, "PDF") is True


def test_a_directive_whose_number_is_only_in_the_footer_or_body_is_refused():
    with pytest.raises(ValueError, match="not the cited instrument"):
        pennsylvania.check_identity(dict(MD, identity_text="205.34"), MD_205_43, "PDF")
    body_only = "\n".join(["Management Directive 205.99"] + ["filler words to push the next line past the title block"] * 20 + ["see 205.43 for the rule"])
    with pytest.raises(ValueError, match="not the cited instrument"):
        pennsylvania.check_identity(MD, body_only, "PDF")


def test_an_itp_is_the_cited_policy_when_its_title_is_in_the_title_block():
    assert pennsylvania.check_identity(ITP_MOBILE, ITP_MOBILE_TEXT, "PDF") is True


def test_an_itp_that_only_cross_references_another_policys_title_is_refused():
    # the Mobile Device Policy's first page names the Data Classification Policy (real bytes), but not in its title block
    assert "data classification policy" in " ".join(ITP_MOBILE_TEXT.split()).casefold()
    assert "data classification policy" not in " ".join(ITP_MOBILE_TEXT[:800].split()).casefold()
    with pytest.raises(ValueError, match="not the cited instrument"):
        pennsylvania.check_identity(ITP_CLASSIFICATION, ITP_MOBILE_TEXT, "PDF")


def test_the_identity_phrase_defaults_to_the_title_when_the_entry_has_none():
    no_phrase = {k: v for k, v in ITP_MOBILE.items() if k != "identity_text"}
    assert pennsylvania.check_identity(no_phrase, ITP_MOBILE_TEXT, "PDF") is True


def test_a_policy_page_that_is_not_a_pdf_is_left_to_the_shared_check():
    assert pennsylvania.check_identity(ITP_MOBILE, "Mobile Device Policy", "page") is False


def test_other_document_types_are_left_to_the_shared_check():
    page = {"id": "pa-watch", "doc_type": "rule", "jurisdiction": "pennsylvania", "citation": "4 Pa. Code Chapter 7", "title": "x"}
    assert pennsylvania.check_identity(page, "x", "page") is False
