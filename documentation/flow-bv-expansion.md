# Flow and BV foundations

This expansion adds **59 entries** in six new sections: 42 entries on mean curvature flow and 17 on BV functions and finite-perimeter variational problems. It includes **36 local proofs**, **5 externally proved theorem statements**, 11 definitions, and 7 examples. The resulting edition has **213 mathematical and historical entries in 39 sections and 15 chapters**, including 74 local proofs and 45 externally proved theorems. Its 252 addressable entries also count the section headings.

## Mathematical development

| Section | Content |
| --- | --- |
| Evolution equations and comparison | Normal-variation formulas, Simons identity, curvature evolution, preservation of nonnegative mean curvature, position equations, confinement, avoidance, existence and continuation, curvature rates, parabolic rescaling, and graphical comparison |
| Huisken monotonicity and entropy | Test-function transport, the Gaussian kernel, a proof of smooth closed-flow monotonicity, Gaussian density, entropy invariance and monotonicity, area-growth bounds, and multiplicity |
| Rescaled flow and self-similar models | Logarithmic rescaling, Gaussian dissipation, times of small dissipation, a conditional smooth-limit argument, equality in monotonicity, translators, expanders, and the grim reaper |
| Brakke flows and loss of mass | An integrated boundaryless definition, smooth-flow compatibility, disappearing planes, a shrinking cutoff, local curvature energy, one-sided mass limits, weak compactness, Gaussian monotonicity, unit regularity, and cyclicity |
| BV approximation and compactness | Total-variation lower semicontinuity, cutoff products, mollification, strict convergence, translation estimates, a proof of BV compactness, compactness of sets, and weak convergence of derivative measures |
| Perimeter blow-ups and the direct method | Measure-theoretic boundary, reduced-boundary half-space blow-ups, null modifications, fixed-volume minimization, local minimization with a bulk term, and the Euler equation on a smooth interface |

All existing labels, permanent tags, chapter identifiers, and section URLs are retained. New sections are appended within their subject chapters. The old flow-program remark now links to the developed results rather than describing all of them as future work.

## Sources and normalization checks

The reference catalogue now contains 119 files. Three additional primary sources were located in the user's local library; their PDFs are not redistributed. Bibliography records link to public primary-source locations where available.

- **Huisken--Polden (1999), Geometric evolution equations for hypersurfaces:** Corollary 2.2, printed p. 49; Theorems 3.1--3.2, pp. 51--52; the rescaling and translator discussion in Section 4. The normal-variation formulas on p. 52 were checked visually against the scan.
- **Huisken (1990), Asymptotic behavior for singularities of the mean curvature flow:** Theorem 1.1 and Lemma 1.2, p. 286; the rescaling in Section 2; Theorem 3.1 and Corollary 3.2, pp. 288--289. The monotonicity formula was checked visually. The project uses the scale-one equation with coefficient one half, while Huisken's rescaled convention uses coefficient one.
- **White, notes by Chodosh (June 8, 2015), Mean Curvature Flow:** Sections 3--4, 6, and 9--11. The Gaussian normalization is checked against Huisken's original paper. The project does not silently adopt transcription errors or unqualified interpretations of regularity across a possible mass drop.
- **Chodosh--Choi--Mantoulidis--Schulze, supplied arXiv v1 (2020):** Sections 2.4--2.6, pp. 10--11, for the Brakke inequality, density, convergence, unit regularity, and cyclicity. The project's working definition explicitly excludes a singular first-variation boundary term.
- **Simon, supplied 2017/2018 Introduction to GMT:** Chapter 2, Section 2, especially Lemma 2.5 and Theorem 2.6, pp. 52--55; Chapter 3, proof of Theorem 4.4, equations (9)--(13), pp. 98--100. The BV compactness statement was checked visually against the two-page spread.

## Assumptions kept explicit

The curvature evolution identities are Euclidean. Smooth Gaussian integration by parts is proved for closed flows; the weak Gaussian theorem has a uniform entropy hypothesis on compact time intervals to control spatial tails. A lower curvature blow-up rate is not a Type I upper bound. Small Gaussian dissipation only identifies a shrinker after a separately stated smooth convergence assumption. Brakke convergence is weak and may use a different further varifold subsequence at almost every time.

The BV compactness theorem includes local L1 control. Strict convergence is distinguished from convergence in the BV norm. Volume passes to the limit under global L1 convergence, supplied by the common compact container. The local bulk-energy problem fixes competitors outside a compact subset of the ambient domain; it makes no unstated trace-continuity claim. The half-space blow-up is stated at reduced-boundary points, with the outward normal determining which half-space is the interior.

## Remaining scope

Full proofs of parabolic existence, Simons commutation, Brakke compactness, weak Gaussian monotonicity, and De Giorgi's blow-up theorem remain external. Level-set flows, tangent-flow extraction, higher singularity theory, BV coarea and traces, and geometric regularity of the direct-method minimizers remain further development. No independent human review or formal verification is claimed.
