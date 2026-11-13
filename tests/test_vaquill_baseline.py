"""Seam: src.vaquill_baseline -- match(state, result), score(...), build(raw_dir, root). Each test states
one thing the outside-baseline scorer owes the reviewer. The raw responses are never committed, so these
tests build tiny fake ones in a temp directory."""
import json
from pathlib import Path

import pytest

from src import vaquill_baseline as vb


def res(state, citation, section, corpus="STATE", code=None, chapter=None, act="X"):
    return {"citation": citation, "sectionNumber": section, "corpusType": corpus, "chapter": chapter,
            "parent": {"code": code} if code else None, "actId": act, "sourceUrl": "https://example.gov/x"}


def test_ors_chapter_matches_any_section_of_276a_and_no_other_chapter():
    assert vb.match("oregon", res("or", "ORS 276A.300", "276A.300", chapter="276A")) == "or-ors-276a"
    assert vb.match("oregon", res("or", "ORS 276.300", "276.300", chapter="276")) is None


def test_oar_division_is_matched_by_section_prefix():
    r = res("or", "OAR 128-030-0020", "128-030-0020", corpus="REGULATION")
    assert vb.match("oregon", r) == "or-oar-128-30"
    assert vb.match("oregon", res("or", "OAR 128-020-0010", "128-020-0010", corpus="REGULATION")) == "or-oar-128-20"
    assert vb.match("oregon", res("or", "OAR 128-300-0010", "128-300-0010", corpus="REGULATION")) is None


def test_a_regulation_never_matches_a_statute_rule_and_vice_versa():
    assert vb.match("oregon", res("or", "x", "276A.203", corpus="REGULATION")) is None


def test_california_range_includes_decimal_sections_and_stops_at_the_end():
    g = lambda n: res("ca", f"Cal. Gov't Code § {n}", n, code="ca_gov")
    assert vb.match("california", g("11546.1")) == "ca-gov-11545-11548"
    assert vb.match("california", g("11544")) == "ca-gov-11531-11544"
    assert vb.match("california", g("11549.5")) == "ca-gov-11549-11549-10"
    assert vb.match("california", g("11549.11")) is None
    assert vb.match("california", g("11549.2")) == "ca-gov-11549-11549-10"
    assert vb.match("california", g("11549.60")) is None
    assert vb.match("california", g("11549.64")) == "ca-gov-11549-63-11549-66"
    assert vb.match("california", g("7405")) == "ca-gov-7405"


def test_california_civil_code_1798_100_is_not_in_the_1798_to_1798_78_instrument():
    c = lambda n: res("ca", n, n, code="ca_civ")
    assert vb.match("california", c("1798.29")) == "ca-civ-1798-1798-78"
    assert vb.match("california", c("1798.100")) is None
    assert vb.match("california", c("1798.8")) == "ca-civ-1798-1798-78"


def test_california_code_must_agree_with_the_instrument():
    assert vb.match("california", res("ca", "x", "11545", code="ca_civ")) is None


def test_colorado_articles_and_parts_and_the_ccr_rules():
    s = lambda n: res("co", n, n)
    assert vb.match("colorado", s("24-37.5-106")) == "co-crs-24-37-5"
    assert vb.match("colorado", s("24-37-106")) is None
    assert vb.match("colorado", s("24-37.7-102")) == "co-crs-24-37-7"
    assert vb.match("colorado", s("2-3-1701")) == "co-crs-2-3-pt17"
    assert vb.match("colorado", s("2-3-1601")) is None
    assert vb.match("colorado", s("24-33.5-1903")) == "co-crs-24-33-5-pt19"
    r = lambda n: res("co", n, n, corpus="REGULATION")
    assert vb.match("colorado", r("1501-5")) == "co-ccr-8-1501-5"
    assert vb.match("colorado", r("1501-12")) is None


