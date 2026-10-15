# Reader and machine index

## Status and citation

*Finite convex certificates for quadratic informational substitutes*, Anonymous,
0.1.0-candidate, 2026-10-15. DOI: 10.5281/zenodo.23401650.
AI-assisted theoretical research; not externally human peer reviewed or formally
verified. Detailed simulated judgments and their uncertainty belong to the review
evidence, not an institutional rating. See [status](STATUS.md),
[citation metadata](CITATION.cff), [provenance](PROVENANCE.md) and
[assurance](ASSURANCE.md). Metadata alone does not attest public availability.

## Scientific question and result

For two finite signals and a scalar square-integrable target with quadratic value,
when does every admissible partial disclosure of one signal satisfy the specified
substitution inequality? The main result reduces the infinite posterior test to one
simultaneous convex row-loss completion system at each distinct scalar source mean.
Structural zeros are allowed. Only supported cell means have semantic meaning.
The criterion is necessary and sufficient, not merely a sufficient bound.

The sharp coefficient is an attained convex-program value whenever finite; finiteness
is equivalent to agreement of equal-mean rows on overlapping support. Strict failures
for rational data have rational posterior witnesses. This does not promise rational
optimal completions, an exact general solver, or polynomial bit complexity. Under
full support the completion constraints force an explicit directed-pair formula.
The fixed-prior normalized gap is distinguished from an absolute economic gap.

The sparse family has exact coefficients 16/9 and 4/9 at the two displayed parameter
choices, demonstrating both rejection and nontrivial acceptance. A separate full-support
vector example defeats directed pairwise sufficiency, including after a four-category
probability embedding. It is not a scalar counterexample or a complete vector theory.

Read the complete [PDF](paper.pdf), authoritative [LaTeX](paper.tex), or generated
[Markdown reading format](paper.md). [Claims](CLAIMS.json) give theorem locators,
assumptions and exclusions. [Research gates](RESEARCH_GATES.json) separate the new
candidate contribution from inherited minimax, conic, posterior and scoring methods.

## Reproduction and evidence limits

Run `python3 -B verify_release.py`, `python3 -B test_sharp_coefficient.py`,
`python3 -B completion_exact.py`, and `python3 -B vector_exact.py`; repeat with `-O`.
All use the supplied implementation. The release wrapper already invokes the sharp
suite, so its separate execution is not independent replication.
See [instructions](README.md), [fresh outputs](PREPARATION_REPLAY.json),
[receipt](REPLAY_RECEIPT.md), [source replay](REPLAY.json) and
[source manifest](MANIFEST.sha256). That manifest covers the supplied scientific
bundle, not the extra packaging documents. A full-package manifest, when supplied, is separate from this source-file manifest.

The universal theorem rests on the written minimax/interpolation proof, not finite
arithmetic counts. The completion checker verifies supplied rational certificates;
it is not an SOCP feasibility oracle. Solver tolerance at a boundary is not proof.
No statistical guarantee for estimated tables, arbitrary proper scoring rules,
more than two base signals or arbitrary pairs of partial disclosures is asserted.

## Review and intellectual lineage

[Academic synthesis](review-evidence/SYNTHESIS.md) is bound to the preceding frozen
v3 input. [Revision verification](review-evidence/REVISION_VERIFICATION.md) explicitly
binds the revised manuscript and preserves the qualified judgment. It verifies
exposition and regression changes without upgrading significance. Reviewers disclose
development overlap; these are not five external, fresh-context or cross-model reviews.

[Prior art](PRIOR_ART.md), [novelty refresh](NOVELTY_REFRESH.md),
[extension admission](EXTENSION_PRIOR_ART.md), [sources](SOURCES.md), and
[citation audit](CITATION_AUDIT.md) document bounded comparisons. Earlier notes describe
earlier scopes and are historical evidence, not the current theorem statement.
No-match searches do not prove priority or exclude equivalent minimax-risk results.

## Rights and accessibility

Original prose/data are [CC0](LICENSE); executable code is [MIT](LICENSE-CODE).
See [rights map](LICENSES.md), [public-domain declaration](PUBLIC_DOMAIN.md),
and [accessibility limits](ACCESSIBILITY.md). Citation references do not relicense
third-party works. The Markdown preserves mathematics and named citations but does
not establish tagged-PDF or assistive-technology compliance. The planned repository
is `ipitchford/finite-signal-quadratic-substitutes`; its existence or publication is
not asserted by this local index.
