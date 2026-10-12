---
name: keynote
description: Build and edit the talk deck in Keynote via osascript from template.key. Covers opening a copy, picking layouts, filling title/body/subtitle slots, inserting PDF figures and LaTeX equations as images, presenter notes, saving, and exporting PNGs for review. Use whenever creating or modifying .key files or rendering equations for slides.
---

# Keynote via osascript

Verified 2026-10-01 with Keynote 14.2 on the Minimalist Light template (1920 x 1080).
Layout inventory and placeholder geometry live in `notes/template.md`.

## Workflow

1. Copy `template.key` to the target path with `cp`. Never edit `template.key` in place.
2. Open the copy, build slides, `save`, then `export` PNGs to a folder.
3. Look at every exported PNG. Fix, re-export, look again.
4. Leave the user's own Keynote documents alone. Always address the deck by name
   (`document "test"`), never by `front document`.

Write scripts to a file in the scratchpad and run `osascript script.applescript`.
Return a string of diagnostics from the script, because output written before an
error is lost when the script aborts.

## Shell rules

- Use absolute paths everywhere. Parallel Bash calls share one shell, and a `cd` in
  one call changes the working directory of the others mid-run.
- Allowed without prompts: `osascript`, `pdflatex`, `pdftoppm`, `cp`, `mkdir`.
  `pdftocairo` is not on the allowlist but is the only way to get transparent PNGs.

## Open, address, save, export

```applescript
set P to "/abs/path/to/project/"
-- Build file references OUTSIDE the tell block. Inside it, POSIX file (variable)
-- is sent to Keynote and fails with "Can't get POSIX file ...".
set deckFile to POSIX file (P & "exports/test.key")
set outFolder to POSIX file (P & "exports/test")

tell application "Keynote"
	set doc to open deckFile
	delay 1
	-- ... build slides ...
	save doc
	export doc to outFolder as slide images with properties {image format:PNG, skipped slides:false}
end tell
```

Export writes `<docname>.001.png`, `<docname>.002.png`, ... at 1920 x 1080 into the
folder, overwriting silently. A slide whose placeholders are all empty exports as a
blank white image.

Close without saving (for throwaway inspection copies):

```applescript
tell application "Keynote" to close document "template-inspect" saving no
```

## Slides and text

```applescript
tell application "Keynote"
	set doc to document "test"
	set slideW to width of doc

	-- Slide 1 already exists in the template on the "Title" layout.
	set s1 to slide 1 of doc
	set object text of default title item of s1 to "Talk title"
	set object text of default body item of s1 to "Speaker name"
	set object text of shape 1 of s1 to "Venue, date"   -- footer line

	-- New slide on a named layout
	tell doc
		set s2 to make new slide at end with properties {base layout:slide layout "Title & Bullets"}
	end tell
	set object text of default title item of s2 to "Slide title"
	set object text of shape 1 of s2 to "Subtitle line under the title"
	set object text of default body item of s2 to "First bullet" & return & "Second bullet" & return & "Third bullet"

	-- Presenter notes. Paragraphs split on return.
	set presenter notes of s2 to "First paragraph." & return & "Second paragraph."
end tell
```

Text slot rules for this template:

- Title and body: `default title item of slide` and `default body item of slide`.
  Check `title showing of slide` / `body showing of slide` first. Hidden slots still
  return an item at position 0,0 with size 0 x 0.
- The third slot (footer on Title layouts, subtitle on Title & Bullets / Title Only /
  Agenda, caption on Big Fact, attribution on Quote) is `shape 1 of slide`. Fresh
  slides on those layouts have exactly one shape.
- `text items of slide` lists each visible placeholder twice (same object) plus a
  0 x 0 ghost per hidden one, and `class of` every item says `shape`. Iterate it only
  as a last resort and tell items apart by geometry.
- Line breaks inside a body are `return`. Bulleted layouts bullet each line.

## Images: PDF figures and PNGs

Keynote inserts PDF files directly as images. No conversion needed for paper figures.

```applescript
set figFile to POSIX file (P & "paper/figures/stage_per_iteration.pdf")  -- outside tell
tell application "Keynote"
	set s3 to slide 3 of document "test"
	tell s3
		set img to make new image with properties {file:figFile}
	end tell
	-- Inserted size is 1 point per pixel of the source (a 600 dpi PNG arrives huge).
	-- Setting height or width keeps the aspect ratio. Then center it.
	set height of img to 740
	set w to width of img
	set position of img to {(slideW - w) / 2, 280}
end tell
```

