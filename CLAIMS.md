# v3 claims and evidence boundaries

This ledger covers the v3 scalar completion extension, full-support specialization, and vector obstruction. It is a reader-facing scope map, not a review decision or an assertion that publication gates have been completed. The integrated manuscript is authoritative.

## Claim map

| Claim | Precise domain and conclusion | Evidence | Do not infer |
|---|---|---|---|
| Posterior reduction | Finite signals, real square-integrable target, positive source prior, and disclosures independent of `(B,Y)` conditional on `A`. The gap is `E[D-N]`; every posterior can be embedded at every fixed positive prior. Structural zeros are allowed. | Conditional-variance proof and special-report construction. Direct score calculations test supplied examples. | That disclosure randomness may depend on the hidden target or second signal; that a finite disclosure grid establishes the identity. |
| Arbitrary-support completion equivalence | For each finite `C>=0`, `N(q)<=C D(q)` for every posterior iff every distinct scalar source mean has a simultaneous row-loss completion satisfying the stated inequalities. | Compact-box clipping, Sion minimax necessity, and interpolation between adjacent scalar knots. | Pairwise sufficiency on sparse support; a vector analogue; novelty of minimax duality. |
| Finite convex characterization | At most `n` knot systems, each with at most `n` convex quadratic row constraints and `m` completion coordinates. Fixed-`C` problems are SOCP representable; minimizing `C` is a convex QCQP. | Theorem 5 and Corollary 6 of the integrated manuscript. | An implemented general solver, exact acceptance of floating-point solver output, or a proved bit-complexity bound. |
| Finiteness and attainment | A finite coefficient exists iff equal-mean source rows agree on each column they both support. When finite, the QCQP minimum is attained. | Compatibility argument and compactness proof. | Equality of undefined null-cell means; rationality of an optimum or of all feasible completions. |
| Rational failure witnesses | With rational model and threshold, infeasibility yields some rational posterior with strict `N>C D`. At `C=1`, rational positive prior yields a rational negative-gap disclosure. | Positive minimax separation, continuity and density, followed by posterior embedding. | A uniform separation margin, polynomial certificate length, or an efficient complete rational search. |
| Full-support sharp formula | For a scalar target and positive mass in every signal cell, the coefficient is the maximum directed row ratio; incompatible equal-mean rows give infinity. Finite nonconstant models have normalized worst-gap infimum `1-C_*` at every positive prior. | Analytic proof, boundary posterior sequence, and full-support exact test suites. | Attainment of the limiting normalized gap by a nondegenerate interior posterior; prior-independence of absolute effects. |
| Strict quantitative substitution | In the full-support scalar result, finite `C_*<1` bounds gap below by `(1-C_*) E[D]`; zero gap occurs exactly when the disclosure determines the scalar source mean. | Written proof; quantitative examples. | That zero gap always requires revealing the entire source state when source means repeat. |
| Sparse family sharp coefficient | For the displayed three-row family, `C_*=4a^2/(a+b)^2`, hence `16/9` at `(a,b)=(1,1/2)`. Every two-row posterior can pass although a three-row posterior fails. | Two explicit knot completions, forced-coordinate lower bound, and analytic ratio along `q=(s,(1-s)/2,(1-s)/2)`. `completion_exact.py` checks the concrete rational instance. | That a finite grid proves sharpness or classifies all sparse models. |
| Full-support vector obstruction | Two three-valued signals and a two-dimensional quadratic target have six positive directed pair margins but a negative global residual. Edge concavity proves every two-state posterior passes in the stated orientation. | Exact table, analytic edge argument, and `vector_exact.py`. | Failure of the scalar theorem; impossibility of every alternative vector characterization; both-orientation success of all binary restrictions. |
| Four-category realization | The vector counterexample maps affinely into positive four-category probabilities, scaling squared differences and residuals by `1/200`. | Explicit probability map and norm identity; code checks cellwise positivity and normalization. | That four categories are minimal, or that this is a binary-target counterexample. |
| Two-sided scalar property | Apply the appropriate scalar criterion to both signal orientations, with the reversed conditional table obtained by Bayes' rule. | Same theorem applied twice. | Unrestricted submodularity between arbitrary garbled signals or a multi-signal classification. |

## What the four verification programs establish

`verify_release.py`, `test_sharp_coefficient.py`, `completion_exact.py`, and `vector_exact.py` can be run normally and under `python3 -O`; see `README.md`. Their explicit exception checks remain active. The full-support release wrapper repeats critical returned-witness checks even though the legacy helper contains an assertion. The wrapper also calls the sharp suite, so separate execution does not create independent unique coverage.

They provide exact rational arithmetic for executed cases, check model/certificate properties within their documented interfaces, and compare posterior residuals with direct four-score aggregation. The sparse checker rejects deliberately corrupted supplied certificates. They do **not** formally verify the proofs, solve the general conic optimization problem, or certify an infinite statement by enumeration.

Three different evidence levels must stay separate:

1. **Proof:** the written argument establishes universal equivalence and sharpness.
2. **Certificate verification:** a supplied rational completion or strict violating posterior is checked by exact arithmetic. Acceptance depends on the theorem connecting the certificate to the universal claim.
3. **Search or optimization:** a diagnostic grid or numerical solver may find a candidate; finite failure to find one does not prove nonexistence, and floating-point feasibility is not exact feasibility.

Historical `exact.py` regression and `test_extensions.py` use assertions and may overwrite historical JSON receipts when invoked. They are not the optimized-Python verification standard. Historical review hashes cover historical bytes only.

## Exact numerical anchors

For the full-support symmetric scalar example, the coefficient is `100/289` in each orientation. For the sparse instance, uniform-posterior residual is `-1/24`; embedding the same posterior as a report of mass `1/2` yields gap `-1/48`. These are consistent results for different disclosure channels.

For the vector example, the maximum directed ratio is `4529900/4824097 < 1`, while the uniform-posterior ratio is `90354732925/83974161964 > 1`. Thus the directed ratio is **not** the sharp global vector coefficient. The exact uniform-posterior gap is `-708952329/4119500000`.

## Originality and scope of literature evidence

The prior-art notes record targeted primary-source comparisons and dated queries. They distinguish the existing binary-source predecessor, generic posterior splitting, mean elicitation, optimal garbling, binary SDPI extremizers, Sion minimax, and standard QCQP/SOCP conversion from the candidate's scalar finite-knot reduction. No blanket first-result claim follows from these searches.

Use `PRIOR_ART.md`, `NOVELTY_REFRESH.md`, and especially `SPARSE_EXTENSION.md` for inspected locators and unresolved translation questions. Relevant primary sources include [Chen–Waggoner](https://arxiv.org/abs/1703.08636), [Sion](https://doi.org/10.2140/pjm.1958.8.171), [Lobo et al.](https://web.stanford.edu/~boyd/papers/pdf/socp.pdf), and [Ordentlich–Polyanskiy](https://arxiv.org/abs/2010.01987). Related extension geometry and finite-action substitution work are compared in the notes rather than represented as equivalent theorems.

No empirical prediction-market improvement, statistical confidence bound for estimated tables, strategic-equilibrium theorem without additional assumptions, unrestricted informational-substitutes solution, numerical star rating, publication status, or external peer-review endorsement is asserted by this ledger.
