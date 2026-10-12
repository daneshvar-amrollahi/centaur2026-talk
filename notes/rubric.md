# Slide critique rubric

Applies to the PNGs in `exports/<deck>/` (1920 x 1080, one per slide).
Per-slide items are checked on each image alone. Deck items need the images in order.
Report each failure as `slide NN, item ID, one-line evidence`.

Reference sizes in the export: body text on the bullet layouts is about 40 px tall for a
capital letter, subtitles about 50 px, titles about 90 px. Left margin is 95 px.

## MUST-FIX

Per slide

- **M1 Text overflow or autoshrink.** Fail if text touches or crosses the slide edge, runs into
  another element, or is visibly smaller than the same slot on neighbouring slides (Keynote
  shrinks text silently when a box is full). Compare capital-letter height against the
  reference sizes above.
- **M2 More than 4 bullets.** Count bullet glyphs. Fail at 5 or more, including sub-bullets.
- **M3 Bullet longer than two lines.** Fail if any single bullet wraps past a second line.
- **M4 Figure unreadable at projection size.** Fail if the smallest text in a figure (tick
  labels, legend, annotations) is under 26 px tall in the export, or if lines, markers, or
  colour differences cannot be distinguished at 50% zoom of the PNG.
- **M5 Slide restates a paper paragraph.** Fail if the slide contains three or more full
  sentences of running prose, or if no single element (title, big statement, or highlighted
  result) states the one thing the audience should take away.
- **M6 No takeaway in the title.** Fail if the title is only a topic label ("Results",
  "Method") on a content slide rather than a claim or question. Section dividers are exempt.
- **M7 Elements overlap or fall off the slide.** Fail if any text, figure, or shape overlaps
  another element or is clipped by the slide boundary.
- **M8 Leftover template content.** Fail if a stock photo, placeholder label, or empty slot
  that visibly shifts the layout is still present.
- **M9 Figure or equation blurry.** Fail if edges of text or lines in an inserted image are
  visibly soft or pixelated at 100% zoom.

Deck

- **M10 Notation used before defined.** Walk the slides in order and keep a list of symbols
  (T1, Sigma, x', y^orig, and so on). Fail at the first slide that shows a symbol not defined
  on that slide or an earlier one.
- **M11 Terminology inconsistent across slides.** Keep a list of names for each concept
  (stage versus step, back-translation versus reconstruction, repair versus fix, roundtrip
  versus round-trip). Fail if any concept appears under two names.
- **M12 Unexplained reference.** Fail if a slide points at something the deck has not shown
  ("as we saw", "the earlier example", a figure legend entry never introduced).

## NICE-TO-HAVE

Per slide

- **N1 One visual per slide.** Flag slides with two or more figures, tables, or equations
  unless they are being compared side by side.
- **N2 Title fits on one line.** Flag titles that wrap.
- **N3 Margins respected.** Flag content whose left edge is not at 95 px or whose right edge
  passes 1825 px, except full-bleed images.
- **N4 Figure centred in its area.** Flag figures whose left and right gaps to the margins
  differ by more than 40 px, unless text sits beside them.
- **N5 Empty space balanced.** Flag slides where more than half the content area below the
  title is empty while text elsewhere is dense.
- **N6 Numbers trimmed.** Flag more than two significant figures in a headline number, or
  more than three numbers on one slide outside a table.
- **N7 Consistent capitalization.** Flag mixed Title Case and sentence case in titles or
  subtitles.
- **N8 Figure text matches slide text.** Flag figure labels whose names differ from the
  slide's own wording for the same thing (model names, dataset names, stage labels).
- **N9 Readable colour contrast.** Flag grey-on-white text lighter than the template's own
  body grey, and figure colours that cannot be told apart in a greyscale view.
- **N10 Equation image size.** Flag equations whose character height is smaller than body
  text or larger than the subtitle.

Deck

- **N11 Section dividers present.** Flag runs of more than six content slides with no
  Section slide.
- **N12 Visual rhythm.** Flag three or more consecutive bullet-only slides.
- **N13 Consistent figure style.** Flag figures that differ in font, colour palette, or
  background from the others.
- **N14 Closing slide states the contribution.** Flag a final slide that is only a thank-you
  or a reference list.
