# Stack Project of Geometric Measure Theory and Variational Problems

A subject-based mathematical reference built on [Mingchen Xia’s Pome framework](https://github.com/MingchenXia/Pome).

The project covers geometric measure theory, minimal surfaces, min-max theory, the volume spectrum, constant mean curvature surfaces, Willmore geometry, Allen–Cahn and phase transitions, obstacle problems, and mean curvature flows. The first chapter is **Introduction**.

The current draft contains 84 mathematical and editorial entries in 22 sections and 14 chapters, including 17 local proofs and 18 cited theorems whose proofs remain external. Obstacle problems and mean curvature flow currently have introductory formulations and elementary calculations; their deeper theories are planned. No independent human review or formal verification is claimed.

The 22 supplied reference files represent 21 distinct works or editions. See the [classical source guide](documentation/classical-sources.md) and [variational source guide and scope](documentation/variational-sources.md). The manuscript is original exposition; source books and extracted full text are not redistributed.

The framework retains subject-based chapters and sections, stable tags, cross-references, search, citations, source provenance, reviewed proof and prose additions, and formalization badges. The reader keeps Pome’s Stacks-style layout. Comments are disabled until this repository has its own Discussions and giscus configuration.

## Local preview

Requires Python 3.11+ and Git. Create a local environment and build:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
npm ci --prefix vendor --ignore-scripts --no-audit --no-fund
.venv/bin/python scripts/build.py
python3 -m http.server 8000 --directory _site
```

The registered local manuscript builds without fetching remote sources. Its exact input files are recorded in a SHA-256 manifest. Remote source manuscripts still require `scripts/build.py --fetch` and exact Git revisions.

## Adding mathematical content

- Edit `content/gmt-foundations/` for the current original exposition. Keep `entry-review.json` and source citations in sync.
- Register additional local manuscripts with `local_path` in `books.json`, or register remote repositories; add an adapter in `adapters/`.
- Organize chapters, subjects, and canonical entries in `collection.json`.
- Add formal proof evidence to `formalizations.json` only after verification.
- Optional proof expansions, reading edits, and historical exposition must be explicitly registered in `collection.json`. No inherited registrations remain.

See [integration rules](documentation/integration-layout.md), [adapter contract](adapters/README.md), and [deployment](documentation/deployment.md).

## Checks

```sh
npm ci --prefix vendor --ignore-scripts --no-audit --no-fund
.venv/bin/python -m unittest discover -s tests
node --test tests/*.test.mjs
.venv/bin/python scripts/build.py --fetch
```

Tests use small synthetic mathematical fixtures to verify the renderer; those fixtures are never published as project content. Source-specific Pome integration tests have been removed with their adapters.

## Attribution

The software is derived from Mingchen Xia’s Pome project and the Gerby renderer. The original infrastructure copyright and MIT license are retained in [LICENSE](LICENSE). New mathematical contributions must record their sources and licenses.
