# Academic perspective review — v3 frozen manuscript

## Input identity and reviewer disclosure

- Title: *Finite convex certificates for quadratic informational substitutes*.
- Input directory: `assessment-bundle-v3-final`.
- Manuscript SHA-256, independently computed in this review: `f4e67ea7ea6b582160d6bbf3666b202ba2e89453bdd1127fd6222321e2a2f53f`.
- ZIP SHA-256 supplied with the assignment: `ef5be66e9f0fa75d3e6fd51cfd2181a1477b957b94d5d172cd3e9408013bdeb9`. I did not independently hash the ZIP; the review was restricted to the frozen directory.
- Entire manuscript read from `paper.tex`, including the completion proof, vector example, limitations and bibliography. Supplementary `CLAIMS.md` and `EXTENSION_PRIOR_ART.md` were read as author-supplied scope material, not as independent validation or reviewer instructions.
- No other new review was consulted. No frozen file was changed. I did not execute code or inspect PDF rendering for this perspective assessment.

I am a simulated decision-theory/optimization reviewer applying the academic-paper-reviewer perspective role and theoretical-paper criteria. I have prior project context: I reviewed the earlier full-support manuscript and subsequently explored a separate absolute-gap extension. That extension is absent here and receives no credit; its omission is not a defect. This is therefore an independent report relative to the other new reviewers, but not a fresh-context or blinded review. This is an academic assessment, not a publishing-panel decision or external human peer review.

## Overall assessment

**Recommendation: Accept**, with optional minor expository improvements below, for a specialist mathematical decision-theory or information-theory venue. This does not imply fit for a particular named journal or acceptance by an editor.

**Confidence: 4/5** on scope, interpretation and the value of the convex characterization; **3/5** on historical originality and prospective wider influence. No empirical calibration of these judgments was performed.

### Summary

The manuscript now supplies a finite convex characterization of scalar quadratic substitution for arbitrary finite signal support. This is a substantive change in the result's reach: structural zeros are no longer an excluded case or only a counterexample boundary. The completion vectors describe exactly what must replace the full-support pairwise tests, and the sparse example explains why simultaneous rather than separate constraints are necessary. The proof connects a compact minimax argument with scalar interpolation; neither ingredient is claimed as new in isolation.

From a decision-theory perspective, the strongest contribution is an exact model-screening criterion with positive certificates and strict rejection witnesses, not merely a better numerical bound. From an optimization perspective, the continuum of posterior inequalities becomes finitely many convex systems with an attained sharp coefficient when finite. The manuscript also draws the right distinctions between convex formulation and numerical certification, and between normalized substitution strength and absolute payoff optimization. The full-support vector counterexample demonstrates that the scalar boundary has substantive content, including for multicategory quadratic probability scoring.

I find no blocking concern within my review remit. The principal remaining limitations are acknowledged and appropriate: exact model inputs, no efficient exact bit-complexity claim, restricted disclosure quantifiers, and unresolved historical translation questions. Optional solver-facing preprocessing advice and a compact operational summary would improve usability, but neither requires new research. The work supports a stronger specialist contribution assessment than the earlier support-restricted result, without establishing a world-leading or unrestricted theory.

## Strengths

### S1. A qualitative classification advance

Section 4, Theorem 5, characterizes *every* posterior by completions at the finitely many distinct source means, allowing arbitrary structural zeros. This is not just the generic observation that persuasion involves a convex envelope: it provides explicit, model-specific row constraints at specified knots and proves that they suffice. The source mean is the scalar index that makes the interpolation possible.

### S2. The constraints have useful geometry and interpretable failure

At a knot equal to a row's source mean, its zero budget fixes supported coordinates. Other rows constrain the remaining coordinates by weighted squared-distance budgets. Section 5.3 makes this concrete: equal-mean rows together force coordinates that no individual row supplies. The resulting coefficient `4a²/(a+b)²` and the positive example with coefficient `4/9` show that the theorem both rejects and certifies genuinely overlapping sparse models. These examples are more informative than solver output alone.

### S3. The practical claim is calibrated correctly

Section 4.3 distinguishes rational strict failure witnesses from rational primal completions and from exact feasibility at a numerical boundary. Section 7 distinguishes exact table certification from plug-in estimates. These qualifications are important for responsible use of convex optimization and do not undermine the mathematical result.

### S4. The target restriction is tested, not merely asserted

