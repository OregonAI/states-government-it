"""Seam: src.ingest / src.states for Minnesota: the Revisor of Statutes' full-chapter pages for statutes
(www.revisor.mn.gov/statutes/cite/<chapter>/full) and rules (www.revisor.mn.gov/rules/<chapter>/full), and
the identity checks of statute and rule pages. Fixtures are slices of the real pages the Revisor served on
2026-11-11: the page head, some whole sections (a repealed one among them) and the page footer, cut from the
bytes, nothing re-typed. MNIT's policies and the executive orders are PDFs, which the shared reader handles."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "minnesota"
STAT = (FIX / "revisor-chapter-16E-slice.html").read_bytes()
RULE = (FIX / "revisor-rules-1205-slice.html").read_bytes()


def text(raw, doc_type):
    return ing.to_text(raw, "html", doc_type, "minnesota")


def test_statute_text_opens_with_the_chapter_title_then_each_section_heading_subdivision_and_paragraph():
    lines = text(STAT, "statute").splitlines()
    assert lines[0] == "CHAPTER 16E. DEPARTMENT OF INFORMATION TECHNOLOGY SERVICES"
    assert "16E.01 DEPARTMENT OF INFORMATION TECHNOLOGY SERVICES." in lines
    assert "Subdivision 1. Creation; chief information officer." in lines
    i = lines.index("Subdivision 1. Creation; chief information officer.")
    assert lines[i + 1].startswith('The Department of Information Technology Services, which may also be known as Minnesota')
    assert "Subd. 1a. Responsibilities." in lines


def test_statute_text_keeps_history_and_the_repealed_section_line_and_drops_menus_footer_and_the_table_of_sections():
    t = text(STAT, "statute")
    assert "History:" in t
    assert "1997 c 202 art 3 s 7; 1998 c 366 s 41;" in t
    assert "16E.035 MS 2022 [Repealed, 2024 c 123 art 17 s 31]" in t
    assert "Table of Sections" not in t and "Headnote" not in t
    for furniture in ("Minnesota House of Representatives", "Skip to main content", "Contact Your Legislator",
                      "Official Publication of the State of Minnesota", "Search Minnesota Statutes"):
        assert furniture not in t
    assert "<" not in t and "&amp;" not in t and "§" not in t and "\xa0" not in t


def test_statute_section_has_a_blank_line_before_it():
    lines = text(STAT, "statute").splitlines()
    i = lines.index("16E.01 DEPARTMENT OF INFORMATION TECHNOLOGY SERVICES.")
    assert lines[i - 1] == ""


def test_rule_text_opens_with_the_chapter_and_agency_then_parts_with_subparts_authority_and_publication():
    lines = text(RULE, "rule").splitlines()
    assert lines[0] == "CHAPTER 1205, DATA PRACTICES"
    assert lines[1] == "DEPARTMENT OF ADMINISTRATION"
    t = "\n".join(lines)
    assert "1205.0100 HOW THESE RULES APPLY." in t
    assert "Subpart 1. Scope." in t.splitlines()
    assert "Statutory Authority:" in t and "Published Electronically:" in t
    assert "Table of Parts" not in t
    assert "Official Publication of the State of Minnesota" not in t and "Contact Your Legislator" not in t


def test_rule_repealed_part_is_kept_as_printed():
    assert "[Repealed, L 2010 c 365 art 1 s 12]" in text(RULE, "rule")


def test_a_page_without_the_revisor_text_region_is_refused():
    with pytest.raises(ValueError, match="layout"):
        text(b"<html><body><main>nothing</main></body></html>", "statute")


STAT_SRC = {"id": "mn-stat-16e", "jurisdiction": "minnesota", "doc_type": "statute",
            "citation": "Minn. Stat. ch. 16E", "title": "Chapter 16E. Department of Information Technology Services"}


def test_statute_identity_accepts_its_chapter_and_refuses_another():
    states.check_identity(STAT_SRC, text(STAT, "statute"), "html")
    with pytest.raises(ValueError, match="not Minn. Stat. ch. 13"):
        states.check_identity({**STAT_SRC, "citation": "Minn. Stat. ch. 13"}, text(STAT, "statute"), "html")


def test_rule_identity_needs_the_printed_chapter_heading():
    src = {"id": "mn-rule-1205", "jurisdiction": "minnesota", "doc_type": "rule",
           "citation": "Minn. R. ch. 1205", "title": "CHAPTER 1205, DATA PRACTICES"}
    states.check_identity(src, text(RULE, "rule"), "html")
    with pytest.raises(ValueError):
        states.check_identity({**src, "title": "CHAPTER 1215, EMERGENCY 911"}, text(RULE, "rule"), "html")


def test_notes_say_where_the_text_came_from():
    src = {**STAT_SRC, "format": "html"}
    n = ing.conversion_notes(src, "html", text(STAT, "statute"))
    assert "revisor.mn.gov" in n and "Table of Sections" in n


# ---- MNIT policy and standard PDFs: the identity phrase must be in the title block ----

def _mnit(name):
    return (FIX / f"mnit-{name}.txt").read_text()


def _src(id_, title, doc_type, **kw):
    return {"id": id_, "jurisdiction": "minnesota", "doc_type": doc_type, "title": title,
            "citation": f"MNIT {title}, Version 1", "identity_text": title, "format": "pdf", **kw}


def test_mnit_pdf_identity_accepts_a_title_split_over_two_lines():
    states.check_identity(_src("mn-mnit-isrm-applicability-standard",
                               "Information Security and Risk Management Applicability Standard", "standard"),
                          _mnit("isrm-applicability-standard"))


def test_mnit_pdf_identity_accepts_a_title_split_between_the_left_column_lines_of_the_supply_chain_policy():
    states.check_identity(_src("mn-mnit-supply-chain-risk-policy", "Supply Chain Risk Management Policy", "policy"),
                          _mnit("supply-chain-risk-policy"))


@pytest.mark.parametrize("sibling, id_, title, doc_type", [
    ("isrm-applicability-standard", "mn-mnit-isrm-standard", "Information Security Risk Management Standard", "standard"),
    ("secure-configuration-standard", "mn-mnit-technical-security-policy", "Technical Security Policy", "policy"),
    ("threat-vulnerability-standard", "mn-mnit-threat-vulnerability-policy",
     "Threat and Vulnerability Management Policy", "policy"),
])
def test_mnit_pdf_identity_refuses_a_sibling_that_only_names_the_cited_instrument(sibling, id_, title, doc_type):
    text = _mnit(sibling)
    assert title.casefold() in " ".join(text.split()).casefold()       # the sibling does name it, further down
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(_src(id_, title, doc_type), text)


def test_mnit_pdf_identity_takes_the_phrase_from_the_seed_not_the_citation():
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(_src("mn-mnit-supply-chain-risk-policy", "Supply Chain Risk Management Standard",
                                   "standard"), _mnit("supply-chain-risk-policy"))
