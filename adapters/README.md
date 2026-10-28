# Book conversion adapters

No source-specific adapters are registered in the empty GMT edition. Pome’s book adapters and source profiles were removed. The common Gerby renderer and HTML templates remain available.

After choosing an actual GMT source, add `<book-slug>.py` and register it in `books.json`. The adapter receives `SOURCE_DIRECTORY OUTPUT_DIRECTORY`. Call `common.configure` with the source identity before exporting. The default preparation expands a web-compatible `book.tex` with explicit theorem environments and stable labels; use an explicit preparation callback for other document classes or layouts. Bibliography defaults to `references.bib`.

Export `entries.json`, a complete `tags.json` inventory, `references.json`, `edition.json` with the exact source commit, temporary validation pages, and required assets. Keep statement/proof HTML, source labels, original numbers, and statement fingerprint inputs distinct. The builder verifies page coverage and formalization markers, then integrates the content into shared subjects.

Adapters must follow only the reviewed manuscript input graph and keep paths inside its source directory. Preserve attribution and license information. Regression tests should use synthetic content and cover source numbering, tags, references, proofs, and rejected inputs. See the [deployment contract](../documentation/deployment.md).

## Local GMT manuscript

`gmt-foundations.py` calls the common renderer with `local=True`. The `local_path` registry field selects a directory inside this project. Every manuscript file is fingerprinted before and after rendering; the full SHA-256 manifest appears on the Sources page. A working-tree snapshot is never presented as a Git commit. Local input requires no network fetch. Keep the reference inventory and entry/proof-status record current; do not add source scans or OCR to the manuscript directory.
