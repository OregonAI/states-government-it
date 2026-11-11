# California: how long it took and what was hard (issue #6)

Dated 2026-11-11. Issue #6 asks for "how long the state took and what was hard", as the evidence for
whether the pattern scales to more states. Times come from `git log` author dates on this branch;
every difficulty below was observed with the toolkit's Fetcher on 2026-11-11 unless marked UNVERIFIED.

## Time

- Colorado's last commit is 00:29 (2026-11-11, -0800). California's ingester commits start 00:44; its
  seed list and 22 documents (13 statute slices, 2 CCR chapters, 7 SAM chapters) are committed by 00:58.
  About 30 minutes of agent time from the last state to the first full California ingest.
- The review-fix pass (this PR's later commits) took about the same again, 01:18 to 01:25 for code,
  plus the fetching of discovery pages. The review found three classes of error that the first pass
  missed: list markers (below), unconfirmed claims in stubs, and an unlisted table (the ITPLs).
- Result: 25 documents (after the fix pass) and 391 seed entries, of which the large majority are
  stubs, because the Department of Technology's site refuses the Fetcher.

## What was hard

1. **403 on three of the four official hosts that matter.** `www.cdt.ca.gov` (every page and file),
   `www.gov.ca.gov`, and `leginfo.legislature.ca.gov` answer the Fetcher with HTTP 403 and
   `cf-mitigated: challenge` (Cloudflare managed challenge). Rechecked on 2026-11-11 against the
   Technology Letters page, the executive orders page, the executive orders category page and
   a Governor's order PDF. Consequence: the SIMM, Technology Letter and Information Technology
   Policy Letter layer (about 150 entries) is stubs, and titles and urls for them came from a
   web-reading tool, not the Fetcher (stated in every stub's `stub_reason`).
2. **The statutes only come through a 1.2 GB bulk zip.** The per-section pages are behind the
   challenge. The Legislature's bulk download (`downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip`)
   answers, so the ingester reads it by HTTP range requests (the zip directory, three tables, one small
   file per section) and snapshots a JSON bundle per slice. This works but is a workaround: the toolkit
   has no ranged get (the ingester's `CaZip` copies the Fetcher's 429 backoff and refusal handling), and
   the monthly drift run GETs the whole zip once per entry and cannot compare it with a slice baseline.
3. **List markers drawn by CSS.** The Secretary of State's stylesheet (`www-specific.css`) sets
   `list-style:none!important` on the regulation lists and draws `(a)`, `(1)`, `(A)`, `(i)` with
   `::before`; the State Administrative Manual page uses inline `list-style-type`, including `lower-latin`
   and compound values such as `upper-roman; margin-left: 40px`. A parser that guesses falls back to
   `1.` silently; the first pass did, for 52 items of SAM chapter 4900. The ingester now maps the classes
   and styles it knows and raises on one it does not.
4. **A chapter title that the page does not print.** The SAM chapter view prints no chapter title, so the
   seed title cannot be checked against the bytes; a fixture of the manual's contents page
   (`tests/fixtures/sam-toc.html`) is what the test compares seed titles to.
5. **Executive orders.** The Governor's live site refuses the Fetcher, but the Governor's archive site
   (`www.archive.gov.ca.gov`) answers it and prints Executive Order B-34-15 in full in a press-release
   page, so that one order is a document and the rest are in the left-out record. The CDT page that
   lists the orders prints no per-order link.
6. **A second table on the same page.** The Technology Letters page also holds the Information Technology
   Policy Letters table (31 rows, 20 Active). A reader of the page's first table does not see it.

## Does the pattern scale?

For a state whose official host answers the Fetcher (Oregon, Washington, Colorado), yes. For a state
whose policy library sits behind a managed challenge, the corpus is a seed list of stubs plus whatever the
state's other official hosts serve; the quantity of full text is set by the hosts' access policy, not by
the ingester. Toolkit features that would change this: a ranged get on `Fetcher`, and a recheck mode for
sliced sources (see the issue text in the PR description).
