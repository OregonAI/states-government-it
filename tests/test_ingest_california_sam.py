"""Seam: src.ingest, State Administrative Manual chapters (dgs.ca.gov). Fixtures are the real
pages served on 2026-11-11: the Department of General Services' chapter views (chapters 5000
and 5900, whole) and the Secretary of State's two California Code of Regulations chapters."""
from pathlib import Path

import pytest

from src import ingest as ing

FIX = Path(__file__).resolve().parent / "fixtures"
SAM_5000 = (FIX / "sam-chapter-5000.html").read_bytes()
SAM_5900 = (FIX / "sam-chapter-5900.html").read_bytes()


def sam(raw):
    return ing.to_text(raw, "html", "policy", "california")


def test_sam_chapter_text_opens_with_the_chapter_line_then_each_section_in_order():
    lines = sam(SAM_5900).splitlines()
    assert lines[0] == "Chapter 5900 - Chapter-View"
    heads = [l for l in lines if l.endswith(tuple(f" - {n}" for n in (5901, 5902, 5903, 5951, 5952, 5953)))]
    assert heads == ["PURPOSE - 5901", "BASIC POLICY - 5902", "AGENCY RESPONSIBILITY - 5903",
                     "PURPOSE - 5951", "BASIC POLICY - 5952", "AGENCY RESPONSIBILITY - 5953"]


def test_sam_section_keeps_its_revision_line_and_unwraps_links_into_the_sentence():
    t = sam(SAM_5900)
    assert "(Reviewed: 02/2015 )" in t.splitlines()
    assert ("Salvage value of state-owned IT equipment (SAM Section 4819.2) and purchase option "
            "credits for leased IT equipment are a source of value to the state.") in t


def test_sam_text_has_no_site_navigation_table_of_contents_scripts_or_markup():
    t = sam(SAM_5900)
    assert "<" not in t and "printChapterView" not in t and "Skip to Main Content" not in t
    assert "Please wait" not in t and "Back to Top" not in t and "scWebEditInput" not in t
    assert t.count("BASIC POLICY - 5902") == 1          # the page's contents table is not repeated
    assert "\xa0" not in t and "&rsquo;" not in t


def test_sam_ordered_list_items_get_the_numbers_a_browser_would_print():
    t = sam(SAM_5000)
    assert "1. The time at which the vendor maintenance contact was notified by the state;" in t
    assert "5. Signature of the vendor and a representative of the state." in t


def test_sam_nested_and_lettered_lists_follow_their_list_style():
    html = (b'<main><h1>Chapter 1 - Chapter-View</h1><div class="modal">Please wait... We are generating'
            b' the manual...</div><div class="row"><h1>X - 1</h1><p><strong>(Revised: 01/2020 )</strong></p>'
            b'<p><p><span>Intro:</span></p><ol style="list-style-type: lower-alpha;"><li><span>one</span>'
            b'<ol style="list-style-type: lower-roman;"><li><span>deep</span></li></ol></li>'
            b'<li><span>two</span></li></ol><ul><li><span>dot</span></li></ul></p></div><hr />'
            b'<script>var x;</script></main>')
    assert sam(html).splitlines() == [
        "Chapter 1 - Chapter-View", "X - 1", "(Revised: 01/2020 )", "Intro:",
        "a. one", "  i. deep", "b. two", "• dot"]


def test_sam_page_without_a_chapter_region_is_refused():
    with pytest.raises(ValueError, match="no chapter"):
        sam(b"<html><body><h1>Not the manual</h1></body></html>")


def test_sam_identity_is_the_cited_chapter():
    src = {"id": "ca-sam-5900", "doc_type": "policy", "jurisdiction": "california",
           "citation": "SAM chapter 5900", "title": "Information Technology - Disposal of IT Equipment"}
    ing.check_identity(src, sam(SAM_5900))
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity({**src, "citation": "SAM chapter 5000"}, sam(SAM_5900))


