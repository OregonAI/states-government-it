"""Seam: src.authority_refs. extract(state, text) -> citations a state's documents make to that
state's own statutes, rules and executive orders; resolve/report -> what the corpus holds of them.

Every text below is a line copied verbatim from a committed document (the file is named beside it);
test_every_sample_is_in_its_document keeps that true when documents are regenerated.
"""
import json
import re
from pathlib import Path

import pytest

from src import authority_refs as ar

ROOT = Path(__file__).resolve().parent.parent

# (state, verbatim text, document it is copied from, expected [(kind, code, level, sec, end)])
FORMS = [
    ("oregon", "Statutes/Other Implemented: ORS 276A.340-276A.344 & Or Laws 2025, ch 396 (HB 3936)",
     "rules/oregon/or-oar-128-20.md", [("statute", "ORS", "section", "276A.340", "276A.344")]),
    ("oregon", "(2) Notwithstanding ORS chapters 279A, 279B and 279C, the State Chief Information Officer:",
     "statutes/oregon/or-ors-276a.md",
     [("statute", "ORS", "chapter", "279A", None), ("statute", "ORS", "chapter", "279B", None),
      ("statute", "ORS", "chapter", "279C", None)]),
    ("oregon", "Oregon Identity Theft Protection Act (ORS 646A.600-628)",
     "policies/oregon/or-eis-privacy-guidance.md", [("statute", "ORS", "section", "646A.600", "646A.628")]),
    ("oregon", "OAR 125-800-0005, 125-800-0020",
     "policies/oregon/or-das-107-004-050.md",
     [("rule", "OAR", "section", "125-800-0005", None), ("rule", "OAR", "section", "125-800-0020", None)]),
    ("washington", "       custody” requirements in WAC 434-615-020.",
     "policies/washington/wa-ea-01-01-g.md", [("rule", "WAC", "section", "434-615-020", None)]),
    ("washington", "      8. RCW 42.56.250 Employment and Licensing.",
     "standards/washington/wa-sec-08-01-s.md", [("statute", "RCW", "section", "42.56.250", None)]),
    ("california", "Pursuant to Government Code Sections 11545 and 11546, the California Department of Technology",
     "policies/california/ca-tl-17-07.md",
     [("statute", "Gov", "section", "11545", None), ("statute", "Gov", "section", "11546", None)]),
    ("colorado", "accordance with C.R.S. 24-37.5-105.4. For an information technology function to receive",
     "policies/colorado/co-oit-delegation-of-authority-policy.md", [("statute", "CRS", "section", "24-37.5-105.4", None)]),
    ("colorado", "annual cyber security plan for their agency, in accordance with Rule 8 CCR 1501-5 and this",
     "policies/colorado/co-oit-cisp-003.md", [("rule", "CCR", "section", "1501-5", None)]),
    ("kentucky", "title: Action for injunctive relief for injury due to violation of KRS 61.980 to 61.988",
     "statutes/kentucky/ky-krs-61-988.md", [("statute", "KRS", "section", "61.980", "61.988")]),
    ("louisiana",
     "(1) Contracts of this type shall be entered into using one of the methods of source selection provided in R.S. 39:199, 200, 1594, 1595, 1600(D), 1600.2, and 1702.",
     "statutes/louisiana/la-rs-39-198.md",
     [("statute", "RS", "section", "39:199", None), ("statute", "RS", "section", "39:200", None),
      ("statute", "RS", "section", "39:1594", None), ("statute", "RS", "section", "39:1595", None),
      ("statute", "RS", "section", "39:1600", None), ("statute", "RS", "section", "39:1600.2", None),
      ("statute", "RS", "section", "39:1702", None)]),
    ("idaho", "   Authority: Idaho Code § 67-831 through § 67-833",
     "policies/idaho/id-ita-p4590.md", [("statute", "IC", "section", "67-831", "67-833")]),
    ("idaho", "   Idaho Code §§ 28-51-104, 28-51-105, 28-51-106, and 28-51-107 applies to any city,",
     "standards/idaho/id-ita-s6010.md",
     [("statute", "IC", "section", s, None) for s in ("28-51-104", "28-51-105", "28-51-106", "28-51-107")]),
    ("iowa", "                       by Iowa Code section 8B.21(​k​)-(​l​).",
     "standards/iowa/ia-ocio-1054.md", [("statute", "IC", "section", "8B.21", None)]),
    ("minnesota", "assaultive or threatening conduct as defined in Minnesota Statutes, section 13.32, subdivision 8",
     "statutes/minnesota/mn-stat-13.md", [("statute", "MS", "section", "13.32", None)]),
    ("north-dakota", "Law Implemented: NDCC 23-12-19, 54-59-25, 54-59-26, 54-59-28, 54-59-29",
     "rules/north-dakota/nd-nac-113-02-01.md",
     [("statute", "NDCC", "section", s, None) for s in ("23-12-19", "54-59-25", "54-59-26", "54-59-28", "54-59-29")]),
    ("nebraska", "    (1) Purpose. Pursuant to Neb. Rev. Stat. §§ 81-1117, 81-1120.17, and 81-1120.20, certain",
     "policies/nebraska/ne-nitc-1-204.md",
     [("statute", "NRS", "section", s, None) for s in ("81-1117", "81-1120.17", "81-1120.20")]),
    ("new-hampshire",
     "I. Providing technical information technology consultation to all executive branch agencies and to any other agency that requests it, including technical advice consistent with the principles of open government data established in RSA 21-R:11 through RSA 21-R:",
     "statutes/new-hampshire/nh-st-21-r.md", [("statute", "RSA", "section", "21-R:11", None)]),
    ("virginia", "    In accordance with Code of Virginia, § 2.2-2009,",
     "policies/virginia/va-sec519-01.md", [("statute", "VA", "section", "2.2-2009", None)]),
    ("texas", "1 TAC § 202.25", "standards/texas/tx-dir-security-control-standards-catalog.md", [("rule", "TAC", "section", "1/202.25", None)]),
    ("wisconsin", "   Pursuant to the legal authority and mandates set forth in Wis. Stat. §§ 16.971-",
     "policies/wisconsin/wi-det-aup.md", [("statute", "WS", "section", "16.971", None)]),
    ("utah", "Authority: Utah Administrative Code, R895-7. Acceptable Use of Information Technology Resources; Utah Administrative Code, R477-11. Discipline. DTS Policy 5000-0002 Enterprise Security Policy",
     "policies/utah/ut-dts-1000-0003.md",
     [("rule", "UAC", "section", "R895-7", None), ("rule", "UAC", "section", "R477-11", None)]),
    ("oklahoma", "Chief Information Officer in accordance with Title 62 O.S. §§ 34.11.1 and 34.12 and Title 62 O.S.",
     "policies/oklahoma/ok-pol-information-security-ppg.md",
     [("statute", "OS", "section", "62/34.11.1", None), ("statute", "OS", "section", "62/34.12", None)]),
    ("north-carolina", "Pursuant to N.C.G.S. § 143B-1376 - Statewide Security and Privacy Standards, the State Chief",
     "policies/north-carolina/nc-fipp-memo.md", [("statute", "GS", "section", "143B-1376", None)]),
    ("massachusetts", "              M.G.L. c. 6, § 167. Pursuant to the definition contained within M.G.L. c. 66A, § 1, CORI is not",
     "rules/massachusetts/ma-940-cmr-11.md",
     [("statute", "MGL", "section", "6/167", None), ("statute", "MGL", "section", "66A/1", None)]),
    ("south-dakota", "Source: SDC 1939, § 55.2004; SL 1988, ch 11, § 11; SDCL §§ 1-14-13, 1-14-14.2; SL 1994, ch 412 (Ex. Ord. 94-4), § 21; SL 2026, ch 1 (Ex. Ord. 26-2), § 17, eff. Apr. 13, 2026.",
     "statutes/south-dakota/sd-sdcl-1-33-bit.md",
     [("statute", "SDCL", "section", "1-14-13", None), ("statute", "SDCL", "section", "1-14-14.2", None),
      ("eo", "EO", "section", "94-4", None), ("eo", "EO", "section", "26-2", None)]),
    ("delaware", "       will be posted on the DTI website. 29 Del. C. § 9004C(10).",
     "policies/delaware/de-oth-psp-001.md", [("statute", "DEL", "section", "29/9004C", None)]),
    ("maryland", "    Code, SF&P \u00a7 3A-302. Agency executives, managers and staff shall ensure compliance with this policy.",
     "policies/maryland/md-doit-policy-20-08-it-security-boundary-protection.md", [("statute", "SFP", "section", "3A-302", None)]),
    ("west-virginia", "        ​5.7.​   ​WV Code § 5A-6-4a​",
     "policies/west-virginia/wv-wvot-po2002.md", [("statute", "WV", "section", "5A-6-4a", None)]),
    ("kansas", "75-7201. Definitions. As used in K.S.A. 75-7201 through 75-7212, and amendments thereto:",
     "statutes/kansas/ks-ksa-75-7201.md", [("statute", "KSA", "section", "75-7201", "75-7212")]),
    ("new-jersey", "        N.J.S.A. 52:18A-224 through.52:18A-234",
     "policies/new-jersey/nj-njoit-13-09.md", [("statute", "NJSA", "section", "52:18A-224", "52:18A-234")]),
    ("ohio", "5. ORC Section 1347.15 requires each Agency to post on its’ website the policies adopted in accordance with that law.",
     "policies/ohio/oh-it-08.md", [("statute", "ORC", "section", "1347.15", None)]),
    ("hawaii", "    HRS § 94-1.1 https://www.capitol.hawaii.gov/hrscurrent/Vol02_Ch0046-0115/HRS0094/HRS_0094-0001_0001.htm.",
     "policies/hawaii/hi-pol-cdo-005.md", [("statute", "HRS", "section", "94-1.1", None)]),
    ("new-mexico", "[1.12.6.1 NMAC - N, 7-14-00]", "rules/new-mexico/nm-nmac-1-12-6.md",
     [("rule", "NMAC", "section", "1.12.6.1", None)]),
    ("washington", "     vulnerabilities. See Executive Order 24-01, Sections 8.d, 8.e and 8.f.",
     "policies/washington/wa-watech-ai-risk-assessments.md", [("eo", "EO", "section", "24-1", None)]),
]

