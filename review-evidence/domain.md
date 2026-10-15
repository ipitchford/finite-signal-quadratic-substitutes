# Domain review: informational economics

## Manuscript and reviewer scope

Title: *Finite convex certificates for quadratic informational substitutes*. Review date: 15 October 2026. This is a simulated domain-referee report, not an editor's decision, external peer review, or publication authorization. The persona has expertise in information design, scoring rules and informational substitution; no real identity or affiliation is claimed.

The submitted input is `assessment-bundle-v3-final`. I independently computed the manuscript-source SHA-256 as `f4e67ea7ea6b582160d6bbf3666b202ba2e89453bdd1127fd6222321e2a2f53f`, matching the supplied binding. The PDF hash is `caf2c616a40e4b9fb617931f323d212b217bf6bfca9fffba564e875f00263fdf`. The supplied ZIP binding is `ef5be66e9f0fa75d3e6fd51cfd2181a1477b957b94d5d172cd3e9408013bdeb9`; I did not independently hash the archive. I read the manuscript source, including all proof sections, and consulted its frozen prior-art notes. I did not read other reviewers' reports, modify the submission, or perform a fresh computational replay.

**Independence disclosure:** I previously contributed to this project's novelty screening and reader-facing documentation. This is therefore not independent of development. The assessment below is a fresh reading of the frozen submission, but familiarity and anchoring remain possible. It must not be counted as an external independent validation.

## Overall assessment

Recommendation: **Minor Revision**, for consideration as a specialist theoretical/methodological paper. This is not a recommendation to a named journal. Confidence: **3/5 overall**, higher for the definition mapping than for historical originality or eventual disciplinary impact.

The paper characterizes a precisely defined scalar quadratic substitution property for arbitrary finite signal tables, including structural zeros. Its main contribution is the reduction from all randomized disclosures to finitely many simultaneous completion problems, with an explicit directed-pair formula under full support. This is a substantive extension in source cardinality and support, rather than simply another constructed substitutable example. The sparse and vector counterexamples explain why the completion formulation and scalar restriction matter. The manuscript also distinguishes the sharp normalized gap from an economically larger absolute effect, and avoids claiming a strategic-equilibrium or statistical-estimation result.

The remaining domain weaknesses concern presentation of lineage and the level of significance established. The exact definition is correctly tied to the revised Chen–Waggoner framework, but readers would benefit from a compact theorem-level map against the binary predecessor and the thesis. The formal certification problem is convincingly solved within its scope; substantial practical influence or a new general theory of information design is not established. My recommendation does not require empirical validation of a mathematical theorem or expansion to general scoring rules. It asks for more economical, explicit positioning of what the new characterization adds, and preservation of the current cautious originality language.

## Strengths