Section 6 gives full support and strictly positive directed margins while a three-state vector posterior violates substitution. The affine four-category realization establishes relevance to probability scoring: scalar quadratic prediction is not interchangeable with multicategory Brier-type scoring. The concavity argument proves the statement on every edge, not just on a grid. No minimum-category or alternative-vector-impossibility claim is made.

### S5. Normalized and absolute utility are now clearly separated

The paragraph after Theorem 1 explains that the denominator is source-information value lost by withholding A, and that an endpoint sequence may have vanishing absolute payoff effect. The illustrative three-level example interprets the bound without claiming its no-disclosure policy attains the ratio. This adequately addresses the potential operational confusion; an additional absolute-gap theorem is unnecessary.

## Weaknesses and optional revisions

### W1. State the structural equality preprocessing for implementations

**Location:** Section 4.1, completion constraints and SOCP representation; Section 4.3, numerical-certification warning.

**Issue:** Every knot has at least one row with zero right-hand side. Those constraints force equalities on supported coordinates; strict feasibility in the original cone representation is therefore not generally an appropriate numerical expectation. The manuscript proves the geometry but does not translate it into elementary solver preprocessing.

**Why it matters:** A user implementing the criterion might interpret structural degeneracy as a generic numerical pathology, despite the forced coordinates being available analytically.

**Suggestion:** Add an optional implementation sentence: first impose and check consistency of all zero-budget coordinates at a knot, then solve the reduced system over the remaining coordinates. This does not promise Slater regularity of the reduced system or remove genuine boundary issues. No new numerical algorithm or experiment is required.

**Severity:** Minor, optional.

### W2. Make the size of the convex formulation visible in the manuscript

**Location:** Theorem 5 and Corollary 6.

**Issue:** “At most n second-order cone feasibility problems” is correct, but the reader must reconstruct that each knot has at most m variables and n row constraints, and that minimizing a common C couples them in a program with at most `m|X|+1` variables and `n|X|` row inequalities.

**Why it matters:** These elementary dimensions communicate the operational advantage over an uncountable posterior test without implying a bit-complexity theorem.

**Suggestion:** Add the counts, already presented clearly in the supplied claims ledger, to the main text. Retain all exact-feasibility caveats.

**Severity:** Minor, optional.

### W3. The reading order emphasizes the specialization before the headline result

**Location:** Sections 2–4 versus title and abstract.

**Issue:** The reader reaches the general theorem after a full derivation of its full-support specialization. The introductory roadmap explains this, so it is not a coherence defect; nevertheless a reader interested in sparse-model certification must wait to see the main operational statement.

**Suggestion:** Consider a brief boxed roadmap or a forward pointer listing the knot constraints near the end of the introduction. Reordering all proofs is unnecessary and may make the intuition harder to follow.

**Severity:** Minor, optional editorial choice.

## Detailed perspective assessment

### Assumptions and applicability

The theorem's implicit application premise is access to exact model tables. This is explicitly acknowledged in Section 7. Structural zeros are now permitted, but empirically determining that a cell is truly zero remains a separate inference problem. Small mean separations and perturbations across equality of means may affect numerical sensitivity. It is appropriate to leave statistical certification for future research.

The explicit modeling restrictions are substantive rather than arbitrary: one real target, quadratic loss, two finite base signals, and a disclosure generated from one base signal with fresh randomness. The result is neither utility-uniform experiment comparison nor unrestricted submodularity over arbitrary garbling pairs. Applying it in reverse orientation remains a separate calculation. These statements are clearly maintained, and I do not recommend broadening them for rhetorical appeal.

### Decision-theoretic payoff

The exact practical task solved is screening a designed information structure: certify its universal oriented substitute inequality, quantify residual-variance domination, or obtain a strictly violating disclosure on rational input. A researcher can use the finite characterization analytically even without a turnkey implementation. That is a genuine mathematical application; deployment data and behavioral experiments are not necessary to support it.

The coefficient measures a normalized comparison, not an optimal absolute information-release policy. Section 2 says so explicitly. The omission of the separate absolute-gap exploration preserves focus rather than reducing completeness of the stated result.

### Optimization and evidentiary limits

The compact clipping box justifies attainment and the minimax exchange. The fixed-C formulation is convex; the variable-C constraints are convex quadratic plus an affine term in C. I see no apparent nonconvexity hidden by the notation. Rational SOCP input conventions can introduce square roots in the displayed norm representation, but the rational quadratic formulation remains available; the paper does not claim a rational conic encoding or a polynomial exact decision procedure.