# Lines that look like a citation and are not one to this state's own instruments.
LOOKALIKES = [
    ("oregon", "Statewide Policy 107-004-010 Information Technology Asset Inventory and Management"),
    ("oregon", "Effective date: 11/10/2026; policy 107-004-052; retrieved 2026-11-10"),
    ("oregon", "NIST SP 800-53 Rev. 5 controls and 44 U.S.C. 3554 apply"),
    ("washington", "45 C.F.R. 164.312 and 42 U.S.C. 1320d-6 are federal requirements"),
    ("virginia", "see 28 C.F.R. 1.2-3 and FIPS 199"),
    ("colorado", "the Office issued 24-37.5 notices, and 2026-11 was the revision"),
]


def seen(state, text):
    return [(c.kind, c.code, c.level, c.sec, c.end) for c in ar.extract(state, text)]


@pytest.mark.parametrize("state,text,source,expected", FORMS, ids=[f"{f[0]}-{i}" for i, f in enumerate(FORMS)])
def test_extracts_the_form(state, text, source, expected):
    assert seen(state, text) == expected


@pytest.mark.parametrize("state,text", LOOKALIKES)
def test_no_hit_on_lookalikes(state, text):
    assert seen(state, text) == []


def test_federal_citations_are_counted_not_extracted():
    text = "Comply with NIST SP 800-53, 44 U.S.C. 3554 and 45 C.F.R. 164.312 (FedRAMP)."
    assert ar.extract("oregon", text) == []
    assert ar.count_federal(text) == {"usc": 1, "cfr": 1, "nist": 1, "fedramp": 1}


