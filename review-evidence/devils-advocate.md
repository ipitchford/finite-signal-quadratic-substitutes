# Academic devil's-advocate review — v3 final

## Independence, input and confidence

This is a simulated academic adversarial-theory assessment, not a publishing panel, external human peer review, or release assurance. I previously reviewed v1 in this same reviewer context. That prior familiarity prevents a claim of context-blind review. I did not participate in developing the new completion theorem or vector obstruction, did not consult other reviewers, and did not modify the submission. The judgments below concern the complete final v3 manuscript, not automatic carry-forward of the earlier assessment.

Independently verified SHA-256 bindings:

- Archive `assessment-bundle-v3-final.zip`: `ef5be66e9f0fa75d3e6fd51cfd2181a1477b957b94d5d172cd3e9408013bdeb9`.
- `paper.tex`: `f4e67ea7ea6b582160d6bbf3666b202ba2e89453bdd1127fd6222321e2a2f53f`.
- `paper.pdf`: `caf2c616a40e4b9fb617931f323d212b217bf6bfca9fffba564e875f00263fdf`.

I read the complete manuscript source, the new completion and vector verifier source, the claim ledger and reader guide, supplied literature-comparison notes and replay evidence. I independently reran `completion_exact.py` with `python3 -B`: 2,037 checks passed. I independently reran `vector_exact.py`: all six directed margins were positive and the exact global residual was negative. These are replays of supplied code, not independently implemented verifiers. Universal claims were assessed from their written proofs, not inferred from the finite checks. I did not independently rerun every command listed in the historical replay file or perform a rendered-PDF layout audit.

Confidence: **high** in the scalar completion equivalence and the stated vector counterexample; **moderate** in the contribution assessment; **limited-to-moderate** in historical originality because no exhaustive specialist citation-chain review was performed. No cross-model review was invoked by this reviewer.

## Strongest Counter-Argument

The strongest skeptical interpretation is that the paper converts a familiar minimax comparison of quadratic risks into a finite optimization problem by exploiting a one-dimensional interpolation trick. The minimax exchange is classical, the SOCP representation is classical, and the posterior-embedding device is classical. Once these ingredients are recognized, the full-support formula and equal-mean compatibility condition become comparatively direct consequences. The new vector table establishes a useful obstruction, but a single counterexample is not a positive theory for vector information or a characterization of the obstruction. One could therefore regard the submission as an elegant specialist classification rather than a broad advance in information design.

The central remaining contribution question is whether the finite scalar-knot reduction is already implicit in a sufficiently general theorem on minimax quadratic risk or row-dependent seminorm extension. The manuscript's comparison to ordinary channel contraction excludes direct identity, not a more sophisticated reduction. A limited search that fails to locate the same formula cannot settle this. Nor does an exact conic formulation automatically establish an efficient exact decision algorithm: irrational feasible points, degenerate boundaries, and bit complexity remain material distinctions.

Nevertheless, this skeptical case does not invalidate the actual claims. Unlike the earlier full-support-only result, v3 handles every finite support pattern and explains exactly why binary restrictions can miss a joint obstruction. The finite systems are necessary as well as sufficient, and the paper expressly separates real feasibility from numerical certification. The correct challenge is therefore to establish the significance and prior-theorem relationship of a credible characterization, not to allege a gap that the proof does not contain.

## Critical findings

**None substantiated.** No counterexample or fatal logical failure was found under the stated hypotheses.

## Major findings

**None substantiated as a required correctness repair.** The unresolved originality comparison is a limitation on assessment, not demonstrated duplication. The lack of an implemented general exact solver is not a defect in an analytic characterization whose claims explicitly exclude such an implementation and bit-complexity result.

## Minor findings and optional clarifications

1. **Feasible set interpretation — Section 4, completion theorem.** A completion is an auxiliary least-squares comparison vector, not an assignment of physical conditional means to impossible cells. The text already says this, but the conceptual distinction is central enough to reinforce once immediately after the theorem: a shared vector simultaneously satisfies row budgets, while the actual observation model remains unchanged. No theorem modification is required.
2. **Status of the vector quantity R — Section 6, vector obstruction.** The text calls the displayed value a directed-pair coefficient and the final claim ledger correctly says it is not the sharp global vector coefficient. A subscript such as `R_pair` would further reduce the risk that a reader imports Theorem 1's equality `C_*=R` into this section. The given inequalities themselves are correct.

