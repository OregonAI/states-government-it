# 02 — Source availability: state law text and the state-IT-governance pilot domain

Researched 2026-11-10. Not legal advice; the legal section reports what the sources say and where a lawyer is needed.

## How to read this

Evidence tags used throughout:

- **F** — the page was fetched and read in this research pass.
- **S** — seen only in a search-result snippet; the page itself was not opened. Treat as a lead.
- **UNVERIFIED** — not confirmed. Anything marked "(memory)" is a recollection, not a finding.
- **BLOCKED** — the site refused the fetch (403, bot challenge, broken TLS chain) or returned only a JavaScript shell.

Method caveats:

- Every state row was checked with roughly 4-6 fetches. Terms pages that were not found are reported as "none found", which is weaker than "none exist".
- Risk ratings are this research's judgment, not sourced facts.
- Some robots.txt and page reads (AK, IL, NM, and the MA-NJ group) were made with `curl` sending a browser-style User-Agent before the session's permission system stopped that practice. Those facts are accurate but were not obtained with an honestly labelled client; where a plainly labelled client was refused, the row says BLOCKED. A production crawler should not rely on that route.
- Four of the eight pilot-sample statute citations (CA, CO, and parts of NY, OH) were confirmed only on unofficial mirrors or by section headings, because the official host was blocked or not fetched.
- The Lexis free-access portals (`advance.lexis.com`) and `govt.westlaw.com` returned no readable text or terms to any fetch, so vendor terms for every vendor-hosted code are UNVERIFIED.

---

## 1. Legal position on reusing state law text

### 1.1 What *Georgia v. Public.Resource.Org* decided

Source: slip opinion, No. 18-1150, 590 U.S. ___ (Apr. 27, 2020), https://www.supremecourt.gov/opinions/19pdf/18-1150_7m58.pdf (F, text extracted from the PDF).

| Point | What the opinion says |
|---|---|
| Holding | "We hold that the annotations in Georgia's Official Code are ineligible for copyright protection" (slip op. at 5). |
| Test | "copyright does not vest in works that are (1) created by judges and legislators (2) in the course of their judicial and legislative duties" (slip op. at 9). |
| Force of law is not the test | The rule "applies both to binding works (such as opinions) and to non-binding works (such as headnotes and syllabi)" (slip op. at 7). |
| Limit | "It does not apply, however, to works created by government officials (or private parties) who lack the authority to make or interpret the law, such as court reporters" (slip op. at 7). |
| Statutes and regulations | The majority notes that state claims of copyright "in their primary law materials," including statutes and regulations, are conceded by the dissent to be "plainly foreclosed by our government edicts precedents" (slip op. at 13 n.3). This is a footnote aside, not a holding on regulations. |
| Scale | The dissent counts "25 other jurisdictions—22 States, 2 Territories, and the District of Columbia—that rely on arrangements similar to Georgia's to produce annotated codes" (Thomas, J., dissenting, at 1). |

### 1.2 Coverage by instrument type

| Instrument | Position | Basis |
|---|---|---|
| Statute text (session laws, codified sections) | Not copyrightable. | *Georgia* test; legislators acting as legislators. |
| Annotations, notes, catchlines produced by or for a legislative body | Not copyrightable where the legislature (or its arm) is the author, as in Georgia. A vendor's own unofficial annotations remain copyrightable. | Slip op. at 9-11; Compendium § 313.6(C)(2). |
| Court opinions, headnotes written by judges | Not copyrightable. | Slip op. at 7. |
| Administrative rules / regulations | Not squarely decided. The *Georgia* test names only judges and legislators. The Copyright Office will not register "legislative enactments, judicial decisions, administrative rulings, public ordinances, or similar types of official legal materials" issued by any state government. Strong position, but an inference rather than a Supreme Court holding. | Compendium (Third) § 313.6(C)(2), https://www.copyright.gov/comp3/chap300/ch300-copyrightable-authorship.pdf (F); slip op. at 13 n.3. |
| Executive orders | Same analysis as rules: a "similar type of official legal material" under the Compendium, not addressed in *Georgia*. | Same. |
| CIO policies, standards, guidelines, manuals | **Weakest category.** Unlike federal works, state works that are not edicts can be copyrighted: "a work that does not constitute a government edict may be registered, even if it was prepared by an officer or employee of a state ... government while acting within the course of his or her official duties." Whether a binding statewide IT standard is an "edict" is untested. | Compendium § 313.6(C)(2) (F). |
| Privately authored standards incorporated by reference (NIST is federal and free; ISO, CIS and similar are not) | Copyright survives, but non-commercial posting of incorporated standards was held fair use. | *ASTM v. Public.Resource.Org*, 82 F.4th 1262 (D.C. Cir. 2023), summarised at https://www.copyright.gov/fair-use/summaries/amsoc-publicresourceorg-dccirc2023.pdf (F). |
| Compilation, arrangement, numbering | Several states claim copyright in arrangement or numbering rather than text (Michigan rules, Georgia rules via Fastcase). Not resolved by *Georgia*. | See table 1.3. |

Two separate risks that copyright doctrine does not remove:

- **Contract and access terms.** A site's terms of use, a no-robots clause (Colorado SOS, Maryland regs) or a bot wall is a contract/access question, not a copyright one. Enforceability of browse-wrap scraping bans was not researched here and needs counsel.
- **State statutes that assert ownership or charge fees.** Idaho Code § 74-123 and Kentucky's KRS 61.874 notice are still on the books after *Georgia*. Whether they survive is a legal question this research did not resolve.

### 1.3 Fifty-state table: copyright assertions, restrictive terms, vendor publication

"Stat." = codified statutes; "Rules" = administrative code. Quotes are short operative extracts.

