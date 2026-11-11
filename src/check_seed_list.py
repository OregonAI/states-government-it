#!/usr/bin/env python3
"""Check the seed list (_meta/source-manifest.yml) against the domain pack (_meta/domain.yml).

  python3 src/check_seed_list.py --check     # exit 1 and list every problem

Rules: a key written twice anywhere in the file (e.g. two `sources:` blocks) fails; every entry has the required fields, non-empty; `jurisdiction`, `doc_type` and
`tags` take only values from domain.yml; `format` is declared from a known set; ids and
urls are unique; a stub carries `stub_reason`; `stub` and `watch_only` are true booleans
and never both. An empty list fails: a missing or emptied manifest must not pass.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ("id", "url", "format", "citation", "title", "doc_type", "jurisdiction", "tags",
            "why_relevant")
FORMATS = {"html", "pdf", "docx", "xlsx", "json", "xml", "txt"}


class DuplicateKeyError(ValueError):
    """A mapping key written twice. PyYAML keeps the last one silently, which drops every
    entry under an earlier `sources:` block while the check still passes."""


class _UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        seen = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=True)
            if key in seen:
                raise DuplicateKeyError(
                    f"duplicate key {key!r} at line {key_node.start_mark.line + 1}")
            seen.add(key)
        return super().construct_mapping(node, deep)


def load_yaml_text(text: str):
    """yaml.safe_load, except that a duplicate mapping key at any level raises."""
    return yaml.load(text, Loader=_UniqueKeyLoader)  # noqa: S506 -- SafeLoader subclass


def _blank(v) -> bool:
    return v is None or (isinstance(v, (str, list)) and not (v.strip() if isinstance(v, str) else v))


def check(manifest: dict, domain: dict) -> list[str]:
    sources = (manifest or {}).get("sources") or []
    if not sources:
        return ["no entries in sources: an empty seed list cannot pass"]
    states, types = set(domain["states"]), set(domain["instrument_types"])
    tags = set(domain["tags"])
    errors: list[str] = []
    ids: set = set()
    urls: set = set()
    for i, e in enumerate(sources):
        if not isinstance(e, dict):
            errors.append(f"entry #{i}: not a mapping")
            continue
        eid = e.get("id") or f"#{i}"
        bad = lambda msg: errors.append(f"{eid}: {msg}")  # noqa: E731
        for f in REQUIRED:
            if _blank(e.get(f)):
                bad(f"missing or empty required field {f}")
        if e.get("id") in ids:
            bad("duplicate id")
        ids.add(e.get("id"))
        if e.get("url") in urls:
            bad("duplicate url")
        urls.add(e.get("url"))
        url = e.get("url")
        if isinstance(url, str) and not url.startswith(("http://", "https://")):
            bad(f"url is not http(s): {url}")
        if e.get("format") and e["format"] not in FORMATS:
            bad(f"format {e['format']!r} not one of {sorted(FORMATS)}")
        if e.get("jurisdiction") and e["jurisdiction"] not in states:
            bad(f"jurisdiction {e['jurisdiction']!r} not in domain.yml states")
        if e.get("doc_type") and e["doc_type"] not in types:
            bad(f"doc_type {e['doc_type']!r} not in domain.yml instrument_types")
        t = e.get("tags")
        if isinstance(t, list):
            for x in t:
                if x not in tags:
                    bad(f"tags: {x!r} not in domain.yml tags")
        elif t is not None:
            bad("tags must be a list")
        for flag in ("stub", "watch_only"):
            if flag in e and e[flag] is not True:
                bad(f"{flag} must be true when present (omit it otherwise)")
        if e.get("stub") is True and _blank(e.get("stub_reason")):
            bad("stub: true requires stub_reason")
        if e.get("stub") is True and e.get("watch_only") is True:
            bad("stub and watch_only are exclusive")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="the default; accepted for gates")
    ap.add_argument("--manifest", default=str(ROOT / "_meta" / "source-manifest.yml"))
    ap.add_argument("--domain", default=str(ROOT / "_meta" / "domain.yml"))
    a = ap.parse_args()
    try:
        manifest = load_yaml_text(Path(a.manifest).read_text())
        domain = load_yaml_text(Path(a.domain).read_text())
    except (DuplicateKeyError, yaml.YAMLError) as e:
        print(f"seed list cannot be loaded: {e}")
        return 1
    errors = check(manifest, domain)
    for m in errors:
        print(m)
    if errors:
        print(f"{len(errors)} seed-list problem(s)")
        return 1
    print(f"seed list ok: {len(manifest['sources'])} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
