# Peer Review Report — Methodology and proof

## Manuscript information

- Title: *Finite convex certificates for quadratic informational substitutes*.
- Input: `assessment-bundle-v3-final`, version 3, 15 October 2026.
- Review date: 15 October 2026.
- Verified ZIP SHA-256: `ef5be66e9f0fa75d3e6fd51cfd2181a1477b957b94d5d172cd3e9408013bdeb9`.
- Verified `paper.tex` SHA-256: `f4e67ea7ea6b582160d6bbf3666b202ba2e89453bdd1127fd6222321e2a2f53f`.
- All 15 entries of `MANIFEST.sha256` verified after the replay.

## Reviewer information

Role: Peer Reviewer 1, methodology. Persona: researcher in convex analysis, finite probability and exact certificate verification. This is an independent simulated AI review, not human peer review, institutional assessment, or proof-assistant verification. No other reviewer report was consulted. The complete manuscript source, mathematical/evidence notes, reader guide, claims ledger, historical replay and all five Python source files were read. The submission was not modified.

## Overall assessment

Recommendation: **Accept on mathematical-methodological grounds**, with optional small improvements to supplementary regression coverage and presentation. This is not a venue-level originality clearance.

Confidence: **4/5** for the stated analytic claims; lower for historical originality and significance. No calibration against a gold-standard reviewer set was performed.

The paper characterizes a universal posterior residual-variance inequality by simultaneous convex completion constraints at finitely many scalar means. It also obtains an attained convex-program formulation of the sharp coefficient, a precise sparse-support finiteness criterion, rational rejection witnesses, and counterexamples delimiting pairwise tests. The proof architecture is appropriate to the quantifiers: minimax supplies a simultaneous completion rather than merely individually feasible constraints, while scalar interpolation transfers finitely many knot certificates to every posterior mean. I checked the compactness and continuity issues, including zero-probability columns, repeated means and zero variance. I found no substantive gap in these arguments. The full-support formula and its normalized fixed-prior sharpness follow correctly, and the vector example establishes all-edge validity analytically rather than through enumeration. Eight fresh normal/optimized replay commands passed and reproduced the displayed anchors. These runs support arithmetic reliability but do not establish the universal theorem; the written proofs do that work. The strongest reservation concerns the size and historical status of the contribution, not proof correctness: classical minimax and elementary interpolation produce a useful, narrow characterization, whose broader influence remains unestablished. I would not require extensions to vector classification, estimated models or bit complexity as a condition of accepting the stated result.

## Strengths

### S1. Correct simultaneous minimax reduction

Section 4.1 explicitly clips each coordinate to the range of supported cell means. This produces a common compact convex set independent of the posterior, including when posterior columns disappear. The continuous affine/convex minimax exchange then gives one completion satisfying every row constraint. This addresses the actual universal quantifier; separate rowwise minimizers would not suffice.

### S2. The scalar interpolation step identifies the substantive geometry

Section 4.1 interpolates between consecutive distinct scalar means, applying each row's own seminorm. Every source mean lies outside the intervening open interval, so the absolute-distance interpolation identity is exact. Singular row weights do not break the triangle inequality. This proves sufficiency without requiring a common nonsingular norm or undefined null-cell means.

### S3. Sharpness and degeneracy are not conflated

Section 2's boundary posterior sequence proves the directed formula is sharp even if the infimum is not attained by a nondegenerate disclosure. Section 4.2 separately resolves equal-mean compatibility and attainment of the finite QCQP optimum. These are distinct attainment statements and both are correctly handled.

### S4. Exact evidence is appropriately subordinate to proof

Section 6 proves the vector example's continuum of edge inequalities by concavity. Sections 4.3 and 7 distinguish rational strict rejection from rational optimal primal certificates and from floating-point feasibility. The supplementary checks retain meaningful exceptions under optimized Python.

## Weaknesses and suggested improvements

No critical or major mathematical defect was found. The following are optional improvements, not missing hypotheses or required theorem extensions.

### W1. Categorical replay checks less than the written categorical proof

Location: `vector_exact.py`, final cell loop; Section 6's affine map. The checker verifies probability positivity and normalization but does not recompute the four-dimensional residual and all margins and compare their scaling by `1/200`. The written affine-isometry calculation is sufficient and correct, so this is not a proof gap. A direct exact categorical-score regression would improve mutation detection and align computational coverage more closely with the prominently stated categorical conclusion. Severity: minor, optional evidence improvement.

### W2. Some degenerate proof branches lack direct targeted fixtures

Location: `completion_exact.py`, `main()`. The tests cover disagreement on shared equal-mean cells, structural zero columns and a disjoint-support zero coefficient; they do not explicitly isolate the all-source-means-equal, compatible, partially overlapping case. The theorem's single-knot proof covers it. Add one compatible repeated-mean sparse fixture to protect this branch against future software regressions. Severity: minor, optional software improvement.

