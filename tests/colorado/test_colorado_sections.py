"""Seam: src.ingest for Colorado provisions seeded as a section slice: `slice: {section_start, section_end_before}`.

Two sources serve a whole file where the provision is a few sections of it. The OLLS title file (one
Word-HTML file for the whole of title 24) prints every section heading twice, once in the caption list at
the head of its article and once in the body; a slice is the body, from the heading of the first section to
the line before the heading of the section that follows the last. The Code of Colorado Regulations serves a
whole rule set as one PDF, so a rule inside it (1 CCR 101-9, rule R-24-103-201.5-03) is cut by its printed
rule heading. Fixtures are real bytes fetched 2026-11-13: article 71.3 to article 72 part 5 of
crs2026-title-24.htm (the bytes between two paragraph boundaries, with the file's own head) and the PDF of
1 CCR 101-9 as it stood on the Secretary of State's page (effective 07/01/2026)."""
from pathlib import Path

import pytest

from src import ingest as ing

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "colorado"
CRS = (FIX / "crs-title-24-articles-71-3-to-72-part-5.html").read_bytes()
PROCUREMENT_PDF = (FIX / "ccr-1-101-9-procurement-rules.pdf").read_bytes()

UETA_GOV = {"section_start": "24-71.3-117", "section_end_before": "24-71.3-120"}
PRIVACY = {"section_start": "24-72-501", "section_end_before": "24-72-601"}
CO_UETA = {"id": "co-crs-24-71-3-117", "doc_type": "statute", "jurisdiction": "colorado",
           "citation": "C.R.S. 24-71.3-117 to 24-71.3-119",
           "title": "Electronic Records of State Agencies", "slice": UETA_GOV}
CO_PRIVACY = {"id": "co-crs-24-72-501", "doc_type": "statute", "jurisdiction": "colorado",
              "citation": "C.R.S. 24-72-501 to 24-72-502",
              "title": "Privacy Policies of Governmental Entities", "slice": PRIVACY}
RULE_SLICE = {"section_start": "R-24-103-201.5-03", "section_end_before": "R-24-103-201.5-04"}
CO_RULE = {"id": "co-ccr-1-101-9-it-projects", "doc_type": "rule", "jurisdiction": "colorado", "format": "pdf",
           "url": "https://www.sos.state.co.us/CCR/GenerateRulePdf.do?ruleVersionId=12601&fileName=1%20CCR%20101-9",
           "citation": "1 CCR 101-9, rule R-24-103-201.5-03",
           "title": "Procurement Rules: Information Technology Projects", "slice": RULE_SLICE}


def crs(slice_, raw=CRS):
    return ing.to_text(raw, "html", "statute", "colorado", slice_)


def heads(text):
    return [l.split(". ")[0] for l in text.splitlines() if l.startswith("24-") and ". " in l[:20]]


# ---- statutes -------------------------------------------------------------------------------

def test_a_section_slice_starts_at_the_first_heading_and_includes_every_section_in_range():
    lines = crs(UETA_GOV).splitlines()
    assert lines[0] == "24-71.3-117. Creation and retention of electronic records by political subdivisions."
    assert heads(crs(UETA_GOV)) == ["24-71.3-117", "24-71.3-118", "24-71.3-119"]
    assert "in consultation with the office of information technology" in crs(UETA_GOV)
    # the section's own source note, official comment and the last section's comment stay
    assert any(l.startswith("Source: L. 2002: Entire article added, p. 855") for l in lines)
    assert any(l.startswith("Legislative Note Regarding Adoption of Sections 17-19") for l in lines)


def test_a_section_slice_is_the_body_not_the_caption_list():
    # the caption list at the head of the article prints the same headings as bare lines
    text = crs(UETA_GOV)
    assert text.count("24-71.3-118. Acceptance and distribution of electronic records") == 1
    assert "24-71.3-101. Short title." not in text and "24-71.3-102" not in text


def test_a_section_slice_excludes_the_next_section_and_what_follows():
    text = crs(UETA_GOV)
    assert "24-71.3-120" not in text and "Severability" not in text
    assert "ARTICLE 71.5" not in text.splitlines()


def test_a_slice_that_ends_at_a_part_boundary_drops_the_next_parts_heading_lines():
    lines = crs(PRIVACY).splitlines()
    assert lines[0] == "24-72-501. Definitions."
    assert heads(crs(PRIVACY)) == ["24-72-501", "24-72-502"]
    assert lines[-1].startswith("Source: L. 2002: Entire part added, p. 774")
    assert "PART 6" not in lines and not any("LIMITS ON GOVERNMENT ACCESS" in l for l in lines)
    assert not any(l.startswith("24-72-601") for l in lines)
    assert "PART 5" not in lines          # the part heading belongs to the part, not to its sections


def test_a_slice_with_nothing_but_html_markup_removed_is_plain_lines():
    text = crs(UETA_GOV)
    assert "<" not in text and "\xa0" not in text and "font-family" not in text and "\n\n" not in text


