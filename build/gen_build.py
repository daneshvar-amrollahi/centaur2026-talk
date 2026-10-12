# Notes are plain keyword lines since 2026-10-05 (full prose script in exports/talk/script.md).
# Snapshot of the spec matching exports/talk.key as of 2026-10-02 (23 slides after the 2026-10-05 NLI split and the removal of the proxy statement and related-work slides, after the
# author's slide 2 edits and the slide 3 related-work rework were synced in). Run `python3 gen_build.py` to regenerate
# build.applescript next to this file, then `cp template.key exports/talk.key` and
# `osascript build/build.applescript`. Hand edits in Keynote made after this snapshot are
# NOT reflected here. Rebuilding overwrites them.
# Generates build.applescript for the talk deck from a slide spec.

def q(s):
    """AppleScript string literal from a Python string. Paragraphs joined with return."""
    parts = s.split("\n")
    esc = lambda t: '"' + t.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return " & return & ".join(esc(p) for p in parts) if parts else '""'

# (layout, title, subtitle/footer/caption, body, notes, image, box)
# box: (x, y, w, h) area to fit the image into. None = no image.
TO_BOX = (95, 280, 1730, 750)       # Title Only open area
PH_BOX = (1000, 140, 825, 800)      # right half of the photo layout

slides = []

slides.append(dict(layout="Title",
    title="Faithful Autoformalization via Roundtrip Verification and Repair",
    sub="CENTAUR 2026",
    body="Daneshvar Amrollahi†, Jerry Lopez‡, Clark Barrett†\n†Stanford University, ‡Independent researcher\nFindings of EMNLP 2026",
    notes="joint work with Jerry Lopez and Clark Barrett; Findings of EMNLP 2026\none sentence: a proxy for faithfulness that needs no ground truth (no human-written reference formula)"))

slides.append(dict(layout="Title & Bullets",
    title="What is faithful autoformalization?",
    sub="",
    body="Autoformalization: an LLM translates natural language (e.g., a loan rule/theorem in NL) into a machine-checkable formal representation (an FOL formula, or a Lean theorem)\n"
         "Faithful: the formalization captures what the sentence says, nothing lost, nothing added\n"
         "Our instance: Texas statutes to FOL.",
    img="assets/fig/autoformalization.pdf", box=(95, 690, 1730, 330),
    notes="LLM: learned text generator, no specification, output must be checked\nautoformalization: sentence in, formula out; parses, type checks, satisfiable, can still be wrong\nfaithful: says what the sentence says, nothing lost, nothing added; dashed red line is the question\nour instance: Texas statutes to FOL, Z3; framework only needs an equivalence check on the target"))

slides.append(dict(layout="Section", title="Roundtrip verification",
    notes="part one: the roundtrip check"))

slides.append(dict(layout="Title Only",
    title="Formalize twice, then compare",
    sub="If every stage keeps the meaning, the two formulas are equivalent",
    img="assets/fig/roundtrip.pdf", box=TO_BOX,
    notes="x, T1, y orig, T2, x prime, T3, y rt; three separate LLM calls, they can disagree\nsecond formalization because two formulas go to a solver, two sentences cannot\nall stages faithful implies equivalent, so disagreement means some stage lost or added meaning, no ground truth needed\nagreement not a guarantee; wrong formulas rarely survive the trip unchanged, tested later"))

slides.append(dict(layout="Title Only",
    title="Equivalency check",   # retitled by the author by hand, 2026-10-05
    sub="UNSAT means equivalent, SAT gives a counterexample",
    img="assets/fig/check.pdf", box=(95, 285, 1730, 740),
    notes="Sigma: the target formalism; everything hinges on Sigma coming with an equivalence check; here many-sorted FOL over the schema, Z3 decides\nX strings, Y Sigma well-formed formulas; T1 and T3 same type, T3 a fresh call so blame lands on a stage\nnegated biconditional, literally what goes to Z3 after the schema declarations\nUNSAT equivalent, SAT counterexample model\nthree LLM calls, one solver query; only the solver's answer has a guarantee, and it is about equivalence\nLean or any formalism with an equivalence check would work too"))

slides.append(dict(layout="Section", title="Diagnosis and scoped repair",
    notes="the other outcome, SAT: some stage lost or added meaning; part two is what to do about it"))

