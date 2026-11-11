# 03 — Domain taxonomy: state government IT (with AI)

Research date: 2026-11-10. Question: what does a "domain definition" consist of, how do existing bodies carve up and compare this domain, and how much of that is generic?

Citations use the keys in [Sources](#sources). Anything not confirmed from a primary source on the research date is marked **UNVERIFIED**. Blocked or missing sources are listed in [Access problems](#access-problems-and-gaps).

## 1. Headline findings

1. **Every serious tracker draws the same first line: who is the obligated party.** Government-as-user and private-sector regulation are separated by NCSL (separate tags) [NCSL-AIDB], IAPP (excludes "government-only bills") [IAPP-AI], FPF (private-sector report; government bills kept only where they bind vendors) [FPF-2025], CDT (counts only bills "focused solely on government agencies' use") [CDT-LEG], and NCSL's data security tables (state-government table separate from private-sector table) [NCSL-DSL]. The pilot boundary should use the same test.
2. **Much of this domain is not statute.** NCSL: "At least 30 states have issued guidance on state agency use through governor executive orders, agency collaboration, rulemaking and state legislation" [NCSL-VT]. State CISO authority comes from statute (63%), CIO/secretary directive (35%), administrative rule (31%), executive order (22%), interagency agreement (16%) [DELOITTE-2024]. A statutes-only corpus would miss most of the comparison surface.
3. **The best comparison dimensions for state IT are in surveys, not legal trackers.** NASCIO compares states through CIO self-report (percentages, no state-by-state legal coding) [CIO-2024][CIO-2025]. No source found codes CIO statutory authority, procurement authority or project-oversight thresholds across 50 states (see gaps). That is the open niche.
4. **Bill trackers classify bills; they do not code law in force.** NCSL, MultiState, FPF, BSA and university trackers tag bills by topic per session [NCSL-AIDB][MULTISTATE][FPF-2025][BSA-2024][UF-PURC][DU-CAID]. Only the policy-surveillance method (Temple CPHLR / LawAtlas) codes the law in force, per jurisdiction, with effective dates, a published protocol and codebook [PHLR-M1][PHLR-M3][PHLR-M7].
5. **One precedent already applies policy surveillance to this exact topic:** ASTHO's LawAtlas dataset on state-agency use of AI, 50 jurisdictions, Jan 2023 to Sep 2024, with published protocol and codebook [ASTHO-DS][ASTHO-PROTO].

## 2. How existing bodies carve the domain

### 2.1 State government IT

| Body | Instrument | How it carves the domain | Source |
|---|---|---|---|
| NASCIO | State CIO Top Ten 2026 (51 CIOs, 20th year) | Strategies/policy: 1 AI (governance, policies, use cases...), 2 Cybersecurity and risk management (incl. "whole-of-state"), 3 Budget/cost control, 4 Modernization, 5 Digital government/services, 6 Accessibility (incl. procurement, DOJ rule), 7 Identity and access management, 8 Data management and analytics, 9 Consolidation/optimization, 10 Cloud services (incl. governance, procurement) | [TOP10-2026][TOP10-PAGE] |
| NASCIO | State CIO Survey 2025 (51 CIOs, summer 2025) | Sections: Dimensions of Leadership; IT Accessibility; Generative AI; Modernization/Innovation Funding; Cloud; Data Governance and Management; State and Local Collaboration; Service Delivery | [CIO-2025] |
| NASCIO | State CIO Survey 2024 (49 CIOs) | Sections: Generative AI; Digital Services; Enterprise Architecture; Business Continuity/DR/Resiliency; Business Operating Models; Acquisition; Workforce; Identity and Access Management; Federal Cybersecurity Funding | [CIO-2024] |
| NASCIO | Governance testimony (Kentucky, Dec 2023) | CIO role wheel: State IT governance; enterprise project and portfolio management; security and risk; enterprise architecture; legislation, policy and directives; strategic planning; operations and infrastructure; acquisition and contracting; BRM/customer service; cross-boundary collaboration. Organization spectrum of five models from "complete decentralization" to "unified". CIO reporting map: cabinet/reports to governor (25), reports to agency head (26), reports to board (2), updated Nov 2023 | [NASCIO-KY] |
| Deloitte-NASCIO | Cybersecurity Study 2024 | CISO authority mechanism; status of cyber statutes by provision (CISO role and authority; threat information sharing; continuity of government), each coded established-and-funded / established-not-funded / in progress / not in place | [DELOITTE-2024] |
| NCSL | Cybersecurity legislation pages | 2025 page: flat bill table (Jurisdiction, Bill, Title, Status, Summary), no categories; scope "deal significantly with cybersecurity"; 800+ bills. 2021 page gave themes: agency training / formal security policies / incident response planning; insurance; task forces; training and education programs | [NCSL-CYBER25][NCSL-CYBER21] |
| NCSL | "Data Security Laws: State Government" 50-state table | Columns: State; Statutory citation; Applies to (which government entities); Summary. 32 states. Excludes private-sector laws and data-type-specific laws. Last updated Feb 2020 (stale) | [NCSL-DSL] |
| NCSL | Database index | Separate databases for AI, Cybersecurity (enacted only), Consumer Privacy, Broadband, 911, Autonomous Vehicles, Social Media and Children, State Elections; all "powered by State Net" | [NCSL-DBS] |
| Center for Digital Government | Digital States Survey (biennial, self-reported) | 2024 areas: aligned leadership; constituent digital experience; continuous innovation; cyber risk management; data governance and use; workforce planning; IT investment management; resilience; enterprise computing and broadband expansion; business process alignment (source says 11 areas, lists 10). 2026 award categories add Artificial Intelligence. Letter grades A to C | [DSS-GA][DSS-2026] |
| GAO | GAO-20-123 | Federal requirements states must meet: CMS (MARS-E), FBI CJIS Security Policy, IRS Publication 1075, SSA TSSR; 49 to 79 percent of requirement parameters conflict across agencies | [GAO-20-123] |
| GovRAMP (formerly StateRAMP) | Participating governments list | 33 states listed; "NIST 800-53-based approach to cloud security"; statuses Snapshot / Core / Ready / Authorized-Provisional; some states "requiring GovRAMP authorization for certain cloud services" (not named) | [GOVRAMP] |
| NIST | CSF 2.0 | "For industry, government, and organizations". Six functions (Govern, Identify, Protect, Detect, Respond, Recover): **UNVERIFIED** on the fetched page | [NIST-CSF] |
| NGA | AI briefing (May 2025) | Only NGA item found; it concerns AI, see 2.2. NGA material on state IT governance generally: not found | [NGA-AI] |
| CISA | State and Local Cybersecurity Grant Program | Page blocked (403). Plan-element list **UNVERIFIED** | — |

### 2.2 AI in and by state government

| Tracker | Scope rule (government vs private) | Categories / dimensions | Source |
|---|---|---|---|
| NCSL AI Legislation Database (2025 onward, monthly, all introduced bills) | Multi-tag. "Government Use: Legislation focused on the use of AI by government agencies and law enforcement." "Private Sector Use: Legislation focused on the use of AI by private sector businesses and organizations." | 25 tags: Appropriations, Audit, Child Pornography, Criminal Use, Cybersecurity, Deepfake, Education/Training, Education Use, Effect on Labor/Employment, Elections, Energy, Government Use, Health Use, Housing, Impact Assessment, Judicial Use, Notification, Oversight/Governance, Personhood, Private Right of Action, Private Sector Use, Provenance, Responsible Use, Studies, Taxes | [NCSL-AIDB][NCSL-DBS] |
| NCSL 2025 session counts | Government 154 bills vs Private Sector Use 202 (multi-tag) | — | [NCSL-VT] |
| NCSL "AI in Government" brief (Nov 2024) and Vermont testimony (May 2025) | Government use only | Six levers: Study; Inventories ("over 10 states"); Impact assessments; Oversight (offices, councils); Guidelines ("at least 30 states"); Procurement | [NCSL-GOV][NCSL-VT] |
| CDT, public-sector AI legislation (Jan 2025; 43 bills in 2024 session) | Counts only bills solely about agency use; excludes sector-specific, ADMT and comprehensive bills | Task forces and studies (26); risk management practices (15); AI inventories (12); procurement requirements (7); pilot programs (3); chief AI officers (3). Sub-dimensions: inventory scope (high-risk only vs all), update cadence (annual / biennial / none), CAIO per agency vs single | [CDT-LEG] |
| CDT, executive orders (Jan 2025; 13 states + DC) | Government use only | AI definition used (federal NAII Act vs own; generative-only); harms acknowledged; pilots and their goals; governance body composition; procurement updates; inventories of high-risk uses; public disclosure; bias testing | [CDT-EO] |
| NGA (May 2025) | Separate headings for executive orders and legislative trends | 14 states with EOs named; EOs "nearly all" create a task force, may direct inventories, training, guidance; legislative themes list puts "State Government AI Use and Oversight" beside "Private-Sector Governance and Consumer Protection" | [NGA-AI] |
| FPF, State of State AI 2025 (210 bills, 42 states) | Report is "private-sector"; a "Government Use and Strategy" class is kept only for bills with "downstream or indirect effects on the private sector, such as ... standards ... for agencies procuring AI systems from private sector vendors" | Use/context-specific; technology-specific; liability and accountability; government use and strategy. About 30 percent of tracked bills were government use; most enacted bills were government use or investment | [FPF-2025] |
| IAPP US State AI Governance Legislation Tracker | "excluding government-only bills"; sectoral bills also omitted | Scope column (which AI systems) plus obligation themes split by developer vs deployer; "a check mark ... does not imply identical obligations" | [IAPP-AI] |
| BSA 2024 state summary (693 bills) | Section headings | High-risk uses; digital replicas; deepfakes; training-data transparency; directing government use (19 states, 40+ bills) | [BSA-2024] |
| MultiState | Broad "AI-related" definition; "dozens of AI subtopics", not enumerated publicly; filters by status, topic, chamber | Includes task forces, sandboxes, budget items, autonomous vehicles | [MULTISTATE] |
| Brennan Center | Only an elections-focused expert brief found (Aug 2024), not a general tracker | Deepfake-law dimensions: scope, enforcement entity, penalties, ban vs disclosure, time window before election | [BRENNAN] |
| Government Technology tracker (Aug 2024) | Internal government use only | Task forces/work groups; governance and inventories; legislatively mandated projects; dedicated AI officials and offices | [GOVTECH-AI] |
| Univ. of Florida PURC (Jan 2026) | Theme "Public-Sector Governance: Frameworks for AI procurement, use, and oversight by government entities" | 223 public-sector bills in 2025, of which "Government-use" 110, Education 46, Cross-sector 31, Health 19 | [UF-PURC] |
| Univ. of Denver CAID (Mar 2026) | Two tiers: "Core AI" (AI is the primary subject) vs "Adjacent AI" (AI as a tool inside another policy area) | Built on Plural/OpenStates bulk data, reconciled against NCSL | [DU-CAID] |
| ASTHO on LawAtlas | "Studying or governing the use of artificial intelligence by government agencies" coded separately from AI in employment decisions | Policy-surveillance dataset; questions not visible without login | [ASTHO-DS][ASTHO-PROTO] |
| NASCIO CIO Survey 2025 (practice, not law) | CIO-reported actions | Responsible-use guardrails 88%; inventory of uses 84%; advisory committees/task forces 82%; enterprise policies 76%; governance framework 65%; data governance 53%; procurement terms 41%; vendor disclosure 41%; transparency and accountability 41%; workforce impact 27% | [CIO-2025] |
| EPIC | Page blocked (403). Categories **UNVERIFIED** | — | — |

### 2.3 How comparative trackers make states comparable

| Model | Who defines the questions | Unit and coding | Currency | Source |
|---|---|---|---|---|
| **Policy surveillance** (Temple CPHLR, LawAtlas) | Research team from a five-state memo and a sample of laws; constructs narrowed to scope; reviewed by subject experts (ASTHO example) | Unit = jurisdiction x effective-date iteration. Questions "measure the law, rather than interpret it"; parent/child questions; closed response sets, extended by iterative coding. "Read, observe, and record". Every answer carries a citation; caution notes for oddities | Step 8 "tracking and updating": re-run protocol search terms and re-check every Master Sheet citation for jurisdictions that had a session; new iteration coded per amendment; law collected from an "unencumbered source" | [PHLR-M1][PHLR-M3][PHLR-M4][PHLR-M5][PHLR-M7][PHLR-M8][ASTHO-PROTO]; definition of the method also in [BURRIS] |
| Policy surveillance quality control | Supervisor | Redundant research: 100 percent of jurisdictions until divergence is below 5 percent, then 20 percent. Redundant and naive coding; daily supervisor review. Delphi standard: codebook and protocol "must accompany every completed legal dataset" | Published set: essential information, protocol, data file, codebook; dataset page shows date range and last-updated date | [PHLR-M6][PHLR-M5][PHLR-M7][DELPHI][LAWATLAS] |
| **NCSL 50-state statute table** | NCSL staff | One row per state: citation, applicability, prose summary. No coded variables | Ad hoc; example last updated 2020 | [NCSL-DSL] |
| **NCSL bill database** | NCSL staff tag set | Unit = bill; multi-tag; status; State Net feed | Weekly to annual per database; AI monthly | [NCSL-DBS][NCSL-AIDB] |
| **IAPP privacy chart** | IAPP Westin Research Center | Unit = bill or statute; scope = "comprehensive" bills only ("industry-specific, information-specific and narrowly scoped bills ... are not included"). Fixed provision columns, X = "right or obligation exists", with qualifiers (L = limited private right of action; S/P = opt-out scope; number = opt-in age). Columns in the 2024 chart: rights to access, correct, delete, opt out of certain processing, portability, opt out of sales, opt in for sensitive data, against automated decision-making, private right of action; obligations: opt-in default (age), notice/transparency, risk assessments, prohibition on discrimination, purpose/processing limitation | "Last updated" date; reader corrections by email | [IAPP-PRIV][IAPP-2024][IAPP-16] |
| **ULC** | The uniform act itself is the template; comparison = adopted or not | Site offers "Legislative Report by Act" and "by State" PDFs and per-act Enactment Kits. Enactment-map structure **UNVERIFIED** (not reachable in fetched pages) | — | [ULC-ACT][ULC-UETA] |
| **Correlates of State Policy** (MSU IPPSR) | Aggregator: variables taken from external sources | Unit = state-year; 3,000+ variables in 16 categories, about 1900 to 2019; each codebook entry has name, description, time frame, source | Versioned releases 1.0 to 2.6 with update logs | [CSPP] |
| **SPID** | Aggregated policy-adoption data, 728 policies coded by topic area (from search snippet; codebook not opened: **UNVERIFIED** detail) | Unit = state x policy adoption year | — | [SPID] |
| **NASCIO / CDG surveys** | Association staff | Unit = respondent state, self-reported; published as aggregates (NASCIO) or grades (CDG) | Annual / biennial | [CIO-2025][DSS-GA] |

Design consequence: policy surveillance is the only model here whose output is traceable to legal text with effective dates, so it is the model to copy for the comparison layer. The bill trackers are best used as seed lists and as a validation set (ASTHO validated against NCSL [ASTHO-PROTO]).

## 3. Proposed boundary for the pilot domain

**Scope statement (draft):** instruments that govern how a state government itself plans, buys, builds, secures, operates and oversees information technology, including AI and automated decision systems, where the obligated party is a state government entity or a vendor acting under a state contract.

**Inclusion test:** (a) the obligated party is a state entity or its contractor, and (b) the subject is IT, data or AI as a government function. This is the same line used by IAPP, FPF, CDT and NCSL (finding 1).

### 3.1 Clearly in

| Sub-area | Why | How trackers treat it |
|---|---|---|
| IT governance and organization (CIO office, authority, boards) | Core of NASCIO's CIO role wheel and reporting-model map | [NASCIO-KY] |
| IT planning, investment and project oversight | "Enterprise project and portfolio management"; "IT investment management" | [NASCIO-KY][DSS-GA] |
| IT acquisition and procurement | NASCIO survey section; cloud approval; AI contract terms | [CIO-2024][CIO-2025] |
| IT funding models | Chargeback / general fund / assessment asked directly | [CIO-2023] |
| Cybersecurity of state systems | NCSL state-government security table; Deloitte-NASCIO statute provisions | [NCSL-DSL][DELOITTE-2024] |
| Data governance and privacy of government-held data | NASCIO section; CDG category | [CIO-2025][DSS-GA] |
| Government use of AI | Distinct category in NCSL, CDT, FPF, BSA, UF, ASTHO | section 2.2 |
| Digital services, accessibility, identity | Top Ten items 5 to 7; survey sections | [TOP10-2026][CIO-2024] |
| Cloud, enterprise architecture, resilience/DR | Survey sections; GovRAMP | [CIO-2024][CIO-2025][GOVRAMP] |

### 3.2 Clearly out

| Sub-area | Reasoning | How trackers draw the line |
|---|---|---|
| Private-sector AI regulation (developer/deployer duties, chatbots, frontier models, algorithmic pricing) | Obligated party is a business | FPF and IAPP make it their whole scope and exclude government-only bills [FPF-2025][IAPP-AI]; NCSL uses a separate tag [NCSL-AIDB] |
| Comprehensive consumer privacy law | Obligated party is a business | IAPP separate tracker [IAPP-PRIV]; NCSL separate database [NCSL-DBS] |
| Deepfakes, AI crimes, child sexual abuse material, digital replicas | Criminal or civil conduct rules | NCSL tracks deepfakes separately [NCSL-AI25]; BSA separate headings [BSA-2024] |
| Broadband deployment and subsidy, 911, telecom | Infrastructure for the public | NCSL separate databases [NCSL-DBS] |
| Autonomous vehicles; social media and children; data-center siting and energy | Other regulated parties | NCSL separate databases and tags [NCSL-DBS][NCSL-AIDB] |
| AI workforce training programs, AI tax incentives, AI in K-12 curriculum | Economic or education policy | FPF excludes; NCSL separate tags (Education/Training, Taxes, Education Use) [FPF-2025][NCSL-AIDB] |

### 3.3 Contested (decision needed)

| Sub-area | Case for in | Case for out | Tracker practice | Recommendation |
|---|---|---|---|---|
| Comprehensive AI acts that also bind government as deployer | The state may be a covered deployer | Text is mostly private-sector duties | CDT excludes them and warns its count is therefore low; notes vendor duties still reach government [CDT-LEG] | In only as a pointer: record applicability to government, do not ingest as core |
| Vendor obligations inside government-use laws | Procurement is how government-use rules bite | — | FPF keeps exactly these bills [FPF-2025] | In |
| Law-enforcement technology (facial recognition, ALPR, predictive policing) | NCSL's Government Use definition includes "law enforcement" [NCSL-AIDB] | Policing policy has its own database and literature [NCSL-DBS]; NCSL tracks facial recognition separately [NCSL-AI25] | Split | Out for pilot except where a general agency-AI rule names law enforcement |
| Public records law | Cyber-related exemptions and AI inventory disclosure are IT governance; NCSL notes records exemptions for cybersecurity information [NCSL-CYBER21] | General records access is a separate domain | No tracker found | Only IT-specific provisions in |
| Breach notification and data security statutes | NCSL has a state-government table [NCSL-DSL] | Private-sector versions are a different table [NCSL-DSL] | Split by applicability | Government-applicable provisions in |
| Election systems | State-run IT; Deloitte notes election security in CISO agendas [DELOITTE-2024] | NCSL treats elections as its own database and AI tag [NCSL-DBS][NCSL-AIDB]; Brennan treats it standalone [BRENNAN] | Separate | Out (later pack) |
| K-12 edtech and student data privacy | Public-sector IT | Districts are local; NCSL "Education Use" is its own tag [NCSL-AIDB]; UF splits Education from Government-use [UF-PURC] | Separate | Out |
| Local government and higher education | "Whole-of-state" cybersecurity; state services to locals [TOP10-2026][CIO-2025][DELOITTE-2024] | Local ordinances multiply the corpus | NASCIO asks about state-to-local services only | State instruments that reach locals in; local instruments out |
| Legislative and judicial branch IT/AI | Same functions | Separate authority; NCSL has "Judicial Use" tag and a separate legislative survey [NCSL-AIDB][NCSL-VT] | Separate | Out for pilot; record branch applicability as a dimension |
| State-operated broadband networks | CDG category "enterprise computing and broadband expansion" [DSS-GA] | Mostly public-facing subsidy policy | Mixed | Out, except state network as enterprise infrastructure |
| IT workforce rules | NASCIO survey section [CIO-2024]; CDG category [DSS-GA] | Civil-service law is its own domain | Survey only | Out, except IT-specific classification or AI-training mandates for state staff |
| Study bills and task forces | Largest category in CDT (26 of 43) and "nearly all" EOs [CDT-LEG][NGA-AI] | Low durable legal content; FPF excludes task forces [FPF-2025] | Mixed | In as a governance-body record, low priority for full text |
| Federal instruments states must comply with (IRS 1075, CJIS, MARS-E, SSA TSSR, DOJ accessibility rule) | Drive state rules [GAO-20-123][CIO-2025] | Not state law | — | Reference layer, not corpus |

## 4. Draft taxonomy with comparison dimensions

Dimensions listed are ones a named source actually compares. "Gap" marks dimensions the brief asks about that no source was found to code across states.

| # | Sub-area | Comparison dimensions in use | Sources |
|---|---|---|---|
| A | **IT governance and organization** | CIO reporting line (governor / agency head / board); organizing model (five steps, decentralized to unified); role of CIO organization (infrastructure provider, strategy voice, compliance, broker); consolidation of infrastructure, services, personnel, project oversight; legal basis of authority (statute / rule / EO / directive: coded for CISO only). **Gap:** CIO appointment and statutory powers by state | [NASCIO-KY][CIO-2024][DELOITTE-2024] |
| B | **Planning, investment, project oversight** | Centralized project management and oversight under CIO; enterprise architecture maturity; IT investment management; metrics for projects. **Gap:** dollar or risk thresholds triggering oversight (individual statutes exist, e.g. NC, VA, ND, but no cross-state table: **UNVERIFIED** from search snippets) | [CIO-2024][DSS-GA][NASCIO-SEARCH] |
| C | **Acquisition and procurement** | Definition of an "IT procurement"; master contracts (96%), cooperative agreements (85%), pre-approved vendor pools (75%); CIO approves all agency cloud acquisitions (72%); CIO owns vendor cloud contracts (74%); cybersecurity review before acquisition (86%); accessibility in procurement; AI clauses in contracts; GovRAMP required or accepted | [CIO-2024][CIO-2025][TOP10-2026][GOVRAMP] |
| D | **Funding model** | Chargeback (90% at least partly) / general fund (63%) / agency assessment (20%); modernization or innovation fund; supplemental cyber funding | [CIO-2023][NASCIO-KY][CIO-2025] |
| E | **Cybersecurity of state systems** | CISO role and authority in statute; legal mechanism of authority; entities covered; required security program or standards; employee training; incident response and reporting; periodic risk assessment or audit; threat information sharing; continuity of government; whole-of-state services to locals; alignment to federal frameworks | [NCSL-DSL][DELOITTE-2024][NCSL-CYBER21][GAO-20-123] |
| F | **Data governance and privacy (government-held data)** | Data governance maturity; CDO role and reporting; data-sharing; how analytics services are delivered; secure disposal; entities covered | [CIO-2025][NCSL-DSL] |
| G | **Government use of AI** | Definition of AI (federal-derived vs own; generative-only); scope (all AI vs high-risk); inventory (required? scope, public?, update cadence); impact assessment (required? pre-deployment? who reviews); governance body (task force / council / office / CAIO; composition; advisory vs binding); enterprise policy or guidelines and their instrument type; procurement rules and vendor disclosure; pilots and sandboxes; disclosure to the public; human review / limits on AI-only adverse decisions; prohibited uses; training of staff; audit and reporting to legislature; enforcement | [NCSL-GOV][NCSL-VT][CDT-LEG][CDT-EO][NGA-AI][CIO-2025][NCSL-AIDB] |
| H | **Digital services, accessibility, identity** | Accessibility coordinator; accessibility funding; method of ensuring vendor compliance; status against DOJ rule; enterprise IAM status; citizen digital identity; mobile driver's license status | [CIO-2025][CIO-2024][TOP10-2026] |
| I | **Cloud, architecture, resilience** | Cloud strategy ("cloud first/smart"); cloud governance components; DR/BC model (enterprise 17% / federated 72% / decentralized 9%) | [CIO-2025][CIO-2024] |
| X | **Cross-cutting record fields** (every sub-area) | Instrument type; legal basis; entities covered and exempted (branch, higher ed, locals); effective date and iteration; responsible official; reporting duty; funding attached (established-and-funded vs not) | [PHLR-M3][DELOITTE-2024][NCSL-DSL] |

## 5. Example analyst questions (all drawn from what sources compare)

1. To whom does the state CIO report: governor, agency head or board? [NASCIO-KY]
2. Where does each state sit between decentralized and unified IT, and what has been consolidated (infrastructure, services, staff, project oversight)? [NASCIO-KY][CIO-2024]
3. Is the state CISO's authority set by statute, rule, executive order, CIO directive or interagency agreement? [DELOITTE-2024]
4. Which states have a statute establishing the enterprise CISO role, and is it funded? [DELOITTE-2024]
5. Which government entities do state data-security statutes cover (executive agencies only, locals, contractors)? [NCSL-DSL]
6. Which states require agencies to run security training, periodic risk assessments or incident response plans? [NCSL-DSL][NCSL-CYBER21]
7. Must the CIO approve agency cloud acquisitions, and is a pre-acquisition security review required? [CIO-2025]
8. How is the central IT organization funded: chargeback, general fund, assessment or hybrid? [CIO-2023]
9. How does each state define an "information technology procurement"? [CIO-2024]
10. Which states require an inventory of agency AI systems; all uses or high-risk only; how often updated; published? [NCSL-GOV][CDT-LEG]
11. Which states require impact assessments before agencies deploy AI, and who reviews them? [NCSL-GOV][NCSL-AIDB]
12. How does each state's instrument define "artificial intelligence", and does it borrow the federal definition? [CDT-EO]
13. What body governs state AI use (task force, council, office, chief AI officer), who sits on it, and is it advisory or binding? [CDT-LEG][CDT-EO][NCSL-GOV]
14. Is the state's AI policy set by statute, executive order, rule or CIO guideline? [NCSL-VT][NGA-AI]
15. Which states impose AI-specific procurement terms or vendor disclosure duties? [CIO-2025][CDT-LEG][FPF-2025]
16. Which states restrict AI-only adverse decisions (for example benefit cuts or fraud findings) or require public disclosure of AI use? [CDT-LEG][CDT-EO]
17. Which states have a technology accessibility coordinator and how do they verify vendor compliance? [CIO-2025]
18. Is disaster recovery centralized, federated or left to agencies? [CIO-2024]
19. What cybersecurity or IT services does the state provide to local governments (whole-of-state)? [CIO-2025][DELOITTE-2024]
20. Which states require or accept GovRAMP authorization for cloud purchases? [GOVRAMP]

Note: for questions 1 to 9 and 17 to 19 the sources publish only aggregates or maps. State-by-state legal answers do not exist in the open; producing them is the project's added value.

## 6. Generic versus domain-specific: the shape of a "domain pack"

| Pack element | Generic (pipeline) | Domain-specific (pack content) | Basis |
|---|---|---|---|
| Scope statement and inclusion test | Schema: statement, obligated-party test, in/out/contested list with reasons | The text itself | Policy-surveillance "defining your scope"; IAPP and FPF scope statements [PHLR-M1][IAPP-PRIV][FPF-2025] |
| Instrument types | Enum and per-type fetchers: statute, rule, executive order, session law, bill | Which extra types matter: here statewide IT policies and standards, AI inventories, strategic plans, contract terms | [NCSL-VT][DELOITTE-2024] |
| Taxonomy | Tree of sub-areas, multi-label tagging | Sub-areas A to I | section 4 |
| Constructs and question set | Question types (parent/child, closed response sets, citation per answer, caution notes); observation-not-interpretation rule | The questions and response sets | [PHLR-M3][PHLR-M5] |
| Seed lists | Format: per-state citations ("Master Sheet"), responsible bodies, search terms | Here: CIO statutes, NCSL tables and tags, EO lists, CDT bill lists | [PHLR-M4][NCSL-DSL][CDT-EO] |
| Search protocol | Recorded search terms and sources per jurisdiction | Terms (for example ASTHO's proximity strings) | [ASTHO-PROTO][PHLR-M4] |
| External trackers for validation | Reconciliation step against a named tracker | Which tracker (NCSL AI database here) | [ASTHO-PROTO][DU-CAID] |
| Reference frameworks | Slot for non-state instruments that states map to | NIST CSF, 800-53/GovRAMP, IRS 1075, CJIS, MARS-E, DOJ accessibility rule | [GAO-20-123][GOVRAMP] |
| Currency and versioning | Effective-dated iterations; re-check after each session; published protocol and codebook | Session calendar is generic; EO and policy revision cadence is domain-specific | [PHLR-M8][DELPHI] |
| Quality control | Redundant collection and coding thresholds (5 percent divergence, then 20 percent sampling) | None | [PHLR-M6] |
| Entity registry | Generic 50-state registry of legislatures, codes, registers | Domain actors: CIO office, CISO, CDO, AI office, procurement office | [NASCIO-KY] |

Count: the structure of all eleven elements is generic. The content is domain-specific for nine, partly for one (currency: revision cadence of executive orders and policies) and not at all for one (quality control).

**Same shape for career and technical education (not researched; all UNVERIFIED, from general knowledge):**

| Element | CTE sketch |
|---|---|
| Scope test | Obligated party is a state education or workforce agency, district or postsecondary system delivering CTE |
| Instrument types | Statute, rule, state board policy, state Perkins plan, funding formula, graduation requirements |
| Taxonomy | Governance; funding; program approval and standards; credentials and dual credit; teacher licensure; work-based learning; accountability |
| Seed lists | State CTE director offices; state Perkins plans; education-policy 50-state comparisons |
| Reference frameworks | Federal Perkins V |
| Contested edges | Apprenticeship (labor law), adult workforce programs, higher-education governance |

The parallel holds on the point that matters: in both domains much of the comparable content sits in sub-statutory instruments (IT policies; state plans and board policy).

## 7. Open scoping decisions

1. Statutes and rules only, or also executive orders and CIO-issued policies and standards? Evidence says the latter carry most AI and security content [NCSL-VT][DELOITTE-2024].
2. Law in force only (policy-surveillance model) or pending bills too (NCSL model)?
3. Executive branch only, or record legislative, judicial, higher-education and local applicability?
4. Law-enforcement technology: in under NCSL's definition, or deferred?
5. Comprehensive AI acts: pointer-only or full ingest?
6. Whether to code questions (a dataset) at all in the pilot, or ship full text plus taxonomy tags and let the agent compare.
7. Whether survey-derived dimensions with no legal text behind them (for example maturity, funding mix) belong in the pack.

## Access problems and gaps

| Item | Status |
|---|---|
| NASCIO PDFs | Direct download returned 403; text obtained through the fetch tool's saved copy and extracted locally |
| EPIC state AI laws page | 403; not used |
| SSRN "Technical Guide for Policy Surveillance" | 403; method taken from Temple training modules and the Delphi paper instead |
| CISA SLCGP page | 403; not used |
| LawAtlas methods page, PHLR self-guided training index | 404 / redirect; individual module PDFs were reachable |
| NCSL AI database original URL | 404; live under /financial-services/ path |
| ULC enactment maps | Not reachable in fetched pages; structure UNVERIFIED |
| MultiState subtopic list | Not published on the fetched page |
| Brennan Center general AI tracker | Not found; only an elections brief |
| SPID codebook | Not opened |
| NASCIO comparison of CIO statutory authority, procurement authority, project thresholds | Not found in one search; treat absence as UNVERIFIED |
| NGA on state IT governance (non-AI) | Not found |
| IAPP current chart columns | Taken from the 2024 PDF copy; the current chart may differ |

## Sources

| Key | URL |
|---|---|
| TOP10-2026 | https://www.nascio.org/wp-content/uploads/2025/12/NASCIO-2026-State-Top-10-Priorities_a11y.pdf |
| TOP10-PAGE | https://www.nascio.org/resource-center/resources/state-cio-top-ten-policy-and-technology-priorities-for-2026/ |
| CIO-2025 | https://www.nascio.org/wp-content/uploads/2025/09/The-2025-State-CIO-Survey_a11y.pdf |
| CIO-2024 | https://nascio.org/wp-content/uploads/2024/09/NASCIO_2024-State-CIO-Survey_a11y-1.pdf |
| CIO-2023 | https://www.nascio.org/wp-content/uploads/2023/09/NASCIO_2023-State-CIO-Survey-A.pdf |
| NASCIO-KY | https://apps.legislature.ky.gov/CommitteeDocuments/382/28334/NASCIO_KY%20IT%20Oversight%20Board_Dec2023.pdf |
| NASCIO-SEARCH | Search snippets only: https://ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_143B/GS_143B-1340.html ; https://law.lis.virginia.gov/vacode/2.2-2016.1 ; https://www.ndit.nd.gov/it-services/find-or-improve-technology-solution/project-management/project-management-oversight |
| DELOITTE-2024 | https://www.deloitte.com/content/dam/insights/pdfs/DI-2024-Deloitte-NASCIO-Cybersecurity-Study.pdf |
| NCSL-AIDB | https://www.ncsl.org/financial-services/artificial-intelligence-legislation-database |
| NCSL-AI25 | https://www.ncsl.org/technology-and-communication/artificial-intelligence-2025-legislation |
| NCSL-GOV | https://www.ncsl.org/technology-and-communication/artificial-intelligence-in-government-the-federal-and-state-landscape |
| NCSL-VT | https://legislature.vermont.gov/Documents/2026/Workgroups/House%20Energy%20and%20Digital/Artificial%20Intelligence/W~Chelsea%20Canada~AI%20Regulation%20and%20AI%20Government%20Use~5-15-2025.pdf |
| NCSL-CYBER25 | https://www.ncsl.org/technology-and-communication/cybersecurity-2025-legislation |
| NCSL-CYBER21 | https://www.ncsl.org/technology-and-communication/cybersecurity-legislation-2021 |
| NCSL-DSL | https://www.ncsl.org/technology-and-communication/data-security-laws-state-government |
| NCSL-DBS | https://www.ncsl.org/technology-and-communication/ncsl-50-state-searchable-bill-tracking-databases |
| DSS-GA | https://gta.georgia.gov/node/19681 |
| DSS-2026 | https://www.govtech.com/cdg/digital-states/center-for-digital-government-recognizes-top-performing-states-in-2026-digital-states-survey |
| GAO-20-123 | https://www.gao.gov/products/gao-20-123 |
| GOVRAMP | https://govramp.org/participating-governments/ |
| NIST-CSF | https://www.nist.gov/cyberframework |
| NGA-AI | https://www.nga.org/updates/legal-and-regulatory-considerations-for-states-related-to-artificial-intelligence/ |
| CDT-LEG | https://cdt.org/insights/regulating-public-sector-ai-emerging-trends-in-state-legislation/ |
| CDT-EO | https://cdt.org/insights/state-government-use-of-ai-the-opportunities-of-executive-action-in-2025/ |
| FPF-2025 | https://fpf.org/wp-content/uploads/2025/10/The-State-of-State-AI-2025.pdf |
| IAPP-AI | https://www.iapp.org/resources/article/us-state-ai-governance-legislation-tracker |
| IAPP-PRIV | https://iapp.org/resources/article/us-state-privacy-legislation-tracker/ |
| IAPP-2024 | https://wyoleg.gov/InterimCommittee/2024/S19-2024052017-10USStatePrivacyLegislationTracker2024.pdf |
| IAPP-16 | https://iapp.org/news/a/us-state-comprehensive-privacy-law-comparison |
| BSA-2024 | https://techpost.bsa.org/2024/10/22/2024-state-summary-on-ai/ |
| MULTISTATE | https://www.multistate.ai/artificial-intelligence-ai-legislation |
| BRENNAN | https://www.brennancenter.org/our-work/research-reports/states-take-lead-regulating-ai-elections-within-limits |
| GOVTECH-AI | https://govtech.com/biz/data/is-your-government-ai-ready-an-interactive-tracker-of-ai-action |
| UF-PURC | https://bear.warrington.ufl.edu/centers/purc/docs/papers/2602_Mapping_State_AI_Regulation_2025.pdf |
| DU-CAID | https://du-caid.github.io/reports/ai-tracker-launch.html |
| ASTHO-DS | https://lawatlas.org/datasets/public-health-infrastructure-legislative-tracking-20241015171327 |
| ASTHO-PROTO | https://www.astho.org/4900ce/globalassets/pdf/public-health-infrastructure-legislative-tracking-protocol-ai.pdf |
| LAWATLAS | https://lawatlas.org/ |
| PHLR-M1 | https://phlr.temple.edu/sites/phlr/files/documents/PS%20Guided%20Training/Module%201.2.pdf |
| PHLR-M3 | https://phlr.temple.edu/sites/phlr/files/documents/PS%20Guided%20Training/mod%203/Module%203%20(1).pdf |
| PHLR-M4 | https://phlr.temple.edu/sites/phlr/files/documents/PS%20Guided%20Training/mod%204/Module%204%20(2).pdf |
| PHLR-M5 | https://phlr.temple.edu/sites/phlr/files/documents/PS%20Guided%20Training/mod%205/Module%205%20(1).pdf |
| PHLR-M6 | https://phlr.temple.edu/sites/phlr/files/documents/PS%20Guided%20Training/mod%206/Module%206.2%20(1).pdf |
| PHLR-M7 | https://phlr.temple.edu/sites/phlr/files/documents/PS%20Guided%20Training/mod%207/Module%207.pdf |
| PHLR-M8 | https://phlr.temple.edu/sites/phlr/files/documents/PS%20Guided%20Training/mod%208/Module%208.pdf |
| DELPHI | https://phlr.org/sites/default/files/uploaded_images/Creating%20Legal%20Data%20for%20Public%20Health%20Monitoring%20and%20Evaluation-%20Delphi%20Standards%20for%20Policy%20Surveillance.pdf |
| BURRIS | https://am.aals.org/app/uploads/sites/4/2025/01/burris_et_al_policy_surveillance_jhppl.pdf |
| CSPP | https://ippsr.msu.edu/public-policy/correlates-state-policy |
| SPID | https://par.nsf.gov/biblio/10121487-spid-new-database-inferring-public-policy-innovativeness-diffusion-networks |
| ULC-ACT | https://www.uniformlaws.org/legislation/activity |
| ULC-UETA | https://www.uniformlaws.org/committees/community-home?CommunityKey=2c04b76c-2b7d-4399-977e-d5876ba7e034 |
