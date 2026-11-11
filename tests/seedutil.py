"""A temporary corpus's seed directory: `_meta/sources/<state>.yml`, one file per state, as in the real one."""
from pathlib import Path

import yaml


def write_seed(root: Path, sources: list) -> None:
    """Write `sources` into `<root>/_meta/sources/<jurisdiction>.yml`, one file per state."""
    seed = Path(root) / "_meta" / "sources"
    seed.mkdir(parents=True, exist_ok=True)
    by_state: dict = {}
    for s in sources:
        by_state.setdefault(s["jurisdiction"], []).append(s)
    for state, entries in by_state.items():
        (seed / f"{state}.yml").write_text(yaml.safe_dump({"sources": entries}))


def make_corpus(tmp_path: Path, sources: list):
    """A copy of this corpus's configuration in a temp repo (with `sources` as its seed list), so a test
    never touches the real one."""
    import shutil

    from corpus_toolkit import config as config_mod

    root = Path(__file__).resolve().parent.parent
    (tmp_path / "_meta").mkdir(exist_ok=True)
    shutil.copy(root / "_meta" / "corpus.yml", tmp_path / "_meta" / "corpus.yml")
    write_seed(tmp_path, sources)
    return config_mod.load(tmp_path / "_meta" / "corpus.yml")


def make_fetcher(cfg, routes, calls=None):
    """A Fetcher whose network is `routes` ({url: (status, bytes)}), with no rate limit and no sleeping."""
    import httpx

    from corpus_toolkit.sources.fetch import Fetcher

    def handler(request):
        if calls is not None:
            calls.append(str(request.url))
        status, body = routes.get(str(request.url), (404, b""))
        return httpx.Response(status, content=body)
    return Fetcher(cfg, min_interval=0, transport=httpx.MockTransport(handler), sleep=lambda s: None)
