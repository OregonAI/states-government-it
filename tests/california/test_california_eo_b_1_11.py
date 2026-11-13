"""Seam: src.ingest.to_text / check_identity for Executive Order B-1-11 (state-issued phones), another order
the Governor's archive prints in full. Fixture: the real page fetched 2026-11-13 with the Fetcher
(HTTP 200, text/html, 59,659 bytes), with its press-release furniture."""
from pathlib import Path

import pytest

from src import ingest as ing

RAW = (Path(__file__).resolve().parent.parent / "fixtures" / "california" / "eo-b-1-11-archive.html").read_bytes()
SRC = {"id": "ca-eo-b-1-11", "doc_type": "executive_order", "jurisdiction": "california",
       "citation": "Executive Order B-1-11", "title": "x"}


def eo():
    return ing.to_text(RAW, "html", "executive_order", "california")


def test_the_order_runs_from_its_heading_to_the_attestation():
    lines = eo().splitlines()
    assert lines[0] == "EXECUTIVE ORDER B-1-11"
    assert lines[1].startswith("WHEREAS; the Governor’s 2011-12 budget proposes")
    assert any(l.startswith("IT IS ORDERED that all State agency secretaries") for l in lines)
    assert lines[-2:] == ["DEBRA BOWEN", "Secretary of State"]
    assert "IN WITNESS WHEREOF I have hereunto set my hand" in eo()


def test_no_page_furniture_and_identity_is_the_cited_order():
    t = eo()
    assert "<" not in t and "\xa0" not in t
    ing.check_identity(SRC, t)
    with pytest.raises(ValueError, match="not the cited"):
        ing.check_identity({**SRC, "citation": "Executive Order B-2-11"}, t)


def test_conversion_notes_describe_this_page_not_the_press_release_shape():
    n = ing.conversion_notes(SRC, "html", "x")
    assert "press release" not in n and "PDF" not in n
    assert "Published" in n and "Latest News" in n