### W3. Historical filenames create small reader friction

Location: `test_sharp_coefficient.py` module docstring, and the reader guide's historical-program discussion. The docstring references `SHARP_COEFFICIENT.md`, absent from the frozen bundle; the guide also names an absent historical `test_extensions.py`. The integrated manuscript already contains the necessary arguments and the four current commands work, so this is not a self-containment failure. Point current checker documentation directly to the corresponding manuscript section and label absent historical names as archival references. Severity: minor, presentation only.

## Detailed proof audit

### Posterior identity and disclosure embedding — Section 2

The conditional independence assumption is explicit and sufficient: after conditioning on the source state, the reporting kernel does not alter either the channel or target conditional mean. Thus the two variance differences are exactly `E[D]` and `E[N]`. The embedding respects every positive prior by selecting `alpha <= min(pi_i/q_i)` and uses a distinct special report plus revealing reports. All non-special posterior residuals vanish, so a violating posterior gives a violating disclosure with the correct sign. General output spaces introduce no missing finite-support assumption, since finite indicator conditional expectations define the posterior.

### Full-support formula — Sections 2 and 3

The rowwise norm interpolation gives the upper bound. The endpoint limit weights the numerator by the rare source row, agreeing with the directed ratio's indices. Equal means with differing cell vectors force a positive residual numerator and zero denominator. The derivative bound in the rational negative-witness construction uses a valid positive denominator lower bound and its rational choice of `s` preserves strict negativity. Normalized fixed-prior sharpness is a ratio statement, not absolute-gap optimality, as the text correctly emphasizes.

### Compact minimax and null cells — Section 4.1

Deleting globally unsupported columns leaves at least one column because the rows are stochastic. Clipping to each supported coordinate interval weakly lowers every row loss, including rows that do not observe that coordinate. Therefore `N(q)` is a minimum on one compact box even when `q` has boundary support. `F_t` is affine in `q`, convex in `z`, and continuous, satisfying the stated compact minimax hypotheses. The identity `sum q_i(x_i-t)^2 = D(q)+(t(q)-t)^2` and nonnegative `C` yield the needed direction. The attained minimum of the maximum row deficit supplies actual feasibility rather than merely infimum zero.

The sufficiency proof can use any finite representatives on null coordinates when writing a seminorm: all losses and inequalities restrict to supported coordinates. No semantic conditional target value on a null event is required. At `C=0` the same argument works; with one distinct mean the single completion forces all relevant losses to zero. No limiting passage through a changing support is being assumed.

### QCQP, finiteness and attainment — Section 4.2

Each inequality has a positive-semidefinite diagonal quadratic part in the completion vector and an affine coefficient variable. For any finite feasible `C_0`, clipping and restricting to `[0,C_0]` gives a nonempty compact feasible set, so its minimum is attained. Pairwise agreement among equal-mean rows on shared coordinates is sufficient for a consistent coordinate assignment at each knot; unequal-mean rows then have strictly positive denominators and only finitely many ratios to bound. It is also necessary because disagreement at an overlap contributes strictly positive conditional variance on a two-row posterior with `D=0`. The criterion is therefore genuinely iff, not just necessary.

### Rational failure — Section 4.3

Failure at a knot makes the continuous maximum deficit strictly positive on the compact box: its minimum cannot be zero without a feasible point. Minimax supplies a maximizing posterior. The uniform coefficient bound proves Lipschitz continuity of the minimized function on the entire simplex, resolving the apparent singularity in quotient formulas at zero-mass columns. Density then supplies a rational strictly positive-deficit posterior, and `N-CD = h_t + C(t(q)-t)^2` preserves the sign. Rational model data make that residual exactly evaluable. A rational positive prior and rational mass produce a rational kernel. The paper correctly refrains from turning this existence proof into a complexity bound or a rational-primal guarantee.

### Sparse family — Section 5

The knot at `h` forces `(a,a,b)` through the two equal-mean rows; this gives the exact lower bound `a^2/h^2`. The displayed other completion provides the matching upper bound. The limiting posterior formula approaches the same coefficient, consistently with the direct uniform-posterior violation. At `(a,b)=(1,1/2)`, the no-disclosure gap `-1/24` differs from the embedded half-mass channel's `-1/48` for a stated and valid reason. The positive sparse fixture `(1/2,1)` has coefficient `4/9`.

### Full-support vector obstruction — Section 6

For each edge, minus a nonnegative weighted sum of reciprocal positive affine functions is concave, so positive endpoint margins imply positivity throughout the open edge. The six exact margins and uniform residual reproduce correctly. The probability map has affine translation plus a linear part whose squared norm is `1/200` times the original squared norm. Conditional means commute with that affine map, and centered differences eliminate translation, so both variance terms and margins scale correctly. All displayed cell coordinates give strictly positive category probabilities. The text confines the claim to one orientation and does not assert category minimality.

