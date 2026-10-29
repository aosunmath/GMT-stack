# Phase kernels, curved layers and fixed-parameter compactness

This expansion adds 41 entries with 41 local proofs in seven sections. Four sections extend Allen–Cahn theory, two add explicit phase examples, and one develops the analytic compactness input in the minimal-surface chapter. All prior reader numbers, tags, source labels and routes are preserved.

## Source and normalizations

The principal source is Chodosh's *Lecture Notes on Geometric Features of the Allen–Cahn Equation*, revision June 29, 2023. The supplied 38-page copy was checked at pp. 3–5, 14 and 28–31, including visual inspection of the compactness exercise and the normal-kernel and Fermi-coordinate formulas. The source inventory records the exact hash and checked passages. Simon's previously checked BV mollification method provides the model for the separate Sobolev argument. No source scan or extracted full text is exported.

The potential is `(1−u²)²/4`, the profile is `tanh(t/√2)`, and its derivative has squared integral `2√2/3`. Normal quadratic forms, the operator with an epsilon-squared Laplacian, and the operator with an epsilon-inverse-squared potential have different spectral scales; the text states each. The curved-interface residual is `epsilon² Δu − W′(u)`, whereas fixed-parameter compactness uses its negative. These conventions are explicit in their sections.

Some source displays need correction when used for these calculations. The normal quadratic form has a squared test function in its potential term. Linearization of the corrector equation uses the second derivative of the potential; boundedness is necessary for its normalized uniqueness. The fixed-parameter residual must retain the epsilon-squared Laplacian. The local proofs derive these formulas directly. They do not adopt the same error order for every unscaled normal derivative.

## Normal and tangential analysis

Two first-order factorizations prove the exact normal gap `3/2`, including its equality mode. An adjoint primitive for compact orthogonal data and a limiting argument prove the inequality without a spectral decomposition. Intertwining classifies all square-integrable eigenfunctions; no full continuous-spectrum theorem is claimed. Hilbert representation on the orthogonal subspace supplies an explicit normal inverse with quantitative bounds.

The bounded flat kernel is handled separately. A coercive half-space barrier proves normal decay. External interior elliptic estimates then justify derivative decay, differentiation under the normal integral and integration by parts. The translation coefficient is bounded harmonic and hence constant. The squared norm of the orthogonal slice satisfies a strictly coercive differential inequality and vanishes by a penalized maximum argument. A full quadratic-form splitting explains why the normal gap does not imply a positive Rayleigh bottom on the entire ambient space.

## Curved layers and explicit examples

The Fermi calculation uses a two-sided embedded surface in Euclidean three-space, a buffered compact patch and an injective fixed tube. The shape convention is `A = Dν`. Exact parallel curvature gives a special cancellation on a minimal surface. A bounded odd normal corrector improves the unshifted residual to fourth order in the uniform norm. The shifted profile has physical displacement of order epsilon squared. Pairing its cubic residual with the translation mode gives the surface Jacobi operator. A global inverse, nonlinear correction and gluing existence theorem remain separate problems.

The bounded ODE classification includes constants, heteroclinics and periodic profiles. The latter have a strictly increasing period, an exact cell-energy derivative, an explicit positive negative-eigenvalue mode, and infinite compactly supported index on Euclidean space. Circle solutions require a strict length threshold. A degenerating one-period family converges to precisely two multiplicity-one interface points in its energy measure.

Vertical graph layers illustrate a persistent area excess and nonzero discrepancy. Signed-distance normalization repairs the tilted-plane case. The second-order energy of a symmetric tubular layer is governed by total Gauss curvature, with controlled exponential tails; the sphere and torus computations distinguish this quantity from Willmore energy. These are computations for specified competitors, with no implicit assertion of criticality or minimization.

## Fixed-parameter compactness and dependencies

A quadratic translation estimate and mollification give strong L2 compactness on a closed manifold. The same argument yields a positive Poincare constant when the manifold is connected. Functional-analytic background includes L2 completeness and translation continuity, Hilbert weak compactness, smooth partitions of unity and Arzela–Ascoli.

For a fixed positive epsilon, bounded-range residual sequences tending to zero in the dual of H1 converge strongly in H1, with energy convergence. The range bound avoids any dimension restriction from an H1-to-L4 embedding. Smoothness and compactness in all finite differentiability norms still use external elliptic estimates and bootstrapping. Negative finite matrices give index lower semicontinuity. The Poincare threshold rules out nonconstant solutions, including the equality case, and is sharp on a circle. No uniform compactness as epsilon tends to zero or mountain-pass existence is inferred.

The proof ledger also removes a reverse dependency from the external Marques–Neves theorem to its explanatory immersed-surface corollary. The corollary uses that theorem; its backlink is not a proof of the theorem.

No independent human review or formal verification is claimed.
