# Independent academic EIC review — version 3

## Identity, independence and input

Simulated specialist mathematical-economics editor, not an actual journal official or affiliated human referee. Date: 15 October 2026. This is an independent academic report before v3 synthesis, not a publishing-assurance decision. I have read no other v3 reviewer reports. I previously assessed v1/v2; that history is disclosed, but its verdict is not treated as binding on this substantially changed manuscript.

Title: *Finite convex certificates for quadratic informational substitutes*.

Reviewed directory: `[local project root]/assessment-bundle-v3-final`.

Freshly computed bindings:

| Input | SHA-256 |
|---|---|
| paper.tex | `f4e67ea7ea6b582160d6bbf3666b202ba2e89453bdd1127fd6222321e2a2f53f` |
| paper.pdf | `caf2c616a40e4b9fb617931f323d212b217bf6bfca9fffba564e875f00263fdf` |
| MANIFEST.sha256 | `c11c29ec3a921b2ac5b565c108119f022115a096ba1a592abd67eb86521c93f2` |
| assessment-bundle-v3-final.zip | `ef5be66e9f0fa75d3e6fd51cfd2181a1477b957b94d5d172cd3e9408013bdeb9` |

All 15 manifest entries passed fresh verification. I read the entire manuscript source, README, CLAIMS, extension admission/search record, sparse extension research note, and supplied replay record. Earlier source comparisons are treated as historical evidence, not fresh independent searches. I freshly replayed the sparse and vector verification entry points under optimized Python, with bytecode disabled. I did not perform an independent implementation of those checkers, a full code audit, a visual PDF review, or an extraction comparison of the ZIP contents. Hashing the archive is not that comparison. The submission remains unchanged.

## Overall assessment

**Recommendation: Accept as a specialist theoretical article, with optional explanatory improvements.** Confidence: **3/5 overall**, higher on the internal structure and contribution delta than on historical priority. No critical or major manuscript defect was identified in this editorial reading. This is an individual recommendation, not a synthesized panel verdict.

Version 3 supplies a materially stronger result than the earlier full-support pairwise formula. It characterizes the scalar quadratic inequality for arbitrary finite signal support, replacing all posterior tests by a finite collection of simultaneous convex completion constraints. Minimax necessity and scalar interpolation sufficiency are complementary: the former explains why a single completion must meet every row budget, while the latter reduces a continuum of scalar means to finitely many knots. Finiteness, attainment, and rational failure witnesses give the characterization useful mathematical closure. The full-support formula now appears as the forced-completion case, rather than a result separated from sparse models by an unexplained obstruction.

The manuscript also distinguishes two genuine failure mechanisms for binary certification. In sparse scalar models, simultaneous coordinate constraints can carry information absent from any two-state restriction; in full-support vector models, even strict directed pair margins need not control a three-state posterior. The categorical realization makes the latter relevant to familiar quadratic probability scoring, rather than merely to an artificial Euclidean target. These additions form one coherent structural account. They do not solve arbitrary-score or multi-signal substitution, nor establish an efficient exact bit-model solver. Nevertheless, they strengthen the originality and significance case on mathematical substance, not merely presentation. I consider a provisional 3* overall assessment defensible for this version, subject to the bounded priority uncertainty below.

## Strengths

### S1. The former support limitation is resolved, not merely softened

Section 4, Theorem 5, covers arbitrary stochastic support patterns. The result is an if-and-only-if characterization, not a sufficient condition for a convenient graph class. The compact coordinate box handles zero columns and noncompact completion variables cleanly. This is the largest contribution delta from the earlier manuscript.

### S2. The coefficient receives a complete structural treatment

Corollary 6 identifies the sharp coefficient as a convex QCQP value, proves attainment when finite, and gives an exact compatibility criterion for finiteness. Equal-mean rows need agreement only on common supported cells. These are natural and informative consequences of completion geometry, not unmotivated additional propositions.

### S3. The examples explain the characterization

Section 5.3 derives the sparse family's exact coefficient `4a²/(a+b)²` from forced coordinates and an explicit completion. The same family gives a failure at `16/9` and a positive quantitative example at `4/9`. This shows that the new machinery both certifies and rejects genuinely overlapping sparse structures; it is not just an abstract reformulation with no worked content.

### S4. The vector counterexample sharpens the conceptual boundary

