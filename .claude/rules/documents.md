---
paths:
  - "statutes/**"
  - "rules/**"
  - "executive-orders/**"
  - "policies/**"
  - "standards/**"
---

# Documents

One instrument per file at `<type>/<state>/<id>.md`, written by the ingester from an
approved seed entry. Start from `_meta/templates/document.md`.

- **`## Full text` is verbatim** from the committed snapshot, complete, in source order.
  The provenance gate diffs it. Your own words go only in `## At a glance`,
  `## Curator notes` and `## Cross-references`.
- **Regenerate, don't hand-edit.** To change a document's text, fix the ingester and run
  it again, so the text and its hash stay tied to the snapshot.
- **`jurisdiction` is the state**, from `_meta/domain.yml`, and matches the folder.
  `tags` come from the same file. `doc_type` matches the content folder.
- **`source_url` is the official page** the text was fetched from. `source_sha256` comes
  from `corpus_toolkit.repo.hash_snapshot`.
- **Dates are transcribed** from the source. A date the source does not print stays empty.
- **A stub has no document file yet.** It lives only in the seed list. The toolkit
  (v1.36.4) rejects a policy without a snapshot and verbatim text; stub documents arrive
  with the toolkit's stub support (see the `coverage` issue in `OregonAI/corpus-toolkit`).
- **Scanned PDFs** go through the two-engine OCR procedure in the corpus-template
  `AGENTS.md` ("OCR" section); record the engines and agreement in `conversion_notes`.
- The file name equals `id`: lowercase letters, digits and hyphens.
- Only documents live in these folders: every `.md` here is validated as one.
