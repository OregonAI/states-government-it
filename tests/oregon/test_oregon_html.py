"""Seam: src.ingest.to_text for Oregon's pages (ORS chapters, OAR chapters). Fixtures are real bytes
the official sites served on 2026-11-10 (the ORS one trimmed after the first section)."""
from pathlib import Path

import pytest

from src import ingest as ing

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "oregon"
ORS = (FIX / "ors-276a-excerpt.html").read_bytes()
OAR = (FIX / "oar-128-050.html").read_bytes()


def test_ors_text_is_one_paragraph_per_line_in_source_order():
    t = ing.to_text(ORS, "html", "statute")
    lines = t.splitlines()
    assert lines[0] == "Chapter 276A — Information Technology"
    assert "2025 EDITION" in lines
    # a source paragraph wrapped across several HTML lines is one line of text
    assert ("(5) Although each agency is responsible for the agency’s information resources, "
            "centralized information resource management must also exist to:") in lines
    assert lines.index("(State Chief Information Officer)") < \
        lines.index("276A.200 Legislative findings on information resources")


def test_ors_text_has_no_markup_no_page_furniture_no_blank_paragraphs():
    t = ing.to_text(ORS, "html", "statute")
    assert "<" not in t and "font-family" not in t and "MsoNormal" not in t
    assert "\xa0" not in t and "&nbsp;" not in t
    assert "\n\n" not in t                       # empty source paragraphs are dropped
    assert all(line == line.strip() for line in t.splitlines())


def test_ors_text_keeps_typography_of_the_source():
    t = ing.to_text(ORS, "html", "statute")
    assert "’" in t and "—" in t                 # decoded from windows-1252, not mangled
    assert "â€" not in t and "�" not in t


def test_oar_text_keeps_rule_number_title_body_authority_and_history():
    t = ing.to_text(OAR, "html", "rule")
    assert "Division 50" in t and "Identity Authentication/Electronic Signatures" in t
    assert "128-050-0005" in t
    assert "Statutory/Other Authority:" in t and "Statutes/Other Implemented:" in t
    assert "OSCIO 1-2026, amend filed 11/09/2026, effective 12/01/2026" in t
    assert "DAS 11-2005, f. & cert. ef. 10-21-05" in t     # entities decoded


def test_oar_text_drops_site_navigation_footer_and_scripts():
    t = ing.to_text(OAR, "html", "rule")
    for furniture in ("Search Current Rules", "Oregon State Archives", "ga('create'",
                      "Privacy Policy", "<", "Skip to main content"):
        assert furniture not in t


def test_oregon_statute_path_is_unchanged_when_no_jurisdiction_is_given():
    assert ing.to_text(ORS, "html", "statute").startswith("Chapter 276A")