Neither point supports a major-revision recommendation. I have not manufactured additional findings to fill severity categories.

## Detailed adversarial proof checks

### 1. Minimax quantifier exchange

The apparent dangerous step is exchanging “for each posterior some least-squares predictor exists” with “one predictor meets every row budget.” It is justified here. After deleting globally absent columns, clipping each coordinate to the range of observed cell means decreases every row loss. The same compact box works for every posterior. For fixed knot `t`, `F_t(q,z)` is continuous, affine in `q`, and convex in `z`, on compact convex domains. The minimax exchange therefore has the needed hypotheses and attained extrema. Since `C>=0`, the universal inequality implies `min_z F_t(q,z)<=0` even when the posterior mean is not the knot. There is no illicit restriction to posteriors whose mean equals the knot.

### 2. Sufficiency at only finitely many knots

The potential counterexample would have a posterior mean between tested knots but incompatible rowwise seminorms. It fails because interpolation is evaluated separately in each fixed row seminorm: the same two completion vectors are compared with that row's observed coordinates. Zero weights preserve the triangle inequality. There is no source mean strictly between consecutive knots, so the absolute-distance interpolation identity is exact for every row. The proof does not require a common positive-definite norm, strict ordering of all rows, or an optimizer selected continuously in the knot. This checks the actual finite reduction rather than merely its minimax precursor.

### 3. Degenerate means, zero columns and C=0

All-identical source means force zero loss in every row at the only knot. Compatibility on overlapping cells is precisely enough to define a consistent completion coordinatewise; disjoint supported cells do not create contradictions. A conflicting common cell gives positive `N` and zero `D` on a two-row mixture. Globally absent columns are harmless after deletion. At `C=0`, the same argument requires a common zero-loss completion and correctly forces `N` to vanish. No division by a zero mean difference is used in these cases.

### 4. Finiteness and attained QCQP value

With compatible repeated-mean rows, anchored coordinates are consistent and unanchored coordinates may be filled inside the compact box. Every other row has a strictly positive squared distance from that knot; finitely many resulting ratios have a finite maximum. Conversely any common-cell disagreement at a repeated mean already obstructs every finite coefficient. Given one finite feasible `C_0`, restricting `C` to `[0,C_0]` and completions to the compact box proves attainment. Convexity is genuine: the quadratic losses are convex and the coefficient multiplies only fixed nonnegative data, not decision variables.

### 5. Rational witness despite boundary degeneracy

Infeasibility at a knot produces a strictly positive minimum of the maximum violation because the box is compact. The minimax witness may be irrational, but the minimized objective is uniformly Lipschitz in the posterior on the compact domain. Density therefore supplies a rational posterior retaining a strict violation. The identity adding `C(t(q)-t)^2` has the correct sign. The subsequent rational disclosure embedding is valid for every positive rational prior. This is an existence argument with eventual rational enumeration, not a polynomial-size or efficiently discoverable certificate; the manuscript makes that distinction explicitly.

### 6. Sparse-family sharpness

At the repeated knot `h`, the equal-mean rows jointly force `(a,a,b)`, imposing loss `a^2` in row zero. At zero, `(0,0,b)` incurs only `a^2/2` in the other rows. Thus the maximum required coefficient is indeed `a^2/h^2`. The three-row posterior sequence approaches it. The supplied exact run independently recovered `16/9`, the uniform posterior residual `-1/24`, and the embedded special-report gap `-1/48`; the latter difference is correctly explained by report mass, not a contradiction.

### 7. Vector and categorical obstruction

