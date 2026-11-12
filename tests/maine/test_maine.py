"""Seam: src.ingest / src.states for Maine: the maine.gov web pages that are themselves instruments (the Governor's
order page, MaineIT's Prohibited Technologies and Digital Signatures pages, the Bureau of Human Resources policy
page), the identity of statutes, rules and executive orders, and the dates the MaineIT PDFs print. Everything else
Maine holds is a Word file or a PDF, which the shared readers handle. Fixtures are the real bytes the sites served
on 2026-11-12, whole, with page furniture."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "maine"
EO_AI = (FIX / "eo-ai-task-force.html").read_bytes()
PROHIBITED = (FIX / "oit-prohibited-technologies.html").read_bytes()
SIGNATURES = (FIX / "oit-digital-signatures.html").read_bytes()
BHR = (FIX / "bhr-personal-use-of-social-media.html").read_bytes()
CH164 = (FIX / "title5-ch164.docx").read_bytes()
RULE = (FIX / "rule-29-250-ch950.docx").read_bytes()
EO25 = (FIX / "eo-25-fy-20-21.pdf").read_bytes()
ARCH = (FIX / "architecture-compliance-policy.pdf").read_bytes()
ACCESS = (FIX / "access-control-policy.pdf").read_bytes()


def html(raw, doc_type):
    return ing.to_text(raw, "html", doc_type, "maine")


# ---- web pages ------------------------------------------------------------------------

def test_order_page_text_is_title_then_recitals_then_numbered_sections_then_signature_block():
    lines = html(EO_AI, "executive_order").splitlines()
    assert lines[0] == "An Order Establishing the Maine Artificial Intelligence Task Force"
    assert lines[1] == "FY 24/25"
    assert lines[2].startswith("WHEREAS, the recent proliferation of technologies that rely on artificial intelligence")
    assert "1. Task Force Established; Purpose" in lines
    assert "  1. The Maine Artificial Intelligence Task Force (“Task Force”) is hereby established." in lines
    assert lines[-2:] == ["Janet T. Mills", "Governor"]


def test_order_page_drops_menus_images_social_links_and_footer():
    t = html(EO_AI, "executive_order")
    for furniture in ("Facebook", "Site Policies", "Document Viewers", "Credit", "Skip to", "Sitemap", "<", "&nbsp;", "\xa0"):
        assert furniture not in t
    assert "Copyright" not in t


def test_prohibited_technologies_page_keeps_the_notice_the_list_and_the_contact_line():
    t = html(PROHIBITED, "policy")
    lines = t.splitlines()
    assert lines[0] == "Prohibited Technologies"
    assert lines[1] == "Notice"
    assert "• DeepSeek" in lines
    assert "• TikTok, or any successor application or service developed or provided by ByteDance Limited, or an entity owned by ByteDance Limited" in lines
    assert lines[-1].startswith("Please direct any questions on these lists to Charles Rote")
    for furniture in ("Delivering reliable", "Mailing Address", "Sitemap", "Skip to"):
        assert furniture not in t


def test_digital_signatures_page_text():
    lines = html(SIGNATURES, "policy").splitlines()
    assert lines[0] == "Digital Signatures"
    assert any(l.startswith("For state agencies: All state agencies must consult with the Chief Information Officer") for l in lines)
    assert "1. It must be based upon the X.509 Public Key Infrastructure;" in lines
    assert "Delivering reliable, cost effective, and secure IT services to the State and for the citizens of Maine." not in lines


def test_bhr_policy_page_opens_with_its_number_and_ends_before_the_site_footer():
    lines = html(BHR, "policy").splitlines()
    assert lines[0] == "6.7 Personal Use of Social Media"
    assert lines[-1] == "051915 JTC"
    assert "Business Hours" not in "\n".join(lines) and "Credit" not in lines


def test_a_page_without_a_heading_is_refused():
    with pytest.raises(ValueError, match="layout changed"):
        html(b"<html><body><p>nothing</p></body></html>", "policy")


# ---- identity --------------------------------------------------------------------------

def src(**kw):
    base = {"id": "x", "jurisdiction": "maine", "tags": ["governance"]}
    base.update(kw)
    return base


def test_statute_identity_is_the_chapter_number_and_title_on_the_first_lines():
    ok = src(doc_type="statute", format="docx", citation="5 M.R.S. ch. 164", title="Cybersecurity and Protection of Critical Infrastructure")
    fmt, text = ing.derive(ok, CH164)
    assert fmt == "docx" and text.startswith("CHAPTER 164")
    wrong = dict(ok, citation="5 M.R.S. ch. 163")
    with pytest.raises(ValueError, match="not 5 M.R.S. ch. 163"):
        ing.derive(wrong, CH164)


def test_rule_identity_is_the_umbrella_chapter_and_title_line():
    ok = src(doc_type="rule", format="docx", citation="29-250 C.M.R. ch. 950", title="Rules Governing the Use of Digital Signatures")
    fmt, text = ing.derive(ok, RULE)
    assert text.splitlines()[0].startswith("29-250 DEPARTMENT OF THE SECRETARY OF STATE")
    with pytest.raises(ValueError, match="not the cited"):
        ing.derive(dict(ok, citation="29-250 C.M.R. ch. 951"), RULE)


def test_executive_order_identity_must_match_the_heading_not_a_mention():
    ok = src(doc_type="executive_order", format="pdf", citation="Executive Order 25 FY 20/21",
             title="An Order Establishing the State of Maine Cybersecurity Advisory Council",
             identity_text="AN ORDER ESTABLISHING THE STATE OF MAINE CYBERSECURITY ADVISORY COUNCIL")
    fmt, text = ing.derive(ok, EO25)
    assert "25 FY 20/21" in text
    with pytest.raises(ValueError, match="not the cited"):
        ing.derive(dict(ok, identity_text="AN ORDER ESTABLISHING THE MAINE ARTIFICIAL INTELLIGENCE TASK FORCE"), EO25)
    ai = src(doc_type="executive_order", format="html", citation="Order of December 2024 (FY 24/25)",
             title="An Order Establishing the Maine Artificial Intelligence Task Force",
             identity_text="An Order Establishing the Maine Artificial Intelligence Task Force")
    assert ing.derive(ai, EO_AI)[0] == "html"
    with pytest.raises(ValueError, match="not the cited"):
        ing.derive(dict(ai, identity_text="An Order Establishing the Maine Data Center Advisory Council"), EO_AI)


def test_executive_order_phrase_quoted_only_in_body_text_is_refused():
    title = "AN ORDER ESTABLISHING THE STATE OF MAINE CYBERSECURITY ADVISORY COUNCIL"
    later_pdf = ("Office of\n The Governor     DATE   March 1, 2027\n\n   AN ORDER CONCERNING SOMETHING ELSE\n\n"
                 "WHEREAS, the State depends on its networks;\n\nWHEREAS, the Governor has acted before;\n\n"
                 "WHEREAS, Executive Order 25 FY 20/21, An Order Establishing the State of Maine\n"
                 "Cybersecurity Advisory Council, provided for a council;\n")
    pdf = src(id="x", doc_type="executive_order", format="pdf", identity_text=title)
    with pytest.raises(ValueError, match="not the cited"):
        states.check_identity(pdf, later_pdf)
    later_html = "An Order Concerning Something Else\nFY 26/27\nWHEREAS, " + title.title() + " was established;\n"
    page = src(id="x", doc_type="executive_order", format="html", identity_text=title.title())
    with pytest.raises(ValueError, match="not the cited"):
        states.check_identity(page, later_html)
    states.check_identity(page, title.title() + "\nFY 20/21\nWHEREAS, ...\n")


def test_web_page_policy_identity_is_the_first_line():
    ok = src(doc_type="policy", format="html", citation="MaineIT Prohibited Technologies", title="Prohibited Technologies")
    assert ing.derive(ok, PROHIBITED)[0] == "html"
    with pytest.raises(ValueError, match="not 'Digital Signatures'"):
        ing.derive(dict(ok, title="Digital Signatures"), PROHIBITED)


def test_web_page_policy_whose_printed_heading_differs_from_the_index_title_uses_identity_text():
    e = src(doc_type="policy", format="html", citation="c", title="Social Media for Personal Use Policy",
            identity_text="6.7 Personal Use of Social Media")
    assert ing.derive(e, BHR)[0] == "html"
    with pytest.raises(ValueError, match="not 'Prohibited Technologies'"):
        ing.derive(dict(e, identity_text="Prohibited Technologies"), BHR)


# ---- dates -----------------------------------------------------------------------------

def test_policy_pdf_version_is_the_latest_revision_date_as_printed():
    t = ing.to_text(ARCH, "pdf", "policy", "maine")
    assert states.source_version(t, "policy", "maine", "pdf") == "Latest Revision Date: April 6, 2023"
    t2 = ing.to_text(ACCESS, "pdf", "policy", "maine")
    assert states.source_version(t2, "policy", "maine", "pdf") == "Latest Revision Date: January 16, 2026"


def version_of(name):
    t = ing.to_text((FIX / f"oit-{name}.pdf").read_bytes(), "pdf", "policy", "maine",
                    no_text_pages=(45,) if name == "telecom-wiring" else ())      # a drawing page, listed in the seed entry
    return states.source_version(t, "policy", "maine", "pdf")


@pytest.mark.parametrize("name, want", [
    ("domain-name", "Latest Revision: 21 August 2026"),
    ("salesforce-background", "Latest Revision: 22 September 2021"),
    ("power-platform-quick-start", "Latest Revision: 21 October 2021"),
    ("general-architecture-principles", "Latest Revision: 15, July 2025"),
    ("user-device-commodity-app", "Latest Revision: May 29, 2026"),
    ("digital-accessibility", "Current Revision Date (Version 3.1): May 29, 2026"),
    ("telecom-wiring", "REVISED JANUARY 2024"),
    ("app-deployment-certification", "Last Revision Date: July 10, 2026"),
    ("sdlc", "Last Revision Date: October 16, 2026"),
    ("bcdr", "Latest Revision Date: October 2, 2017"),
    ("policy-creation-process", "Latest Revision Date: September 18, 2019"),
])
def test_policy_pdf_version_keeps_the_label_as_printed_and_stops_at_the_date(name, want):
    assert version_of(name) == want


def test_statute_version_is_the_currency_line_the_revisor_prints():
    t = ing.to_text(CH164, "docx", "statute", "maine")
    assert states.source_version(t, "statute", "maine", "docx") == "Current through October 1, 2026 (Second Regular Session of the 132nd Maine Legislature)"
    assert states.effective_date(t, "statute", "maine") is None


def test_order_and_rule_effective_dates_are_the_ones_printed():
    assert states.effective_date(ing.to_text(EO25, "pdf", "executive_order", "maine"), "executive_order", "maine") == "2021-01-13"
    assert states.effective_date(ing.to_text(RULE, "docx", "rule", "maine"), "rule", "maine") == "2014-07-31"
    assert states.effective_date(html(EO_AI, "executive_order"), "executive_order", "maine") is None


def test_conversion_notes_describe_the_web_page_reading():
    e = src(doc_type="policy", format="html", citation="c", title="Prohibited Technologies")
    n = ing.conversion_notes(e, "html", html(PROHIBITED, "policy"))
    assert "maine.gov" in n and "numbered" in n and "menus" in n
