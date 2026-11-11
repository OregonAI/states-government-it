# 01 — Prior art: 50-state law MCP servers, data sources, comparison tools

Researched 2026-11-10. Sources are the projects' own repos, docs, dataset cards and terms unless marked.
**UNVERIFIED** = could not be confirmed from a primary source. **BLOCKED** = the site refused automated fetching.
Verdicts: **reuse** (build on it), **competitor** (overlaps the product), **reference** (useful input, not machine-reusable), **irrelevant**.

## 0. Bottom line

- The claim "no one has combined semantic vector search with cross-state comparative primitives in an MCP server" is **false as worded**. Two servers already do it over codified state law: **Vaquill MCP** and **America's Law Graph**. Both are general-purpose and commercially operated.
- The claim survives only in a narrow form: nobody ships an **open, domain-scoped** server whose corpus is curated to one policy domain and includes the non-statutory layer (executive orders, agency IT policies and standards) with **structured** comparison (same attribute, every state, with "no provision found" distinguished from "not in corpus").
- Biggest reuse finding: bulk codified statutes for ~all states now exist as open datasets (**reglab/statecodes**, MIT; **vaquill/open-us-law**, CC BY-NC 4.0 data + Apache-2.0 scrapers). The 50-state scraping problem does not have to be solved from zero.

## 1. MCP servers over state legislation or law

