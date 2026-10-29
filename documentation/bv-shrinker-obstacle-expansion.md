# BV representatives, shrinker gaps and an obstacle transition

This expansion adds seven subject sections, 36 entries and 36 local proofs. Existing tags and reader locations are retained. The existing definition of BV now links to a local proof of its vector-measure representation.

## Source evidence and conventions

- Simon, supplied 2017/2018 *Introduction to Geometric Measure Theory*, Chapter 2, equations (2.1)–(2.4), printed pp. 52–53 (two-up PDF page 30): the distributional definition and variation measure for BV functions.
- Colding–Minicozzi, *Generic mean curvature flow I; generic singularities*, printed pp. 808–809 (supplied PDF pages 54–55), Lemma 10.8 and equations (10.15)–(10.17): the shrinker tensor identity and the logarithmic mean-curvature test. The source's later global integrability conclusions are not imported.
- Cao–Li, *A Gap Theorem for Self-shrinkers of the Mean Curvature Flow in Arbitrary Codimension*, arXiv:1101.0516v2, February 2, 2012, pp. 1–3 and 7–9: gap theorems and higher-codimension model examples. Their normalization is (\vec H=-X^\perp); dilation by (\sqrt2) converts to this project's (\vec H=-X^\perp/2), and divides squared curvature by two.
- Figalli, *Free boundary regularity in obstacle problems*, author-hosted notes, pp. 8–12, especially equation (5.2): the normalized obstacle equation and regular/singular blow-up models.

Exact file hashes and checked passages are recorded in the source inventory. The exposition and calculations are original; source PDFs and full-text extracts are not redistributed.

## BV proofs and representative examples

The representation argument uses the already proved finite-dimensional vector Riesz theorem and identifies its variation with the open-set supremum in the BV definition. On a bounded interval, a finite signed measure gives a right-continuous cumulative function; all BV classes have this representative up to a constant. The text proves one-sided traces, atom/jump correspondence, classical variation, absolute continuity, Lipschitz characterizations, and the finite-interval structure of one-dimensional sets of finite perimeter. Relative perimeter excludes the domain endpoints; zero extension adds the two trace atoms.

The nonlinear chain rule treats the jump coefficient as a divided difference. A continuous divided-difference kernel and partitions yield a proof against the full variation measure, including its singular continuous part. The product rule uses midpoint representatives at common jumps, and integration by parts includes boundary traces. Examples show why applying a derivative at a midpoint gives the wrong coefficient for nonlinear jumps, why a singular continuous derivative survives composition, and why arbitrary almost-everywhere representatives need not have bounded pointwise variation. A boundary-layer example records the failure of trace continuity under mere (L^1) convergence with bounded variation.

These arguments do not establish the multidimensional jump-set structure theorem or the full multidimensional BV chain rule. Completeness of Lebesgue spaces, elementary one-dimensional integration and smooth approximation remain background inputs.

## Shrinker gap and higher-codimension examples

The hypersurface convention is (A=D\nu), (H=\operatorname{tr}A), and (H=\langle X,\nu\rangle/2). The proof first derives the tensor drift identity and a cutoff estimate. Intrinsic completeness, no boundary and finite Gaussian area then force parallel second fundamental form under (|A|^2\leq1/2). A separate complete-image proof classifies parallel hypersurfaces and imposes the shrinker equation to center and size the resulting plane or cylinder. The conclusion concerns the immersion's image and does not silently assert injectivity. Local test functions are supported away from any boundary.

The positive-mean-curvature estimate is a compact-test weighted inequality, not a classification theorem or a claim of entropy stability. The higher-codimension section distinguishes spherical minimal submanifolds from round hyperspheres. It computes products of spheres and a Clifford torus, their Gaussian areas at the specified center and scale, and their Euclidean and spherical curvature norms. These Gaussian-area calculations are not claims that a supremum defining entropy has been attained there. A cutoff proof gives the Gaussian radial moment under polynomial volume growth. Compactness and a separate sign computation exclude closed expanders.

## An explicit obstacle problem

For (J(u)=\int(\tfrac12|\nabla u|^2+u)) on a ball in dimension at least two, with lower obstacle zero and constant boundary value (h), a radial formula gives the unique minimizer. Verification uses the variational inequality against all admissible competitors. Below the threshold (h=R^2/(2n)), the contact set is a concentric ball; at the threshold it is a single point; above it the contact set is empty. Continuous matching of the gradient removes any spurious surface measure from the distributional Laplacian.

The section computes the reaction, regular and singular blow-ups, contact-radius asymptotics and the derivative of minimum energy with respect to boundary height. At the threshold the point contact set carries no reaction measure. These exact examples illustrate free-boundary alternatives; they do not prove general free-boundary regularity.

No independent human review or formal verification is claimed. Deeper rectifiability, singular-flow and free-boundary regularity results retain their external proof dependencies.