slides.append(dict(layout="Title Only",
    title="Disagreement points at a stage",
    sub="Name the first failed stage, repair only that stage",
    img="assets/fig/framework.pdf", box=TO_BOX,
    notes="blue text, orange formulas; on SAT an LLM judge D reads the four artifacts, not the counterexample\nexamine in order: x vs y orig, y orig vs x prime, x prime vs y rt; halt at first inconsistency; explanation names only those two artifacts\njudge never accepts, acceptance is still UNSAT; wrong diagnosis wastes a round, cannot make a wrong formula pass\nR i rewrites only that stage from its two artifacts plus the explanation; rerun downstream; check again\nexamine-in-order comes back in the results"))

slides.append(dict(layout="Title Only",
    title="At most three rounds of repair",
    sub="Stop at equivalence, or give up after K = 3",
    img="assets/eq/algorithm.pdf", box=TO_BOX,
    notes="at most K rounds: check, diagnose, repair, rerun; SUCCESS with the equivalent pair or FAILURE with the last artifacts\nK equals 3, gains flatten; K checks, up to K repairs\nevery T i, R i, D is one stateless LLM call; schema in the prompt; nothing carried between calls"))

slides.append(dict(layout="Section", title="Experiments",
    notes="part three: does this work in practice"))

slides.append(dict(layout="Title, Bullets & Photo",
    title="No ground truth",
    sub="Two domains, two LLMs",
    body="Traffic: 150 rules, Texas Transportation Code\n"
         "Wildlife: 77 rules, Texas Parks and Wildlife Code\n"
         "Many-sorted FOL over a curated schema, about 200 predicates\n"
         "Claude Opus 4.6 and GPT-5.2, same prompts. Z3 under 1 s per check",
    img="assets/eq/schema.pdf", box=PH_BOX,
    notes="Traffic 150 rules Texas Transportation Code, Wildlife 77 rules Parks and Wildlife Code; one provision, one rule, formalized alone\nno reference formalization exists, exactly the setting for the check\nmany-sorted FOL, curated schema, about 200 predicates, excerpt on the right\nClaude Opus 4.6 and GPT-5.2, same prompts; Z3 under a second; 7 unknown or errored queries across all runs counted as not equivalent\ntwo domains times two LLMs, four cells\nif asked about related work: learned alignment scorers (FormalAlign, ReForm) need labeled pairs to train; self-consistency (Li et al.) votes among sampled candidates with a prover plus a learned similarity; here one given formula, a solver, no labels, no human"))

slides.append(dict(layout="Title & Bullets",
    title="Three baselines, two design choices",
    sub="Random tests diagnosis. Regenerate tests scoping.",
    body="No repair: the first pass is final\n"
         "Random stage: same loop, stage picked uniformly at random, no diagnosis\n"
         "Regenerate: redo the whole pipeline from x, no diagnosis\n"
         "Scoped: diagnose the first failed stage, repair only that stage",
    notes="No repair: first pass final; Random: same loop, random stage, tests diagnosis; Regenerate: redo from x, tests scoping; Scoped: first failed stage only, rerun downstream (Full in the paper)\nsame first pass, K equals 3\nequivalence rate: share UNSAT at the end; cost: LLM calls on repair per rule brought to UNSAT\nrate is the proxy, not faithfulness; tested at the end of this section"))

slides.append(dict(layout="Title Only",
    title="Scoped repair wins only with Claude",
    sub="One LLM formalizes, judges, and repairs",
    img="assets/eq/table1-same.pdf", box=TO_BOX,
    notes="one LLM does everything; a row is domain times LLM\nClaude: scoped repair highest rate, lowest cost, both domains\nGPT: Regenerate beats scoped, scoped most expensive\nmethod depends on the model, why"))

slides.append(dict(layout="Big Fact",
    body="83% and 97%",
    sub="of GPT's diagnoses blame stage 1 (Traffic and Wildlife)",
    notes="83 and 97 percent of GPT's diagnoses blame stage 1\nstage-1 repair reruns everything, scoped degenerates into Regenerate plus a judge call, hence the cost gap\nre-judged the same artifacts without examine-in-order: blame drops to 9 and 16 percent, so it is the judge protocol with GPT, not the data\nkeep the protocol, it defines the first failed stage; change the judge instead"))

