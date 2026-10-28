# Expanding the regularity summaries

This expansion adds **44 entries**, including **18 local proofs** and **12 cited theorems**. At the completion of that expansion, the manuscript contained 154 mathematical and historical entries in 33 sections and 15 chapters, with 38 local proofs and 40 cited theorems whose proofs remain external. The 187 addressable entries include section headings. These counts do not claim independent human review or formal verification. See the later [flow and BV expansion](flow-bv-expansion.md) and the README for subsequent coverage.

The existing `rem:regularity-program` entry, previously Remark 7.2.2, keeps its label and permanent tag. It now links to explicit statements instead of compressing whole theories into a reading list. Existing chapter and section URLs remain unchanged; new sections are appended to their subject chapters.

## What is now stated separately

| Reading section | Additions |
| --- | --- |
| Minimal graphs and elliptic regularity | 12 entries: weak solutions; ellipticity constants; linearization; Lipschitz regularity; classical bootstrap; strong comparison; boundary uniqueness; tangency; calibrations; minimization; graph calibration; a Scherk graph example |
| Elliptic estimates for weak solutions | 9 entries: Sobolev spaces; weak uniformly elliptic equations; Hölder seminorms; Caccioppoli; local boundedness; Harnack; oscillation decay; Schauder; an interior Sobolev estimate |
| Positive Jacobi fields and graphical convergence | 6 entries: local stability; mean-curvature linearization; the positive-Jacobi identity; stability of graphs; separated sheets; a low-dimensional stable curvature bound |
| Tangent cones and stratification | 11 entries: varifold dilation; scaling; density semicontinuity; support density; regular and singular points; tangent cones; spine; splitting; strata; dimension bounds; crossing planes |
| Excess and Allard regularity | 6 entries: height and tilt excess; scaling; Allard with Lp mean curvature; density-one regularity; a density gap; a multiple-plane example |

## Source passages checked

- **Simon, Introduction to Geometric Measure Theory (2017/2018 edition):** Chapter 5, hypotheses (5.1) and Theorem 5.2, printed pp. 145–146 (PDF pp. 76–77). The project states the integral-varifold specialization with the singular part of first variation excluded, p greater than the varifold dimension, and scale-correct mean-curvature control.
- **Simon, Lectures on PDE (March 5, 2015):** Chapters 5–6 and 12; Chapter 18, Theorems 1–2, printed pp. 211–212 (PDF pp. 108–109); Chapters 18–19. Because the PDF font encoding is damaged, theorem formulas were checked against rendered pages. Harnack is stated for nonnegative solutions on a strictly smaller ball, with symmetric measurable coefficients and zero lower-order terms.
- **Chodosh, Introduction to Minimal Surfaces (March 15, 2025):** Section 16; Exercise 18.1, Theorem 18.1 and Exercise 18.2; Lemma 19.1, Proposition 19.3 and Corollary 19.4; Theorem 23.4; Propositions 33.3–33.4, pp. 80–81; Appendix A, p. 86. The sign of the mean-curvature linearization is reconciled with the project's convention.
- **Minter, Regularity Techniques in GMT (Spring 2024):** Lemma 0.6 and Definitions 0.8–0.9; Lemmas 1.1–1.5, Definition 1.6 and Theorem 1.7; scalar graph regularity in Sections 2–3; Corollary 3.2. Tangent cones are not assumed unique, and singular strata quantify over every tangent cone.
- **Sharp, Compactness of minimal hypersurfaces with bounded index (2017):** Theorem 2.1, pp. 320–321, stating the Schoen–Simon estimate. The project takes the smooth, two-sided, Euclidean case, retains the area bound, and restricts to hypersurface dimensions 2 through 6.

## Editorial and mathematical checks

All source labels and previously published permanent tags are retained. Direct dependencies and citations are recorded in `entry-review.json`; the source inventory records checked passages without distributing PDFs or extracted text. Local arguments distinguish interior from boundary conclusions, scalar equations from systems, local from global ellipticity, and smooth graphs from general stationary varifolds.

The density-semicontinuity proof uses continuity radii for weak convergence of mass. Calibration comparisons keep both orientation and the cylinder containing the homology. The positive-Jacobi identity tests compactly supported variations. The separated-sheet theorem assumes globally ordered normal graphs on an exhaustion. Excess zero is explicitly distinguished from multiplicity one.

Cylindrical-cone theory, the full Schoen–Simon and Wickramasekera sheeting theories, and detailed proofs of Allard excess decay remain future work. This expansion develops the analytic and geometric foundations needed to state those results accurately.
