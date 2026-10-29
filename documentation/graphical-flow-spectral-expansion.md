# Graphical mean curvature flow and spherical harmonics

This expansion adds 50 entries with 47 local proofs in seven subject sections. The existing round-shrinker F-stability and CMC sphere nullity proofs now use a locally developed spherical-harmonic decomposition. Their statements, permanent tags and reader locations are preserved. The edition has 1,028 mathematical and historical entries, 802 local proofs, 43 cited theorems with external proofs, 148 sections and 17 chapters. Section headings bring the addressable total to 1,176.

## Sources and conventions

- **EH89:** Klaus Ecker and Gerhard Huisken, *Mean curvature evolution of entire graphs*, Annals of Mathematics 130 (1989), 453–471. The supplied journal copy has 20 PDF pages including its archive cover. Checked passages include Lemma 3.1, Corollary 3.2, Lemma 4.1, Corollary 4.2, Propositions 4.3–4.4 and Theorem 4.6; printed pages 458–461 and 464 were visually inspected. [Publisher record](https://annals.math.princeton.edu/1989/130-3/p01).
- **Wang09:** Lu Wang, *A Bernstein Type Theorem For Self-similar Shrinkers*, arXiv:0912.1809v1, December 9, 2009, seven pages. Theorem 1.1 and Lemmas 2.1–2.3 were checked; pages 5–6 were visually inspected. [Versioned source](https://arxiv.org/abs/0912.1809v1).
- **ABR01:** Sheldon Axler, Paul Bourdon and Wade Ramey, *Harmonic Function Theory*, second edition, Springer copyright 2001; inspected author PDF dated July 17, 2020. Chapter 5, printed pages 74–81, contains Proposition 5.5, Theorem 5.7, Proposition 5.8, Proposition 5.9 and Theorem 5.12. Printed page 81 was visually inspected. [Author edition](https://www.axler.net/HFT.pdf).

Exact hashes and selected-passages records appear in the source inventory. Source PDFs, extracted text and private working files are not redistributed. The manuscript contains original exposition and derivations.

The flow uses the upward graph normal, the shape operator obtained by differentiating that normal, scalar mean curvature equal to its trace, and normal velocity minus scalar mean curvature times the normal. A normal material derivative and the derivative at a fixed base coordinate are explicitly distinguished. The graphical tangential drift is derived before any maximum principle is used. Self-shrinkers use the normalization with the factor one half in the position-normal equation.

## Graphical flows

The vertical-angle equation gives the reciprocal-angle and power equations. An exact tensor-square calculation controls slope-weighted squared curvature, including at curvature zeros. A time-weighted quantity then yields curvature smoothing from the starting slope alone. On a periodic graph these are compact maximum-principle arguments. Uniformly bounded ancient periodic slopes force a stationary horizontal graph; the grim reaper demonstrates why the domain and slope assumptions matter.

For all-time smooth periodic flows, graph curvature controls the Euclidean Hessian, periodicity controls the slope and height oscillation, and nested height intervals identify the limiting horizontal slice. The proof gives polynomial C2 convergence. The area functional has a variable mobility, whose dissipation and the torus Poincare inequality give exponential area and gradient-energy decay. A local interpolation argument upgrades this to exponential C1 convergence. Total squared-mean-curvature dissipation is exactly the initial area excess.

Entire graphs receive a separate maximum-principle proof with an explicit polynomial-growth barrier. The graph-coordinate heat operator cancellation is proved, and bounded-slope/curvature slab assumptions justify the drift estimates. Those assumptions remain in the ancient entire-flow rigidity and uniqueness statements; smoothness on a noncompact slice is not substituted for a global bound.

The Ecker–Huisken globally Lipschitz entire-graph existence theorem is cited with its slope, higher-curvature-derivative and approximation conclusions. Its proof remains external. Smooth periodic existence follows from it by translation and uniqueness. The manuscript does not claim to prove existence solely from an a priori curvature estimate, nor attribute later unrestricted local-Lipschitz theory to the 1989 paper.

Examples separate conservation of mean height for periodic curve graphs from its failure on a two-dimensional torus. A trigonometric initial graph gives an explicit nonzero cubic mean-height velocity. A single decaying Fourier mode is compared with the nonlinear equation by its exact residual; it is not presented as an exact nonlinear solution.

## Entire graphical self-shrinkers

The positive vertical angle gives a Gaussian quadratic identity for the shifted Jacobi operator. Completeness and finite Gaussian area then permit intrinsic exhaustion cutoffs and force a flat image, without a uniform positive angle bound.

For an entire graph, those growth assumptions are conclusions. Compact-flow avoidance is justified by uniform compactness of closest pairs, then shrinking spheres give a linear height bound. A cylinder divergence comparison bounds graph area using height and mean curvature. The shrinker equation converts that estimate into polynomial area growth and hence finite Gaussian area. The resulting Bernstein theorem therefore assumes only a smooth entire graphical self-shrinker in any dimension. It does not assume the conclusion of its growth lemma.

The cylinder proof avoids imposing an unproved topology on an intersection with a sphere. A spherical hemisphere is a worked example showing why positivity of the angle and finite Gaussian area do not replace completeness or an entire domain. Source normalization and typographical issues were checked rather than copied into the derivation.

## Spherical harmonics and replaced proof dependencies

The coefficient inner product makes multiplication by squared radius adjoint to the Euclidean Laplacian. Finite-dimensional orthogonal decomposition then gives harmonic polynomial decomposition and dimensions. The polar Laplacian gives the eigenvalues; orthogonality and polynomial approximation give the complete L2 expansion.

The Sobolev energy expansion is justified separately. Finite harmonic projections first satisfy a gradient-energy bound, which makes their partial sums Cauchy in H1. This proves derivative convergence rather than inferring it from L2 convergence alone. The expansion gives all weak eigenfunctions, sharp higher-mode gaps, their equality cases, second and fourth coordinate moments, explicit low-mode projections, and a mean-zero weak Poisson inverse with quantitative bounds.

The round-shrinker F-stability proof now obtains its second positive gap from this section. The geodesic CMC sphere nullity proof obtains its eigenspace and dimension from the same local expansion. Their earlier external spherical-harmonic steps are removed. Stone–Weierstrass approximation, continuous-function density for a finite Radon surface measure and completeness of H1 remain stated background inputs. The weak inverse does not assert additional elliptic regularity or operator-domain results without proof.

## Review and publication

Existing labels, permanent tags and reader numbers are retained. A duplicate normal-Laplacian lemma was removed during preparation and the established Gauss-map result reused. No canonical merge or source-specific renderer was introduced. Explanatory forward links are excluded from proof dependencies where they would create a false reverse dependency.

Publication requires the Python and JavaScript suites, a complete build and link checks, mathematical rendering, desktop/mobile reader inspection, proof disclosure and citation-return checks, followed by native GitHub Pages delivery verification. Supplementary Fourier-grid and surface-quadrature checks support the calculations; they are not formal verification. No independent human review is claimed.
