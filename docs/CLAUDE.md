# docs: decisions and research

- **`spec.md` is the record of what the owner decided.** Change it when the owner decides
  something, in the same PR as the work that depends on it. An open question goes in its
  "Open" section until answered.
- **`research/` files are dated findings.** Every claim cites the primary source it came
  from; a claim you could not confirm is marked UNVERIFIED. Add a new numbered file for
  new research and leave earlier files as written. A note about one state is
  `research/<state>-<slug>.md`, unnumbered, so parallel state PRs never take the same number.
- **Work items are GitHub issues**, not files here.
- `agents/` configures the mattpocock-skills workflow (issue tracker, labels, domain docs).