def test_a_section_slice_that_is_missing_is_refused_not_guessed():
    with pytest.raises(ValueError, match="24-71.3-999"):
        crs({"section_start": "24-71.3-999", "section_end_before": "24-71.3-120"})
    with pytest.raises(ValueError, match="24-71.3-998"):
        crs({"section_start": "24-71.3-117", "section_end_before": "24-71.3-998"})
    with pytest.raises(ValueError, match="does not follow"):
        crs({"section_start": "24-71.3-119", "section_end_before": "24-71.3-117"})
    with pytest.raises(ValueError, match="section number"):
        crs({"section_start": "117", "section_end_before": "120"})


def test_a_section_slice_in_a_file_with_the_article_twice_is_refused():
    doubled = CRS.replace(b"</body>", b"<p>ARTICLE 71.3</p></body>")
    with pytest.raises(ValueError, match="more than once"):
        crs(UETA_GOV, doubled)


def test_a_section_slice_identity_is_the_cited_range():
    ing.check_identity(CO_UETA, crs(UETA_GOV))
    ing.check_identity(CO_PRIVACY, crs(PRIVACY))
    with pytest.raises(ValueError, match="not C.R.S. 24-71.3-117 to 24-71.3-118"):
        ing.check_identity(dict(CO_UETA, citation="C.R.S. 24-71.3-117 to 24-71.3-118"), crs(UETA_GOV))
    with pytest.raises(ValueError, match="not C.R.S. 24-71.3-118 to 24-71.3-119"):
        ing.check_identity(dict(CO_UETA, citation="C.R.S. 24-71.3-118 to 24-71.3-119"), crs(UETA_GOV))


def test_a_repealed_single_section_is_not_in_force():
    one = {"section_start": "24-72-100.1", "section_end_before": "24-72-101"}
    src = {"id": "x", "doc_type": "statute", "jurisdiction": "colorado", "citation": "C.R.S. 24-72-100.1",
           "title": "Short title", "slice": one}
    with pytest.raises(ValueError, match="repealed"):
        ing.check_identity(src, crs(one))


def test_section_slice_notes_say_what_was_cut():
    notes = ing.conversion_notes(CO_UETA, "html", crs(UETA_GOV))
    assert "24-71.3-117" in notes and "24-71.3-120" in notes and "title file" in notes


def test_an_article_slice_is_still_read_as_before():
    assert crs({"article": "71.3"}).splitlines()[0] == "ARTICLE 71.3"


# ---- a rule inside a rule set -------------------------------------------------------------

def rule(slice_=RULE_SLICE, raw=PROCUREMENT_PDF):
    return ing.to_text(raw, "pdf", "rule", "colorado", slice_)


def test_a_rule_slice_runs_from_its_heading_to_the_line_before_the_next_rule():
    lines = rule().splitlines()
    assert lines[0] == "R-24-103-201.5-03 Information Technology Projects"
    assert "formal market research is required for major information technology projects" in rule()
    assert "R-24-103-201.5-04" not in rule() and "R-24-103-201.5-02" not in rule()
    assert lines[-1].strip() == "most appropriate information technology requirements in its solicitations."


def test_a_rule_slice_that_is_missing_or_out_of_order_is_refused():
    with pytest.raises(ValueError, match="R-24-103-999"):
        rule({"section_start": "R-24-103-999", "section_end_before": "R-24-103-201.5-04"})
    with pytest.raises(ValueError, match="does not follow"):
        rule({"section_start": "R-24-103-201.5-04", "section_end_before": "R-24-103-201.5-03"})


def test_a_rule_slice_across_a_page_break_is_refused_not_cut_with_the_furniture():
    with pytest.raises(ValueError, match="page break"):
        rule({"section_start": "R-24-103-201.5-01", "section_end_before": "R-24-103-201.5-03"})


def test_a_slice_of_a_repealed_rule_pdf_is_refused():
    repealed = (FIX / "ccr-8-1501-6-repealed.pdf").read_bytes()
    with pytest.raises(ValueError, match="repealed|no text|heading"):
        rule(raw=repealed)


def test_a_rule_slice_identity_is_the_cited_rule_of_the_cited_rule_set():
    ing.check_identity(CO_RULE, rule())
    with pytest.raises(ValueError, match="not the cited"):
        ing.check_identity(dict(CO_RULE, citation="1 CCR 101-9, rule R-24-103-201.5-04"), rule())
    with pytest.raises(ValueError, match="not the cited"):
        ing.check_identity(dict(CO_RULE, citation="1 CCR 101-1, rule R-24-103-201.5-03"), rule())


def test_a_rule_slice_has_no_invented_effective_date_and_says_it_is_a_slice():
    text = rule()
    assert ing.effective_date(text, "rule", "colorado") is None
    notes = ing.conversion_notes(CO_RULE, "pdf", text)
    assert "R-24-103-201.5-03" in notes and "not part of the slice" in notes and "letter fragments" not in notes
