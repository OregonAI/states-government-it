# 11 — The 20 analyst questions through Vaquill: the outside baseline

Run 2026-11-12 (the balance calls bracketing the run are stamped 21:19 and 21:27 UTC) on branch `research/vaquill-baseline`, cut from `eval/analyst-questions` (the unmerged branch that holds `_meta/eval/`, `src/eval_questions.py` and `10-analyst-questions-hybrid-trial.md`). Issue #9; `docs/spec.md` "Done" item 2. Vaquill is the closest existing product (`01-prior-art.md`: hosted MCP server `mcp.vaquill.ai`, hybrid semantic and keyword search over state codes and regulations). Every number below is output of `src/vaquill_baseline.py` run over the saved raw responses (`--raw DIR --write --tables`); none is typed from memory. The scorer's explicit citation-to-document mapping is `RULES` in that file, tested in `tests/test_vaquill_baseline.py`.

## What was run

- **Free calls first:** `get_credit_balance`, `get_pricing` and `list_statutes_coverage` for OR, WA, CA and CO. `get_pricing` lists `search_us_statutes` at 4 credits without bodies; `includeBody` (6 credits per row that returns text), every per-section text tool and every unpriced tool were not used.
- **80 calls**, one per (question, state): tool `search_us_statutes`, `query` = the question text exactly as in `_meta/eval/questions.yml`, `state` = that state, the default meaning-ranked match type, `limit` 10, no `includeBody`. No `corpusType` filter: the schema does not require one, so each search covered everything Vaquill holds for the state. One `Idempotency-Key` per (question, state), derived from the pair, so a retry would not have been charged twice (none was needed). Rate: one call about every 2.5 seconds, under the 30 a minute limit; balance checked at the start, after every 20 calls and at the end.
- **Sent to the service:** the question text, the state code, `limit`, and the idempotency key. Nothing else.
- **Credits:** the script sums `creditsConsumed` over the 80 responses. Calls 80, credits spent 320, balance 1000 -> 680. The 400-credit cap and the 600-credit floor were not reached.
- **Raw responses are not committed** (Vaquill's data is licensed CC BY-NC). The repo holds `_meta/eval/vaquill-baseline.json`: per call the rank, citation, section id (`actId`), corpus type, official source URL and the match, plus the scoring and a sha256 of each raw file. No excerpts and no section text. Where this note quotes nothing, nothing is quoted.

## What Vaquill holds for these four states

From the free coverage call, section counts by corpus type:

Vaquill coverage held for each state (sections, from the free coverage call): oregon REGULATION 40975, STATE 71629, STATE_AGENCY_GUIDANCE 104, STATE_AG_OPINION 114, STATE_CONSTITUTION 388, STATE_RULES 788; washington REGULATION 51277, STATE 55994, STATE_AGENCY_GUIDANCE 25, STATE_AG_OPINION 4430, STATE_CONSTITUTION 273, STATE_REGISTER 6033, STATE_RULES 1433; california REGULATION 74785, STATE 161441, STATE_AGENCY_GUIDANCE 467, STATE_AG_OPINION 1967, STATE_CONSTITUTION 372, STATE_REGISTER 5147, STATE_RULES 4307; colorado REGULATION 1155, STATE 46888, STATE_AG_OPINION 109, STATE_CONSTITUTION 399, STATE_RULES 1194

- Statutes (`STATE`) and regulations (`REGULATION`) are held for all four. Colorado's regulations are thin: 1,155 sections against 40,975 for Oregon.
- No state holds governors' executive orders (the `EXECUTIVE_ACTION` type is federal Presidential documents), CIO policies, standards or memoranda. The only agency guidance is Oregon 104, Washington 25 and California 467 documents; in the 80 searches the Washington guidance that came back was an insurance-commissioner advisory, nothing from a state IT office. Colorado holds no agency guidance at all.
- So an expected document that is a statute or a rule could be returned; one that is an executive order, policy, standard or memorandum could not. This is the cell classification:
  - **(a)** at least one expected document is a statute or rule that `RULES` maps to Vaquill's citations.
  - **(b)** every expected document is sub-statutory.

Distinct expected documents by kind: oregon executive-orders 2, policies 17, rules 2, standards 1, statutes 1; washington executive-orders 1, policies 16, standards 3, statutes 4; california executive-orders 3, policies 15, standards 4, statutes 9; colorado policies 6, rules 3, standards 1, statutes 7.

## Method of scoring

A cell is a (state, question) pair with at least one expected document: the same 76 cells as `10`. It PASSES at 5 (or 10) when one of the first 5 (10) returned sections belongs to an instrument that an expected document mirrors, decided by `match()` from the returned citation fields and the expected document's own `citation` frontmatter. Examples: ORS 276A.300 is a section of chapter 276A, so it matches `or-ors-276a`; OAR 128-030-0020 matches `or-oar-128-30`; Cal. Gov't Code 11546.1 matches `ca-gov-11545-11548` (its range 11545 to 11548 includes decimal sections); Cal. Civ. Code 1798.100 does not match `ca-civ-1798-1798-78` (it is outside 1798 to 1798.78). A section that belongs to a mapped instrument that is not expected for that cell is not a match. Matches are by section number, so a historical-edition row (Colorado returned two) counts as its instrument; both are listed in the JSON.

The comparison columns are the figures in `10` at cut-off 5: keyword from `_meta/eval/baseline.json` (12 of 76), hybrid from `10` (69 of 76; the seven misses are listed in `HYBRID_MISSES_AT_5`, taken from `10`'s "Hybrid cells that miss at 5", not re-run: the hybrid leg needs the embedder, which was not loaded for this note).

## Result

Cut-off 5 for the keyword and hybrid columns; Vaquill at 5 and at 10.

| State | Cells | Keyword (5) | Hybrid (5) | Vaquill top 5 | Vaquill top 10 |
|---|---|---|---|---|---|
| oregon | 19 | 1/19 | 18/19 | 12/19 | 12/19 |
| washington | 19 | 5/19 | 17/19 | 10/19 | 10/19 |
| california | 20 | 5/20 | 17/20 | 15/20 | 16/20 |
| colorado | 18 | 1/18 | 17/18 | 14/18 | 14/18 |
| **all four** | 76 | **12/76** | **69/76** | **51/76** | **52/76** |

By class:

| Class | Cells | Keyword (5) | Hybrid (5) | Vaquill top 5 | Vaquill top 10 |
|---|---|---|---|---|---|
| (a) an expected statute or rule | 55 | 10/55 | 50/55 | 51/55 | 52/55 |
| (b) sub-statutory only | 21 | 2/21 | 19/21 | 0/21 | 0/21 |

By state and class:

| State and class | Cells | Keyword (5) | Hybrid (5) | Vaquill top 5 | Vaquill top 10 |
|---|---|---|---|---|---|
| oregon (a) | 12 | 1/12 | 11/12 | 12/12 | 12/12 |
| oregon (b) | 7 | 0/7 | 7/7 | 0/7 | 0/7 |
| washington (a) | 11 | 4/11 | 10/11 | 10/11 | 10/11 |
| washington (b) | 8 | 1/8 | 7/8 | 0/8 | 0/8 |
| california (a) | 17 | 4/17 | 15/17 | 15/17 | 16/17 |
| california (b) | 3 | 1/3 | 2/3 | 0/3 | 0/3 |
| colorado (a) | 15 | 1/15 | 14/15 | 14/15 | 14/15 |
| colorado (b) | 3 | 0/3 | 3/3 | 0/3 | 0/3 |

Per question (the class (a) count is how many of the four states have a statute or rule among the expected documents):

| Question | Cells | Class (a) cells | Keyword (5) | Hybrid (5) | Vaquill top 5 | Vaquill top 10 |
|---|---|---|---|---|---|---|
| 1 | 4 | 4 | 1/4 | 4/4 | 4/4 | 4/4 |
| 2 | 4 | 4 | 0/4 | 4/4 | 4/4 | 4/4 |
| 3 | 4 | 4 | 1/4 | 4/4 | 4/4 | 4/4 |
| 4 | 4 | 4 | 1/4 | 2/4 | 4/4 | 4/4 |
| 5 | 4 | 4 | 1/4 | 4/4 | 4/4 | 4/4 |
| 6 | 4 | 4 | 1/4 | 4/4 | 4/4 | 4/4 |
| 7 | 4 | 2 | 0/4 | 3/4 | 2/4 | 2/4 |
| 8 | 4 | 4 | 0/4 | 1/4 | 4/4 | 4/4 |
| 9 | 4 | 3 | 2/4 | 3/4 | 3/4 | 3/4 |
| 10 | 3 | 1 | 1/3 | 3/3 | 1/3 | 1/3 |
| 11 | 4 | 0 | 2/4 | 4/4 | 0/4 | 0/4 |
| 12 | 4 | 3 | 0/4 | 4/4 | 3/4 | 3/4 |
| 13 | 4 | 2 | 0/4 | 4/4 | 1/4 | 2/4 |
| 14 | 4 | 4 | 2/4 | 4/4 | 4/4 | 4/4 |
| 15 | 4 | 2 | 0/4 | 4/4 | 2/4 | 2/4 |
| 16 | 4 | 1 | 0/4 | 4/4 | 1/4 | 1/4 |
| 17 | 3 | 2 | 0/3 | 3/3 | 2/3 | 2/3 |
| 18 | 4 | 3 | 0/4 | 4/4 | 0/4 | 0/4 |
| 19 | 4 | 4 | 0/4 | 4/4 | 4/4 | 4/4 |
| 20 | 2 | 0 | 0/2 | 2/2 | 0/2 | 0/2 |

Cell by cell (rank = position of the first returned section of an expected instrument, blank = none in the 10; class in brackets):

| Q | oregon | washington | california | colorado |
|---|---|---|---|---|
| 1 | [a] 1 | [a] 1 | [a] 1 | [a] 1 |
| 2 | [a] 1 | [a] 1 | [a] 1 | [a] 1 |
| 3 | [a] 1 | [a] 1 | [a] 3 | [a] 1 |
| 4 | [a] 1 | [a] 1 | [a] 4 | [a] 1 |
| 5 | [a] 2 | [a] 2 | [a] 2 | [a] 3 |
| 6 | [a] 1 | [a] 1 | [a] 1 | [a] 1 |
| 7 | [b] - | [a] 1 | [b] - | [a] 1 |
| 8 | [a] 1 | [a] 2 | [a] 1 | [a] 1 |
| 9 | [a] 1 | [b] - | [a] 1 | [a] 3 |
| 10 | [b] - | [b] - | [a] 1 | no cell |
| 11 | [b] - | [b] - | [b] - | [b] - |
| 12 | [a] 1 | [b] - | [a] 3 | [a] 1 |
| 13 | [b] - | [b] - | [a] 10 | [a] 1 |
| 14 | [a] 1 | [a] 2 | [a] 1 | [a] 1 |
| 15 | [a] 1 | [b] - | [a] 3 | [b] - |
| 16 | [b] - | [b] - | [a] 4 | [b] - |
| 17 | no cell | [b] - | [a] 2 | [a] 1 |
| 18 | [b] - | [a] - | [a] - | [a] - |
| 19 | [a] 1 | [a] 1 | [a] 1 | [a] 1 |
| 20 | [b] - | no cell | [b] - | no cell |

Overlap with the hybrid leg at cut-off 5, by class:

| Class | Hybrid (5) | Vaquill (5) | Cells |
|---|---|---|---|
| a | miss | pass | 5 |
| a | pass | miss | 4 |
| a | pass | pass | 46 |
| b | miss | miss | 2 |
| b | pass | miss | 19 |

Vaquill misses at 5 in class (a): washington 18, california 13, california 18, colorado 18

## What the numbers say

- **Vaquill does what a statute and rule search can do, about as well as our hybrid leg.** In class (a), the 55 cells where an expected document is a statute or rule, Vaquill's top 5 holds an expected instrument in 51, our hybrid leg in 50, our keyword leg in 10. Of the 55 cells, 46 pass in both, 5 only in Vaquill and 4 only in hybrid. This is not a margin: at 55 cells and one run the two are tied.
- **Vaquill cannot answer class (b).** 21 of the 76 cells expect only executive orders, policies, standards or memoranda; Vaquill holds none for these states, so 0 of 21 by construction, while our hybrid leg passes 19 of 21. Across all 76 cells, Vaquill's 51 against hybrid's 69 is therefore the product of what each corpus holds, not of how each ranks: the whole difference sits in class (b), and class (b) is the part of the domain (`01-prior-art.md`: the sub-statutory layer, "unlikely" to be in Vaquill) the project exists for. Questions 11 and 20 have no class (a) cell at all.
- **Colorado:** Vaquill's 1,155 Colorado regulation sections include the Office of Information Technology's rules: it returned 8 CCR 1501-5, 1501-7 and 1501-11 in the cells that expect them (see the match table).
- **Where Vaquill misses class (a) at 5:** Washington 18, California 13, California 18 and Colorado 18 (the line under the overlap table). California 13 is a pass at 10 (first match at rank 10); Washington 18, California 18 and Colorado 18, all question 18 (disaster recovery), are misses at 10 as well. I did not read the returned sections to see whether they answer.
- **Vaquill returns sections, we return documents.** A chapter-sized instrument (ORS 276A, RCW 43.105, C.R.S. 24-37.5) can fill the top 5 with its own sections, and matching is by instrument. So "top 5" is not the same unit for the two systems, and a Vaquill top 5 can hold fewer distinct instruments than ours. The rank in the cell table is the rank of the section, not of a document.

## What Vaquill returned that our corpus does not hold

By the script: STATE or REGULATION instruments in a top-5 list that no statute or rule document of ours contains by section number. These are **candidate seed-list gaps, UNVERIFIED**: citations only. I read the returned titles (not the text) to flag which look relevant to the domain; none was confirmed against an official source, none is a recommendation to seed, and the seed list is the owner's.

- oregon:
  - OAR 125-247: questions [7, 9, 20]; returned OAR 125-247-0185, OAR 125-247-0691
  - ORS ch. 291: questions [1, 8, 9]; returned ORS 291.018, ORS 291.032, ORS 291.034, ORS 291.045
  - OAR 414-070: questions [7, 9]; returned OAR 414-070-0410
  - ORS ch. 283: questions [4, 8]; returned ORS 283.100, ORS 283.143
  - OAR 125-246: questions [20]; returned OAR 125-246-0360
  - OAR 167-001: questions [20]; returned OAR 167-001-0360
  - OAR 177-040: questions [17]; returned OAR 177-040-0070
  - OAR 259-007: questions [20]; returned OAR 259-007-0150

- washington:
  - RCW ch. 42.64: questions [10, 14, 15, 16]; returned RCW 42.64.010
  - RCW ch. 43.386: questions [10, 11, 15, 16]; returned RCW 43.386.020, RCW 43.386.030, RCW 43.386.050
  - RCW ch. 19.440: questions [12, 15, 16]; returned RCW 19.440.020, RCW 19.440.030, RCW 19.440.050
  - RCW ch. 19.435: questions [12, 15]; returned RCW 19.435.010, RCW 19.435.020
  - RCW ch. 41.05: questions [12, 16]; returned RCW 41.05.845
  - RCW ch. 43.41: questions [8, 9]; returned RCW 43.41.430, RCW 43.41.440, RCW 43.41.442
  - RCW ch. 48.43: questions [12, 16]; returned RCW 48.43.830
  - WAC ch. 182-70: questions [7, 17]; returned WAC 182-70-410, WAC 182-70-440, WAC 182-70-470

- california:
  - Cal. Bus. & Prof. Code § 22757.12: questions [10, 11]; returned Cal. Bus. & Prof. Code § 22757.12
  - Cal. Ins. Code § 10123.135: questions [12, 16]; returned Cal. Ins. Code § 10123.135
  - Cal. Bus. & Prof. Code § 22757.1: questions [12]; returned Cal. Bus. & Prof. Code § 22757.1
  - Cal. Bus. & Prof. Code § 22757.2: questions [15]; returned Cal. Bus. & Prof. Code § 22757.2
  - Cal. Bus. & Prof. Code § 22757.3: questions [15]; returned Cal. Bus. & Prof. Code § 22757.3
  - Cal. Bus. & Prof. Code § 22757.3.2: questions [15]; returned Cal. Bus. & Prof. Code § 22757.3.2
  - Cal. Bus. & Prof. Code § 6008.6: questions [9]; returned Cal. Bus. & Prof. Code § 6008.6
  - Cal. Civ. Code § 3110: questions [12]; returned Cal. Civ. Code § 3110

- colorado:
  - C.R.S. art. 6-1: questions [10, 11, 12, 13, 15, 16]; returned C.R.S. § 6-1-1315, C.R.S. § 6-1-1701, C.R.S. § 6-1-1702, C.R.S. § 6-1-1703, C.R.S. § 6-1-1704, C.R.S. § 6-1-1708, C.R.S. § 6-1-1710
  - C.R.S. art. 24-18: questions [11, 15]; returned C.R.S. § 24-18-302, C.R.S. § 24-18-304
  - 1 CCR 101-1: questions [9]; returned 1 CCR 101-1
  - 3 CCR 702-10: questions [10]; returned 3 CCR 702-10
  - 8 CCR 1507-40: questions [6]; returned 8 CCR 1507-40
  - C.R.S. art. 1-46: questions [12]; returned C.R.S. § 1-46-102
  - C.R.S. art. 10-16: questions [16]; returned C.R.S. § 10-16-112.7
  - C.R.S. art. 10-3: questions [16]; returned C.R.S. § 10-3-1104.9

By title, the ones that look relevant: Oregon OAR 125-247 (Department of Administrative Services rules, IT procurement approval) and ORS 283.100 to 283.143 (DAS information-technology and telecommunications functions); Washington RCW 43.41.430 to 43.41.450 (statewide IT investment pool and revolving accounts, which bear on question 8, funding), RCW 43.386 (agency notice, human review and testing before facial recognition) and WAC 182-70 (data vendor privacy and security requirements); Colorado C.R.S. 24-18-302 to 24-18-304 (government facial recognition: notice, human review, testing) and C.R.S. 6-1-1701 and following (the artificial-intelligence consumer-protection part of the Colorado code, whose reach to state agencies is not known to me). The California and Colorado insurance rows and the Business and Professions Code section 22757 rows came from questions about AI definitions, disclosure and adverse decisions, and by their titles they concern private parties; I do not think they are in scope. Whether any of these is state IT governance within `_meta/domain.yml`'s inclusion test is the owner's call.

## What our corpus holds that Vaquill cannot

- Every class (b) cell: 21 cells, 7 in Oregon, 8 in Washington, 3 in California, 3 in Colorado. The expected documents there are governors' executive orders, statewide policies and procedures, standards and memoranda, which none of Vaquill's four states' coverage holds. Our hybrid leg puts an expected document in the top 5 for 19 of them.
- Beyond the cells: the kinds line above shows that most distinct expected documents in Oregon, Washington and California are policies, standards or executive orders, which no Vaquill corpus holds for these states; Colorado's expected list is mostly statutes and rules plus policies and one standard.
- Vaquill returned no document from any state IT office in 80 searches (the only agency-guidance rows were seven repeats of one Washington insurance-commissioner advisory).

## What this does not show

- **One run, one query per cell.** The question as typed, default match type, one page of 10. No rewording, no `get_section_cross_state`, no boolean search, no `fifty_state_survey` prompt, no filters by code or chapter. A tuned Vaquill query could do better; so could a tuned query against ours.
- **Document-level (instrument-level) scoring against hand-made lists.** The expected lists in `_meta/eval/expected/` are not exhaustive, were written by the same author as our corpus, and name only documents we hold: a returned section we did not list may still be a good answer, and the 51 of 55 counts a hit on any section of the instrument, including sections that do not answer the question. Class (a) cells where Vaquill returned only sections of unlisted instruments are not shown to be wrong.
- **It does not read the answers.** I did not check whether the returned sections answer each question, only whether they belong to an expected instrument.
- **Two different units:** sections for Vaquill, documents for ours, and different cut-offs in practice.
- **The class (a) comparison is statutes and rules only** and rests on my mapping table; a different reasonable mapping (for example reading ORS 276A as the sections we hold, not the chapter) would move cell counts by a few.
- **The hybrid column is `10`'s figure**, taken as written, not re-run here; the hybrid leg is not the shipped configuration (`10`).
- **Vaquill's index is a point in time** (its own coverage call is stamped 2026-11-12) and its data is non-commercial licensed; this note is a comparison, not a recommendation to reuse its data.
- **No cost-benefit claim:** 320 credits is $3.20 at the listed 1 credit = $0.01; cost to a user over many questions was not measured.