slides.append(dict(layout="Title Only",
    title="Swap the judge, keep everything else",
    sub="Claude judges, GPT still formalizes and repairs",
    img="assets/eq/table1-gpt.pdf", box=TO_BOX,
    notes="swap only the judge: Claude diagnoses, GPT still formalizes and repairs\nno-judge rows unchanged, shown once; red behind Regenerate, green back in front\nTraffic 82.7 to 90.7, Wildlife 78.9 to 94.7; cost 14.6 to 7.9 and 26.4 to 6.1 calls, below every other method\nthe judge was the bottleneck, not the pipeline, not the repair operators"))

slides.append(dict(layout="Title & Bullets",
    title="Does x' match x?",
    sub="No solver for sentences, so ask a text classifier",
    # Hand inserts on the live deck (2026-10-05): assets/fig/roundtrip-mini.pdf at height 260, right-aligned to x 1825, y 40,
    # and assets/fig/nli.pdf at width 1600 at (160, 460), sitting in the seven soft-break lines (U+2028) after bullet 1.
    body="Natural Language Inference (NLI) models evaluate text pairs (a premise, and a hypothesis) to determine whether the premise entails, contradicts, or is neutral toward the hypothesis.       \n"
         "We use facebook/bart-large-mnli, BART-large fine-tuned on MultiNLI, a corpus of human-labeled sentence pairs with those three labels",
    notes="x prime is y orig in words, so a lost or added meaning shows up as a difference from x; sentences cannot go to a solver, they can go to a text classifier\nNLI: premise and hypothesis in, probabilities of entailment, contradiction, neutral out; the soccer pair is the classic SNLI example; the numbers are illustrative\ntrained on human-labeled pairs; estimates, not decisions\nBART: Facebook AI 2019, pretrained to reconstruct corrupted text, summarization and translation; bart-large-mnli is BART-large fine-tuned on MultiNLI, about 433k labeled pairs, public\npost-hoc only, the repair loop never sees it"))

# Hand edit on the live deck (2026-10-05): in the next slide's body, the "min" of "Emin" and the
# "max" of "Cmax" are set to 0.62 x the body size (subscript look, Keynote scripting has no baseline shift).
slides.append(dict(layout="Title Only",
    title="NLI Categories",   # retitled by the author by hand
    sub="Both ways, worse one counts",
    img="assets/fig/nli-cats.pdf", box=TO_BOX,   # definitions typeset in LaTeX beside the tree, so symbols match exactly, 2026-10-05
    notes="both directions: E right, x entails x prime, nothing lost; E left, x prime entails x, nothing added; C the same for contradiction\nE min and C max take the worse direction; the tree gives six categories\nEquivalent leaf is the classifier's label, not the solver's verdict; Strengthened and Weakened unused\ndrift: Unrelated or Contradiction, the shaded leaves; fixed thresholds everywhere"))

slides.append(dict(layout="Title Only",
    title="Failing rules drift twice as much",
    sub="Failing means still SAT after scoped repair",
    img="assets/fig/drift_bars.pdf", box=TO_BOX,
    notes="failing means still SAT after scoped repair, same-model judge, first-table runs\nfailing rules drift 1.4 to 2.5 times more, 2.0 pooled; gap already there before any repair\ndrift is a proxy too, so blind human check on 25 rules: 13 of 14 passing faithful, 8 of 11 failing faithful\nmany failing rules still faithful: the false-reject side, coming in the limits\nthe claim from the roundtrip slide, now with evidence"))

slides.append(dict(layout="Section", title="Limits and what comes next",
    notes="part four: where it stops, what comes next"))