Usable figure area on "Title Only" (below the subtitle): x 95 to 1825, y about 280 to 1030.

Replacing an image: `set file of image ...` fails with "Can't set file of image".
Instead read its position and size, `delete` it, and `make new image` with the new
file, then restore the geometry. This is also how to replace the stock photos in the
photo layouts' image placeholders (`images of slide`, see `file name` and
`description` to identify them).

## Equations with pdflatex + standalone

Source file (one `.tex` per equation under `assets/eq/` for the talk, `exports/eq/` was the test):

```latex
\documentclass[border=4pt]{standalone}
\usepackage{times}
\usepackage{amsmath,amssymb}
\begin{document}
\Large
$\displaystyle
\begin{aligned}
T_1 &: \mathcal{X} \rightarrow \mathcal{Y}_{\Sigma} \\
T_2 &: \mathcal{Y}_{\Sigma} \rightarrow \mathcal{X}
\end{aligned}$
\end{document}
```

Do not use the `preview` class option with `align`/`equation`. Display environments
take the full line width, so the PDF is mostly whitespace and the equation shrinks to
a thumbnail on the slide. `aligned` inside inline math gives a tight box.

Build and rasterize (600 dpi so it survives scaling to 300 points tall):

```bash
cd /abs/path/exports/eq
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/abs/path/exports/eq stages.tex
pdftoppm -r 600 -png -singlefile stages.pdf stages            # white background
pdftocairo -png -r 600 -transp -singlefile stages.pdf stages   # transparent background
rm -f stages.aux stages.log
```

Then insert the PNG like any image and set `height` to roughly 90 to 110 points per
equation line (300 for three lines reads well).

## Per-paragraph fonts and placeholder autoshrink

The Title layout body (`95,579 1730x158`) holds three 55 pt lines only by autoshrinking them
to about 44 pt. Adding lines shrinks everything further (rubric M1). To add lines, grow the
box and pin the size yourself:

```applescript
set b to default body item of slide 24 of doc
set height of b to 300
set object text of b to "line 1" & return & "line 2" & return & "code line"
set size of object text of b to 44
set font of paragraph 3 of object text of b to "Menlo-Regular"   -- PostScript name
set size of paragraph 3 of object text of b to 40
```

Read a paragraph's font with `font of (paragraph k of object text of b)`, inline. Storing the
paragraph in a variable first coerces it to text and `font of` then fails with -1700.
Non-ASCII characters in a script file are unreliable under osascript; build them with
`character id 183` (middle dot) and the like. Menlo-Regular is the safe monospace choice:
the system SF Mono (`SFNSMono.ttf`) is not exposed to Keynote by name.

## Tables with colortbl: crop before inserting

A standalone table using `\rowcolor`, `\columncolor` or a negative `\multirow` header can come
out with uneven whitespace (one table had 23 pt on the left and 8 pt on the right), so centring
the image in the slide box leaves the visible table off-centre (rubric N4). Run
`pdfcrop --margins 8 table.pdf table.pdf` after pdflatex, then insert. Pale tints below about
`blue!10` are indistinguishable from `black!8` headers in greyscale (rubric N9).

## Dumping presenter notes to a file

The critic agents are read only, so notes must be written to disk before deck mode.
Return the markdown from the script and redirect it in the shell.

```applescript
tell application "Keynote"
	set doc to document "talk"
	set out to ""
	repeat with s in slides of doc
		set out to out & "## Slide " & (slide number of s) & ": " & (object text of default title item of s as text) & linefeed & linefeed
		set out to out & (presenter notes of s as text) & linefeed & linefeed
	end repeat
end tell
return out
```

```bash
osascript dump-notes.applescript > /abs/path/exports/talk/notes.md
```

Paragraph breaks inside notes come out as carriage returns. Normalize with
`tr "\r" "\n"` if a reader needs real newlines.

## Inspecting a deck

