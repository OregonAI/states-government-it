"""Seam: src.eval_questions -- validate(root), run_leg(root, mode), build_baseline(root),
check(root) and main(argv, root). Each test states one thing the expected-documents check owes
the owner. The corpora here are tiny temporary ones with real documents on disk, queried through
the toolkit's own CorpusFramework.compare (the code path the MCP "compare" tool uses)."""
import json
import re
import shutil
from pathlib import Path

import pytest
import yaml

from src import eval_questions as ev

REPO = Path(__file__).resolve().parent.parent

DOC_OR = ("The Governor shall appoint the State Chief Information Officer, who serves at the "
          "pleasure of the Governor.\n\nThe officer sets enterprise standards for every agency.")
DOC_OR2 = "Agencies shall report cloud purchases to the Department of Administrative Services."
DOC_WA = "The Washington consolidated technology services agency   is overseen by a board."


def write_doc(root: Path, state: str, doc_id: str, body: str, folder="statutes", mode="verbatim"):
    p = root / folder / state / f"{doc_id}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    fm = {"schema_version": 1, "corpus": "states-government-it", "jurisdiction": state,
          "id": doc_id, "title": f"Title of {doc_id}", "doc_type": "statute",
          "citation": f"Cite {doc_id}", "source_url": "https://example.gov/x",
          "source_format": "html", "retrieved": "2026-11-10", "status": "current",
          "content_mode": mode}
    p.write_text("---\n" + yaml.safe_dump(fm) + "---\n\n## Full text\n\n" + body + "\n")


def make_repo(tmp_path: Path) -> Path:
    root = tmp_path
    (root / "_meta" / "eval" / "expected").mkdir(parents=True)
    shutil.copy(REPO / "_meta" / "corpus.yml", root / "_meta" / "corpus.yml")
    write_doc(root, "oregon", "or-a", DOC_OR)
    write_doc(root, "oregon", "or-b", DOC_OR2)
    write_doc(root, "washington", "wa-a", DOC_WA)
    seed = root / "_meta" / "sources"
    seed.mkdir()
    (seed / "oregon.yml").write_text(yaml.safe_dump({"sources": [
        {"id": "or-eo-stub", "stub": True, "stub_reason": "scan"},
        {"id": "or-a"}, {"id": "or-b"}]}))
    (seed / "washington.yml").write_text(yaml.safe_dump({"sources": [{"id": "wa-a"}]}))
    questions = [{"number": 1, "text": "Governor appoint State Chief Information Officer"},
                 {"number": 2, "text": "agency cloud purchases"},
                 {"number": 3, "text": "technology services agency board"}]
    (root / "_meta" / "eval" / "questions.yml").write_text(yaml.safe_dump({"questions": questions}))
    exp = {
        "oregon": [
            {"number": 1, "expected": [{"id": "or-a", "quote": "appoint the State Chief  Information Officer"}]},
            {"number": 2, "expected": [{"id": "or-b", "quote": "report cloud purchases"}]},
            {"number": 3, "expected": [], "none_reason": "No Oregon instrument."}],
        "washington": [
            {"number": 1, "expected": [], "none_reason": "Not held."},
            {"number": 2, "expected": [], "none_reason": "Not held."},
            {"number": 3, "expected": [{"id": "wa-a", "quote": "consolidated technology services agency is overseen"}]}],
    }
    for state, qs in exp.items():
        write_expected(root, state, qs)
    return root


def write_expected(root, state, qs):
    (root / "_meta" / "eval" / "expected" / f"{state}.yml").write_text(
        yaml.safe_dump({"jurisdiction": state, "questions": qs}))


def edit_expected(root, state, fn):
    p = root / "_meta" / "eval" / "expected" / f"{state}.yml"
    d = yaml.safe_load(p.read_text())
    fn(d["questions"])
    p.write_text(yaml.safe_dump(d))


