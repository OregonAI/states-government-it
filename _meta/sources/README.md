# _meta/sources

Seed list: one `<state>.yml` per state (see `_meta/CLAUDE.md`). The header below is the
key reference the single manifest carried before it was split.

```
# Every upstream source this corpus consumes. Human-approved via PR BEFORE any
# ingestion (review gate #1).
#
# WHICH KEYS THE TOOLKIT ACTUALLY READS (corpus_toolkit/sources/changes.py):
#   url     REQUIRED. Missing it raises KeyError mid-run, not a clean error.
#   format  Strongly recommended. Without it the format is INFERRED FROM THE URL
#           EXTENSION — and an extensionless URL that actually serves a PDF is
#           inferred as html, so drift detection runs an HTML-to-text converter
#           over PDF bytes and reports a change EVERY RUN, FOREVER. Declare it
#           whenever the URL does not end in a real extension.
#   id      Used to name the snapshot and report which source drifted.
#
# Everything else below is for humans and for this repo's own ingester; the
# toolkit ignores it. That is fine — record what your reviewers need.
#
# sources:
#   - id: ""                # -> _meta/snapshots/<id>.<format>
#     url: ""               # REQUIRED
#     format: pdf           # html | pdf | json | xlsx | ... declare it explicitly
#     citation: ""
#     title: ""
#     doc_type: ""
#     recheck: monthly | quarterly | annual | biennial
#     sha256: ""            # filled at first fetch
#     why_relevant: ""
#     references_out: []
#     identity_text: ""     # optional, PDF policies/standards only: a phrase the document itself
#                           # prints, which the ingester requires before it writes anything. Used
#                           # when the printed title differs from `title` and the policy number is
#                           # not printed. Without it: the citation's policy number, else the title.
```