I did not reproduce the exact arithmetic of the vector fixture or run the supplementary checkers. The proof architecture and the numerical values as presented were read, and the counterexample's infinite edge claim correctly rests on an analytic concavity argument. A numerical table alone would not have been sufficient.

### Literature and novelty limits

I credit the combination of finite scalar knots, simultaneous rowwise completion, and the sharp coefficient—not minimax, SOCP conversion, posterior splitting, or binary extremality in general. The author-supplied prior-art screen is bounded and is presented as such. Prior project context includes familiar persuasion and SDPI distinctions, but I performed no new external literature search for this frozen-only review. Thus I cannot certify historical priority or exclude a translation from another quadratic information-comparison framework. That uncertainty is relevant to originality grading, not evidence of a specific duplicate result.

### Broader implications

The vector obstruction strengthens the explanation of why the scalar method works and where it does not. It does not establish that no finite vector characterization exists. Likewise the sparse theorem removes a support restriction, not the quadratic or two-base-signal restrictions. No market equilibrium, welfare, privacy or fairness conclusion follows automatically. The manuscript does not claim one, so no forced stakeholder or empirical section is warranted.

## Questions for authors

These questions are optional clarifications, not acceptance blockers.

1. Would you include the forced-coordinate preprocessing observation for readers who implement the completion systems?
2. Would it help to expose the variable/constraint counts directly after Theorem 5 rather than only in the companion claims ledger?
3. Is analytic model screening the intended primary use, with numerical optimization serving as a candidate-finding layer? The text currently supports this interpretation.

## Dimension scores

These scores adapt the skill's rubric to theoretical work. Source counts, statistical power and empirical deployment are not scoring requirements. The numbers are ordinal aids, not calibrated acceptance probabilities.

| Dimension | Score | Descriptor | Reason |
|---|---:|---|---|
| Originality (20%) | 84 | Strong | Distinct scalar completion characterization and boundaries; historical priority remains uncertain. |
| Methodological rigour (25%) | 87 | Strong | Explicit compactness, minimax and interpolation structure with degenerate cases addressed; not a formal proof audit. |
| Evidence sufficiency (25%) | 86 | Strong | Complete analytic statements with positive and negative examples, and correct limits on computation. |
| Argument coherence (15%) | 87 | Strong | General theorem, specialization and two distinct obstruction mechanisms form a coherent whole. |
| Writing quality (15%) | 85 | Strong | Precise and self-contained; minor practical presentation opportunities. |
| Significance and impact (optional) | 83 | Strong | Universal scalar certification now includes arbitrary support; credible specialist relevance without demonstrated wider transformation. |
| Weighted average | 85.85 | Accept | Consistent with the substantive assessment, not a forecast of editorial outcome. |

## Prospective REF-style assessment

This is an informal prospective output-level assessment, not an institutional REF decision, a publication grade, or an inference from test counts. No target rating was supplied. I assess only the frozen v3 paper.

| Dimension | Central judgment | Uncertainty and rationale |
|---|---|---|
| Originality | 3* | A meaningful finite characterization in a previously excluded support regime, with a sharp coefficient and structural boundaries. Depends on the characterization not being an immediate known specialization under different terminology. |
| Significance | 3* | Removing the support restriction makes this a coherent scalar finite-signal classification rather than only a full-support test. Its specialist utility is convincing; wider field-changing consequences remain unshown. |
| Rigour | 3* | The analytic mechanisms and limitations are well specified. This perspective report has not independently replayed all fixtures or formally verified the proof. |
| Overall | Provisional 3* | Stronger and less borderline than the earlier full-support-only output, because the theorem's domain and explanatory completeness have materially improved. This is not an arithmetic average or a guarantee of actual REF treatment. |

The strongest counterargument to 3* is that the completion theorem may be regarded as a neat specialized consequence of standard minimax and one-dimensional interpolation, with limited downstream use. The strongest argument for 3* is that those ingredients yield an explicit necessary-and-sufficient classification over every finite scalar support pattern, together with a coefficient, finiteness criterion, and exact boundary mechanisms. Simplicity of proof does not by itself make that classification incremental. I do not find sufficient evidence here for 4*: broad influence, exceptional conceptual reach, and historical originality at that level are not established by this frozen record.