def test_every_sample_is_in_its_document():
    for state, text, source, _ in FORMS:
        assert text.strip() in (ROOT / source).read_text(encoding="utf-8"), (source, text[:60])
        assert source.split("/")[1] == state


# ---- resolution against the real seed files ----------------------------------------------------------

def status(state, text):
    """[(cite code/sec, status, instrument label)] for the citations in `text`, resolved against the real seed."""
    return [(r.cite.sec, r.status, r.instrument) for r in ar.resolve_text(state, text)]


def test_section_inside_a_held_chapter_is_held():
    assert status("oregon", "ORS 276A.300") == [("276A.300", "HELD", "ORS chapter 276A")]
    assert status("texas", "Government Code Section 2054.510") == [("2054.510", "HELD", "Gov't Code chapter 2054")]


def test_range_form_is_held_when_inside_a_held_run():
    assert status("alaska", "see AS 44.21.160") == [("44.21.160", "HELD", "AS 44.21.160")]
    assert status("kentucky", "violation of KRS 42.720 to 42.724")[0][1] == "HELD"


def test_a_section_outside_every_held_run_is_not_held():
    assert status("alaska", "see AS 44.21.100") == [("44.21.100", "NOT_HELD", "AS 44.21.100")]
    assert status("oregon", "under ORS 279A.010") == [("279A.010", "NOT_HELD", "ORS chapter 279A")]
    assert status("oregon", "OAR 125-247-0110") == [("125-247-0110", "NOT_HELD", "OAR 125-247")]


