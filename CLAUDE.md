# states-it-governance

Full-text mirror of how state governments regulate their own IT, including government use
of AI, served to AI agents for cross-state comparison. Non-authoritative: every document
cites its official source. The states held are the files in `_meta/sources/` (listed in `llms.txt`).

- **What and why:** `docs/spec.md`. Scope, states and tags: `_meta/domain.yml`.
- **Work queue:** GitHub issues on `OregonAI/states-it-governance` (`docs/agents/issue-tracker.md`).
- **Folder rules** load when you work there: `_meta/`, `src/`, `docs/`, and
  `.claude/rules/documents.md` for the five content folders.

## Workflow

Seed list approved by the owner → ingest → `scripts/gates.sh` green → PR → owner review.
Branch off `main`, one PR per issue, rebase to update (the org squash-merges). The owner
merges.

**One state = one PR of new files:** `_meta/sources/<state>.yml`, `src/states/<state>.py`,
`tests/<state>/`, `tests/fixtures/<state>/`, the documents and snapshots, `changelog.d/<state>-*.md`.
No shared file is edited. Then run `scripts/regen.sh`: it rebuilds the generated files (`_meta/graph.json`,
`STATUS.md`, `llms.txt`, `CHANGELOG.md`). Commit them last, and after every rebase run it again: it is the whole
resolution of a conflict in any of them (`scripts/regen.sh`, `git add -A`, `git rebase --continue`), and git may
also merge them cleanly into stale content, which `scripts/gates.sh` catches.

## Hard rules

1. **Source or stop.** Every word of a document comes from the fetched official source.
   When a source is unreachable or unparseable, make the entry a stub and say so.
2. **The owner approves the seed list before any fetch.** Nothing enters by crawling.
3. **This repo holds content, not shared code.** A feature another policy domain would
   need belongs in `OregonAI/corpus-toolkit`. Code here is this domain's ingester and checks.
4. **Gates are scripts.** `scripts/gates.sh` is the gate. Report its output as it printed,
   failures included.
5. **Leave `last_verified` and `verified_by` empty.** The owner fills them at review.
6. **Names in mirrored records are public record.** Commit them as published.

## Found a defect? Fix it in the change you are making.

A defect is anything that gives a wrong answer: a check that checks nothing, a documented
command that fails, a stale claim, wrong or incomplete data, a workaround.

Open an issue only when one of these holds:

1. It needs a decision that is the owner's to make. Label it `ready-for-human`.
2. The fix would make this change's diff hard to review.
3. The fix is in a file this change does not touch, or in another repo. File it in the
   repo that owns the fix (toolkit defects go to `OregonAI/corpus-toolkit`).

An issue states what is wrong, how it was found (the command or the data), what it breaks,
what would fix it, and its **trigger**: the condition under which it starts to matter. With
no trigger, write a comment at the site instead. At most two issues per task: more than two
findings is one issue naming the pattern. A review finding fixed in the same change is
already tracked. If you cannot file, hand the owner the issue text in your final message.

## Commands

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt   # once
scripts/gates.sh                                                       # before every commit
```

Commit identity is repo-local (`git config user.email`); keep it.
