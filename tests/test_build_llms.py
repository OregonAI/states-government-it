"""Seam: src.build_llms. llms.txt is generated from _meta/templates/llms.txt: the states it names are the
files in _meta/sources/, so adding a state does not edit it by hand."""
import subprocess
import sys
from pathlib import Path

from src import build_llms as bl

ROOT = Path(__file__).resolve().parent.parent


def test_the_states_token_becomes_the_display_names_of_the_seed_files_in_order(tmp_path):
    for s in ("washington", "new-york", "oregon"):
        (tmp_path / f"{s}.yml").write_text("sources: []\n")
    (tmp_path / "README.md").write_text("not a state")
    assert bl.state_names(tmp_path) == ["New York", "Oregon", "Washington"]
    assert bl.render("held: @@STATES@@.\n", tmp_path) == "held: New York, Oregon, Washington.\n"


def test_a_template_without_the_token_is_refused_so_the_check_cannot_pass_vacuously(tmp_path):
    (tmp_path / "oregon.yml").write_text("sources: []\n")
    try:
        bl.render("no token here\n", tmp_path)
    except ValueError as e:
        assert "@@STATES@@" in str(e)
    else:
        raise AssertionError("expected ValueError")


def test_the_repos_llms_txt_is_current_and_names_every_state():
    r = subprocess.run([sys.executable, "-m", "src.build_llms", "--check"], cwd=ROOT,
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout
    text = (ROOT / "llms.txt").read_text()
    for s in ("Oregon", "Washington", "California", "Colorado"):
        assert s in text
