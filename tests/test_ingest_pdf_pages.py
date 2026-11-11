"""Seam: src.ingest.pdf_to_text / derive / conversion_notes on a PDF with pages that have no text layer.

The fixture is real bytes: pages 1-2 of Executive Order N-30-25 (www.gov.ca.gov, fetched 2026-11-11), cut with
pdfseparate and pdfunite. Page 1 has a text layer (466 words); page 2 is a scanned image (0 words). The
whole PDF has 4 pages, 3 of them scans, and was once committed as a complete document because only the
page-1 text was compared with itself."""
from pathlib import Path

import pytest

from src import ingest as ing

PARTLY_SCANNED = (Path(__file__).resolve().parent / "fixtures" / "eo-n-30-25-pages-1-2.pdf").read_bytes()
EO_PDF = (Path(__file__).resolve().parent / "fixtures" / "eo-n-5-26.pdf").read_bytes()


def test_a_pdf_with_a_page_that_has_no_text_layer_is_refused_naming_the_page():
    with pytest.raises(ValueError, match=r"page\(s\) 2 have no text layer"):
        ing.pdf_to_text(PARTLY_SCANNED)


def test_a_page_the_seed_entry_lists_as_figure_or_image_only_is_let_through():
    text = ing.pdf_to_text(PARTLY_SCANNED, no_text_pages=[2])
    assert "WHEREAS" in text


def test_a_listed_page_that_does_have_text_is_refused_so_the_list_stays_true():
    with pytest.raises(ValueError, match=r"lists page\(s\) 1 .* but .* text"):
        ing.pdf_to_text(PARTLY_SCANNED, no_text_pages=[1, 2])


def test_derive_reads_the_list_from_the_seed_entry():
    src = {"id": "x", "format": "pdf", "doc_type": "executive_order", "jurisdiction": "california",
           "citation": "Executive Order N-30-25", "title": "x", "url": "https://www.gov.ca.gov/x.pdf"}
    with pytest.raises(ValueError, match="no text layer"):
        ing.derive(src, PARTLY_SCANNED)
    fmt, _ = ing.derive({**src, "no_text_pages": [2]}, PARTLY_SCANNED)
    assert fmt == "pdf"


def test_a_pdf_whose_pages_all_have_text_is_unchanged():
    assert "EXECUTIVE ORDER N-5-26" in ing.pdf_to_text(EO_PDF)


def test_the_conversion_notes_say_which_pages_carry_no_text():
    src = {"jurisdiction": "california", "doc_type": "executive_order", "no_text_pages": [2, 3]}
    assert "Pages 2, 3 of the PDF have no text layer" in ing.conversion_notes(src, "pdf", "x")
    assert "no text layer" not in ing.conversion_notes({**src, "no_text_pages": []}, "pdf", "x")
