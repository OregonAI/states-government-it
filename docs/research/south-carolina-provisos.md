# South Carolina: five approved provisos held back by a shared file

Status 2026-11-13. The owner's decision of 2026-11-13 approves a provision of law that is not itself about IT, as a
section slice, when its own focus is the governance of state IT. Nine provisos of Part IB of the FY 2026-27 General
Appropriations Act (H. 5126, as ratified August 11, 2026) pass that test and were read in bytes fetched through the
toolkit Fetcher on 2026-11-13: 93.9, 117.96, 117.106, 117.194 and 117.120 (entries prepared below), and on review
four more, 117.95, 117.101, 117.117 and 117.209 (entries not yet prepared; each is a slice of the same file, cut as
`slice: {section_start: "117.N", section_end_before: "117.(N+1)"}` after checking the next proviso's number in the PDF).
The four, with their headings and the words that make them IT governance: 117.95 "(GP: Technology and Remediation)"
(funds for the Division of Information Security "to develop and implement a statewide information security program");
117.101 "(GP: Information Technology and Information Security Plans)" ("all state agencies must submit an information
technology plan and an information security plan to the Department of Administration"); 117.117 "(GP: SCEIS Data Entry
Compliance)" (the Department "shall develop and issue written SCEIS data entry standards and guidelines for agency
compliance"); 117.209 "(GP: Statewide Data Initiative)" (agencies must follow the Department's standards "regarding
data creation, security, and privacy" and keep an enterprise data inventory). Declined: 117.73 (one agency's health
information exchange) and 117.27 (K-12 school technology, out of scope under domain.yml). Shared change: add all nine
ids to `FORMS["south-carolina"].uncitable` (or a form for provisos). The Governor's veto message (August 17, 2026,
an image-only PDF, read by OCR) lists fourteen vetoes and none is one of these. `src/states/south-carolina.py` cuts a
proviso from the Part IB PDF (`slice: {section_start: "117.106", section_end_before: "117.107"}`, tests in
`tests/south-carolina/`), dropping the PDF's running page header.

They are not in `_meta/sources/south-carolina.yml` because `tests/test_authority_refs.py::
test_every_held_statute_rule_and_order_in_every_seed_parses_to_a_holding` fails the gate for a held statute whose citation
`src/authority_forms.py` cannot parse, and that file has no form for an Appropriations Act proviso. The fix is a shared
change: add the five ids to `FORMS["south-carolina"].uncitable` (or a form for provisos). Then paste the entries below into
the seed file under `sources:` (after `sc-code-30-ch-2`), copy the Part IB PDF from the Fetcher to
`_meta/snapshots/<id>.pdf` for each id (or let `python3 src/ingest.py --state south-carolina` fetch it), ingest and run
`scripts/regen.sh`. The provisos are temporary law for FY 2026-27 and need re-seeding from each year's Act.

