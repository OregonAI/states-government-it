#!/usr/bin/env python3
"""Build the [Unreleased] section of CHANGELOG.md from one fragment file per change in changelog.d/.

  python3 src/build_changelog.py           # rewrite CHANGELOG.md
  python3 src/build_changelog.py --check   # exit 1 if CHANGELOG.md is stale

A fragment is `changelog.d/<state-or-shared>-<slug>.md`: a first line `type: <Type>` (one of the types
the changelog header names), a blank line, then the entry's text (it becomes one bullet). Fragments are
new files, so two branches adding states never edit the same lines; the generated CHANGELOG.md is rebuilt
by `scripts/regen.sh` after a rebase. Everything from the first `## [` heading after `## [Unreleased]`
(released sections) is kept as it is.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TYPES = ("Added", "Source-Updated", "Superseded", "Repealed", "Removed", "Verified", "Fixed", "Security")
UNRELEASED = "## [Unreleased]"


def read_fragment(path: Path) -> tuple[str, str]:
    first, _, rest = path.read_text(encoding="utf-8").partition("\n")
    if not first.startswith("type:"):
        raise ValueError(f"{path.name}: the first line must be `type: <Type>`")
    type_, body = first[len("type:"):].strip(), rest.strip()
    if type_ not in TYPES:
        raise ValueError(f"{path.name}: type {type_!r} is not one of {', '.join(TYPES)}")
    if not body:
        raise ValueError(f"{path.name}: empty entry text")
    return type_, body


def render(existing: str, fragments: Path) -> str:
    """CHANGELOG.md's text with its [Unreleased] section rebuilt from the fragments."""
    start = existing.find(UNRELEASED)
    if start < 0:
        raise ValueError(f"CHANGELOG.md has no {UNRELEASED} heading")
    nxt = existing.find("\n## [", start + len(UNRELEASED))
    rest = existing[nxt + 1:] if nxt >= 0 else ""
    by_type: dict[str, list[str]] = {}
    for path in sorted(Path(fragments).glob("*.md")):
        type_, body = read_fragment(path)
        by_type.setdefault(type_, []).append(body)
    out = existing[:start] + UNRELEASED + "\n"
    for type_ in TYPES:
        if type_ in by_type:
            out += f"\n### {type_}\n" + "".join(f"- {b}\n" for b in by_type[type_])
    return out + (("\n" + rest) if rest else "")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="exit 1 if CHANGELOG.md is stale")
    ap.add_argument("--fragments", default=str(ROOT / "changelog.d"))
    ap.add_argument("--file", default=str(ROOT / "CHANGELOG.md"))
    a = ap.parse_args()
    log = Path(a.file)
    try:
        text = render(log.read_text(encoding="utf-8"), Path(a.fragments))
    except ValueError as e:
        print(e)
        return 1
    if a.check:
        if log.read_text(encoding="utf-8") != text:
            print(f"{log.name} is stale: run scripts/regen.sh")
            return 1
        print(f"{log.name} is current.")
        return 0
    log.write_text(text, encoding="utf-8")
    print(f"wrote {log.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