slides.append(dict(layout="Title & Bullets",
    title="Repair failures",   # retitled by the author by hand, 2026-10-05
    sub="26 of 227 rules resist every repair method for at least one LLM",
    body="Schema vocabulary gaps: the rule needs a predicate the schema does not have\n"
         "Compound conditions: “shall stop, yield, and grant immediate use of the intersection to a vehicle on the other roadway that is a hazard” "   # U+2028 soft breaks keep one bullet
         "hazard → (stop ∧ yield): all duties are owed to a hazard vehicle. stop ∧ (hazard → yield): you had to stop whether or not anyone was coming "
         "The solver finds a case with no hazard vehicle, so no yielding is required, but the two formulas differ on the stop\n"
         "Exception clauses: rules here are condition → required state, so “not required to” can only be written as “must not”\n"
         "Conditional thresholds: a bound that depends on another variable gets dropped",
    notes="residual: SAT before and after Random, Regenerate, Scoped; 11, 8, 2, 7 per cell, 26 unique, only 2 resist both LLMs; rule structure, not rounds\nschema gaps: safety zone strip between zone and curb, no predicate; repair answered SCHEMA_INSUFFICIENT; defile or canyon unknown to the schema\ncompound: hazard implies stop and yield, versus stop and hazard implies yield; solver's case a lone car, nobody around; grammar favours the first, cautious driving the second; roundtrip surfaced an ambiguity\nexceptions: not required to stop; rules are condition implies required state, no deontic operator, so both stages write must not stop; SAT only on a side guard, else a false accept\nthresholds: 20 feet on the station's side, 75 opposite, came back as a flat 75\nif asked why 3 rounds: 14 of 22 Claude Traffic failures lack a predicate, the rest cycle or fixate; residual rules longer\nif asked schema gap: a missing modality, not a predicate; reify required_to_stop, formalize with the rule it modifies"))

slides.append(dict(layout="Title Only",
    title="A proxy can fail",
    sub="Where the proxy goes wrong",
    img="assets/fig/proxyfail.pdf", box=TO_BOX,   # two columns: false accept (dropped bound, UNSAT) vs false reject (lane_adjacent symmetry, SAT), 2026-10-05
    notes="two directions, two columns\nfalse accept: both formulas drop the same constraint, the 50-foot upper bound; T1 drops it, T2 verbalizes without it, T3 never sees it; identical formulas, UNSAT, both wrong; illustrative, the real near miss was r143, both wrote must not stop\nfalse reject: move only to an adjacent lane; the two stages write adj a b vs adj b a; both faithful, adjacency is symmetric to any reader\nthe solver was never told; the schema has zero axioms; it returns a model: a move from l1 to l2 where adj(l1,l2) holds but adj(l2,l1) does not; one symmetry axiom fixes it\nequivalence is relative to the theory you hand the solver\nreal hit: rule 150, ft_15_sq vs ft_15 times ft_15, two names for one quantity, a schema smell; the ambiguity from the repair-failures slide is a false reject too\nif asked: adj stands for the schema's lane_adjacent; kinds are datatypes, distinct and exhaustive; relations uninterpreted, axiom-free; no unknowns or timeouts in the main repair logs"))

slides.append(dict(layout="Title & Bullets",
    title="Our evidence stops at Texas law",
    sub="One kind of text, one rule at a time, one noisy check",
    body="Texas law in English only. No claim for programs or scientific text\n"
         "Each rule is formalized alone, although rules cross-reference each other heavily\n"
         "The NLI check is itself noisy: a general-purpose model with known lexical biases on legal text",
    notes="English Texas statutes only; where a ground-truth-free check is most needed, 200-predicate schema, no hand verification at scale; no claim for code or scientific text\none rule at a time; statutes cross-reference, import definitions, suspend obligations elsewhere; clusters needed\nNLI noisy, lexical-overlap bias on legal text; partial mitigation, not a second oracle"))

slides.append(dict(layout="Title & Bullets",
    title="A reward with no ground truth",
    sub="Roundtrip equivalence as a post-training signal",
    body="Post-training: train an LLM further to maximize a numeric score, the reward\n"
         "Roundtrip equivalence can be that score, and it needs no ground truth\n"
         "Already happening: AWS (Sep 2026) fine-tunes an LLM into a reward model on Z3 equivalence verdicts, with roundtrip back-translation as a baseline",
    notes="post-training: train further to maximize a numeric reward; roundtrip equivalence is a candidate because it needs no ground truth\nguard: the false accept; a model must not learn to make T1 and T3 agree without being faithful\nAWS and Case Western, Sep 2026, Beyond Solver Verdicts: verdict-preserving unfaithfulness; SFT on Z3 equivalence labels against a reference encoding, reference-free score at test time; 0.96 AUROC, plus 11 points downstream\nthey cite the roundtrip check and run roundtrip back-translation as a baseline; their oracle needs a reference in training, the roundtrip needs none\nsmaller directions: NLI or LLM check inside the loop; cross-referenced clusters together\nonly if asked: their roundtrip baseline scores 0.578 AUROC on their reference-equivalence task, a different task from ours"))

