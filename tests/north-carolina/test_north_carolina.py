"""North Carolina through the shared seam (src.ingest / src.states): the General Assembly's article pages, the OAH
subchapter pages and NCDIT's own web page. Fixtures are real bytes fetched on 2026-11-11: Article 84 of G.S. chapter
143 whole, Article 15 of chapter 143B cut after its first sections (head and style sheet kept), the OAH page of
09 NCAC subchapter 06A whole and of 06B cut after its first rules, and the NCDIT pressing-needs guidance page
whole with its menus, scripts and footer."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "north-carolina"
ART84 = (FIX / "ncgs-143-article-84.html").read_bytes()
ART15 = (FIX / "ncgs-143b-article-15-part-1.html").read_bytes()
R06A = (FIX / "09-ncac-06a-subchapter-rules.html").read_bytes()
R06B = (FIX / "09-ncac-06b-subchapter-rules-head.html").read_bytes()
GUIDE = (FIX / "it-nc-gov-pressing-needs-guidance.html").read_bytes()
NC = "north-carolina"


def text(raw, doc_type):
    host = "it.nc.gov" if doc_type == "policy" else ""         # the shared flow passes the seed url's host
    return ing.to_text(raw, "html", doc_type, NC, None, host)


def test_the_state_is_found_by_its_hyphenated_name():
    assert NC in states.modules(refresh=True)


# ---- statutes: one article per page -------------------------------------------------------

def test_an_article_page_is_the_article_title_then_one_line_per_paragraph_with_a_blank_line_before_each_section():
    t = text(ART84, "statute")
    lines = t.splitlines()
    assert lines[:3] == ["Article 84.", "Various Technology Regulations.", ""]
    assert lines[3].startswith("§ 143-800. State entities and ransomware payments.")
    assert "\n\n§ 143-805. Prohibit viewing of pornography on government networks and devices.\n" in t
    # tabs and non-breaking spaces inside a paragraph are squeezed to single spaces
    assert "(c) The following definitions apply in this section:" in lines
    assert "consult with the Department of Information Technology in accordance with G.S. 143B-1379." in t


def test_the_session_law_history_stays_on_the_last_paragraph_of_a_section():
    t = text(ART84, "statute")
    assert "or other entity of the executive, judicial, or legislative branches of State government." in t
    assert "(2021-180, s. 38.13(a).)" in t
    assert t.rstrip().endswith("(2024-26, s. 7(a); 2026-34, s. 3(a); 2026-44, s. 5.2(a).)")


def test_no_markup_or_style_sheet_leaks_from_the_head_of_the_page():
    for raw in (ART84, ART15):
        t = text(raw, "statute")
        for leak in ("<", ">", "font-family", "text-indent", "&nbsp;", "&sect;", "\t", "\xa0", "DOCTYPE"):
            assert leak not in t
        assert "Chapter 143B - Article 15" not in t          # the page <title> is furniture, not law


def test_article_15_keeps_part_headings_and_repealed_notes_as_published():
    t = text(ART15, "statute")
    lines = t.splitlines()
    assert lines[:4] == ["Article 15.", "Department of Information Technology.", "", "Part 1. General Provisions."]
    assert any(l.startswith("(2) Repealed by Session Laws 2021-180, s. 19A.7A(d)") for l in lines)
    assert "\n\n§ 143B-1321. Powers and duties of the Department; cost-sharing with exempt entities.\n" in t


def test_a_page_with_no_statute_body_is_refused_not_committed():
    with pytest.raises(ValueError, match="no statute text"):
        text(b"<html><body><h1>Not Found</h1></body></html>", "statute")


# ---- identity -----------------------------------------------------------------------------

def src(**kw):
    base = {"id": "nc-x", "jurisdiction": NC, "doc_type": "statute", "citation": "G.S. 143, Article 84",
            "title": "General Statutes, Chapter 143, Article 84. Various Technology Regulations"}
    base.update(kw)
    return base


def test_the_page_must_be_the_cited_article():
    states.check_identity(src(), text(ART84, "statute"), "html")
    with pytest.raises(ValueError, match="not G.S. 143, Article 15"):
        states.check_identity(src(citation="G.S. 143, Article 15"), text(ART84, "statute"), "html")
    with pytest.raises(ValueError, match="not G.S. 143, Article 84"):
        states.check_identity(src(), text(ART15, "statute"), "html")


def test_the_page_must_be_the_cited_chapter_not_only_the_cited_article_number():
    # Article 15 of chapter 143B cited as article 15 of chapter 143: only the chapter differs
    with pytest.raises(ValueError, match="chapter mismatch"):
        states.check_identity(src(citation="G.S. 143, Article 15"), text(ART15, "statute"), "html")
    states.check_identity(src(citation="G.S. 143B, Article 15"), text(ART15, "statute"), "html")


# ---- rules: the OAH subchapter page ---------------------------------------------------------

def test_a_subchapter_page_is_the_subchapter_line_then_each_rule_with_a_blank_line_before_it():
    t = text(R06A, "rule")
    lines = t.splitlines()
    # the page prints the subchapter and section lines in lower case (a style sheet capitalises them on screen)
    assert lines[0] == "subchapter 06a – information technology procurement"
    assert "section .0100 – forms, terms and conditions and definitions" in lines
    assert "09 NCAC 06A .0101 FORMS, TERMS AND CONDITIONS" in lines
    assert "\n\n09 NCAC 06A .0102 DEFINITIONS\n" in t
    # the page is Windows-1252: the en dash and the non-breaking spaces are read, not replaced
    assert "�" not in t and "\xa0" not in t
    assert "Pursuant to G.S. 150B-21.3A, rule Expired May 1, 2015." in lines


def test_the_history_note_of_each_rule_is_kept_with_its_authority():
    t = text(R06B, "rule")
    assert "History Note: Authority G.S. 147-33.76(b1); 147-33.95(b);" in t
    assert "09 NCAC 06B .0102 VERBAL REQUESTS" in t.splitlines()
    assert "Repealed Eff. September 1, 2013." in t.splitlines()


def test_a_rule_page_is_the_cited_subchapter_or_it_is_refused():
    s = {"id": "nc-r", "jurisdiction": NC, "doc_type": "rule", "citation": "09 NCAC Subchapter 06A",
         "title": "SUBCHAPTER 06A – INFORMATION TECHNOLOGY PROCUREMENT"}
    states.check_identity(s, text(R06A, "rule"), "html")
    with pytest.raises(ValueError, match="not 09 NCAC Subchapter 06B"):
        states.check_identity(dict(s, citation="09 NCAC Subchapter 06B",
                                   title="SUBCHAPTER 06B – PROCUREMENT REQUESTS"), text(R06A, "rule"), "html")


# ---- policy: NCDIT's own web page ---------------------------------------------------------

def test_a_web_guidance_page_is_its_title_and_body_without_menus_scripts_or_footer():
    t = text(GUIDE, "policy")
    lines = t.splitlines()
    assert lines[0] == "IT Procurement Guidance for Pressing Needs"
    assert "Procurement of Information Technology Products and Services During a State of Emergency or Pressing Need Situations" in lines
    assert any(l.startswith("Pursuant to N.C.G.S. 143B-1350, along with 09 NCAC 06B .1302:") for l in lines)
    for furniture in ("Contact NCDIT", "Network Menu", "Follow NCDIT", "googletagmanager", "Back to top",
                      "Disclaimer & Terms of Use", "dataLayer", "navbar-top"):
        assert furniture not in t


def test_a_policy_page_with_no_article_region_is_refused():
    with pytest.raises(ValueError, match="no article"):
        text(b"<html><body><main>menu only</main></body></html>", "policy")


def test_the_page_must_print_the_seed_title():
    s = {"id": "nc-p", "jurisdiction": NC, "doc_type": "policy", "format": "html",
         "citation": "NCDIT guidance", "title": "IT Procurement Guidance for Pressing Needs"}
    states.check_identity(s, text(GUIDE, "policy"), "html")
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(dict(s, title="Something Else Entirely"), text(GUIDE, "policy"), "html")


def test_the_shared_flow_reaches_these_readers_and_no_other_combination():
    with pytest.raises(ValueError, match="no to_text"):
        ing.to_text(ART84, "json", "statute", NC)
    with pytest.raises(ValueError, match="no to_text"):
        ing.to_text(ART84, "html", "executive_order", NC)


def test_conversion_notes_say_how_each_page_was_read():
    n = ing.conversion_notes(src(), "html", text(ART84, "statute"))
    assert "General Assembly" in n and "style sheet" in n
    r = {"id": "nc-r", "jurisdiction": NC, "doc_type": "rule", "citation": "09 NCAC Subchapter 06A",
         "title": "SUBCHAPTER 06A – INFORMATION TECHNOLOGY PROCUREMENT"}
    assert "Office of Administrative Hearings" in ing.conversion_notes(r, "html", text(R06A, "rule"))
    p = {"id": "nc-p", "jurisdiction": NC, "doc_type": "policy", "citation": "x", "title": "x"}
    assert "NCDIT" in ing.conversion_notes(p, "html", text(GUIDE, "policy"))


# ---- executive orders: "Executive Order No. 24" is the citation, not the 24-01 form the shared check expects ----

# the order's first lines as the Governor's page prints them (the PDF behind it is an image-only scan read by OCR)
EO24 = ("September 2, 2025\nExecutive Order No. 24\nAdvancing Trustworthy Artificial Intelligence That Benefits "
        "All North Carolinians\nWhereas, artificial intelligence (\u201cAI\u201d) is a transformational and rapidly "
        "evolving technology\n")


def eo(**kw):
    base = {"id": "nc-eo-24", "jurisdiction": NC, "doc_type": "executive_order", "citation": "Executive Order No. 24",
            "title": "Executive Order No. 24: Advancing Trustworthy Artificial Intelligence That Benefits All North Carolinians"}
    base.update(kw)
    return base


def test_an_order_is_the_cited_number_or_it_is_refused():
    states.check_identity(eo(), EO24, "pdf")
    states.check_identity(eo(), EO24.replace("Order No. 24", "Order  No.  24"), "pdf")   # OCR may space it out
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(eo(citation="Executive Order No. 2"), EO24, "pdf")           # 24 is not 2
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(eo(citation="Executive Order No. 25"), EO24, "pdf")
