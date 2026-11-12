#!/usr/bin/env python3
"""Scores the outside baseline (issue #9): the 20 analyst questions run once through Vaquill's hosted
`search_us_statutes`, for the four pilot states, against the hand-listed expected documents.

  python3 src/vaquill_baseline.py --raw DIR --write      # rebuild _meta/eval/vaquill-baseline.json
  python3 src/vaquill_baseline.py --raw DIR --tables     # print the markdown tables used in docs/research/11
  python3 src/vaquill_baseline.py --check                # offline: the committed JSON is internally consistent

DIR holds one raw response per call (`search_qNN_<st>.json`, `{"request":..., "response":...}`), the free
`free_coverage_<st>.json` and the `free_balance_*.json` files. Raw responses are NOT committed (Vaquill's data
is CC BY-NC); the committed JSON holds only citations, section ids, official source URLs, ranks, the scoring
and a sha256 of each raw file. No excerpts, no titles, no section text.

MATCHING. A returned section MATCHES an expected document when it belongs to the instrument that document
mirrors. RULES is the explicit mapping, written by hand from each document's own `citation` frontmatter:
only statute and rule documents are mapped, because Vaquill's coverage for these four states holds statutes
(STATE), regulations (REGULATION), constitutions, court rules, AG opinions, registers and a little agency
guidance, and no governor's executive orders, CIO policies or standards. An unmapped expected document cannot
be matched. A cell is class (a) when at least one of its expected documents is mapped, class (b) otherwise.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = Path("_meta") / "eval" / "vaquill-baseline.json"
STATES = {"oregon": "or", "washington": "wa", "california": "ca", "colorado": "co"}
CUTOFFS = (5, 10)

# doc id -> (corpusType, spec). Spec kinds: chapter (result.chapter), prefix and exact (sectionNumber),
# regex (sectionNumber), range (code, lo, hi: sections lo..hi inclusive, with decimal sub-sections).
RULES: dict[str, list[tuple[str, str, tuple]]] = {
    "oregon": [
        ("or-ors-276a", "STATE", ("chapter", "276A")),                       # ORS chapter 276A
        ("or-oar-128-20", "REGULATION", ("prefix", "128-020-")),             # OAR chapter 128, division 20
        ("or-oar-128-30", "REGULATION", ("prefix", "128-030-")),             # OAR chapter 128, division 30
    ],
    "washington": [
        ("wa-rcw-39-26-340", "STATE", ("exact", "39.26.340")),
        ("wa-rcw-39-34-240", "STATE", ("exact", "39.34.240")),
        ("wa-rcw-42-56-590", "STATE", ("exact", "42.56.590")),
        ("wa-rcw-43-105", "STATE", ("prefix", "43.105.")),                   # RCW chapter 43.105
    ],
    "california": [
        ("ca-civ-1798-1798-78", "STATE", ("range", "ca_civ", "1798", "1798.78")),
        ("ca-gov-11531-11544", "STATE", ("range", "ca_gov", "11531", "11544")),
        ("ca-gov-11545-11548", "STATE", ("range", "ca_gov", "11545", "11548")),
        ("ca-gov-11549-11549-10", "STATE", ("range", "ca_gov", "11549", "11549.10")),
        ("ca-gov-11549-63-11549-66", "STATE", ("range", "ca_gov", "11549.63", "11549.66")),
        ("ca-gov-7405", "STATE", ("range", "ca_gov", "7405", "7405")),
        ("ca-gov-8586-5", "STATE", ("range", "ca_gov", "8586.5", "8586.5")),
        ("ca-gov-8592-30-8592-50", "STATE", ("range", "ca_gov", "8592.30", "8592.50")),
        ("ca-pcc-12100-12113", "STATE", ("range", "ca_pcc", "12100", "12113")),
    ],
    "colorado": [
        ("co-crs-2-3-pt17", "STATE", ("regex", r"2-3-17\d\d")),               # title 2, article 3, part 17
        ("co-crs-24-33-5-pt19", "STATE", ("regex", r"24-33\.5-19\d\d")),      # title 24, article 33.5, part 19
        ("co-crs-24-37-5", "STATE", ("prefix", "24-37.5-")),
        ("co-crs-24-37-7", "STATE", ("prefix", "24-37.7-")),
        ("co-crs-24-73", "STATE", ("prefix", "24-73-")),
        ("co-crs-24-74", "STATE", ("prefix", "24-74-")),
        ("co-crs-24-85", "STATE", ("prefix", "24-85-")),
        ("co-ccr-8-1501-5", "REGULATION", ("exact", "1501-5")),
        ("co-ccr-8-1501-7", "REGULATION", ("exact", "1501-7")),
        ("co-ccr-8-1501-11", "REGULATION", ("exact", "1501-11")),
    ],
}

# Hybrid leg at cut-off 5 from docs/research/10 ("Hybrid cells that miss at 5": seven cells). Everything else
# with expected documents passed. 69 of 76. The keyword leg per cell is read from _meta/eval/baseline.json.
HYBRID_MISSES_AT_5 = {("california", 4), ("california", 7), ("california", 8), ("colorado", 4),
                      ("oregon", 8), ("washington", 8), ("washington", 9)}


def section_key(num: str):
    try:
        return tuple(int(p) for p in str(num).split("."))
    except ValueError:
        return None


def _in_range(key, lo, hi) -> bool:
    return lo <= key and (key <= hi or key[:len(hi)] == hi)


def match(state: str, r: dict) -> str | None:
    """The id of the expected document whose instrument the returned section r belongs to, or None."""
    sec = str(r.get("sectionNumber") or "")
    code = (r.get("parent") or {}).get("code")
    for doc_id, corpus, spec in RULES.get(state, []):
        if r.get("corpusType") != corpus:
            continue
        kind = spec[0]
        if kind == "chapter" and str(r.get("chapter")) == spec[1]:
            return doc_id
        if kind == "prefix" and sec.startswith(spec[1]):
            return doc_id
        if kind == "exact" and sec == spec[1]:
            return doc_id
        if kind == "regex" and re.fullmatch(spec[1], sec):
            return doc_id
        if kind == "range" and code == spec[1]:
            key, lo, hi = section_key(sec), section_key(spec[2]), section_key(spec[3])
            if key and _in_range(key, lo, hi):
                return doc_id
    return None


def first_match_rank(matched: list, expected: set) -> int | None:
    for i, m in enumerate(matched, 1):
        if m is not None and m in expected:
            return i
    return None


def passes(rank: int | None, cutoff: int) -> bool:
    return rank is not None and rank <= cutoff


def cell_class(state: str, expected_ids) -> str:
    mapped = {d for d, _, _ in RULES.get(state, [])}
    return "a" if any(i in mapped for i in expected_ids) else "b"


def section_in_text(num: str, text: str) -> bool:
    return re.search(r"(?<![\w.\-])" + re.escape(num) + r"(?![\w\-]|\.\d)", text) is not None


def _collapse(t: str) -> str:
    return re.sub(r"\s+", " ", t)


def _held_texts(root: Path, state: str) -> dict[str, str]:
    out = {}
    for folder in ("statutes", "rules"):
        for p in sorted((root / folder / state).glob("*.md")):
            out[p.stem] = _collapse(p.read_text(encoding="utf-8"))
    return out


def _group(state: str, r: dict) -> str:
    sec, code = str(r.get("sectionNumber") or ""), (r.get("parent") or {}).get("code") or ""
    c = r.get("corpusType")
    if c == "STATE":
        if state == "oregon":
            return f"ORS ch. {r.get('chapter')}"
        if state == "washington":
            return "RCW ch. " + ".".join(sec.split(".")[:2])
        if state == "california":
            return f"{r.get('citation', '').split(' §')[0]} ch. {r.get('chapter')}" if r.get("chapter") else \
                f"{r.get('citation', '').split(' §')[0]} § {sec}"
        if state == "colorado":
            return "C.R.S. art. " + "-".join(sec.split("-")[:2])
    if c == "REGULATION":
        if state == "oregon":
            return "OAR " + "-".join(sec.split("-")[:2])
        if state == "washington":
            return f"WAC ch. {r.get('chapter')}"
        return f"{r.get('citation', '')}"
    return f"{c}: {r.get('citation')}"


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def build(raw: Path, root: Path = ROOT) -> dict:
    qs = {int(q["number"]): q["text"]
          for q in yaml.safe_load((root / "_meta/eval/questions.yml").read_text())["questions"]}
    expected = {}
    for st in STATES:
        d = yaml.safe_load((root / f"_meta/eval/expected/{st}.yml").read_text())
        expected[st] = {int(q["number"]): [e["id"] for e in q.get("expected") or []] for q in d["questions"]}
    kw = json.loads((root / "_meta/eval/baseline.json").read_text())["cells"]
    held = {st: _held_texts(root, st) for st in STATES}
    cells: dict = {st: {} for st in STATES}
    shas, credits, calls = {}, 0.0, 0
    for st, code in STATES.items():
        for n, text in qs.items():
            f = raw / f"search_q{n:02d}_{code}.json"
            data = json.loads(f.read_text())
            assert data["request"]["query"] == text and data["request"]["state"] == code, f.name
            assert data["request"]["limit"] == 10 and "includeBody" not in data["request"], f.name
            sc = data["response"]["result"]["structuredContent"]
            shas[f.name] = _sha(f)
            credits += float(sc["creditsConsumed"]); calls += 1
            exp = expected[st][n]
            rows, matched = [], []
            for i, r in enumerate(sc["results"], 1):
                m = match(st, r)
                matched.append(m)
                in_doc = None
                if m:
                    in_doc = section_in_text(str(r["sectionNumber"]), held[st].get(m, ""))
                rows.append({"rank": i, "citation": r["citation"], "actId": r["actId"],
                             "corpusType": r["corpusType"], "sourceUrl": r.get("sourceUrl"),
                             "matched": m, "section_in_our_document": in_doc})
            rank = first_match_rank(matched, set(exp))
            cell = {"expected": exp, "class": cell_class(st, exp) if exp else None,
                    "scored": bool(exp), "first_match_rank": rank,
                    "top5": passes(rank, 5) if exp else None, "top10": passes(rank, 10) if exp else None,
                    "matched_expected_top10": sorted({m for m in matched[:10] if m in set(exp)}),
                    "matchRank_any_instrument_top10": sorted({m for m in matched[:10] if m}),
                    "results": rows}
            if exp:
                cell["keyword_top5"] = bool(kw[st][str(n)]["passed"])
                cell["hybrid_top5"] = (st, n) not in HYBRID_MISSES_AT_5
            cells[st][str(n)] = cell
    bal = {p.stem: json.loads(p.read_text())["result"]["structuredContent"]
           for p in sorted(raw.glob("free_balance_*.json"))}
    cov = {}
    for st, code in STATES.items():
        j = json.loads((raw / f"free_coverage_{code}.json").read_text())["result"]["structuredContent"]["data"]
        jur = j["jurisdictions"][0]
        cov[st] = {"sectionCount": jur["sectionCount"], "corpora": jur["corpora"]}
        shas[f"free_coverage_{code}.json"] = _sha(raw / f"free_coverage_{code}.json")
    return {"tool": "search_us_statutes via mcp.vaquill.ai", "calls": calls, "credits_spent": credits,
            "balance_before": bal["free_balance_pre_run"]["creditsRemaining"],
            "balance_after": bal["free_balance_end"]["creditsRemaining"],
            "balance_as_of_start": bal["free_balance_pre_run"]["asOf"],
            "balance_as_of_end": bal["free_balance_end"]["asOf"],
            "coverage": cov, "raw_sha256": shas, "cells": cells}


def summary(data: dict) -> dict:
    """Counts from the cells: per state, per class, per question, at cut-offs 5 and 10."""
    out = {"all": Counter(), "state": defaultdict(Counter), "class": defaultdict(Counter),
           "question": defaultdict(Counter), "state_class": defaultdict(Counter)}
    for st, cs in data["cells"].items():
        for n, c in cs.items():
            if not c["scored"]:
                continue
            for bucket in (out["all"], out["state"][st], out["class"][c["class"]],
                           out["question"][int(n)], out["state_class"][(st, c["class"])]):
                bucket["cells"] += 1
                bucket["v5"] += c["top5"]; bucket["v10"] += c["top10"]
                bucket["kw5"] += c["keyword_top5"]; bucket["hy5"] += c["hybrid_top5"]
    return out


def candidates(data: dict, root: Path = ROOT, limit: int = 8) -> dict:
    """Per state, instruments (STATE / REGULATION) in Vaquill's top 5 that no document of ours holds,
    most cells first. `held` = the section number appears in some statute or rule document of the state."""
    held = {st: _held_texts(root, st) for st in STATES}
    out = {}
    for st, cs in data["cells"].items():
        agg: dict = defaultdict(lambda: {"cells": set(), "sections": {}})
        for n, c in cs.items():
            for r in c["results"][:5]:
                if r["corpusType"] not in ("STATE", "REGULATION"):
                    continue
                g = _group_from_row(st, r)
                agg[g]["cells"].add(int(n))
                agg[g]["sections"][r["citation"]] = any(
                    section_in_text(_secnum(r), t) for t in held[st].values())
        rows = [(g, sorted(v["cells"]), v["sections"]) for g, v in agg.items()
                if not any(v["sections"].values())]
        rows.sort(key=lambda x: (-len(x[1]), x[0]))
        out[st] = rows[:limit]
    return out


def _secnum(r: dict) -> str:
    cit = r["citation"]
    m = re.search(r"(?:§\s*|ORS |OAR |RCW |WAC |CCR )([\w.\-]+)", cit)
    return m.group(1) if m else cit


def _group_from_row(st: str, r: dict) -> str:
    sec = _secnum(r)
    fake = {"corpusType": r["corpusType"], "sectionNumber": sec, "citation": r["citation"],
            "chapter": sec.split(".")[0] if st == "oregon" and r["corpusType"] == "STATE" else None}
    if st == "washington" and r["corpusType"] == "REGULATION":
        fake["chapter"] = "-".join(sec.split("-")[:2])
    if st == "california" and r["corpusType"] == "STATE":
        fake["chapter"] = None
    if st == "oregon" and r["corpusType"] == "STATE":
        fake["chapter"] = re.match(r"\d+[A-Z]?", sec).group(0) if re.match(r"\d+[A-Z]?", sec) else sec
    return _group(st, fake)


def check(root: Path = ROOT) -> list[str]:
    """Offline: the committed JSON re-derives its own scoring from its own rows, and uses the current
    expected lists."""
    p = root / OUT
    if not p.exists():
        return [f"{OUT} is missing"]
    data = json.loads(p.read_text())
    errs = []
    for st, cs in data["cells"].items():
        exp = {int(q["number"]): [e["id"] for e in q.get("expected") or []] for q in
               yaml.safe_load((root / f"_meta/eval/expected/{st}.yml").read_text())["questions"]}
        for n, c in cs.items():
            if c["expected"] != exp[int(n)]:
                errs.append(f"{st} {n}: expected list changed since the run")
            if not c["scored"]:
                continue
            rank = first_match_rank([r["matched"] for r in c["results"]], set(c["expected"]))
            if rank != c["first_match_rank"]:
                errs.append(f"{st} {n}: first_match_rank {c['first_match_rank']} != {rank}")
            if c["top5"] != passes(rank, 5) or c["top10"] != passes(rank, 10):
                errs.append(f"{st} {n}: top5/top10 do not follow from the rank")
    return errs


def kinds(data: dict, st: str, root: Path = ROOT) -> Counter:
    ids = {i for c in data["cells"][st].values() for i in c["expected"]}
    out: Counter = Counter()
    for i in ids:
        for folder in ("statutes", "rules", "executive-orders", "policies", "standards"):
            if (root / folder / st / f"{i}.md").exists():
                out[folder] += 1
    return out


def tables(data: dict) -> str:
    s = summary(data)
    pct = lambda a, b: f"{a}/{b}"
    L = []
    a = s["all"]
    L.append("| State | Cells | Keyword (5) | Hybrid (5) | Vaquill top 5 | Vaquill top 10 |")
    L.append("|---|---|---|---|---|---|")
    for st in STATES:
        x = s["state"][st]
        L.append(f"| {st} | {x['cells']} | {pct(x['kw5'], x['cells'])} | {pct(x['hy5'], x['cells'])} | "
                 f"{pct(x['v5'], x['cells'])} | {pct(x['v10'], x['cells'])} |")
    L.append(f"| **all four** | {a['cells']} | **{pct(a['kw5'], a['cells'])}** | **{pct(a['hy5'], a['cells'])}** | "
             f"**{pct(a['v5'], a['cells'])}** | **{pct(a['v10'], a['cells'])}** |")
    L.append("")
    L.append("| Class | Cells | Keyword (5) | Hybrid (5) | Vaquill top 5 | Vaquill top 10 |")
    L.append("|---|---|---|---|---|---|")
    for k, name in (("a", "(a) an expected statute or rule"), ("b", "(b) sub-statutory only")):
        x = s["class"][k]
        L.append(f"| {name} | {x['cells']} | {pct(x['kw5'], x['cells'])} | {pct(x['hy5'], x['cells'])} | "
                 f"{pct(x['v5'], x['cells'])} | {pct(x['v10'], x['cells'])} |")
    L.append("")
    L.append("| State and class | Cells | Keyword (5) | Hybrid (5) | Vaquill top 5 | Vaquill top 10 |")
    L.append("|---|---|---|---|---|---|")
    for st in STATES:
        for k in "ab":
            x = s["state_class"][(st, k)]
            L.append(f"| {st} ({k}) | {x['cells']} | {pct(x['kw5'], x['cells'])} | {pct(x['hy5'], x['cells'])} | "
                     f"{pct(x['v5'], x['cells'])} | {pct(x['v10'], x['cells'])} |")
    L.append("")
    L.append("| Question | Cells | Class (a) cells | Keyword (5) | Hybrid (5) | Vaquill top 5 | Vaquill top 10 |")
    L.append("|---|---|---|---|---|---|---|")
    for n in range(1, 21):
        x = s["question"][n]
        na = sum(1 for st in STATES if data["cells"][st][str(n)]["class"] == "a")
        L.append(f"| {n} | {x['cells']} | {na} | {pct(x['kw5'], x['cells'])} | {pct(x['hy5'], x['cells'])} | "
                 f"{pct(x['v5'], x['cells'])} | {pct(x['v10'], x['cells'])} |")
    L.append("")
    L.append("Cell by cell (rank = position of the first returned section of an expected instrument, "
             "blank = none in the 10; class in brackets):")
    L.append("")
    L.append("| Q | oregon | washington | california | colorado |")
    L.append("|---|---|---|---|---|")
    for n in range(1, 21):
        row = []
        for st in STATES:
            c = data["cells"][st][str(n)]
            if not c["scored"]:
                row.append("no cell")
            else:
                row.append(f"[{c['class']}] " + (str(c["first_match_rank"]) if c["first_match_rank"] else "-"))
        L.append(f"| {n} | " + " | ".join(row) + " |")
    L.append("")
    L.append("First match in each scored cell that has one in the top 10 (state, question, rank, returned "
             "citation, expected document it was matched to, whether that section number appears in our "
             "mirrored document). Every match is in `_meta/eval/vaquill-baseline.json`.")
    L.append("")
    L.append("| State | Q | Rank | Returned citation | Matched document | In our document text |")
    L.append("|---|---|---|---|---|---|")
    for st in STATES:
        for n in range(1, 21):
            c = data["cells"][st][str(n)]
            if not c["scored"] or not c["first_match_rank"] or c["first_match_rank"] > 10:
                continue
            r = c["results"][c["first_match_rank"] - 1]
            L.append(f"| {st} | {n} | {r['rank']} | {r['citation']} | {r['matched']} | "
                     f"{'yes' if r['section_in_our_document'] else 'no'} |")
    L.append("")
    both = Counter()
    for st, cs in data["cells"].items():
        for c in cs.values():
            if c["scored"]:
                both[(c["class"], c["hybrid_top5"], c["top5"])] += 1
    L.append("| Class | Hybrid (5) | Vaquill (5) | Cells |")
    L.append("|---|---|---|---|")
    for k in sorted(both):
        L.append(f"| {k[0]} | {'pass' if k[1] else 'miss'} | {'pass' if k[2] else 'miss'} | {both[k]} |")
    L.append("")
    L.append("Vaquill misses at 5 in class (a): " + ", ".join(
        f"{st} {n}" for st, cs in data["cells"].items() for n, c in cs.items()
        if c["scored"] and c["class"] == "a" and not c["top5"]))
    L.append("")
    types = defaultdict(Counter)
    for st, cs in data["cells"].items():
        for c in cs.values():
            for r in c["results"]:
                types[st][r["corpusType"]] += 1
    L.append("Returned rows by corpus type (all 20 questions, top 10): " + "; ".join(
        f"{st}: " + ", ".join(f"{k} {v}" for k, v in sorted(types[st].items())) for st in STATES))
    L.append("")
    L.append("Vaquill coverage held for each state (sections, from the free coverage call): " + "; ".join(
        f"{st} " + ", ".join(f"{k} {v}" for k, v in sorted(data["coverage"][st]["corpora"].items()))
        for st in STATES))
    L.append("")
    L.append("Distinct expected documents by kind (from the document's folder): " + "; ".join(
        f"{st} " + ", ".join(f"{k} {v}" for k, v in sorted(kinds(data, st).items())) for st in STATES))
    L.append("")
    L.append(f"Calls {data['calls']}, credits spent {data['credits_spent']:g}, balance "
             f"{data['balance_before']:g} -> {data['balance_after']:g}.")
    L.append("")
    L.append("Candidate gaps (STATE/REGULATION instruments in a top-5 list that no statute or rule document of "
             "ours contains by section number; UNVERIFIED):")
    for st, rows in candidates(data).items():
        L.append("")
        L.append(f"- {st}:")
        for g, qs, secs in rows:
            L.append(f"  - {g}: questions {qs}; returned {', '.join(sorted(secs))}")
    return "\n".join(L)


def main(argv=None, root: Path = ROOT) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", type=Path)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--tables", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        errs = check(root)
        print("\n".join(errs) or "vaquill baseline consistent")
        return 1 if errs else 0
    data = build(a.raw, root)
    if a.write:
        (root / OUT).write_text(json.dumps(data, indent=1, sort_keys=True) + "\n")
        print(f"wrote {OUT}")
    if a.tables:
        print(tables(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
