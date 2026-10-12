# template.key inventory

Inspected 2026-10-01 on a scratch copy of `template.key` opened in Keynote 14.2 via `osascript`.
The copy was closed without saving. The original `template.key` was not touched.

## Document

| Property | Value |
|---|---|
| Slide size | 1920 x 1080 |
| Theme | Minimalist Light |
| Existing slides | 1 (layout "Title", every placeholder empty, no presenter notes) |
| Slide layouts | 17 |

Coordinates below are in slide points, origin top left, written as `x,y w x h`.
Left margin is 95 everywhere. Full-width text runs 1730 wide. Half-width text runs 770 wide.

## Layouts

| # | Layout name | Title | Body | Extra text slot (a `shape`) | Image placeholders |
|---|---|---|---|---|---|
| 1 | Title | yes, `95,206 1730x366` | yes, `95,579 1730x158`, plain subtitle lines | footer line `95,966 1730x52` (small, bottom left) | none |
| 2 | Title & Photo | yes, `95,206 1730x366` | yes, `95,579 1730x158` | footer line `95,966 1730x52` | 1 full bleed `0,0 1920x1080` (behind text) |
| 3 | Title & Photo Alt | yes, `95,105 770x463` | yes, `95,563 770x424` | none | 1 right half `975,0 945x1080` |
| 4 | Title & Bullets | yes, `95,50 1730x133` | yes, `95,335 1730x650`, bulleted | subtitle `95,183 1730x79` under the title | none |
| 5 | Bullets | hidden | yes, `95,335 1730x650`, bulleted | none | none |
| 6 | Title, Bullets & Photo | yes, `95,50 770x133` | yes, `95,335 770x650`, bulleted | subtitle `95,183 770x79` | 1 right half `975,0 945x1080` |
| 7 | Title, Bullets & Live Video Small | yes, `95,50 1730x133` | yes, `95,335 770x650`, bulleted | subtitle `95,183 1730x79` | none (right half is empty, reserved for live video) |
| 8 | Title, Bullets & Live Video Large | yes, `95,50 770x133` | yes, `95,335 770x650`, bulleted | subtitle `95,183 770x79` | none (right half empty) |
| 9 | Section | yes, `95,308 1730x366`, large | hidden | none | none |
| 10 | Title Only | yes, `95,50 1730x133` | hidden | subtitle `95,183 1730x79` | none |
| 11 | Agenda | yes, `95,50 1730x133` | yes, `95,335 1730x650`, plain lines without bullets | subtitle `95,183 1730x79` | none |
| 12 | Statement | hidden | yes, `95,330 1730x322`, centered, large | none | none |
| 13 | Big Fact | hidden | yes, `95,95 1730x579`, centered, very large | caption `95,640 1730x85` centered under the fact | none |
| 14 | Quote | hidden | yes, `409,328 1102x349`, large | attribution `430,753 1081x55` under the quote | none |
| 15 | Photo - 3 Up | hidden | hidden | none | 3 images: `99,286 574x508`, `673,286 574x508`, `1245,286 574x508` |
| 16 | Photo | hidden | hidden | none | 1 full bleed `0,0 1920x1080` |
| 17 | Blank | hidden | hidden | none | none |

Thumbnails of each layout with the placeholders filled with labels are in `notes/template-layouts/`
(TITLE, BODY lines, and EXTRA mark the three text slots).

### Stock images in the image placeholders

These are the theme's sample photos. They will need replacing on any photo layout we use.

| Layout | File name in placeholder | Description |
|---|---|---|
| Title & Photo | `1387253285_3212x2409_JS.jpg` | Futuristic, curved, white structure |
| Title & Photo Alt | `613219920_1620x1620.jpg` | Close-up of a curved, white, layered pattern |
| Title, Bullets & Photo | `1254439506_1418x1891.jpg` | Close-up of the edge of white curved stone |
| Photo - 3 Up | `613219920_861x861_flip.jpg`, `937803416_1143x762.jpg`, `968312736_1142x762.jpeg` | layered white pattern, gray stone, white ribbed pattern |
| Photo | `1316507664_2880x1920_JS.jpg` | Angular, futuristic, white corridor with shadows |

## Preferred layouts for the talk

- Title: opening slide. Footer slot fits venue and date.
- Section: part dividers.
- Title & Bullets, Title Only: the workhorse content slides. Title Only leaves a clean 1730 x 800 area below the subtitle for figures placed by script.
- Title, Bullets & Photo: text left, figure right. The image placeholder on the right accepts a figure PNG.
- Statement, Big Fact: one-line takeaways and headline numbers.
- Quote: for quoting a definition or a reviewer.
- Blank, Photo: full-bleed figures.
- Agenda: outline slide.
- Live Video layouts: not useful here.

## Scripting notes (verified on the scratch copy)

- Make a slide on a layout with `make new slide at end with properties {base layout:slide layout "Title & Bullets"}` inside `tell doc`.
- Title and body are reached through `default title item of slide` and `default body item of slide`. Set `object text` on them. Check `title showing` and `body showing` first. When hidden, these accessors still return an item, but it reports position `0,0` and size `0 x 0`.
- `text items of slide` lists each visible placeholder twice (both entries are the same object, setting one changes the other) plus one 0 x 0 ghost for each hidden placeholder. Do not count on `text items` for anything beyond iteration.
- The extra slot (footer, subtitle, caption, attribution) is `shape 1 of slide`. It accepts `set object text of shape 1 of slide to "..."`. Every layout that has one has exactly one shape, so `shape 1` is unambiguous on a fresh slide.
- `class of` every text item reports `shape` in this Keynote version. Use geometry, not class, to tell items apart.
- Image placeholders show up in `images of slide` with `file name` and `description`. The `file` property is read only (verified: `set file of image` fails). To replace one, record its position and size, `delete` it, and `make new image with properties {file:...}` at the same geometry.
- Deleting several slides by stored reference fails silently once indices shift. A loop over 17 stored references deleted only 9. Delete from the last slide backwards, or re-fetch `slide N of doc` each time.
- Export to PNGs works with `export doc to (POSIX file folder) as slide images with properties {image format:PNG, skipped slides:false}`. Files come out as `<docname>.001.png`, `<docname>.002.png`, and so on. Placeholders with empty text render as nothing, so an untouched slide exports blank.
- Line breaks inside a body: join with `return`. Bulleted layouts bullet each line.
- Reading `position of x` must go through a variable (`set pos to position of x`, then `item 1 of pos`). Inline `item 1 of (position of x)` fails with a coercion error.
- `it` is a reserved word and cannot be a handler parameter.
