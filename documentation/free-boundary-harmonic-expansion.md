# Free boundaries, CMC reconstruction, and harmonic-map energy

This expansion adds 42 entries with 37 local proofs in seven sections. Free-boundary theory joins the minimal-surface chapter, Gauss maps and reconstruction join CMC theory, and three worked-example sections extend Examples. A new final chapter, Harmonic maps and variational systems, holds domain stationarity and energy monotonicity. Existing chapter and entry locations are preserved.

## Sources and conventions

- Fraser, *On the free boundary variational problem for minimal disks*, CPAM 53 (2000), 931–971: Section 2.1, p. 960 and Theorem 2.9, pp. 967–970. The supplied PDF was checked, including the instability calculation in the source image. We give the ambient-flow and hypersurface normal second variations and the conformal-field instability proof in every positive codimension.
- Fraser–Schoen, *The first Steklov eigenvalue, conformal geometry, and minimal surfaces*: the checked text is arXiv:0912.5392v2, December 3, 2010, Sections 1 and 3, especially PDF pp. 6–9; journal metadata is Advances in Mathematics 226 (2011), 4011–4030. The v2 conclusion of Theorem 3.1 prints `t=cosh(t)` where its preceding condition and proof give `t=coth(t)`. We derive the boundary condition directly. No unrestricted annulus optimization theorem is imported.
- Hélein, notes by Moser, *Constant Mean Curvature Surfaces, Harmonic Maps and Integrable Systems*, Birkhäuser, 2001: printed pp. 18–21 (Gauss maps and reconstruction), 22–33 (variations and Noether's theorem), and 34–37 (Hopf differentials and CMC spheres). The supplied scan was visually read; text extraction alone is empty. We use trace mean curvature and the second fundamental form given by the derivative of the normal. The source uses the opposite form and the averaged scalar curvature. The reconstruction is asserted to be an immersion only where its conformal factor is positive.

The bibliography and source inventory distinguish the versions and mark the source files as not redistributed. Public material is original exposition with local derivations.

## Proof coverage and restrictions

The free-boundary section proves the area/boundary identity, elementary Steklov identities, coordinate eigenvalue one, and instability. It does not infer that eigenvalue one is always the first positive eigenvalue. The disk and critical catenoid examples calculate that first eigenvalue directly by Fourier separation. The disk has a complete index/nullity calculation; the catenoid section exhibits an unstable direction without claiming its full Morse index. Moving-boundary variations are distinguished from Dirichlet variations.

The harmonic Gauss-map equation, conformal invariance, Hopf differential, and conformally parametrized CMC-sphere theorem have local proofs. Genus-zero uniformization remains an explicit external input for the topological-sphere formulation. Basic complex analysis, Fourier expansions, and ordinary Sobolev absolute continuity are background tools, not claims of new formal verification.

CMC reconstruction includes the closed form, its period obstruction, metric and sign calculations, and its degeneration criterion. The cylinder, sphere/constant-map pair, harmonic phases, and logarithmic period example prevent local formulas from being read as a global immersion theorem.

The stress-energy calculation is derived from the checked Noether framework. Radial energy monotonicity is proved from domain stationarity, which is a separate assumption for weak maps. The normalization uses half the squared gradient, fixing the coefficient in the monotonicity formula. The radial projection example checks the weak equation and domain variation across its singular point; it is not asserted to minimize energy. Two-dimensional bubbles show energy measures concentrating while maps converge weakly. Explicit higher-degree energies are not a general quantization theorem.

## Validation

See the local batch audit for exact test and browser receipts. The standard Python and JavaScript suites, complete build/link checks, old-location preservation, mathematical rendering, and desktop/mobile proof and citation behavior are required before publication. No formal verification or independent human review is claimed.
