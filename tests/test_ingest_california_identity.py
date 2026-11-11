"""Seam: src.ingest.derive / check_identity must tell the cited instrument from another document that
only names it. Fixtures are real bytes fetched 2026-11-11 through the Fetcher with its curl transport:
the Technology Letter 24-01 page (whose reference list names Executive Order N-12-23), the first two
pages of SIMM 19E.1 and 19F.1 (two sets of 'Preparation Instructions' that differ in their section
number), Executive Order N-5-26, and letters and pages from earlier tests."""
from pathlib import Path

import pytest

from src import ingest as ing

FIX = Path(__file__).resolve().parent / "fixtures"
CDT = "https://www.cdt.ca.gov/"
TL_24_01 = (FIX / "cdt-tl-24-01.html").read_bytes()
S19E = (FIX / "cdt-simm-19e-1-pages-1-2.pdf").read_bytes()
S19F = (FIX / "cdt-simm-19f-1-pages-1-2.pdf").read_bytes()
EO_5_26 = (FIX / "eo-n-5-26.pdf").read_bytes()
SIMM_40A = (FIX / "cdt-simm-40a.html").read_bytes()
ITPL = (FIX / "cdt-itpl-09-03.pdf").read_bytes()
TL_21_01 = (FIX / "cdt-tl-21-01.pdf").read_bytes()


def src(id_, url, fmt, citation, title, doc_type="policy", **more):
    return {"id": id_, "url": url, "format": fmt, "doc_type": doc_type, "jurisdiction": "california",
            "citation": citation, "title": title, **more}


EO = src("ca-eo-n-5-26", "https://www.gov.ca.gov/x.pdf", "pdf", "Executive Order N-5-26", "x", "executive_order")


def test_an_executive_order_is_its_own_heading_before_the_first_whereas_not_a_letter_that_cites_it():
    assert ing.derive(EO, EO_5_26)[0] == "pdf"
    letter_text = ing.cdt_html_to_text(TL_24_01)
    assert "Executive Order N-12-23" in letter_text            # the letter's reference list names it
    with pytest.raises(ValueError, match="PDF is not the cited instrument"):
        ing.check_identity({**EO, "citation": "Executive Order N-12-23"}, letter_text, "pdf")


def test_a_cdt_page_is_its_own_heading_not_a_page_that_mentions_the_citation():
    tl = src("ca-tl-24-01", CDT + "policy/technology-letters/technology-letter-24-01/", "html", "TL 24-01", "x",
             identity_text="Technology Letter 24-01")
    assert ing.derive(tl, TL_24_01)[0] == "html"
    simm_40 = src("ca-simm-40", CDT + "policy/simm/simm-40/", "html", "SIMM 40", "Internet Domain Name Taxonomy",
                  identity_text="SIMM 40")
    with pytest.raises(ValueError, match="page is not the cited instrument"):      # 'SIMM 40A' is another section
        ing.derive(simm_40, SIMM_40A)
    simm_40a = {**simm_40, "id": "ca-simm-40a", "citation": "SIMM 40A", "identity_text": "SIMM 40A"}
    assert ing.derive(simm_40a, SIMM_40A)[0] == "html"


def test_two_sets_of_preparation_instructions_are_told_apart_by_their_section_number():
    e = src("ca-simm-19e-1", CDT + "x/SIMM-19E.1.pdf", "pdf", "SIMM 19E.1", "Preparation Instructions")
    f = src("ca-simm-19f-1", CDT + "x/SIMM-19F.1.pdf", "pdf", "SIMM 19F.1", "Preparation Instructions")
    assert ing.derive(e, S19E)[0] == "pdf" and ing.derive(f, S19F)[0] == "pdf"
    with pytest.raises(ValueError, match="PDF is not the cited instrument"):
        ing.derive(e, S19F)
    with pytest.raises(ValueError, match="PDF is not the cited instrument"):
        ing.derive(f, S19E)


def test_a_letter_pdf_is_the_cited_number_in_its_header_not_a_number_in_its_reference_list():
    itpl = src("ca-itpl-09-03", CDT + "x/ITPL_09-03.pdf", "pdf", "ITPL 09-03", "x", identity_text="ITPL 09-03")
    assert ing.derive(itpl, ITPL)[0] == "pdf"
    with pytest.raises(ValueError, match="PDF is not the cited instrument"):
        ing.derive({**itpl, "identity_text": "ITPL 09-04"}, ITPL)
    tl = src("ca-tl-21-01", CDT + "x/TL_21-01.pdf", "pdf", "TL 21-01", "x", identity_text="TL 21-01")
    assert ing.derive(tl, TL_21_01)[0] == "pdf"
    # a number that only appears further down the letter (here a SAM section) is not the letter's number
    with pytest.raises(ValueError, match="PDF is not the cited instrument"):
        ing.derive({**tl, "identity_text": "4819.34"}, TL_21_01)


def test_the_refusal_names_the_format():
    wrong = src("ca-x", CDT + "policy/simm/simm-40a/", "html", "SIMM 99", "x", identity_text="SIMM 99")
    with pytest.raises(ValueError, match="^ca-x: page is not"):
        ing.derive(wrong, SIMM_40A)


def test_a_letter_and_its_faq_that_share_a_number_are_told_apart():
    letter = src("ca-itpl-10-09", CDT + "x/ITPL_10-09.pdf", "pdf", "ITPL 10-09", "x",
                 identity_text="IT POLICY LETTER ITPL 10-09")
    faqs = src("ca-itpl-10-09-faqs", CDT + "x/FAQs.pdf", "pdf", "ITPL 10-09 FAQs", "x",
               identity_text="Policy Letter 10-09 Frequently Asked Questions")
    a, b = (FIX / "cdt-itpl-10-09.pdf").read_bytes(), (FIX / "cdt-itpl-10-09-faqs.pdf").read_bytes()
    assert ing.derive(letter, a)[0] == "pdf" and ing.derive(faqs, b)[0] == "pdf"
    with pytest.raises(ValueError, match="PDF is not the cited instrument"):
        ing.derive(letter, b)
    with pytest.raises(ValueError, match="PDF is not the cited instrument"):
        ing.derive(faqs, a)
