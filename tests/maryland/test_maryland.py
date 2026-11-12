"""Maryland: DoIT's SharePoint policy pages, the Division of State Documents' COMAR/executive-order pages, and the
General Assembly's statute section pages. Fixtures are real bytes with their page furniture (navigation, footers,
scripts): the AI policy, the MCP guidance card (tables, collapsible sections), the printer memo, EO 01.01.2019.07
and the whole of COMAR 14.33 (the full-subtitle file)."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states
from src.states import maryland

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "maryland"
AI_POLICY = (FIX / "doit-responsible-ai-policy.html").read_bytes()
MCP_CARD = (FIX / "doit-mcp-guidance-card.html").read_bytes()
PRINTER = (FIX / "doit-teleworking-printer-guidance.html").read_bytes()
EO_2019_07 = (FIX / "eo-01-01-2019-07.html").read_bytes()
COMAR_14_33 = (FIX / "comar-14-33-full.html").read_bytes()


def test_the_state_is_found_by_name():
    assert "maryland" in states.modules(refresh=True)


# ---- DoIT policy pages ---------------------------------------------------------------------

def test_a_doit_page_is_its_title_then_its_content_with_no_site_furniture():
    text = maryland.doit_page_to_text(AI_POLICY)
    lines = text.splitlines()
    assert lines[0] == "The State of Maryland’s Responsible AI Policy"
    assert "Revision History:" in lines
    assert "Date Issued: 05/23/25" in text
    for furniture in ("Skip to Content", "Accessibility Information", "Policies & Guidance",
                      "Find my Portfolio Officer", "100 Community Place", "Cybersecurity & Privacy Policy Suite",
                      "&#58;", "&nbsp;", "​", "\xa0", "<", "\t"):
        assert furniture not in text


def test_headings_stand_alone_and_lists_keep_their_markers_and_nesting():
    lines = maryland.doit_page_to_text(AI_POLICY).splitlines()
    assert "Purpose" in lines and "Scope" in lines
    assert "• Define roles and responsibilities related to the State’s usage of AI systems." in lines
    assert "1. All AI systems and use cases deployed (or under consideration) by State executive branch agencies; and" in lines
    # a list nested in a list is indented (the printer memo nests three deep, one <ul> directly in another)
    memo = maryland.doit_page_to_text(PRINTER).splitlines()
    assert "• The use of cloud printing services is prohibited, unless such use is covered under an existing "\
           "contractual relationship between the State of Maryland and the service provider." in memo
    assert "  • Personal Information/Personally Identifiable Information, as defined in MD State Gov’t Code §10-1301" in memo
    assert "    • Federal Tax Information;" in memo


def test_a_table_row_is_one_line_with_its_cells_joined_and_a_collapsible_section_is_kept():
    text = maryland.doit_page_to_text(MCP_CARD)
    assert "Risk | Description" in text.splitlines()
    assert any(l.startswith("Tool Poisoning | Attackers alter descriptions/behaviors of tools") for l in text.splitlines())
    assert "5.1 BYOD — Default Position: Prohibited" in text
    assert "Connecting any MCP server to State systems from a personal, unmanaged device is prohibited by default" in text


def test_a_page_with_no_main_content_is_refused_not_committed():
    with pytest.raises(ValueError, match="no policy text"):
        maryland.doit_page_to_text(b"<html><body><nav>menu</nav><h1>Not found</h1></body></html>")


# ---- COMAR and executive orders (Division of State Documents) -------------------------------

def test_an_executive_order_is_its_heading_then_one_line_per_paragraph_with_the_history():
    text = maryland.comar_to_text(EO_2019_07)
    lines = text.splitlines()
    assert lines[0] == "Executive Order 01.01.2019.07"
    assert lines[1] == "Maryland Cyber Defense Initiative"
    assert "A. There is a Maryland Cyber Defense Initiative to strengthen the State’s ability to manage the consequences of a cybersecurity incident." in lines
    assert "  1. There is a State Chief Information Security Officer (“SCISO”)." in lines
    assert "Administrative History" in lines and "Effective date: June 18, 2019" in lines
    for furniture in ("Previous", "Next", "Executive Orders 2019", "CC BY-NC-SA", "Please do not scrape", "Open Law Library"):
        assert furniture not in text


def test_a_regulation_subtitle_keeps_its_chapters_sections_and_annotations():
    text = maryland.comar_to_text(COMAR_14_33)
    lines = text.splitlines()
    assert lines[0] == "Subtitle 33 DEPARTMENT OF INFORMATION TECHNOLOGY"
    assert "Chapter 01 Definitions and General Provisions" in lines
    assert "Chapter 02 Information and Communication Technology Nonvisual Access Standards" in lines
    assert ".01 Scope." in lines and ".11 Information, Documentation, and Support." in lines
    assert "A. This subtitle does not apply to changes relating to or the purchase, lease, or rental of information technology by:" in lines
    assert "  (1) Public institutions of higher education solely for academic or research purposes;" in lines
    assert "Administrative History" in lines and "Authority" in lines and "Cross References" in lines
    assert "Please do not scrape" not in text


def test_a_page_with_no_article_is_refused():
    with pytest.raises(ValueError, match="no COMAR text"):
        maryland.comar_to_text(b"<html><body><main>404</main></body></html>")


# ---- the shared flow ------------------------------------------------------------------------

def test_the_shared_flow_reaches_the_readers_for_each_host_and_type():
    assert ing.to_text(AI_POLICY, "html", "policy", "maryland", None, "doit.maryland.gov").startswith(
        "The State of Maryland’s Responsible AI Policy\n")
    assert ing.to_text(EO_2019_07, "html", "executive_order", "maryland", None,
                       "raw.githubusercontent.com").startswith("Executive Order 01.01.2019.07\n")
    assert ing.to_text(COMAR_14_33, "html", "rule", "maryland", None,
                       "raw.githubusercontent.com").startswith("Subtitle 33 ")
    with pytest.raises(ValueError, match="no to_text"):
        ing.to_text(AI_POLICY, "html", "policy", "maryland", None, "example.com")


def test_an_executive_order_prints_its_effective_date_and_a_policy_prints_none():
    eo = maryland.comar_to_text(EO_2019_07)
    assert states.effective_date(eo, "executive_order", "maryland") == "2019-06-18"
    assert states.effective_date(maryland.doit_page_to_text(AI_POLICY), "policy", "maryland") is None


def test_a_regulation_subtitle_gets_no_effective_date_because_each_chapter_prints_its_own():
    text = maryland.comar_to_text(COMAR_14_33)
    assert text.count("Effective date:") == 2
    assert states.effective_date(text, "rule", "maryland") is None


def test_identity_refuses_bytes_that_are_not_the_cited_instrument():
    eo = {"id": "md-eo-2019-07", "jurisdiction": "maryland", "doc_type": "executive_order",
          "citation": "Executive Order 01.01.2019.07", "title": "Maryland Cyber Defense Initiative"}
    states.check_identity(eo, maryland.comar_to_text(EO_2019_07), "html")
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({**eo, "citation": "Executive Order 01.01.2021.09"},
                              maryland.comar_to_text(EO_2019_07), "html")
    rule = {"id": "md-comar-14-33", "jurisdiction": "maryland", "doc_type": "rule",
            "citation": "COMAR 14.33", "title": "Subtitle 33 DEPARTMENT OF INFORMATION TECHNOLOGY"}
    states.check_identity(rule, maryland.comar_to_text(COMAR_14_33), "html")
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({**rule, "title": "Subtitle 34 PUBLIC SCHOOL LABOR RELATIONS BOARD"},
                              maryland.comar_to_text(COMAR_14_33), "html")
    page = {"id": "md-ai-policy", "jurisdiction": "maryland", "doc_type": "policy", "citation": "Responsible AI Policy",
            "title": "The State of Maryland’s Responsible AI Policy"}
    states.check_identity(page, maryland.doit_page_to_text(AI_POLICY), "html")
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({**page, "title": "Maryland Open Source Policy"},
                              maryland.doit_page_to_text(AI_POLICY), "html")


# ---- statutes: one page per section, bundled -------------------------------------------------

from tests.seedutil import make_corpus, make_fetcher  # noqa: E402

SEC = {s: (FIX / f"mga-section-{s}.html").read_bytes() for s in ("3-5-101", "3-5-2A-02", "3-5-2A-03")}
NOT_FOUND = (FIX / "mga-section-not-found.html").read_bytes()
STATUTE = {"id": "md-sfp-test", "jurisdiction": "maryland", "doc_type": "statute", "format": "html",
           "article": "gsf", "sections": ["3.5-2A-02", "3.5-2A-03"], "citation": "Md. Code, State Fin. & Proc. tit. 3.5, subtit. 2A",
           "title": "Subtitle 2A. Office of Security Management", "url": maryland.statute_url("gsf", "3.5-2A-02")}


def _bundle(*pairs):
    return maryland.build_bundle([(maryland.statute_url("gsf", s.replace("_", ".")), maryland.section_fragment(SEC[k]))
                                  for k, s in pairs])


def test_a_section_page_gives_its_fragment_and_a_missing_section_gives_none():
    frag = maryland.section_fragment(SEC["3-5-101"]).decode()
    assert frag.startswith("<html>") and frag.endswith("</html>") and "In this title the following words" in frag
    assert "Skip to" not in frag and "Statutes Text" not in frag      # the page around the fragment is not kept
    assert maryland.section_fragment(NOT_FOUND) is None


def test_a_bundle_is_the_article_line_once_then_each_section_with_its_indentation():
    text = maryland.statute_to_text(_bundle(("3-5-101", "3.5-101"), ("3-5-2A-02", "3.5-2A-02"), ("3-5-2A-03", "3.5-2A-03")))
    lines = text.splitlines()
    assert lines[0] == "Article - State Finance and Procurement"
    assert lines.count("Article - State Finance and Procurement") == 1
    assert lines[1:3] == ["", "§3.5–101."]
    assert "(a) In this title the following words have the meanings indicated." in lines
    assert "(b) “Cloud computing” means a service that enables on–demand self–service network access to a shared pool of configurable computer resources, including data storage, analytics, commerce, streaming, e–mail, document sharing, and document editing." in lines
    assert "(d) (1) “Oversight of implementation” means management of the process to implement a new technology, system, or product into practice and use by a unit." in lines
    assert "  (2) “Oversight of implementation” includes:" in lines          # one level in: 8 &nbsp;
    assert "    (i) planning and preparation to implement the product or practice; and" in lines
    assert "\n\n§3.5–2A–02.\nThere is an Office of Security Management within the Department." in text
    assert "\n\n§3.5–2A–03.\n" in text
    for leak in ("Previous", "Next", "<", "&nbsp;", "\xa0", "Skip to"):
        assert leak not in text


def test_a_bundle_with_no_section_is_refused():
    with pytest.raises(ValueError, match="no statute text"):
        maryland.statute_to_text(b"")


def test_the_snapshot_fetches_each_listed_section_once_and_caches_the_bundle(tmp_path):
    cfg = make_corpus(tmp_path, [])
    calls = []
    routes = {maryland.statute_url("gsf", "3.5-2A-02"): (200, SEC["3-5-2A-02"]),
              maryland.statute_url("gsf", "3.5-2A-03"): (200, SEC["3-5-2A-03"])}
    dest = tmp_path / "snap.html"
    with make_fetcher(cfg, routes, calls) as f:
        raw, fresh = maryland.snapshot(STATUTE, f, dest, False)
        again, fresh2 = maryland.snapshot(STATUTE, f, dest, False)
    assert fresh and not fresh2 and again == raw == dest.read_bytes()
    assert calls == [maryland.statute_url("gsf", "3.5-2A-02"), maryland.statute_url("gsf", "3.5-2A-03")]
    assert raw.decode().count(maryland.SECTION_MARK) == 2
    assert maryland.snapshot({**STATUTE, "sections": None}, None, dest, False) is None     # not a statute bundle


def test_a_section_the_site_does_not_have_is_an_error_and_writes_nothing(tmp_path):
    cfg = make_corpus(tmp_path, [])
    routes = {maryland.statute_url("gsf", "3.5-2A-02"): (200, NOT_FOUND)}
    dest = tmp_path / "snap.html"
    with make_fetcher(cfg, routes) as f:
        with pytest.raises(ValueError, match="no section 3.5-2A-02"):
            maryland.snapshot(STATUTE, f, dest, False)
    assert not dest.exists()


def test_statute_identity_needs_every_listed_section_printed():
    text = maryland.statute_to_text(_bundle(("3-5-2A-02", "3.5-2A-02"), ("3-5-2A-03", "3.5-2A-03")))
    states.check_identity(STATUTE, text, "html")
    with pytest.raises(ValueError, match="section 3.5-2A-04 does not appear"):
        states.check_identity({**STATUTE, "sections": ["3.5-2A-02", "3.5-2A-04"]}, text, "html")


def test_the_shared_flow_reads_a_statute_bundle():
    bundle = _bundle(("3-5-2A-02", "3.5-2A-02"))
    assert ing.to_text(bundle, "html", "statute", "maryland", None, "mgaleg.maryland.gov").startswith("Article - State Finance")


# ---- review fixes ---------------------------------------------------------------------------

SEC_309 = (FIX / "mga-section-3-5-309.html").read_bytes()


def test_a_page_that_prints_two_versions_of_a_section_keeps_only_the_one_in_effect():
    # 3.5-309 prints '§3.5–309. IN EFFECT' and then '§3.5–309. // EFFECTIVE JUNE 30, 2031 PER CHAPTERS 436 AND 437 OF 2026 //'
    raw = maryland.build_bundle([(maryland.statute_url("gsf", "3.5-309"), maryland.section_fragment(SEC_309))])
    assert b"EFFECTIVE JUNE 30, 2031" in raw                  # the snapshot keeps the page as served
    text = maryland.statute_to_text(raw)
    assert "§3.5–309. IN EFFECT" in text
    assert "EFFECTIVE JUNE 30, 2031" not in text and "CHAPTERS 436 AND 437" not in text
    assert text.count("There is an Information Technology Investment Fund.") == 1
    assert text.count("§3.5–309.") == 1


def test_two_versions_with_none_in_effect_are_refused():
    frag = maryland.section_fragment(SEC_309).decode().replace("IN EFFECT", "NOT YET")
    raw = maryland.build_bundle([(maryland.statute_url("gsf", "3.5-309"), frag.encode())])
    with pytest.raises(ValueError, match="in effect"):
        maryland.statute_to_text(raw)


def test_a_void_img_or_input_tag_does_not_hide_the_text_after_it():
    fragment = ('<main id="mdgovMain"><h1>T</h1><p>before</p><img src=x><p>after the image</p>'
                '<input type=text name=q><p>after the input</p><br><hr><wbr><p>last</p></main>')
    assert maryland._blocks(fragment) == ["T", "before", "after the image", "after the input", "last"]
    # a real hidden element is still skipped
    assert maryland._blocks('<p>a</p><button>go</button><script>x</script><p>b</p>') == ["a", "b"]


def test_a_statute_bundle_must_hold_exactly_the_sections_the_seed_lists_in_order():
    text = maryland.statute_to_text(_bundle(("3-5-2A-02", "3.5-2A-02"), ("3-5-2A-03", "3.5-2A-03")))
    states.check_identity(STATUTE, text, "html")
    with pytest.raises(ValueError, match="not listed"):          # a section dropped from the seed list
        states.check_identity({**STATUTE, "sections": ["3.5-2A-02"]}, text, "html")
    with pytest.raises(ValueError, match="does not appear"):     # a section added to the seed list
        states.check_identity({**STATUTE, "sections": ["3.5-2A-02", "3.5-2A-03", "3.5-2A-04"]}, text, "html")
    with pytest.raises(ValueError, match="order"):               # the same sections in another order
        states.check_identity({**STATUTE, "sections": ["3.5-2A-03", "3.5-2A-02"]}, text, "html")
