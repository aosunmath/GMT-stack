# First GMT reading

This guide records the original foundational batch, now part of the broader [variational reference](variational-sources.md). That batch is an initial collection of original exposition based on the six supplied files, representing five distinct works or editions. It contains 39 mathematical/editorial entries in nine sections and six subject chapters. The source manuscript is in `content/gmt-foundations/`; each entry keeps a stable label and a generated permanent GMT tag.

| Reference | Edition identified from the supplied file | Use in this batch |
| --- | --- | --- |
| Federer, *Geometric Measure Theory* | Springer-Verlag, 1969 | Hausdorff normalization (§2.10.2), rectifiability terminology (§3.2.14), area (§3.2.3), coarea (§3.2.22), mass and comass (§1.8) |
| Simon, *Introduction to Geometric Measure Theory* | Title-page copyright 2017, 2018 | Main source for measures, rectifiability, BV, finite perimeter, currents, varifolds |
| Simon, *Introduction to Geometric Measure Theory* | Title-page copyright 2014 | Separate earlier edition; retained for comparison, without duplicate entries |
| White, *Topics in GMT (Math 258)*, notes by Chodosh | November 6, 2014 | Polyhedral chains and flat norm, §§2.1–2.3, pp. 4–8 |
| Fleming, *De Giorgi and Geometric Measure Theory* | 2016 Pisa tribute article | Historical context, §§3–5, pp. 3–7 |

`Topics in GMT_White.pdf` and `Geometric measure theory_White_Chodosh.pdf` have identical SHA-256 hashes. They are one source. The Simon PDFs are different editions, and citations must not transfer page numbers between them. Citations use printed page numbers; both Simon PDFs generally place two printed pages on a PDF page. Federer's numbered sections provide an additional stable locator. The 2014 Simon PDF has a damaged text encoding; its title and edition were checked from the rendered page.

## Reading structure

1. **Introduction:** source editions, notation, prerequisites, and conventions.
2. **Measure theory:** Radon measures and weak convergence; Hausdorff measure, Lipschitz distortion, and density.
3. **Rectifiability and integration:** countable rectifiability, Rademacher, approximate tangents, area and coarea, graph area.
4. **Sets of finite perimeter:** BV, variational perimeter, lower semicontinuity, reduced boundary, De Giorgi and Gauss–Green.
5. **Currents and flat chains:** boundary and mass, integer rectifiability, compactness, polyhedral chains, flat norm and examples.
6. **Varifolds:** weight, rectifiable and integral varifolds, first variation, stationarity, monotonicity.

## Conventions requiring attention

- Hausdorff measure is normalized to agree with Lebesgue measure in its own Euclidean dimension.
- This draft's countable rectifiability allows an exceptional Hausdorff-null set. Federer calls this countable `(H^m,m)` rectifiability; his unqualified countably `m` rectifiable sets are exact countable unions.
- The reduced-boundary normal points outward. Simon's Chapter 3 uses the inward normal, so the distributional derivative here is `Dχ_E = −ν_E |Dχ_E|`.
- Current mass uses comass. Simon's initial Euclidean-covector convention agrees on rectifiable currents but need not agree on arbitrary currents.
- Flat-chain entries currently use integer coefficients and ambient fillings. They do not assert compactness or rectifiability for arbitrary normed coefficient groups.

## Proof coverage and provenance

Eight entries have complete local proofs. Eight deeper theorems explicitly refer to external proofs; related facts used inside definitions are also identified in the manuscript and `entry-review.json`. The expanded current draft does not claim independent human review or formal verification. `formalizations.json` remains empty.

The next additions should develop the covering and differentiation lemmas, then proofs of Rademacher and area/coarea, BV compactness and De Giorgi's blow-up theorem, the deformation theorem, and varifold monotonicity. Allard regularity and area-minimizing regularity require that foundation.

The public source page includes a reference inventory and entry-status record. Local manuscript builds use a SHA-256 manifest of the exact source files, rather than claiming that uncommitted text belongs to a Git commit. Remote source adapters continue to require exact Git revisions.

The supplied books, scans, and extracted full text are not redistributed. Their copyrights remain with the original holders. The project contains newly written exposition and citations. The existing MIT license and attribution for Pome's infrastructure are retained.
