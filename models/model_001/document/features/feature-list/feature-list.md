# Feature list — canonical layout (LOCKED)

The feature backlog, organized as a three-level hierarchy: **Epic → Feature → User Story**, rendered as **one sheet with exactly 9 columns** and **three row types**. Derived from the requirements table; consumed by every downstream skill (SRS, Jira, Google Sheets sync).

> 🔒 **This layout is LOCKED.** Every project using model_001 produces the same 9 columns in the same order. Sessions MUST NOT add, remove, rename, reorder, or merge columns. Project-level convention overrides allowed values only (priorities, status labels, ID prefix widths) — never the column set or the row pattern.

## The hierarchy

| Level | What it is | Code |
|---|---|---|
| **Epic** | A large area of capability — groups related features. | `EPIC-XX` |
| **Feature** | A deliverable capability within an epic, justified by ≥ 1 requirement. | `FEAT-XXX` |
| **User Story** | An INVEST-style story within a feature, short form `[User] can [Action]`. | `STORY-XXX` |

Every level carries a sequential code, globally unique, never reused, **auto-generated**. Width of the numeric suffix (`2 / 3 / 4` digits) is the only ID format an override can change.

## Canonical column set — exactly 9 columns, in this order

| # | Column header (literal) | Filled on | Type / dropdown values |
|---|---|---|---|
| A | `Epic ID` | **Epic row only** | text — `EPIC-XX` |
| B | `Epic Name` | **Epic row only** | text |
| C | `Feature ID` | **Feature row only** | text — `FEAT-XXX` |
| D | `Feature Name` | **Feature row only** | text |
| E | `Story ID` | **Story row only** | text — `STORY-XXX` |
| F | `User Story` | **Story row only** | text — `[User] can [Action]` |
| G | `Priority` | **Story row only** | dropdown — defaults: `Very high` / `High` / `Medium` / `Low` |
| H | `Status` | **Story row only** | dropdown — defaults: `Backlog` / `Ready` / `In Progress` / `In Review` / `Done` |
| I | `Lifecycle` | **Story row only** | dropdown — defaults: `Active` / `Done` / `Archived` / `Superseded` |

Header row is row 1. Headers above are the **literal strings** that must appear — no synonyms, no translations.

## Row pattern — three row types, NO merged cells

The hierarchy is encoded by **which columns are filled in each row**, NOT by Excel-merged cells. Cells outside a row's "filled" set stay **empty** (no merge, no repeat).

```
| A         | B                  | C        | D                  | E         | F                  | G        | H        | I         |
| Epic ID   | Epic Name          | Feat. ID | Feature Name       | Story ID  | User Story         | Priority | Status   | Lifecycle |
|-----------|--------------------|----------|--------------------|-----------|--------------------|----------|----------|-----------|
| EPIC-01   | Case Management    |          |                    |           |                    |          |          |           | ← Epic row
|           |                    | FEAT-001 | Browse & search    |           |                    |          |          |           | ← Feature row
|           |                    |          |                    | STORY-001 | A staff can list…  | High     | Backlog  | Active    | ← Story row
|           |                    |          |                    | STORY-002 | A staff can sort…  | High     | Ready    | Active    | ← Story row
|           |                    | FEAT-002 | Create & edit      |           |                    |          |          |           | ← Feature row
|           |                    |          |                    | STORY-007 | A staff can…       | Medium   | Backlog  | Active    | ← Story row
| EPIC-02   | …                  |          |                    |           |                    |          |          |           |
```

**Row classification rule** (a session MUST be able to derive this from any row):

| Filled columns | Row type |
|---|---|
| A + B (and C empty) | **Epic** |
| C + D | **Feature** |
| E starts with `STORY-` | **Story** |
| anything else | spacer / ignore |

## Forbidden — common deviations sessions invent

These have been observed in past sessions and are **all violations**:

- ❌ Adding an `Epic Name` column whose value is **merged/repeated** across every feature row of the epic (instead of one Epic row with everything else blank)
- ❌ Adding extra columns like `SRS Feature ID`, `AC count`, `Ref. Req`, `Description`, `Ready?`, `Done?`, `In Scope`, `Owner`, `Sprint`, `Created`, `Updated` — **NONE** belong in this sheet. Keep AC in the separate AC sheet (see `ac-writing.md`), SRS refs in the SRS document, owner/sprint in Jira.
- ❌ Reordering columns (e.g. putting `Status` before `Priority`)
- ❌ Translating headers (e.g. `Tên Epic` instead of `Epic Name`)
- ❌ Using Excel merge-cells on Epic Name / Feature Name to span story rows — use the 3-row-type pattern instead
- ❌ Putting Feature ID and Story ID in the same row (mashing the Feature row + first Story row together)
- ❌ Color/background as a primary classifier — color is **decoration only**; the row-filled pattern is the actual classifier (so a script reading the sheet can parse it without RGB inspection)
- ❌ Renaming `STORY-` to `US-`, `Story ID` to `US ID`, etc.

