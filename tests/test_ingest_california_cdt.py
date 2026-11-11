"""Seams: src.ingest.derive / to_text / check_identity for the California Department of Technology's
library (www.cdt.ca.gov: Technology Letters and SIMM pages as web pages, letters as PDFs), the
Governor's executive orders as PDFs (www.gov.ca.gov), and src.ingest.make_fetcher (opting in to the
toolkit's curl transport only when the pinned toolkit has it).

cdt.ca.gov and gov.ca.gov answer the toolkit's httpx client with a Cloudflare managed challenge and
answer system curl, with the same User-Agent, HTTP 200. Fixtures are real bytes fetched 2026-11-11
through the toolkit Fetcher with curl_on_challenge=True: the <main> element of two pages, one
Technology Letter PDF (TL 21-01) and one executive order PDF (N-5-26)."""
from pathlib import Path

import pytest

from src import ingest as ing

FIX = Path(__file__).resolve().parent / "fixtures"
TL_PAGE = (FIX / "cdt-tl-26-01.html").read_bytes()
SIMM_PAGE = (FIX / "cdt-simm-40a.html").read_bytes()
TL_PDF = (FIX / "cdt-tl-21-01.pdf").read_bytes()
EO_PDF = (FIX / "eo-n-5-26.pdf").read_bytes()

TL_SRC = {"id": "ca-tl-26-01", "url": "https://www.cdt.ca.gov/policy/technology-letters/technology-letter-26-01/",
          "format": "html", "doc_type": "policy", "jurisdiction": "california", "citation": "TL 26-01",
          "title": "SIMM 5340-A Information Security Incident Response and Reporting",
          "identity_text": "Technology Letter 26-01"}


def cdt(raw=TL_PAGE):
    return ing.cdt_html_to_text(raw)


def test_a_technology_letter_page_runs_from_its_heading_to_its_signature():
    lines = cdt().splitlines()
    assert lines[:3] == ["Technology Letter 26-01", "February 2026", "Subject:"]
    assert "SIMM 5340-A Information Security Incident Response and Reporting" in lines
    assert "Background" in lines
    assert "Questions:" in lines
    assert "Direct questions regarding this Technology Letter to the Department of Technology, "\
           "Office of Information Security at security@state.ca.gov." in lines
    assert lines[-4:] == ["Signature:", "On file", "Liana Bailey-Crimmins, State CIO and Director",
                          "California Department of Technology"]


def test_menus_print_button_scripts_and_footer_are_not_the_letter():
    t = cdt()
    for not_letter in ("Print page", "Our department", "Register to Vote", "elemButton", "Flex Alert",
                       "Website Accessibility Certification", "<", "\xa0"):
        assert not_letter not in t


def test_a_simm_page_keeps_tables_and_accordion_headings_but_not_its_navigation():
    lines = cdt(SIMM_PAGE).splitlines()
    assert lines[0] == "SIMM 40A – Internet Domain Name Taxonomy Instructions Revised May 2023"
    assert "Revision History" in lines
    assert "Initial Release | May 2017 | California Department of Technology | New" in lines
    assert "Revision | Release date | Owner | Summary of changes" in lines
    assert "General information" in lines
    for nav in ("On this page", "SIMM 40B", "Section 1 | Section 2", "SIMM 40"):
        assert nav not in lines


def test_a_page_without_a_heading_and_a_footer_is_refused():
    with pytest.raises(ValueError, match="no CDT page region"):
        cdt(b"<html><body><main><p>Nothing here.</p></main></body></html>")


def test_a_cdt_policy_page_is_read_by_derive_from_its_host_and_checked_against_its_heading():
    fmt, text = ing.derive(TL_SRC, TL_PAGE)
    assert fmt == "html" and text.startswith("Technology Letter 26-01\n")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.derive({**TL_SRC, "identity_text": "Technology Letter 26-02"}, TL_PAGE)


def test_a_dgs_sam_page_is_still_checked_as_a_sam_chapter():
    src = {**TL_SRC, "url": "https://www.dgs.ca.gov/Resources/SAM/TOC/5000/Chapter-View",
           "citation": "SAM chapter 5000"}
    with pytest.raises(ValueError):
        ing.derive(src, TL_PAGE)


def test_a_letter_pdf_is_the_cited_letter_by_the_number_it_prints():
    text = ing.to_text(TL_PDF, "pdf", "policy", "california")
    src = {"id": "ca-tl-21-01", "doc_type": "policy", "jurisdiction": "california",
           "citation": "TL 21-01", "title": "Project Cost Delegation", "identity_text": "TECHNOLOGY LETTER TL 21-01"}
    ing.check_identity(src, text)
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity({**src, "identity_text": "TECHNOLOGY LETTER TL 21-02"}, text)


def test_an_executive_order_pdf_is_the_cited_order_by_its_printed_heading():
    text = ing.to_text(EO_PDF, "pdf", "executive_order", "california")
    src = {"id": "ca-eo-n-5-26", "doc_type": "executive_order", "jurisdiction": "california",
           "citation": "Executive Order N-5-26", "title": "x"}
    ing.check_identity(src, text)
    assert "EXECUTIVE ORDER N-5-26" in text
    for wrong in ("Executive Order N-6-26", "Executive Order N-5-2", "Executive Order B-5-26"):
        with pytest.raises(ValueError, match="not the cited instrument"):
            ing.check_identity({**src, "citation": wrong}, text)


class _Old:
    def __init__(self, config=None, *, user_agent=None):
        self.kwargs = {}


class _New:
    def __init__(self, config=None, *, user_agent=None, curl_on_challenge=False):
        self.kwargs = {"curl_on_challenge": curl_on_challenge}


def test_the_curl_transport_is_requested_only_when_the_toolkit_has_it():
    assert ing.make_fetcher("cfg", cls=_New).kwargs == {"curl_on_challenge": True}
    assert ing.make_fetcher("cfg", cls=_Old).kwargs == {}


def test_conversion_notes_describe_the_cdt_page_not_a_rule_page():
    n = ing.conversion_notes(TL_SRC, "html", "x")
    assert "Department of Technology" in n and "Rule text" not in n and "pdftotext" not in n
    assert "navigation" in n and "print button" in n and "table row" in n
