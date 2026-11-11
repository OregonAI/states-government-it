# State Government IT Governance

> ## NON-AUTHORITATIVE: AI-friendly reference only
> Curated copies, not official text. Always verify at the official source linked in
> each document. See [DISCLAIMER.md](DISCLAIMER.md).

How state governments regulate their own information technology, including government
use of AI, as full text an AI agent can search and compare across states. Pilot states:
Oregon, Washington, California, Colorado.

Part of the OregonAI civic corpus platform, built on
[corpus-toolkit](https://github.com/OregonAI/corpus-toolkit). It is also the proof of a
repeatable pattern: a second policy domain is a new repo with its own
[`_meta/domain.yml`](_meta/domain.yml) and seed list, and no new shared code.

Status: scaffold. No documents yet.

| Entry point | For |
|---|---|
| [docs/spec.md](docs/spec.md) | What is being built and why |
| [_meta/domain.yml](_meta/domain.yml) | Scope, states and tag vocabulary |
| [CLAUDE.md](CLAUDE.md) | Rules for agents working here |
| [llms.txt](llms.txt) | Machine-readable index |
| [STATUS.md](STATUS.md) | Generated health: freshness, coverage, drift |
| [docs/research/](docs/research/) | Prior art, source availability, domain taxonomy |

## Local setup

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
scripts/gates.sh
```

## License
Content (curated government material): CC0-1.0. Tooling, structure, metadata: MIT.
See [LICENSE](LICENSE).
