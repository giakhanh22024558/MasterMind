# model_001_srs · conventions schema

Checklist of the conventions a project must declare when using the `model_001_srs` skill. The project fills this schema into `<project-root>/model_001_srs-conventions.md`; any item left blank → falls back to [`conventions-defaults/`](../../conventions-defaults/).

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../../../core/meta/conventions-as-data-pattern/).)

## Required conventions

### 1 · Project identity

| Item | Format | Default | Example |
|---|---|---|---|
| Project name | Short text | (taken from the cover-page title of the `.md`) | `RoomBooking` |
| Document subtitle | Text | `Software Requirements Specification` | — |
| Logo path | Path to an image file (.png) | [`scripts/v1/assets/srs_logo.png`](../../scripts/v1/assets/srs_logo.png) | `assets/my_logo.png` |

> The project name is **not hard-coded** — the generator takes it from the first title line of the `.md` frontmatter and passes it into the footer and cover page.

### 2 · Document metadata

| Item | Format | Default | Example |
|---|---|---|---|
| Version | `Draft x.y.z` semver | `Draft 1.0.0` | `Draft 1.0.3` |
| Date | `DD/MM/YYYY` | (creation date) | `19/05/2026` |
| Prepared by | Text | `[Đội kỹ thuật]` | `Đội kỹ thuật Slitigenz` |

### 3 · Color palette (optional override)

| Item | Format | Default | Note |
|---|---|---|---|
| Primary color | Hex `RRGGBB` | `193D74` | Heading 1/2 + table-header background + H1 underline |
| Accent color | Hex | `156082` | Heading 5 |
| Body text color | Hex | `252729` | — |

> Most projects **do not need to override colors** — the default palette is decoded from a standard SRS. Override only when matching a specific brand.

## Optional conventions

- **AI prompt limit** (`Max_N_char` for AI input fields) — declare only if the system has AI features; default `4000`
- **Additional Loại/Thuộc tính values** — if the domain needs a new component type, add it to the canonical Legend (`LEGEND_TYPES` / `LEGEND_ATTRS` in `scripts/v1/srs_format.py`) before use; do **not** invent it ad hoc in the `.md`

## Checklist (for the skill agent)

When loading a project's conventions file for the first time:

- [ ] Project name determined (from the `.md` or the conventions file)
- [ ] Logo: use the project file or the default?
- [ ] Version + date + prepared-by present
- [ ] Any brand color override?
- [ ] Does the system have AI features → does the prompt limit need declaring?

If any required item is unclear and not optional → **ask the user** before generating the document.