@pytest.fixture
def repo(tmp_path):
    return make_repo(tmp_path)


def test_valid_expected_files_have_no_errors(repo):
    assert ev.validate(repo) == []


def test_quote_matches_after_whitespace_collapse(repo):
    # DOC_WA has three spaces, the quote one; the quote spans a paragraph break in OR
    edit_expected(repo, "oregon", lambda qs: qs[0]["expected"][0].update(
        quote="Officer, who serves at the pleasure of the Governor. The officer sets"))
    assert ev.validate(repo) == []


def test_broken_quote_is_named(repo):
    edit_expected(repo, "oregon", lambda qs: qs[0]["expected"][0].update(quote="appoint the Chief Technology Officer"))
    out = ev.validate(repo)
    assert len(out) == 1 and "oregon" in out[0] and "or-a" in out[0] and "quote" in out[0]


def test_unknown_id_is_named(repo):
    edit_expected(repo, "oregon", lambda qs: qs[0]["expected"][0].update(id="or-nope"))
    out = ev.validate(repo)
    assert len(out) == 1 and "or-nope" in out[0] and "unknown" in out[0]


def test_stub_id_is_refused_as_a_stub(repo):
    edit_expected(repo, "oregon", lambda qs: qs[0]["expected"].append({"id": "or-eo-stub", "quote": "anything"}))
    out = ev.validate(repo)
    assert len(out) == 1 and "or-eo-stub" in out[0] and "stub" in out[0]


def test_content_mode_stub_document_is_refused(repo):
    write_doc(repo, "oregon", "or-c", "No text held.", mode="stub")
    edit_expected(repo, "oregon", lambda qs: qs[0]["expected"].append({"id": "or-c", "quote": "No text held."}))
    out = ev.validate(repo)
    assert len(out) == 1 and "or-c" in out[0] and "stub" in out[0]


def test_id_of_another_jurisdiction_is_refused(repo):
    edit_expected(repo, "oregon", lambda qs: qs[0]["expected"].append({"id": "wa-a", "quote": "board"}))
    out = ev.validate(repo)
    assert len(out) == 1 and "wa-a" in out[0] and "oregon" in out[0]


def test_missing_question_is_named(repo):
    edit_expected(repo, "washington", lambda qs: qs.pop(1))
    out = ev.validate(repo)
    assert len(out) == 1 and "washington" in out[0] and "question 2" in out[0]


def test_question_with_neither_documents_nor_reason_fails(repo):
    edit_expected(repo, "oregon", lambda qs: qs[2].pop("none_reason"))
    out = ev.validate(repo)
    assert len(out) == 1 and "question 3" in out[0] and "none_reason" in out[0]


def test_question_with_documents_and_a_reason_fails(repo):
    edit_expected(repo, "oregon", lambda qs: qs[0].update(none_reason="x"))
    assert any("both" in e for e in ev.validate(repo))


def test_question_number_outside_the_list_fails(repo):
    edit_expected(repo, "oregon", lambda qs: qs.append({"number": 99, "expected": [], "none_reason": "x"}))
    assert any("99" in e for e in ev.validate(repo))


def test_no_expected_files_fails(repo):
    for p in (repo / "_meta" / "eval" / "expected").glob("*.yml"):
        p.unlink()
    assert ev.validate(repo)


# ---- the retrieval leg -------------------------------------------------------------------

def test_keyword_leg_marks_a_cell_pass_when_an_expected_document_is_in_the_top(repo):
    res = ev.run_leg(repo, "keyword", cutoff=5)
    cell = res["cells"]["oregon"]["1"]
    assert cell["passed"] is True and cell["top"][0] == "or-a" and cell["expected"] == ["or-a"]


def test_cells_exist_only_where_documents_are_expected(repo):
    res = ev.run_leg(repo, "keyword", cutoff=5)
    assert sorted(res["cells"]["oregon"]) == ["1", "2"]
    assert sorted(res["cells"]["washington"]) == ["3"]