| State | Statutes: assertion / terms | Rules: assertion / terms | Vendor-only? | Risk |
|---|---|---|---|---|
| AL | "Copyright © 2026 The Alabama Legislature. All rights reserved." https://dev.alaleg.gov/code-of-alabama (F). Ala. Code § 36-13-5 copyright provision (S, old copy). | None found; terms UNVERIFIED. https://admincode.legislature.state.al.us/administrative-code (F) | No | Medium: JS-only apps, statutory copyright claim |
| AK | "To obtain permission to reproduce the information ... send an email"; "All Rights Reserved." https://akleg.gov/disclaimer.php (F). robots.txt: `ai-train=no`, AI crawlers disallowed (F). | Same site and notices. | No (print: LexisNexis, S) | Medium: permission language, bot filtering |
| AZ | "© 2026 Arizona State Legislature. All Rights Reserved"; official version "is published by Thomson Reuters." https://www.azleg.gov/arstitle/ (F). robots.txt `Crawl-delay: 120` (F). | "may reproduce, without restrictions"; "Commercial use fees apply to those who intend to use the Code for resale or profit." azsos.gov/node/75 (S; site BLOCKED) | No | Stat. low-medium; rules medium |
| AR | Lexis portal; "the user acknowledges the State's copyright interests in the Arkansas Code of 1987" https://aogc.state.ar.us/Rules/Code.aspx (S). Lexis terms UNVERIFIED. | "© 2026 - Arkansas State Government"; no terms. https://codeofarrules.arkansas.gov/ (F) | **Stat.: LexisNexis** | Stat. high; rules low-medium |
| CA | "within the public domain and the State of California retains no copyright or other proprietary interest" (Gov. Code § 10248.5) https://leginfo.ca.gov/ (F) | Westlaw-hosted under OAL contract with Barclays/Thomson Reuters. https://oal.ca.gov/publications/ccr/ (F). Westlaw terms UNVERIFIED. | **Rules: Westlaw** | Stat. low; rules high |
| CO | Committee "suspended its practice of copyrighting" in 2016; republication "may not contain any notice ... that it is the official statutes". https://leg.colorado.gov/agencies/office-legislative-legal-services/colorado-revised-statutes-data (F) | "Use of computerized 'robots' or 'data mining' ... is prohibited." https://www.sos.state.co.us/pubs/info_center/terms.html (F) | Viewer is Lexis; state zips exist | Stat. low; rules medium-high |
| CT | UNVERIFIED (cga.ct.gov BLOCKED, broken TLS chain). Print copyright reported second-hand (S). | "© 2018 CT.GOV"; no reuse terms. https://eregulations.ct.gov/eRegsPortal/ (F) | No (memory) | Medium: unverified |
| DE | No copyright notice; online code is "an official version". https://delcode.delaware.gov/ (F) | No reuse statement found (F); new app terms UNVERIFIED | No | Low |
| FL | "Copyright © 1995-2026 The Florida Legislature"; no terms page. https://www.leg.state.fl.us/statutes/ (F) | "Copyright @ 2010 State of Florida Department of State"; no terms. https://www.flrules.org/ (F) | No | Low |
| GA | Lexis portal; terms UNVERIFIED. Annotations held uncopyrightable (*Georgia*). | "Copyright © 2026 Fastcase, Inc - All rights reserved."; XML feed sold to "Resellers". https://rules.sos.ga.gov/ (F) | **Stat.: LexisNexis; rules: Fastcase** | Stat. medium; rules high |
| HI | No claim found. https://data.capitol.hawaii.gov/hrsall/ (F) | "Copyright © 2026, State of Hawaii. All rights reserved." on the directory page. https://ltgov.hawaii.gov/the-office/administrative-rules/ (F) | No | Medium: rules scattered over ~24 agency sites |
| ID | "the state of Idaho and the taxpayers shall be deemed to have a copyright on the Idaho Code"; commercial reproduction owes "a royalty fee". Idaho Code § 74-123, https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH1/SECT74-123 (F) | "© 2026 Division of Financial Management. All rights reserved." https://adminrules.idaho.gov/rules/current/ (F) | No (print: LexisNexis, F) | **High** |
| IL | UNVERIFIED; no claim surfaced. Site returns "Automated Request Blocked" to labelled clients. | UNVERIFIED | No | Medium: BLOCKED |
| IN | UNVERIFIED | UNVERIFIED | No | Medium: JS-only, terms unknown |
| IA | Footer "© Iowa Legislature"; "as is" disclaimer only. https://www.legis.iowa.gov/law/disclaimer (F) | Same. | No | Low |
| KS | No copyright or terms page found. https://www.ksrevisor.gov/ksa.html (F) | "© 2025 Kansas Secretary of State"; rules.ks.gov terms UNVERIFIED | No | Stat. low; rules medium |
| KY | "does not alter or relinquish any copyright"; "unlawful to use any records available on this site for a commercial purpose without agreement" (KRS 61.874). https://legislature.ky.gov/Law/Statutes/Pages/default.aspx (F) | "Copyright © 2024 Kentucky Legislative Research Commission ... All rights reserved" https://apps.legislature.ky.gov/law/kar/titles.htm (F) | No | **Medium-high** |
| LA | No claim found; "not official or authoritative." https://legis.la.gov/legis/LawSearch.aspx (F) | "© Louisiana Division of Administration"; disclaimer page not read. | No | Low |
| ME | "The State of Maine claims a copyright in its codified statutes"; republication allowed with a prescribed disclaimer. https://legislature.maine.gov/statutes/1/title1sec502.pdf (F) | UNVERIFIED (maine.gov BLOCKED) | No | Medium: claim with a compliance path |
| MD | None found on https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes (F) | "licensed under the CC BY-NC-SA 4.0 license ... dedicated to the public domain under the CC0 1.0 license 180 days after publication"; "Please do not scrape." https://regs.maryland.gov/ (F) | No (Open Law Library) | Low via GitHub |
| MA | "the General Court forbids any copying or use other than" fair use, for material it copyrights (design, layout). https://malegislature.gov/StateHouse/TermsAndConditions (F) | "unofficial and for informational use" (second-hand, F); mass.gov BLOCKED | No | Medium |
| MI | Automated policy: "maximum of one (1) request per second". https://www.legislature.mi.gov/Home/AutomatedDataCollectionPolicy (F). No text copyright found. | Arrangement and numbering "protected under copyright"; "unauthorized reproduction, sale, or other commercial use is hereby prohibited" (S; source page BLOCKED) | No | Stat. low; rules medium |
| MN | "the revisor of statutes is not claiming copyright" following *Georgia*. https://www.revisor.mn.gov/statutes/2024/document/misc/Preface/ (F) | Disclaimer does not name Rules; Minn. Stat. 14.47 still authorises copyright. https://www.revisor.mn.gov/statutes/cite/14.47 (F) | No | Low |
| MS | Lexis portal; terms UNVERIFIED. Miss. Code § 1-1-9 and 2013 AG takedown demand to Public.Resource.Org (S). | UNVERIFIED (sos.ms.gov BLOCKED) | **Stat.: LexisNexis** | **High** |
| MO | "©Missouri Legislature, all rights reserved."; "uncertified and unofficial." https://revisor.mo.gov/main/Home.aspx (F) | None found. https://www.sos.mo.gov/adrules/csr/csr (F) | No | Medium |
| MT | No copyright notice. https://mca.legmt.gov/bills/mca/index.html (F) | Terms UNVERIFIED (disclaimer PDF BLOCKED) | No | Stat. low; rules medium |
| NE | "Copyright © Nebraska Legislature, all rights reserved." https://nebraskalegislature.gov/contact/disclaimer.php (F) | UNVERIFIED | No | Medium |
| NV | Footer "Copyright © by State of Nevada" https://www.leg.state.nv.us/law1.html (F) | "Copyright © by State of Nevada" / "All rights reserved." https://www.leg.state.nv.us/NAC/ (F) | No | Medium |
| NH | None found. robots.txt `Crawl-delay: 11`. https://gc.nh.gov/rsa/html/NHTOC.htm (F) | "© Copyright 2026 State Of New Hampshire."; online version "NOT the official version". https://gc.nh.gov/rules/about_rules/official_version.aspx (F) | No | Low |
| NJ | "©2026 New Jersey Office of Legislative Services All rights reserved."; "provided free of charge to the public". https://www.njleg.gov/disclaimer (F) | LexisNexis free access; "not the official Code." https://www.nj.gov/oal/rules/accessp (F). Lexis terms UNVERIFIED. | **Rules: LexisNexis** | Stat. low; rules high |
| NM | "© Copyright New Mexico Compilation Commission All Rights Reserved" https://www.nmcompcomm.us/search-laws/ (F). Platform terms link 404. Default collection is annotated; an unannotated one exists. | "Copyright 2025. All Rights Reserved."; no terms page. https://www.srca.nm.gov/nmac-home/ (F) | State, on Lexum platform (anti-bot script) | Medium |
| NY | API docs: free key; "10 requests per second and 4 concurrent requests" from 2026-12-01. https://legislation.nysenate.gov/static/docs/html/index.html (F). Text-licence terms UNVERIFIED (nysenate.gov BLOCKED). | Westlaw-hosted, "unofficial" (S); terms UNVERIFIED (BLOCKED) | **Rules: Westlaw** | Stat. low; rules high |
| NC | None asserted; "as a service to the public". https://www.ncleg.gov/Laws/GeneralStatutes (F) | "grants permission to copy and distribute ... for non-commercial use, provided they are copied and distributed without alteration" https://www.nc.gov/disclaimer-terms-use (F) | No | Stat. low; rules medium |
| ND | None found; online text "is the official version". https://ndlegis.gov/general-information/north-dakota-century-code/index.html (F) | None found (F) | No | Low |
| OH | No copyright claim; liability disclaimer only. https://codes.ohio.gov/legal/disclaimer (F). robots.txt `User-agent: * Disallow: /` (F). | Same site and terms. | No | Medium: blanket robots disallow |
| OK | No terms found. robots.txt `Disallow: /` on both oklegislature.gov and oscn.net (F). | UNVERIFIED (rules.ok.gov BLOCKED). robots.txt: "As a condition of accessing this website, you agree to abide by the following content signals", `ai-train=no`, AI crawlers disallowed (F). | Rules platform appears vendor-hosted (Tecuity) | Stat. medium; rules high |
| OR | No copyright notice found; "not the official text of Oregon law." https://www.oregonlegislature.gov/bills_laws/Pages/ORS.aspx (F). 2008 claim against Justia later dropped (S). ORS 171.275 copyright power (S). | "© 2026 Oregon Secretary of State All Rights Reserved"; no scraping or reuse restriction found. https://sos.oregon.gov/Pages/terms-and-conditions.aspx (F) | No | Low |
| PA | No copyright claim; "AS IS" and DMCA notice. https://www.palegis.us/legal (F) | "No part of the information on this site may be reproduced for profit or sold for profit." https://www.pacodeandbulletin.gov/Home/Disclaimer (F). robots.txt `Disallow: /` (F). | **Rules: Fry Communications** | Stat. low; rules medium-high |
| RI | "© State of Rhode Island General Assembly"; informational only. https://www.rilegislature.gov/Pages/disclaimer.aspx (F) | "© Rhode Island Department of State"; no terms page. (F) | No | Low |
| SC | "may be copied from this website at the reader's expense and effort without need for permission." https://www.scstatehouse.gov/code/statmast.php (F) | Same grant for unannotated regulations. https://www.scstatehouse.gov/coderegs/statmast.php (F) | No | **Low: express permission** |
| SD | SDCL 2-16-8: code "will be copyrighted by the State of South Dakota ... to the extent permitted by federal copyright law." https://sdlegislature.gov/api/Statutes/2-16-8.html (F). No site terms. | None found. | No | Medium |
| TN | Lexis portal; terms UNVERIFIED. "© 2017 by The State of Tennessee All rights reserved" and click-through terms (S). Trial court (2022) said the *Georgia* test "disqualifies Tennessee Code Annotated as protected by copyright law" but dismissed the records petition. https://law.resource.org/pub/us/code/tn/2022.08.30.Final.Order.On.Petition.pdf (F) | UNVERIFIED (tn.gov, sos.tn.gov BLOCKED) | **Stat.: LexisNexis** | **High** |
| TX | No copyright statement found. FTP notice asks data companies to "stop data mining" the bills site (F, ftp://ftp.legis.state.tx.us/Acceptable_Use_FTP_Public_Site.txt). | Warranty-only disclaimer. https://www.sos.state.tx.us/disclaimer.shtml (F) | Rules on Appian portal | Stat. low; rules medium |
| UT | "may not use any part of the information ... for commercial purposes or publish the information for commercial gain without proper attribution of source." https://le.utah.gov/documents/disclaimer.htm (F) | "Anyone may view, copy, or distribute ... if the documents are not modified in any respect" https://www.utah.gov/support/disclaimer.html (F) | No | Medium |
| VT | "an unofficial copy of the Vermont Statutes Annotated"; "Copyright 2026 State of Vermont. All rights reserved." https://legislature.vermont.gov/statutes/ (F) | Lexis portal; terms UNVERIFIED | **Rules: LexisNexis** | Stat. medium; rules high |
| VA | "excludes material copyrighted by the publisher, Michie"; "© Copyright Commonwealth of Virginia ... All rights reserved." https://law.lis.virginia.gov/vacode/ (F) | Same footer; nothing specific. | No | Low |
| WA | Statute Law Committee "claims copyright for both codes"; contact it if obtaining them "for the purpose of selling". https://leg.wa.gov/disclaimer/ (F). app.leg.wa.gov robots.txt `Disallow: /` (F). | Same sentence covers the WAC. | No | Medium |
| WV | "Copyright © 2026 West Virginia Code."; no terms page. https://code.wvlegislature.gov/ (F) | None found. https://apps.sos.wv.gov/adlaw/csr/ (F) | No | Medium |
| WI | None found; statutes "Certified under s. 35.18". https://docs.legis.wisconsin.gov/statutes/prefaces/toc (F) | None found. (F) | No | Low |
| WY | UNVERIFIED on the current site (JS-only); older state copyright statement (S). | "Wyoming Secretary of State 2016 © All Rights Reserved." https://rules.wyo.gov/ (F) | No (annotated print: LexisNexis, S) | Medium |

Counts from this table (statutes / rules judged separately where they differ):

- **Vendor-only access:** statutes in AR, GA, MS, TN (LexisNexis); rules in CA, NY (Westlaw), NJ, VT (LexisNexis), GA (Fastcase), PA (Fry). Colorado's viewer is Lexis but the state publishes its own zips.
- **Copyright asserted by statute or express notice on code text:** ID, KY, ME, SD, WA, AL (S), AR (S), MS (S), plus arrangement claims in MI rules and NV rules.
- **Express disclaimer or permission:** CA, MN, SC, CO (practice suspended), MD rules (CC0 after 180 days), AZ rules (S).
- **Blanket robots.txt disallow on a state host that still serves pages:** OH, OK (both statute hosts), PA Code, WA app host.

---

## 2. Practical access per state

### 2.1 Fifty-state table: URLs, formats, machine-readable routes

| State | Statutes: URL, format | Statutes: bulk / API | Rules: URL, format | Rules: bulk / API |
|---|---|---|---|---|
| AL | https://alison.legislature.state.al.us/code-of-alabama — JS app (F) | None found | https://admincode.legislature.state.al.us/administrative-code — JS app (F) | Internal `/api` exists; routes UNVERIFIED |
| AK | https://www.akleg.gov/basis/statutes.asp — HTML (WebFetch BLOCKED) | None found | https://www.akleg.gov/basis/aac.asp — HTML | None found |
| AZ | https://www.azleg.gov/arstitle/ — static HTML per section (F) | None; crawlable at 120 s delay | https://apps.azsos.gov/public_services/CodeTOC.htm — PDF/RTF (BLOCKED) | None found |
| AR | Lexis portal linked from https://www.arkleg.state.ar.us/ArkansasLaw — JS app (F) | None | https://codeofarrules.arkansas.gov/ — HTML app (F) | None found |
| CA | https://leginfo.legislature.ca.gov/faces/codes.xhtml — HTML (BLOCKED) | **Yes**: https://downloads.leginfo.legislature.ca.gov/ daily `pubinfo_daily_*.zip` (F; zip contents not opened) | https://govt.westlaw.com/calregs/ (BLOCKED) | None found |
| CO | https://leg.colorado.gov/agencies/office-legislative-legal-services/colorado-revised-statutes — Lexis viewer (F) | **Yes**: `https://olls.info/crs/crs2026-htm.zip`, `-pdf.zip`, `-docx.zip`; SGML on request. https://leg.colorado.gov/agencies/office-legislative-legal-services/2026-crs-titles-download (F) | https://www.sos.state.co.us/CCR/Welcome.do — PDF per rule (F) | None; terms say bulk data is sold |
| CT | https://www.cga.ct.gov/current/pub/titles.htm (BLOCKED) | UNVERIFIED | https://eregulations.ct.gov/eRegsPortal/ (F) | None found |
| DE | https://delcode.delaware.gov/ — HTML + authenticated PDF per title (F) | No single file; 31 title PDFs | https://regulations.delaware.gov/AdminCode/ — JS app (F) | `/api/register/...` path seen (S) |
| FL | https://www.leg.state.fl.us/statutes/ — HTML (F) | `FLLawDL2026.zip` is a Windows app, not data (F) | https://www.flrules.org/ — Word `.doc` per chapter (F) | None found |
| GA | Lexis portal; https://www.legis.ga.gov/ is a JS shell (F) | None | https://rules.sos.ga.gov/ — HTML + PDF (F) | Paid XML feed only |
| HI | https://data.capitol.hawaii.gov/hrscurrent/ — HTML per section, open directory (F); www host BLOCKED | Directory listing | No unified code; index at https://ltgov.hawaii.gov/the-office/administrative-rules/ (F) | None |
| ID | https://legislature.idaho.gov/statutesrules/idstat/ — HTML (F) | None found | https://adminrules.idaho.gov/rules/current/ — format UNVERIFIED (F) | None found |
| IL | https://www.ilga.gov/Legislation/ILCS/Chapters — HTML (BLOCKED) | https://www.ilga.gov/ftp/ILCS/ refreshed about yearly (seen once; S for readme) | https://www.ilga.gov/agencies/JCAR/AdminCode (BLOCKED) | `/ftp/JCAR/` dated 2018, likely stale |
| IN | https://iga.in.gov/laws/2025/ic/titles/1 — JS app (F) | API docs https://docs.api.iga.in.gov/ (BLOCKED); key required (S) | http://iac.iga.in.gov/ — JS app (F) | UNVERIFIED |
| IA | https://www.legis.iowa.gov/law/iowaCode — PDF + RTF (F) | None; stable per-document URLs | https://www.legis.iowa.gov/law/administrativeRules — PDF + RTF (F) | None; stable URLs |
| KS | https://www.ksrevisor.gov/ksa.html — HTML (F) | None found | https://rules.ks.gov/ — JS app (F) | UNVERIFIED |
| KY | https://apps.legislature.ky.gov/law/statutes/ — chapter index; section format UNVERIFIED (F) | None found | https://apps.legislature.ky.gov/law/kar/titles.htm — HTML index (F) | None found |
| LA | https://legis.la.gov/legis/Laws_Toc.aspx?folder=75&level=Parent — HTML with postbacks (F) | None found | https://www.doa.la.gov/doa/osr/louisiana-administrative-code/ — one `.docx` per title (F) | Whole code in a few dozen files |
| ME | https://legislature.maine.gov/statutes/ — HTML, PDF, Word (F) | Whole-title `.docx`/`.pdf` | https://www.maine.gov/sos/cec/rules/rules.html (BLOCKED) | UNVERIFIED |
| MD | https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes — HTML + PDF (F) | None for code text | https://regs.maryland.gov/ — HTML (F) | **Yes**: GitHub `maryland-dsd/law-xml-codified-cc0`, `law-html-cc0` (links F; repos not opened) |
| MA | https://malegislature.gov/Laws/GeneralLaws — HTML (F) | None found | https://www.mass.gov/code-of-massachusetts-regulations-cmr (BLOCKED) | UNVERIFIED |
| MI | https://www.legislature.mi.gov/Laws/MCL — HTML, PDF, XML | **Yes**: https://legislature.mi.gov/documents/mcl/ (XML/PDF, monthly archives); SOAP service; RSS (F via policy page) | https://ars.apps.lara.state.mi.us/AdminCode/AdminCode — PDFs (F) | None found |
| MN | https://www.revisor.mn.gov/statutes/ — HTML + PDF (F) | None found | https://www.revisor.mn.gov/rules/ — HTML + PDF (F) | None found |
| MS | Lexis portal https://www.lexisnexis.com/hottopics/mscode/ — JS app (F) | None | https://www.sos.ms.gov/adminsearch/default.aspx (BLOCKED) | UNVERIFIED |
| MO | https://revisor.mo.gov/main/Home.aspx — HTML (F) | None found | https://www.sos.mo.gov/adrules/csr/csr — PDF per chapter (F) | Predictable PDF URLs |
| MT | https://mca.legmt.gov/bills/mca/index.html — static HTML tree (F) | None found | https://rules.mt.gov/ — JS app (F) | UNVERIFIED |
| NE | https://nebraskalegislature.gov/laws/browse-statutes.php — HTML, whole chapter per page (F) | None; chapter pages | https://rules.nebraska.gov/ — JS app (F) | UNVERIFIED |
| NV | https://www.leg.state.nv.us/NRS/ — static HTML per chapter (F) | None; ~700 predictable files | https://www.leg.state.nv.us/NAC/ — static HTML per chapter (F) | Same |
| NH | https://gc.nh.gov/rsa/html/NHTOC.htm — static HTML per section (F) | None found | https://gc.nh.gov/rules/about_rules/listagencies.aspx (F) | None found |
| NJ | Gateway linked from https://www.njleg.gov — HTML (F) | **Yes**: https://pub.njleg.gov/statutes/ `STATUTES-TEXT.zip`, updated weekdays (F) | Lexis portal http://www.lexisnexis.com/hottopics/njcode — JS app (F) | None |
| NM | https://nmonesource.com/nmos/en/nav.do — HTML viewer (WebFetch BLOCKED) | None found | https://www.srca.nm.gov/nmac-home/nmac-titles/ — HTML index; file format UNVERIFIED (F) | None found |
| NY | https://www.nysenate.gov/legislation/laws (BLOCKED); http://public.leginfo.state.ny.us/lawssrch.cgi?NVLWO: (F) | **Yes**: Open Legislation API, https://legislation.nysenate.gov/api/3/laws, free key, JSON (F docs) | https://govt.westlaw.com/nycrr (BLOCKED) | None found |
| NC | https://www.ncleg.gov/Laws/GeneralStatutesTOC — HTML + PDF (F) | None for statutes | http://reports.oah.state.nc.us/ncac.asp — PDF, HTML, .doc (F; HTTP only) | Predictable paths |
| ND | https://ndlegis.gov/general-information/north-dakota-century-code/index.html — PDF per chapter (F) | Predictable PDF URLs | https://ndlegis.gov/agency-rules/north-dakota-administrative-code/index.html — PDF per chapter (F) | Predictable PDF URLs |
| OH | https://codes.ohio.gov/ohio-revised-code — HTML + authenticated PDF (F) | None found | https://codes.ohio.gov/ohio-administrative-code — HTML + PDF (F) | None found |
| OK | https://www.oklegislature.gov/osStatuesTitle.aspx — one PDF per title; https://www.oscn.net/applications/oscn/index.asp?ftdb=STOKST&level=1 — HTML (F) | `https://www.oklegislature.gov/OK_Statutes/CompleteTitles/os1.pdf` pattern | https://rules.ok.gov/code (BLOCKED) | UNVERIFIED |
| OR | https://www.oregonlegislature.gov/bills_laws/Pages/ORS.aspx — HTML per chapter (F) | Predictable chapter URLs | https://secure.sos.state.or.us/oard/ruleSearch.action — HTML database (F) | None found |
| PA | https://www.palegis.us/statutes/consolidated — HTML, PDF, Word per title (F); unconsolidated statutes are separate | Per-title URLs | https://www.pacodeandbulletin.gov/ — HTML (F) | None found |
| RI | https://webserver.rilegislature.gov/Statutes/ — static HTML per section (F) | Crawlable tree | https://rules.sos.ri.gov/organizations — HTML (F) | None found |
| SC | https://www.scstatehouse.gov/code/statmast.php — HTML + Word per chapter (F) | Per-chapter files | https://www.scstatehouse.gov/coderegs/statmast.php — Word + PDF per chapter (F) | Per-chapter files |
| SD | https://sdlegislature.gov/Statutes — JS shell (F) | **Yes**: keyless `https://sdlegislature.gov/api/Statutes/1-1-1.html`; sitemap https://sdlegislature.gov/Statutes.xml (F) | https://sdlegislature.gov/Rules/Administrative — JS shell (F) | Keyless `/api/Rules/Rule/...`; sitemap (F) |
| TN | Lexis portal https://www.lexisnexis.com/hottopics/tncode/ — JS app (F) | None | https://sos.tn.gov/publications/services/effective-rules-and-regulations-of-the-state-of-tennessee (BLOCKED) | UNVERIFIED |
| TX | https://statutes.capitol.texas.gov/ — JS app (F); static HTML at `https://tcss.legis.texas.gov/resources/GV/htm/GV.2054.htm` (F) | **Yes**: per-code zips (HTML, PDF, Word) listed in https://statutes.capitol.texas.gov/assets/StatuteCodeDownloads.json (F) | https://www.sos.state.tx.us/tac/index.shtml → Appian portal, JS-only (F) | None found |
| UT | https://le.utah.gov/xcode/code.html — HTML, XML, PDF, RTF per section (F) | Per-section XML at versioned URLs; no archive | https://adminrules.utah.gov/ — JS app (F) | None found |
| VT | https://legislature.vermont.gov/statutes/ — HTML (F) | None for statutes | Lexis portal https://www.lexisnexis.com/hottopics/codeofvtrules/ — JS app (F) | None |
| VA | https://law.lis.virginia.gov/vacode/ — HTML (F) | **Yes**: keyless JSON/XML API, https://law.lis.virginia.gov/developers/; per-title CSV/PDF at https://law.lis.virginia.gov/law-library/ (F) | https://law.lis.virginia.gov/admincode/ — HTML (F) | API said to cover it (endpoint not tested) |
| WA | https://app.leg.wa.gov/rcw/ — HTML (F) | Open directory https://lawfilesext.leg.wa.gov/law/RCW/ (F; file types not checked) | https://app.leg.wa.gov/wac/ — HTML (linked, not fetched) | Open directory https://lawfilesext.leg.wa.gov/law/WAC/ (F) |
| WV | https://code.wvlegislature.gov/ — HTML (F) | None; sitemap | https://apps.sos.wv.gov/adlaw/csr/ — PDF + Word per rule (F) | None; RSS |
| WI | https://docs.legis.wisconsin.gov/statutes/prefaces/toc — HTML + PDF per chapter (F) | Predictable URLs | https://docs.legis.wisconsin.gov/code/admin_code — HTML + PDF per chapter (F) | Predictable URLs |
| WY | https://wyoleg.gov/StateStatutes/StatutesDownload — JS shell; `https://wyoleg.gov/statutes/compress/title01.pdf` (F) | Per-title PDFs | https://rules.wyo.gov/ — search interface; format UNVERIFIED (F) | None found |

Official machine-readable or bulk routes confirmed for statutes: **CA, CO, MI, NJ, NY, SD, TX, UT, VA**, plus directory listings in HI, IL (stale, blocked) and WA. For rules: **MD** (GitHub), **SD**, **VA** (claimed), **WA** (directory). Everything else is per-page HTML, per-chapter PDF/Word, or a JavaScript app.

### 2.2 Aggregated sources that could shortcut collection

| Source | What it holds | Licence / terms | Usefulness |
|---|---|---|---|
| Public.Resource.Org bulk | Directories for AR, CA (incl. CCR), CO, DE, GA, ID, MS, OR, TN codes. https://law.resource.org/pub/us/code/ (F). Georgia: OCGA releases 71-73 (2019) as Word/ODT zips. https://law.resource.org/pub/us/code/ga/ (F) | No licence statement on the index pages (F). | Snapshots, mostly stale; valuable as litigation record and for vendor-only states. |
| Public.Resource.Org litigation files | Tennessee: public-records petition against LexisNexis over the Tennessee Code, 2022; Tenn. Supreme Court denied permission to appeal 2024-09-12. https://law.resource.org/pub/us/code/tn/ (F). Oregon: *PRO v. Oregon DCBS*, Marion Co. 24CV30573, dismissed 2025-09-18, on appeal (opening brief 2026-06-01). https://law.resource.org/pub/us/code/or/ (F) | n/a | Shows that vendor-held official codes are still contested through records law, not just copyright. |
| Open Law Library | Platform for governments publishing their own law; DC code at https://code.dccouncil.gov (F). Maryland COMAR is "Powered by the non-profit Open Law Library" with CC0 repos (F, https://regs.maryland.gov/). Full partner list not found. | Per jurisdiction; Maryland CC0 after 180 days. | Best-case model; covers very few states. |
| Open States / Plural | Bills, votes, legislators, committees, events; no codified statutes mentioned. API key required. https://docs.openstates.org/api-v3/ (F). Bulk CSV/JSON/Postgres dumps monthly. | "Unless otherwise noted data is provided under a public domain dedication." https://open.pluralpolicy.com/data/ (F) | Good for tracking amending bills, not for code text. |
| LegiScan datasets | Weekly per-session bill/vote snapshots, CSV and JSON. | CC BY 4.0 per a LegiScan datasets page (S). https://legiscan.com/datasets and its terms page BLOCKED (403). | Bills only; licence needs a manual read. |
| Justia US Law | Free HTML copies of state codes and regulations. | Terms page BLOCKED (403); terms UNVERIFIED. | Do not treat as a licensed bulk source until terms are read. |
| Cornell LII | State regulations and some statutes; much is "maintained by other institutions". | LII's own markup is CC BY-NC-SA 2.5; compilation copyright held by Cornell. https://www.law.cornell.edu/lii/terms/documentation (F) | NC and SA terms conflict with an unrestricted open mirror. |
| Internet Archive | No state-code collection was found in one search. | UNVERIFIED | Open lead. |

Takeaway: no aggregator gives current, licensed, machine-readable codified text for all 50 states. Collection has to be per state, from the official source.

---

## 3. Pilot domain: where the instruments live (8-state sample)

Full per-state instrument lists were gathered; this section keeps the anchors. Tags as above.

| State | CIO / IT agency enabling statute | Cybersecurity statute | AI statute or EO on government use | Policy library | Outside statute (est.) | Discovery |
|---|---|---|---|---|---|---|
| OR | ORS ch. 276A, esp. 276A.200-.209. https://www.oregonlegislature.gov/bills_laws/ors/ors276A.html (F) | ORS 276A.300-.335; 276A.550-.575 (F) | EO 23-26 (2023-11-28), https://www.oregon.gov/gov/eo/eo-23-26.pdf (F; scanned, no text layer). DAS policy 107-004-190 (S). A reported "EO 26-26" on AI procurement is S only. | Two partial indexes: https://www.oregon.gov/eis/pages/policies.aspx (F, 17 items) and https://www.oregon.gov/das/Pages/policies.aspx (script-rendered) | ~70% | Medium |
| CA | Gov. Code § 11545 et seq. (S; leginfo BLOCKED) | Gov. Code §§ 11549-11549.3; § 8586.5 (S) | EO N-12-23 (2023-09-06); N-5-26 (2026), listed at https://www.cdt.ca.gov/policy/executive-orders-related-to-it/ (F). Gov. Code § 11546.45.5; SB 896 (S) | SAM ch. 4800 https://www.dgs.ca.gov/Resources/SAM/TOC/4800 (F); SIMM https://cdt.ca.gov/policy/simm/ (F); 84 Technology Letters https://cdt.ca.gov/policy/technology-letters/ (F) | ~90% | Medium-hard |
| TX | Gov't Code ch. 2054. https://tcss.legis.texas.gov/resources/GV/htm/GV.2054.htm (F) | Gov't Code ch. 2063, Texas Cyber Command, eff. 2025-09-01. https://tcss.legis.texas.gov/resources/GV/htm/GV.2063.htm (F) | ch. 2054 subch. S (SB 1964 and HB 2818, colliding section numbers) (F); Bus. & Com. Code ch. 552 (F). No AI EO found. | https://dir.texas.gov/resource-library — "1,367 Resources", mixed types (F). Rules: 1 TAC Part 10 (S) | ~50% | Hard |
| NY | State Technology Law art. 1, §§ 101-107. https://www.nysenate.gov/legislation/laws/STT/A1 (F) | State Tech. Law § 103-f, § 210 (F headings) | State Tech. Law § 103-e, art. 5 §§ 501-504 (F). No AI EO found. Policy NYS-P24-001 (S) | https://its.ny.gov/policies — 64 results (F) | ~80% | Easy-medium |
| CO | C.R.S. 24-37.5-101 et seq. (F on an unofficial mirror, https://colorado.public.law/statutes/crs_title_24_article_37.5) | C.R.S. 24-37.5-401 to -405 (unofficial mirror) | SB 26-189 repeals and reenacts SB 24-205. https://leg.colorado.gov/bills/sb26-189 (F). OIT GenAI policy (S). No AI EO found (not searched in depth). | https://oit.colorado.gov/standards-policies-guides/technical-standards-policies (BLOCKED); part employee-only (S) | UNVERIFIED (library uncounted) | Hard |
| UT | Utah Code 63A-16. https://le.utah.gov/xcode/Title63A/Chapter16/C63A-16_2026050620260506.pdf (F) | 63A-16-1101 to -1104, Utah Cyber Center (F) | Utah Code 13-72 (private-sector focus) (F). DTS Policy 4000-0008 (title only, F). A reported October 2026 governor's AI order is S only. | https://dts.utah.gov/policies — public subset of 10 in a Google Drive folder; rest "(Sign In Required)" (F) | UNVERIFIED (most of library not public) | Hard |
| VA | Va. Code 2.2-2005 to 2.2-2034.1. https://law.lis.virginia.gov/vacode/title2.2/chapter20.1/ (F) | Va. Code 2.2-2009 (F); 2.2-5514 (S) | EO 30 (2024) rescinded; EO 22 (2026-09-18) and ED 6 (2026-10-23) listed on the governor's site (F list; PDFs not read). VITA AI standard and policy (F links) | https://www.vita.virginia.gov/policy--governance/policies-standards--guidelines/ — ~60 files (F) | ~85% | Easy-medium |
| OH | R.C. 125.18. https://codes.ohio.gov/ohio-revised-code/section-125.18 (F) | Inside R.C. 125.18; R.C. 9.64 covers local government (S) | No AI EO found. DAS policy IT-17 (official FAQ link; text seen on a third-party mirror) | DAS Policy Finder (das.ohio.gov returned 404 on tried URLs) | UNVERIFIED (library uncounted) | Medium |

Observations from the sample:

- **One enabling chapter plus 3-6 satellite statutes per state.** Finding the statute is the easy part; half of the example citations supplied for this task still needed correcting (Virginia EO 30 is rescinded; Colorado SB 24-205 was replaced; Ohio OAC 123:3 is not procurement; Texas cybersecurity moved to ch. 2063 in 2025).
- **Government-use AI is mostly not statute.** Oregon, California and Virginia use executive orders plus policy; Ohio, Utah, Colorado and New York use CIO policy; only Texas and New York have substantial government-AI statute text.
- **Executive orders are volatile and badly published.** Virginia's EO 30 now survives only as a library archive link; Oregon's EO is an image scan needing OCR; California's index lists 20 orders with no per-order links.
- **Policy libraries are the hard part.** Formats seen: PDF, DOCX, XLSX, Google Docs, a Google Drive folder, HTML manuals on a second agency's site.
- **Some instruments are not public.** California SIMM 5300-A is "classified as confidential" (https://cdt.ca.gov/policy/simm/simm-5300/, F). Utah's full enterprise policy set is behind sign-in (F). Colorado project-management policies are employee-only (S).
- **Copyright on policy pages.** Virginia: "©2026 Virginia IT Agency. All Rights Reserved." (F). California: "considered in the public domain" (https://cdt.ca.gov/conditions-of-use/, F). Texas: bare "©2026" footer (F). Oregon, New York, Utah: no notice found (F). Colorado, Ohio: UNVERIFIED.

---

## 4. Seed lists for 50-state discovery

| Source | What it gives | Machine-readable? | Reuse terms |
|---|---|---|---|
| NCSL AI legislation (annual pages) | Per-state bill list with number, title, status, summary and category tags including "Government Use". https://www.ncsl.org/technology-and-communication/artificial-intelligence-2025-legislation (F) | HTML table only; no download seen. Bill links go to LexisNexis State Net, not official sites. | "All intellectual property rights are reserved"; no republishing or copying "without permission". https://www.ncsl.org/terms-of-use (F) |
| NCSL cybersecurity legislation (annual pages) | Per-state bill list; 2025: 800+ bills, 200+ enacted. https://www.ncsl.org/technology-and-communication/cybersecurity-2025-legislation (F) | HTML table only. | Same. |
| NCSL "Data Security Laws — State Government" | Statute citations for 32 states with links, mostly to official sites. https://www.ncsl.org/technology-and-communication/data-security-laws-state-government (F) | HTML table. Last updated 2020-02-14: stale. | Same. |
| NCSL AI in government brief | Names six state AI EOs with links (AL, CA, MD, MA, OK, OR). Updated 2024-11-22. https://www.ncsl.org/technology-and-communication/artificial-intelligence-in-government-the-federal-and-state-landscape (F) | Prose + PDF. | Same. |
| NCSL 50-state CIO-statute table | Not found. A CISO-statutes page is referenced in 2022 testimony (S); URL unverified. | UNVERIFIED | Same. |
| NASCIO resource centre | Surveys and reports; no 50-state table of CIO statutes or AI policies found. https://www.nascio.org/resource-center/ (F) | PDFs, aggregates. | "© 2026 NASCIO"; no reuse terms found. |
| CDT state AI executive-order analysis | 13 states plus DC with government-AI EOs as of 2025-01-10, each linked: AL, CA, MD, MA, MS, NJ, OK, OR, PA, RI, VA, WA, WI. https://cdt.org/insights/state-government-use-of-ai-the-opportunities-of-executive-action-in-2025/ (F) | Prose with links. | No licence stated on the page. |
| Government Technology AI tracker | Interactive maps of state AI task forces, frameworks, leadership. https://www.govtech.com/biz/data/is-your-government-ai-ready-an-interactive-tracker-of-ai-action (F) | No download described. | "©2026 All rights reserved. e.Republic LLC". |
| Open States / LegiScan | Bill full text and status for all states (see 2.2). | Yes: API, CSV, JSON. | Public domain dedication (Open States, F); CC BY 4.0 (LegiScan, S). |

Practical reading: the curated lists are HTML-only and all-rights-reserved. They can be used as **pointers** (a citation is a fact) to find the official instrument, but their summaries and category text should not be copied into the corpus. The only openly licensed machine-readable seeds are bill feeds, which then need mapping from session law to codified section.

---

## 5. Conclusions

### (a) Easy, hard, legally risky

Judged on statutes and rules together; a state lands in the worst bucket either code puts it in. Based on tables 1.3 and 2.1, with their UNVERIFIED gaps.

| Bucket | States | Why |
|---|---|---|
| **Easy** (state-hosted, no restrictive terms found, workable format) | DE, FL, IA, LA, MN, ND, NH, OR, RI, SC, VA, WI | Static HTML or stable per-chapter files; SC grants express permission; MN disclaims copyright; VA has a keyless API. |
| **Easy for statutes, hard or risky for rules** | CA, NJ, NY (rules vendor-only); TX, MI, NC, PA, CO (rules behind a portal, a non-commercial or no-robots term, or an arrangement claim) | Official bulk or API for statutes; the administrative code is the problem. |
| **Technically hard** (JS-only apps, bot walls, PDF-only, scattered) | AL, IN, KS (rules), MT (rules), NE (rules), IL, MA (rules), HI (rules), OK, NM, UT (rules), WY, CT | Needs a headless browser, an undocumented API, a negotiated access route, or OCR/PDF parsing. |
| **Legally risky** | ID, KY, MS, TN, AR, GA (rules), VT (rules), WA, SD, ME | Statutory or express copyright claims (ID, KY, SD, WA, ME), vendor-only official codes with unread terms (MS, TN, AR, VT, GA), and a history of enforcement threats or litigation (MS, TN, GA, ID). |
| **Policy call rather than legal risk** | OH, OK, PA, WA, MD | Pages are served, but robots.txt says `Disallow: /` (or the site says "Please do not scrape"). |

Not yet placed with confidence because key facts are UNVERIFIED: AK, AZ, MO, NV, WV.

### (b) Where the pilot domain lives

Estimate from the 8-state sample (section 3). Shares are by count of distinct instruments, which overweights policy libraries; by legal weight statute matters more than its share suggests.

| Layer | Share of instruments | Notes |
|---|---|---|
| Statute | 10-25% (Texas ~40%) | One enabling chapter plus cyber, data, privacy, procurement and AI satellites. |
| Administrative rule | 0-10% | Substantial only in Texas (1 TAC Part 10), Utah (R895), Oregon (OAR 128), Colorado (8 CCR 1501). California, New York and Virginia showed none. |
| Executive order | 1-5%, but most of government-AI in about a third of states | 13 states plus DC had government-AI EOs by January 2025 (CDT). Volatile: rescinded on change of governor. |
| CIO policy, standard, manual, memo | 60-90% | 17 to 150+ documents per state; partly non-public in at least CA, UT, CO. |

Three of eight libraries could not be counted (CO, OH blocked or 404; UT mostly behind sign-in), so the upper end of the policy range is soft.

Implication: a statute-and-rule-only corpus would cover the authority to govern state IT and miss most of what the governing actually says. The policy layer is also where copyright is least settled (section 1.2) and where publication is least stable.

### (c) Open questions for a human

1. **Scope of "law".** Are CIO policies and standards in scope for full-text mirroring, given they are probably copyrightable state works rather than edicts? Options: mirror only where the state disclaims or permits (e.g. California), ask permission per state, or index with links only.
2. **robots.txt and no-scrape terms.** Does the project honour blanket `Disallow: /` (OH, OK, PA, WA) and "do not scrape" or no-robots terms (MD site, CO Secretary of State)? This decides whether several otherwise easy states are in.
3. **Bot walls.** Will the project ever use a browser-identity client or headless browser against sites that block labelled crawlers (IL, mass.gov, azsos.gov, tn.gov, leginfo.ca.gov)? This research stopped at the block. The alternative is asking each state for an access route.
4. **Vendor-only codes.** For AR, GA, MS, TN statutes and CA, NY, NJ, VT, GA, PA rules: skip, link only, request the data from the state under public-records law, or accept the Public.Resource.Org posture? Tennessee's courts refused a records request for the code in 2022-2024.
5. **States with live statutory claims** (ID royalty, KY commercial-use bar, WA, SD, ME disclaimer requirement): does the project comply with their conditions, rely on *Georgia*, or defer those states? Maine and Kentucky conditions also bind downstream commercial users of an open corpus.
6. **Licence of the project's own output.** Cornell LII (NC-SA), NCSL (all rights reserved) and several state terms (NC, UT "not modified", AZ commercial fee) are incompatible with a permissive downstream licence if their text or structure is copied.
7. **Annotated vs. unannotated text.** Where the free official copy is annotated (NM default, vendor portals), does the pipeline strip to statute text only?
8. **Executive-order lifecycle.** Keep rescinded EOs (Virginia EO 30) as historical documents, and from what source once the governor's site drops them?
9. **Seed-list use.** Is using NCSL and CDT lists as citation pointers (not copied text) acceptable, or should discovery start only from open bill feeds (Open States, LegiScan)?
10. **Verification debt.** About 40 cells are UNVERIFIED and every vendor terms page is unread. Decide whether a manual browser pass on those is needed before the pilot, or only for the states the pilot actually loads.
11. **Counsel.** Rules, executive orders and CIO standards rest on inference from *Georgia* and the Copyright Office Compendium, and scraping-terms enforceability was not researched. A lawyer should confirm the position before publication.
