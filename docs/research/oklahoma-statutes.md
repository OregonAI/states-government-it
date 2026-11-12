# Oklahoma statutes: why the eight statute entries are stubs

Measured 2026-11-12 through the toolkit Fetcher.

**OSCN** (`oscn.net`, the Oklahoma State Courts Network's "Oklahoma Statutes Citationized", the host OMES's own pages link): one page per
section (`DeliverDocument.asp?CiteID=...`). The first request answered HTTP 200 (15,232 bytes, section 35.1). The next 66, made in one run
two seconds apart, and a repeat a few minutes later all answered HTTP 201 with 2,309 bytes: a page titled "OSCN Turnstile" (a Cloudflare
Turnstile form). That is a challenge. It was not solved and no other route to the same pages was tried. The index pages
(`index.asp?ftdb=STOKST62&level=1`, 234,548 bytes; Title 74, 606,535 bytes) answered 200 and were read for headings.
Its robots.txt is `Disallow: /` for every agent (`docs/spec.md` sets robots aside for the pilot).

**The Legislature** (`oklegislature.gov`): one PDF per title, `OK_Statutes/CompleteTitles/os62.pdf` (2,798,279 bytes, 687 pages, created
2025-12-30) and `os74.pdf` (5,271,337 bytes, 1,289 pages). Its index says "last updated on November 18th, 2025", so a section amended in the 2026
session is not in it (OSCN's index lists second versions, CiteIDs 553xxx, for 34.6, 34.11.1, 34.32, 35.9 and 36, which were not compared; Title 74
section 13002 is in OSCN's index and not in the PDF). The text is clean: each section starts with a line `§62-35.1. Heading`, the page footer
`Oklahoma Statutes - Title 62. Public Finance   Page 146` falls mid-section, and the contents (the first pages) wrap entries so that
only the last line carries dot leaders.

**What was built and not kept.** A state-module `snapshot` hook that fetches the title once and keeps the pages from the one printing the first
heading to the one printing the next (pages cut with `gs -sDEVICE=pdfwrite -dShowAnnots=false`: `pdfseparate` keeps every font whole,
450 KB a page; the words match the source pages, the indentation of a few lines differs by a space), with tests on real pages 1-2 and 145-158 of
Title 62. The core of it (the org squash-merges, so the branch history will not survive) is below. It cannot be seeded as it stands.

One shared change blocks the statute entries: `src/check_seed_list.py` accepts a `slice` only in the Colorado (article, part) and California shapes, so
`slice: {start, end_before}` fails the gate. The two other obstacles first listed here (duplicate urls, and a drift-hash mismatch) apply
only to the cut-pages design that was tried; they do not apply to Colorado's pattern, which the check already supports: the whole title file is
the snapshot (so the drift hash matches what the url serves), the slice is applied in the state module's `to_text` hook, and the check
allows one url under different slices (`(url, slice)` is the unit that must be unique).

**Shared change that would unblock them:** allow an Oklahoma title-PDF slice shape in `src/check_seed_list.py`, for example
`{section_start, section_end_before}` (printed headings such as `34.11.1` and `35.9`); the state module would then slice the
whole-title snapshot in `to_text`, as Colorado does. The cut-pages code below would not be needed in that form; its heading-finding logic
(contents pages skipped, headings starting a line) is what the `to_text` slice would reuse.

**Currency.** The Legislature's December 2025 PDF (created 2025-12-30; the index says "last updated on November 18th, 2025") predates the
2026 session amendments, so even with the slice shape a section would need a currency check against OSCN's second versions.

**Ranges** (from the Legislature's PDF headings and OMES's own pages): 62 O.S. 34.11.1 to 34.33 (the PDF prints 34.11.1.1 and 34.11.1.2 before 34.11.1),
35.1 to 35.9, 34.202 to 34.210, 34.43, 36, 41.5a-4; 74 O.S. 3106.3 to 3106.4, 3113.1.

**The slice, as built** (tests cut real pages 1-2 and 145-158 of the Title 62 PDF; the snapshot hook fetched the title once and wrote this to `<id>.pdf`):

```python
def _page_texts(raw: bytes) -> list[str]:
    out = subprocess.run(["pdftotext", "-layout", "-", "-"], input=raw, capture_output=True, check=True)
    pages = out.stdout.decode("utf-8", "replace").split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    return pages


def _heading_page(pages: list[str], heading: str, after: int = 0) -> int | None:
    """1-based number of the first page at or after `after` whose lines include one that begins with `heading`
    on a page that is not part of the contents (five or more lines with dot leaders)."""
    for n in range(max(after, 1), len(pages) + 1):
        if sum("...." in line for line in pages[n - 1].splitlines()) >= 5:
            continue                                  # a contents page: its entries wrap, and only the last line has leaders
        for line in pages[n - 1].splitlines():
            if line.lstrip().startswith(heading) and "...." not in line:
                return n
    return None


def slice_statute_pdf(raw: bytes, start: str, end_before: str) -> bytes:
    """The pages of a title PDF from the page that prints the heading `start` to the page that prints `end_before`."""
    pages = _page_texts(raw)
    first = _heading_page(pages, start)
    if first is None:
        raise ValueError(f"heading {start} is not in the title PDF (the layout changed, or the section was renumbered)")
    last = _heading_page(pages, end_before, first)
    if last is None:
        raise ValueError(f"heading {end_before} does not follow {start} in the title PDF")
    with tempfile.TemporaryDirectory() as d:
        src, dst = Path(d) / "in.pdf", Path(d) / "out.pdf"
        src.write_bytes(raw)
        subprocess.run(["gs", "-q", "-dNOPAUSE", "-dBATCH", "-dSAFER", "-dShowAnnots=false", "-sDEVICE=pdfwrite",
                        f"-dFirstPage={first}", f"-dLastPage={last}", f"-sOutputFile={dst}", str(src)],
                       check=True, capture_output=True)
        return dst.read_bytes()
```
