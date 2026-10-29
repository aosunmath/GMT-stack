# Differentiability, Sobolev inequalities, and curvature estimates

This batch adds 45 entries in six subject sections and supplies 46 additional local proofs. Three existing statements retain their tags, labels, and reader locations while receiving proofs: Rademacher's theorem, the Sobolev input to Moser iteration, and the Euclidean Simons identity. The new sections are appended to their subject chapters so existing reader numbers remain unchanged. The edition contains 731 entries, 520 local proofs, 43 external theorem statements, 100 sections, and 16 chapters; the 831 addressable tags include section headings.

## Analytic foundations

`lipschitz-tools.tex` proves scalar McShane extension, absolute continuity on lines, weak directional linearity, the finite-angular-net argument, and mollification bounds. The existing Rademacher theorem uses a countable dense set of directions before invoking the uniform angular estimate. It does not interchange an uncountable intersection of full-measure sets. The counterexample with all directional derivatives shows why linearity and uniformity matter. Background inputs are the one-variable fundamental theorem for absolutely continuous functions, Fubini, and dominated convergence; Lebesgue differentiation is linked to its local proof.

Source: Simon, *Introduction to Geometric Measure Theory*, 2017/2018 edition, Chapter 2, Section 1, printed pp. 43–46 (two-page-spread PDF pp. 25–27). The source attributes its differentiability proof to Morrey. The [Euclidean integration proofs](euclidean-integration-expansion.md) and [rectifiable tangent proofs](rectifiable-tangents-expansion.md) are now developed separately, with their remaining inputs identified.

`sobolev-foundations.tex` proves an iterated Holder inequality, the first-power Euclidean Sobolev estimate, the power substitution for all derivative exponents below dimension, volume-dependent Poincare, every finite gain in dimension two, and scaled ball estimates. Concentrating bumps and a logarithmic singularity demonstrate the endpoint restrictions. The zero-boundary space is defined by closure, so the proof does not silently assume a trace theorem on an arbitrary open set.

Source: Simon, *Lectures on PDE*, March 5, 2015 edition, Lecture 17, Lemma 2 and Corollary 1, printed pp. 200–202 (PDF pp. 103–104). Printed pp. 200–201 were visually checked because extraction damages exponents. No sharp Sobolev constant or geometric-submanifold Sobolev theorem is claimed.

## Curvature and stability

`gauss-simons.tex` separates Gauss–Codazzi, the covariant two-tensor commutator, the space-form Simons identity, and the norm identities. The convention is scalar second form positive on an outward-oriented Euclidean sphere, scalar mean curvature equal to its trace, and curvature operator `R(X,Y)Z = ∇X∇YZ − ∇Y∇XZ − ∇[X,Y]Z`. The commutator signs and the space-form term `c(nh − Hg)` are derived in a geodesic principal frame. Further entries prove ordinary and improved Kato inequalities, a weak curvature inequality through flat points, and a curvature Caccioppoli estimate.

Source: Huisken–Polden, *Geometric evolution equations for hypersurfaces*, LNM 1713 (1999), Section 2, printed pp. 47–49, especially Corollary 2.2. The supplied PDF's p. 49 was rendered and checked. The improved Kato calculation is also compared with Schoen–Simon–Yau, equations (1.29)–(1.33), in the Euclidean minimal case.

`stable-curvature-integrals.tex` proves the Euclidean Schoen–Simon–Yau integral curvature estimate for `4 ≤ p < 4 + sqrt(8/n)`. The proof regularizes curvature by `sqrt(|A|² + ε²)`, retains the resulting stability error until it vanishes, and displays the decisive positive coefficient `2/n − q²`. Intrinsic distance cutoffs require completeness; extrinsic distance cutoffs require properness. Induced volumes count immersion multiplicity. Growth rigidity and the graph consequence are proved through dimension five. The failure of this exponent range to reach dimension six is described only as a limitation of this argument.

Source: Schoen–Simon–Yau, *Curvature estimates for minimal hypersurfaces*, Acta Mathematica 134 (1975), pp. 275–288. The supplied 14-page PDF was checked at pp. 277–285; p. 281 was rendered to verify the range in Theorem 1. Theorem 2 and equation (2.9) supply the growth comparison. The pointwise estimates later in the paper depend on a geometric Sobolev inequality and are deferred.

## CMC pinching

`cmc-pinching.tex` proves the trace-free Simons equation, the sharp cubic bound, and a compact-manifold pinching gap, followed by spherical minimal and product-sphere examples. Alencar–do Carmo use the opposite shape-operator sign and averaged mean curvature; the conversion is made explicit. The space-form gap requires `nc + H²/n > 0`. Compactness, absence of boundary, connectedness, and two-sidedness are stated. The general classification of equality cases is not imported; the displayed products are checked directly.

Source: Alencar–do Carmo, *Hypersurfaces with constant mean curvature in spheres*, Proc. AMS 120 (1994), pp. 1223–1229. The author-hosted manuscript has nine independently numbered pages. Sections 1–2, manuscript pp. 1–6, were checked; p. 4 was rendered. Intermediate typographical errors in that manuscript are not copied: the norm equation, constrained cubic optimization, and product signs are rederived. The cubic inequality is attributed to Okumura through the authors' Lemma 1; their paper is the checked primary source.

## Flow pinching

`mcf-pinching.tex` proves an endomorphism maximum principle with an evolving metric, preservation of weak and strict convexity and linear principal-curvature bounds, and the normalized curvature-ratio equation. Its strong-maximum-principle equality case is proved under closedness, connectedness, and strict convexity. A round-cylinder example identifies the missing hypotheses in the noncompact weakly convex case. Scalar maximum principles remain background analytic inputs; the full round-point convergence proof is deferred.

Source: Huisken, *Flow by mean curvature of convex surfaces into spheres*, Journal of Differential Geometry 20 (1984), pp. 237–266. The supplied PDF was checked at pp. 241–248, especially Theorem 4.3 and Lemma 5.2; p. 246 was rendered. The scalar convention and the time derivative of the mixed-index shape operator agree with the existing evolution section.

All source records retain exact file hashes and checked passage locators. Original PDFs and private extracts remain outside the publication. Local proofs are original exposition with recorded dependencies; no formal verification or independent human review is claimed.
