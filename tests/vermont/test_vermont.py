"""Vermont: the Legislature's full-chapter statute pages, the portal's web policy page, and the identity an executive
order's own heading prints. Fixtures are real bytes with the page furniture: chapter 69 and chapter 62 (a chapter with
subchapters) of Title 3 and Title 9, the vermont.gov accessibility policy page, and executive order 2-18's PDF."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "vermont"
CH69 = (FIX / "ch69-fullchapter.html").read_bytes()
CH62 = (FIX / "ch62-fullchapter.html").read_bytes()
ACCESS = (FIX / "accessibility-policy.html").read_bytes()
EO218 = (FIX / "eo-02-18.pdf").read_bytes()
SRC69 = {"id": "vt-3-vsa-69", "jurisdiction": "vermont", "doc_type": "statute",
         "citation": "3 V.S.A. chapter 69", "title": "Title 3, Chapter 69. Division of Artificial Intelligence"}
SRC_EO = {"id": "vt-eo-02-18", "jurisdiction": "vermont", "doc_type": "executive_order",
          "citation": "Executive Order 02-18", "title": "Internet Neutrality in State Procurement"}


def test_the_state_is_found_by_name():
    assert "vermont" in states.modules(refresh=True)


def test_a_chapter_is_its_title_and_chapter_headings_then_each_section_after_a_blank_line():
    text = ing.to_text(CH69, "html", "statute", "vermont")
    lines = text.splitlines()
    assert lines[:2] == ["Title 3: Executive", "Chapter 069: Division of Artificial Intelligence"]
    assert "\n\n§ 5022. Division of Artificial Intelligence\n" in text
    assert text.index("§ 5021.") < text.index("§ 5022.") < text.index("§ 5023.")
    assert any(l.startswith("(a) Creation. There is established the Division of Artificial Intelligence within the "
                            "Agency of Digital Services to review all aspects") for l in lines)
    assert text.rstrip().endswith("2025, No. 156 (Adj. Sess.), § 5, eff. June 17, 2026.)")


def test_no_menu_script_sidebar_or_footer_leaks_into_a_statute():
    text = ing.to_text(CH69, "html", "statute", "vermont")
    for leak in ("<", "&amp;", "Print", "Vermont Statutes Online", "Statutes Search", "Lexis", "Capitol Police",
                 "function", "Legislative Email", "Contains:"):
        assert leak not in text


def test_a_chapter_with_subchapters_keeps_each_subchapter_heading_in_its_place():
    text = ing.to_text(CH62, "html", "statute", "vermont")
    lines = text.splitlines()
    assert lines[1] == "Chapter 062: Protection of Personal Information"
    assert "Subchapter 001: General Provisions" in lines
    assert text.index("Subchapter 001") < text.index("§ 2430.") < text.index("Subchapter 002")


def test_a_page_with_no_chapter_text_is_refused():
    with pytest.raises(ValueError, match="no chapter text"):
        ing.to_text(CH69.replace(b'class="statute-chapter"', b'class="x"'), "html", "statute", "vermont")


def test_a_statute_must_be_the_chapter_cited():
    text = ing.to_text(CH69, "html", "statute", "vermont")
    ing.check_identity(SRC69, text, "html")
    with pytest.raises(ValueError, match="not 3 V.S.A. chapter 56"):
        ing.check_identity({**SRC69, "citation": "3 V.S.A. chapter 56"}, text, "html")
    with pytest.raises(ValueError, match="not 22 V.S.A. chapter 69"):
        ing.check_identity({**SRC69, "citation": "22 V.S.A. chapter 69"}, text, "html")


def test_a_web_policy_page_is_its_heading_and_body_without_menus_styles_or_footer():
    text = ing.to_text(ACCESS, "html", "policy", "vermont")
    lines = text.splitlines()
    assert lines[0] == "Accessibility Policy"
    assert "Accessibility Statement for Official Vermont Government Websites" in lines
    for leak in ("<", "text-decoration", "list-style", "Skip to", "Copyright"):
        assert leak not in text


def test_an_executive_order_must_print_its_own_number_in_its_heading():
    text = ing.to_text(EO218, "pdf", "executive_order", "vermont")
    ing.check_identity(SRC_EO, text, "pdf")            # the order prints "NO. 2-18"
    with pytest.raises(ValueError, match="Executive Order 04-18"):
        ing.check_identity({**SRC_EO, "citation": "Executive Order 04-18"}, text, "pdf")


def test_an_order_that_only_mentions_the_number_is_not_that_order():
    text = ing.to_text(EO218, "pdf", "executive_order", "vermont").replace("EXECUTIVE ORDER NO. 2-18", "AN ORDER")
    with pytest.raises(ValueError, match="Executive Order 02-18"):
        ing.check_identity(SRC_EO, text + "\nsee Executive Order 02-18\n", "pdf")
