# Variational sources and development status

The expanded reference is **Stack Project of Geometric Measure Theory and Variational Problems**. It includes the classical GMT foundation and branches for minimal surfaces, min-max theory, the volume spectrum, CMC surfaces, phase transitions, obstacle problems, and mean curvature flows. The Introduction retains the former `orientation` route and all pre-existing tags.

The current manuscript contains 84 mathematical/editorial entries in 22 sections and 14 chapters. Seventeen entries include local proofs; eighteen are cited theorems with external proofs. Definitions, examples, and editorial dependency maps make up the remainder. No independent human review or formal verification is recorded. The website's count of 106 addressable entries also includes the 22 section headings.

## The sixteen additional supplied references

| Reference | Supplied edition | Initial use |
| --- | --- | --- |
| Pitts, *Existence and Regularity of Minimal Surfaces on Riemannian Manifolds* | Princeton, Mathematical Notes 27, 1981 | Discrete min-max, almost minimizing, original smooth existence range; Introduction Theorem A and §7.13 |
| Liokumovich–Marques–Neves, *Weyl law for the volume spectrum* | Published Annals 187 (2018), 933–961, with JSTOR cover | Admissible families (§2.6), mass fineness (§2.9), Weyl law (Theorem 1.1) |
| Colding–De Lellis, *The min-max construction of minimal surfaces* | Published survey, 2003, pp. 75–107; scanned PDF | Smooth families and saturation (§1.1); opening pages visually checked |
| Ketover–Marques–Neves, *The catenoid estimate and its geometric applications* | Supplied 27-page manuscript; revision date unstated; first arXiv posting 2016 | Neck-deformation mechanism (Theorem 2.4) and fundamental-class width (Theorem 1.5) |
| Minter, *Regularity Techniques in Geometric Measure Theory* | Spring 2024 Princeton course, 169 pages | Dependency map for tangent cones, Allard, excess decay, stable hypersurfaces, cylindrical cones, and sheeting |
| Simon, *Lectures on PDE* | Tsinghua notes, updated March 5, 2015 | Sobolev/elliptic prerequisites and graph equations (Chapter 19); date visually checked |
| Yangyang Li, *Introduction to Almgren-Pitts Min-Max Theory* | Preliminary version, July 7, 2019 | Expository guide to cycle topology, almost minimizing, pull-tight, and regularity |
| Marques–Neves, *Morse index of multiplicity one min-max minimal hypersurfaces* | Published Advances 378 (2021), 107527 | Continuous conventions, realization statement, Main Theorem 1.3 with its full multiplicity hypothesis |
| Chodosh–Mantoulidis, *Minimal surfaces and the Allen-Cahn equation on 3-manifolds…* | arXiv:1803.02716v2, posted May 14, 2018; manuscript dated May 16 | Curvature, sheet separation, Jacobi fields, and index dependency map |
| Marques, notes by Montezuma, *Surfaces minimales: théorie variationnelle et applications* | Supplied undated 71-page notes | First and second variation and stability |
| Zhou–Zhu, *Min-max theory for networks of constant geodesic curvature* | Submission version 1, March 7, 2019 | Theorem 1.1, retaining the finite junction set |
| Zhou–Zhu, *Min-max theory for constant mean curvature hypersurfaces* | arXiv:1707.08012v2, August 11, 2017 | Area-minus-volume functional and Theorem 0.1; almost embeddedness and sheet multiplicity distinguished |
| Marques–Neves, *Min-Max theory and the Willmore conjecture* | Published Annals 179 (2014), 683–782 | Averaged mean curvature, Definition 1.2 and Theorem A |
| Nurser, *Low min-max widths of the round three-sphere* | Imperial College PhD thesis, October 2016 | Theorem 8 and explicit families; historical statements, not a complete current spectrum |
| Chodosh, *Lecture notes on geometric features of the Allen-Cahn equation (Princeton, 2019)* | Supplied revision June 29, 2023 | Energy normalization, equation, and transition layer |
| Chodosh, *Introduction to Minimal Surfaces* | March 15, 2025 | Smooth geometry, variations, minimal graphs, and compactness program |

The [Colding–De Lellis author page](https://www.math.ias.edu/delellis/node/257) identifies the publication and links an erratum. Detailed imports from that survey must consult the correction. The [catenoid preprint record](https://arxiv.org/abs/1601.04514) supplies the work's initial posting year; its current version is not assumed to match the undated local manuscript.

Together with the [classical sources](classical-sources.md), these are 22 supplied files representing 21 distinct works or editions. `content/gmt-foundations/source-inventory.json` records each hash and source role. Citations refer to original printed pages and theorem numbers. For Pitts, printed page 1 is PDF page 11; for the Weyl-law paper, printed page 933 is PDF page 2. Simon's PDE PDF contains two-page spreads and a damaged text encoding. The supplied files and full extracted text are not part of the published content.

## Assumptions that must remain visible

| Construction | Competitors and topology | Scope of the current entry |
| --- | --- | --- |
| Homotopy width | Mod-two boundary cycles; F-continuous maps, flat homotopies; fixed finite parameter complex | Positive width has a smooth embedded minimal-cycle realizer in ambient dimensions 3–7; integer multiplicities remain possible |
| Pitts' original existence theorem | Discrete min-max and almost-minimizing regularity | Smooth-metric specialization in ambient dimensions 3–6, matching the supplied book |
| Volume spectrum | Mod-two boundary component; flat continuity, bounded maximal mass, no concentration, nonzero cup power | Infimum over admissible families, not an arbitrary fixed homotopy class; closed connected ambient manifold |
| Index equality | Bumpy metric, ambient dimensions 3–7, width-realizing class of p-sweepouts on a finite p-dimensional complex | Every embedded minimal cycle in the indicated critical set must have multiplicity one; conclusion is existence of an index-p realizer |
| Positive-Ricci one-parameter result | Integer fundamental-class sweepouts based at zero; orientable closed manifold | Index one and multiplicity one for that width; no transfer to arbitrary periodic mod-two families |
| CMC | Finite-perimeter regions; perimeter minus c times volume | c>0, ambient dimensions 3–7, almost embedded output; touching allowed |
| Curvature networks | Boundaries of regions in a closed surface | Finite exceptional set and stationary tangent networks retained |
| Allen–Cahn | Functions with diffuse-interface energy | Elementary formulas plus a map to the cited analytic results; equality with cycle-space widths is not assumed |

Hypersurface dimension is `n`, ambient dimension is `n+1`. The smooth scalar mean curvature is the trace, positive on an outward-oriented sphere; its vector is `−Hν`. The Willmore energy explicitly uses the average of the two principal curvatures. The Allen–Cahn potential is `(1−u²)²/4`, whose one-dimensional interface energy is `2√2/3`.

## Scope still to develop

Obstacle problems currently have a precise admissible set and a proved variational inequality. Mean curvature flow currently has its smooth definition, proved area dissipation, and a shrinking-sphere example. Dedicated source corpora, existence theory, regularity, singularities, Brakke flow, and level-set flow are pending. Further planned branches include Plateau problems, free-boundary minimal surfaces, capillarity, prescribed mean curvature, and additional Willmore problems.

The full proof ledger is `content/gmt-foundations/entry-review.json`, also exported on the Sources page. Theorems cited without proofs are visibly labeled in their entries. The project retains the Pome/Gerby framework and infrastructure attribution; its GitHub repository and public root remain stable in `scripts/project.py`.
