# Stack Project of Geometric Measure Theory and Variational Problems

**[Read the project online → aosunmath.github.io/GMT-stack](https://aosunmath.github.io/GMT-stack/)**

[Table of contents](https://aosunmath.github.io/GMT-stack/chapters/) · [Search](https://aosunmath.github.io/GMT-stack/search/) · [Bibliography](https://aosunmath.github.io/GMT-stack/references/) · [Sources and revisions](https://aosunmath.github.io/GMT-stack/sources/)

A growing, subject-based mathematical reference for geometric measure theory and variational problems, built on [Mingchen Xia’s Pome framework](https://github.com/MingchenXia/Pome). The website presents connected exposition, definitions, examples, theorem statements, and proofs with stable tags and cross-references. It is intended to develop into a Stacks-style reference for these subjects.

## Reading the project

Start with the [Introduction](https://aosunmath.github.io/GMT-stack/chapters/orientation/) for sources and conventions, or use the table of contents to enter by subject. Search accepts keywords and permanent tags. Proofs are collapsed by default: select **Proof** or its down arrow to open the argument. Citations jump to a reference list on the same page, with return links. The bibliography links back to the pages that use each source. Each reading page also provides a permalink and citation tools.

| Area | Chapters |
| --- | --- |
| Foundations | [Measure theory](https://aosunmath.github.io/GMT-stack/chapters/measure-theory/), [rectifiability and integration](https://aosunmath.github.io/GMT-stack/chapters/rectifiability/), [sets of finite perimeter](https://aosunmath.github.io/GMT-stack/chapters/finite-perimeter/) |
| Generalized surfaces | [Currents and flat chains](https://aosunmath.github.io/GMT-stack/chapters/currents-flat-chains/), [varifolds](https://aosunmath.github.io/GMT-stack/chapters/varifolds/) |
| Minimal surfaces and min-max | [Minimal surfaces](https://aosunmath.github.io/GMT-stack/chapters/minimal-surfaces/), [min-max theory](https://aosunmath.github.io/GMT-stack/chapters/min-max-theory/), [volume spectrum and Morse index](https://aosunmath.github.io/GMT-stack/chapters/volume-spectrum/), [geometric applications](https://aosunmath.github.io/GMT-stack/chapters/geometric-applications/) |
| Constrained and diffuse interfaces | [Constant mean curvature surfaces](https://aosunmath.github.io/GMT-stack/chapters/constant-mean-curvature/), [Allen–Cahn and phase transitions](https://aosunmath.github.io/GMT-stack/chapters/allen-cahn/) |
| Free boundaries and evolution | [Obstacle problems](https://aosunmath.github.io/GMT-stack/chapters/obstacle-problems/), [mean curvature flows](https://aosunmath.github.io/GMT-stack/chapters/mean-curvature-flow/) |

Explore the **[History chapter](https://aosunmath.github.io/GMT-stack/chapters/history/)** for sourced notes about the origins of GMT, the Bernstein problem, and min-max theory. Browse the **[reference library](https://aosunmath.github.io/GMT-stack/sources/gmt-foundations/#reference-library)** for study status and source editions.

## Current scope and sources

The project covers geometric measure theory, minimal surfaces, min-max theory, the volume spectrum, constant mean curvature surfaces, Willmore geometry, Allen–Cahn and phase transitions, obstacle problems, and mean curvature flows. The first chapter is **Introduction**.

The latest expansions develop smooth and weak mean curvature flow, Gaussian monotonicity and entropy, BV compactness, current operations and slicing, Plateau existence, volume-constrained CMC stability, scalar-curvature consequences of stability, Bernstein’s theorem, the spectral criterion for smooth-link minimal cones, weighted and BV coarea, level-set calculus, and smooth-support varifold constancy. They follow the expanded minimal-graph, elliptic, Jacobi-field, and Allard regularity sections.

The current draft contains **464 mathematical and historical entries in 66 sections and 15 chapters**, including 268 local proofs and 47 cited theorems whose proofs remain external. The website's total of 530 addressable entries includes the 66 section headings. The current and perimeter chapters now include calibrated mass comparison, equality and weak-limit results, a singular calibrated complex cusp, and strict Simons cone perimeter minimization for arbitrary compact perturbations. The varifold foundations now prove exact stationary monotonicity, tangent-cone homogeneity, spine splitting, qualitative singular stratification, one-dimensional cone classification, convergence of supports, bounded-curvature monotonicity, and the density gap as a consequence of Allard regularity. General-varifold examples distinguish weight homogeneity, rectifiability, sphere atoms, and boundary contributions. The Allen–Cahn branch now develops transition profiles, sharp energy bounds, BV phase compactness, perimeter lower bounds, equipartition, recovery layers, Modica gradient bounds, diffuse monotonicity, geometric stability, sliding minimization, and bounded monotone rigidity in dimensions two and three. Its Gamma limit and local-minimizer consequences explicitly depend on the external relative-boundary recovery theorem. The classical obstacle branch now includes existence, comparison, reaction measures, quadratic blow-ups, Weiss and Monneau monotonicity, and singular blow-up uniqueness. Deep obstacle regularity and singular-stratum manifold containment retain external proof dependencies; thin and geometric obstacles remain in development. The flow chapter includes evolution equations, comparison, Gaussian monotonicity, entropy, rescaling, and Brakke flow; level-set flows and finer singularity theory are still in development. No independent human review or formal verification is claimed.

The initial sources include Federer, Simon, White, Fleming, and Pitts, together with papers and lecture notes on min-max theory, the volume spectrum, the Willmore conjecture, CMC surfaces, regularity, and Allen–Cahn. The reference library now records 120 reference files, including duplicate copies and separate editions. Forty bibliographic works or editions are cited; other files are explicitly catalogued for further study. See the [classical source guide](documentation/classical-sources.md), [variational source guide and scope](documentation/variational-sources.md), [library expansion](documentation/library-expansion.md), [regularity expansion](documentation/regularity-expansion.md), [flow and BV expansion](documentation/flow-bv-expansion.md), [currents and CMC expansion](documentation/currents-cmc-expansion.md), [stability and cones](documentation/stability-cones-expansion.md), [coarea and constancy](documentation/coarea-constancy-expansion.md), [classical obstacle theory](documentation/obstacle-expansion.md), [phase-transition foundations](documentation/phase-transition-expansion.md), and [phase geometry and rigidity](documentation/phase-geometry-expansion.md) for exact editions and coverage. The manuscript is original exposition; source books and extracted full text are not redistributed.

Statements retain their hypotheses, conventions, and source attribution. The [proof ledger](content/gmt-foundations/entry-review.json) distinguishes local proofs from cited results. The renderer supports formalization badges, but no verified formalizations are currently registered. Comments are disabled pending a project-specific configuration.

## Repository guide

| Path | Purpose |
| --- | --- |
| [`content/gmt-foundations/`](content/gmt-foundations/) | LaTeX manuscript, bibliography, source inventory, and proof ledger |
| [`collection.json`](collection.json) | Subject organization and chapter/section placement |
| [`books.json`](books.json) | Registered manuscripts and source locations |
| [`scripts/`](scripts/) and [`adapters/`](adapters/) | Build, rendering, validation, and publication tools |
| [`site/assets/`](site/assets/) | Reader styles and browser behavior |
| [`docs/`](docs/) | Complete prebuilt website served by GitHub Pages |
| [`documentation/`](documentation/) and [`tests/`](tests/) | Editorial contracts, development guides, and infrastructure tests |

## Local preview

Requires Python 3.11+, Node.js/npm, and Git. Clone the repository, install dependencies, and build:

```sh
git clone https://github.com/aosunmath/GMT-stack.git
cd GMT-stack
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
npm ci --prefix vendor --ignore-scripts --no-audit --no-fund
.venv/bin/python scripts/build.py
python3 -m http.server 8000 --directory _site
```

Open [localhost:8000](http://localhost:8000/). To preview the already-built edition without installing build dependencies, run `python3 -m http.server 8000 --directory docs` from the repository root.

The registered local manuscript builds without fetching remote sources. Its exact input files are recorded in a SHA-256 manifest. Remote source manuscripts still require `scripts/build.py --fetch` and exact Git revisions.

## Contributing mathematical content

Propose corrections or additions through a pull request. Include precise references and explain changes to hypotheses, notation, or proof status. Preserve existing tags and source labels so citations remain stable. Read [AGENTS.md](AGENTS.md) and the [integration rules](documentation/integration-layout.md) before reorganizing material.

- Edit `content/gmt-foundations/` for the current original exposition. Keep `entry-review.json` and source citations in sync.
- Register additional local manuscripts with `local_path` in `books.json`, or register remote repositories; add an adapter in `adapters/`.
- Organize chapters, subjects, and canonical entries in `collection.json`.
- Add formal proof evidence to `formalizations.json` only after verification.
- Optional proof expansions, reading edits, and historical exposition must be explicitly registered in `collection.json`. No inherited registrations remain.

See [integration rules](documentation/integration-layout.md), [adapter contract](adapters/README.md), and [deployment](documentation/deployment.md).

## Publishing

GitHub Pages serves the complete `docs/` directory from `main` at **[aosunmath.github.io/GMT-stack/](https://aosunmath.github.io/GMT-stack/)**. Builds and validation run locally; there is no custom CI or scheduled content update. After an authorized update has been committed and checked, the publisher replaces the generated edition and verifies its public revision. See the [deployment guide](documentation/deployment.md).

[Ao Sun's homepage](https://aosunmath.github.io/) links to this project.

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
