# Sparse-support extension: prior-art screen and structural research note

Date: 15 October 2026. This is targeted mathematical research, not the deferred final reviewer panel. The existing paper was read; it has not been edited. The work began with graph-restricted pairwise criteria and, at the main agent's request, pivoted to its proposed arbitrary-support finite completion characterization.

Read input: paper.md, SHA-256 `448db1ccd9821be4e8716172171d94f40aee95051a26a8621164db12d2bd695d`.

## Research outcome

1. Tree/acyclic bipartite support does **not** suffice for pairwise posterior checks. A path-supported counterexample follows exactly from the paper's cyclic family by splitting an equal-valued column.
2. The main agent's stronger completion theorem has a clean relationship to established convex minimax and second-order-cone machinery. No matching informational-substitutes theorem was located in this bounded search.
3. The possible contribution is the exact equivalence between the all-posterior variance inequality and finitely many scalar-knot completion problems. Minimax duality, convex QCQP-to-SOCP conversion, generic Lipschitz extension, and binary reduction are established ideas and must not be claimed as new.

This is not a historical priority clearance. The fresh proof reviewer is separately examining mathematical correctness. The arguments below identify hypotheses, source mappings, and useful safeguards for that review.

## 1. Prior-art-first search record

Queries issued before developing a graph claim:

- “informational substitutes” “support” graph tree;
- “conditional variance” “acyclic” “pairwise”;
- “informational substitutes” sparse support characterization;
- “informational substitutes” “sunflower”;
- “informational substitutes” “acyclic”;
- “conditional variance” “private” “support” substitutes;
- “variance” “common support” “pairwise” coefficient;
- “signal” “support graph” “substitutes” variance;
- “Lipschitz” “variance comparison” weighted norms.

After the completion-theorem pivot:

- variance inequality intersection ellipsoids minimax Lipschitz extension pairwise;
- “informational substitutes” “second order cone”;
- “conditional variance” “completion” “minimax”;
- “Lipschitz extension” “variance” “Kirszbraun”;
- “informational substitutes” “semidefinite”;
- “informational substitutes” “convex” “completion”;
- Sion 1958 On general minimax theorems pdf;
- “Kirszbraun extensions preserving uniform distance in Hilbert spaces” arxiv.

The specialized searches produced no located exact match; broad searches also returned substantial irrelevant material. Search silence is weak evidence, especially when the same theorem could be indexed under decision-theoretic minimax risk, extension of seminorm-valued data, or finite convex feasibility.

## 2. Primary-source comparisons actually inspected

### A. Sion: the minimax engine is classical

[Maurice Sion, *On general minimax theorems*, Pacific Journal of Mathematics 8 (1958), 171–176](https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-p.pdf). Inspected Theorem 3.4, printed p.174/PDF index 4, and the following one-compact-space corollary. The compact convex, continuous affine/convex function needed here lies within this established theorem. The proposed application requires spelling out the relevant sets and attainment; it does not require a new minimax theorem.

### B. Lobo–Vandenberghe–Boyd–Lebret: the conic formulation is classical