| Server | Text indexed | Tools (from README) | Semantic search | Cross-state compare | Access / licence | Verdict |
|---|---|---|---|---|---|---|
| [Vaquill MCP](https://github.com/Vaquill-AI/vaquill-mcp) (hosted `mcp.vaquill.ai`) | USC, CFR, state statutes, state regulations, constitutions, court rules, Fed. Register, EOs, agency guidance. Docs state 56 jurisdictions, 2,642,636 state statute sections and 1,504,702 state regulation sections ([coverage](https://www.vaquill.ai/docs/api-guide/coverage.md)) | 37 US tools incl. `search_us_statutes`, `get_section_cross_state`, `list_statutes_coverage`, `get_section_changes`; prompt `fifty_state_survey(topic, states)` | Yes: "Hybrid semantic + keyword search", plus Boolean mode | Yes: `get_section_cross_state` = "Provisions in other states addressing the same subject, ranked by similarity"; at most one provision per state, up to 25 states, no page two ([docs repo](https://github.com/Vaquill-AI/vaquill-ai-docs), `api-guide/pagination.mdx`, `recipes/multi-state-comparison.mdx`) | Client MIT; backend proprietary, API key, credit-metered (500 free credits; free keys for non-commercial on request, per [open-us-law README](https://github.com/Vaquill-AI/open-us-law)). Per-credit price not published on pages fetched | **Competitor** (closest existing thing) |
| [America's Law Graph](https://github.com/edgardomunoznajar/america-law-graph) | "529,386 statute sections", 5,164 works, 50 states + DC + USC + CFR | 11 tools incl. `semantic_search` ("Vector similarity search across 529K embedded sections"), `compare_jurisdictions` ("Compare how different states regulate a topic"), `traverse_graph`, `get_recent_changes` | Yes | Yes (tool exists; behaviour not inspected, backend closed) | npm shim is MIT; README says "Proprietary", 100 calls/day free. Repo last pushed 2026-04-04, 2 stars; `americalawgraph.ai` returned 404 on 2026-11-10. 529K sections is well under a quarter of the ~1.8M sections other corpora hold, so coverage is partial. Data sources **UNVERIFIED** | **Competitor**, possibly dormant |
| [state-statutes-mcp](https://github.com/vvXranjan/state-statutes-mcp) | Codified statutes fetched live from official state sites; 44/50 states (AR, IN, LA, MS, TN, UT missing) | `list_states`, `list_titles`, `list_chapters`, `list_sections`, `get_section` | No (no search at all) | No | No licence file; last push 2026-09-02 | **Reference** (per-state adapter notes in `docs/research/`) |
| [pipeworx-io `mcp-<state>-code`](https://github.com/pipeworx-io) | One MCP per state code (40+ repos seen), statutes by citation, some topic search | Citation lookup per state | No | No | MIT (per sampled repos) | Irrelevant (single-state lookup) |
| [GroundRules](https://glama.ai/mcp/connectors/ai.agentlookups/groundrules) (`law.agentlookups.ai/mcp`) | USC, CFR, some state and local codes; state list not published on the listing | `law_search` (has a meaning-only mode), `law_get_section`, `law_for_location`, `law_coverage` | Partial | No | Operator, pricing, licence **UNVERIFIED** (directory listing only) | Irrelevant / watch |
| [cyanheads/openstates-mcp-server](https://github.com/cyanheads/openstates-mcp-server) | **Bills**, legislators, committees, events via Open States API v3. No codified law | 10 tools: `openstates_search_bills`, `openstates_get_bill`, people, committees, events, jurisdictions | No (upstream Postgres full-text) | No. README warns a `q`-only search across all 56 jurisdictions "exceeds the upstream timeout for a common term" | Apache-2.0; needs free Open States key; public host `openstates.caseyjhand.com/mcp` | **Reuse** as a bill-tracking sidecar; not a competitor |
| [sh-patterson/legiscan-mcp](https://github.com/sh-patterson/legiscan-mcp) | **Bills**, votes, people via LegiScan API | 10 tools: `legiscan_search`, `legiscan_get_bill`, roll calls, legislator composites | No | No | MIT; needs LegiScan key | Irrelevant (bill tracking, legislator-centric) |
| [Bill Commons](https://github.com/GDACS-droid/billcommons) (`mcp.billcommons.org/mcp`) | 209k+ current-session **bills**, full text, built on Open States bulk CSV + v3 API | 10 tools incl. `search_legislation`, `get_bill_record`, `compare_bill_versions`, `trace_legislative_history` | No evidence (Postgres `pg_trgm`/`unaccent`) | No (compares versions of one bill, not states) | Apache-2.0; no key, 2,000 req/day anonymous | **Reference** (good open architecture for the bill layer) |
| [civic-awareness-mcp](https://github.com/julianken/civic-awareness-mcp) | State bills (Open States), Congress.gov, OpenFEC | 8 state tools, title search only | No | No | MIT | Irrelevant |
| [open-legal-compliance-mcp](https://github.com/TCoder920x/open-legal-compliance-mcp) | USC/CFR via GovInfo; state codes scraped for CA, NY, IL only; Open States bills | `search_state_law`, `search_open_states`, etc. | No | No | MIT; last push 2025-12 | Irrelevant |
| CourtListener MCPs ([blakeox](https://github.com/blakeox/courtlistener-mcp), [cyanheads](https://github.com/cyanheads/courtlistener-mcp-server), [Vaquill-AI](https://github.com/Vaquill-AI/courtlistener-mcp), [DefendTheDisabled](https://github.com/DefendTheDisabled/courtlistener-mcp)) | Case law, dockets, judges. CourtListener's API overview lists no statutes or legislation ([API docs](https://wiki.free.law/c/courtlistener/help/api/rest/v4/overview)) | Opinion/docket search | Some (DefendTheDisabled advertises semantic search) | No | Mostly MIT | Irrelevant to statutes |
| Congress.gov / GovInfo / eCFR MCPs ([congress_gov_mcp](https://github.com/AshwinSundar/congress_gov_mcp), [govinfo-mcp](https://github.com/Travis-Prall/govinfo-mcp), [ecfr-mcp-safety-net](https://github.com/ctrimm/ecfr-mcp-safety-net)) | Federal only | — | `ecfr-mcp-safety-net` is a **domain-scoped** eCFR slice with semantic search and point-in-time | No | MIT | Irrelevant for states; `ecfr-mcp-safety-net` is the nearest precedent for "one domain slice as an MCP" |
| [AI Law Radar](https://ailawradar.com/api) | Curated register of AI-law **obligations and deadlines**, not law text; jurisdiction list not shown on the API page | `search_obligations`, `next_deadlines`, `list_jurisdictions`, `recent_changes` | No | No | Free API + MCP; data CC BY 4.0 | **Reference** (domain-scoped, but private-sector obligations) |

Not found: any official MCP server from LegiScan, Plural/Open States, Justia, Cornell LII, NCSL or NASCIO (GitHub and web search, 2026-11-10).

## 2. 50-state data sources

### 2a. Bulk codified statutes and regulations (the layer the pilot needs most)

| Source | Coverage | Format | Licence | Freshness | Verdict |
|---|---|---|---|---|---|
| [reglab/statecodes](https://huggingface.co/datasets/reglab/statecodes) (Stanford RegLab; paper [arXiv:2508.19365](https://arxiv.org/abs/2508.19365), Hariri & Ho) | `all_codes`: 1,844,116 rows; `all_regs`: 2,208,863 rows; fields `url, state, path, title, content`. Paper calls it "a novel and comprehensive state statute and regulatory corpus of 8.7 GB" | Parquet, ungated | **MIT** (dataset card) | Static; last modified 2025-05-02. Underlying text source and per-state completeness are not stated on the card: **UNVERIFIED** | **Reuse** — best-licensed starting corpus; needs a per-state audit and a refresh path |
| [vaquill/open-us-law](https://huggingface.co/datasets/vaquill/open-us-law) + [repo](https://github.com/Vaquill-AI/open-us-law) | Snapshot v2026.09.1: 5,081,709 sections; statutes 1,828,123 across 48 jurisdictions; regulations 1,383,931 across 40; AG opinions, court rules, agency guidance, constitutions. Statute scrapers "in progress" for AR, CO, GA, MS, TN; state-regulation scrapers listed for 14 states | Parquet (27-column schema, `act_status`, citation, hierarchy, `source_url`); scrapers emit JSONL | Data **CC BY-NC 4.0**; scrapers **Apache-2.0**. Commercial use of the compilation needs a licence | "New dated snapshots quarterly"; README warns snapshots are "point-in-time, not current law" | **Reuse the scrapers** freely; reuse the data only if a non-commercial licence on the derived corpus is acceptable |
| [davidawad/statedb](https://github.com/davidawad/statedb) | "(almost) all" state codes scraped from Justia, JSON; README says "not comprehensive" | JSON | MIT code; text from Justia | Dead since 2020 | Irrelevant |
| [Public.Resource.Org](https://law.resource.org/pub/us/code/) | Directories for AR, CA (+CCR), CO, DE, GA, ID, MS, OR, TN | Not stated on listing | No licence statement on the page | Stale: directory dates 2013–2024 | Irrelevant as a corpus; matters as the *Georgia v. PRO* precedent |
| [Justia US Law](https://law.justia.com/codes/) | State codes, all states (**UNVERIFIED**) | HTML | Terms page **BLOCKED** (HTTP 403) | **UNVERIFIED** | Not usable without reading terms |
| [Cornell LII](https://www.law.cornell.edu/lii/terms/documentation) | Federal primary law; state law section largely links out (**UNVERIFIED** whether hosted) | HTML | LII markup CC BY-NC-SA 2.5; no consent to "commercial redistribution" | — | Irrelevant |
| [Free Law Project / CourtListener](https://wiki.free.law/c/courtlistener/help/api/rest/v4/overview) | Case law, PACER, judges; no statutes | REST API | Open-source API; 5 req/min, 50/hour, 125/day authenticated | Live | Irrelevant to this layer |
| [Open Law Library](https://www.openlawlib.org/) | Publishing platform for governments; only DC named on the homepage (`code.dccouncil.gov`) | "computer-friendly formats"; specifics not stated | "without onerous copyright restrictions"; licence not named | Live for client jurisdictions | Irrelevant at 50-state scale |
| Casetext | Folded into Thomson Reuters; closed | — | — | **UNVERIFIED** | Irrelevant |

### 2b. Bills and session legislation

| Source | Coverage | Format / API | Licence | Cost | Verdict |
|---|---|---|---|---|---|
| [Open States API v3](https://docs.openstates.org/api-v3/) (Plural) | Bills, people, committees, events; 50 states + DC + territories | REST, key required. `/bills` has `q` = "Filter by full text search term", implemented as Postgres `websearch_to_tsquery` ([api-v3 `bills.py`](https://github.com/openstates/api-v3)) — keyword, not semantic | API code MIT; [scrapers](https://github.com/openstates/openstates-scrapers) GPL-3.0 | Free key; rate limits exist ([changelog](https://github.com/openstates/documentation)) but current tiers **UNVERIFIED** | **Reuse** for the "pending/recent bills" layer |
| [Open States bulk data](https://open.pluralpolicy.com/data/) | Per-session CSV and JSON (JSON "Include full text"), plus a PostgreSQL dump | CSV / JSON / pgdump | "provided under a public domain dedication"; attribution requested | Free; monthly | **Reuse** |
| [LegiScan API](https://api.legiscan.com/dl/LegiScan_API_User_Manual.pdf) (manual rev. 20250317) | Bills, texts, amendments, votes, people; 50 states + Congress. Bills only | JSON API: `getSearch`, `getBillText` (base64), `getDataset` weekly session ZIPs | Web pages **BLOCKED** (403). CC BY 4.0 licence is reported by search snippets of `legiscan.com/legiscan/features` but not read directly: **UNVERIFIED** | Manual: "Public service keys have a monthly limit of 30,000 queries". Paid tier prices **UNVERIFIED** | Second-choice bill source; Open States is more open |
| [Plural](https://pluralpolicy.com/) | "all 50 states, DC, Puerto Rico, Congress, and 40+ countries"; AI summaries on arrival | SaaS | Closed | $609/yr Essential, $5,000/yr Professional, Enterprise custom | Competitor on tracking only; no cross-state statute comparison advertised |
| [Quorum State](https://www.quorum.us/products/state/) | 50 legislatures + DC + PR; AI assistant; "side-by-side comparisons of similar bills moving in different states" | SaaS, API product listed | Closed | Custom quote | Competitor on bills, closed |
| FiscalNote, StateScape | Commercial trackers | — | — | Pages **BLOCKED**/404: **UNVERIFIED** | Closed; irrelevant to reuse |

## 3. Cross-state comparison products and research

| Item | What it is | Access | Verdict |
|---|---|---|---|
| [vLex Vincent "50-State Survey"](https://support.vlex.com/vincent-by-vlex/vincent/core-workflows/50-state-survey) | LLM workflow "running a single, natural-language question across all 50 US states and federal law"; table with a row per state, per-state memo, authorities with confidence scores | Subscription | **Competitor** (closed; lawyer-facing, any topic) |
| [Lexis+ AI Protégé "Survey of Laws and Regulations"](https://www.lexisnexis.com/community/amp-insights/81/cut-multi-state-legal-research-from-weeks-to-minutes-with-lexis-ai) | Natural-language prompt to a 50-state chart with AI summaries, clickable citations, Excel/PDF export | Subscription | **Competitor** (closed) |
| [Westlaw Jurisdictional Surveys](https://www.thomsonreuters.com/en-us/help/westlaw-precision/tools/jurisdictional-surveys) | Compare laws on a topic across U.S.C.A., 50 states, DC, CFR; reports to Word/PDF/CSV. This help page mentions no AI; the "AI Jurisdictional Surveys" CoCounsel help page returned 404 (**UNVERIFIED**) | Subscription | **Competitor** (closed) |
| Bloomberg Law Chart Builders | Editor-built state-law comparison charts by topic; official page not found: **UNVERIFIED** (library guides only) | Subscription | Competitor (closed, fixed topics) |
| [NCSL legislation databases](https://www.ncsl.org/technology-and-communication/ncsl-50-state-searchable-bill-tracking-databases) | Topic bill trackers, "powered by State Net" (LexisNexis). Human-tagged bills, not statute comparison | Public web search forms; no export or API shown; NCSL terms forbid republishing or copying "without permission" ([terms](https://www.ncsl.org/terms-of-use)) | **Reference** only — not machine-reusable |
| [Correlates of State Policy](https://ippsr.msu.edu/public-policy/correlates-state-policy) (MSU IPPSR) | 3,000+ coded variables, 50 states, ~1900–2019; CSV + R package. Coded variables, no law text | Free; no licence named | **Reference** (covariates; possible evaluation labels) |
| SPID (Boehmke et al., *Policy Studies Journal* 2020) | 728 policies with first-adoption year per state. Details from search summary and R docs only; Dataverse page did not render: **UNVERIFIED** | Free (Harvard Dataverse) | **Reference** (adoption dates, no text) |
| [dssg/policy_diffusion](https://github.com/dssg/policy_diffusion) (Legislative Influence Detector) | Text-reuse detection across state bills and model legislation. Last push 2016, 50 stars | MIT | **Reference** (method only; dead code) |
| Open-source RAG over state law on GitHub | Searches for state-statute RAG / embeddings / cross-state comparison returned nothing beyond the MCP servers in §1 and single-state demos (e.g. [semantic-law-search](https://github.com/ALPHAintelligenceBD/semantic-law-search), NY only) | — | Nothing to reuse |

## 4. Pilot domain: state government IT, cybersecurity, data, AI

| Item | Covers | Machine-readable? | Verdict |
|---|---|---|---|
| [NCSL AI Legislation Database](https://www.ncsl.org/financial-services/artificial-intelligence-legislation-database) | Bills 2025–present, all introduced, monthly; 25 topics incl. "Government Use" ("use of AI by government agencies and law enforcement") | No export/API; State Net-powered; bill text via LexisNexis links | **Reference** — the best seed list for the AI slice, hand-harvest only |
| [NCSL AI 2025 Legislation summary](https://www.ncsl.org/technology-and-communication/artificial-intelligence-2025-legislation) | One HTML table: jurisdiction, bill, status, summary, category; "Thirty-eight states adopted or enacted around 100 measures" | HTML table only; copying restricted by NCSL terms | Reference |
| [NCSL Cybersecurity 2025 Legislation](https://www.ncsl.org/technology-and-communication/cybersecurity-2025-legislation) and Cybersecurity database (2026–present, enacted-only) | 800+ bills in 49 states; includes state-agency items (e.g. Idaho H 35 MFA mandate for state agencies) | HTML table only | Reference |
| [NASCIO resource center](https://www.nascio.org/resource-center/) | Annual State CIO Survey, governance and AI reports, podcasts, awards | PDFs and media. No statute compendium or 50-state legal comparison found | Reference (context, vocabulary for the domain definition) |
| [CDT, "Regulating Public Sector AI"](https://cdt.org/insights/regulating-public-sector-ai-emerging-trends-in-state-legislation/) (2025-01-10) | "at least 16 states ... have passed legislation" on government agency AI use | Prose with links; no dataset | Reference (seed list) |
| [MultiState AI tracker](https://www.multistate.ai/artificial-intelligence-ai-legislation) | 1,561 AI bills in 45 states (March 2026); interactive map | No download or API stated | Reference |
| [IAPP state AI governance tracker](https://iapp.org/resources/article/us-state-ai-governance-legislation-tracker) | Private-sector bills; explicitly "excluding government-only bills" | Chart/map; all rights reserved | Irrelevant (wrong scope) |
| Law-firm trackers (Orrick, Steptoe, Clifford Chance, Epstein Becker) | AI bills, mostly private-sector | PDFs / web apps; not examined individually: **UNVERIFIED** | Irrelevant |

No machine-readable, 50-state source was found for: state CIO enabling statutes, IT procurement/oversight statutes, or — most importantly — the sub-statutory layer (governors' executive orders on AI/cyber, statewide IT policy manuals and standards issued by CIO offices). Vaquill lists executive orders and "state agency guidance" (13,402 documents, described as bulletins, per [legal-api page](https://www.vaquill.ai/legal-api)); whether any of that reaches state IT policy is **UNVERIFIED** and unlikely.

## 5. Verdict on the claim

**Killed as stated.** Closest existing things, in order:

1. **Vaquill MCP** — hybrid semantic search over all state codes and regulations plus a dedicated cross-state primitive (`get_section_cross_state`) and a `fifty_state_survey` prompt. Actively maintained (pushed 2026-11-10).
2. **America's Law Graph** — `semantic_search` + `compare_jurisdictions` over 529K sections; small, proprietary, apparently idle since April 2026.
3. **Closed legal-research products** — vLex Vincent, Lexis Protégé and Westlaw do LLM 50-state surveys, just not over MCP.

What is still true: none of these is **domain-specific**, none is **open end to end** (corpus + index + server), and their comparison primitive is "nearest similar section per state", not a structured comparison along defined policy attributes.

## 6. Gaps that remain open

1. **Domain-scoped corpus.** No one publishes a curated, per-domain slice (which sections in each state belong to "state IT governance") with a swappable domain definition. General servers leave the agent to find the slice by search, state by state.
2. **Sub-statutory policy.** Executive orders, statewide IT/security/AI policies and standards, CIO office directives. No aggregator covers these for any domain; for the pilot domain this is where much of the real policy lives.
3. **Structured comparison.** Attribute-level answers (e.g. "does the CIO have procurement approval authority; cite it") across all states, with explicit absent / not-in-corpus / not-yet-reviewed states. Vaquill returns at most 25 similar sections with no second page; NCSL-style trackers are hand-coded and closed.
4. **Enacted law joined to pending bills** per domain. Statute corpora and bill trackers are separate products; only Vaquill mentions session laws, and the open bill servers have no codified text.
5. **Openness and licence.** The only MIT-licensed 50-state corpus (reglab/statecodes) is a static 2025 snapshot with undocumented provenance; the fresher one (open-us-law) is non-commercial. An openly licensed, refreshed, provenance-tracked corpus does not exist.
6. **Evaluation.** No public benchmark for cross-state comparison accuracy in a policy domain. CSPP/SPID coded variables and NCSL topic tags are the nearest ground truth.

## 7. Implications for the project (short)

- Do not pitch novelty on "semantic search + cross-state compare over MCP". Pitch domain curation, the sub-statutory layer, structured comparison, and openness.
- Start the statute layer from reglab/statecodes and/or the Apache-2.0 open-us-law scrapers rather than writing 50 scrapers; budget for a per-state completeness audit and for the five states both projects struggle with (AR, GA, MS, TN, plus CO).
- Use Open States bulk data (public domain) for the bill layer; treat NCSL and NASCIO as human-read seed lists, not data feeds.
- Decide early whether CC BY-NC data is acceptable; if not, MIT statecodes + own refresh is the path.
- Try Vaquill's free tier on the pilot questions before building: it is the baseline the project has to beat.

## 8. Not verified / blocked

- LegiScan web pages (licence, paid pricing): HTTP 403. Only the API manual PDF was read.
- Justia terms of service: HTTP 403.
- FiscalNote: HTTP 403. StateScape tracker URL: 404. `americalawgraph.ai`: 404. Smithery listing for America's Law Graph: 404.
- Thomson Reuters "AI Jurisdictional Surveys" help page: 404. Bloomberg Law Chart Builders: no official page found.
- SPID Dataverse page did not render; Bill Commons directory listing returned 503 (repo README used instead).
- Vaquill per-credit pricing and the behaviour of America's Law Graph's `compare_jurisdictions` were not tested (no accounts created, no tools called).
- reglab/statecodes text provenance and per-state completeness.
