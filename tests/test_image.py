"""Seam: what the deployed image is built from, and whether a server started from only that
answers. platform-deploy builds the image from a shallow clone with `docker build`, so the build
context is the working tree minus what `.dockerignore` removes. Docker is not available in CI or
on a developer machine here, so these tests rebuild that context by hand from the real
`.dockerignore` and run the real toolkit server code over it.

What each test catches: a mount path that does not match the tunnel's (every request 404s), a
`.dockerignore` that stops excluding the ~700 MB of raw snapshots or starts excluding `.git`
(which the FTS cache key needs), and a server code path that comes to need a file the image
leaves out. What they do not catch: anything docker itself does (the build, the healthcheck).
"""
import fnmatch
import re
import shutil
from pathlib import Path

import pytest
import yaml
from corpus_toolkit import config as config_mod
from corpus_toolkit.mcp.framework import CorpusFramework

ROOT = Path(__file__).resolve().parent.parent
CORPUS_ID = "states-government-it"
# The path the tunnel routes. Written out, not derived from corpus.yml, so that a rename of the
# corpus id cannot silently change what is asserted: platform-deploy's ingress rule and
# healthcheck name this literal.
MOUNT = "/states-government-it/mcp"


def dockerignore_patterns() -> list[str]:
    lines = (ROOT / ".dockerignore").read_text(encoding="utf-8").splitlines()
    return [ln.strip() for ln in lines if ln.strip() and not ln.strip().startswith("#")]


def excluded(rel: str, patterns: list[str]) -> bool:
    """Docker's rule, for the plain patterns this file uses: a directory pattern
    (`dir/`) removes everything under it; a glob matches the whole relative path or any
    path component sequence from the root. Negations are refused rather than guessed at."""
    for pat in patterns:
        assert not pat.startswith("!"), f".dockerignore negation {pat!r}: extend this reader"
        bare = pat.rstrip("/")
        if rel == bare or rel.startswith(bare + "/") or fnmatch.fnmatch(rel, bare):
            return True
        # a bare name like `__pycache__/` or `.venv/` matches at any depth in .gitignore style,
        # but docker anchors at the context root; only the root form is honoured here.
    return False


def build_context(dest: Path) -> Path:
    """Copy the working tree to `dest` the way `docker build` would see it, minus `.git`
    (the image keeps it; the server only shells out to it, and it is 479 MB)."""
    patterns = dockerignore_patterns()

    def ignore(directory, names):
        base = Path(directory).relative_to(ROOT)
        return [
            n for n in names
            if n == ".git" or n == ".venv"
            or excluded(str(base / n) if str(base) != "." else n, patterns)
        ]

    shutil.copytree(ROOT, dest, ignore=ignore)
    return dest


def test_dockerfile_mounts_at_the_path_the_tunnel_routes():
    text = (ROOT / "Dockerfile").read_text(encoding="utf-8")
    cmd = text[text.rindex("\nCMD"):]
    assert re.search(r'"--path",\s*"' + re.escape(MOUNT) + '"', cmd), cmd
    assert re.search(r'"--public-hostname",\s*"oregonai.morficflux.com"', cmd), cmd


def test_corpus_id_is_the_mount_prefix():
    cfg = yaml.safe_load((ROOT / "_meta" / "corpus.yml").read_text(encoding="utf-8"))
    assert cfg["corpus"]["id"] == CORPUS_ID
    assert MOUNT == f"/{cfg['corpus']['id']}/mcp"


def test_dockerignore_drops_the_heavy_inputs_the_server_never_opens():
    patterns = dockerignore_patterns()
    assert excluded("_meta/snapshots/x.pdf", patterns), "raw snapshots must stay out of the image"
    assert excluded("_meta/.cache/fts.db", patterns), "a host-built index has the wrong cache key"
    assert excluded("_meta/embeddings/vectors.i8.npy", patterns), "vectors are bind-mounted"


def test_dockerignore_keeps_git_and_the_content():
    patterns = dockerignore_patterns()
    # `.git` is a RUNTIME dependency: the FTS cache key is HEAD plus `git status --porcelain`.
    assert not excluded(".git", patterns) and not excluded(".git/HEAD", patterns)
    for kept in ("_meta/corpus.yml", "_meta/graph.json", "statutes/oregon", "requirements.txt"):
        assert not excluded(kept, patterns), kept


def test_embeddings_mount_does_not_dirty_the_tree():
    """The platform bind-mounts the vectors at _meta/embeddings. If git does not ignore that
    path, populating it changes `git status --porcelain`, so the FTS cache key differs from the
    one stamped at build and the index is rebuilt on the first request."""
    ignored = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    assert "_meta/embeddings/" in [ln.strip() for ln in ignored]


@pytest.fixture(scope="module")
def image_tree(tmp_path_factory):
    return build_context(tmp_path_factory.mktemp("image") / "repo")


def test_server_answers_from_the_image_context_alone(image_tree):
    """No `_meta/snapshots`, no prebuilt index: the framework must build its index from the
    content roots and serve search and full text from it."""
    assert not (image_tree / "_meta" / "snapshots").exists()
    fw = CorpusFramework(config_mod.load(image_tree / "_meta" / "corpus.yml"))
    fw.ensure_index()
    on_disk = sum(1 for root in ("statutes", "rules", "executive-orders", "policies", "standards")
                  for _ in (image_tree / root).rglob("*.md"))
    assert on_disk > 2000
    # the framework's own count of what it indexed, through the same query the platform's
    # healthcheck runs against fts.db
    import sqlite3
    db = sqlite3.connect(f"file:{image_tree}/_meta/.cache/fts.db?mode=ro", uri=True)
    assert db.execute("select count(*) from docs").fetchone()[0] == on_disk
    hits = fw.search_corpus("information technology", limit=3)
    assert hits, hits
    doc = fw.get_document(hits[0]["id"], part="auto")
    assert doc and not doc.get("error"), doc
    assert fw.corpus_overview()
