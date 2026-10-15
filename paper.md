# Finite convex certificates for quadratic informational substitutes

Anonymous — unpublished candidate, manuscript version 3; package 0.1.0-candidate. AI-assisted; not externally human peer reviewed.

DOI: [10.5281/zenodo.23401650](https://doi.org/10.5281/zenodo.23401650). Release metadata date: 2026-10-15.

## Abstract

For a scalar square-integrable target and two finite signals with arbitrary joint support, we characterize quadratic informational substitution by finitely many convex completion problems. At each distinct source mean, a completion vector must satisfy one weighted squared-distance constraint per source state. Minimax duality proves necessity, and interpolation between consecutive scalar means proves sufficiency for every randomised disclosure. The sharp residual-variance coefficient is the value of a convex quadratically constrained program; it is finite exactly when equal-mean rows agree on their commonly supported cells. For rational input, every failure admits a rational violating posterior and disclosure, although exact feasibility at a numerical boundary requires separate certification. Under full rectangular support, completions are forced and the coefficient reduces to an explicit maximum of directed pairwise ratios. This specialization also gives the exact infimum of the normalised substitution gap at every positive prior. A sparse scalar family passes all two-state posterior restrictions but fails globally, with its exact coefficient obtained from the completion theorem. A separate full-support vector example has the same pairwise-versus-global failure, even under four-category quadratic probability scoring. The universal statements are analytic; rational computations are supplementary checks, not formal verification. The results concern one partially disclosed base signal, not arbitrary scoring rules or arbitrary pairs of partial disclosures.

**Keywords:** informational substitutes; quadratic scoring; convex certificates; randomised disclosure; minimax; finite signals.

# Introduction and relation to prior work

Strong informational substitution compares the marginal value of a whole signal before and after partial disclosure of another. Its definition quantifies over a continuum of randomised disclosures, even when the original signals have finite alphabets. Chen and Waggoner `[CW]` introduced the framework and its connections with prediction markets and information acquisition. We study its two-base-signal specialisation for scalar quadratic value.

The main result replaces this continuum by finitely many convex completion problems for arbitrary finite signal support. For each distinct source mean, a single vector must simultaneously meet all rowwise variance budgets. A compact minimax argument establishes necessity, and interpolation between consecutive scalar means establishes sufficiency. The same constraints characterize the sharp coefficient through a convex quadratically constrained program. These statements are analytic: no grid over disclosures or numerical solver establishes their universal quantifiers.

In operational terms, write $r_{ib}=\Pr(B=b\mid A=i)$, $v_{ib}=\mathbb E[Y\mid A=i,B=b]$ on supported cells, and $x_i=\sum_{b:r_{ib}>0}r_{ib}v_{ib}$. Theorem [5](#thm:completion){reference-type="ref" reference="thm:completion"} tests oriented substitution by asking, at each distinct $t\in\{x_i\}$, whether a vector $z^t$ satisfies $$\sum_{b:r_{ib}>0}r_{ib}(v_{ib}-z_b^t)^2\leq(x_i-t)^2
 \quad\text{for every }i.$$ Full support forces each anchored completion to equal a source row; structural zeros leave coordinates to be completed jointly. This is a finite characterization over the reals, not a guarantee that a numerical solver certifies feasibility at a boundary; Section [4.3](#sec:rational-certificates){reference-type="ref" reference="sec:rational-certificates"} distinguishes the two.

Full rectangular support gives an explicit specialization. Each completion is then forced by a source row, leaving only directed pairwise inequalities and a closed formula for the sharp coefficient. We first prove this formula and its disclosure consequences, then establish the general completion theorem in Section [4](#sec:completion){reference-type="ref" reference="sec:completion"}. The sparse example shows why the more general convex constraints cannot be replaced by testing every two-state posterior. Section [6](#sec:vector){reference-type="ref" reference="sec:vector"} gives a full-support vector obstruction to that binary reduction.

The closest predecessor within Evidence Press is the binary-source classification `[EP]`. Its Theorem 2 assumes a nonconstant binary source $A$, a finite second signal $B$, and a square-integrable real target, allowing arbitrary support and measurable disclosure outputs. With $O=\{b:r_{0b}r_{1b}>0\}$, it characterizes the orientation disclosing $A$ by the two tests $$(x_1-x_0)^2\geq\sum_{b\in O}r_{ib}(v_{1b}-v_{0b})^2,
 \qquad i=0,1.$$ Its Corollary 2.1 replaces scalar squares by squared norms for vector targets (and, more generally, square-integrable Hilbert-space targets). When $B$ is nonbinary, that result does not classify the reverse orientation. The binary edge calculation and posterior-disclosure construction are therefore inherited ingredients. The present contribution is the arbitrary-finite-source scalar completion characterization, its sharp coefficient and full-support formula, and the sparse and vector obstructions to extending binary checks alone. All arguments needed here are included independently of that candidate.

The assumption trade is important: the predecessor permits vector targets but fixes a binary source; the present characterization permits arbitrary finite source cardinality but fixes a scalar target. Neither result contains the other's entire domain. The concrete analytic use is screening a designed many-state information structure. Completion certificates establish the inequality for all admissible disclosures; failed systems admit violating posteriors. Under full support, directed contrasts give an explicit test and quantitative coefficient. No strategic-equilibrium conclusion follows without additional modelling assumptions.

Posterior optimisation and finite disclosure constructions are established machinery. Kong and Schoenebeck `[KS]` study information-revelation optimisation and support reduction; Anunrojwong, Chen, Waggoner and Xu `[ACWX]` study optimal garbling through persuasion. We do not claim the posterior-splitting construction or a generic small-message theorem as new. Our question is a particular universal inequality, not general optimal-garbling computation. The bounded source comparison supplied with this manuscript distinguishes statement, object and proof mechanism; it is not a guarantee of historical priority.

The mean-scoring framework is also treated by Anunrojwong `[Thesis: Section 2.4]`. Binary extremal reductions themselves are not new: Ordentlich and Polyanskiy `[OP: Theorems 1--2]` reduce channel strong data-processing constants for $f$-divergences to binary-input subchannels. Our coefficient depends on a prescribed cellwise target table, not solely on the channel $B\mid A$. For example, the identical-row channel in Section [5.1](#sec:full-example){reference-type="ref" reference="sec:full-example"} has ordinary divergence contraction coefficient zero but our coefficient two, or infinity for another target table. This demonstrates non-identity with that channel-only coefficient; it does not preclude a more elaborate derivation from prior theory. The contribution claimed here is the scalar completion characterization, its full-support directed formula, and the stated boundaries to pairwise certification, not binary reduction or minimax duality in general. The necessity proof uses Sion's established minimax theorem `[Sion1958]`.

Shah, Mandal and Azhar `[SMA: Section 2 and Remark 7]` study local substitution for finite-action decision problems with piecewise-linear convex value. Their boundary-crossing mechanism uses flat decision regions. Our quadratic prediction action is continuous and its value is not that finite-action envelope; the completion theorem addresses a different universal disclosure inequality. This distinction does not by itself establish historical priority for our characterization.

# Model and the full-support sharp coefficient

The thesis citation above is for mean elicitation (`[Thesis: Definition 2.21]`), not for interchangeable substitution quantifiers: its earlier lattice-wide formulation (`[Thesis: Definitions 2.8--2.9]`) differs from the revised two-base-signal definition used here; see also `[CW: Definition 2.2.3 and footnote 4]`. Its scoring-function design result (`[Thesis: Theorem 4.2]`) is a different task from testing a fixed quadratic value. Let $Y\in L^2$ be real valued, let $A\in\{1,\ldots,n\}$ and $B\in\{1,\ldots,m\}$, and assume $$\pi_i=\Pr(A=i)>0,\qquad r_{ib}=\Pr(B=b\mid A=i)>0.$$ Thus every signal pair has positive probability in this section and the next. Section [4](#sec:completion){reference-type="ref" reference="sec:completion"} removes this assumption. Full signal support is not a requirement that every value of $Y$ occur in every signal cell. Define $$v_{ib}=\mathbb E[Y\mid A=i,B=b],\qquad x_i=\sum_b r_{ib}v_{ib}.$$ Only these conditional means and signal probabilities enter the results. Every finite real table $v$ can be realised, for example by taking $Y=v_{AB}$.

For information $S$, write $V(S)=\mathbb E[\mathbb E(Y\mid S)^2]$. This is the part of optimal negative squared-error utility that depends on information. If $Y$ is binary, the binary Brier value is a positive multiple of $V$ plus an affine term, so its substitution inequalities agree with ours.

An admissible disclosure $T$ is generated from $A$ using fresh randomness, or equivalently satisfies $T\perp(B,Y)\mid A$. Its substitution gap is $$\begin{equation}
\label{eq:gap}
 G(T)=V(T,B)-V(T)-V(A,B)+V(A).
\end{equation}$$ The oriented substitutes property is $G(T)\geq0$ for every admissible $T$. The two-sided property requires this and the same condition with $A,B$ exchanged. This is the two-base-signal instance of the strong-substitutes definition in `[CW: Definition 2.2.3]`. It is not a claim of submodularity between arbitrary pairs of garbled signals.

For a probability vector $q$ on the source alphabet, set $$\begin{align}
 p_b(q)&=\sum_iq_ir_{ib},\qquad t(q)=\sum_iq_ix_i,\nonumber\\
 D(q)&=\sum_iq_i(x_i-t(q))^2,\label{eq:D}\\
 N(q)&=\sum_b\left\{\sum_iq_ir_{ib}v_{ib}^2-
 \frac{(\sum_iq_ir_{ib}v_{ib})^2}{p_b(q)}\right\}.\label{eq:N}
\end{align}$$ Full support ensures every denominator is positive. Both quantities are nonnegative. Define the extended-real sharp coefficient $$C_* = \inf\{C\geq0:N(q)\leq C D(q)\text{ for every }q\},$$ where the infimum of the empty set is $+\infty$.

::: {#thm:sharp .theorem}
**Theorem 1** (Sharp pairwise coefficient). *If $x_i=x_j$ but $v_i\ne v_j$ for some pair, then $C_*=+\infty$. Otherwise $$\begin{equation}
\label{eq:R}
 C_*=R:=\max_{i,j:x_i\ne x_j}
 \frac{\sum_b r_{ib}(v_{ib}-v_{jb})^2}{(x_i-x_j)^2},
\end{equation}$$ with $R=0$ if all source means coincide. In the finite case with at least two distinct source means, for every positive prior $\pi$, $$\begin{equation}
\label{eq:normalised}
 \inf_{T:\mathbb E\operatorname{Var}(x_A\mid T)>0}
 \frac{G(T)}{\mathbb E\operatorname{Var}(x_A\mid T)}=1-R.
\end{equation}$$ There is no assumption that $R\leq1$. The infimum need not be attained.*
:::

The denominator in [\[eq:normalised\]](#eq:normalised){reference-type="eqref" reference="eq:normalised"} is $V(A)-V(T)$: the value lost by withholding some source information. Thus $R$ bounds the fraction of that loss remaining after $B$ is supplied, and $1-R$ measures the corresponding substitution gap per unit of source-value loss. This is not the minimum absolute gap $G(T)$ or a solution to an unconstrained optimal-disclosure problem. In the endpoint construction below, both the source-value loss and the absolute gap can tend to zero while their ratio approaches the sharp constant. Prior-independence of this ratio therefore does not imply prior-independence of absolute economic effects.

## Posterior identity and embedding

For $q_i(T)=\Pr(A=i\mid T)$, conditional variance decomposition gives $$\begin{equation}
\label{eq:identity}
 G(T)=\mathbb E[D(q(T))-N(q(T))].
\end{equation}$$ Indeed, $\mathbb ED(q(T))=V(A)-V(T)$ and $\mathbb EN(q(T))=V(A,B)-V(T,B)$, using the conditional independence in the disclosure definition. These identities also hold for general disclosure output spaces by taking conditional expectations of the finite indicators of $A$; no finite output assumption is needed for the upper bounds.

Every posterior $q$ can be tested at any positive fixed prior. Choose $$0<\alpha\leq\min_{i:q_i>0}\frac{\pi_i}{q_i}.$$ In source state $i$, issue a special report with probability $\alpha q_i/\pi_i$ and otherwise report $i$ itself. The special report has probability $\alpha$ and posterior $q$; every other report reveals the state. Since $D(e_i)=N(e_i)=0$, this channel satisfies $$\begin{equation}
\label{eq:embed}
 G(T)=\alpha[D(q)-N(q)],\qquad
 \mathbb E\operatorname{Var}(x_A\mid T)=\alpha D(q).
\end{equation}$$ Consequently oriented substitution is equivalent to $D(q)-N(q)\geq0$ throughout the simplex, not merely at the original prior.

## Proof of Theorem [1](#thm:sharp){reference-type="ref" reference="thm:sharp"} {#proof-of-theorem-thmsharp}

If $x_i=x_j$ and $v_i\ne v_j$, an interior posterior on their edge has $D(q)=0$ and $N(q)>0$. The latter follows from full support: in at least one column the two conditional means differ and both posterior weights are positive. No finite coefficient exists.

Suppose instead that equal source means have equal conditional-mean vectors. For each row define the norm $$\|w\|_i^2=\sum_b r_{ib}w_b^2.$$ The pairwise definition of $R$ gives $$\begin{equation}
\label{eq:lipschitz}
 \|v_i-v_j\|_i\leq\sqrt R\,|x_i-x_j|\quad\text{for all }i,j.
\end{equation}$$ If all means coincide then all vectors agree, $N$ vanishes, and the result follows. Otherwise order the distinct source means. Fix $q$ and let $t=t(q)$. If $t$ equals a source mean, choose its vector $z$; then [\[eq:lipschitz\]](#eq:lipschitz){reference-type="eqref" reference="eq:lipschitz"} yields $\|v_i-z\|_i\leq\sqrt R|x_i-t|$.

If $t$ lies strictly between two consecutive distinct means $x_a<x_c$, let $$\theta=\frac{t-x_a}{x_c-x_a},\qquad z=(1-\theta)v_a+\theta v_c.$$ The choice of representative for a repeated mean is immaterial. Each original row retains its own probability vector and norm. By the triangle inequality and [\[eq:lipschitz\]](#eq:lipschitz){reference-type="eqref" reference="eq:lipschitz"}, $$\begin{align*}
 \|v_i-z\|_i
 &\leq\sqrt R\{(1-\theta)|x_i-x_a|+\theta|x_i-x_c|\}\\
 &=\sqrt R|x_i-t|.
\end{align*}$$ The equality holds because no source mean lies strictly between consecutive knots: every $x_i$ lies on one side or at an endpoint. Finally, minimising separately in each coordinate gives $$\begin{equation}
\label{eq:min}
 N(q)=\min_{z\in\mathbb R^m}\sum_iq_i\|v_i-z\|_i^2
 \leq R\sum_iq_i(x_i-t)^2=RD(q).
\end{equation}$$ This proves $C_*\leq R$.

For the reverse inequality choose an ordered pair $(i,j)$ attaining [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"}. For $q=(1-s)e_j+se_i$, $0<s<1$, direct evaluation gives $$\frac{N(q)}{D(q)}=
 \sum_b\frac{r_{jb}r_{ib}(v_{jb}-v_{ib})^2}
 {((1-s)r_{jb}+sr_{ib})(x_j-x_i)^2}.$$ As $s\downarrow0$ this tends to the ordered-pair ratio in [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"}, namely $R$. Thus $C_*\geq R$. Equation [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"} gives the lower bound $1-R$ in [\[eq:normalised\]](#eq:normalised){reference-type="eqref" reference="eq:normalised"}; embedding this edge sequence by [\[eq:embed\]](#eq:embed){reference-type="eqref" reference="eq:embed"} proves sharpness at every positive fixed prior.0◻

# Full-support finite certification and rejection

::: {#cor:test .corollary}
**Corollary 2** (Finite substitutes test). *Oriented substitution holds if and only if $$\begin{equation}
\label{eq:margin}
 M_{ij}:=(x_i-x_j)^2-\sum_b r_{ib}(v_{ib}-v_{jb})^2\geq0
 \quad\text{for every ordered pair }(i,j).
\end{equation}$$ Applying the criterion in both orientations requires at most $n(n-1)+m(m-1)$ nontrivial tests. Direct evaluation takes $O(n^2m+m^2n)$ arithmetic operations.*
:::

::: proof
*Proof.* The inequalities eliminate inconsistent equal-mean rows and are equivalent to $R\leq1$ in the remaining case. Apply Theorem [1](#thm:sharp){reference-type="ref" reference="thm:sharp"} and the posterior identity. Conversely, a ratio exceeding one gives a negative residual near an edge endpoint; an inconsistent equal-mean pair gives a negative residual on its interior edge. The embedding makes either a violating disclosure. The reverse conditional table is obtained by Bayes' rule, and full support is preserved. ◻
:::

The complexity statement counts exact arithmetic operations, not unit-cost operations on arbitrarily long bit strings. It is not a bit-complexity analysis. The oriented criterion is independent of the positive prior when $r,v$ are fixed; the reversed conditional table generally changes with that prior.

::: {#cor:strict .corollary}
**Corollary 3** (Strict quantitative substitution). *If $R<1$ is finite, then $G(T)\geq(1-R)\mathbb E\operatorname{Var}(x_A\mid T)$ for every admissible disclosure. Moreover $G(T)=0$ if and only if $T$ determines $x_A$ almost surely. When the means are distinct, this is equivalent to revealing $A$.*
:::

::: proof
*Proof.* The inequality follows from [\[eq:min\]](#eq:min){reference-type="eqref" reference="eq:min"}. If $G(T)=0$, nonnegativity and $1-R>0$ force zero conditional variance. Conversely a posterior concentrated on one mean has identical vectors $v_i$ on its support, hence both $D$ and $N$ vanish. ◻
:::

::: {#prop:witness .proposition}
**Proposition 4** (Rational negative witness). *Given rational $r,v,\pi$ satisfying the hypotheses, any negative margin produces a rational channel with strictly negative gap.*
:::

::: proof
*Proof.* Write $M_{ji}=-\varepsilon<0$. On $q=(1-s)e_i+se_j$, $$D(q)-N(q)=s(1-s)H(s),\quad
 H(s)=(x_i-x_j)^2-
 \sum_b\frac{r_{ib}r_{jb}(v_{ib}-v_{jb})^2}{(1-s)r_{ib}+sr_{jb}}.$$ Here $H(0)=M_{ji}$. Its derivative has absolute value at most $$L=\sum_b\frac{r_{ib}r_{jb}(v_{ib}-v_{jb})^2|r_{jb}-r_{ib}|}
 {\min(r_{ib},r_{jb})^2}.$$ Choose $s=\min(1/2,\varepsilon/(2L))$ if $L>0$, or $s=1/2$ otherwise. Then $H(s)\leq-\varepsilon/2$, or $H$ is constantly $-\varepsilon$. Embed $q$ with $\alpha$ half the maximal permitted mass in [\[eq:embed\]](#eq:embed){reference-type="eqref" reference="eq:embed"}. Every channel entry is rational and its gap is negative. ◻
:::

The construction uses a special report and at most $n$ revealing reports. This is a convenient implementation, not a claim of a new optimal support-size bound.

# Finite convex certificates with arbitrary signal support {#sec:completion}

We now allow $r_{ib}\geq0$ while retaining $\pi_i>0$ and stochastic rows. Define $v_{ib}$ only on supported cells and set $$x_i=\sum_{b:r_{ib}>0}r_{ib}v_{ib},\qquad
 L_i(z)=\sum_{b:r_{ib}>0}r_{ib}(v_{ib}-z_b)^2.$$ For $q\in\Delta_n$, retain $t(q)=\sum_iq_ix_i$ and $D(q)$ from [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"}, and define $$\begin{equation}
\label{eq:completion-N}
 N(q)=\min_{z\in\mathbb R^m}\sum_iq_iL_i(z).
\end{equation}$$ Coordinatewise minimisation gives [\[eq:N\]](#eq:N){reference-type="eqref" reference="eq:N"} with zero-mass columns omitted and all cell sums restricted to supported cells. In particular, no value is assigned to a null-cell conditional mean. The same conditional variance calculation proves [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"}: a column with $p_b(q(T))=0$ contributes neither probability nor variance. The revealing-report construction of [\[eq:embed\]](#eq:embed){reference-type="eqref" reference="eq:embed"} is unchanged. Thus oriented substitution is again equivalent to $N(q)\leq D(q)$ throughout the simplex, at every positive prior.

## The completion theorem

Let $\mathcal X=\{x_1,\ldots,x_n\}$ denote the set of distinct source means. A completion at $t\in\mathcal X$ is a vector $z^t\in\mathbb R^m$; its entries need not equal any observed row outside the coordinates forced by zero-loss constraints.

::: {#thm:completion .theorem}
**Theorem 5** (Finite convex completion certificates). *For every finite $C\geq0$, the following are equivalent:*

1.  *$N(q)\leq C D(q)$ for every $q\in\Delta_n$;*

2.  *for each $t\in\mathcal X$ there exists $z^t\in\mathbb R^m$ such that $$\begin{equation}
    \label{eq:completion-constraints}
     L_i(z^t)\leq C(x_i-t)^2\qquad\text{for every }i.
    \end{equation}$$*

*Consequently, oriented substitution is equivalent to at most $n$ second-order cone feasibility problems, obtained by setting $C=1$.*
:::

::: proof
*Proof.* Delete any column unsupported by every row. For every remaining column let $$a_b=\min_{i:r_{ib}>0}v_{ib},\qquad
 d_b=\max_{i:r_{ib}>0}v_{ib},\qquad
 K=\prod_b[a_b,d_b].$$ Coordinatewise clipping to $K$ does not increase any $L_i$. All minimisations below can therefore be restricted to the nonempty compact convex set $K$, without changing their values.

Suppose first that $N(q)\leq CD(q)$ for every $q$. Fix $t\in\mathcal X$ and define $$F_t(q,z)=\sum_iq_i\{L_i(z)-C(x_i-t)^2\}.$$ The identity $$\sum_iq_i(x_i-t)^2=D(q)+(t(q)-t)^2$$ and $C\geq0$ imply $\min_{z\in K}F_t(q,z)\leq0$ for every $q$. The function $F_t$ is continuous, affine in $q$, and convex in $z$. The compact convex minimax theorem of Sion `[Sion1958: Theorem 3.4]` therefore gives $$\begin{align*}
 \min_{z\in K}\max_i\{L_i(z)-C(x_i-t)^2\}
 &=\min_{z\in K}\max_{q\in\Delta_n}F_t(q,z)\\
 &=\max_{q\in\Delta_n}\min_{z\in K}F_t(q,z)\leq0.
\end{align*}$$ The minimum is attained, yielding a feasible completion at $t$.

Conversely, choose a completion at each distinct source mean. For any posterior $q$, put $t=t(q)$. If $t\in\mathcal X$, its completion directly gives $N(q)\leq CD(q)$. Otherwise let $a<c$ be consecutive elements of $\mathcal X$ with $a<t<c$, and put $$\theta=\frac{t-a}{c-a},\qquad
 z=(1-\theta)z^a+\theta z^c.$$ The row seminorm $\|w\|_i=(\sum_b r_{ib}w_b^2)^{1/2}$ obeys the triangle inequality even when some weights vanish. Applying it on supported coordinates gives $$\begin{align*}
 \sqrt{L_i(z)}
 &\leq(1-\theta)\sqrt{L_i(z^a)}+\theta\sqrt{L_i(z^c)}\\
 &\leq\sqrt C\{(1-\theta)|x_i-a|+\theta|x_i-c|\}
 =\sqrt C\,|x_i-t|.
\end{align*}$$ The last equality holds because no source mean lies strictly between consecutive knots. Squaring and averaging gives $N(q)\leq\sum_iq_iL_i(z)\leq CD(q)$. With only one distinct source mean, the single completion has zero loss for every row, so the same conclusion holds without interpolation.

For fixed $C$, each constraint in [\[eq:completion-constraints\]](#eq:completion-constraints){reference-type="eqref" reference="eq:completion-constraints"} is equivalently $$\left\|\bigl(\sqrt{r_{ib}}(v_{ib}-z_b^t)\bigr)_{b:r_{ib}>0}\right\|_2
 \leq\sqrt C\,|x_i-t|,$$ which is a second-order cone constraint. Such conic representations of convex quadratic problems are standard `[Lobo1998: Section 2.1]`. ◻
:::

## Sharp coefficient and equal-mean compatibility

Each fixed-$C$ knot problem has at most $m$ completion variables and $n$ row inequalities. Before solving it, impose the coordinates forced by rows with $x_i=t$: zero loss requires $z_b^t=v_{ib}$ wherever $r_{ib}>0$. Conflicting prescriptions reject that knot immediately; otherwise substitute the prescribed values and solve over the remaining coordinates. This preprocessing neither guarantees strict feasibility of the reduced system nor removes boundary-certification issues. The joint coefficient program below has at most $m|\mathcal X|+1$ variables and $n|\mathcal X|$ row inequalities, in addition to $C\geq0$.

Define the extended-real coefficient $$C_* =\inf\{C\geq0:N(q)\leq CD(q)\text{ for every }q\in\Delta_n\},$$ with the infimum of the empty set equal to infinity.

::: {#cor:completion-coefficient .corollary}
**Corollary 6**. *The coefficient $C_*$ is the value of the convex quadratically constrained program $$\begin{equation}
\label{eq:completion-QCQP}
 \begin{split}
 \text{minimise }&C\\
 \text{subject to }&C\geq0,\quad
 L_i(z^t)-C(x_i-t)^2\leq0
 \quad(i=1,\ldots,n,\ t\in\mathcal X).
 \end{split}
\end{equation}$$ If this program has a finite value, its minimum is attained. Moreover, $C_*<\infty$ if and only if $$\begin{equation}
\label{eq:completion-compatible}
 x_i=x_j,\quad r_{ib}r_{jb}>0
 \quad\Longrightarrow\quad v_{ib}=v_{jb}
\end{equation}$$ for every pair of rows and every column.*
:::

::: proof
*Proof.* The optimization identity follows from Theorem [5](#thm:completion){reference-type="ref" reference="thm:completion"}. Every constraint is convex quadratic in the completion coordinates and affine in $C$. If $C_0$ is any finite feasible value, clipping all completions to $K$ leaves a compact feasible search domain $K^{|\mathcal X|}\times[0,C_0]$, so a minimum is attained.

If [\[eq:completion-compatible\]](#eq:completion-compatible){reference-type="eqref" reference="eq:completion-compatible"} fails, an interior posterior on the two offending equal-mean rows has $D=0$ and a strictly positive within-column variance, so $N>0$ and no finite coefficient exists. If compatibility holds, fix a knot $t$. For rows with $x_i=t$, the requirements $L_i(z^t)=0$ prescribe consistent values on their supported coordinates. Fill the other coordinates with arbitrary values in $K$. Every remaining row has $(x_i-t)^2>0$. Taking the maximum of the finitely many ratios $L_i(z^t)/(x_i-t)^2$ over these rows and all knots gives a finite feasible coefficient. If there are no such rows, all losses vanish and $C_*=0$. ◻
:::

Under full rectangular support, the constraint at $t=x_j$ forces $z^t=v_j$. Thus the completion constraints become the directed pair inequalities $$\sum_b r_{ib}(v_{ib}-v_{jb})^2\leq C(x_i-x_j)^2.$$ Equal-mean rows must then have identical full vectors. The explicit full-support formula follows by taking the largest ratio over unequal source means, with value zero when all means coincide and the compatibility condition holds.

## Rational certificates of failure {#sec:rational-certificates}

::: {#prop:completion-rational .proposition}
**Proposition 7**. *Suppose $r$, all supported $v$, and a finite $C\geq0$ are rational. If the completion system fails, there exists a rational posterior $q$ such that $N(q)>CD(q)$. At $C=1$, any rational positive prior admits a rational disclosure with strictly negative substitution gap.*
:::

::: proof
*Proof.* Some knot $t$ has no feasible completion. By compactness, $$\delta=\min_{z\in K}\max_i\{L_i(z)-C(x_i-t)^2\}>0.$$ The same minimax identity supplies a posterior $q$ for which $$h_t(q):=N(q)-C\sum_iq_i(x_i-t)^2=\delta>0.$$ The function $h_t$ is continuous on the whole simplex, including its boundary: it is the minimum over compact $K$ of the continuous family $F_t(q,z)$, whose coefficients are uniformly bounded. More explicitly, if $B_t=\max_{i,z\in K}|L_i(z)-C(x_i-t)^2|$, then $$|h_t(q)-h_t(q')|\leq B_t\|q-q'\|_1.$$ Rational posteriors are dense, so one can choose a rational $q'$ with $h_t(q')>0$. Since $$N(q')-CD(q')=h_t(q')+C(t(q')-t)^2,$$ this posterior strictly violates the universal inequality. Its residual can be evaluated exactly using rational arithmetic, omitting zero-mass columns. At $C=1$, choose rational $\alpha>0$ in [\[eq:embed\]](#eq:embed){reference-type="eqref" reference="eq:embed"}; the resulting rational reporting kernel has gap $\alpha[D(q')-N(q')]<0$. ◻
:::

The finite convex formulation does not make an arbitrary floating-point solver status an exact certificate. Rational rejection witnesses have directly checkable strict residuals, but the argument does not guarantee rational primal completions, rational optimal coefficients, a polynomial certificate-size bound, or a uniform numerical separation from the feasibility boundary. An exhaustive rational search eventually detects every strict failure; failure to find one after finitely many steps proves nothing about feasibility. The scalar ordering used in the sufficiency proof does not extend automatically to vector targets or general scoring rules.

# Exact scalar examples and the boundary of pairwise tests

## A full-support model in both orientations {#sec:full-example}

Index both alphabets by $0,1,2$, take a uniform source prior, and set $$r_{ib}=\begin{cases}4/5&i=b,\\1/10&i\ne b,\end{cases}
 \qquad v_{ib}=(i+b)/4.$$ These are valid conditional Bernoulli means. Since $\mathbb E[B\mid A=i]=3/10+7i/10$, the source means are $x_i=3/40+17i/40$. For every distinct pair, $v_{ib}-v_{jb}=(i-j)/4$, so $$R=\frac{100}{289},\qquad 1-R=\frac{189}{289}.$$ Symmetry gives the same coefficient in the other orientation. The margins are $189/1600$ for adjacent source values and $189/400$ for the outer pair. This is a nonbinary, strictly substitutable example, not merely a duplicated binary model.

Interpret $A$ and $B$ as positively correlated three-level reports and $v_{ib}$ as an additive conditional success probability. If $T$ reveals nothing, the source-value loss is $\operatorname{Var}(x_A)=289/2400$. The theorem guarantees $G(T)\geq(189/289)(289/2400)=63/800$. This is a lower bound, not a claim that this particular disclosure attains the sharp ratio. More generally the same coefficient applies to every randomised coarsening, without enumerating reporting policies. When source means repeat, the zero-gap condition concerns disclosure of the source mean, not necessarily revelation of the full source state.

For comparison, two identical rows $r_i=(1/2,1/2)$ with $v_1=(0,0)$ and $v_2=(0,1)$ have $R=2$. Here every nondegenerate edge posterior has $N/D=2$, so the sharp normalised gap is $-1$. With $v_1=(0,1)$ and $v_2=(1,0)$ instead, the source means agree and $C_*=+\infty$.

## A sparse three-way obstruction

The completion theorem handles zero cells, but the full-support reduction to pairwise tests does not survive unchanged. The next result separates every two-state posterior restriction from the global scalar inequality.

::: {#prop:sparse .proposition}
**Proposition 8**. *There are three-valued signals and a binary target for which $D(q)-N(q)\geq0$ at every posterior supported on at most two source states, but $D(q)-N(q)<0$ at a three-state posterior.*
:::

::: proof
*Proof.* Let the prior be uniform and take conditional probability rows $$(1/2,1/2,0),\qquad(0,1/2,1/2),\qquad(1/2,0,1/2).$$ On supported cells set $v_{00}=v_{01}=0$, $v_{11}=v_{20}=a$, and $v_{12}=v_{22}=b$, where $0<a\leq1$ and $0\leq b\leq1$. Put $h=(a+b)/2$, so the source means are $(0,h,h)$.

On either edge joining row zero to another row, the sole shared column has conditional probability $1/2$ in both rows and mean contrast $a$. Thus $$D(q)-N(q)=s(1-s)(h^2-a^2/2).$$ Columns belonging to just one row have zero conditional variance. On the edge between rows one and two, the source means agree and the shared-column conditional means are both $b$, so the residual is zero. Therefore every two-row posterior passes exactly when $h^2\geq a^2/2$.

At the uniform posterior direct substitution gives $$D(q)-N(q)=\frac{(a+b)^2-3a^2}{18}.$$ Choose $\sqrt2-1\leq b/a<\sqrt3-1$ with the stated probability constraints. Then every two-row posterior passes but the uniform posterior fails. For $a=1,b=1/2$, the two nonzero edge residuals are $s(1-s)/16$ and the uniform residual is $-1/24$. The coefficient $1/16$ is not a uniform positive residual on the edge. The actual prior is uniform, so revealing nothing is a violating disclosure. Independently evaluating scores gives $$V(A)=3/8,\quad V(A,B)=5/12,\quad V(B)=V(\varnothing)=1/4,$$ which verifies the gap $-1/24$. ◻
:::

The proposition concerns two-state posterior restrictions in one orientation. It does not assert that both orientations pass for every binary restriction. The completion theorem nevertheless supplies a finite convex criterion for this family and every other finite scalar support pattern.

## Exact coefficient of a sparse three-row family

Take probability rows $$(1/2,1/2,0),\qquad(0,1/2,1/2),\qquad(1/2,0,1/2),$$ and supported conditional means $v_{00}=v_{01}=0$, $v_{11}=v_{20}=a$, and $v_{12}=v_{22}=b$, where $0<a\leq1$ and $0\leq b\leq1$. Here rows and columns are indexed by $0,1,2$, and the source means are $(0,h,h)$ with $h=(a+b)/2>0$. At knot $h$, the two zero-loss rows force the completion $(a,a,b)$; its loss in row zero is $a^2$. At knot zero, the completion $(0,0,b)$ has loss $a^2/2$ in each other row. Therefore $$\begin{equation}
\label{eq:completion-sparse-sharp}
 C_* =\frac{a^2}{h^2}=\frac{4a^2}{(a+b)^2}.
\end{equation}$$ Direct evaluation at $q=(s,(1-s)/2,(1-s)/2)$, $0<s<1$, gives $$D(q)=s(1-s)h^2,\qquad
 N(q)=\frac{s(1-s)a^2}{1+s},\qquad
 \frac{N(q)}{D(q)}=\frac{a^2}{(1+s)h^2}.$$ The ratio tends to [\[eq:completion-sparse-sharp\]](#eq:completion-sparse-sharp){reference-type="eqref" reference="eq:completion-sparse-sharp"} as $s$ decreases to zero. For $a=1,b=1/2$, the sharp coefficient is $16/9$. The equal-mean rows jointly prescribe completion coordinates that neither row alone prescribes; this is how a three-state posterior can detect failure missed by every two-state restriction.

The same overlapping-support family also supplies a strictly substitutable instance. For $a=1/2,b=1$, formula [\[eq:completion-sparse-sharp\]](#eq:completion-sparse-sharp){reference-type="eqref" reference="eq:completion-sparse-sharp"} gives $C_*=4/9$. The universal bound $N(q)\leq(4/9)D(q)$ and the posterior identity yield $$G(T)\geq\frac59\,\mathbb E\operatorname{Var}(x_A\mid T)$$ for every admissible disclosure at any positive prior. Thus the sparse completion criterion certifies a quantitative positive case with genuine overlap between row supports, as well as detecting failures.

For a designed-information screening problem, suppose the displayed channel is fixed and a designer compares two proposed conditional success-probability tables. With $(a,b)=(1/2,1)$, the certificate $C_*=4/9$ guarantees that supplying $B$ after any randomized disclosure of $A$ has marginal quadratic value at least that after full revelation of $A$, with the displayed quantitative margin. With $(a,b)=(1,1/2)$, the same support pattern is rejected: at the uniform prior, withholding $A$ entirely gives gap $-1/24$, although every two-state posterior restriction passes. The comparison screens exact proposed models; it neither optimizes the reporting policy nor establishes an equilibrium or a guarantee for estimated tables. Two-sided screening requires the reverse-orientation test as well.

# A full-support obstruction for vector targets {#sec:vector}

The scalar restriction is substantive even when all signal cells have positive probability. For a square-integrable target in $\mathbb R^d$, use quadratic value $V(S)=\mathbb E\|\mathbb E[Y\mid S]\|^2$. Write $x_i=\sum_b r_{ib}v_{ib}$, where $v_{ib}=\mathbb E[Y\mid A=i,B=b]$, and define $$\begin{align*}
 D(q)&=\sum_iq_i\left\|x_i-\sum_jq_jx_j\right\|^2,\\
 N(q)&=\sum_b\left\{\sum_iq_ir_{ib}\|v_{ib}\|^2-
 \frac{\|\sum_iq_ir_{ib}v_{ib}\|^2}{\sum_iq_ir_{ib}}\right\}.
\end{align*}$$ The conditional-variance identity still gives $G(T)=\mathbb E[D(q(T))-N(q(T))]$.

The scalar proof interpolates between consecutive means so that every source mean lies outside the open interval between them. Planar means need not admit such a common bracket: no corresponding absolute-distance identity controls all rows at once. The following example turns that missing step into a failure of pairwise sufficiency, without ruling out other vector characterizations.

::: {#prop:vector-obstruction .proposition}
**Proposition 9** (Full-support vector obstruction). *There are two three-valued signals with full rectangular support and a two-dimensional target such that every posterior supported on at most two source states has nonnegative substitution residual, but the uniform three-state posterior has negative residual. All six directed pairwise margins are strictly positive. The example also admits a four-category target realisation under quadratic probability scoring, with strictly positive target probabilities in every signal cell.*
:::

::: proof
*Proof.* Take a uniform source prior and the following channel and conditional target means, with rows and columns indexed by $0,1,2$: $$r=\frac1{100}\begin{pmatrix}2&43&55\\40&9&51\\46&53&1\end{pmatrix},
 \qquad
 v=\frac1{10}\begin{pmatrix}
 (3,-3)&(18,5)&(13,8)\\
 (-10,8)&(8,-2)&(-21,-4)\\
 (14,-17)&(2,-12)&(-6,3)
 \end{pmatrix}.$$ Every channel entry is positive, and a vector target can be realised by setting $Y=v_{AB}$. Its row means are $$x_0=(299/200,649/1000),\quad
 x_1=(-1399/1000,49/500),\quad
 x_2=(93/125,-283/200).$$ For $M_{ij}=\|x_i-x_j\|^2-\sum_b r_{ib}\|v_{ib}-v_{jb}\|^2$, direct rational evaluation gives $$\begin{array}{c|rrrrrr}
(i,j)&(0,1)&(0,2)&(1,0)&(1,2)&(2,0)&(2,1)\\\hline
10^6 M_{ij}&830137&294197&754737&557818&438797&608818
\end{array}$$ In particular all six margins are strictly positive. For a posterior $q=(1-s)e_i+se_j$, $0<s<1$, write $$D(q)-N(q)=s(1-s)H_{ij}(s),\qquad
 H_{ij}(s)=\|x_i-x_j\|^2-
 \sum_b\frac{r_{ib}r_{jb}\|v_{ib}-v_{jb}\|^2}
 {(1-s)r_{ib}+sr_{jb}}.$$ Each reciprocal positive affine function is convex, so $H_{ij}$ is concave. Its endpoint values are $H_{ij}(0)=M_{ji}>0$ and $H_{ij}(1)=M_{ij}>0$. Thus every interior two-state posterior has strictly positive residual; at a singleton posterior the residual is zero.

At $q=(1/3,1/3,1/3)$, however, $$D(q)=\frac{2548069}{1125000},\qquad
 N(q)=\frac{3614189317}{1483020000},\qquad
 D(q)-N(q)=-\frac{708952329}{4119500000}<0.$$ Since the actual prior is uniform, revealing nothing is a violating disclosure. As a separate score calculation, $$V(A)=\frac{897349}{375000},\quad
 V(A,B)=\frac{3689}{1250},\quad
 V(B)=\frac{762499307}{1483020000},\quad
 V(\varnothing)=\frac{71989}{562500},$$ which gives the same gap. In particular the directed-pair coefficient is $$R_{\mathrm{pair}}=\frac{4529900}{4824097}<1,
 \qquad
 \frac{N(q)}{D(q)}=\frac{90354732925}{83974161964}>1.$$

Finally replace each cell vector $(a,b)$ by the probability vector $$F(a,b)=\left(\frac14+\frac a{20},\frac14-\frac a{20},
                 \frac14+\frac b{20},\frac14-\frac b{20}\right).$$ All four entries are strictly positive for the displayed table, and they sum to one. Draw a four-category target with these conditional probabilities and represent it by its one-hot vector. Since $F$ is affine and $\|F(u)-F(w)\|^2=\|u-w\|^2/200$, both residual variances and every margin are scaled by $1/200$. Their signs are unchanged, proving the categorical assertion. ◻
:::

The proposition concerns one orientation. It does not assert that every binary restriction passes in both orientations, nor that four is the smallest number of target categories permitting the obstruction. The endpoint calculations were checked with rational arithmetic, but the claim for every edge posterior follows from the concavity argument, not from a finite grid.

# Evidence, limitations and conclusion

The universal results rest on the written minimax, interpolation and variance arguments. Supplementary Python code uses rational arithmetic to check examples, completion certificates and negative witnesses, and to compare posterior identities with direct expected-score aggregation. The full-support checks include $R<1$, $R>1$, inconsistent equal-mean rows, constant rows, and edge sequences. Sparse and vector examples test the boundaries of binary reduction. These are finite checks, not a proof-assistant formalisation or an empirical validation of prediction-market behaviour.

The completion characterization covers arbitrary support for finite signals and scalar targets. Full support is needed only for its collapse to the explicit directed pairwise formula. Scalar ordering remains essential to the sufficiency proof: consecutive real knots leave every source mean outside their intervening interval. The full-support vector counterexample proves that the directed pairwise test does not extend in general to vector targets, including categorical quadratic scoring. It does not rule out other finite characterizations for vector targets. General proper scoring rules, arbitrary pairs of partial disclosures, and collections of more than two base signals are outside the theorem. No solution of the unrestricted informational-substitutes programme is claimed.

Certification here assumes exact model tables. A plug-in estimate is not a statistical certificate: near-coincident source means can make the coefficient sensitive, and positive cells can be arbitrarily rare. Applications to estimated tables would require uncertainty bounds on the completion constraints or directed margins, including support and mean uncertainty; no finite-sample guarantee is proved here. Convex feasibility at a boundary is also distinct from a floating-point solver status. The rational rejection result guarantees finite exact witnesses for strict failures, not rational optimal completions or a polynomial bit-complexity bound.

The result replaces an infinite disclosure test by finitely many convex completion systems for arbitrary finite scalar signal support. Full support forces the completions and yields a sharp closed formula, together with an exact normalised worst-case comparison at every positive prior. The sparse family explains why simultaneous completion constraints carry information absent from separate binary restrictions, while the vector example identifies a distinct scalar boundary. Originality and significance require assessment separate from the proof's correctness.

#### Data and code availability.

The accompanying evidence bundle contains the exact conditional tables, checker source and test instructions. All examples are constructed; no observational or personal data are used. The manuscript contains the complete analytic arguments and does not require private research notes.

#### Ethics and competing interests.

No human participants, animals or sensitive records are involved. No competing-interest declaration from an identified human author is available; no human endorsement is implied by the anonymous byline.

#### Contributions and AI disclosure.

Mathematical development, literature comparison, software, validation and drafting were performed with AI assistance. These describe activities, not attribution of human CRediT roles. Evidence Press's account owner acts as maintainer and publisher; that role does not establish research authorship. Internal AI checking is not external human peer review.

#### Funding.

No project-specific external research grant is recorded in the supplied project evidence. Computational assistance used the configured agent environment.

# References {#references .unnumbered}

## \[Sion1958\] {#sion1958 .unnumbered}

M. Sion. On general minimax theorems. *Pacific Journal of Mathematics* 8(1) (1958), 171--176. [doi:10.2140/pjm.1958.8.171](https://doi.org/10.2140/pjm.1958.8.171).

## \[Lobo1998\] {#lobo1998 .unnumbered}

M. S. Lobo, L. Vandenberghe, S. Boyd and H. Lebret. Applications of second-order cone programming. *Linear Algebra and its Applications* 284 (1998), 193--228. [doi:10.1016/S0024-3795(98)10032-0](https://doi.org/10.1016/S0024-3795(98)10032-0).

## \[SMA\] {#sma .unnumbered}

N. Shah, S. Mandal and A. Azhar. *All Substitution Is Local*. arXiv:2604.01443, 2026. [doi:10.48550/arXiv.2604.01443](https://doi.org/10.48550/arXiv.2604.01443).

## \[CW\] {#cw .unnumbered}

Y. Chen and B. Waggoner. *Informational Substitutes*. FOCS 2016; expanded manuscript, 2017. [doi:10.1109/FOCS.2016.33](https://doi.org/10.1109/FOCS.2016.33); <https://arxiv.org/abs/1703.08636>.

## \[EP\] {#ep .unnumbered}

Anonymous. *Four tests for binary informational substitutes*. Evidence Press candidate, version 1.1.0, 2026. [doi:10.5281/zenodo.23238557](https://doi.org/10.5281/zenodo.23238557). Source: <https://github.com/ipitchford/binary-quadratic-informational-substitutes>.

## \[KS\] {#ks .unnumbered}

Y. Kong and G. Schoenebeck. *Optimizing Bayesian Information Revelation Strategy in Prediction Markets*. ITCS 2018, article 14. [doi:10.4230/LIPIcs.ITCS.2018.14](https://doi.org/10.4230/LIPIcs.ITCS.2018.14).

## \[ACWX\] {#acwx .unnumbered}

J. Anunrojwong, Y. Chen, B. Waggoner and H. Xu. *Computing Equilibria of Prediction Markets via Persuasion*. 2020 preprint. [doi:10.48550/arXiv.2009.03607](https://doi.org/10.48550/arXiv.2009.03607).

## \[Thesis\] {#thesis .unnumbered}

J. Anunrojwong. *Structure and Design of Informational Substitutes*. Harvard University undergraduate thesis, 2018. <https://nrs.harvard.edu/urn-3:HUL.InstRepos:38811526>.

## \[OP\] {#op .unnumbered}

O. Ordentlich and Y. Polyanskiy. *Strong Data Processing Constant is Achieved by Binary Inputs*. Author manuscript, arXiv:2010.01987. [doi:10.48550/arXiv.2010.01987](https://doi.org/10.48550/arXiv.2010.01987).
