# Manuscript revision response

15 October 2026. Revision implementation under the academic-paper skill, explicitly separate from the earlier domain-review role. Only the root working `paper.tex` and this response were edited. The frozen assessment bundle and release-preparation files were not modified. No compilation, freeze, publication, solver run, or new review was performed.

Input working manuscript SHA-256: `f4e67ea7ea6b582160d6bbf3666b202ba2e89453bdd1127fd6222321e2a2f53f` (identical to the frozen submission before this edit). Main-agent diff inspection remains pending. The modifications are expository; all theorem statements, hypotheses and proof arguments are retained. The sole change inside a proof is the requested notational rename of the vector example's `R` to `R_pair`.

## Point-by-point response

| Review item | Status | Change and location |
|---|---|---|
| Domain W1: exact predecessor comparison | RESOLVED | Introduction, binary-predecessor paragraph: states Theorem 2's binary nonconstant source, finite second signal, square-integrable real target, arbitrary support, and measurable disclosure outputs; displays the two overlap-only endpoint inequalities. Identifies Corollary 2.1's vector/Hilbert extension and its one-orientation limitation. Separates inherited edge/embedding ingredients from the present arbitrary-source completion characterization. |
| Domain W2: designed-information interpretation | RESOLVED | End of Section 5.3: compares the existing sparse positive `(a,b)=(1/2,1)` and negative `(1,1/2)` tables at fixed channel. Specifies acceptance/rejection consequences, quantitative margin and uniform-prior negative gap, with reverse-orientation, exact-input and no-equilibrium caveats. No new example or economic theorem is asserted. |
| Domain W3: thesis locators | RESOLVED | Start of Section 2: adds thesis Definition 2.21, Definitions 2.8–2.9, Theorem 4.2, and Chen–Waggoner Definition 2.2.3/footnote 4. Distinguishes mean elicitation, older lattice-wide quantifiers and score-design tasks. |
| Perspective W1: forced-coordinate preprocessing | RESOLVED | Start of Section 4.2: check zero-budget prescriptions, reject conflicts, substitute consistent forced coordinates, and solve over remaining coordinates. Explicitly does not promise strict feasibility/Slater regularity or remove boundary-certification issues. |
| Perspective W2: formulation size | RESOLVED | Same paragraph: each knot has at most `m` variables and `n` row inequalities; joint coefficient program has at most `m|X|+1` variables and `n|X|` row inequalities plus `C>=0`. These are dimensions, not bit-complexity bounds. |
| Perspective W3 / EIC W1: headline theorem arrives late | RESOLVED | Introduction, after the main-result paragraph: gives the actual `C=1` knot constraints and a forward reference to Theorem 5. Retains the existing specialization-first proof order. |
| EIC W2: finite representation versus exact solver | RESOLVED | Early criterion paragraph distinguishes characterization over the reals from numerical boundary feasibility, with a new cross-reference to Section 4.3. Existing caveats are preserved. |
| EIC W3: vector geometric intuition | RESOLVED | Before the vector proposition: explains the loss of consecutive scalar brackets controlling every source mean, without claiming impossibility of other vector characterizations. |
| Devil's Advocate minor vector notation | RESOLVED | Section 6 displayed ratio: `R_pair=4529900/4824097` prevents conflation with the scalar sharp coefficient. Numeric values and proof unchanged. |

Here RESOLVED means the requested textual change was implemented, not that a reviewer has verified or accepted the revision. Historical-priority uncertainty and the absence of empirical/strategic conclusions remain deliberate limitations, not issues resolved by prose.

## Primary-source checks

### Binary predecessor: freshly inspected, not inferred

Local primary manuscript:
`binary-predecessor repository: manuscript/binary-quadratic-informational-substitutes.md`

SHA-256: `4695ea061f2da2c03226389fd418d5310c2f66bede43d515eafcb452f5689b57`.

Inspected Section 2's overlap set and constant-source convention (lines 41–83), Section 3/Theorem 2 (lines 87–101), and Corollary 2.1 (line 187). Theorem 2 requires `Pr(A=1)` strictly between zero and one, allows arbitrary finite `B`, uses only common-support columns in the two weighted contrasts, and explicitly permits measurable output alphabets. Corollary 2.1 explicitly extends to squared Euclidean norms and real Hilbert-space targets, while retaining the binary-source orientation. No global coefficient claim was attributed to this predecessor.

The [public primary repository README](https://github.com/ipitchford/binary-quadratic-informational-substitutes) was freshly retrieved and corroborates this scope. Raw/blob manuscript web retrieval returned cache misses, and shell download failed DNS resolution; the local primary manuscript supplied the statement-level verification. The existing EP bibliography entry already points to the repository and version DOI, so no new bibliographic item was required.

### Thesis and revised substitution definition

The exact locators were verified from live primary PDF text during the immediately preceding domain-review turn: [Anunrojwong's official Harvard thesis](https://dash.harvard.edu/server/api/core/bitstreams/7fe62f5f-715a-4282-8191-985cb8bc5cc9/content), Definitions 2.8–2.9, Definition 2.21 and Theorem 4.2; and [Chen–Waggoner](https://arxiv.org/pdf/1703.08636), Definition 2.2.3 and footnote 4. They were not represented as a second new literature search during implementation. Existing bibliography entries suffice.

## Verification and remaining handoff

Read the complete source diff against the frozen manuscript. The diff consists of the requested introductory comparison/roadmap, precise citation locators, a formulation-size/preprocessing paragraph, one cross-reference label, an interpretation paragraph, vector intuition and the notation rename. No formulas establishing the theorems, numerical values, or algorithms were changed. The frozen source hash remains the original binding. No new references or figures were added, and no rating or publication claim was inserted.

The main agent should inspect the diff and compile the working manuscript before any freeze. In particular, the additional displayed predecessor/roadmap equations and explanatory paragraphs may change pagination. This response is not a compilation or release receipt.
