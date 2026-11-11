"""Seam: src.build_changelog. CHANGELOG.md's [Unreleased] section is generated from one fragment file per
change in changelog.d/, so two state PRs never edit the same lines."""
import subprocess
import sys
from pathlib import Path

import pytest

from src import build_changelog as bc

ROOT = Path(__file__).resolve().parent.parent
HEAD = "# Changelog\n\nIntro.\n\n"


def frag(d, name, type_, body):
    (d / name).write_text(f"type: {type_}\n\n{body}\n")


def test_unreleased_lists_each_fragment_under_its_type_in_the_documented_type_order(tmp_path):
    frag(tmp_path, "colorado-a.md", "Fixed", "Colorado fix.")
    frag(tmp_path, "washington-a.md", "Added", "Washington added 3 documents.")
    frag(tmp_path, "colorado-b.md", "Added", "Colorado added 2 documents.")
    out = bc.render(HEAD + "## [Unreleased]\n\nstale\n", tmp_path)
    assert out == (HEAD + "## [Unreleased]\n\n### Added\n- Colorado added 2 documents.\n"
                   "- Washington added 3 documents.\n\n### Fixed\n- Colorado fix.\n")


def test_a_released_section_below_unreleased_is_kept_untouched(tmp_path):
    frag(tmp_path, "a.md", "Added", "New.")
    old = HEAD + "## [Unreleased]\n\nstale\n\n## [0.1.0] - 2026-11-01\n\n### Added\n- Old.\n"
    out = bc.render(old, tmp_path)
    assert out.endswith("## [0.1.0] - 2026-11-01\n\n### Added\n- Old.\n")
    assert "stale" not in out and "- New." in out


@pytest.mark.parametrize("text, why", [
    ("Added\n\nbody\n", "type"),                 # no `type:` line
    ("type: Wishful\n\nbody\n", "Wishful"),      # a type the changelog does not define
    ("type: Added\n\n\n", "empty"),              # no text
])
def test_a_malformed_fragment_is_an_error_naming_the_file(tmp_path, text, why):
    (tmp_path / "bad.md").write_text(text)
    with pytest.raises(ValueError, match=f"bad.md.*{why}|{why}.*bad.md"):
        bc.render(HEAD + "## [Unreleased]\n", tmp_path)


def test_check_fails_when_the_changelog_is_stale_and_passes_when_current(tmp_path):
    (tmp_path / "frags").mkdir()
    frag(tmp_path / "frags", "a.md", "Added", "New.")
    log = tmp_path / "CHANGELOG.md"
    log.write_text(HEAD + "## [Unreleased]\n")
    cmd = [sys.executable, "-m", "src.build_changelog", "--fragments", str(tmp_path / "frags"), "--file", str(log)]
    r = subprocess.run(cmd + ["--check"], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 1 and "stale" in r.stdout
    assert subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True).returncode == 0
    r = subprocess.run(cmd + ["--check"], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout


def test_the_repos_own_changelog_is_current():
    r = subprocess.run([sys.executable, "-m", "src.build_changelog", "--check"], cwd=ROOT,
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout
