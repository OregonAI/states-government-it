"""Seam: src.ingest.to_text / check_identity for a California executive order that the Governor's
archive site (www.archive.gov.ca.gov) prints in full inside a press-release page. The Governor's
live site (www.gov.ca.gov) refuses the Fetcher; the archive answers it. Fixture: the real page
fetched 2026-11-11 with the Fetcher (HTTP 200, text/html, 65,304 bytes)."""
from pathlib import Path

import pytest

from src import ingest as ing

RAW = (Path(__file__).resolve().parent / "fixtures" / "eo-b-34-15-archive.html").read_bytes()
SRC = {"id": "ca-eo-b-34-15", "doc_type": "executive_order", "jurisdiction": "california",
       "citation": "Executive Order B-34-15", "title": "California Cybersecurity Integration Center"}


def eo(raw=RAW):
    return ing.to_text(raw, "html", "executive_order", "california")


def test_the_order_runs_from_its_heading_to_the_attestation():
    lines = eo().splitlines()
    assert lines[0] == "EXECUTIVE ORDER B-34-15"
    assert lines[1].startswith("WHEREAS information technology networks and critical infrastructure")
    assert lines[-5:-2] == ["EDMUND G. BROWN JR.", "Governor of California", "ATTEST:"]
    assert lines[-1] == "Secretary of State" and lines[-2] == "ALEX PADILLA"
    assert "ATTEST:" in lines


def test_ordered_paragraphs_and_the_member_list_are_kept_one_line_each():
    t = eo()
    assert "1. The California Governor’s Office of Emergency Services shall establish and lead" in t
    assert "– California Department of Technology, Chief Information Security Office" in t.splitlines()
    assert "– Other members as designated by the Director of Cal OES" in t.splitlines()
    assert "5. Information sharing by the Integration Center shall be conducted" in t
    assert "I FURTHER DIRECT that all state departments and agencies ensure compliance" in t
    assert "IN WITNESS WHEREOF I have hereunto set my hand" in t


def test_press_release_text_menu_and_footer_are_not_the_order():
    t = eo()
    for not_order in ("SACRAMENTO", "Latest News", "Form 801", "The full text of the executive order is below",
                      "A copy of the executive order can also be found", "###", "<", "&#8217;", "\xa0"):
        assert not_order not in t


def test_a_page_without_the_order_is_refused():
    with pytest.raises(ValueError, match="no executive order"):
        eo(b"<html><body><article><h1>Governor signs bill</h1><p>Nothing here.</p></article></body></html>")


def test_identity_is_the_cited_order_number_with_its_letter():
    ing.check_identity(SRC, eo())
    with pytest.raises(ValueError, match="not the cited"):
        ing.check_identity({**SRC, "citation": "Executive Order N-34-15"}, eo())
    with pytest.raises(ValueError, match="not the cited"):
        ing.check_identity({**SRC, "citation": "Executive Order B-34-16"}, eo())


def test_conversion_notes_describe_the_archive_page():
    n = ing.conversion_notes(SRC, "html", "x")
    assert "archive" in n.lower() and "pdftotext" not in n


def test_the_order_prints_no_effective_date_label_to_misread():
    assert ing.effective_date(eo(), "executive_order") is None
