# centaur2026-talk

Slides for my CENTAUR 2026 talk, built in Keynote by Claude Code from a paper and a Keynote
template. The template and the agentic setup are meant to be reused for future talks.

## How it works

1. You write `intuition.md` (your rough take on the story) and point `paper/` at the LaTeX sources.
2. Claude drafts `outline.md`, one entry per slide. The `audience-critic` agent reviews it, then
   Claude stops and waits for your approval.
3. Claude builds the deck from `template.key` through AppleScript (`osascript`), exports PNGs, and
   loops with the `slide-critic` agent until the slides pass the rubric.
4. Presenter notes are dumped to markdown and the whole deck gets one final audience pass.

The full workflow, talk length, audience, and constraints live in `CLAUDE.md`.

## Layout

| Path | What it is |
|---|---|
| `CLAUDE.md` | Talk spec and workflow. Edit this first for a new talk. |
| `template.key` | Keynote template (Minimalist Light, 1920 x 1080). Never edited in place. |
| `notes/template.md` | Layout inventory with placeholder geometry, plus the preferred layouts. |
| `notes/template-layouts/` | Thumbnail of each layout with its placeholders labeled. |
| `notes/rubric.md` | Rubric used by `slide-critic`. |
| `.claude/skills/keynote/` | Working AppleScript for every Keynote operation, plus known quirks. |
| `.claude/agents/` | `audience-critic` (outline and deck review) and `slide-critic` (per-slide rubric check). |
| `build/` | Deck generator (`gen_build.py` writes `build.applescript`), notes dump, figure scripts. |
| `assets/eq/`, `assets/fig/` | LaTeX sources and PDF renders for equations and figures. |
| `exports/` | The built deck (`talk.key`), PNG exports, and presenter notes. |
| `intuition.md`, `outline.md` | Talk-specific story and slide plan. |

## Reusing for a new talk

Keep `template.key`, `notes/`, `.claude/`, and `build/dump-notes.applescript`. Replace
`intuition.md`, `outline.md`, `assets/`, and `exports/`, repoint the `paper` symlink, and update the
talk section of `CLAUDE.md` (length, audience). Paths are resolved relative to the project root, so the folder can live anywhere.

Requires macOS with Keynote, a LaTeX install (`pdflatex`), and `pdftoppm` (poppler).
