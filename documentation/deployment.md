# Deployment and updates

The repository is [aosunmath/GMT-stack](https://github.com/aosunmath/GMT-stack). Its configured Pages address is `https://aosunmath.github.io/GMT-stack/`. The repository name, public root, and reader identity live in `scripts/project.py`. Configuration does not imply that Pages has been enabled or that an edition has been deployed.

## Empty edition

Run `.venv/bin/python scripts/build.py`. With empty registries this fetches no mathematical sources and needs no MathJax assets. `--fetch` also works and has no upstream sources to download. Each build replaces `_site/` completely, so old generated pages and search chunks cannot survive a rebuild.

`docs/` contains the prebuilt reading edition; `documentation/` contains authored project documentation. Replacing an edition must replace the whole generated directory, including its old tag, section, bibliography, source, and search routes. The publisher accepts a source-free receipt only when the generated collection has explicitly empty chapters, topics, and entries.

## Publication

After local tests, link checks, and desktop/mobile checks, publication uses a clean `main` checkout and the authenticated GitHub CLI. Run `.venv/bin/python scripts/publish.py` only when publication is requested. It checks that `origin` is this fork, fast-forwards `main`, checks the build revision, replaces `docs/`, and pushes a normal commit. It never force-pushes. Configure native GitHub Pages delivery from `main` and `/docs` before using the deployment request.

No source-build workflow or scheduled update is included. On a requested update, `scripts/update.py` checks registered sources and proof revisions, rebuilds changed content, and invokes the publisher. A generated-only publication commit does not trigger another rebuild.

## Source export contract

A registered source adapter receives `SOURCE_DIRECTORY OUTPUT_DIRECTORY` and exports `entries.json`, `tags.json`, `edition.json`, `references.json`, temporary validation pages, and any required assets. Export only the reviewed active manuscript. Never export unrelated scans, drafts, or private research files.

The shared builder integrates source exports into chapter, section, entry, tag, bibliography, search, and source routes. `navigation.json` records reading order. `collection.json`, `deduplication.json`, `reading-edition.json`, and `upstream.json` record the generated structure, review results, and revisions. See [integration layout](integration-layout.md) and [adapters](../adapters/README.md).

Comments remain disabled; see [comments](comments.md). The expanded variational manuscript uses mathematical rendering; no formalization evidence has been registered.
