"""Seam: src.ingest for Idaho: Idaho Code section pages (legislature.idaho.gov) and their identity.
Fixtures are the real pages the Legislature served on 2026-11-11, whole, page furniture included."""
from pathlib import Path

import pytest

from src import ingest as ing

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "idaho"
SEC_67_830 = (FIX / "id-code-67-830-section.html").read_bytes()
SEC_28_51_105 = (FIX / "id-code-28-51-105-section.html").read_bytes()

SRC = {"id": "id-code-67-830", "doc_type": "statute", "jurisdiction": "idaho",
       "citation": "Idaho Code § 67-830", "title": "Idaho Code § 67-830 - Declaration of purpose"}


def test_section_text_is_title_chapter_section_then_history():
    t = ing.to_text(SEC_67_830, "html", "statute", "idaho")
    lines = t.splitlines()
    assert lines[0] == "TITLE 67"
    assert lines[1] == "STATE GOVERNMENT AND STATE AFFAIRS"
    assert lines[2] == "CHAPTER 8"
    assert lines[4].startswith("67-830. DECLARATION OF PURPOSE. The legislature finds that advances in information technology")
    assert lines[-2] == "History:"
    assert lines[-1].startswith("[67-830, added 2018, ch. 258, sec. 5, p. 612")


def test_section_text_drops_site_furniture_markup_and_the_generator_stub():
    t = ing.to_text(SEC_28_51_105, "html", "statute", "idaho")
    for furniture in ("Search Idaho Statutes", "Who", "pecnv.out", "How current is this law?",
                      "Download Entire Chapter", "Print Friendly", "Maintained By"):
        assert furniture not in t
    assert "<" not in t and "&nbsp;" not in t and "\xa0" not in t
    assert "within twenty-four (24) hours of such discovery, notify the office of the Idaho attorney general" in t


def test_page_without_a_code_region_is_refused():
    with pytest.raises(ValueError, match="code region"):
        ing.to_text(b"<html><body><p>Not found</p></body></html>", "html", "statute", "idaho")


def test_identity_accepts_the_cited_section_and_refuses_another():
    t = ing.to_text(SEC_67_830, "html", "statute", "idaho")
    ing.check_identity(SRC, t)
    with pytest.raises(ValueError, match="not Idaho Code § 67-831"):
        ing.check_identity(dict(SRC, citation="Idaho Code § 67-831"), t)


def test_a_statute_gets_no_effective_date():
    t = ing.to_text(SEC_67_830, "html", "statute", "idaho")
    assert ing.effective_date(t, "statute", "idaho") is None


# ---- identity of Idaho executive orders: the order's own heading line, "EXECUTIVE ORDER NO. 2022-06" ----

EO = {"id": "id-eo-2022-06", "doc_type": "executive_order", "jurisdiction": "idaho",
      "citation": "Executive Order No. 2022-06", "title": "Banning TikTok on State Devices"}
# tesseract's reading of the first lines of the scan the Governor's office serves (2026-11-11)
EO_HEAD = ("Executive Department State Capitol\n\nState of Idaho Boise\nEXECUTIVE DEPARTMENT\nSTATE OF IDAHO\n\n"
           "BOISE\nEXECUTIVE ORDER NO. 2022-06\n\nBANNING TIKTOK ON STATE DEVICES\n\nWHEREAS, maintaining the safety\n")


def test_identity_accepts_the_orders_own_heading_line():
    ing.check_identity(EO, EO_HEAD)


def test_identity_refuses_another_order_and_a_mere_mention_of_the_number():
    with pytest.raises(ValueError, match="not the order's heading line"):
        ing.check_identity(dict(EO, citation="Executive Order No. 2022-05"), EO_HEAD)
    mention = EO_HEAD.replace("EXECUTIVE ORDER NO. 2022-06", "EXECUTIVE ORDER NO. 2022-04") + "\nrepealing Executive Order No. 2022-06\n"
    with pytest.raises(ValueError, match="not the order's heading line"):
        ing.check_identity(EO, mention)


# ---- effective date of a PDF standard ----------------------------------------------------------
from src.states import effective_date  # noqa: E402


def test_standard_date_is_the_title_block_line_not_a_data_dictionary_label():
    # real S4266 text: the title block prints "Effective July 20, 2023"; further down a FEMA
    # data-dictionary table has "Effective date of current map revision ... 7/7/2009"
    text = (FIX / "id-ita-s4266-title-block.txt").read_text() + (FIX / "id-ita-s4266-data-dictionary.txt").read_text()
    assert "7/7/2009" in text
    assert effective_date(text, "standard", "idaho") == "2023-07-20"


def test_standard_with_only_table_labels_has_no_date():
    text = (FIX / "id-ita-s4266-data-dictionary.txt").read_text()
    assert effective_date(text, "standard", "idaho") is None


def test_standard_reads_the_printed_line_after_an_unparsable_label():
    # real S4232 text: "Effective Date: May 1,2011" (no space) ends the revision history, then the title block
    text = (FIX / "id-ita-s4232-titleblock-after-history.txt").read_text()
    assert effective_date(text, "standard", "idaho") == "2024-11-20"


def test_labelled_policy_date_still_reads():
    assert effective_date("Policy\n   Effective Date: 12/6/2016\n", "policy", "idaho") == "2016-12-06"
    assert effective_date("Effective date is August 25, 2011.\n", "standard", "idaho") == "2011-08-25"