def test_sam_conversion_notes_describe_the_chapter_view_not_a_pdf():
    src = {"id": "ca-sam-5900", "doc_type": "policy", "jurisdiction": "california"}
    n = ing.conversion_notes(src, "html", "x")
    assert "chapter view" in n.lower() and "pdftotext" not in n


def test_sam_has_no_effective_date_label_to_misread():
    assert ing.effective_date(sam(SAM_5900), "policy") is None


# ---- California Code of Regulations chapters the Secretary of State publishes (sos.ca.gov) ----

CCR_10 = (FIX / "ccr-2-div-7-ch-10.html").read_bytes()
CCR_15 = (FIX / "ccr-2-div-7-ch-15.html").read_bytes()


def ccr(raw):
    return ing.to_text(raw, "html", "rule", "california")


def test_ccr_text_is_the_chapter_headings_then_each_regulation_in_source_order():
    lines = ccr(CCR_10).splitlines()
    assert lines[:3] == ["Title 2. Administration", "Division 7. Secretary of State", "Chapter 10. Digital Signatures"]
    assert lines[3] == "\u2022 22000 Definitions."        # the chapter's contents list
    heads = [l for l in lines if l.startswith("2200") and l.endswith(".") and "." in l[:7]]
    assert [h.split(".")[0] for h in heads if h.split(".")[0] in ("22000", "22001", "22002", "22003", "22004", "22005")] == \
        ["22000", "22001", "22002", "22003", "22004", "22005"]
    assert "Note: Authority cited: Section 16.5, Government Code. Reference: Section 16.5, Government Code." in lines


def test_ccr_nested_lists_keep_their_letters_and_numbers_and_the_text_has_no_site_chrome():
    t = ccr(CCR_10)
    assert "a. For purposes of this chapter, and unless the context expressly indicates otherwise" in t.splitlines()
    assert '  1. “Digitally signed communication” is a message' in t
    for chrome in ("Skip to", "Certification Authorities", "Career Opportunities", "<", "\xa0", "&ldquo;"):
        assert chrome not in t


def test_ccr_chapter_15_is_its_own_chapter_text():
    t = ccr(CCR_15)
    assert t.splitlines()[:4] == ["California Code of Regulations", "Title 2. Administration",
                                  "Division 7. Secretary of State",
                                  "Chapter 15. Trustworthy Electronic Document or Record Preservation"]
    assert "Authority Cited: Government Code section 12168.7" in t
    assert "22620.1." in t and "Digital Signatures" not in t


def test_ccr_page_without_the_regulation_region_is_refused():
    with pytest.raises(ValueError, match="no regulation"):
        ccr(b"<html><body><main><h2>Something else</h2></main></body></html>")


SRC_CCR10 = {"id": "ca-ccr-2-div-7-ch-10", "doc_type": "rule", "jurisdiction": "california",
             "citation": "Cal. Code Regs., tit. 2, div. 7, ch. 10", "title": "Digital Signatures"}


def test_ccr_identity_is_the_cited_title_division_and_chapter():
    ing.check_identity(SRC_CCR10, ccr(CCR_10))
    with pytest.raises(ValueError, match="not the cited"):
        ing.check_identity(dict(SRC_CCR10, citation="Cal. Code Regs., tit. 2, div. 7, ch. 15"), ccr(CCR_10))
    with pytest.raises(ValueError, match="not the cited"):
        ing.check_identity(dict(SRC_CCR10, citation="Cal. Code Regs., tit. 2, div. 8, ch. 10"), ccr(CCR_10))
    with pytest.raises(ValueError, match="not the cited"):
        ing.check_identity(dict(SRC_CCR10, citation="Cal. Code Regs., tit. 3, div. 7, ch. 10"), ccr(CCR_10))


def test_ccr_conversion_notes_describe_the_sos_page_not_the_oar_page():
    n = ing.conversion_notes(SRC_CCR10, "html", "x")
    assert "Secretary of State" in n and "OAR" not in n and "rule number" not in n


def test_ccr_has_no_effective_date_label_to_misread():
    assert ing.effective_date(ccr(CCR_10), "rule") is None
