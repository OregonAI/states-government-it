"""New Hampshire: the General Court's RSA pages (gc.nh.gov/rsa/html). Fixtures are the real bytes the site served on
2026-11-12: the whole chapter 5-D and chapter 21-R pages and the page of one section, 359-C:19 (the breach subdivision)."""
import importlib
from pathlib import Path

import pytest

from src import states

FX = Path(__file__).parent.parent / "fixtures" / "new-hampshire"
nh = importlib.import_module("src.states.new-hampshire")
CH5D = (FX / "chapter-5-d.html").read_bytes()
CH21R = (FX / "chapter-21-r.html").read_bytes()
SEC = (FX / "section-359-c-19.html").read_bytes()

CH_SRC = {"id": "nh-st-5-d", "jurisdiction": "new-hampshire", "doc_type": "statute",
          "citation": "RSA Chapter 5-D", "title": "Chapter 5-D. Use of Artificial Intelligence by State Agencies",
          "format": "html"}
SEC_SRC = {"id": "nh-st-359-c-19", "jurisdiction": "new-hampshire", "doc_type": "statute",
           "citation": "RSA 359-C:19", "title": "RSA 359-C:19 Definitions (Notice of Security Breach)", "format": "html"}


def test_the_state_is_found_by_name():
    assert "new-hampshire" in states.modules(refresh=True)


def test_a_chapter_page_becomes_title_and_chapter_lines_then_each_section_after_a_blank_line():
    lines = nh.statute_html_to_text(CH5D).splitlines()
    assert lines[:2] == ["TITLE I THE STATE AND ITS GOVERNMENT", "Chapter 5-D USE OF ARTIFICIAL INTELLIGENCE BY STATE AGENCIES"]
    assert "" in lines and lines[lines.index("") + 1] == "5-D:1 Definitions. –"
    assert "Source. 2024, 209:1, eff. July 1, 2024." in lines


def test_the_metadata_comment_and_redundant_section_banners_do_not_leak():
    text = nh.statute_html_to_text(CH5D)
    for leak in ("Hide metadata", "<", ">", "&nbsp;", "&#150;", "titlename", "Section 5-D:1\n", "\x96"):
        assert leak not in text
    assert text.count("5-D:1 Definitions.") == 1


def test_paragraph_breaks_become_one_line_each_and_numbering_is_kept():
    lines = nh.statute_html_to_text(CH5D).splitlines()
    assert 'I. "Artificial intelligence" or "AI" is the ability of a machine to display human-like capabilities for cognitive tasks such as reasoning, learning, planning, and creativity. AI systems may adapt their behavior to a certain degree by analyzing the effects of previous actions and operating under varying and unpredictable circumstances without significant human oversight.' in lines
    assert any(l.startswith("(a) Review the use of AI") for l in lines)


def test_a_repealed_section_keeps_its_heading_and_a_subdivision_heading_keeps_its_place():
    lines = nh.statute_html_to_text(CH21R).splitlines()
    assert "21-R:9 Repealed by 2022, 323:1, II, eff. Sept. 6, 2022. –" in lines
    assert lines.index("Open Standards") < lines.index("21-R:10 Definitions. –")
    assert lines.index("Cybersecurity Software") < lines.index("21-R:15 Use of Kaspersky Software Prohibited. –")


def test_a_section_page_keeps_its_subdivision_heading():
    lines = nh.statute_html_to_text(SEC).splitlines()
    assert lines[:3] == ["TITLE XXXI TRADE AND COMMERCE", "CHAPTER 359-C RIGHT TO PRIVACY", "Notice of Security Breach"]
    assert "359-C:19 Definitions. –" in lines


def test_text_with_no_section_is_refused():
    with pytest.raises(ValueError):
        nh.statute_html_to_text(b"<html><body><h1>Access Denied</h1></body></html>")


def test_to_text_hook_serves_html_statutes_only():
    assert nh.to_text(CH5D, "html", "statute", None, "gc.nh.gov").startswith("TITLE I")
    assert nh.to_text(CH5D, "html", "rule", None, "gc.nh.gov") is None


def test_chapter_identity_needs_the_chapter_heading_line():
    text = nh.statute_html_to_text(CH5D)
    assert nh.check_identity(CH_SRC, text, "page") is True
    with pytest.raises(ValueError):
        nh.check_identity({**CH_SRC, "citation": "RSA Chapter 5-C"}, text, "page")
    with pytest.raises(ValueError):    # 5-D must not match 5-DX or a mention
        nh.check_identity({**CH_SRC, "citation": "RSA Chapter 5"}, text, "page")


def test_section_identity_needs_the_section_heading_line():
    text = nh.statute_html_to_text(SEC)
    assert nh.check_identity(SEC_SRC, text, "page") is True
    with pytest.raises(ValueError):
        nh.check_identity({**SEC_SRC, "citation": "RSA 359-C:20"}, text, "page")


def test_other_states_are_not_claimed():
    assert nh.check_identity({**CH_SRC, "jurisdiction": "oregon"}, "x", "page") is False


def test_the_whole_flow_uses_the_hooks():
    text = states.to_text(CH5D, "html", "statute", "new-hampshire")
    states.check_identity(CH_SRC, text)
    assert states.effective_date(text, "statute", "new-hampshire") is None


# ---- section pages of a non-IT chapter (RSA 294-E:17 to :19, owner decision 2026-11-13) ----
SEC18 = (FX / "section-294-e-18.html").read_bytes()
SEC19 = (FX / "section-294-e-19.html").read_bytes()
S18_SRC = {"id": "nh-st-294-e-18", "jurisdiction": "new-hampshire", "doc_type": "statute", "citation": "RSA 294-E:18",
           "title": "RSA 294-E:18 Acceptance and Distribution of Electronic Records by Governmental Agencies",
           "format": "html"}


def test_a_section_page_of_a_non_it_chapter_is_that_section_only():
    lines = nh.statute_html_to_text(SEC18).splitlines()
    assert lines[:2] == ["TITLE XXVII CORPORATIONS, ASSOCIATIONS, AND PROPRIETORS OF COMMON LANDS",
                         "CHAPTER 294-E UNIFORM ELECTRONIC TRANSACTIONS ACT"]
    assert lines[3] == "294-E:18 Acceptance and Distribution of Electronic Records by Governmental Agencies. –"
    assert sum(1 for l in lines if l[:6] == "294-E:") == 1          # no other section rides along
    assert lines[-1].startswith("Source. 2001, 265:1.")
    for leak in ("Hide metadata", "<", "&#150;", "Section 294-E:18\n"):
        assert leak not in "\n".join(lines)


def test_the_identity_check_tells_one_section_page_from_the_next():
    text = nh.statute_html_to_text(SEC18)
    assert nh.check_identity(S18_SRC, text, "page") is True
    with pytest.raises(ValueError):
        nh.check_identity({**S18_SRC, "citation": "RSA 294-E:19"}, text, "page")
    assert nh.check_identity({**S18_SRC, "citation": "RSA 294-E:19"}, nh.statute_html_to_text(SEC19), "page") is True
