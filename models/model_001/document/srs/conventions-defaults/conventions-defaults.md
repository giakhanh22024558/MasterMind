# model_001_srs · conventions defaults

Default formatting applied when `<project-root>/model_001_srs-conventions.md` does not declare a value. Every value below is **decoded directly from a real standard SRS document** in actual use, and is encoded in [`srs_format.py`](../scripts/srs_format.py). Projects may override.

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../../core/meta/conventions-as-data-pattern/).)

## Page & margins

| Property | Default | Note |
|---|---|---|
| Paper size | A4 portrait (210 × 297 mm) | — |
| Margins | 19.05 mm on all four sides | = 1080 dxa |
| Header/footer distance | 12.5 mm | = 708 dxa |

## Font

| Role | Font | Size |
|---|---|---|
| Body text | Mulish | 11 pt |
| Table text | Mulish | 10 pt |
| Cover-page title | Mulish | 28 pt |
| Caption (figures) | Mulish italic | 9 pt |

## Color palette

| Name | Hex | Used for |
|---|---|---|
| Primary color | `193D74` | Heading 1/2, table-header background, H1 underline |
| Accent teal | `156082` | Heading 5 |
| Gray | `656668` | Heading 4, cover-page version line |
| Navy caption | `0E2841` | Captions |
| Body text | `252729` | Body text, Title, Heading 3 |
| Callout background | `FFF8DF` | Single-cell callout table (placeholder) |
| Table-header text | `FFFFFF` | Text on the blue header background |

## Headings

| Level | Size | Bold | Color | Numbering |
|---|---|---|---|---|
| Title | 28 pt | — | `252729` | — |
| Heading 1 | 16 pt | ✅ | `193D74` | `1` · with an **underline** `#193D74` |
| Heading 2 | 13 pt | ✅ | `193D74` | `1.1` |
| Heading 3 | 11.5 pt | ✅ | `252729` | `1.1.1` |
| Heading 4 | 11 pt | ✅ | `656668` | `1.1.1.1` (lowest numeric level) |
| Heading 5 | 11 pt | ✅ | `156082` | `A. B. C.` (uppercase, restarts per H4) |
| Heading 6 | 11 pt | — | `1F4D78` | `a. b. c.` (lowercase, restarts per H5) |

- The first frontmatter heading (`Lịch sử Phiên bản` — version history) is **not** numbered.

## Tables

| Property | Default |
|---|---|
| Content width | 171.9 mm (A4 − 2 margins) |
| Border | Single 0.5 pt, all cells |
| Header | Background `#193D74`, white bold 10 pt text |
| Body | 10 pt black text |
| Row with all cells identical | Auto-merged into one cell |

## Auto-generated conventions

| Convention | Default format |
|---|---|
| Component-table STT/ID codes | `COM-<Heading 4 without dots>-<NNN>` · continuous within the same H4 |
| Business Rule codes | `BR-<Heading 4 without dots>-<NNN>` |
| Figure numbers | `Hình <Heading 4>-<n>` · centered · applied to Wireframes + Flow diagrams |
| Cover page | Standalone on one page |
| Table of contents | Native TOC field levels 1-3, standalone on one page, updates when opened in Word |
| Page breaks | After the cover page · after the TOC · after `Lịch sử Phiên bản` (version history) |

## Footer

`{Project name}  ·  Software Requirements Specification` + right tab + `Trang {PAGE} / {NUMPAGES}` — all 9 pt.

## Legend of Loại / Thuộc tính (canonical)

The list of `Loại` (type — Input, Select, Button, Date Picker…) and `Thuộc tính` (attribute — `Required`, `Unique`, `Read-only`, `Max_N_char`, `[Mặc định]`…) values is **canonical**, defined in `LEGEND_TYPES` / `LEGEND_ATTRS` in [`srs_format.py`](../scripts/srs_format.py). The main document **reuses** them; it never creates new ones.

## When defaults apply

Any item the project does not declare in `model_001_srs-conventions.md` → takes the default here. The skill **acknowledges the source** when explaining:

- "Per the project's `model_001_srs-conventions.md`, used X"
- "The project did not declare Y, used the default from `conventions-defaults/`"