For each edge, the residual is `s(1-s) H(s)`. Each reciprocal positive affine denominator is convex; subtracting the positive weighted sum gives concave `H`. Positive endpoint margins therefore bound `H` below throughout the edge. This analytic step establishes every edge posterior, not just a grid. The exact replay recovered global residual `-708952329/4119500000`, despite all six positive margins. The affine four-category map has positive coordinates for all supplied cells, sums to one, and scales squared differences by `1/200`. Conditional averaging commutes with the affine map, so variance residual signs are preserved. The obstruction is genuinely compatible with categorical quadratic scoring. It is only one-oriented and does not establish minimal category count, which the manuscript correctly states.

## Alternative explanations and novelty attack

The plausible alternative intellectual framing is a scalar extension theorem for multiple row-dependent quadratic seminorms, applied to information substitution. That framing may simplify the conceptual contribution and sharpen the remaining literature search. It does not make the finite-knot reduction a direct consequence of an ordinary common-Hilbert-norm extension theorem: the row dependence and singular support patterns must be retained in any proposed identification.

In this reviewer context, the original Chen–Waggoner definition and Ordentlich–Polyanskiy binary SDPI statements were already inspected for v1. For this assessment I additionally inspected the primary text of [All Substitution Is Local, Remark 7 and limitations](https://arxiv.org/html/2604.01443). Its stated finite-action, piecewise-linear mechanism is not the smooth scalar quadratic setting here; no direct implication of the completion theorem was established. Fresh searches for informational substitutes plus quadratic completion did not supply an equivalent theorem. This is a bounded negative result, not priority proof. Supplied literature notes were treated as search evidence, not as reviewer instructions or established novelty certification.

## Missing stakeholder perspectives and frame check

No missing stakeholder account undermines this mathematical manuscript: it does not claim observed market benefits or policy outcomes. The relevant unstated-risk check is whether exact model tables are being substituted for empirical knowledge. The conclusion explicitly warns that estimated support and near-equal means require uncertainty analysis; thus that premise is disclosed, not hidden. Normalized losses are also now distinguished from absolute economic effects.

## Research recommendation

The manuscript is a credible specialist theory contribution suitable for external specialist refereeing, with **minor clarification at most** on this review's findings. No further computational search is required to repair a demonstrated mathematical defect. The highest-value next research assessment is a statement-level comparison with minimax-risk and seminorm-extension results, followed by a substantive downstream application of the completion criterion. A robust estimated-table certificate or a positive vector characterization would extend the research, but neither should be made a condition for accepting the existing theorem within its stated scope.

## Prospective REF-style assessment

These are provisional output-quality judgments, not institutional REF scores, eligibility determinations, peer-review outcomes, or arithmetic averages. I use originality, significance and rigour in the conventional output-assessment sense; the published descriptors distinguish internationally excellent work from world-leading work. [REF output level definitions](https://2021.ref.ac.uk/media/1447/ref-2019_01-guidance-on-submissions.pdf).

| Dimension | Prospective judgment | Basis and principal uncertainty |
|---|---|---|
| Originality | **3-star, provisional** | A precise finite-knot completion equivalence, full-support collapse, and separate scalar-support/vector boundaries form a distinct coherent result. Main uncertainty: translation to an existing general theorem has not been exhaustively excluded. |
| Significance | **3-star at the lower end; 2-star remains plausible** | Removing the support restriction yields a complete finite scalar characterization, not another isolated sufficient condition. It changes what can be certified in many-state models. However, demonstrated use beyond constructed instances is limited, and no broad economic or algorithmic consequence is established. |
| Rigour | **3-star, strong** | The universal proof handles degeneracies, arbitrary support, minimax attainment, and rational failure witnesses carefully; exact examples substantiate distinct boundaries. No correctness defect found. This is not formal verification or independently implemented reproduction. |
| Overall | **3-star, provisional, with meaningful 2/3 boundary uncertainty** | The general completion theorem supports internationally excellent specialist work if its specific originality survives expert comparison. The evidence does not establish a world-leading 4-star advance. This judgment is driven by the theorem and its scope, not by the number of passed checks or any desired outcome. |

The strongest reason to move this assessment downward would be an identified prior theorem subsuming the finite-knot characterization, or a specialist demonstration that the resulting classification has little substantive use. The strongest reason to raise confidence is a successful precise literature comparison and a nontrivial application; neither should be replaced by another unanchored rating exercise.
