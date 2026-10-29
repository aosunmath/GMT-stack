# Local graphical estimates and cone expanders

This expansion adds 31 entries with 30 local proofs in six sections. The edition contains 1,059 mathematical and historical entries, 832 local proofs, 44 cited theorems with external proofs, 154 sections and 17 chapters. Including section headings gives 1,213 addressable tags. Existing tags, reader numbers and routes are preserved.

## Source and conventions

The principal new source is Klaus Ecker and Gerhard Huisken, *Interior estimates for hypersurfaces moving by mean curvature*, Inventiones Mathematicae 105 (1991), 547–569, [DOI and publisher record](https://link.springer.com/article/10.1007/BF01232278). The supplied 23-page journal copy was checked at Theorem 2.1 and Remark 2.2, Theorem 2.3, Theorem 3.1 and Corollary 3.2, equation (20), Theorem 3.4 and Remark 3.6, and Theorem 5.1 with Remark 5.2. Printed pages 550, 552–553, 555 and 567 were visually inspected. Exact hashes and passage records are in the source inventory. The earlier Ecker–Huisken 1989 globally Lipschitz-data theorem is reused with its distinct scope.

The exposition treats Euclidean hypersurface graphs in every dimension at least one. It uses the upward normal, scalar mean curvature equal to the trace of its derivative, and normal velocity equal to minus scalar mean curvature times that normal. The normal material heat operator is converted explicitly to graph coordinates. Expanders use the position-normal factor one half. No source PDFs or full-text extracts are redistributed.

## Local estimates and comparison

Ambient and base cutoffs have their heat operators and support properties computed explicitly. The localized reciprocal-angle estimate proves slope preservation without imposing polynomial growth at later times. A rational curvature weight has an exact tensor-square identity, valid also at curvature zeros. Time-weighted cutoff maxima then give curvature estimates on fixed base balls and shrinking ambient balls. The spatial-radius term is distinguished from the positive-time term.

Letting the base radius tend to infinity gives automatic curvature control for an entire bounded-slope flow. This supplies the hypotheses for the earlier sharper weighted estimate. Ancient bounded-slope rigidity therefore no longer needs a separate slab-curvature assumption. The bounded-gradient minimal-graph consequence holds in every dimension; it is distinct from the unrestricted Bernstein problem.

A polynomial barrier with a time-integrable drift gives comparison and uniqueness from locally continuous initial traces in the bounded-slope class. Curvature smoothing bounds the comparison drift by a constant times inverse square-root time. The proof does not assume differentiability of the initial graph or a uniform initial curvature bound. Convex initial data can be compared with their supporting affine planes and with time shifts, proving strictly upward motion for nonaffine data. This argument proves the sign of motion, not preservation of convexity of the second fundamental form.

## Heights and arbitrary growth

Compact-flow avoidance is extended to locally uniform continuous initial traces by keeping closest points in a common compact base ball. Shrinking spheres yield local height bounds and an optimized one-half time Hölder estimate for globally Lipschitz initial functions. Vertical translation and comparison yield uniform contraction. The shrinking-sphere estimate does not require a later global slope bound.

The height-dependent cutoff argument of Ecker–Huisken is developed with explicit, nonoptimal constants. Its intrinsic mixed-gradient estimate forces a reciprocal-angle bound at a positive maximum. Combining this with local sphere barriers and the base curvature estimate gives a priori geometry from initial height and slope on a larger ball.

The all-time existence theorem for arbitrary locally Lipschitz entire graphs remains external. Its boundary-value construction, higher derivative estimates, exhaustion and approximation are not inferred solely from the proved estimates. No uniqueness theorem for unrestricted unbounded-slope entire flows is asserted. A superexponential initial graph illustrates the distinction between this nonlinear existence theorem and divergence of the corresponding positive heat-kernel integral.

## Examples and expanders

The explicit planar corner models show that the one-half time exponent and inverse square-root curvature scale occur in actual solutions. Their tip-to-asymptotic-slope map is proved continuous, strictly increasing and onto the positive slopes. The proof uses local ODE dependence with uniform tails, not monotonicity alone. Graphical comparison then gives uniqueness for each symmetric corner within the bounded-slope graphical class. A scaled Scherk graph proves the necessity of the spatial-radius term in local curvature estimates.

For every globally Lipschitz positively homogeneous graphical cone, global existence and uniqueness imply self-similarity by parabolic rescaling. The resulting expander has a uniform height error from the cone and a quantitative blow-down estimate. Order, base rotations and height reflection pass from the initial cone to the profile. Completeness and proper embedding of the entire graph are justified directly.

Radial cones give examples in every dimension, with an exact relation between tip height and tip curvature. A saddle cone gives an entire nonflat expander with changing-sign height and mean curvature, and zero height and mean curvature at the origin. The sign-change argument uses antisymmetry together with the fact that a smooth homogeneous minimal expander graph would be linear. Convex nonaffine cones instead have strictly positive expander defect. None of these results classifies arbitrary immersed expanders or weak flows.

## Proof boundaries and checks

Local proofs are separated from external existence and regularity inputs. The classical local strong maximum principle, finite-dimensional supporting-hyperplane theorem, and smooth ODE dependence are stated background. Earlier weaker statements keep their permanent locations; explanatory references to them are not treated as logical proof dependencies. No canonical merge was made.

Publication requires Python and JavaScript tests, a complete build with link checks, actual-page mathematical rendering, desktop/mobile reader checks, proof disclosure and citation-return checks, and exact native GitHub Pages delivery verification. Supplementary numerical checks cover tensor contractions, optimized sphere barriers, expander ODEs and the height-cutoff cross term. These checks are not formal verification, and no independent human review is claimed.
