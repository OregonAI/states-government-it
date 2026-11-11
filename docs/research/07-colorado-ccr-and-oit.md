# Colorado: the CCR answers curl, OIT's library is a portal we cannot read (2026-11-11)

Everything below was measured on 2026-11-11 with the toolkit `Fetcher` (shipped User-Agent, rate limit) with
`curl_on_challenge=True` (toolkit branch through PYTHONPATH; CI and the gate run at the v1.36.4 pin, offline),
unless marked UNVERIFIED. It corrects the Colorado notes in `02` and in the seed list's earlier comments.

## Administrative rules

- `www.sos.state.co.us/CCR` answers the Fetcher once it uses curl (200 for the browse lists, rule pages and PDFs).
- Department 1501 is the Office of the Governor; agency 168 is the Governor's Office of Information Technology. Its list
  names 8 CCR 1501-4 to 1501-12 (no 1501-10). In force: 1501-5 (eff. 06/30/2026), -7 (01/30/2010), -9 (03/20/2017),
  -11 (06/30/2025), -12 (01/14/2025). Not in force: -4 (repealed 04/14/2014), -6 (repealed 04/14/2026; one of the five
  leads), -8 (repealed 06/30/2024). The Secretary of State keeps a repealed rule's number with a one-page repeal notice
  as its "current version", so the ingester refuses a PDF whose cover says "repealed eff.".
- The PDF is the official version of the rule (the page says it governs); its cover's logotype comes out of
  pdftotext as letter fragments, kept as extracted and said in the conversion notes. `effective_date` is the last
  `eff.` line of the History.

## OIT policies

- `oit.colorado.gov` answers HTTP 403 to the Fetcher with curl too. Its index page was read only through the Wayback
  Machine copy 20260822055824 (GenAI page: 20260214051202) to find links; no text comes from it.
- Three files are Google Drive PDFs OIT links from that page, fetched in Drive's download form: the OIT Authority &
  Governance Operations Memorandum (revised Feb. 2026), the eSignature Recommended Policy Guidelines (published January 2020;
  the PDF itself names OIT once, as approver of further solutions, so its attribution rests on OIT's page) and the Vendor
  Selection Standard (OIT-FinSvc-100). They are documents.
- Everything else in force on the index (4 CISPs, 7 technical-standard families, the Statewide GenAI Policy, Delegation of
  Authority, billing dispute documents: 54) is an article on `servicehub.colorado.gov`, a ServiceNow portal. The article
  address answers 200 with the same ~513 KB script-rendered shell for every article, the classic view redirects to the state
  sign-on, and the article body is loaded by a call that is not a plain page fetch. They are stubs. A probe of the portal's
  backing API was stopped by the session's permission check and not pursued: asking OIT for a public export or PDF of the
  articles is the owner's next step.
- The index marks the 2026 (16 policies), 2022 and 2019 CISP sets and POL 200-01/200-02 as archived: left out.

## Executive orders

`governor.colorado.gov` and `spl.cde.state.co.us` (the State Publications Library, which holds the Governor's orders as PDFs)
time out on connection; `www.colorado.gov/governor` and `governorsoffice.colorado.gov` answer 403 with curl too. None seeded.
