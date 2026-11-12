"""Seam: src.ingest / src.states for Virginia: the Code of Virginia pages (law.lis.virginia.gov), VITA's
own web-page policies (vita.virginia.gov), and the identity checks of statutes and executive orders.
Fixtures are the real pages the sites served on 2026-11-11, whole, with page furniture."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "virginia"
CH_55_3 = (FIX / "vacode-chapter-55.3.html").read_bytes()
CH_38 = (FIX / "vacode-chapter-38.html").read_bytes()
SEC = (FIX / "vacode-section-2.2-2699.5.html").read_bytes()
CLOUD = (FIX / "vita-cloud-third-party-use-policy.html").read_bytes()
RULES = (FIX / "vita-rules.html").read_bytes()


def text(raw, doc_type="statute"):
    return ing.to_text(raw, "html", doc_type, "virginia")


def test_chapter_text_opens_with_chapter_then_each_section_heading_and_paragraphs():
    lines = text(CH_55_3).splitlines()
    assert lines[0] == "Chapter 55.3. Prohibition on the Use of Certain Products and Services."
    assert lines[1] == ""
    assert lines[2] == "§ 2.2-5514. Prohibited products and services and required incident reporting."
    assert lines[3] == "A. As used in this chapter, unless the context requires a different meaning:"
    assert "§ 2.2-5514.1. Prohibited applications and websites." in lines
    assert lines[lines.index("§ 2.2-5514.1. Prohibited applications and websites.") - 1] == ""


def test_chapter_text_keeps_the_history_line_and_drops_links_menus_and_the_print_date():
    t = text(CH_55_3)
    assert "2019, c. 302; 2022, cc. 626, 627; 2024, c. 503." in t
    assert t.rstrip().endswith("2023, c. 768.")
    assert "<" not in t and "&amp;" not in t and "\xa0" not in t
    for furniture in ("Creating a Report", "Table of Contents", "Popular Names", "11/11/2026", "Sign In"):
        assert furniture not in t


def test_chapter_with_two_versions_of_a_section_keeps_both_in_source_order():
    t = text(CH_38)
    a = t.index("§ 2.2-3803. (Effective until July 1, 2027)")
    b = t.index("§ 2.2-3803. (Effective July 1, 2027)")
    assert a < b


def test_section_page_text_is_the_section_heading_then_its_paragraphs_and_history():
    lines = text(SEC).splitlines()
    assert lines[0].startswith("§ 2.2-2699.5. Information Technology Advisory Council; membership")
    assert lines[1].startswith("A. The Information Technology Advisory Council (ITAC) is established")
    assert lines[-1].endswith("2022, cc. 260, 261.")
    assert "may not constitute a comprehensive list" not in text(SEC)   # the site's note under the section


def test_statute_identity_chapter_and_section():
    chap = {"id": "x", "doc_type": "statute", "jurisdiction": "virginia", "citation": "Va. Code tit. 2.2, ch. 55.3"}
    sec = {"id": "y", "doc_type": "statute", "jurisdiction": "virginia", "citation": "Va. Code § 2.2-2699.5"}
    states.check_identity(chap, text(CH_55_3), "html")
    states.check_identity(sec, text(SEC), "html")
    with pytest.raises(ValueError):
        states.check_identity(chap, text(SEC), "html")
    with pytest.raises(ValueError):
        states.check_identity(sec, text(CH_55_3), "html")


def test_executive_order_identity_uses_the_printed_heading():
    eo = {"id": "e", "doc_type": "executive_order", "jurisdiction": "virginia",
          "citation": "Executive Order 22 (2026)", "identity_text": "EXECUTIVE ORDER 22 (2026)"}
    states.check_identity(eo, "  EXECUTIVE ORDER 22 (2026)\n\n ESTABLISHING", "pdf")
    with pytest.raises(ValueError):
        states.check_identity(eo, "EXECUTIVE ORDER 21 (2026)", "pdf")


def test_vita_page_text_is_the_title_then_the_main_content_without_site_furniture():
    lines = text(CLOUD, "policy").splitlines()
    assert lines[0] == "Cloud Third Party Use Policy"
    assert "The Adoption of Cloud-Based Services" in lines
    assert any(l.startswith("Prior written approval") for l in lines)
    t = "\n".join(lines)
    for furniture in ("Change COV Password", "Return to top", "All Rights Reserved", "Translation Disclaimer"):
        assert furniture not in t
    assert "<" not in t and "&amp;" not in t and "\xa0" not in t


def test_vita_rules_page_keeps_hidden_accordion_text():
    t = text(RULES, "policy")
    assert t.splitlines()[0] == "VITA Rules"
    assert "Suppliers must deliver their goods and perform their services" in t
    assert "Payment Card Industry" in t


def test_vita_page_identity_is_its_title():
    src = {"id": "c", "doc_type": "policy", "jurisdiction": "virginia", "title": "Cloud Third Party Use Policy",
           "citation": "VITA Cloud Third Party Use Policy"}
    states.check_identity(src, text(CLOUD, "policy"), "html")


# ---- effective dates: the shared reader takes the first date after an `Effective Date` label. Two Virginia
# documents print something that is not one date, and the label reader must not invent one. Fixtures are
# the real pdftotext lines of the documents' publication-designation tables.
def _eff(name):
    return states.effective_date((FIX / name).read_text(), "standard", "virginia")


def test_effective_date_is_read_from_the_publication_designation_table():
    assert _eff("sec519-publication-designation.txt") == "2021-09-15"


def test_effective_date_left_empty_when_the_table_prints_a_placeholder_date():
    assert _eff("gov101-publication-designation.txt") is None      # 'January x, 2023 June 23, 2020'


def test_effective_date_left_empty_when_the_document_prints_a_list_of_effective_dates():
    assert _eff("legacy-it-effective-dates.txt") is None           # 'Effective Dates:' then four milestones


def test_effective_date_is_the_left_column_date_when_the_right_column_text_comes_between_label_and_date():
    # The two-column table puts the right-hand column's text between the label and the date: the shared
    # 200-character window cut these two (191 and 260 characters after the label).
    assert _eff("cpm110-05-publication-designation.txt") == "2021-09-01"
    assert _eff("sec527-publication-designation.txt") == "2021-01-01"


CH_38_1 = "Chapter 38.1. Protection of Social Security Numbers Act.\n\n§ 2.2-3815. Access to Social Security numbers.\n"


def test_statute_identity_chapter_designator_must_match_whole_not_as_a_prefix():
    ch38 = {"id": "x", "doc_type": "statute", "jurisdiction": "virginia", "citation": "Va. Code tit. 2.2, ch. 38"}
    ch20 = {"id": "z", "doc_type": "statute", "jurisdiction": "virginia", "citation": "Va. Code tit. 2.2, ch. 20"}
    with pytest.raises(ValueError):
        states.check_identity(ch38, CH_38_1, "html")           # ch. 38.1 is not ch. 38
    with pytest.raises(ValueError):
        states.check_identity(ch20, "Chapter 20.1. Virginia Information Technologies Agency.\n", "html")
    states.check_identity(ch38, text(CH_38), "html")           # the real ch. 38 still passes


def test_vita_page_identity_refuses_a_page_with_another_title():
    cloud = {"id": "c", "doc_type": "policy", "jurisdiction": "virginia", "title": "Cloud Third Party Use Policy",
             "citation": "VITA Cloud Third Party Use Policy"}
    rules = {"id": "r", "doc_type": "policy", "jurisdiction": "virginia", "title": "VITA Rules", "citation": "VITA Rules"}
    with pytest.raises(ValueError):
        states.check_identity(rules, text(CLOUD, "policy"), "html")
    with pytest.raises(ValueError):
        states.check_identity(cloud, text(RULES, "policy"), "html")


def test_effective_date_header_date_is_kept_when_the_table_row_prints_two_dates():
    # GOV 102-02 prints 'Effective Date: June 01, 2016' in its running header and 'July 24, 2009 June 01, 2016' in the table
    assert _eff("gov102-publication-designation.txt") == "2016-06-01"