```yaml
- id: "sc-act-2026-27-proviso-93-9"
  sha256: "6551b0792796a503a77c07e65904846beeb4967d3870a075fcbd5cff96d9847f"
  url: "https://www.scstatehouse.gov/sess126_2025-2026/appropriations2026/tap1b.pdf"
  format: "pdf"
  citation: "FY 2026-27 General Appropriations Act (H. 5126), Part IB, Proviso 93.9"
  title: "General Appropriations Act FY 2026-27, Part IB, Proviso 93.9. DOA: Cyber Security"
  doc_type: "statute"
  jurisdiction: "south-carolina"
  issuing_body: "South Carolina General Assembly (Legislative Council) (Appropriations Act, H. 5126)"
  tags: [cybersecurity, governance, oversight]
  recheck: "monthly"
  slice: {section_start: "93.9", section_end_before: "93.10"}
  why_relevant: "OWNER DECISION 2026-11-13: a provision in law that is not itself about IT is in scope, as a section slice, when its own focus is the governance of state government IT. The slice is one proviso of the Appropriations Act, which is temporary budget law and not IT law as a whole. Proviso 93.9: 'All state agencies must adopt and implement cyber security policies, guidelines and standards developed by the Department of Administration'; the Department may audit agencies for compliance (not higher education, technical colleges, political subdivisions or quasi-governmental bodies, who show on request that theirs meet or exceed the Department's), must be informed of all agency cyber security breaches and may oversee incident responses, and all agencies must cooperate with its requests for information; the Judicial and Legislative Branches are exempt. The Statewide Information Security Program Policy cites a proviso numbered 93.9 as its authority. Temporary law for fiscal year 2026-27 (the proviso says 'current fiscal year'): H. 5126, ratified by the General Assembly on August 11, 2026, with the Governor's line-item vetoes of August 17, 2026; the Governor's veto message (an image-only PDF, read by OCR for this check) lists fourteen vetoes and none is this proviso. "

- id: "sc-act-2026-27-proviso-117-96"
  sha256: "6551b0792796a503a77c07e65904846beeb4967d3870a075fcbd5cff96d9847f"
  url: "https://www.scstatehouse.gov/sess126_2025-2026/appropriations2026/tap1b.pdf"
  format: "pdf"
  citation: "FY 2026-27 General Appropriations Act (H. 5126), Part IB, Proviso 117.96"
  title: "General Appropriations Act FY 2026-27, Part IB, Proviso 117.96. GP: Data Breach Notification"
  doc_type: "statute"
  jurisdiction: "south-carolina"
  issuing_body: "South Carolina General Assembly (Legislative Council) (Appropriations Act, H. 5126)"
  tags: [data, cybersecurity]
  recheck: "monthly"
  slice: {section_start: "117.96", section_end_before: "117.97"}
  why_relevant: "OWNER DECISION 2026-11-13: a provision in law that is not itself about IT is in scope, as a section slice, when its own focus is the governance of state government IT. The slice is one proviso of the Appropriations Act, which is temporary budget law and not IT law as a whole. Proviso 117.96: 'An agency of this State owning or licensing computerized data or other data that includes personal identifying information shall disclose any breach of the security of the system' to the residents whose information was acquired, notify the owner or licensee of data it maintains but does not own, within the time limits stated, and defines 'agency' and 'breach of the security of the system'. It binds state agencies' systems. The Statewide Information Security Program Policy cites a proviso numbered 117.96 as one of its authorities. Temporary law for fiscal year 2026-27 (the proviso says 'current fiscal year'): H. 5126, ratified by the General Assembly on August 11, 2026, with the Governor's line-item vetoes of August 17, 2026; the Governor's veto message (an image-only PDF, read by OCR for this check) lists fourteen vetoes and none is this proviso. "

- id: "sc-act-2026-27-proviso-117-106"
  sha256: "6551b0792796a503a77c07e65904846beeb4967d3870a075fcbd5cff96d9847f"
  url: "https://www.scstatehouse.gov/sess126_2025-2026/appropriations2026/tap1b.pdf"
  format: "pdf"
  citation: "FY 2026-27 General Appropriations Act (H. 5126), Part IB, Proviso 117.106"
  title: "General Appropriations Act FY 2026-27, Part IB, Proviso 117.106. GP: Statewide Strategic Information Technology Plan Implementation"
  doc_type: "statute"
  jurisdiction: "south-carolina"
  issuing_body: "South Carolina General Assembly (Legislative Council) (Appropriations Act, H. 5126)"
  tags: [governance, oversight, funding]
  recheck: "monthly"
  slice: {section_start: "117.106", section_end_before: "117.107"}
  why_relevant: "OWNER DECISION 2026-11-13: a provision in law that is not itself about IT is in scope, as a section slice, when its own focus is the governance of state government IT. The slice is one proviso of the Appropriations Act, which is temporary budget law and not IT law as a whole. Proviso 117.106 directs state agencies to use the Department of Administration's shared IT services, to comply with the rules, standards, plans, policies and directives of the Division of Technology Operations on IT governance, standards and enterprise architecture, to submit all IT budget requests to the Executive Budget Office and the Division, to create an IT plan with the Division's approval for purchases over $50,000, to develop a three-year IT strategic plan approved by the Chief Information Officer, and to enter IT costs into SCEIS; the Legislative and Judicial Branches, higher education, technical colleges, political subdivisions and quasi-governmental bodies are exempt. The Department's IT Planning page names this proviso. Temporary law for fiscal year 2026-27 (the proviso says 'current fiscal year'): H. 5126, ratified by the General Assembly on August 11, 2026, with the Governor's line-item vetoes of August 17, 2026; the Governor's veto message (an image-only PDF, read by OCR for this check) lists fourteen vetoes and none is this proviso. "

- id: "sc-act-2026-27-proviso-117-194"
  sha256: "6551b0792796a503a77c07e65904846beeb4967d3870a075fcbd5cff96d9847f"
  url: "https://www.scstatehouse.gov/sess126_2025-2026/appropriations2026/tap1b.pdf"
  format: "pdf"
  citation: "FY 2026-27 General Appropriations Act (H. 5126), Part IB, Proviso 117.194"
  title: "General Appropriations Act FY 2026-27, Part IB, Proviso 117.194. GP: AI Appropriations"
  doc_type: "statute"
  jurisdiction: "south-carolina"
  issuing_body: "South Carolina General Assembly (Legislative Council) (Appropriations Act, H. 5126)"
  tags: [ai, governance, funding]
  recheck: "monthly"
  slice: {section_start: "117.194", section_end_before: "117.195"}
  why_relevant: "OWNER DECISION 2026-11-13: a provision in law that is not itself about IT is in scope, as a section slice, when its own focus is the governance of state government IT. The slice is one proviso of the Appropriations Act, which is temporary budget law and not IT law as a whole. Proviso 117.194: 'Any agency or institution that is appropriated or authorized funds for artificial intelligence shall coordinate their efforts and budget requests with the Department of Administration's AI Center of Excellence (AI COE)'; institutions of higher learning are exempt for instructional and research purchases if they report monthly to the AI COE, and are not exempt from procurement policies. The AI Center of Excellence page names this proviso, and the Governor's veto message of August 17, 2026 (Veto 11) says that 'All state agencies procuring and implementing artificial intelligence (AI) solutions must be reviewed and coordinated through the AI Center of Excellence.' Temporary law for fiscal year 2026-27 (the proviso says 'current fiscal year'): H. 5126, ratified by the General Assembly on August 11, 2026, with the Governor's line-item vetoes of August 17, 2026; the Governor's veto message (an image-only PDF, read by OCR for this check) lists fourteen vetoes and none is this proviso. "

- id: "sc-act-2026-27-proviso-117-120"
  sha256: "6551b0792796a503a77c07e65904846beeb4967d3870a075fcbd5cff96d9847f"
  url: "https://www.scstatehouse.gov/sess126_2025-2026/appropriations2026/tap1b.pdf"
  format: "pdf"
  citation: "FY 2026-27 General Appropriations Act (H. 5126), Part IB, Proviso 117.120"
  title: "General Appropriations Act FY 2026-27, Part IB, Proviso 117.120. GP: Mobile Device Protection Plan"
  doc_type: "statute"
  jurisdiction: "south-carolina"
  issuing_body: "South Carolina General Assembly (Legislative Council) (Appropriations Act, H. 5126)"
  tags: [procurement, governance]
  recheck: "monthly"
  slice: {section_start: "117.120", section_end_before: "117.121"}
  why_relevant: "OWNER DECISION 2026-11-13: a provision in law that is not itself about IT is in scope, as a section slice, when its own focus is the governance of state government IT. The slice is one proviso of the Appropriations Act, which is temporary budget law and not IT law as a whole. Proviso 117.120 directs the Department of Administration to implement updated policies for protecting state-owned mobile devices (cellular phones, tablets and laptops), considering consolidation of agencies' protection plans, and the State Fiscal Accountability Authority to establish a statewide contract for protecting all state-owned mobile devices, competitively awarded under the Procurement Code. It is the current Act's form of the Mobile Device Protection Plan proviso, which SWM-300 (held) cites as Proviso 117.148 of the FY 2018-19 Act; the numbering has changed and the text is not the same. Temporary law for fiscal year 2026-27 (the proviso says 'current fiscal year'): H. 5126, ratified by the General Assembly on August 11, 2026, with the Governor's line-item vetoes of August 17, 2026; the Governor's veto message (an image-only PDF, read by OCR for this check) lists fourteen vetoes and none is this proviso. "
```
