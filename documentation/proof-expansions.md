# Reviewed proof expansions

The empty GMT edition has no proof additions or unresolved dependency inventory. Pome’s proof fragments and review records were removed with its mathematical content.

The reusable machinery in `scripts/proof_expansions.py` remains. A future source integration may create a proof registry and explicitly set `proof_expansions` in `collection.json`. Each added argument must identify the source statement, preserve its hypotheses, record statement and original-proof fingerprints, and give checkable dependencies. Changed source mathematics requires fresh review.

Additional prose is not a formalization certificate. Formal proof evidence belongs in `formalizations.json`; see [formalizations](formalizations.md). Keep source attribution and distinguish complete proofs from external inputs and unresolved gaps.
