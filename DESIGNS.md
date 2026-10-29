# Design System — Resume Slides

Reverse-engineered from *"How to Sell Consumer Apps Globally"* (Radja Thaher / ALIF Academy).
Editorial, magazine-like: heavy grotesk + italic serif, lots of white, one loud color bar per slide, 3D emoji as the only illustration.

---

## 1. Canvas

| Property | Value |
|---|---|
| Size | **1440 × 810 pt** (16:9) |
| Side margin | **54 pt** left and right |
| Top kicker baseline | 50 pt from top |
| Headline top | ~130 pt from top |
| Bottom bar | 64 pt tall, bottom edge ~76 pt from page bottom, spans margin → margin |
| Default background | `#FFFFFF` |

## 2. Color

| Token | Hex | Use |
|---|---|---|
| `ink` | `#111111` | All primary text, rules, title-slide background |
| `paper` | `#FFFFFF` | Default background, text on color |
| `muted` | `#6B6B6B` | Secondary text, captions, column headers |
| `hairline` | `#E6E6E6` | Row dividers in tables/lists |
| `mustard` | `#D9A520` | Intro-section bottom bars, highlight rows |
| `blue` | `#2643A8` | Act 01 — bars, section-divider background |
| `red` | `#E0352B` | Act 02 — bars, section-divider background |
| `green` | `#3E8E4E` | Act 03 — bars, section-divider background |
| `ghost` | paper @ 25% over color | Giant section numerals ("01") on divider slides |

**Rules**
- Each slide gets **one** accent color, and it shows up only in the bottom bar (plus maybe one highlighted row/card). Everything else is ink on paper.
- The accent follows the section: mustard = intro, blue = act 1, red = act 2, green = act 3.
- On mustard the text is **ink**. On blue, red or green it is **paper**.

## 3. Typography

Two families, used in a strict pattern.

| Role | Font | Size | Tracking | Notes |
|---|---|---|---|---|
| Headline (sans half) | **Archivo Black** (wght 900) | 64–76 pt | **−4%** (tight) | Sentence case, ends with punctuation |
| Headline (serif half) | **DM Serif Display Italic** | same as sans | 0 | The "second voice" of the headline |
| Section numeral | Archivo Black | 260 pt | −6% | `ghost` color, divider slides only |
| Kicker (top-left) | Archivo Bold | 8.5 pt | **+18%** | ALL CAPS, `SECTION · TOPIC` with a middle dot |
| Brand mark (top-right) | DM Serif Display Regular | 13 pt | +12% | ALL CAPS |
| Subhead / item title | Archivo Bold | 20–26 pt | −2% | |
| Body | Archivo Regular | 15–18 pt | 0 | `ink` or `muted` |
| Column header / label | Archivo SemiBold | 8.5 pt | +14% | ALL CAPS, `muted` |
| Big stat number | Archivo Black | 56–72 pt | −4% | |
| Bar text (left) | Archivo Bold | 18 pt | −1% | Takeaway sentence |
| Bar text (right) | DM Serif Display Italic | 18 pt | 0 | Short kicker, e.g. *"Then go for 100."* |

**The headline formula** — always two voices in one line:

> **Heavy sans statement,** 🚀 *italic serif twist.*

- Example: **"Build it, sell it,"** 🚀 *"count the cash."*
- An inline 3D emoji (about 0.9× cap height + ascender) goes between the halves, or after the sans half.
- Headlines can wrap onto two lines; the second line is often entirely serif italic.

## 4. Imagery

- **3D emoji only** (Microsoft Fluent Emoji 3D, `assets/emoji/*.png`). No stock photos, gradients or shadows.
- Use them inline in headlines (~64 pt), as row icons (~36 pt), and as card heroes (~72 pt).
- At most one emoji per headline.

## 5. Layout components

### Chrome (every content slide)
```
INTRO · WHO'S TALKING                                   ALEX MORGAN
                                                        (serif caps)
Headline sans part, 🎯 serif italic part.
───────────────────────────────────────────── (1.5 pt ink rule, full width)
  content …
█████ Bold takeaway sentence.                    Italic serif kicker. █
```

### Rule + table
- A 1.5 pt ink rule sits under the headline area. Content tables start under it.
- Rows are separated by 0.75 pt `hairline` lines. There are no vertical lines and no zebra striping.
- Column headers are tiny tracked caps in `muted`, optionally numbered (`01 · BUILD`).

### Bottom bar
- A solid accent rectangle, margin to margin, 64 pt tall, with square corners.
- On the left, bold sans takeaway text. On the right, optional italic serif.

### Highlight row/card
- A full-width mustard row with a bold headline and a smaller line underneath (see "Latest product: …").

### Stat cards
- Very large Archivo Black number, a short label underneath, and a hairline divider above. No card fill.

### Section divider (act opener)
- Full-bleed `blue` / `red` / `green` background.
- Top-left: three small dots (filled = current act) plus `ACT 1 OF 3 · BUILD` in kicker style.
- Left: a giant ghost numeral `01`. Right: a three-line headline in paper (sans + serif italic + emoji).
- Bottom: `INSIDE THIS ACT:` followed by a dotted list of topics in small paper text.

### Title slide
- `ink` background with paper text.
- Kicker on the top-left (`LIVE WEBINAR · SAT 10 OCT 2026`) and the brand on the top-right.
- A three-line hero headline with inline emoji, closing on an italic serif line.
- `with <Name>`: *with* in serif italic, the name in Archivo Bold.
- A tricolor strip along the bottom edge, 32 pt tall, in thirds: blue / red / green, labelled `01 · BUILD`, `02 · SELL`, `03 · FINANCE` in tiny paper caps.

## 6. Voice

- Short, punchy, second person. Headlines are full sentences with a period.
- The serif half carries the emotion or the twist; the sans half carries the fact.
- Bar text is the single takeaway of the slide.

## 7. Files

| Path | What |
|---|---|
| `assets/fonts/Archivo-*.ttf` | Static instances of Archivo (400–900), cut from the variable font |
| `assets/fonts/DMSerifDisplay-*.ttf` | DM Serif Display Regular + Italic |
| `assets/emoji/*.png` | Fluent 3D emoji (MIT, microsoft/fluentui-emoji) |
| `make_sample.py` | Generates `sample-resume-slides.pdf` using this system |