1. **Correctly delimited economic property.** Section 2 specifies `T ⟂ (B,Y) | A`, a fixed quadratic decision value, and both orientations separately. This is not indiscriminate submodularity over every pair of partial signals. The live primary comparison supports the distinction: Chen–Waggoner Definition 2.2.3 restricts the base signals to the subsets lattice, and footnote 4 expressly distinguishes earlier lattice-wide definitions. [Primary PDF, printed p.9](https://arxiv.org/pdf/1703.08636).
2. **Actual classification beyond the binary-source case.** Theorem 5 and Corollary 6 characterize arbitrary finite scalar tables, not only full-support ones. Joint knot completions handle coordinates forced by several equal-mean rows. Section 5's coefficient `16/9` identifies a genuine failure of separate binary restrictions; the positive instance `4/9` demonstrates that the sparse theorem is also a certification tool.
3. **Sharpness has a clear interpretation and limitation.** Theorem 1 and its following paragraph identify the denominator as source-value loss. Endpoint sharpness is not confused with a large absolute gain, a maximizing interior disclosure, or prior-independent economic magnitudes.
4. **Boundary evidence supports, rather than replaces, the theory.** Section 6 supplies a full-support vector obstruction and a categorical realization. It neither claims both-orientation success for all binary restrictions nor a minimal number of categories. Section 7 separates analytic statements, finite exact checks, and floating-point feasibility.

## Weaknesses and actionable revisions

### W1. The closest-predecessor comparison remains more verbal than theorem-level

Location: Introduction, paragraphs on the Evidence Press binary predecessor and the assumption trade. The manuscript correctly says that source cardinality increases while vector generality is relinquished. However, a reader must assemble support, target dimension, disclosure domain, sharpness and computational output from several passages. Because this is the nearest predecessor and shares the project provenance, the contribution audit deserves a compact explicit comparison. Add a small table or paragraph stating each exact inherited component and each new component. Do not count posterior embedding, binary edge calculations or generic conic representation as separate innovations. Severity: **minor**, since the current text already acknowledges the essential trade.

### W2. The motivating use is credible but remains generic

Location: Introduction's “screening a designed many-state information structure” paragraph and Section 5.1. The paper demonstrates a usable mathematical test, but does not show a concrete decision-design question that would change when the test accepts versus rejects. Add one short worked interpretation of the existing example: what is fixed, what a designer is screening, and what certification does—and does not—guarantee about disclosure. No new equilibrium theorem or empirical exercise is required. This is chiefly a **significance limitation**, not a correctness defect; revision severity: **minor**.

### W3. Primary-source locators should make the definition change easier to audit

Location: start of Section 2 and thesis discussion in the Introduction. The distinction between mean elicitation and substitution quantifiers is important enough to cite the precise thesis definitions, not only Section 2.4. Anunrojwong's Definitions 2.8–2.9 use the lattice-wide formulation, whereas Definition 2.21 supplies the canonical mean score. Its Theorem 4.2 designs a scoring function for specified information structures; that is not the present problem of testing a fixed quadratic value. Add these locators, retaining the existing disclaimer that a different object is not itself proof of originality. Severity: **minor**. [Official thesis PDF, printed pp.9–10, 16 and 36–38](https://dash.harvard.edu/server/api/core/bitstreams/7fe62f5f-715a-4282-8191-985cb8bc5cc9/content).

## Detailed domain findings

### Precise quantifiers and theoretical framework

At a fixed positive prior, testing every posterior is justified by a special report plus revealing residual reports; it is not an assumption that the designer may change the prior. The oriented property holds for every admissible randomized disclosure, including output spaces treated through conditional expectations. Exchanging the signals requires recomputing the reverse conditional table, which generally changes when the prior changes. The manuscript explicitly says this. Scalar quadratic prediction is a legitimate decision problem, and binary Brier scoring is appropriately presented as an equivalent special case, not as all proper scoring rules.

The unrestricted scalar support result makes the finite test materially broader than the initial full-support formula. Nevertheless, the conclusion is still about a fixed target and fixed score, two base signals, and one signal's partial disclosure. It does not solve the design of arbitrary scoring rules, all decision problems, or unrestricted multi-agent information aggregation.

### Originality: what is and is not supported

The candidate-specific delta is: **the universal target-dependent residual-variance inequality is equivalent to finitely many scalar-knot completion systems, with full support forcing an explicit sharp pairwise formula.** Sion supplies the necessity engine, and standard SOCP machinery supplies the representation. The finite-knot sufficiency step uses ordering of scalar means in row-dependent seminorms; that is the contribution-bearing mechanism.

The live source check revisited Chen–Waggoner's definition and footnote, the thesis's mean-score definition and design-theorem passages, and Ordentlich–Polyanskiy's abstract. The latter establishes binary-input reductions for channel divergence contraction, not this stated target-table-dependent coefficient. The manuscript's identical-channel/different-target examples correctly exclude literal identity with a channel-only coefficient. They do not exclude an augmented-variable or restricted-function derivation from more general prior theory. [Ordentlich–Polyanskiy primary record](https://arxiv.org/abs/2010.01987).

I found no demonstrated prior equivalent in this bounded comparison. That is a provisional originality assessment, not clearance. Earlier broader inspections documented in the frozen notes are historical search evidence, not newly replicated searches in this review. I have not independently re-audited every theorem of the binary predecessor, the full optimal-garbling literature, or all extension/minimax-risk equivalents. No specific uncited source is asserted here to contain the result.

### Significance and correctness are separate

The theorem removes an infinite disclosure quantifier without imposing full support, and supplies a meaningful boundary between scalar and vector certification. This is useful structural information for the domain. Its proof being relatively short does not make the result trivial; conversely, exact checks and a clean proof do not establish field-changing significance. No domain-level contradiction was found. Detailed code correctness and exhaustive proof auditing remain outside this report's remit.

## Questions for the authors

1. Can the predecessor comparison enumerate precisely which results were already available for binary sources, including support and vector scope, and which claims first occur here?
2. Which concrete information-design screening decision is the principal intended use: verifying a fixed mechanism, comparing candidate signal structures, or another task? State the guaranteed consequence without adding unproved strategic claims.
3. Is there an identified target-specific experiment-comparison or minimax-risk theorem that might subsume the scalar-knot result? If none was located, retain that as an unresolved literature boundary rather than a universal negative claim.

## Scores and prospective REF-style assessment

These are uncalibrated simulated judgments, not probabilities of acceptance. Mathematical evidence is assessed by proofs and exact statements, not by an empirical-paper reference-count quota.

| Skill dimension | Score | Interpretation |
|---|---:|---|
| Originality | 72/100 | Adequate, potentially stronger; bounded priority uncertainty |
| Rigor | 82/100 | Strong within this domain reading, not a replacement for proof review |
| Evidence sufficiency | 76/100 | Strong for stated mathematical claims; impact evidence necessarily limited |
| Argument coherence | 82/100 | Strong, with a clearer predecessor map desirable |
| Writing | 80/100 | Strong and unusually careful about scope |
| Literature integration | 74/100 | Adequate-to-strong, with precise mappings but unresolved equivalent formulations |
| Significance | 68/100 | Useful specialist advance; broad uptake unestablished |

Using the skill's 20/25/25/15/15 weighting gives **78.2/100**, consistent with Minor Revision. The arithmetic is not a decision algorithm.

Prospective REF-style dimensions, offered only as a cautious heuristic:

- **Originality: 3-star provisional**, plausible range 2–3. The arbitrary-support finite characterization is a nontrivial structural extension, conditional on no prior equivalent.
- **Significance: 2-star**, plausible range 2–3. A useful specialized classification is demonstrated; substantial influence on economic theory or practice is not yet evidenced.
- **Rigour: 3-star provisional**, plausible range 3–4, subject to the designated proof/reproducibility review. Exact scope and analytic evidence are strong; this report is not independent development validation.
- **Overall: cautious 2-star, with 3-star plausible.** I would not infer 3-star overall merely by averaging the component labels. The main uncertainty is significance, followed by originality under alternative formulations. No 4-star overall case is established by this bundle.

This assessment is not a REF-panel judgment, a publishing-panel rating, or an institutional endorsement. My prior involvement lowers the evidential weight of this report relative to a genuinely independent specialist review.