def test_a_query_that_finds_nothing_is_a_fail_with_an_empty_top(repo):
    q = repo / "_meta" / "eval" / "questions.yml"
    d = yaml.safe_load(q.read_text())
    d["questions"][0]["text"] = "Governor appoint the Chief Technology Officer for aliens"
    q.write_text(yaml.safe_dump(d))
    cell = ev.run_leg(repo, "keyword", cutoff=5)["cells"]["oregon"]["1"]
    assert cell["passed"] is False and cell["top"] == []


def test_results_are_restricted_to_the_jurisdiction(repo):
    write_doc(repo, "washington", "wa-b", DOC_OR)   # same words, other state
    cell = ev.run_leg(repo, "keyword", cutoff=5)["cells"]["oregon"]["1"]
    assert "wa-b" not in cell["top"]


def test_cutoff_limits_how_far_down_an_expected_document_counts(repo):
    for i in range(3):
        write_doc(repo, "oregon", f"or-x{i}", "Governor appoint State Chief Information Officer " * 6)
    deep = ev.run_leg(repo, "keyword", cutoff=1)["cells"]["oregon"]["1"]
    wide = ev.run_leg(repo, "keyword", cutoff=5)["cells"]["oregon"]["1"]
    assert len(deep["top"]) == 1 and len(wide["top"]) == 4 and wide["passed"] is True


def test_rates_overall_per_state_and_per_question(repo):
    res = ev.run_leg(repo, "keyword", cutoff=5)
    assert res["overall"] == {"passed": 3, "cells": 3}
    assert res["per_state"]["oregon"] == {"passed": 2, "cells": 2}
    assert res["per_question"]["3"] == {"passed": 1, "cells": 1}


def test_hybrid_leg_is_unavailable_without_embeddings(repo):
    res = ev.run_leg(repo, "hybrid", cutoff=5)
    assert res["available"] is False and "embeddings" in res["reason"]


# ---- the baseline and the gate ------------------------------------------------------------

def test_baseline_records_the_keyword_leg_per_cell(repo):
    base = ev.build_baseline(repo)
    assert base["mode"] == "keyword" and base["cutoff"] == 5
    assert base["cells"]["oregon"]["1"]["passed"] is True
    assert base["overall"] == {"passed": 3, "cells": 3}


def write_baseline(repo):
    (repo / "_meta" / "eval" / "baseline.json").write_text(json.dumps(ev.build_baseline(repo)))


def test_check_passes_when_nothing_changed(repo):
    write_baseline(repo)
    assert ev.check(repo)[0] == []


def test_check_fails_without_a_baseline(repo):
    assert any("baseline" in e for e in ev.check(repo)[0])


def test_check_fails_on_a_broken_quote(repo):
    write_baseline(repo)
    edit_expected(repo, "oregon", lambda qs: qs[0]["expected"][0].update(quote="not in the text"))
    assert any("quote" in e for e in ev.check(repo)[0])


def test_check_fails_on_an_unknown_id(repo):
    write_baseline(repo)
    edit_expected(repo, "oregon", lambda qs: qs[0]["expected"][0].update(id="or-nope"))
    assert any("unknown" in e for e in ev.check(repo)[0])


def test_check_fails_on_a_stub_id(repo):
    write_baseline(repo)
    edit_expected(repo, "oregon", lambda qs: qs[0]["expected"][0].update(id="or-eo-stub"))
    assert any("stub" in e for e in ev.check(repo)[0])


def test_check_fails_on_a_missing_question(repo):
    write_baseline(repo)
    edit_expected(repo, "oregon", lambda qs: qs.pop(0))
    assert any("question 1" in e for e in ev.check(repo)[0])


