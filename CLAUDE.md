# CENTAUR 2026 talk

Keynote talk built from the paper in `paper/` (symlink to the EMNLP 2026 LaTeX sources)
using `template.key`, driven through osascript.

## Talk

- Length: 18 minutes. Plan for about 15 content slides plus title, section dividers, and a
  closing slide. Budget roughly one minute per content slide.
- Audience: Automated Reasoning people. They know formal methods well, including the dry
  parts (SMT, logics, semantics, soundness arguments). They do not know AI or NLP. Every
  LLM, autoformalization, or NLP term must be introduced before it is used, in words a
  formal methods person would accept.

## Files

- `intuition.md`: my rough take on the story. Written by me.
- `outline.md`: the slide-by-slide plan, produced in step 2 below.
- `notes/template.md`: layout inventory, placeholder geometry, and the preferred layouts.
- `notes/rubric.md`: the slide critique rubric used by slide-critic.
- `exports/talk.key`: the deck. PNGs go to `exports/talk/`, presenter notes to
  `exports/talk/notes.md`.
- `exports/test.key`, `exports/test/`: throwaway test deck, ignore.
- Equation sources and renders: `assets/eq/`. Figure renders if any: `assets/fig/`.

## Workflow

1. Read `paper/` and `intuition.md`. Follow the spirit of intuition.md. Deviate where the
   paper suggests something better, and list every deviation with a one-line reason at the
   top of outline.md.
2. Draft `outline.md`: one entry per slide with layout, title, subtitle, body, figure or
   equation, and presenter notes. Run the `audience-critic` agent on it in outline mode.
   Revise. Then STOP and wait for my approval. Do not build anything before that.
3. Build `exports/talk.key` with the keynote skill, export PNGs to `exports/talk/`, run the
   `slide-critic` agent. Fix MUST-FIX items only. Re-export and re-run. Stop at
   `VERDICT: PASS` or after 4 iterations, whichever comes first.
4. Dump presenter notes to `exports/talk/notes.md` (snippet in the keynote skill). Run
   `audience-critic` once in deck mode on the PNGs plus notes. Apply its fixes. Re-run
   `slide-critic` only on the slides that changed.
5. Report to me: the leftover NICE-TO-HAVE items, any remaining GAPS, and anything from
   either critic that needs my decision.

## Constraints

- Use only the layouts listed under "Preferred layouts for the talk" in `notes/template.md`.
- Text goes only into layout placeholders: title, body, and the subtitle, footer, caption,
  or attribution shape the layout provides. No free-floating text boxes.
- Figures and equations are inserted as images into the open area of Title Only or the
  image placeholder of a photo layout.
- Slides carry one point each. Details, caveats, numbers, and citations go in presenter
  notes, not on the slide.
- Never edit `template.key` in place. Never touch Keynote documents I have open myself.

## Tools

- The `keynote` skill (`.claude/skills/keynote/SKILL.md`) has the working AppleScript for
  every operation and the quirks already hit. Read it before touching Keynote.
- `notes/template.md` has every layout's placeholder positions in points.
