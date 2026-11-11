# Spec: states-it-governance pilot

Status: agreed in grilling on 2026-11-10. Research behind it is in `docs/research/01`–`03`.

## Purpose

An MCP server over the full text of how state governments regulate their own information
technology, including government use of AI, so an AI agent can compare how states handle
the same problem. It is a research tool, not a product.

This repo is also the proof of a repeatable pattern: a second policy domain (for example
career and technical education) must need a new repo of content and no new shared code.

## User

A state IT policy analyst drafting or revising policy, working through an AI agent. They
ask questions like "how do the other three states set project oversight thresholds?" and
need passages with citations they can open at the official source.

## Scope

**States:** Oregon, Washington, California, Colorado.

**Inclusion test:** the obligated party is a state government entity or its contractor,
and the subject is IT, data or AI as a government function.

**Sub-areas** (the tag vocabulary):

| Tag | Sub-area |
|---|---|
| `governance` | IT governance and organization: CIO office, authority, boards |
| `oversight` | IT planning, investment and project oversight |
| `procurement` | IT acquisition and procurement |
| `funding` | IT funding models |
| `cybersecurity` | Cybersecurity of state systems |
| `data` | Governance and privacy of government-held data |
| `ai` | Government use of AI |
| `digital-services` | Digital services, accessibility, identity |
| `cloud-resilience` | Cloud, enterprise architecture, resilience |

**Instrument types:** statute, administrative rule, executive order, CIO-issued policy or
standard. In force only. Full text, not summaries.

**Out:** private-sector AI regulation, consumer privacy law, deepfakes and AI crimes,
broadband and telecom, law-enforcement technology, election systems, K-12 edtech,
legislative and judicial branch IT, local government instruments, federal requirements,
bills not yet enacted. Contested cases follow the recommendation column of
`docs/research/03-domain-taxonomy.md` section 3.3; in particular, public-records and
breach statutes come in only for their IT-specific or government-applicable provisions.

**Not in the pilot:** coded per-state answers. The server returns text; the agent reasons.

## Corpus rules

1. **Seed list per state.** Every document enters through a seed list that an agent
   proposes and the owner approves. Nothing enters by crawling. A seed entry names the
   instrument, its citation, official URL, instrument type and sub-area tags.
2. **Official sources.** Statutes and rules are fetched from the official state site.
   The Hugging Face bulk datasets (`reglab/statecodes`, `vaquill/open-us-law`) may be
   used to find candidates, never as the text of record.
3. **Tags are per document**, set in the seed list. No per-passage tagging.
4. **Stubs.** A known instrument that is not public, or whose official source cannot be
   fetched, becomes a stub: title, issuer, citation, link and the reason. No unofficial
   copies are used in its place.
5. **Provenance.** Every document carries source URL, fetch date, content hash, and an
   effective date where the source gives one.
6. **In force only.** A replaced instrument is removed; git history is the record.
7. **Robots.txt and no-scrape terms** are set aside for the pilot. Fetches still identify
   themselves honestly and are rate-limited.

## Tools

| Tool | Behaviour |
|---|---|
| `search` | Hybrid keyword and semantic search. Filters: state, sub-area tag, instrument type. |
| `get_document` | Full text and provenance of one document. |
| `compare` | Runs one query separately per requested state and returns the top passages grouped by state, so a state with more text cannot crowd out another. |
| `coverage` | What is loaded per state and sub-area, counting stubs separately, so "no provision found" is distinguishable from "not in the corpus". |

Every result carries the document's citation and official source URL. The server is a
non-authoritative mirror and says so.

## Architecture

- **This repo** is a corpus-toolkit corpus created from corpus-template, pinned to a
  toolkit tag. It holds the domain pack and the documents, and no search code.
- **Domain pack** = this repo's scope statement, tag vocabulary, per-state seed lists and
  test questions.
- **corpus-toolkit** provides fetch, frontmatter schema, validation gates, drift
  detection, PDF text extraction, index build, hybrid search and the MCP server.
- **Toolkit changes needed**, built as general features and released under the normal
  toolkit release process:
  - documents in one corpus may carry different jurisdictions (`us-or`, `us-wa`, ...);
  - `search` filters on jurisdiction and tag;
  - `compare` and `coverage` tools;
  - stub documents as a recognised content mode, if the schema does not already allow it.
- **Hosting:** one service on the existing deploy box at
  `oregonai.morficflux.com/<id>/mcp`. Not added to corpus-gateway until the pilot passes
  its test.

## Keeping current

A monthly drift run covers every document and each state's index pages (policy library,
executive order list). A change to an index page raises a "review the seed list" report.
Any addition or removal goes through seed-list approval.

## Done

1. Each of the 20 analyst questions in `docs/research/03-domain-taxonomy.md` section 5
   has a hand-listed set of expected documents per state, drawn from the approved seed
   lists, and an automated check confirms they appear in the top results of `compare`.
2. The same 20 questions are run once through Vaquill's free tier as an outside baseline,
   and the comparison is written up.
3. `coverage` reports the share of each state that is stubbed.
4. The server is live on the deploy box.

## Build order

1. Oregon end to end on the toolkit as it is today: seed list, ingest, gates, search.
2. Toolkit changes and release.
3. Washington, California, Colorado.
4. Test questions and baseline.
5. Deploy.

## Open

- GitHub repo, visibility and licence: on hold.
- Whether a toolkit plugin could add the filters without a toolkit change was not
  confirmed; the decision is to change the toolkit either way.
- The two Hugging Face datasets have not been downloaded or checked.
- The legal footing for mirroring CIO policies is weaker than for statute
  (`docs/research/02-source-availability.md` section 1.2). Accepted for a research tool;
  revisit before the repo is made public.
- California's administrative rules are published only through Westlaw and will likely
  be stubs.