def test_rule_division_and_executive_order_held():
    assert status("oregon", "OAR 128-030-0020")[0][1:] == ("HELD", "OAR 128-030")
    assert status("oregon", "Executive Order No. 23-26")[0][1] == "HELD"


def test_a_stub_is_a_stub_and_keeps_its_reason():
    [r] = ar.resolve_text("florida", "Rule 60GG-2.003, F.A.C.")
    assert (r.status, r.instrument, r.seed_ids) == ("STUB", "F.A.C. 60GG-2", ["fl-fac-60gg-2"])
    assert "Word 97-2003" in r.reason
    [e] = ar.resolve_text("oregon", "Executive Order 16-13")
    assert e.status == "STUB"


def test_a_left_out_item_keeps_the_recorded_reason():
    [r] = ar.resolve_text("alaska", "AS 40.21.010")
    assert r.status == "LEFT_OUT"
    assert "Left out as records management" in r.reason


def test_a_chapter_citation_with_only_a_section_held_is_not_held_and_says_so():
    [r] = ar.resolve_text("washington", "RCW 42.56")
    assert r.status == "NOT_HELD" and r.partial_ids


def test_every_held_statute_rule_and_order_in_every_seed_parses_to_a_holding():
    assert sorted(FORMS_STATES) == sorted(ar.FORMS)
    assert len(ar.FORMS) == 42
    bad = {s: ar.load_seed(s).unparsed for s in ar.FORMS if ar.load_seed(s).unparsed}
    assert bad == {}


FORMS_STATES = [p.stem for p in (ROOT / "_meta" / "sources").glob("*.yml")]


# ---- authority context, quotes, the report -----------------------------------------------------------

def ctx(text, needle):
    i = text.index(needle)
    return ar.in_authority_context(text, i)


def test_authority_lines_and_phrases_count_as_authority_context():
    assert ctx("Statutes/Other Implemented: ORS 276A.340-276A.344 & Or Laws 2025, ch 396 (HB 3936)", "ORS")
    assert ctx("Law Implemented: NDCC 23-12-19, 54-59-25", "NDCC")
    assert ctx("   Authority: Idaho Code § 67-831 through § 67-833", "Idaho")
    assert ctx("    In accordance with Code of Virginia, § 2.2-2009,", "Code")
    assert ctx("    (1) Purpose. Pursuant to Neb. Rev. Stat. §§ 81-1117, 81-1120.17, and 81-1120.20, certain", "Neb.")


