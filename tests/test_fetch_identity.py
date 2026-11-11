"""Seam: src.ingest.make_fetcher, the one way this corpus builds its Fetcher. Every request must say who we
are: the product token OregonAI-CivicCorpus/<version> and no browser engine or platform token (toolkit
ADR-0019; Colorado's firewall answers 403 to anything else). The version token comes from the installed package
metadata, so under PYTHONPATH=toolkit v1.37.0 it still reads the pinned 1.36.4 (docs/research/09)."""
import inspect
import re

import httpx
import pytest
from corpus_toolkit.sources.fetch import Fetcher

from src import ingest as ing

_BROWSER = re.compile(r"Chrome|Chromium|Safari|Firefox|Edg/|AppleWebKit|Gecko|Windows NT|Macintosh|X11|Linux x86")


def names_us(ua) -> bool:
    """The shipped identity says who we are: the product token OregonAI-CivicCorpus/<version> is in it
    (v1.36.4 starts with it; v1.37.0, ADR-0019, wraps it as 'Mozilla/5.0 (compatible; ...)'), and it
    carries no browser engine or platform token."""
    return bool(ua) and bool(re.search(r"(?:^|[\s(;])OregonAI-CivicCorpus/\d", ua)) and not _BROWSER.search(ua)


@pytest.mark.parametrize("ua", [
    "OregonAI-CivicCorpus/1.36.4 (+https://github.com/OregonAI/corpus-toolkit; public-records archival)",
    "Mozilla/5.0 (compatible; OregonAI-CivicCorpus/1.37.0; +https://github.com/OregonAI/states-government-it)",
])
def test_both_toolkit_identities_name_us(ua):
    assert names_us(ua)


@pytest.mark.parametrize("ua", [
    None, "",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; NotOregonAI-CivicCorpus/1.0)",
    "Mozilla/5.0 (Windows NT 10.0) Chrome/126.0 OregonAI-CivicCorpus/1.37.0",
    "python-httpx/0.27",
])
def test_a_browser_string_or_one_without_our_name_is_not_our_identity(ua):
    assert not names_us(ua)


class _Mocked(Fetcher):
    """The toolkit's Fetcher with the network faked and every request recorded. Its __init__ signature is the
    real one, so src.ingest.make_fetcher feature-detects `curl_on_challenge` here exactly as it does live."""
    sent: list = []

    def __init__(self, config, **kw):
        def handler(request):
            _Mocked.sent.append(dict(request.headers))
            return httpx.Response(200, content=b"<html><body>ok</body></html>", headers={"Content-Type": "text/html"})
        super().__init__(config, **{"min_interval": 0, "transport": httpx.MockTransport(handler),
                                    "sleep": lambda s: None, **kw})

    __init__.__signature__ = inspect.signature(Fetcher.__init__)


def test_the_fetcher_the_corpus_builds_sends_our_identity_and_nothing_that_overrides_it(tmp_path):
    """Through src.ingest.make_fetcher, not a Fetcher built by the test: if make_fetcher ever passed a
    user_agent= or extra headers, the request would stop naming us (or gain a browser token) and this fails."""
    _Mocked.sent = []
    with ing.make_fetcher(ing.CONFIG, cls=_Mocked) as f:
        f.snapshot("https://oit.colorado.gov/standards-policies-guides/technical-standards", tmp_path / "page.html")
    assert _Mocked.sent
    for headers in _Mocked.sent:
        assert names_us(headers.get("user-agent"))
        assert not {"cookie", "sec-fetch-mode", "sec-ch-ua", "referer", "origin"} & set(headers)
