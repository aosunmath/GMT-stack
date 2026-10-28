# Deployment and updates

The repository is [aosunmath/GMT-stack](https://github.com/aosunmath/GMT-stack). The complete reading edition is published at **[aosunmath.github.io/GMT-stack/](https://aosunmath.github.io/GMT-stack/)** using GitHub Pages with `main` and `/docs` as its publishing source. The repository name, public root, and reader identity live in `scripts/project.py`.

The personal homepage at [aosunmath.github.io](https://aosunmath.github.io/) is maintained separately in [aosunmath/aosunmath.github.io](https://github.com/aosunmath/aosunmath.github.io), with `main` and `/` as its publishing source. It currently links to this project.

## Build the reading edition

Install the dependencies listed in the [README](../README.md), then run `.venv/bin/python scripts/build.py --fetch`. The active manuscript is local, so this requires no remote mathematical source checkout. Each build replaces `_site/` completely, so old generated pages and search chunks cannot survive a rebuild. Link validation is part of the build.

`docs/` contains the prebuilt reading edition; `documentation/` contains authored project documentation. Replacing an edition must replace the whole generated directory, including its old tag, section, bibliography, source, and search routes. The publisher accepts a source-free receipt only when the generated collection has explicitly empty chapters, topics, and entries.

## Publication

After local tests, link checks, and desktop/mobile checks, publication uses a clean `main` checkout and an authenticated GitHub CLI (`gh`) available on `PATH`, with Git authentication configured for this fork. Commit authored changes **before** the final build so its source revision is exact. Run `.venv/bin/python scripts/publish.py` only when publication is requested. It checks that `origin` is this fork, fast-forwards `main`, checks the build revision, replaces `docs/`, and pushes a normal commit. It never force-pushes.

GitHub Pages is configured to deploy from the branch, not a custom workflow. The generated `docs/.nojekyll` makes GitHub serve the prebuilt files without processing the manuscript with Jekyll. All reader pages, assets, search data, citations, and source records are included. Relative internal links work under the `/GMT-stack/` prefix.

The publisher requests native Pages delivery and checks the live `upstream.json` against the local build receipt. A successful Git push alone does not confirm that the public site has updated. To inspect deployment state, use `gh api repos/aosunmath/GMT-stack/pages` and `gh api repos/aosunmath/GMT-stack/pages/builds/latest`.

No source-build workflow or scheduled update is included. On a requested update, `scripts/update.py` checks registered sources and proof revisions, rebuilds changed content, and invokes the publisher. A generated-only publication commit does not trigger another rebuild.

## Source export contract

A registered source adapter receives `SOURCE_DIRECTORY OUTPUT_DIRECTORY` and exports `entries.json`, `tags.json`, `edition.json`, `references.json`, temporary validation pages, and any required assets. Export only the reviewed active manuscript. Never export unrelated scans, drafts, or private research files.

The shared builder integrates source exports into chapter, section, entry, tag, bibliography, search, and source routes. `navigation.json` records reading order. `collection.json`, `deduplication.json`, `reading-edition.json`, and `upstream.json` record the generated structure, review results, and revisions. See [integration layout](integration-layout.md) and [adapters](../adapters/README.md).

Comments remain disabled; see [comments](comments.md). The expanded variational manuscript uses mathematical rendering; no formalization evidence has been registered.
