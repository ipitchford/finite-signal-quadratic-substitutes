# Finite quadratic informational substitutes — v3 reader guide

Release version: **0.1.0-candidate**, 2026-10-15. Scholarly creator: Anonymous. DOI: [10.5281/zenodo.23401650](https://doi.org/10.5281/zenodo.23401650). This AI-assisted research is not externally peer reviewed. See STATUS.md for the qualified academic assessment and publication boundary.

This candidate studies when every randomized disclosure of one finite signal preserves a specified diminishing-returns inequality under scalar quadratic value. Version 3 adds an exact finite convex characterization for arbitrary signal support, including structural zeros. The explicit directed-pair formula remains the simpler full-support specialization.

The written mathematical proofs establish the universal statements. The accompanying Python programs verify supplied examples and certificates using rational arithmetic; they are not proof assistants, general conic solvers, or exhaustive searches over disclosures. This guide makes no publication, external-peer-review, priority, or rating claim.

## What the results say

Let `r[i][b] = P(B=b | A=i)` and, only on supported cells, `v[i][b] = E[Y | A=i,B=b]`. The source prior `pi` is positive, each row of `r` sums to one, and `x[i]` is the corresponding row mean. An admissible disclosure `T` uses only `A` and fresh independent randomness: `T` is conditionally independent of `(B,Y)` given `A`.

For `V(S) = E[E(Y|S)^2]`, the oriented substitution gap is

```text
G(T) = V(T,B) - V(T) - V(A,B) + V(A).
```

For a posterior `q` on `A`, let `D(q)` be the variance of `x` and `N(q)` the remaining conditional variance of the cell means after observing `B`. Then `G(T) = E[D(q(T))-N(q(T))]`. The sharp coefficient is the least nonnegative `C` such that `N(q) <= C D(q)` for every posterior.

- **Arbitrary support, scalar target:** for every distinct row mean `t`, find a completion vector `z[t]` satisfying `sum_b r[i][b](v[i][b]-z[t][b])^2 <= C(x[i]-t)^2` for every row, with sums restricted to supported cells. These finitely many systems are necessary and sufficient. Fixed-`C` feasibility is second-order-cone representable; minimizing `C` gives a convex quadratically constrained program. Set `C=1` to test oriented substitution.
- **Full rectangular support, scalar target:** the completion at a row mean is forced to be that row's conditional-mean vector. The coefficient becomes an explicit maximum of directed pair ratios. Equal-mean rows with unequal vectors instead give an infinite coefficient.
- **Sparse finiteness condition:** a finite coefficient exists exactly when equal-mean rows agree in every column they both support. They need not agree on nonexistent cells. If the coefficient is finite, the convex program attains it.
- **Two-sided substitution:** apply the relevant scalar criterion again after exchanging the two signals. The theorem uses the two-base-signal definition, not unrestricted submodularity among arbitrary garblings.

For rational input, strict failure admits a rational posterior and a rational rejecting disclosure. This existence result does not supply a polynomial search bound or guarantee that optimal feasible completions are rational.

## Read the evidence in this order

| File | Purpose |
|---|---|
| `paper.tex`, `paper.pdf` | Main manuscript source and rendered paper; use the final matching pair from the frozen bundle. |
| `CLAIMS.md` | Claim-by-claim scope and evidence boundaries. |
| `verify_release.py` | Hardened full-support regression, direct disclosure-score checks, invalid-input cases, and sharp-coefficient tests. |
| `test_sharp_coefficient.py` | Separately runnable full-support coefficient and limiting-disclosure tests. |
| `completion_exact.py` | Sparse scalar model parsing, rational completion verification, posterior evaluation, and rejecting-disclosure checks. |
| `vector_exact.py` | Exact arithmetic for the vector obstruction and categorical embedding. |
| `PRIOR_ART.md`, `NOVELTY_REFRESH.md`, `SPARSE_EXTENSION.md` | Bounded literature searches, source mappings, and unresolved equivalence questions. |

Historical review reports and receipts are bound to their named inputs. They do not automatically certify later manuscript or code revisions. The integrated manuscript contains all proofs; no development fragment is required.

## Run the four verification programs

Python 3 and its standard library are sufficient for these four programs. From the package directory, run each normally and with assertions disabled:

```sh
python3 -B verify_release.py
python3 -B -O verify_release.py
python3 -B test_sharp_coefficient.py
python3 -B -O test_sharp_coefficient.py
python3 -B completion_exact.py
python3 -B -O completion_exact.py
python3 -B vector_exact.py
python3 -B -O vector_exact.py
```

These entry points print their results rather than regenerate the historical JSON receipts. `-B` suppresses bytecode-cache writes. `verify_release.py` already invokes the sharp-coefficient suite; running it separately is an explicit additional entry-point check, not independent evidence or additional unique coverage. The active checks use explicit exceptions. Although the full-support helper retains an internal assertion, the release wrapper independently rechecks its returned witnesses even under `-O`.

Expected exact anchors include:

- full-support three-state example: `C = 100/289` in both orientations;
- sparse cyclic family at `a=1, b=1/2`: `C = 16/9`;
- sparse uniform posterior: `D = 1/8`, `N = 1/6`, residual `-1/24`;
- that posterior embedded with special-report mass `1/2`: channel gap `-1/48`—a different channel from revealing nothing;
- vector example: six strictly positive directed margins but uniform-posterior residual `-708952329/4119500000`.

Successful finite runs verify the executed arithmetic and checks, not every possible input. A saved output should identify the exact code revision and command. This guide itself is not a replay receipt.

## Supplying exact data and certificates

Use integers, rational strings such as `"1/2"`, or `fractions.Fraction`; do not use floating-point estimates as exact input. A binary target additionally requires supported conditional means in `[0,1]`; an arbitrary real scalar target does not.

`completion_exact.py` exposes Python functions rather than a general input-file solver:

1. `sparse_model(r, v, pi)` validates a sparse table and ignores null-cell placeholders. `None` is suitable for a null cell; no semantic conditional mean is assigned there.
2. `verify_completion(r, v, C, knots)` checks a supplied rational completion for every distinct source mean and every row. It rejects missing knots, incorrect dimensions, or negative constraint margins.
3. `moments(r, v, q)` evaluates `D,N` at a supplied rational posterior, omitting zero-mass columns.
4. `violating_disclosure(r, v, pi, q)` requires a strict substitution violation, constructs the report channel, and cross-checks its gap by direct score aggregation.

Call the helpers on validated model data. They do not discover missing completions or solve the QCQP. A numerical optimizer may help propose candidates, but neither its status nor a rounded completion is an exact certificate. An exhaustive rational search could eventually detect a strict failure; a finite unsuccessful search is not a feasibility proof. Some valid primal certificates or optimum values may be irrational.

The older `exact.py --input example.json` interface is a full-support prototype, not the arbitrary-support solver. Invoking `exact.py` without arguments runs historical assertion-based regressions and regenerates a JSON receipt. Do not treat that `-O` run as equivalent verification; use the four programs above. No historical development document or omitted archival program is required by these four entry points; their analytic reference is the integrated `paper.tex` manuscript.

The sparse suite includes a compatible equal-mean, partially overlapping support fixture, checking its zero coefficient, zero posterior residuals, direct score gap and rejection of a corrupted completion. The vector suite independently recomputes four-category variances, all six directed margins and the direct four-score gap, checking their exact `1/200` scaling. These are additional finite regression checks, not additional universal theorems.

## Why the boundaries matter

The sparse example passes every two-source-state posterior restriction but fails at a three-state posterior. Joint completion constraints detect what pairwise checks miss. Its coefficient `16/9` is established by feasible knot completions and an analytic limiting posterior sequence, not by maximizing a finite grid.

The vector example has full rectangular signal support and a two-dimensional target. Every two-state posterior passes in one orientation, yet a three-state posterior fails. It also embeds into a four-category quadratic probability-scoring model with positive probabilities in every signal cell. This rules out a blanket extension of scalar pairwise sufficiency to vector targets. It does not prove impossibility of every other vector characterization, show that both orientations pass on each binary restriction, or establish that four target categories are minimal.

## Prior-art scope

The bounded search compared the precise informational-substitutes definition, mean scoring, optimal garbling, binary SDPI reductions, minimax duality, conic programming, and related Lipschitz-extension geometry. It did not find an equivalent exact arbitrary-support scalar-knot formulation in the inspected passages. That is not an exhaustive priority claim.

Primary foundations and comparison points include [Chen–Waggoner, Definition 2.2.3](https://arxiv.org/abs/1703.08636), [Anunrojwong's mean-scoring thesis](https://nrs.harvard.edu/urn-3:HUL.InstRepos:38811526), [Sion's minimax theorem](https://doi.org/10.2140/pjm.1958.8.171), [Lobo–Vandenberghe–Boyd–Lebret on SOCP](https://web.stanford.edu/~boyd/papers/pdf/socp.pdf), and [Ordentlich–Polyanskiy's binary-input SDPI reduction](https://arxiv.org/abs/2010.01987). Exact inspected locators and remaining gaps appear in the prior-art notes. The contribution is the model-specific finite characterization; these established ingredients are not claimed as new.

General proper scores, an arbitrary number of base signals, general vector-target classification, empirical estimation uncertainty, and a complete bit-complexity analysis remain outside the stated results.
