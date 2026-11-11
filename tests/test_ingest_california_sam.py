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
           "citation": "SAM chapter 5900",
           "title": "State Administrative Manual chapter 5900: Information Technology - Disposal of IT Equipment"}
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


def test_ccr_nested_lists_use_the_designators_the_page_draws_and_the_text_has_no_site_chrome():
    t = ccr(CCR_10)
    assert "a. For purposes of this chapter, and unless the context expressly indicates otherwise" in t.splitlines()
    assert '  (1) “Digitally signed communication” is a message' in t
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


# ---- list markers: the real SAM 4900 page (snapshot of 2026-11-11) -----------------------------

SNAP = Path(__file__).resolve().parent.parent / "_meta" / "snapshots"
SAM_4900 = (SNAP / "ca-sam-4900.html").read_bytes()


def test_sam_lower_latin_list_is_lettered_like_lower_alpha():
    """SAM 4983: <ol style="list-style-type: lower-latin;"> shows a. b. c. in a browser."""
    t = sam(SAM_4900)
    assert "  a. Data classification (e.g., public, private, internal, confidential, restricted) of information assets" in t
    assert "  b. Host location (e.g., on-premises, off-premises, hybrid, or multi-cloud)" in t
    assert "  1. Data classification" not in t


def test_sam_list_style_with_a_second_property_still_sets_the_marker():
    """`upper-roman; margin-left: 40px` shows I. II. III.; `lower-roman; margin-left: 80px` shows i. ii."""
    t = sam(SAM_4900)
    assert "I. Identify and define the cloud computing technical and security requirements" in t
    assert "II. Identify a cloud service model" in t
    assert "III. The use of cloud services must be consistent" in t
    # the real page's `upper-roman; margin-left: 40px` and `lower-roman; margin-left: 80px` lists
    assert "I. Four CDT managed Internet connections" in t
    assert "II. The CDT SD-WAN Service, required for the use of Internet circuits" in t
    assert "i. CDT may allow the direct offloading through a CDT SD-WAN edge device" in t
    assert "iii. Traffic must be inspected by CDT or CDT approved cloud inspection point." in t


def test_sam_every_list_marker_of_chapter_4900_is_known():
    # no list item of 4900 falls back to a decimal marker when its source style says otherwise
    html = (b'<main><h1>Chapter 1 - Chapter-View</h1><div>Please wait... We are generating the manual...</div>'
            b'<div class="row"><ol style="list-style-type: lower-latin;"><li>x</li></ol>'
            b'<ol style="list-style-type: upper-latin;"><li>y</li></ol>'
            b'<ol style="margin-left: 40px;"><li>z</li></ol></div><hr /><script>1</script></main>')
    assert sam(html).splitlines()[1:] == ["a. x", "A. y", "1. z"]


def test_sam_unknown_list_style_is_an_error_not_a_decimal_list():
    html = (b'<main><h1>Chapter 1 - Chapter-View</h1><div>Please wait... We are generating the manual...</div>'
            b'<div class="row"><ol style="list-style-type: hebrew;"><li>x</li></ol></div><hr /><script>1</script></main>')
    with pytest.raises(ValueError, match="hebrew"):
        sam(html)


# ---- identity: the seed title is the chapter's title in the manual's contents page ---------------

SAM_TOC = (FIX / "sam-toc.html").read_bytes()      # https://www.dgs.ca.gov/Resources/SAM/TOC, fetched 2026-11-11


def test_sam_contents_page_titles_are_read_by_chapter_number():
    titles = ing.sam_toc_titles(SAM_TOC)
    assert titles["5900"] == "Information Technology - Disposal of IT Equipment"
    assert titles["4900"] == "Information Technology - California Department of Technology"


def test_sam_seed_titles_are_state_administrative_manual_chapter_n_colon_the_contents_title():
    import yaml
    manifest = yaml.safe_load((Path(__file__).resolve().parent.parent / "_meta" / "source-manifest.yml").read_text())
    titles = ing.sam_toc_titles(SAM_TOC)
    seeded = [e for e in manifest["sources"]
              if e.get("jurisdiction") == "california" and e["id"].startswith("ca-sam-")]
    assert len(seeded) == 7
    for e in seeded:
        n = e["citation"].rsplit(" ", 1)[1]
        assert e["title"] == f"State Administrative Manual chapter {n}: {titles[n]}", e["id"]


SRC_SAM = {"id": "ca-sam-5900", "doc_type": "policy", "jurisdiction": "california",
           "citation": "SAM chapter 5900",
           "title": "State Administrative Manual chapter 5900: Information Technology - Disposal of IT Equipment"}


def test_sam_identity_refuses_a_title_that_is_not_the_manuals_chapter_title_form():
    ing.check_identity(SRC_SAM, sam(SAM_5900))
    for bad in ("totally wrong title", "State Administrative Manual chapter 5000: Information Technology - Maintenance Records",
                "State Administrative Manual chapter 5900: "):
        with pytest.raises(ValueError, match="title"):
            ing.check_identity({**SRC_SAM, "title": bad}, sam(SAM_5900))


def test_ccr_identity_title_is_the_whole_chapter_heading_not_a_part_of_it():
    ing.check_identity(SRC_CCR10, ccr(CCR_10))
    for bad in ("Signatures", "Digital", "Digital Signatures and More", "digital signatures"):
        with pytest.raises(ValueError, match="not the cited"):
            ing.check_identity(dict(SRC_CCR10, title=bad), ccr(CCR_10))
