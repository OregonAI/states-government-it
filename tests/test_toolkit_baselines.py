"""Seam: the pinned toolkit's writers of a source's `sha256` baseline, run over a copy of the real seed
directory. The toolkit reads a directory of group files and edits, by line, the file that declares an id
(`record_snapshot` at ingest, `corpus-detect-changes` after a drift run). Splitting the seed list per state is
only safe if those edits land on the right entry in the right file and move nothing else, the left-out record
included."""
import difflib
import shutil
from pathlib import Path

import pytest
import yaml
from corpus_toolkit import config as config_mod
from corpus_toolkit.sources import changes, manifest

from src import check_seed_list

ROOT = Path(__file__).resolve().parent.parent
NEW = "f" * 64


@pytest.fixture
def copy(tmp_path):
    """The real corpus.yml and a copy of the real seed directory, in a temp repo."""
    (tmp_path / "_meta").mkdir()
    shutil.copy(ROOT / "_meta" / "corpus.yml", tmp_path / "_meta" / "corpus.yml")
    shutil.copytree(ROOT / "_meta" / "sources", tmp_path / "_meta" / "sources")
    return config_mod.load(tmp_path / "_meta" / "corpus.yml"), tmp_path / "_meta" / "sources"


def snapshot(seed: Path) -> dict:
    return {p.name: p.read_bytes() for p in sorted(seed.glob("*.yml"))}


def changed_lines(before: bytes, after: bytes) -> list[str]:
    d = difflib.unified_diff(before.decode().splitlines(), after.decode().splitlines(), lineterm="", n=0)
    return [l for l in d if l[:1] in "+-" and l[:3] not in ("+++", "---")]


def entry_of(seed: Path, state: str, with_sha: bool) -> str:
    sources = yaml.safe_load((seed / f"{state}.yml").read_text())["sources"]
    return next(s["id"] for s in sources if bool(s.get("sha256")) == with_sha)


def test_the_toolkit_finds_every_state_file_as_a_group_of_its_own(copy):
    cfg, seed = copy
    groups = {g["group"]: len(g["sources"]) for g in config_mod.load_source_manifest_groups(cfg)}
    assert groups == {p.stem: len(yaml.safe_load(p.read_text())["sources"]) for p in seed.glob("*.yml")}
    assert groups and all(n > 0 for n in groups.values())       # no state count here: a new state adds a file


@pytest.mark.parametrize("state", ["oregon", "washington", "california", "colorado"])
def test_an_ingest_baseline_edits_one_line_in_the_states_own_file_and_nothing_else(copy, state):
    cfg, seed = copy
    before = snapshot(seed)
    sid = entry_of(seed, state, with_sha=True)
    assert manifest.record_baseline(cfg, sid, NEW) == seed / f"{state}.yml"
    after = snapshot(seed)
    assert {n for n in before if before[n] != after[n]} == {f"{state}.yml"}
    edits = changed_lines(before[f"{state}.yml"], after[f"{state}.yml"])
    assert len(edits) == 2 and NEW in edits[1] and "sha256:" in edits[0]
    got = yaml.safe_load(after[f"{state}.yml"])
    assert next(s for s in got["sources"] if s["id"] == sid)["sha256"] == NEW
    assert got["left_out"] == yaml.safe_load(before[f"{state}.yml"])["left_out"]
    _, errors = check_seed_list.check_seed_dir(seed, {**yaml.safe_load((ROOT / "_meta/domain.yml").read_text())})
    assert errors == []


def test_an_entry_with_no_baseline_gets_one_inserted_after_its_id(copy):
    cfg, seed = copy
    state = next((s for s in ("oregon", "washington", "california", "colorado")
                  if any(not e.get("sha256") for e in yaml.safe_load((seed / f"{s}.yml").read_text())["sources"])), None)
    if state is None:
        pytest.skip("every entry has a baseline")
    before = snapshot(seed)
    sid = entry_of(seed, state, with_sha=False)
    manifest.record_baseline(cfg, sid, NEW)
    edits = changed_lines(before[f"{state}.yml"], snapshot(seed)[f"{state}.yml"])
    assert len(edits) == 1 and edits[0].startswith("+") and NEW in edits[0]


def test_a_drift_run_writes_baselines_in_several_states_without_touching_the_rest(copy):
    cfg, seed = copy
    before = snapshot(seed)
    ids = {s: entry_of(seed, s, with_sha=True) for s in ("oregon", "colorado")}
    fetched = {(s, sid): NEW for s, sid in ids.items()}
    tally = changes._record_baselines(cfg, fetched, set(fetched), "refresh")
    assert tally["written"] == 2 and not tally["refused"]
    assert sorted(p.name for p in tally["files"]) == ["colorado.yml", "oregon.yml"]
    after = snapshot(seed)
    assert {n for n in before if before[n] != after[n]} == {"colorado.yml", "oregon.yml"}
    for state, sid in ids.items():
        assert len(changed_lines(before[f"{state}.yml"], after[f"{state}.yml"])) == 2
        assert yaml.safe_load(after[f"{state}.yml"])["left_out"] == yaml.safe_load(before[f"{state}.yml"])["left_out"]


def test_an_id_declared_in_two_state_files_is_refused_not_guessed(copy):
    cfg, seed = copy
    text = (seed / "oregon.yml").read_text()
    other = yaml.safe_load((seed / "washington.yml").read_text())["sources"][0]["id"]
    (seed / "oregon.yml").write_text(text.replace(entry_of(seed, "oregon", True), other, 1))
    with pytest.raises(manifest.BaselineRefused, match="declared 2 times"):
        manifest.record_baseline(cfg, other, NEW)
