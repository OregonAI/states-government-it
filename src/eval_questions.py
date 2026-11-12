#!/usr/bin/env python3
"""The expected-documents check for the 20 analyst questions (issues #8 and #3).

  python3 src/eval_questions.py --check             # the gate: offline, keyword leg, no embedder
  python3 src/eval_questions.py --write-baseline    # record the keyword leg per cell (never by hand)
  python3 src/eval_questions.py --report [--json F] # keyword leg, and the hybrid leg when it can run

Inputs: `_meta/eval/questions.yml` (the 20 questions, as typed) and `_meta/eval/expected/<state>.yml`
(per question: the hand-listed expected documents, each with a verbatim quote, or a `none_reason`).

VALIDATION (a). Every question has an entry in every expected file; each entry has either documents
or a none_reason; every id is a real, non-stub document of that jurisdiction (a stub is a seed entry
with `stub: true`, or a document with content_mode: stub); every quote appears in that document's text
with whitespace collapsed.

RETRIEVAL (b). For each (state, question) with at least one expected document, the question text as
typed is run through CorpusFramework.compare (the code path the MCP `compare` tool uses) for that one
jurisdiction. The cell PASSES when an expected document is among the first CUTOFF hits. CUTOFF is 5.

LEGS (c). `keyword` is the toolkit's BM25 leg alone: every term must match (all-terms AND), so a long
question usually returns nothing. `hybrid` fuses BM25 with the semantic index (_meta/embeddings) and
needs the embedder to load (torch); it is never part of the gate.

THE GATE fails when an expected file is invalid, when the baseline is out of date with the questions or
the expected document ids, or when a cell that passes in `_meta/eval/baseline.json` no longer passes.
It does not fail because the pass rate is low: the rate is recorded, and that is the result.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CUTOFF = 5
SEMANTIC_MODULE = "corpus_toolkit.semantic.search"
EVAL = Path("_meta") / "eval"


def _load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def load_questions(root: Path) -> dict[int, str]:
    data = _load_yaml(root / EVAL / "questions.yml")
    return {int(q["number"]): str(q["text"]) for q in data["questions"]}


def load_expected(root: Path) -> dict[str, dict[int, dict]]:
    """{state: {question number: entry}} from `_meta/eval/expected/*.yml`, the state being the
    file's `jurisdiction`."""
    out: dict[str, dict[int, dict]] = {}
    for path in sorted((root / EVAL / "expected").glob("*.yml")):
        data = _load_yaml(path)
        out[str(data.get("jurisdiction") or path.stem)] = {
            int(q["number"]): q for q in data.get("questions") or []}
    return out


def _content_roots(root: Path) -> list[str]:
    cfg = _load_yaml(root / "_meta" / "corpus.yml")
    return [r["path"] for r in cfg["content_roots"]]


def _documents(root: Path, state: str) -> dict[str, dict]:
    """{id: {"mode": content_mode, "jurisdiction": ..., "text": body}} of the state's document files."""
    docs: dict[str, dict] = {}
    for folder in _content_roots(root):
        for path in sorted((root / folder / state).rglob("*.md")):
            raw = path.read_text(encoding="utf-8")
            if not raw.startswith("---\n"):
                continue
            head, _, body = raw[4:].partition("\n---\n")
            fm = yaml.safe_load(head) or {}
            if fm.get("id"):
                docs[str(fm["id"])] = {"mode": fm.get("content_mode"),
                                       "jurisdiction": fm.get("jurisdiction"), "text": _collapse(body)}
    return docs