slides.append(dict(layout="Title",
    title="Roundtrip equivalence is a proxy for faithfulness with no ground truth",
    # Hand edits on the live deck (2026-10-02), not reproduced by the generator: body box height
    # set to 300 (default 158 autoshrinks 5 lines), all paragraphs pinned to 44 pt, paragraphs 3
    # and 5 (the two address lines) set to Menlo-Regular 40 pt. Paragraph 4 is intentionally empty.
    body="Findings of EMNLP 2026\nCode, data, prompts, schemas:\ngithub.com/daneshvar-amrollahi/roundtrip-autoformalization\n\ndaneshvar@cs.stanford.edu  \u00b7  cs.stanford.edu/~daneshva",
    sub="Daneshvar Amrollahi, Stanford University",
    notes="proxy for faithfulness, no ground truth; code, data, prompts, schemas public; email and page; thank you"))

out = []
out.append('set P to (do shell script "cd \\"$(dirname " & quoted form of POSIX path of (path to me) & ")/..\\" && pwd") & "/"')
out.append('set deckFile to POSIX file (P & "exports/talk.key")')
out.append('set outFolder to POSIX file (P & "exports/talk")')
imgs = sorted({s["img"] for s in slides if s.get("img")})
for i, im in enumerate(imgs):
    out.append(f'set img{i} to POSIX file (P & "{im}")')
imgvar = {im: f"img{i}" for i, im in enumerate(imgs)}

out.append('''
on addSlide(doc, layoutName, titleText, subText, bodyText, notesText)
	tell application "Keynote"
		tell doc
			set s to make new slide at end with properties {base layout:slide layout layoutName}
		end tell
		if titleText is not "" then set object text of default title item of s to titleText
		if bodyText is not "" then set object text of default body item of s to bodyText
		if subText is not "" then set object text of shape 1 of s to subText
		if notesText is not "" then set presenter notes of s to notesText
		return s
	end tell
end addSlide

on fitImage(s, fileRef, boxX, boxY, boxW, boxH)
	tell application "Keynote"
		tell s
			set img to make new image with properties {file:fileRef}
		end tell
		set iw to width of img
		set ih to height of img
		if (boxW / iw) < (boxH / ih) then
			set width of img to boxW
		else
			set height of img to boxH
		end if
		set nw to width of img
		set nh to height of img
		set position of img to {boxX + (boxW - nw) / 2, boxY + (boxH - nh) / 2}
		return (nw as integer) & "x" & (nh as integer)
	end tell
end fitImage

on clearImages(s)
	tell application "Keynote"
		set n to count of images of s
		repeat with k from n to 1 by -1
			delete image k of s
		end repeat
	end tell
end clearImages
''')

out.append('set diag to ""')
out.append('tell application "Keynote"')
out.append('\tset doc to open deckFile')
out.append('\tdelay 1')
out.append('end tell')

# slide 1 is the existing Title slide
s1 = slides[0]
out.append('tell application "Keynote"')
out.append('\tset s to slide 1 of doc')
out.append(f'\tset object text of default title item of s to {q(s1["title"])}')
out.append(f'\tset object text of default body item of s to {q(s1["body"])}')
out.append(f'\tset object text of shape 1 of s to {q(s1["sub"])}')
out.append(f'\tset presenter notes of s to {q(s1["notes"])}')
out.append('end tell')

for n, s in enumerate(slides[1:], start=2):
    out.append(f'set s to my addSlide(doc, {q(s["layout"])}, {q(s.get("title",""))}, {q(s.get("sub",""))}, {q(s.get("body",""))}, {q(s.get("notes",""))})')
    if s.get("img"):
        if s["layout"] == "Title, Bullets & Photo":
            out.append('my clearImages(s)')
        x, y, w, h = s["box"]
        out.append(f'set diag to diag & "slide {n} image " & (my fitImage(s, {imgvar[s["img"]]}, {x}, {y}, {w}, {h})) & linefeed')

out.append('tell application "Keynote"')
out.append('\tsave doc')
out.append('\texport doc to outFolder as slide images with properties {image format:PNG, skipped slides:false}')
out.append('\tset diag to diag & "slides: " & (count of slides of doc)')
out.append('end tell')
out.append('return diag')

import os
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build.applescript"), "w").write("\n".join(out) + "\n")
print("slides:", len(slides))