def test_washington_section_and_chapter():
    s = lambda n: res("wa", n, n)
    assert vb.match("washington", s("43.105.025")) == "wa-rcw-43-105"
    assert vb.match("washington", s("43.1050.1")) is None
    assert vb.match("washington", s("42.56.590")) == "wa-rcw-42-56-590"
    assert vb.match("washington", s("42.56.591")) is None


def test_other_corpus_types_are_never_matched():
    assert vb.match("washington", res("wa", "x", "43.105.025", corpus="STATE_AG_OPINION")) is None


def test_scoring_counts_a_cell_at_each_cutoff():
    ranks = [None, None, None, None, None, "or-ors-276a"]
    assert vb.first_match_rank(ranks, {"or-ors-276a"}) == 6
    assert vb.first_match_rank(ranks, {"other"}) is None
    assert vb.passes(6, 5) is False and vb.passes(6, 10) is True and vb.passes(None, 10) is False


def test_section_in_text_uses_boundaries():
    assert vb.section_in_text("276A.203", "see 276A.203. The CIO") is True
    assert vb.section_in_text("276A.20", "see 276A.203. The CIO") is False
    assert vb.section_in_text("11546", "11546.1. text") is False
    assert vb.section_in_text("11546", "11546. text") is True


def test_class_a_when_any_expected_doc_is_a_mapped_statute_or_rule():
    assert vb.cell_class("oregon", ["or-das-107-004-130", "or-ors-276a"]) == "a"
    assert vb.cell_class("oregon", ["or-das-107-004-130", "or-eo-23-26"]) == "b"


def test_check_fails_when_a_stored_rank_is_wrong(tmp_path):
    (tmp_path / "_meta/eval/expected").mkdir(parents=True)
    (tmp_path / "_meta/eval/expected/oregon.yml").write_text(
        "jurisdiction: oregon\nquestions:\n- number: 1\n  expected:\n  - id: or-ors-276a\n    quote: q\n    where: w\n")
    cell = {"expected": ["or-ors-276a"], "scored": True, "class": "a", "first_match_rank": 1, "top5": True,
            "top10": True, "results": [{"matched": None}, {"matched": "or-ors-276a"}]}
    (tmp_path / vb.OUT).write_text(json.dumps({"cells": {"oregon": {"1": cell}}}))
    assert any("first_match_rank 1 != 2" in e for e in vb.check(tmp_path))
    cell["first_match_rank"] = 2
    (tmp_path / vb.OUT).write_text(json.dumps({"cells": {"oregon": {"1": cell}}}))
    assert vb.check(tmp_path) == []


def test_the_committed_baseline_is_consistent_with_the_current_expected_lists():
    assert vb.check(vb.ROOT) == []


def test_verdicts_cross_class_and_score_with_vaquills_own_noGoodMatch():
    c = lambda cls, top5, ngm, q: {"scored": True, "class": cls, "top5": top5, "noGoodMatch": ngm,
                                   "matchQuality": q}
    data = {"cells": {"oregon": {"1": c("a", True, True, "none"), "2": c("a", True, False, "strong"),
                                 "3": {"scored": False, "noGoodMatch": True, "matchQuality": "none"}}}}
    v = vb.verdicts(data)
    assert (v["searches"], v["ngm_searches"], v["scored"], v["ngm_scored"]) == (3, 2, 2, 1)
    assert v["cross"][("a", True, True)] == 1 and v["cross"][("a", True, False)] == 1
    assert v["quality"] == {"none": 1, "strong": 1}


def test_doc10_parse_gives_76_cells_and_agrees_with_the_hybrid_misses():
    top = vb.hybrid_doc10(vb.ROOT)
    assert len(top) == 76
    misses = {k for k, v in top.items() if not any(b for _, b in v)}
    assert misses == vb.HYBRID_MISSES_AT_5


def test_statute_or_rule_is_decided_by_the_documents_folder():
    assert vb.is_statute_or_rule(vb.ROOT, "oregon", "or-ors-276a") is True
    assert vb.is_statute_or_rule(vb.ROOT, "oregon", "or-eo-23-26") is False