def test_a_passing_mention_is_not_authority_context():
    assert not ctx("Oregon Identity Theft Protection Act (ORS 646A.600-628)", "ORS")
    assert not ctx("      8. RCW 42.56.250 Employment and Licensing.", "RCW")


def test_a_heading_makes_the_lines_below_it_authority_context():
    text = "Statutory Authority\n\n   ORS 276A.203\n   OAR 128-030-0020\n"
    assert ctx(text, "ORS 276A") and ctx(text, "OAR")


def test_a_very_short_line_takes_the_line_before_it_and_stays_verbatim():
    text = "pursuant to the authority in\nORS 276A.203\nnext"
    assert ar.quote(text, text.index("ORS")) == "pursuant to the authority in\nORS 276A.203"
    assert ar.quote(text, text.index("ORS")) in text


def test_quote_is_one_verbatim_line_of_at_most_forty_words():
    text = "first line\n   Authority: " + "word " * 60 + "ORS 276A.203 " + "tail " * 60 + "\nlast line\n"
    q = ar.quote(text, text.index("ORS 276A.203"))
    assert q in text and "ORS 276A.203" in q and len(q.split()) <= 40 and "\n" not in q


@pytest.fixture(scope="module")
def rep():
    return ar.build_report()


def test_federal_citations_never_reach_the_report(rep):
    for st in rep["states"].values():
        for bucket in ("not_held", "stub", "left_out"):
            for inst in st[bucket]:
                assert not re.search(r"U\.?S\.?C|C\.?F\.?R|NIST|FIPS", inst["instrument"])


def test_report_is_per_state_with_verbatim_quotes_and_real_citing_documents(rep):
    assert sorted(rep["states"]) == sorted(ar.FORMS)
    texts = ar.load_texts()
    checked = 0
    for state, st in rep["states"].items():
        for bucket in ("not_held", "stub", "left_out"):
            for inst in st[bucket]:
                assert inst["citing_documents"], inst
                assert inst["authority_context_citations"] <= inst["citations"]
                assert len(inst["quotes"]) <= 3
                for qt in inst["quotes"]:
                    assert len(qt["text"].split()) <= 40
                    assert qt["text"] in texts[qt["document"]], (state, qt)
                    assert qt["document"] in inst["citing_documents"]
                    checked += 1
    assert checked > 100


def test_report_finds_oregons_unheld_statute_chapters(rep):
    insts = {i["instrument"]: i for i in rep["states"]["oregon"]["not_held"]}
    assert "ORS chapter 279A" in insts
    assert insts["ORS chapter 279A"]["kind"] == "statute"


def test_check_fails_on_a_stale_file(tmp_path):
    stale = tmp_path / "authority-refs.json"
    stale.write_text(json.dumps({"states": {}}))
    assert ar.check(stale) is False


def test_labels_read_as_a_person_would_cite_them():
    assert status("massachusetts", "M.G.L. c. 66A, \u00a7 1")[0][1:] == ("HELD", "M.G.L. c. 66A")
    assert status("idaho", "Executive Order 2005-22")[0][2] == "Executive Order 2005-22"
    assert status("wyoming", "W.S. \u00a716-4-201 through 16-4-205")[0][2] == "W.S. 16-4-201 to 16-4-205"


def test_a_range_half_held_names_only_the_missing_end():
    assert status("kentucky", "violation of KRS 61.931 to 61.934") == [("61.931", "LEFT_OUT", "KRS 61.934")]   # 61.934 is recorded as left out


def test_a_title_is_not_read_as_the_chapter_after_it():
    assert seen("texas", "\u2022 Texas Administrative Code, Title 1, Chapter 206 (State Web Sites)") == \
        [("rule", "TAC", "chapter", "1/206", None)]


