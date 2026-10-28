# Integration layout and numbering

The active reference is an original local manuscript in `content/gmt-foundations/`. `collection.json` places its 45 subject sections in 15 chapters. See [classical sources](classical-sources.md), [variational sources](variational-sources.md), [the library expansion](library-expansion.md), [the regularity expansion](regularity-expansion.md), [flow and BV foundations](flow-bv-expansion.md), [currents and CMC variations](currents-cmc-expansion.md), and [stability and cones](stability-cones-expansion.md) for editions, conventions, and proof coverage. Project identity is centralized in `scripts/project.py`; preserve existing tags, source slugs, and URLs when changing display titles.

## Reading structure

Organize content by mathematical subject across contributing sources. Split long or mixed sections using reviewed `section_promotions` boundaries. Absorb a source heading that repeats the containing section title while preserving its introductory text and permanent GMT tags. Chapter pages list sections and retained subsections; section pages show connected prose and complete statements and proofs.

Reader locators belong to the current GMT structure: chapters use `C`, sections use `C.S`, and addressable subordinate blocks share the `C.S.N` counter. Source numbers remain provenance. `scripts/structure.py` places sections, `scripts/numbering.py` assigns locators, and `scripts/collection.py` applies them to headings, equations, references, navigation, and search. Do not globally replace digits in mathematical text.

## Tags, sources, and review

Global tags derive from source slugs and stable labels. A canonical merge requires explicit source bindings and reviewed statement fingerprints. Changed hypotheses or missing reviewed members must fail the build. Different hypotheses remain distinct. Numbered clauses retain anchors inside their parent statement; formalization badges describe complete statements.

Preserve future GMT tags when reorganizing. Pome’s inherited tags and routes were removed in the initial empty edition because they identify mathematical content that is not part of Stack Project of Geometric Measure Theory and Variational Problems.

`books.json` registers source repositories or an explicit project-relative `local_path`. Local manuscripts use an exact SHA-256 file manifest; remote manuscripts retain Git commit provenance. Optional `proof_expansions`, `reading_edits`, and `historical_exposition` paths in `collection.json` activate the retained review machinery. These fields are currently absent. Do not carry over old prose replacements, historical summaries, dependency records, or source fingerprints. If source-coordinate citation conversion is needed, a reading registry must explicitly provide `locator_source` and `locator_bibliography_key`; no source is assumed by default.

Record source licenses, exact revisions, attribution, and unresolved proof dependencies. A prose edit is not mathematical or formal verification. The public Sources pages retain provenance without confusing source numbering with current reader numbering.

## Reader checks

Show tags reveals chapter, section, statement, equation, and clause identifiers. Cite this page must open on repeated clicks and direct `#cite` links, and its BibTeX must identify Stack Project of Geometric Measure Theory and Variational Problems and the current page. Footnotes retain paired references and return links. Long equations scroll within the reading column on narrow screens.

Before publication, run the commands in the README and inspect desktop and mobile layouts. For the empty edition, the build must produce zero chapters, entries, sources, search results, and formalizations, with no links to old mathematical routes or Xia’s comment threads.

Proofs use native closed `details.proof` panels. Fragment links reopen a containing proof, and print events temporarily expand proofs. Citations retain their canonical bibliography identifiers and also receive page-local reference targets with unique return links. Bibliography backlinks point to the exact local reference list; source catalogues distinguish cited sources from files awaiting review.