## Fresh replay record

Executed in the frozen bundle using `python3 -B`, then `python3 -B -O`, for each of:

| Entry point | Result in both modes |
|---|---|
| `verify_release.py` | Exit 0; 600 directions, 586 negative witnesses, 140 positive-posterior checks, 57 sparse-edge checks, 4 invalid-input cases, 3 negative controls; also invokes the 45-check sharp suite |
| `test_sharp_coefficient.py` | Exit 0; 45 checks; reproduces `100/289`, coefficient 2, infinity and constant-row cases |
| `completion_exact.py` | Exit 0; 2,037 checks; coefficient `16/9`, last limiting ratio `160000/90009` |
| `vector_exact.py` | Exit 0; six positive margins; gap `-708952329/4119500000`; directed ratio `4529900/4824097` and uniform ratio `90354732925/83974161964` |

These are eight fresh executions, not eight independent proof implementations. The sharp suite's invocation within the release wrapper is duplicate coverage. `-B` avoided bytecode writes; no historical receipt-generating command was run. The original manifest still passed afterward.

## Strongest counterargument

The strongest objection is that an exact finite formulation can sound more algorithmically decisive than it is. The necessity direction is classical minimax; the finite-knot direction is a short one-dimensional interpolation argument; and fixed-threshold conic constraints may have zero margins and irrational optimal coordinates. An implementer does not receive an efficient exact decision procedure simply from this formulation. Moreover, the elementary proof mechanism may be implicit in prior target-specific minimax-risk or extension results, and a narrow mathematical characterization does not itself demonstrate practical information-design impact. These points could substantially lower originality or significance without falsifying any theorem.

The paper's defense is adequate for its present methodological claims: it explicitly separates finite real convex characterization, supplied rational-certificate checking, and unproved bit-complexity or statistical guarantees. It identifies the candidate-specific finite scalar-knot reduction rather than claiming minimax itself. Sparse and vector obstructions show that the hypotheses have mathematical content. I would retain those scope qualifications and ask domain experts to resolve priority, rather than demand an unrelated general-score or vector classification as a proof correction.

## Questions for authors

1. Would you add an exact recomputation of the categorical model's residual and margin scaling to `vector_exact.py`? This would strengthen the computational support without changing the theorem.
2. Is the intended follow-on artifact a certificate-checking library or a numerical candidate generator plus exact checker? The present guide accurately promises only the former primitives; retaining that interface boundary matters for users.

Neither question is a publication-blocking mathematical uncertainty.

## Dimension scores

The theoretical-paper rubric is used: evidence means complete analytic support and exact cross-checks, not empirical sample sizes or source counts. Scores are uncalibrated judgments, not acceptance probabilities.

| Dimension | Score /100 | Descriptor | Reason |
|---|---:|---|---|
| Originality (20%) | 78 | Strong, provisional | Specific finite-knot characterization appears a meaningful structural step; no independent historical-priority clearance in this methodology review |
| Methodological rigour (25%) | 91 | Exceptional | Complete compactness, quantifier and boundary arguments; no substantive defect located |
| Evidence sufficiency (25%) | 90 | Exceptional | Written proofs support universal claims; exact replay supports examples and supplied certificates |
| Argument coherence (15%) | 88 | Strong | Clear dependency chain and explicit limitations |
| Writing quality (15%) | 85 | Strong | Precise and self-contained; minor archival-documentation friction |
| Significance (optional) | 76 | Strong, uncertain | Useful exact finite certification result; broader uptake and applications unestablished |
| Weighted average | **86.8** | **Accept** | Methodology recommendation; not venue or priority adjudication |

## Prospective REF-style assessment, separate from template scores

- Originality: **provisional 3-star**, plausible range 2–3, contingent on external statement-level priority comparison. The combination is not automatically novel because its ingredients differ in notation from prior work.
- Significance: **borderline 2–3-star**, central judgment 3-star within the specialized mathematical problem. The general arbitrary-support result and substantive counterexamples matter, but there is no established broader application or influence.
- Rigour: **3-star with 4-star potential**, based on the complete and checked analytic argument; not a claim of formal verification or infallibility.
- Overall: **provisional 3-star**, credible uncertainty toward 2-star if the central equivalence is already implicit or the field regards its consequences as narrow. I do not see evidence supporting a confident overall 4-star assessment.

These are prospective qualitative AI judgments, not an official REF outcome and not a conversion of the 0–100 scores. Originality and significance remain materially less certain than correctness. This reviewer did not independently rerun the literature searches reported in the submitted notes; their negative search findings are treated as bounded author-supplied evidence, not established absence of prior art.