[M. S. Lobo, L. Vandenberghe, S. Boyd and H. Lebret, *Applications of second-order cone programming*, Linear Algebra and its Applications 284 (1998), 193–228](https://web.stanford.edu/~boyd/papers/pdf/socp.pdf). Inspected §1.1 and §2.1, especially the convex QCQP formulation on printed p.197/PDF index 4. Convex quadratic inequalities have standard SOCP representations. The prospective novelty is reducing the universal disclosure condition to a finite family of these constraints, not inventing an optimization class or solver.

### C. Ciosmak: relevant extension geometry, different metric structure

[Krzysztof J. Ciosmak, *Kirszbraun extensions preserving uniform distance in Hilbert spaces*, arXiv:2607.17672](https://arxiv.org/html/2607.17672). Inspected Theorem 1.1, Proposition 2.1, and the opening and statements in §6. It characterizes a common-Hilbert-norm extension property through barycentric conditions and develops data-processing/convex-Poincare connections. The proposed completion constraints instead use a different, possibly singular diagonal seminorm for each source row. No identification with its theorem has been established. It is relevant methodological context, not a demonstrated prior equivalent. Further citation-chain comparison remains worthwhile.

### D. Shah–Mandal–Azhar: newly located neighboring paper

[N. Shah, S. Mandal and A. Azhar, *All Substitution Is Local*, arXiv:2604.01443](https://arxiv.org/html/2604.01443). Inspected §2's decision problem, Proposition 2, Theorems 4 and 6 as described in the introduction, Remark 7 and §6 limitations. Its mechanism relies on finite-action piecewise-linear value functions and decision-region boundaries. The paper explicitly distinguishes continuous-action smooth values. Thus it does not directly yield the fixed scalar quadratic, all-disclosure completion criterion. It should not be overlooked merely because it postdates the older substitutes papers.

### E. Existing nearby frameworks

[Chen–Waggoner, *Informational Substitutes*, Definition 2.2.3](https://arxiv.org/html/1703.08636) supplies the underlying substitution notion, not a newly discovered graph-support completion theorem in this search. [Ordentlich–Polyanskiy, *Strong Data Processing Constant is Achieved by Binary Inputs*, Theorems 1–2](https://people.lids.mit.edu/yp/homepage/data/2020_binsdpi.pdf) establishes binary reductions for channel divergence contraction. Its optimized quantity is not the cell-target-dependent residual variance here. The earlier NOVELTY_REFRESH.md contains the detailed non-identity example. These are ingredients and comparison points, not evidence of priority clearance.

## 3. Acyclic support is already insufficient

Use three source rows, four output columns, uniform source prior, and

    r_0=(1/2,1/2,0,0),
    r_1=(0,1/2,1/2,0),
    r_2=(1/2,0,0,1/2).

Supported conditional means are

    v_00=v_01=0,
    v_11=v_20=a,
    v_12=v_23=b.

The bipartite support is the single path

    column2 — row1 — column1 — row0 — column0 — row2 — column3.

Compared with the manuscript's cyclic example, only the shared column carrying the same conditional value b in both rows has been split into two private columns. Its old conditional-variance contribution was zero, and both new contributions are zero. Every row mean and every N(q) is unchanged. Consequently all posterior residual formulas from that example remain true.

At a=1, b=1/2 all two-row posteriors have nonnegative residual, while the uniform posterior has residual -1/24. This disproves pairwise sufficiency even for a connected support path, not just for graphs containing cycles. Therefore a treewidth/acyclicity shortcut cannot be asserted without additional target or ordering assumptions. This is a deductive transformation of the existing example, not a claimed novel graph-theoretic result.

## 4. Exact completion target and hypotheses

Allow r_ib>=0 with each row summing to one. Remove globally impossible columns. Only define v_ib on supported cells. Let x_i=sum_b r_ib v_ib, and define D,N as in the paper, omitting p_b(q)=0 terms.

For fixed finite C>=0 and each distinct source mean t, seek a vector z^t in R^m satisfying

    sum_{b:r_ib>0} r_ib (v_ib-z^t_b)^2 <= C(x_i-t)^2
    for every row i.                                      (K_t)

The main agent's proposed equivalence is

    N(q)<=C D(q) for every posterior q
        iff (K_t) is feasible for each distinct source mean t.

There are at most n knot problems, each with m completion variables and n convex quadratic inequalities. A repeated-mean row imposes zero discrepancy on all its supported coordinates at that knot; incompatible requirements on a shared coordinate correctly make feasibility fail. Unobserved coordinates are decision variables, not invented null-cell conditional means.

### Classical minimax mapping for necessity

For any real t, define

    f_t(q,z)=sum_i q_i[sum_b r_ib(v_ib-z_b)^2-C(x_i-t)^2].

For each column, clip z_b to the closed interval spanned by its supported v_ib values. Clipping cannot increase any row's squared error. Thus all minimizations can be performed on a nonempty compact box Z, independent of q and t. The source simplex and Z are compact convex sets; f_t is affine in q, convex in z, and continuous. Sion's minimax theorem applies, and both relevant extrema are attained.

The exact inner minimum is

    min_z f_t(q,z)=N(q)-C[D(q)+(sum_i q_i x_i-t)^2].

If the universal variance inequality holds, this is at most zero for every q. Minimax therefore gives a z with f_t(e_i,z)<=0 for every i, which is precisely (K_t). In fact necessity holds for every real t, not just the finite knots. This mapping is a direct application of established minimax duality.

### Why only finitely many knots can suffice

For t between consecutive scalar means a<c, interpolate feasible z^a and z^c. In each fixed row seminorm, the triangle inequality bounds the interpolation error by

    sqrt(C)[(1-theta)|x_i-a|+theta|x_i-c|]
      = sqrt(C)|x_i-t|.

No source mean lies strictly between a and c, which justifies the equality. Taking t=sum q_i x_i and summing the squared errors bounds N(q) by C D(q). This is the candidate-specific finite reduction to compare against prior art. Singular seminorms do not invalidate the triangle inequality.

The conjunction is materially broader than the current manuscript's full-support formula: arbitrary structural zeros are allowed. Full support forces every knot completion to equal its anchored row vector and recovers the original explicit pair tests. Under sparse support, completion is genuinely joint and is not equivalent to checking every pair separately.

## 5. Exactness versus numerical tractability

For fixed C the constraints can be written as norms bounded by sqrt(C)|x_i-t|; alternatively use convex quadratic constraints with C as an optimization variable. The finite formulation is exact over the reals. It does not follow that a floating-point solver's “feasible” status is an exact certificate at a zero margin, or that rational inputs guarantee rational optimal completion coordinates.

Appropriate claims distinguish: (i) analytic finite conic characterization; (ii) approximate SOCP computation; (iii) exact verification of a supplied witness; (iv) exact boundary decision and bit-complexity, if separately proved. The conic optimum can be optimized over C, but the extended-real infinity case and attainment should be addressed explicitly by the proof agent. No numerical solver was needed or used for the deductions in this note.

## 6. Optional graph corollary, deprioritized

A narrower valid-looking route is a support pattern whose source components have a common shared-column core plus row-private columns. Equivalently, every column touches either all source rows in its component or a single row. Private columns contribute zero to N. The original interpolation works on the shared core with substochastic row weights, and componentwise variance decomposition then combines the coefficients. This would cover disconnected rectangular blocks and sunflower-type row supports.

The arbitrary-support completion theorem strictly supersedes the need for such a graph restriction. This route was therefore not developed into a separate claimed theorem or subjected to a dedicated novelty search. It is recorded as a possible explanatory corollary, not as a completed independent result.

## 7. Unresolved novelty and contribution questions

- Could the finite-knot completion equivalence already follow as an explicitly stated special case of a target-specific minimax-risk or seminorm-extension theorem? No exact match was located, but this pass is not exhaustive.
- Does a prior information-design paper already give this particular finite SOCP, possibly under different notation? Generic posterior optimization and generic conic feasibility are not enough to answer that question.
- The established Sion and SOCP citations should be incorporated if the theorem is retained. The author's precise contribution is the model reduction and scalar finite-knot sufficiency, not these established tools.
- The path example rules out an attractive but false graph conjecture. It strengthens the motivation for joint completion without constituting a classification of support graphs.
- A final claim should await exact-input proof review and a focused statement-level literature check of the completed theorem. No star rating, acceptance verdict, or priority guarantee is supplied here.