If a project genuinely needs extra fields, put them in a **separate sheet** keyed by `STORY-XXX` (see how `Acceptance Criteria` sheet is structured) — never inflate the Backlog sheet.

## Allowed project overrides (via `<project>/features-conventions.md`)

Only these are project-configurable:

| Override key | What it changes | Default |
|---|---|---|
| `id_formats.epic` | Width of `EPIC-NN` suffix | `EPIC-{n:02d}` |
| `id_formats.feature` | Width of `FEAT-NNN` suffix | `FEAT-{n:03d}` |
| `id_formats.story` | Width of `STORY-NNN` suffix | `STORY-{n:03d}` |
| `priority_values` | Values in Priority dropdown | `Very high` / `High` / `Medium` / `Low` |
| `status_values` | Values in Status dropdown | `Backlog` / `Ready` / `In Progress` / `In Review` / `Done` |
| `lifecycle_values` | Values in Lifecycle dropdown | `Active` / `Done` / `Archived` / `Superseded` |
| `sheet_layout.*_color` | Background color for Epic / Feature / header rows | see [`conventions-defaults.md`](../conventions-defaults/conventions-defaults.md) |

**NOT overridable:** column count, column order, header strings, row pattern.

## Color convention (decoration, not classifier)

| Row type | Default background | Notes |
|---|---|---|
| Header (row 1) | `#1F4E79` (dark blue) + white bold text | Sticky / frozen |
| Epic row | `#7030A0` (purple) + white bold text | Spans only columns A+B; C–I stay white |
| Feature row | `#BDD7EE` (light blue) | Spans only columns C+D; others white |
| Story row | white (no fill) | |

Color is for human visual scan only. **All parsers/scripts MUST classify by the row-filled rule above**, not by RGB.

## Traceability — by code, not by column

Cross-artifact links happen by code reference inside other artifacts:

```
REQ-XXXX  ──cited in──▶  FEAT-XXX in SRS use-case spec
STORY-XXX ──cited in──▶  AC-{n}-NN  in Acceptance Criteria sheet
STORY-XXX ──cited in──▶  Jira issue title  via [STORY-XXX] prefix
CR-XX     ──cited in──▶  STORY-XXX name with [CR-XX] prefix
```

There is **no `Ref. Req` column** in this sheet because traceability lives in the referencing artifacts.

## File form

- **Source of truth:** the live sheet (Google Sheets via `integration/google_sheets` skill, or local `.xlsx`).
- **`.md` mirror:** a sidecar in `context/backlog.md` that mirrors the sheet using the same 9-column markdown table. Used for cheap reading; never the source of truth.
- **`.xlsx` export:** generated by `business_analysis/scripts/ba_md_to_xlsx.py` if needed for delivery — must reproduce the same 9 columns with the dropdowns + colors above.

## Rules — non-negotiable

1. Every feature belongs to exactly one epic; every user story belongs to exactly one feature.
2. Codes are sequential, never reused, never hand-assigned.
3. Use only the project's declared dropdown values for Priority / Status / Lifecycle.
4. **Do not invent columns.** If the requirement does not fit one of the 9 canonical columns, put it in a separate sheet (AC sheet, Gap Analysis sheet, etc.) keyed by `STORY-XXX` or `FEAT-XXX`.
5. **Do not merge cells.** The 3-row-type pattern is the layout — no Excel merge.

## Cross-references

- [`../conventions-defaults/conventions-defaults.md`](../conventions-defaults/conventions-defaults.md) — defaults including color hex codes
- [`../conventions-defaults/ac-writing.md`](../conventions-defaults/ac-writing.md) — Acceptance Criteria sheet (separate sheet, 5 columns)
- [`../../../integration/google_sheets/examples/lex-walkthrough.md`](../../../integration/google_sheets/examples/lex-walkthrough.md) — canonical worked example
- [`../../../integration/google_sheets/patterns/hierarchical-row-types.md`](../../../integration/google_sheets/patterns/hierarchical-row-types.md) — row classifier code template
