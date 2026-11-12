"""Massachusetts: the Legislature's General Laws (section pages, bundled per chapter), mass.gov's executive order,
directive and policy pages, and what the state prints for identity and dates. Fixtures are real bytes, page furniture
included: chapter 66A's table of contents and its three section pages, and whole mass.gov pages."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states
from src.states import massachusetts as ma

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "massachusetts"
CH = "https://malegislature.gov/Laws/GeneralLaws/PartI/TitleX/Chapter66A"
PAGES = {CH: (FIX / "66a-chapter.html").read_bytes()}
for n in (1, 2, 3):
    PAGES[f"{CH}/Section{n}"] = (FIX / f"66a-section-{n}.html").read_bytes()
EO614 = (FIX / "eo-614.html").read_bytes()
EO504 = (FIX / "eo-504-rescinded.html").read_bytes()
AD = (FIX / "ad-2021-2.html").read_bytes()
DOMAIN = (FIX / "website-domain-policy.html").read_bytes()
AD2018 = (FIX / "ad-2018-1.html").read_bytes()
EO629 = (FIX / "eo-629.html").read_bytes()
SRC66A = {"id": "ma-gl-66a", "jurisdiction": "massachusetts", "doc_type": "statute", "url": CH,
          "citation": "G.L. c. 66A", "title": "General Laws, Chapter 66A. Fair Information Practices"}


class FakeFetcher:
    def __init__(self, pages):
        self.pages, self.asked = pages, []

    def get(self, url):
        self.asked.append(url)
        from types import SimpleNamespace
        return SimpleNamespace(body=self.pages[url], status=200)


def bundle(tmp_path):
    raw, fresh = ma.snapshot(SRC66A, FakeFetcher(PAGES), tmp_path / "ma-gl-66a.html", False)
    return raw, fresh


def test_the_state_is_found_by_name():
    assert "massachusetts" in states.modules(refresh=True)


def test_a_chapter_is_bundled_from_its_table_of_contents_and_every_section_page_in_order(tmp_path):
    f = FakeFetcher(PAGES)
    raw, fresh = ma.snapshot(SRC66A, f, tmp_path / "ma-gl-66a.html", False)
    assert fresh and (tmp_path / "ma-gl-66a.html").read_bytes() == raw
    assert f.asked == [CH, f"{CH}/Section1", f"{CH}/Section2", f"{CH}/Section3"]


def test_a_committed_bundle_is_reused_unless_refetch(tmp_path):
    raw, _ = bundle(tmp_path)
    f = FakeFetcher({})
    again, fresh = ma.snapshot(SRC66A, f, tmp_path / "ma-gl-66a.html", False)
    assert again == raw and not fresh and f.asked == []


def test_only_statutes_use_the_bundle(tmp_path):
    assert ma.snapshot({"doc_type": "policy"}, FakeFetcher({}), tmp_path / "x.html", False) is None


def test_a_bundle_becomes_the_chapter_heading_then_each_section_with_its_caption(tmp_path):
    raw, _ = bundle(tmp_path)
    text = ing.to_text(raw, "html", "statute", "massachusetts")
    lines = text.splitlines()
    assert lines[0].startswith("Chapter 66A ")
    assert "Section 2: Holders maintaining personal data system; duties" in lines
    assert "\n\nSection 2: Holders" in text
    assert "(a) identify one individual immediately responsible for the personal data system who shall insure that the requirements of this chapter for preventing access to or dissemination of personal data are followed;" in lines
    assert text.index("Section 1:") < text.index("Section 2:") < text.index("Section 3:")


def test_no_menu_form_script_or_footer_leaks_into_a_statute(tmp_path):
    raw, _ = bundle(tmp_path)
    text = ing.to_text(raw, "html", "statute", "massachusetts")
    for leak in ("<", "&mdash;", "Print Page", "Search the Legislature", "Register", "Copyright", "Helpful Massachusetts Links",
                 "RequestVerificationToken", "Skip to Content"):
        assert leak not in text
    assert "—" in text                                  # the dash the page printed as an entity


def test_a_bundle_whose_section_page_has_no_law_text_is_refused(tmp_path):
    raw, _ = bundle(tmp_path)
    broken = raw.replace(b"genLawHeading", b"nothing")
    with pytest.raises(ValueError, match="no section heading"):
        ing.to_text(broken, "html", "statute", "massachusetts")


def test_a_statute_must_be_the_chapter_cited(tmp_path):
    raw, _ = bundle(tmp_path)
    text = ing.to_text(raw, "html", "statute", "massachusetts")
    ing.check_identity(SRC66A, text, "html")
    with pytest.raises(ValueError, match="not G.L. c. 93H"):
        ing.check_identity({**SRC66A, "citation": "G.L. c. 93H"}, text, "html")


def test_an_executive_order_page_keeps_its_header_and_the_order_and_drops_the_chrome():
    text = ing.to_text(EO614, "html", "executive_order", "massachusetts")
    lines = text.splitlines()
    assert "No. 614: Establishing the Digital Accessibility and Equity Governance Board" in lines
    assert "07/26/2023" in lines and "Revoking and Superseding:" in lines
    assert any(l.startswith("NOW, THEREFORE, I, Maura T. Healey") for l in lines)
    for leak in ("Skip table of contents", "Help Us Improve", "Mass.gov®", "<", "Hide Table of contents"):
        assert not any(leak in l for l in lines)


def test_an_executive_order_must_print_the_number_cited():
    text = ing.to_text(EO614, "html", "executive_order", "massachusetts")
    src = {"id": "ma-eo-614", "jurisdiction": "massachusetts", "doc_type": "executive_order",
           "citation": "Executive Order No. 614", "title": "x"}
    ing.check_identity(src, text, "html")
    with pytest.raises(ValueError, match="Executive Order No. 615"):
        ing.check_identity({**src, "citation": "Executive Order No. 615"}, text, "html")


def test_the_pages_own_rescission_marker_is_in_the_text_so_a_rescinded_order_can_be_told():
    text = ing.to_text(EO504, "html", "executive_order", "massachusetts")
    assert "Rescinded by:\nExecutive Order No. 588" in text


def test_a_directive_page_is_read_like_the_order_page_and_keeps_its_version_table():
    text = ing.to_text(AD, "html", "policy", "massachusetts")
    assert text.splitlines()[1].startswith("Administrative Directive 2021-2")
    assert "Date:\n05/05/2021" in text
    assert "Windows 7" in text and "Help Us Improve" not in text


def test_a_policy_page_needs_its_identity_text():
    text = ing.to_text(DOMAIN, "html", "policy", "massachusetts")
    src = {"id": "ma-website-domain-policy", "jurisdiction": "massachusetts", "doc_type": "policy",
           "citation": "Website Domain Policy, Version 1.3.0", "title": "Website Domain Policy",
           "identity_text": "The Website Domain Policy explains"}
    ing.check_identity(src, text, "html")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity({**src, "identity_text": "Vulnerability Management"}, text, "html")


def test_a_page_with_no_content_region_is_refused():
    with pytest.raises(ValueError, match="layout changed"):
        ing.to_text(b"<html><body><h1>Not Found</h1></body></html>", "html", "executive_order", "massachusetts")


def test_a_rule_pdf_is_identified_by_its_printed_number_in_any_case_and_spacing():
    text = "801 CMR: EXECUTIVE OFFICE\n\n801 CMR 3.00:           PRIVACY AND CONFIDENTIALITY\n"
    src = {"id": "ma-801-cmr-3", "jurisdiction": "massachusetts", "doc_type": "rule",
           "citation": "801 CMR 3.00", "title": "Privacy and confidentiality"}
    ing.check_identity(src, text, "pdf")
    with pytest.raises(ValueError, match="801 CMR 4.00"):
        ing.check_identity({**src, "citation": "801 CMR 4.00"}, text, "pdf")


def test_an_effective_date_printed_with_an_ordinal_day_is_read_and_a_plain_one_is_left_to_the_shared_reader():
    head = "Document Name: X Standard    Effective Date: October 15th, 2018\nDocument ID: IS.011    Last Revised Date: March 4, 2025\n"
    assert ing.effective_date(head, "standard", "massachusetts") == "2018-10-15"
    plain = "Document Name: X    Effective Date: 1/1/2025\nDocument ID: ISP.001    Last Revised Date: 3/25/2025\n"
    assert ing.effective_date(plain, "policy", "massachusetts") == "2025-01-01"


def test_the_contact_column_after_an_order_is_not_part_of_it():
    text = ing.to_text(EO504, "html", "executive_order", "massachusetts")
    assert "Trial Court Law Libraries" not in text and "Chat with a law librarian" not in text
    assert text.rstrip().endswith("William Francis Galvin\nSecretary of the Commonwealth")


def test_a_date_the_layout_wrapped_so_the_year_starts_the_next_line_in_the_same_column_is_read():
    # IS.024's header, as pdftotext -layout printed it
    head = (" Document Name: Physical and Environmental                                  Effective Date:          October 15th,\n"
            " Security Standard                                                          2018\n"
            " Document ID: IS.024                                                        Last Revised Date: March 21, 2025\n")
    assert ing.effective_date(head, "standard", "massachusetts") == "2018-10-15"


def _eo(n):
    return {"id": f"ma-eo-{n}", "jurisdiction": "massachusetts", "doc_type": "executive_order",
            "citation": f"Executive Order No. {n}", "title": "x"}


def test_an_executive_order_is_identified_by_its_own_title_line_not_by_a_number_it_mentions():
    t614 = ing.to_text(EO614, "html", "executive_order", "massachusetts")
    t629 = ing.to_text(EO629, "html", "executive_order", "massachusetts")
    assert "Executive Order No. 348" in t614 and "Replacing:\nExecutive Order No. 628" in t629   # mentioned, not the order
    ing.check_identity(_eo(614), t614, "html")
    ing.check_identity(_eo(629), t629, "html")
    for n, text in ((348, t614), (61, t614), (6, t614), (628, t629)):
        with pytest.raises(ValueError, match="not the cited instrument"):
            ing.check_identity(_eo(n), text, "html")


def test_version_table_cells_are_separated_not_run_together():
    text = ing.to_text(AD, "html", "policy", "massachusetts")
    assert "Version Number | Revised by | Effective date | Description of changes" in text
    assert "1.0.0 | Curtis Wood | 5/5/21 | First version of" in text
    assert "Curtis Wood5/5/21" not in text and "1.0.0Curtis" not in text
    assert "Date:\n05/05/2021" in text                       # the header table keeps one cell per line


def test_the_download_widget_the_repeated_references_and_the_hidden_category_label_are_not_in_the_text():
    text = ing.to_text(AD2018, "html", "policy", "massachusetts")
    lines = text.splitlines()
    for leak in ("Downloads", "Open PDF file", "PDF 204.27 KB", "show more", "show less"):
        assert leak not in text
    assert lines[:3] == ["Directive", "Administrative Directive 2018-1 Enterprise Security Policies and Awareness Training", "Date:"]
    assert text.count("Referenced Sources:") == 1
    assert text.rstrip().splitlines()[-1].startswith("[1] If any provision")        # the footnote is the last of the directive
    for raw, kind in ((AD, "policy"), (DOMAIN, "policy"), (EO614, "executive_order")):
        t = ing.to_text(raw, "html", kind, "massachusetts").splitlines()
        assert t[0] != t[1]
        assert not any("Table of Contents" in l or "×" in l for l in t)