```applescript
tell application "Keynote"
	set doc to document "test"
	repeat with s in slides of doc
		log (slide number of s) & " " & (name of base layout of s) & " | " & (object text of default title item of s as text)
		repeat with im in images of s
			set pos to position of im
			log "  image " & (file name of im) & " " & (item 1 of pos as integer) & "," & (item 2 of pos as integer) & " " & (width of im as integer) & "x" & (height of im as integer)
		end repeat
		log "  notes paragraphs=" & (count of paragraphs of presenter notes of s)
	end repeat
end tell
```

## AppleScript gotchas hit so far

- `it` is a reserved word and cannot be a handler parameter.
- `item 1 of (position of x)` fails with a coercion error. Do `set pos to position of x`
  first, then `item 1 of pos`.
- A `try` block ends with `end try`. Mixing it up with `end tell` gives
  "Expected end but found end tell" and the whole script refuses to compile.
- Deleting several slides through stored references fails silently as indices shift
  (a loop over 17 references deleted 9). Delete from the last slide backwards, or
  re-fetch `slide N of doc` each time.
- Keynote names a document after its file name without extension. Opening a second
  file with the same base name makes `document "name"` ambiguous, so give test copies
  distinct names.
- osascript prints `return` characters in a way that makes multi-line text look joined.
  Trust `count of paragraphs` or the exported PNG, not the console echo.

## Sizing rules measured on the talk deck (2026-10-01)

Measured on the exported PNGs of `exports/talk.key` against `notes/rubric.md`.

- Content titles render at about 43 px per character. The 1730 px title slot on Title Only
  and Title & Bullets holds about 40 characters. The 770 px slot on Title, Bullets & Photo
  holds 17 characters, after which Keynote autoshrinks silently (rubric M1).
- Subtitles render at about 25 px per character: about 65 characters on the full-width
  slot, about 30 on the photo layout.
- Body text on the photo layout wraps at about 30 characters per line, so a bullet there
  must stay under about 55 characters to fit two lines (rubric M3). Full-width bullets
  wrap at about 85 characters per line.
- Figure text must be at least 26 px tall in the export (rubric M4). A figure that fills the
  1730 x 750 area is scaled by min(1730 / width, 750 / height). For a TikZ figure of the
  paper's size (about 440 x 220 pt) that is roughly 3.4x, so every label needs a font of
  at least 12 pt at native size (cap height about 0.66 em). The practical recipe: build
  standalone figures with `12pt` class option and `font=\Large` on the whole picture, drop
  `\scriptsize` and `\footnotesize` entirely, and keep tables and listings under about
  75 characters per row (tables) or 30 characters per line (listings on the photo layout).
- Keynote inserts PDFs as vectors, so re-rendering the TikZ figures from the paper as
  standalone PDFs (`assets/fig/*.tex`) and inserting the PDF keeps them sharp (rubric M9).
- An `algorithmic` block of 16 lines is too tall for 26 px text. `\usepackage[noend]{algorithmic}`
  drops the `end if` and `end for` lines and brings a 15-line algorithm to 12 lines.
- `matplotlib` figures from `paper/figures-src/` can be regenerated for the deck by importing
  `style.py` with `OUT_DIR` redirected to `assets/fig/` and the rcParams font sizes raised to
  13 to 15 pt. The data for the drift chart is hard-coded in `style.py`, no run data needed.

## More AppleScript gotchas

- `by` is a reserved word (the step keyword in `repeat ... by`). A handler parameter named
  `by` makes the whole script fail to compile with "Expected expression but found by" at
  an unrelated line. The same goes for `it`, `to`, `in`, `of`, `at`, `from`.
- Generating the build script from a Python spec (`gen_build.py` writes `build.applescript`)
  is the reliable way to handle quoting and `return` separators in long notes. Escape
  backslashes and double quotes, join paragraphs with ` & return & `.
- To rebuild from scratch: `close document "talk" saving no`, `rm` the deck, `cp` the
  template again, run the build. Deleting slides in place is slower and error-prone.
- To swap one figure without a rebuild: delete `image k of slide N` from the last index
  down, `make new image`, size it, then `save` and `export` again. Export rewrites all PNGs.
- Exporting slide images to a folder replaces that folder's contents. `exports/talk/notes.md`
  vanished after a re-export on 2026-10-02. Always re-run `build/dump-notes.applescript`
  after the last export, and never keep anything else in the export folder.