Section 6 proves passage of every binary posterior through concavity, rather than a finite grid. The negative three-state residual and affine four-category realization demonstrate that scalar order is substantively important to the pairwise conclusion even without structural zeros. The text correctly stops short of ruling out other vector characterizations or asserting categorical minimality.

### S5. Exactness claims are appropriately calibrated

Section 4.3 distinguishes rational strict rejection witnesses from rational primal completions, exact numerical-boundary decisions, and polynomial certificate size. The reader guide similarly distinguishes certificate checking from a general solver. The paper's universal claims rest on written proof, not the number of code checks.

## Weaknesses and optional improvements

These are not fabricated acceptance blockers. I found no required mathematical repair in this editorial remit.

### W1. The new main result is delayed behind its specialization

**Location:** Sections 2–4. **Severity:** Minor, optional structure improvement.

The title and abstract lead with arbitrary-support completion, but a reader encounters the entire full-support proof and its corollaries first. The introduction explains this ordering, so it is not misleading. Still, a compact early statement of the completion equivalence, with a short map of how full support forces completions, would make the organizing idea easier to recognize. Reordering the proof is not necessary; an early roadmap or one boxed statement would suffice.

### W2. The distinction between representation and executable exact decision remains easy to miss

**Location:** Theorem 5's SOCP consequence, Corollary 6, and Section 4.3. **Severity:** Minor, optional emphasis.

The existing limitations are correct and sufficient. For readers entering through the theorem statement, briefly cross-reference the boundary-certification caveat when first saying “SOCP feasibility.” This prevents the finite formulation from being read as a claim that the supplied software decides every rational input exactly. No new complexity theorem or implemented solver is required for acceptance.

### W3. The vector example is compelling but geometrically opaque

**Location:** Section 6. **Severity:** Minor, optional exposition.

The exact table and arithmetic prove existence, but give little intuition for how three row means defeat the scalar interpolation mechanism. A short explanation that a planar configuration lacks consecutive scalar brackets controlling all rows would connect the counterexample more directly to the proof. A simpler example or minimality result is not required.

## Detailed editorial comments

### Contribution and significance

The new mathematical delta is threefold but coherent: arbitrary support is handled by joint completion; the sharp coefficient has a finite convex optimization and finiteness criterion; and full-support vector failure separates scalar ordering from support positivity. The completion equivalence is the primary advance. The QCQP conversion is standard once the constraints are known, and rational rejection follows from separation/continuity; they should not be marketed as independent breakthroughs. Likewise Sion duality itself is not new. The manuscript makes those distinctions.

This is now more than a narrow positive-support specialization accompanied by a counterexample. It offers a full finite characterization for the specified scalar quadratic two-signal problem, including the support patterns that previously defeated pairwise tests. That establishes a stronger specialist significance case without requiring empirical data, adoption, strategic equilibria, or general proper-scoring-rule results. The remaining restrictions still limit claims of field-leading breadth.

### Proof architecture, at editorial depth

For necessity, the universal inequality implies `min_z F_t(q,z)<=0` for every posterior, since the centered second moment is `D(q)+(t(q)-t)^2`. Clipping makes minimax attainment legitimate. For sufficiency, each row's fixed seminorm controls the same interpolated completion, and consecutive scalar knots justify the absolute-distance identity. Singular weights do not break that argument. The compatibility proof correctly treats shared coordinates, and the positive separation argument yields a strict rational witness by density without claiming rational optimal primal solutions. I see no fatal gap in these steps. Detailed algebraic and software scrutiny remains the methodology reviewer's separate task.

The vector edge argument has the correct direction: the negative of a sum of positive reciprocal-affine terms is concave, so positive endpoint residual coefficients imply positive interior coefficients. The four-category affine map preserves squared-distance signs at scale `1/200`. The fresh exact replay corroborates the displayed numbers, not the universal proof by itself.

### Journal fit and coherence

The result fits a specialist mathematical-economics, theoretical decision-theory, or algorithmic information-design readership. It is a concise structural article, not a general-interest economics paper with demonstrated equilibrium or empirical consequences. The title's broader language is supported by the new completion theorem. Abstract, theorem, claims ledger, and conclusion preserve the fixed-score/two-base-signal quantifiers. The candidate remains readable without private notes or the predecessor's proof.

### Prior-art verification and limits

