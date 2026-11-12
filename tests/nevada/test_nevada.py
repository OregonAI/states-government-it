"""Seam: src.ingest for Nevada: NRS and NAC pages (leg.state.nv.us), their identity check, and the note
on scan-layer PDFs. Fixtures are real bytes the Legislative Counsel Bureau served on 2026-11-12: the NAC
chapter whole, the NRS chapter cut to its head (title, revision stamp, table of contents), two sections and
its last section, with the page's markup and head kept."""
from pathlib import Path

import pytest

from src import ingest as ing

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "nevada"
NRS = (FIX / "nrs-242-trimmed.html").read_bytes()
NAC = (FIX / "nac-242-chapter.html").read_bytes()


def _src(doc_type, citation, title):
    return {"id": "x", "jurisdiction": "nevada", "doc_type": doc_type, "citation": citation, "title": title,
            "format": "html"}


def test_nrs_text_starts_with_revision_stamp_and_chapter_title_one_line_per_paragraph():
    lines = ing.to_text(NRS, "html", "statute", "nevada").splitlines()
    assert lines[0] == "[Rev. 4/15/2026 11:45:45 AM--2025]"
    assert lines[1] == "CHAPTER 242 - INFORMATION SERVICES"
    assert "NRS 242.015 “Board” defined." in lines
    assert ("NRS 242.017 “Chief” or “Chief Information Officer” defined. “Chief” or “Chief Information Officer” "
            "means the Chief of the Governor’s Technology Office within the Office of the Governor.") in lines


def test_nrs_text_drops_the_wingdings_continuation_glyph_but_keeps_the_words():
    t = ing.to_text(NRS, "html", "statute", "nevada")
    assert "Ê" not in t
    assert "to encourage the development of strategies to prepare for and mitigate risks to" in t


def test_nrs_text_keeps_history_lines_and_has_no_markup():
    t = ing.to_text(NRS, "html", "statute", "nevada")
    assert "(Added to NRS by 2023, 3558; A 2025, 1957)" in t
    assert "(Added to NRS by 2025, 36th Special Session, 40)" in t
    assert "<" not in t and "&#" not in t and "\xa0" not in t and " " not in t


def test_nac_text_has_the_whole_rule_with_its_history():
    t = ing.to_text(NAC, "html", "rule", "nevada")
    assert "NAC 242.110 Adoption by reference of State Information Security Policies, Standards and Procedures." in t
    assert "(Added to NAC by Dep’t of Data Processing, eff. 9-16-92;" in t


def test_identity_accepts_the_cited_nrs_chapter_and_refuses_another():
    ing.derive({**_src("statute", "NRS ch. 242", "Chapter 242 - Information Services")}, NRS)
    with pytest.raises(ValueError, match="not NRS ch. 603A"):
        ing.derive({**_src("statute", "NRS ch. 603A", "Chapter 603A")}, NRS)


def test_identity_for_a_rule_needs_the_chapter_heading():
    ing.derive(_src("rule", "NAC ch. 242", "CHAPTER 242 - INFORMATION SERVICES"), NAC)
    with pytest.raises(ValueError, match="not NAC ch. 480"):
        ing.derive(_src("rule", "NAC ch. 480", "CHAPTER 480 - SECURITY OF INFORMATION SYSTEMS"), NAC)


def test_scan_layer_pdf_gets_a_note_that_the_text_is_the_publishers_machine_reading():
    from src import states
    h = states.hook("nevada", "extra_notes")
    note = h({"scan_layer": True}, "pdf", "text", None, "")
    assert "machine" in note and "not human-verified" in note.lower()
    assert h({}, "pdf", "text", None, "") == ""


# ---- identity of policy and standard PDFs: the heading block, not any mention -----------------

POLICY_100 = (FIX / "nv-sec-100-page-1.pdf").read_bytes()
STANDARD_3_02_01 = (FIX / "nv-sec-s-3-02-01.pdf").read_bytes()

_P100 = {"id": "nv-sec-100", "jurisdiction": "nevada", "doc_type": "policy", "format": "pdf",
         "citation": "State Information Security Program Policy 100", "title": "State Information Security Program Policy",
         "identity_text": "State Information Security Program Policy"}
_S30201 = {"id": "nv-sec-s-3-02-01", "jurisdiction": "nevada", "doc_type": "standard", "format": "pdf",
           "citation": "S.3.02.01", "title": "Data Sensitivity", "identity_text": "S.3.02.01 Data Sensitivity"}


def test_identity_accepts_policy_100_and_a_standard_by_their_own_heading():
    ing.derive(_P100, POLICY_100)
    ing.derive(_S30201, STANDARD_3_02_01)


def test_identity_refuses_a_standard_that_only_cites_policy_100():
    # the standard's scope paragraph prints "State Information Security Program Policy"; its heading does not
    body = " ".join(ing.to_text(STANDARD_3_02_01, "pdf", "standard", "nevada").split())
    assert "State Information Security Program Policy" in body
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.derive(_P100, STANDARD_3_02_01)


def test_identity_refuses_policy_100_where_a_standard_is_cited():
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.derive(_S30201, POLICY_100)
