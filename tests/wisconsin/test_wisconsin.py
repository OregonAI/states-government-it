"""Seam: src.ingest for Wisconsin: the Legislature's statute and administrative-code pages
(docs.legis.wisconsin.gov), their identity checks and printed versions.
Fixtures are real pages the Legislature served on 2026-11-12. A statute page is a window of
neighbouring sections, so the statute fixtures keep the page furniture and one neighbour each side
of the section; the rule fixture is the whole chapter page."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "wisconsin"
SEC_979 = (FIX / "statute-16-979-window.html").read_bytes()
SEC_134 = (FIX / "statute-134-98-window.html").read_bytes()
ADM_12 = (FIX / "rule-adm-12-chapter.html").read_bytes()
SEC_61 = (FIX / "statute-16-61-window.html").read_bytes()      # the section runs past the end of the window
SEC_973 = (FIX / "statute-16-973-window.html").read_bytes()    # the section ends exactly at the end of the window
FURNITURE = ("Down", "Menu»", "nodeOwnerPath", "/statutes/statutes", "Related»")


def statute(raw):
    return ing.to_text(raw, "html", "statute", "wisconsin")


# ---- statute pages: a window of sections, one section sliced out of it ----

def test_statute_text_is_only_the_requested_section_in_source_order():
    lines = statute(SEC_979).splitlines()
    assert lines[0] == "16.979 Telecommunications operations and planning."
    assert lines[1].startswith("(2) Powers and duties. The department shall ensure maximum utility")
    assert lines[2].startswith("(a) Develop and maintain a statewide long-range telecommunications plan")
    assert lines[-2].startswith("History: 1977 c. 418;")
    text = "\n".join(lines)
    assert "16.977" not in text                      # the neighbouring section in the window
    assert "SUBCHAPTER VIII" not in text             # a heading carries no section: it is not this one


def test_statute_text_does_not_print_the_hidden_reference_labels_twice():
    t = statute(SEC_979)
    assert "16.979(2)(a)" not in t and "16.979 History" not in t
    assert "16.97916.979" not in t


def test_statute_text_keeps_link_text_inside_sentences_and_collapses_spaces():
    t = statute(SEC_134)
    assert "(1) Definitions. In this section:" in t.splitlines()
    assert "Licenses personal information in this state." in t
    assert "<" not in t and "&amp;" not in t and "\xa0" not in t
    assert "  " not in t


def test_statute_text_keeps_history_and_court_annotations():
    lines = statute(SEC_134).splitlines()
    assert "History: 2005 a. 138; 2007 a. 20; 2007 a. 97 s. 238." in lines
    assert any(l.startswith("This section does not create a private right of action. Fox v. Iowa Health System")
               for l in lines)


def test_statute_text_ends_with_the_legislatures_own_certification_line():
    last = statute(SEC_979).splitlines()[-1]
    assert last.startswith("2023-24 Wisconsin Statutes updated through 2025 Wis. Act 247")
    assert last.endswith("(Published 11-4-26)")


def test_statute_section_comes_from_the_page_title_and_is_not_a_prefix_match():
    # the window holds 16.977 and 16.979; the page is titled 16.979, so the text of other sections is not taken
    t = statute(SEC_979)
    assert t.startswith("16.979 Telecommunications operations and planning.\n")
    assert "Information technology portfolio" not in t


def test_statute_page_not_titled_for_one_section_or_without_a_document_region_is_refused():
    whole = SEC_979.replace(b"<title>Wisconsin Legislature: 16.979</title>",
                            b"<title>Wisconsin Legislature: subch. VII of ch. 16</title>")
    with pytest.raises(ValueError, match="window of sections"):
        statute(whole)
    with pytest.raises(ValueError, match="window of sections|document region"):
        statute(b"<html><body><p>Not found</p></body></html>")


def test_section_cut_off_by_the_end_of_the_window_is_refused():
    # 16.61 is the last section in its window and the window stops at (5)(b): the page holds
    # about half of the section and no history line, so it is not the section
    with pytest.raises(ValueError, match="ends at the end of the window"):
        statute(SEC_61)


def test_section_that_ends_at_the_end_of_the_window_with_its_history_line_is_kept_without_page_furniture():
    lines = statute(SEC_973).splitlines()
    assert lines[-2] == ("History: 2001 a. 16 ss. 367 to 369, 1030 to 1030m; 2003 a. 33 ss. 777 to 781; "
                         "Stats. 2003 s. 16.973; 2007 a. 1, 20; 2015 a. 55, 118; 2015 a. 197 s. 51; 2017 a. 369.")
    assert lines[-1].startswith("2023-24 Wisconsin Statutes updated through")
    t = "\n".join(lines)
    assert not any(f in t for f in FURNITURE)


# ---- administrative code pages: the whole chapter ----

def test_rule_text_is_chapter_title_toc_then_each_section_with_its_history():
    lines = ing.to_text(ADM_12, "html", "rule", "wisconsin").splitlines()
    assert lines[0] == "Chapter Adm 12"
    assert lines[1] == "ELECTRONIC RECORDS MANAGEMENT- STANDARDS AND REQUIREMENTS"
    assert lines[2] == "Adm 12.01 Authority."
    assert lines.index("Adm 12.01 Authority.") < lines.index("Adm 12.06 Initial applicability.")
    assert any(l.startswith("Adm 12.01 Authority. This chapter is promulgated under the authority of s. 16.611, Stats.")
              for l in lines)
    assert "History: Cr. Register, November, 2000, No. 539, eff. 5-1-01." in lines
    assert lines[-1].startswith("Published under s. 35.93, Stats.")
    # the last section of the chapter is the last element of the page: its history line is the printed one
    # and the page's navigation and hidden metadata do not run on after it
    printed = [l for l in lines if l.startswith("History:")]
    assert printed[-1].endswith("eff. 5-1-01.") and len(printed[-1]) < 120
    assert not any(f in "\n".join(lines) for f in FURNITURE)


def test_rule_text_drops_navigation_and_keeps_the_chapter_note():
    t = ing.to_text(ADM_12, "html", "rule", "wisconsin")
    assert "Skip navigation" not in t and "Up" not in t.splitlines()
    assert "Note: Chapter Adm 12 as it existed on November 30, 2000 was repealed" in t
    assert "Ch. Adm 12 Note" not in t


# ---- identity, versions, dates ----

ST = {"id": "wi-stat-16-979", "doc_type": "statute", "jurisdiction": "wisconsin",
      "citation": "Wis. Stat. s. 16.979", "title": "Telecommunications operations and planning"}
RULE = {"id": "wi-adm-12", "doc_type": "rule", "jurisdiction": "wisconsin",
        "citation": "Wis. Admin. Code ch. Adm 12",
        "title": "Chapter Adm 12 - Electronic Records Management- Standards And Requirements"}


def test_statute_identity_needs_the_cited_section_as_the_first_words():
    states.check_identity(ST, statute(SEC_979), "html")
    other = dict(ST, citation="Wis. Stat. s. 16.97", id="wi-stat-16-97")
    with pytest.raises(ValueError, match="not Wis. Stat. s. 16.97"):
        states.check_identity(other, statute(SEC_979), "html")


def test_rule_identity_needs_the_chapter_number_and_title_in_the_text():
    states.check_identity(RULE, ing.to_text(ADM_12, "html", "rule", "wisconsin"), "html")
    with pytest.raises(ValueError, match="title"):       # the seed title is checked as well as the chapter number
        states.check_identity(dict(RULE, title="Chapter Adm 12 - Records Of Something Else"),
                              ing.to_text(ADM_12, "html", "rule", "wisconsin"), "html")
    with pytest.raises(ValueError, match="not Wis. Admin. Code ch. Adm 13"):
        states.check_identity(dict(RULE, citation="Wis. Admin. Code ch. Adm 13"),
                              ing.to_text(ADM_12, "html", "rule", "wisconsin"), "html")


def test_statute_version_is_the_publication_date_the_legislature_prints_and_no_effective_date():
    t = statute(SEC_979)
    assert states.source_version(t, "statute", "wisconsin", "html") == "Published 11-4-26"
    assert states.effective_date(t, "statute", "wisconsin") is None


def test_rule_has_no_version_and_no_effective_date():
    t = ing.to_text(ADM_12, "html", "rule", "wisconsin")
    assert states.source_version(t, "rule", "wisconsin", "html") == ""
    assert states.effective_date(t, "rule", "wisconsin") is None


# ---- DET policy and standard PDFs: the version each prints ----

SI2 = (FIX / "flaw-remediation-si-2.pdf").read_bytes()
HANDBOOK_COVER = ing.to_text((FIX / "policy-handbook-first-pages.pdf").read_bytes(), "pdf", "policy", "wisconsin")  # pages 1 to 3 of the real PDF


def test_handbook_version_is_its_printed_revision_date_and_the_effective_date_is_the_label_beside_it():
    assert states.source_version(HANDBOOK_COVER, "policy", "wisconsin", "pdf") == "Revision Date 3/10/2026"
    assert states.effective_date(HANDBOOK_COVER, "policy", "wisconsin") == "2020-11-11"


def test_standard_without_a_cover_block_takes_the_last_row_of_its_issuance_table_and_has_no_effective_date():
    text = ing.to_text(SI2, "pdf", "standard", "wisconsin")
    assert states.source_version(text, "standard", "wisconsin", "pdf") == "Version 1.2, issued 7-13-26"
    assert states.effective_date(text, "standard", "wisconsin") is None


def test_pdf_with_no_printed_version_has_none():
    assert states.source_version("Acceptable Use\n\nEffective Date: March 10, 2025\n", "policy", "wisconsin", "pdf") == ""