def history(doc_type, text, needle):
    return ar.is_history_reference(doc_type, text, text.index(needle))


def test_a_citation_inside_a_history_note_is_not_a_pointer_to_authority():
    wa = "[ 2020 c 65 s 1; 2019 c 241 s 5; 2015 c 64 s 3; 2007 c 197 s 9; 2005 c 368 s 1. Formerly RCW 42.17.31922.]"
    assert history("statute", wa, "RCW")
    va = "1976, c. 597, \u00a7\u00a7 2.1-377, 2.1-378; 1987, c. 506; 2001, c. 844; 2026, c. 748."
    assert history("statute", va, "\u00a7\u00a7")
    sd = "Source: SDC 1939, \u00a7 55.2004; SL 1988, ch 11, \u00a7 11; SDCL \u00a7\u00a7 1-14-13, 1-14-14.2; SL 1994, ch 412"
    assert history("statute", sd, "SDCL")
    assert not history("rule", sd, "SDCL")
    assert not history("policy", "Statutory Authority: ORS 276A.203", "ORS")


def test_an_old_number_the_corpus_itself_records_as_renumbered_resolves_to_the_held_text():
    # oregon.yml: "State Information Security ... renumbered from OAR 125-800 effective 2026-05-01"
    [r] = ar.resolve_text("oregon", "OAR 125-800-0020")
    assert (r.status, r.seed_ids) == ("HELD", ["or-oar-128-30"])
    assert "renumbered from OAR 125-800" in r.reason
    # maryland: "its older policies cite the same duties as 'SF&P 3A-301-309'"
    [m] = ar.resolve_text("maryland", "SF&P 3A-303")
    assert m.status == "HELD" and "3A-301-309" in m.reason
    assert ar.resolve_text("maryland", "SF&P 3A-311")[0].status == "HELD"    # the held bundle prints 3.5-311 too


def test_every_state_table_reads_something_from_that_states_documents(rep):
    assert [s for s, st in rep["states"].items() if st["documents_citing_state_instruments"] == 0] == []
    assert all(st["extraction"]["probable_citations"] >= 0 for st in rep["states"].values())


def test_an_unreliable_kind_is_kept_out_of_the_candidate_list(rep):
    ny = rep["states"]["new-york"]
    assert all(i["kind"] != "eo" for i in ny["not_held"])
    assert any(i["kind"] == "eo" for i in ny["not_held_unverified"])


def test_a_semicolon_ends_a_list_before_the_next_codes_name():
    text = "REFERENCES:\nIT PROJECT PROCUREMENT AUTHORITY    Government Code Sections \u00a7 11145, 11546;\n   Public Contract Code (PCC) Section 12100"
    assert [(c.code, c.sec) for c in ar.extract("california", text)] == [
        ("Gov", "11145"), ("Gov", "11546"), ("PCC", "12100")]


def test_a_thousands_separated_federal_order_number_is_not_a_state_order():
    text = "Whereas, The Trump Administration issued Executive Order No. 13,943 \u201cAddressing the Threat"
    assert ar.extract("south-dakota", text) == []


def test_stub_and_left_out_reasons_are_verbatim_from_the_seed_file(rep):
    import yaml
    checked = 0
    for state, st in rep["states"].items():
        seed = yaml.safe_load((ROOT / "_meta" / "sources" / f"{state}.yml").read_text(encoding="utf-8"))
        items = [str(i["text"]) for i in seed["left_out"]]
        reasons = {e["id"]: str(e.get("stub_reason") or "").strip() for e in seed["sources"] if e.get("stub")}
        for inst in st["left_out"]:
            assert any(inst["reason"] in t for t in items), (state, inst["instrument"])
            checked += 1
        for inst in st["stub"]:
            assert inst["reason"] in reasons.values(), (state, inst["instrument"])
            assert all(i in reasons for i in inst["seed_ids"])
            checked += 1
    assert checked > 50
