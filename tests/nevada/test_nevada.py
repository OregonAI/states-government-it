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


# ---- a section slice of a whole-chapter NRS page (NRS 281.195) ----------------------------------
# Fixture: the real NRS 281 page, cut to its head (revision stamp, whole table of contents), the first two body
# sections, sections 281.190 to 281.210 with the group headings printed between them, and the chapter's last
# section with the page's closing markup.
NRS281 = (FIX / "nrs-281-trimmed.html").read_bytes()
_SLICE = {"section_start": "281.195", "section_end_before": "281.210"}


def _slice_src(**kw):
    return {"id": "nv-nrs-281-195", "jurisdiction": "nevada", "doc_type": "statute", "citation": "NRS 281.195",
            "title": "NRS 281.195: access by a state agency to computers", "format": "html", "slice": _SLICE, **kw}


def _sliced(slice_=_SLICE):
    return ing.to_text(NRS281, "html", "statute", "nevada", slice_)


def test_slice_starts_at_the_first_heading_not_at_the_table_of_contents_or_the_page_head():
    lines = _sliced().splitlines()
    assert lines[0].startswith("NRS 281.195 Access by state agency to computers assigned or loaned")
    assert not any(l.startswith("[Rev.") or l.startswith("CHAPTER 281") for l in lines)


def test_slice_includes_every_subsection_of_the_section_through_its_history_line():
    t = _sliced()
    for needle in ("1. Except as otherwise provided in subsection 3, a state agency that accesses",
                   "(e) The name of each person who will be authorized or required to archive,",
                   "6. Each state agency that has adopted a policy for the use of the computers",
                   "(c) “State agency” means an agency, bureau, board, commission, department, division"):
        assert needle in t
    assert t.splitlines()[-1] == "(Added to NRS by 2005, 671)"


def test_slice_excludes_the_next_section_the_previous_section_and_the_group_headings():
    t = _sliced()
    assert "281.210" not in t and "relatives" not in t
    assert "281.190" not in t and "Unlawful withholding" not in t
    assert "MISCELLANEOUS PROVISIONS AND PROHIBITIONS" not in t and "USE OF COMPUTERS" not in t
    assert "NRS 281.002" not in t


def test_slice_takes_the_body_heading_when_the_table_of_contents_prints_the_same_line():
    full = ing.to_text(NRS281, "html", "statute", "nevada").splitlines()
    heading = [l for l in full if l.startswith("NRS 281.195 ")]
    assert len(heading) == 2                       # contents entry and body heading
    assert _sliced().splitlines()[0] == heading[0]


def test_slice_refuses_a_section_the_page_does_not_print_and_an_end_that_does_not_follow():
    with pytest.raises(ValueError, match="281.196"):
        _sliced({"section_start": "281.196", "section_end_before": "281.210"})
    with pytest.raises(ValueError, match="281.190"):
        _sliced({"section_start": "281.195", "section_end_before": "281.190"})


def test_slice_identity_accepts_the_cited_section_and_refuses_another():
    ing.derive(_slice_src(), NRS281)
    with pytest.raises(ValueError, match="not NRS 281.190"):
        ing.derive(_slice_src(citation="NRS 281.190", slice={"section_start": "281.195",
                                                              "section_end_before": "281.210"}), NRS281)


def test_slice_identity_refuses_a_page_of_another_chapter():
    with pytest.raises(ValueError):
        ing.derive(_slice_src(), NRS)


def test_slice_notes_say_the_source_is_the_whole_chapter_page_and_this_is_one_section():
    fmt, text = ing.derive(_slice_src(), NRS281)
    notes = ing.conversion_notes(_slice_src(), fmt, text)
    assert "whole NRS chapter 281" in notes and "281.195" in notes and "281.210" in notes
    assert "so this document is the whole chapter" not in notes


def test_slice_identity_refuses_a_repealed_section_and_a_section_printed_in_versions():
    rep = {"section_start": "281.157", "section_end_before": "281.1571"}
    from src.states import nevada
    text = "NRS 281.157 Commission: Definition. Repealed. (See chapter 88, Statutes of Nevada 2025, at page 492.)\n"
    with pytest.raises(ValueError, match="repealed|not in force"):
        nevada.check_identity(_slice_src(citation="NRS 281.157", slice=rep), text, "the page")
    text = "NRS 281.129 Deductions. [Effective July 1, 2049.]\n1. x\n(Added to NRS by 1981, 655)\n"
    with pytest.raises(ValueError, match="Effective|effective"):
        nevada.check_identity(_slice_src(citation="NRS 281.129", slice={"section_start": "281.129",
                                      "section_end_before": "281.130"}), text, "the page")


def test_slice_identity_refuses_a_slice_that_runs_into_the_next_section():
    from src.states import nevada
    text = ("NRS 281.195 Access by state agency.\n1. x\n(Added to NRS by 2005, 671)\n"
            "NRS 281.210 Relatives.\n1. y\n(Added to NRS by 1957, 1)\n")
    src = _slice_src(slice={"section_start": "281.195", "section_end_before": "281.220"})
    with pytest.raises(ValueError, match="not NRS 281.195"):
        nevada.check_identity(src, text, "the page")


def test_slice_identity_refuses_a_slice_that_does_not_open_on_the_cited_heading():
    from src.states import nevada
    text = ("Stray line before the section.\nNRS 281.195 Access by state agency.\n1. x\n"
            "(Added to NRS by 2005, 671)\n")
    with pytest.raises(ValueError, match="not NRS 281.195"):
        nevada.check_identity(_slice_src(), text, "the page")