def test_check_fails_on_a_regressed_cell(repo):
    write_baseline(repo)
    # the document still holds the quote (so validation passes) but no longer matches the query
    write_doc(repo, "oregon", "or-a", "Officials appoint the State Chief Information Officer.")
    errs = ev.check(repo)[0]
    assert any("regress" in e and "oregon" in e and "question 1" in e for e in errs)


def test_check_does_not_fail_because_the_pass_rate_is_low(repo):
    q = repo / "_meta" / "eval" / "questions.yml"
    d = yaml.safe_load(q.read_text())
    for x in d["questions"]:
        x["text"] = "zzzz qqqq unmatched words"
    q.write_text(yaml.safe_dump(d))
    write_baseline(repo)                      # baseline records 0 of 3
    errs, report = ev.check(repo)
    assert errs == [] and report["overall"] == {"passed": 0, "cells": 3}


def test_check_fails_when_the_baseline_is_out_of_date_with_the_expected_files(repo):
    write_baseline(repo)
    edit_expected(repo, "oregon", lambda qs: qs[0]["expected"].append(
        {"id": "or-b", "quote": "report cloud purchases"}))
    assert any("out of date" in e for e in ev.check(repo)[0])


def test_check_fails_when_a_question_text_changes_after_the_baseline(repo):
    write_baseline(repo)
    q = repo / "_meta" / "eval" / "questions.yml"
    d = yaml.safe_load(q.read_text())
    d["questions"][1]["text"] = "something else entirely"
    q.write_text(yaml.safe_dump(d))
    assert any("out of date" in e for e in ev.check(repo)[0])


def test_a_newly_passing_cell_does_not_fail_the_check(repo):
    q = repo / "_meta" / "eval" / "questions.yml"
    good = q.read_text()
    d = yaml.safe_load(good)
    d["questions"][0]["text"] = "aliens zzzz"
    q.write_text(yaml.safe_dump(d))
    write_baseline(repo)                      # question 1 fails in this baseline
    q.write_text(good)                        # ...and now passes
    errs = ev.check(repo)[0]
    assert all("regress" not in e for e in errs)


def test_main_check_exit_codes(repo, capsys):
    assert ev.main(["--check"], root=repo) == 1             # no baseline yet
    assert ev.main(["--write-baseline"], root=repo) == 0
    assert (repo / "_meta" / "eval" / "baseline.json").exists()
    assert ev.main(["--check"], root=repo) == 0
    edit_expected(repo, "oregon", lambda qs: qs[0]["expected"][0].update(id="or-nope"))
    assert ev.main(["--check"], root=repo) == 1


def test_write_baseline_refuses_invalid_expected_files(repo):
    edit_expected(repo, "oregon", lambda qs: qs[0]["expected"][0].update(id="or-nope"))
    assert ev.main(["--write-baseline"], root=repo) == 1
    assert not (repo / "_meta" / "eval" / "baseline.json").exists()


# ---- the committed files ------------------------------------------------------------------

def section5_questions():
    text = (REPO / "docs" / "research" / "03-domain-taxonomy.md").read_text()
    sec = text.split("## 5. Example analyst questions", 1)[1].split("\n## ", 1)[0]
    out = {}
    for m in re.finditer(r"^(\d+)\. (.+)$", sec, re.M):
        out[int(m.group(1))] = re.sub(r"(\s*\[[A-Z0-9-]+\])+\s*$", "", m.group(2)).strip()
    return out


def test_committed_questions_are_the_twenty_of_the_taxonomy_section_5():
    want = section5_questions()
    assert sorted(want) == list(range(1, 21))
    got = {q["number"]: q["text"] for q in yaml.safe_load(
        (REPO / "_meta" / "eval" / "questions.yml").read_text())["questions"]}
    assert got == want


def test_committed_expected_files_are_the_four_pilot_states():
    names = sorted(p.stem for p in (REPO / "_meta" / "eval" / "expected").glob("*.yml"))
    assert names == ["california", "colorado", "oregon", "washington"]