def _seed_stubs(root: Path) -> dict[str, str]:
    """{id: state} of every seed entry marked `stub: true`."""
    out: dict[str, str] = {}
    for path in sorted((root / "_meta" / "sources").glob("*.yml")):
        for entry in (_load_yaml(path) or {}).get("sources") or []:
            if entry.get("stub") is True:
                out[str(entry.get("id"))] = path.stem
    return out


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        questions = load_questions(root)
        expected = load_expected(root)
    except (OSError, KeyError, TypeError, ValueError, yaml.YAMLError) as e:
        return [f"cannot read the questions or expected files: {type(e).__name__}: {e}"]
    if not questions:
        return ["_meta/eval/questions.yml holds no questions"]
    if not expected:
        return ["_meta/eval/expected/ holds no expected files"]
    stubs = _seed_stubs(root)
    for state, entries in expected.items():
        docs = _documents(root, state)
        for n in sorted(set(entries) - set(questions)):
            errors.append(f"{state}: question {n} is not one of the questions in questions.yml")
        for n in sorted(questions):
            entry = entries.get(n)
            if entry is None:
                errors.append(f"{state}: question {n} has no entry")
                continue
            listed = entry.get("expected") or []
            reason = str(entry.get("none_reason") or "").strip()
            if listed and reason:
                errors.append(f"{state}: question {n} has both expected documents and a none_reason")
            if not listed and not reason:
                errors.append(f"{state}: question {n} has no expected documents and no none_reason")
            for item in listed:
                doc_id, quote = str(item.get("id") or ""), _collapse(str(item.get("quote") or ""))
                where = f"{state}: question {n}, {doc_id or '(no id)'}"
                if doc_id in stubs or (doc_id in docs and docs[doc_id]["mode"] == "stub"):
                    errors.append(f"{where}: is a stub, which holds no text")
                    continue
                if doc_id not in docs:
                    other = [s for s in expected if s != state and doc_id in _documents(root, s)]
                    errors.append(f"{where}: unknown id for {state}"
                                  + (f" (it is a {other[0]} document)" if other else ""))
                    continue
                if not quote:
                    errors.append(f"{where}: no quote")
                elif quote not in docs[doc_id]["text"]:
                    errors.append(f"{where}: quote not found verbatim in the document: {quote[:80]!r}")
    return errors


def _framework(root: Path, semantic: bool):
    from corpus_toolkit import config as config_mod
    from corpus_toolkit.mcp.framework import CorpusFramework
    cfg = config_mod.load(root / "_meta" / "corpus.yml")
    cfg.semantic_search_module = SEMANTIC_MODULE if semantic else None
    return CorpusFramework(cfg)


def _summary(cells: dict) -> dict:
    per_state: dict = {}
    per_question: dict = {}
    for state, qs in cells.items():
        for n, cell in qs.items():
            for bucket, key in ((per_state, state), (per_question, n)):
                b = bucket.setdefault(key, {"passed": 0, "cells": 0})
                b["cells"] += 1
                b["passed"] += bool(cell["passed"])
    overall = {"passed": sum(v["passed"] for v in per_state.values()),
               "cells": sum(v["cells"] for v in per_state.values())}
    per_question = {k: per_question[k] for k in sorted(per_question, key=int)}
    return {"overall": overall, "per_state": per_state, "per_question": per_question}


def run_leg(root: Path = ROOT, mode: str = "keyword", cutoff: int = CUTOFF) -> dict:
    """Run one leg. `cells` holds a pass/fail per (state, question) with expected documents; `tops`
    holds the top ids for every (state, question), expected or not."""
    base = {"mode": mode, "cutoff": cutoff}
    if mode == "hybrid":
        if not (root / "_meta" / "embeddings" / "meta.json").exists():
            return {**base, "available": False, "reason": "no _meta/embeddings (the semantic index is not built)"}
        fw = _framework(root, True)
        if not (fw._semantic and fw._semantic.available()):
            return {**base, "available": False, "reason": "the embeddings could not be loaded (see stderr; "
                    "the embedder needs torch)"}
    else:
        fw = _framework(root, False)
    questions, expected = load_questions(root), load_expected(root)
    cells: dict = {}
    tops: dict = {}
    for state, entries in expected.items():
        cells[state], tops[state] = {}, {}
        for n in sorted(questions):
            res = fw.compare(questions[n], [state], limit_per_jurisdiction=cutoff, mode=mode)
            if "error" in res:
                raise RuntimeError(res["error"])
            top = [h["id"] for h in res["groups"][0]["hits"]][:cutoff]
            tops[state][str(n)] = top
            ids = [i["id"] for i in (entries.get(n) or {}).get("expected") or []]
            if ids:
                cells[state][str(n)] = {"passed": any(t in ids for t in top), "top": top, "expected": ids}
    return {**base, "available": True, "cells": cells, "tops": tops, **_summary(cells)}