A fresh narrow query for informational substitutes, completion, and convex scalar formulations returned the binary predecessor and unrelated adjacent work, not an exact match. That weak negative evidence does not establish novelty. I freshly inspected Section 2 and Remark 7 of [Shah, Mandal and Azhar, All Substitution Is Local](https://arxiv.org/html/2604.01443): the finite-action piecewise-linear setting and its flat-region mechanism support the manuscript's distinction from continuous quadratic prediction. I did not perform a new exhaustive search of minimax-risk or seminorm-extension literature, trace the full citation chain, or freshly recheck every source cited in the supplied prior-art notes.

The strongest originality objection remains that a general target-specific variance comparison or extension theorem may already imply the finite-knot completion formulation under different notation. Generic SOCP representability, generic posterior optimization, or generic binary SDPI reduction alone does not demonstrate such equivalence. Neither does failure to find an equivalence prove first priority. The current bounded claim is appropriate.

## Fresh supplementary checks

`python3 -B -O completion_exact.py` exited 0 and reported 2,037 rational checks, sparse coefficient `16/9`, and limiting ratio `160000/90009`. `python3 -B -O vector_exact.py` exited 0 and reproduced all six positive directed margins, global gap `-708952329/4119500000`, pair ratio `4529900/4824097<1`, and global ratio `90354732925/83974161964>1`.

These are fresh same-code replays only. The supplied REPLAY.json also records normal/optimized runs; those historical runs are not counted as additional independent verification by this report. No code coverage count is used as a proxy for originality, significance, or universal correctness.

## Questions for authors

1. Would an early standalone statement of the completion criterion better serve the intended reader than the current specialization-first structure?
2. Is the intended practical contribution an exact mathematical characterization with checkable proposed certificates, as the current limitations imply, rather than a delivered general exact solver? Preserve this distinction in any shorter summary.
3. Can the vector example receive one geometric explanatory paragraph without adding an unsupported minimality or general-vector claim?

No answer to these optional questions is needed to repair a substantiated defect found by this review.

## Scores and prospective REF-style assessment

Scores are uncalibrated ordinal judgments adapted to proof-based research. Source counts, empirical sample sizes, adoption, and publication status are not scoring prerequisites.

| Dimension | Score | Descriptor and reason |
|---|---:|---|
| Originality | 82 | Strong: model-specific finite completion equivalence plus distinct structural boundaries; priority unresolved |
| Methodological rigour | 88 | Strong: coherent minimax/interpolation proof, degeneracies, attainment and exactness limits |
| Evidence sufficiency | 87 | Strong: complete analytic arguments with rational examples, not solver-only claims |
| Argument coherence | 85 | Strong: unified structure; specialization-first ordering could be clearer |
| Writing quality | 86 | Strong: precise, self-contained, carefully delimited |
| Literature integration | 79 | Strong but bounded: established machinery credited; equivalence search not exhaustive |
| Significance | 79 | Strong specialist contribution: arbitrary support closes the earlier substantive gap |
| Weighted core score | 85.8 | Consistent with Accept; not an acceptance probability |

| REF-style dimension | Central judgment | Uncertainty |
|---|---|---|
| Originality | 3* | 2*–3* depending on unresolved prior equivalence; no basis for confident 4* |
| Significance | 3* | 2*–3*: the arbitrary-support characterization is substantial within a fixed-score two-signal domain |
| Rigour | 3* | 3*–4* plausible; this is an editorial audit, not formal verification |
| Overall | **Provisional 3*** | **2*–3* range; moderate confidence. No supported 4* overall claim** |

The higher central significance/overall judgment than my earlier version assessment is tied to actual new mathematics: arbitrary support is now characterized rather than excluded, with a coherent convex coefficient theory and a separate full-support vector obstruction. It is not a reward for another revision, better prose, larger test counts, or a desired rating. Conversely, no automatic ceiling is imposed by the earlier 2* judgment. The strongest case for retaining 2* is that this may remain an elegant model-specific application of established minimax and extension ideas with limited downstream consequences; the strongest case for 3* is that it resolves a complete finite characterization problem across all scalar support patterns and identifies why simpler certification fails outside its explicit regime.

This prospective assessment is neither an institutional REF result nor external peer review. It should be synthesized with independent v3 reports before any research-gate decision; publishing assurance remains a separate process.
