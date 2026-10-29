# Delaunay geometry and Cantor-set examples

This expansion adds 33 entries and 31 local proofs in five sections. Rotational equations and Jacobi fields join the CMC chapter; unduloid limits and two measure-theory sections join Examples. The existing reader locations are preserved.

## Sources and conventions

- Mazzeo, *Recent advances in the global theory of constant mean curvature surfaces*, arXiv:math/0209330v1 (2002), Sections 2.1–2.3, pp. 4–10: graph equations, flux, conformal coordinates and geometric Jacobi fields. The source normalizes trace mean curvature to one. Its first integral is minus twice the constant used here. Statements about periodic positive solutions require the domain and flux restrictions: a positive spherical graph on a finite interval is a counterexample to an unrestricted claim.
- Bendito–Bowick–Medina, *Delaunay Surfaces*, arXiv:1305.5681v1 (2013), pp. 2–6: rotational metric, curvature and roulette formulas. The local manuscript uses the derivative of the normal as its second fundamental form and trace mean curvature. Its arclength construction and limits are derived directly.
- Morgan, *Geometric Measure Theory: A Beginner's Guide*, fifth edition (Academic Press, 2016), printed pp. 33 and 36–37, and Exercise 4.17 on p. 59: positive-length Cantor sets, four-corner dust and a rectifiable nonintegral current. The supplied copy's title, edition and relevant source images were checked. Its existing inventory record is upgraded rather than duplicated.

The source inventory records exact file hashes and checked passages. Source books, papers and extracted full text are not redistributed.

## Scope of the local proofs

The unduloid construction proves the rotational CMC system, its first integral, completeness, proper embeddedness, and the cylinder, sphere-chain and catenoid-neck limits. Smooth convergence at a collapsing neck is asserted only after the appropriate dilation; the undilated sphere chain is not a smooth embedded surface at its contact points.

The axial period has a strictly positive derivative with respect to neck radius. This proves the drift of the neck Jacobi field. An elementary positive-potential barrier eliminates higher angular modes, leaving precisely the three translations in the bounded kernel of a noncylindrical complete unduloid. A separate cutoff argument proves that its square-integrable kernel is zero. No unweighted closed-range or weighted Fredholm conclusion follows from those kernel statements alone. The cylinder endpoint is excluded from the unduloid kernel theorem and is calculated separately.

The periodic cylinder lies in the flat ambient quotient of Euclidean space by an axial translation. Its constrained index, nullity and stability threshold are obtained by Fourier expansion. The infinite cylinder has a compactly supported zero-mean unstable speed; exact volume correction concerns the finite signed volume change under that perturbation.

The fat Cantor example proves positive measure, empty interior, approximate continuity and infinite perimeter. Its associated multiplicity-one rectifiable current has finite mass but infinite boundary mass. The four-corner example proves finite positive one-dimensional Hausdorff measure, cylinder differentiation, a quantitative line obstruction and pure unrectifiability. The last proof explicitly retains the external rectifiable tangent theorem. Coarse ball estimates do not establish the source's exact Hausdorff-measure value. The projection calculation treats specified directions, not a general projection theorem.

The geometric Steklov corollary also explicitly assumes a connected immersion, matching the connectedness in the preceding definition.

## Validation

Run the standard Python and JavaScript tests, complete build and link checks, preservation of old tags and reader locations, mathematical rendering, and desktop/mobile proof and citation checks before publication. Numerical checks of the unduloid formulas are supplementary sanity checks, not proof or formal verification. No independent human review is claimed.
