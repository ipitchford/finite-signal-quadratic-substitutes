# Targeted primary-source novelty refresh

15 October 2026. This is literature research, not the final simulated reviewer panel, a priority clearance, or a publication decision. No manuscript or public artifact was modified.

## Scope and input bindings

- SHARP_COEFFICIENT.md SHA-256: `2c30535561149a862d2b160fea8deb6f3c9065143cdc132efbdf0182d7a18834`.
- PRIOR_ART.md SHA-256: `fceb43ebe2c9c0145cfa37c62e903c433309df4ffed471ba9f178465513d441b`.

The target comparison is the sharp identity C_*=R in SHARP_COEFFICIENT.md, including infinite equal-mean degeneracies, its normalized disclosure-gap interpretation, and the associated arbitrary-finite-cardinality pairwise substitution criterion. PRIOR_ART.md supplied the previous search record; its earlier inspections are not silently counted as fresh inspections here.

Searches covered the Harvard thesis access gap, scalar mean elicitation, conditional variance contraction, pairwise/binary extremizers, and standard chi-square SDPI coefficients. The conclusion is bounded: **no equivalent theorem was identified in the passages inspected, but a closely related prior binary-input reduction must be distinguished explicitly.**

## 1. Harvard thesis: access gap narrowed

[Jerry Anunrojwong, *Structure and Design of Informational Substitutes* (2018), official Harvard PDF](https://dash.harvard.edu/server/api/core/bitstreams/7fe62f5f-715a-4282-8191-985cb8bc5cc9/content) was accessible through indexed PDF text: 73 PDF pages. The earlier direct-download failures were not retried repeatedly. A screenshot request later returned a cache-miss error; text remained available. This is not a claim that every page was exhaustively reviewed.

Inspected locators: §2.4, Definition 2.21, Proposition 2.22 and Corollary 2.23 (printed p.16/PDF index 18); §4.2, Proposition 4.1 and Theorem 4.2 (printed pp.37–39/PDF indices 39–41); §4.4, Propositions 4.11–4.13 and 4.16 (printed pp.46–50/PDF indices 48–52); Chapter 5 opening (printed p.52/PDF index 54).

Mapping: canonical mean elicitation already uses squared posterior mean, equivalently negative posterior variance. The inspected design result chooses a convex scoring function using linear constraints; the Gaussian propositions concern prescribed Gaussian structures. None of those inspected statements supplies the candidate's arbitrary finite cell-mean table, directed maximum-ratio coefficient, or its full-posterior endpoint formula. The thesis therefore deserves acknowledgment for the mean-scoring framework, not dismissal as unrelated. Its uninspected passages and citation chain remain a priority-search gap.

## 2. Important adjacent prior: binary-input SDPI reduction

[Ordentlich and Polyanskiy, *Strong Data Processing Constant is Achieved by Binary Inputs*, author PDF](https://people.lids.mit.edu/yp/homepage/data/2020_binsdpi.pdf), [arXiv:2010.01987](https://arxiv.org/abs/2010.01987). Inspected both PDF pages: Theorems 1 and 2, their proof, and the post-SDPI discussion. Theorem 1 reduces a channel's KL contraction optimization to two common input atoms; Theorem 2 extends this to f-divergences. The proof preserves a likelihood ratio and uses extreme points of a simplex intersected with one affine constraint. Page 2 also discusses a binary reduction for post-SDPI.

Thus “high-cardinality optimization reduces to binary subproblems” is not new as a general information-theoretic phenomenon. The candidate needs a narrower claim: fixed cell-dependent target means, a residual-variance ratio against the variance of scalar row means, and an explicit directed endpoint formula. I did not obtain a reduction from that ratio to their divergence ratio. Mere shared binary extremizers do not establish theorem equivalence; neither does failure to find a translation establish novelty.

## 3. Standard chi-square coefficient: precise comparison

[Makur and Zheng, *Linear Bounds between Contraction Coefficients for f-Divergences*](https://arxiv.org/html/1510.01844): inspected §II's chi-square definition, Definition 3, equation (29), Proposition 2, and the channel-coefficient discussion including Proposition 6. Equation (29) identifies fixed-source chi-square contraction with squared maximal correlation; Proposition 2 gives a singular-value characterization. These optimize channel information transfer, not the candidate's fixed cell-mean target table.

### Explicit non-identity test, derived here

Fix the channel with both rows r_0=r_1=(1/2,1/2). It outputs a variable independent of the input, so every output divergence is zero and its standard chi-square contraction coefficient is zero.

Choose target means v_0=(0,0), v_1=(0,1). Then x_0=0, x_1=1/2, and the candidate's two directed ratios are

    [(1/2)*0^2+(1/2)*1^2]/(1/2)^2 = 2.

The candidate therefore has C_*=2 for this fixed channel, whereas the ordinary SDPI coefficient is zero. With the same channel and row-constant v_0=(0,0), v_1=(1,1), the candidate instead gives C_*=1. With v_0=(0,1), v_1=(1,0), it gives infinity because the means coincide but the vectors differ. All these target tables have entries in [0,1] and admit binary-target realizations.

This establishes non-identity with a channel-only coefficient, not immunity from a more elaborate prior theorem involving augmented variables, restricted test functions, or experiment comparison. Any such translation must retain the target dependence and optimization domain; it cannot merely rename B|A as the relevant channel.

## 4. Assumption and quantifier map

| Feature | Candidate under investigation | Equivalence requirement for a prior theorem |
|---|---|---|
| Data | A fixed positive row-stochastic table r and fixed real table v, with x_i=sum_b r_ib v_ib | Must preserve both r and v, not just the joint signal distribution |
| Optimization | All posteriors q on a finite source alphabet | Must account for simplex boundary limits, including D(q)=0 degeneracies |
| Ratio | E_q[Var(v_AB given B)] / Var_q(x_A) | Must derive this exact ratio, rather than retained conditional-mean variance or an arbitrary divergence ratio |
| Formula | Maximum over directed row pairs of a weighted squared difference divided by squared mean difference | A binary-reduction theorem alone is insufficient unless it also yields the endpoint formula |
| Disclosure consequence | Every fixed positive prior permits near-extremizers by a special report plus revealing residual reports | Must distinguish optimization over priors from feasibility at each fixed prior |
| Support | Full rectangular signal support | Must explain the sparse obstruction rather than silently assuming undefined cell means |
| Scale/range | Coefficient may exceed one or be infinite | A standard coefficient confined to [0,1] cannot be literally identical without transformation |

The candidate's upper-bound mechanism is ordered scalar interpolation in row-dependent norms. Its lower-bound mechanism is a two-row boundary limit. The latter is a familiar extremal pattern; the former, or an equivalent general theorem, is the principal remaining novelty target. The sharp coefficient follows rapidly from that mechanism, so it should not be positioned as an independent major breakthrough merely because it strengthens the inequality quantitatively.

## 5. Search record and limits

Fresh queries included:

- “Structure and Design of Informational Substitutes” quadratic;
- “conditional variance” “pairwise” “contraction coefficient”;
- strong data processing inequalities chi square contraction coefficient maximal correlation input distribution supremum;
- “variance” “pairwise” “informational substitutes”;
- “substitutes” “contraction coefficient” quadratic;
- “variance” “Lipschitz” “pairwise” “conditional” interpolation;
- Ordentlich Polyanskiy strong data processing constant binary input distributions;
- “variance” “contraction” “two-point” channel coefficient.

Search hits alone were not used to certify theorem equivalence. Technical comparisons above rely on opened primary text. Broad queries returned substantial irrelevant material; that limits the evidential value of a no-match result. This pass did not independently replicate the prior-art record's inspections of the prediction-market persuasion algorithms, the parent EP result, or the entire Chen–Waggoner paper.

Remaining high-value checks: inspect the thesis's remaining potentially relevant statements and references; examine whether experiment-comparison or target-specific variance-ratio literature proves an equivalent ordered-norm lemma; trace later citations of the binary-input SDPI result; and perform statement-level comparison against the final strengthened manuscript rather than this provisional note.

## Recommended positioning

Use a bounded formulation: “We derive an explicit target-dependent directed-pair formula for the sharp residual-variance coefficient in the stated finite full-support scalar setting. Binary extremal reductions are known for other information coefficients; the relation and distinction are explained.”

Do not claim the first binary reduction, the first mean-scoring formulation, or that an exhaustive literature search has ruled out equivalent results. No unsupported priority clearance is issued.
