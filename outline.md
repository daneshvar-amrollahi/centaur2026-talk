# Outline: Faithful Autoformalization via Roundtrip Verification and Repair

CENTAUR 2026 keynote, 18 minutes. Built deck: 24 slides, title, 4 section dividers, 18 content slides, closing (the table below is the approved plan before the review rounds).
Two content slides (7, 15) are Statement or Big Fact slides of about 30 seconds each, so the plan
sits at roughly 18 minutes with the 20 minute hard limit as buffer.

Reviewed 2026-10-01 by audience-critic (outline mode, VERDICT: FOLLOWABLE) and fresh-eyes-reviewer.
All their fixes are folded in below. One needs your decision, marked DECISION under deviations.

## Deviations from intuition.md

- DECISION. The "aha" on slide 5 is not stated as "if T2 is correct, an unfaithful T1 is caught".
  Both reviewers flagged that this does not hold as a logical consequence: if T1 drops a clause and
  T2 and T3 are each faithful to their own input, the roundtrip reproduces the clause-less formula
  and the check passes (the paper's own "fixed point" caveat). The slide instead states the sound
  direction (if every stage preserves meaning the two formulas agree, so disagreement proves some
  stage lost meaning) and gives the detection intuition as an empirical expectation that slide 18
  then tests. Say the word if you would rather keep the original phrasing.
- Related work is one motivation slide that shows clusters of existing work and the signal
  each cluster scores (proof closes, tests pass, answer right), plus one row for recent
  faithfulness scorers (FormalAlign, ReForm, self-consistency) and one row for this talk. The
  positioning stays at the level of "most work scores the proof, recent work estimates
  faithfulness, we decide equivalence with a solver and localize the failure to a stage". The
  closest papers are named only as examples in that row, not compared one by one.
- After the user's reviews, slide 2 carries a strip figure under its bullets (a sentence card,
  a chip-style LLM icon, a formula card, a dashed "faithful?" between the ends), a separate
  limitations slide follows the failure-modes slide, and the related-work table has a row
  for checks of meaning (Li et al. 2024, FormalAlign 2025, ReForm 2026, Wang et al. 2026)
  followed by a bold row for this talk. The two rows differ in the judge: those estimate
  faithfulness with a learned score, a vote among samples, or a human, ours is an equivalence
  decided by a solver. An earlier version dated the meaning-check row "since 2024" to claim
  recency, dropped on 2026-10-02 because neither recency nor state of the art is defensible
  (no shared benchmark, Li et al. is two years old). Also on 2026-10-02, slide 6 was retitled
  "Three LLM calls, one solver query" and rebuilt as one figure (`assets/fig/check.pdf`): the
  type table on the left (sets, the three functions, the two formulas), and on the right the
  check drawn in the style of the slide 2 strip, two formula cards with a dashed "equivalent?"
  between them, the SMT-LIB query in a code card, an SMT chip, and two verdict cards (UNSAT
  equivalent, SAT counterexample). The section divider before the closing part is titled
  "Limits and what comes next" (was "What is left", which read as a reference to the unrepaired
  rules). The closing slide body carries the venue, the repository line, and a contact line
  (email and web page), with the two address lines in Menlo. On 2026-10-05 the NLI slide was
  split in two at the user's request, to introduce the classifier properly and lengthen the talk:
  a full-width bullet slide "Does x' match x?" (why x against x', what NLI is, what BART is,
  facebook/bart-large-mnli as BART-large fine-tuned on MultiNLI) followed by the photo slide
  "Lost or added?" (E and C as directional probabilities, E min and C max defined with
  subscripts, drift, the tree; the title echoes the slide 2 definition of faithful, nothing lost
  and nothing added, and the tree was re-rendered with larger yes/no labels and 10 pt subscripts
  after a slide-critic M4 flag). The residual-rules slide (author's title "Repair failures") was
  corrected the same day: its subtitle had said the 26 rules resist both LLMs, but the artifacts show
  26 is the union over the four domain-model cells and only two rules resist under both models, so it
  now says "for at least one LLM", and each pattern bullet carries one verified example from the
  residual set, later reduced to one-clause mechanisms at the user's request, except the compound
  condition bullet, which at the user's request carries the r066 quote, the two groupings hazard ->
  (stop and yield) versus stop and (hazard -> yield), and the solver's no-hazard-vehicle case on soft
  line breaks inside one bullet. The false-reject example on "A proxy can fail" is no longer the Lean
  Nat versus Int block (the user judged it weak, a checker can be given the coercion): it is now rule
  150 from the artifacts, where one formula wrote the 15-foot bound as the schema constant ft_15_sq
  and the other as ft_15 * ft_15, both faithful under an implicit assumption the axiom-free schema
  never states, so the solver separates them. The user then called the two-constant case a schema
  smell, so the slide shows a toy with one legitimate predicate instead, (lane_adjacent l1 l2) and
  (lane_adjacent l2 l1), both faithful, symmetry never stated to the axiom-free solver; the rule 150
  instance stays in the notes as the real hit. The post-training slide gained a third bullet on the
  AWS and Case Western reward-model paper (arXiv 2609.11085, Sep 2026), which fine-tunes an LLM on Z3
  equivalence verdicts and cites this work, at the user's request to show the idea has uptake. The
  related-work slide was rebuilt a second time as a four-column table (categories as columns, rows
  Checks / Decided by / Faithful to the text? / Examples, two system names per column, ours as the
  bold cell "this talk: decided by a solver"), after the user flagged inconsistent naming and vague
  cells, and then a third time as a dimension table: rows Checks / Decided by / Ground truth, the
  faithfulness family split into "prior work" and "this talk" sub-columns under one header, our
  column in neutral blue (the user did not want green, since ours is also a proxy), example names
  in the notes only. Subtitle "Others estimate faithfulness. Ours is a solver-decided proxy." After a
  practice run the user removed the Statement slide ("Roundtrip equivalence is a proxy for faithfulness.
  Evidence, not proof.") as a flow breaker, since the limits section covers it; the caveat is now
  carried by the roundtrip slide's notes. Slide 6 ("Equivalency check") got an orange card
  highlighting Sigma as the formalism that must come with an equivalence check, and the NLI slide
  got a small roundtrip reminder figure top right. Then: the related-work slide was deleted entirely (the
  user found it forced for this audience; two positioning lines live in the domains slide's notes), the
  slide 6 card lost the solver name, the reminder lost its dashed line, the NLI slide lost its first
  bullet and gained an NLI box diagram (premise and hypothesis cards, NLI chip, score dictionary, the
  classic SNLI soccer pair with illustrative numbers) between its two bullets, and the proxy slide became
  a Title Only two-column figure: false accept (both encodings drop the 50-foot bound, UNSAT) versus
  false reject (lane_adjacent argument order, SAT), same card and code styles. The deck is 23 slides.
- Table 1 and the ablations come before the NLI signal and Figure 4. Figure 4 is measured under
  Full repair, so the audience has to know what Full is before the drift split makes sense. It
  also lets the talk end its results on the one-sentence message (the proxy works).
- "Necessary, not sufficient" gets its own Statement slide (7) right after the roundtrip definition
  and before diagnosis and repair, rather than living in limitations. It is the "proxy" sentence,
  and its notes announce that an independent measure will test it later (slides 17 and 18).
- The SMT reduction gets one visible line on slide 6 (UNSAT means equivalent, SAT gives a
  counterexample) because the result slides are labelled SAT and UNSAT. The rest of the reduction
  stays in notes, per intuition.md.
- A fourth section divider (19, "What is left") separates failure modes, limitations, and future
  work from the results, so no run of content slides exceeds six without a divider.
- Future work is one slide, not a bullet in the closing, because the reward-model direction
  needs two sentences of setup for this audience (what post-training is).
- Time split, summing to 18: motivation 3 min (slides 1 to 3), roundtrip 3 (4 to 7), diagnosis
  and repair 2.5 (8 to 10), experiments and results 7 (11 to 18), what is left 1.5 (19 to 22),
  close 1 (23).

## Slides

Titles on Title & Bullets, Title Only, and Title, Bullets & Photo are kept under 40 characters
because their title slot holds one line at the template's title size. The Title, Section,
Statement, and Big Fact layouts have larger slots and are exempt. The single point goes into the
subtitle slot, the body, or the notes. "Notes:" marks content that is spoken only.

| # | Layout | Title | Single point | Figure or equation |
|---|---|---|---|---|
| 1 | Title | Faithful Autoformalization via Roundtrip Verification and Repair | Authors, Stanford. Body: Findings of EMNLP 2026. Footer: CENTAUR 2026, date. | none |
| 2 | Title & Bullets | An LLM writes the formula for you | A large language model (LLM) is a learned text-to-text function with no specification. Autoformalization uses it to turn natural language (a statute, a requirement, a theorem) into a formula a tool can check, removing the human bottleneck in front of every solver and prover. Faithful means the formula says what the text says, nothing lost, nothing added, and an LLM output can be well formed, satisfiable, and silently unfaithful. This talk's instance: statutes to first-order logic checked by Z3, but any formalism with an equivalence check works. | none |
| 3 | Title Only | Today's signal: did the proof close? | Clusters of existing work and what each one scores. Proof-assistant benchmarks (miniF2F, ProofNet): compiles or proof closes. Prover feedback loops (LeanDojo, DeepSeek-Prover): proof completion as the score the system is trained to maximize. Solver-in-the-loop reasoning (Logic-LM): final answer right. Specs from requirements or code (nl2spec, Clover): agreement with code or tests. The dominant signals score the proof, the tests, or the answer, not the statement against its text, so a wrong statement with a finished proof counts as success. Subtitle: the question we ask is whether the statement means what the text says. Notes: a benchmark is a fixed problem set used to score systems. | Rendered table image: four rows (one cluster each, one or two example systems), one column for the signal scored, one empty column "statement matches text?" |
| 4 | Section | Roundtrip verification | divider | none |
| 5 | Title Only | Go there and back, then compare | Formalize x into y_orig (T1), translate y_orig back to natural language x' (T2), formalize x' again into y_rt (T3), then check y_orig against y_rt. If every stage preserves meaning, the two formulas agree, so disagreement proves some stage lost or added meaning, with no ground truth needed. Notes: faithful for a stage means its output says what its input says. The expectation, tested on slide 18, is that a wrong formula rarely survives being put into words and formalized again unchanged, so disagreement is a useful alarm even though agreement is not a guarantee. | Fig 1 roundtrip loop (re-render TikZ from `intro.tex`), with x, y_orig, x', y_rt labelled |
| 6 | Title Only | Three functions, one equivalence | X is the set of natural-language strings, Y_Sigma the well-formed formulas of the target formalism Sigma. T1: X to Y_Sigma, T2: Y_Sigma to X, T3: X to Y_Sigma, and the check is T1(x) equiv_Sigma T3(T2(T1(x))). T3 has the same type as T1 and is a fresh call, kept distinct so a failure can be blamed on a stage. Subtitle: Z3 decides the check, UNSAT means equivalent, SAT gives a counterexample. Notes: the solver checks satisfiability of the negated biconditional. Any Sigma with well-formedness and an equivalence relation fits, FOL here, Lean equally. | Equation image: the three stage types and the check, four lines |
| 7 | Statement | Roundtrip agreement is evidence of faithfulness, not a proof of it | Necessary, not sufficient. T1 and T3 can make the same mistake and agree on a wrong formula. Notes: this is the proxy for faithfulness the talk is about, and later we test how good the evidence is against an independent measure. | none |
| 8 | Section | Diagnosis and scoped repair | divider | none |
| 9 | Title Only | Disagreement points at a stage | Stage i is T_i. On SAT, an LLM judge D reads the four artifacts x, y_orig, x', y_rt, examines the stages in order (x against y_orig, then y_orig against x', then x' against y_rt), and halts at the first inconsistency with an explanation that mentions only that stage's two artifacts. Repair operator R_i rewrites only that stage from its two artifacts and the explanation, downstream stages rerun, then recheck. Notes: this sequential checking protocol is the one slide 15 comes back to. | Fig 2 full framework (re-render TikZ from `repair.tex`) |
| 10 | Title Only | The loop, as an algorithm | Bounded repair: at most K rounds of check, diagnose, repair, rerun downstream. Returns SUCCESS with the equivalent pair, or FAILURE with the last artifacts once the budget is spent. K = 3 in all experiments because gains flatten quickly. Notes: types of D and R_i, and that each T_i and R_i is one stateless LLM call with the schema in the prompt. | Algorithm 1 rendered as image |
| 11 | Section | Experiments | divider | none |
| 12 | Title, Bullets & Photo | Two bodies of law, two LLMs, one solver | Traffic: 150 rules from the Texas Transportation Code. Wildlife: 77 rules from the Texas Parks and Wildlife Code. A rule is one statutory provision, formalized on its own. Many-sorted FOL over a curated domain schema (about 200 predicates). Two commercial LLMs from different vendors, Claude Opus 4.6 (Anthropic) and GPT-5.2 (OpenAI), each given the same fixed instruction text (a prompt). Z3 decides every check in under a second. Notes: two domains times two LLMs gives the four domain-model pairs used later. | Traffic schema excerpt (SMT-LIB listing from appendix) as the right-side image |
| 13 | Title & Bullets | Three baselines, two design choices | No repair: the first pass is final. Random stage: same loop, but the stage is picked uniformly at random, so it tests whether diagnosis matters. Regenerate: redo the whole pipeline from x, so it tests whether scoping matters. Full: diagnosis plus scoped repair. All share the same first pass and K = 3. Notes: two metrics from here on. Equivalence rate is the share of rules whose final check is UNSAT. Cost is LLM calls spent on repair divided by the number of rules repair brought to equivalence. | none |
| 14 | Title Only | Scoped repair wins only with Claude | One LLM formalizes, diagnoses, and repairs. With Claude, Full reaches the highest equivalence rate at the lowest cost on both domains. With GPT, Regenerate beats Full and Full is the most expensive. Notes: each table row is one domain and one LLM. | Table 1, same-model rows (2 domains x 2 LLMs, 4 rows) rendered as image |
| 15 | Big Fact | 97% | Caption: of GPT's diagnoses blame stage 1 on Wildlife (83% on Traffic). Notes: stage-1 repairs rerun everything downstream, so Full degenerates into Regenerate plus a judge call, which is the cost gap on slide 14. Re-judging the same GPT artifacts with a prompt that drops the examine-in-order instruction gives 9% on Traffic and 16% on Wildlife, so the skew comes from the judge protocol, not from the data. | none |
| 16 | Title Only | Swap the judge, keep everything else | Claude diagnoses, GPT still writes and repairs every formula. Equivalence rises from 82.7% to 90.7% on Traffic and from 78.9% to 94.7% on Wildlife, and cost per repaired rule falls from 14.6 to 7.9 and from 26.4 to 6.1 LLM calls, below every repair method. The diagnoser was the bottleneck, not the pipeline or the repair operators. | Table 1, GPT block (same-model rows and Claude-judge rows, 2 per domain) rendered as image |
| 17 | Title, Bullets & Photo | A second opinion from a text classifier | Slide 7 said agreement is evidence, not proof. To test how good the evidence is we need a measure of meaning preserved between x and x' that never touches the solver. Natural language inference (NLI): a learned classifier that, given two sentences, estimates how likely one entails or contradicts the other. Run both ways between x and x' (nothing lost, nothing added). Drift means x' says something different from x, the classifier's Unrelated or Contradiction outcomes in the tree. Post-hoc only, the repair loop never sees it. Notes: the six categories and thresholds are in the figure, and only the bottom two separate passing from failing rules. | Fig 3 NLI decision tree (re-render TikZ from `nli-signal.tex`) as the right-side image |
| 18 | Title Only | Failing rules drift twice as much | Failing means still SAT after Full repair. On all four domain-model pairs, failing rules drift 1.4 to 2.5 times more often than passing ones, 2.0 times pooled, and the gap is already there before any repair. So the check carries real signal about faithfulness, which is the claim behind slide 7. Notes: drift is itself a proxy. A blind human check on 25 rules judged 13 of 14 passing formalizations faithful against 8 of 11 failing ones. | Fig 4 `figures/drift_bars.pdf` |
| 19 | Section | What is left | divider | none |
| 20 | Title & Bullets | What repair cannot fix | 26 of the 227 rules stay non-equivalent under every method and both LLMs. Four patterns: schema vocabulary gaps, compound AND/OR conditions, exception clauses that T2 restates positively, thresholds that depend on another variable. The residual bottleneck is rule structure, not the iteration budget (slide 16 was about the diagnoser). | none |
| 21 | Title, Bullets & Photo | Where the proxy can be wrong | False accepts: a shared mistake in T1 and T3 passes (slide 7). False rejects: one sentence can have several faithful encodings, and two faithful outputs are reported as a disagreement when their equivalence is only provable through a library proof, outside what a decision procedure or our solver check establishes. Scope: Texas statutes in English, formalized one rule at a time despite cross-references. | Lean snippet as image: two faithful encodings of "there are infinitely many primes", `forall n, exists p, n < p and p.Prime` versus `{p \| p.Prime}.Infinite` |
| 22 | Title & Bullets | What comes next | Post-training means training an LLM further to maximize a numeric score, called a reward. For faithful autoformalization we need a faithfulness score, and roundtrip equivalence is one that needs no labels. Bring NLI or an LLM check into the loop. Formalize clusters of cross-referenced rules together. | none |
| 23 | Title | Roundtrip equivalence is a proxy for faithfulness with no ground truth | Body: Findings of EMNLP 2026. Footer: code, data, prompts, schemas at github.com/daneshvar-amrollahi/roundtrip-autoformalization. | none |

## Assets to prepare before the build

- Re-render as standalone PDFs then PNGs: Fig 1 (`intro.tex`, keep the x, y_orig, x', y_rt labels),
  Fig 2 (`repair.tex`), Fig 3 (`nli-signal.tex`).
- LaTeX renders: related-work cluster table (slide 3), stage types plus check (four lines, adapt
  `exports/eq/stages.tex`), Algorithm 1, Table 1 split into two images (same-model rows for both
  LLMs, then the GPT block with Claude-judge rows), traffic schema listing, Lean snippet.
- Rasterize `figures/drift_bars.pdf` at a resolution that keeps tick labels above 26 px when scaled
  to the 1730 px content width.

## Backup slides (not built unless asked)

- Table 4 stage diagnosis distribution, all rows.
- `figures/repair_curve.pdf`, cumulative UNSAT per iteration (not used in the paper).
- Human evaluation (Table 8) and pre-repair drift (Table 7).
- Run-to-run variance (Table 9).
- Q&A only: the closest work (Karia et al. roundtrip from a generated formal expression, Li et al.
  2024 self-consistency, ReForm, FormalAlign) with one line each on the difference. Not for the
  talk flow.
