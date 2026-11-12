"""North Dakota: identity checks for the chapter PDFs of the Legislative Council and the Governor's order. Fixtures are
real bytes served on 2026-11-12 (whole files, page footers included)."""
import subprocess
from pathlib import Path

import pytest

from src import states
from src.ingest_common import pdf_to_text

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "north-dakota"


def text(name):
    return pdf_to_text((FIX / name).read_bytes())


def statute(cite):
    return {"id": "x", "jurisdiction": "north-dakota", "doc_type": "statute", "format": "pdf", "citation": cite,
            "title": "t"}


def test_the_state_is_found_by_name():
    assert "north-dakota" in states.modules(refresh=True)


def test_a_chapter_pdf_is_accepted_for_its_own_chapter():
    states.check_identity(statute("N.D.C.C. chapter 54-59"), text("ndcc-54-59.pdf"))
    states.check_identity(statute("N.D.C.C. chapter 54-59.1"), text("ndcc-54-59-1.pdf"))


def test_chapter_54_59_is_not_taken_for_chapter_54_59_1_or_the_reverse():
    with pytest.raises(ValueError, match="not N.D.C.C. chapter 54-59.1"):
        states.check_identity(statute("N.D.C.C. chapter 54-59.1"), text("ndcc-54-59.pdf"))
    with pytest.raises(ValueError, match="not N.D.C.C. chapter 54-59 \\("):
        states.check_identity(statute("N.D.C.C. chapter 54-59"), text("ndcc-54-59-1.pdf"))


def test_the_footer_lines_stay_in_the_text():
    assert "Page No. 1" in text("ndcc-54-59-1.pdf")


def rule(cite):
    return {"id": "x", "jurisdiction": "north-dakota", "doc_type": "rule", "format": "pdf", "citation": cite,
            "title": "Chapter 113-02-01 - North Dakota Health Information Network"}


def test_a_rule_chapter_pdf_is_accepted_for_its_own_chapter_only():
    t = text("nac-113-02-01.pdf")
    states.check_identity(rule("N.D. Admin. Code ch. 113-02-01"), t)
    with pytest.raises(ValueError, match="not N.D. Admin. Code ch. 113-02-02"):
        states.check_identity(rule("N.D. Admin. Code ch. 113-02-02"), t)


def order(cite):
    return {"id": "x", "jurisdiction": "north-dakota", "doc_type": "executive_order", "format": "pdf",
            "citation": cite, "title": "t"}


def test_an_order_is_matched_on_its_own_heading_not_on_a_mention_of_its_number():
    # the real scan carries a garbled hidden text layer; the OCR reading prints the heading line
    ocr_like = "NORTH\nDakota | Office of the Governor\n\nEXECUTIVE ORDER 2026-06\n\nWHEREAS, Executive Order 2022-10 was issued"
    states.check_identity(order("Executive Order 2026-06"), ocr_like)
    with pytest.raises(ValueError, match="Executive Order 2022-10"):
        states.check_identity(order("Executive Order 2022-10"), ocr_like)


def test_the_garbled_text_layer_of_the_real_order_is_not_good_enough():
    # pdftotext reads "EXECUTTVE ORDER 2026-06" from the hidden layer: the entry must be read by OCR instead
    with pytest.raises(ValueError, match="Executive Order 2026-06"):
        states.check_identity(order("Executive Order 2026-06"), text("eo-2026-06.pdf"))


POLICIES = {
    "ndit-ai-policy.pdf": "Artificial Intelligence Policy",
    "ndit-data-classification-policy.pdf": "State of North Dakota Data Classification Policy",
    "ndit-prohibited-technologies-policy.pdf": "Prohibited Technologies Policy",
    "ndit-ai-guideline.pdf": "Artificial Intelligence Guideline",
    "ndit-international-traveler-guidelines.pdf": "International Traveler Guidelines",
}


def policy(title):
    return {"id": "x", "jurisdiction": "north-dakota", "doc_type": "policy", "format": "pdf",
            "citation": f"NDIT: {title}", "title": title}


def test_each_policy_pdf_is_accepted_for_its_own_title():
    for name, title in POLICIES.items():
        states.check_identity(policy(title), text(name))


def test_a_policy_is_not_taken_for_another_that_it_mentions():
    # the AI Policy text names the Data Classification Policy and the AI Guideline names the AI Policy: a
    # mention is not the heading line
    with pytest.raises(ValueError, match="Data Classification Policy"):
        states.check_identity(policy("Data Classification Policy"), text("ndit-ai-policy.pdf"))
    with pytest.raises(ValueError, match="Artificial Intelligence Policy"):
        states.check_identity(policy("Artificial Intelligence Policy"), text("ndit-ai-guideline.pdf"))
    with pytest.raises(ValueError, match="Artificial Intelligence Guideline"):
        states.check_identity(policy("Artificial Intelligence Guideline"), text("ndit-ai-policy.pdf"))


def notes_for(name):
    t = text(name)
    h = states.hook("north-dakota", "extra_notes")
    return h(policy(POLICIES[name]), "pdf", t, None, "")


def test_the_ai_guideline_says_its_risk_matrix_picture_is_not_mirrored():
    n = notes_for("ndit-ai-guideline.pdf")
    assert "Page 6" in n and "AI Risk Matrix" in n and "image" in n and "not mirrored" in n


def test_a_policy_without_the_figure_gets_no_such_note():
    assert notes_for("ndit-ai-policy.pdf") == ""