def _fingerprint(root: Path) -> str:
    """Hash of what decides the cells: the question texts and the expected ids per cell. A changed quote
    does not change it (the quote is validated, not run)."""
    expected = load_expected(root)
    payload = {"questions": {str(n): t for n, t in sorted(load_questions(root).items())},
               "expected": {s: {str(n): sorted(i["id"] for i in e.get("expected") or [])
                                for n, e in sorted(es.items())} for s, es in sorted(expected.items())}}
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def build_baseline(root: Path = ROOT) -> dict:
    res = run_leg(root, "keyword", CUTOFF)
    return {"mode": "keyword", "cutoff": CUTOFF, "query": "the question text as typed, one jurisdiction at a time",
            "expected_fingerprint": _fingerprint(root), "overall": res["overall"],
            "per_state": res["per_state"], "cells": res["cells"]}


def check(root: Path = ROOT) -> tuple[list[str], dict]:
    errors = validate(root)
    if errors:
        return errors, {}
    path = root / EVAL / "baseline.json"
    if not path.exists():
        return [f"{EVAL / 'baseline.json'} is missing: run python3 src/eval_questions.py --write-baseline"], {}
    base = json.loads(path.read_text(encoding="utf-8"))
    if base.get("cutoff") != CUTOFF or base.get("expected_fingerprint") != _fingerprint(root):
        return ["the baseline is out of date with the questions or the expected files: "
                "run python3 src/eval_questions.py --write-baseline and commit it"], {}
    res = run_leg(root, "keyword", CUTOFF)
    for state, qs in base["cells"].items():
        for n, was in qs.items():
            now = res["cells"].get(state, {}).get(n)
            if was["passed"] and not (now and now["passed"]):
                errors.append(f"regression: {state} question {n} passed in the baseline and no longer does "
                              f"(expected {was['expected']}, top now {now['top'] if now else None})")
    return errors, res


def _fmt(r: dict) -> str:
    return f"{r['passed']}/{r['cells']}"


def _print_leg(res: dict) -> None:
    print(f"== {res['mode']} leg, cut-off {res['cutoff']}")
    if not res["available"]:
        print(f"   not run: {res['reason']}")
        return
    print(f"   overall {_fmt(res['overall'])}")
    for s, v in res["per_state"].items():
        print(f"   {s}: {_fmt(v)}")
    print("   per question: " + ", ".join(f"{n}={_fmt(v)}" for n, v in res["per_question"].items()))


def main(argv: list[str] | None = None, root: Path = ROOT) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true", help="the gate: offline, keyword leg only")
    g.add_argument("--write-baseline", action="store_true", help="record the keyword leg per cell")
    g.add_argument("--report", action="store_true", help="keyword leg, and the hybrid leg when it can run")
    ap.add_argument("--json", metavar="FILE", help="with --report: write both legs in full")
    args = ap.parse_args(argv)

    if args.check:
        errors, res = check(root)
        for e in errors:
            print(f"FAIL: {e}")
        if res:
            _print_leg(res)
        return 1 if errors else 0
    if args.write_baseline:
        errors = validate(root)
        if errors:
            for e in errors:
                print(f"FAIL: {e}")
            return 1
        base = build_baseline(root)
        (root / EVAL / "baseline.json").write_text(json.dumps(base, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {EVAL / 'baseline.json'}: keyword leg {_fmt(base['overall'])}")
        return 0
    errors = validate(root)
    for e in errors:
        print(f"FAIL: {e}")
    if errors:
        return 1
    legs = {m: run_leg(root, m, CUTOFF) for m in ("keyword", "hybrid")}
    for leg in legs.values():
        _print_leg(leg)
    if args.json:
        Path(args.json).write_text(json.dumps(legs, indent=1) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
