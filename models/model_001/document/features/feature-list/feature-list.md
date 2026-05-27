# Feature list — canonical layout (LOCKED by default, project-extensible)

The feature backlog, organized as a three-level hierarchy: **Epic → Feature → User Story**, rendered as **one sheet with exactly 9 canonical columns** and **three row types**. Derived from the requirements table; consumed by every downstream skill (SRS, Jira, Google Sheets sync).

> 🔒 **The 9-column layout is the DEFAULT for every project.** Sessions MUST NOT silently add, remove, rename, reorder, or merge columns. Use the canonical layout unless the user **explicitly requests an extension**.
>
> ✅ **Escape hatch — explicit user request:** If the user explicitly asks to add extra columns (e.g. "thêm cột Sprint và Owner", "add an SRS Feature ID column"), the session **does it without arguing** — but scopes the change to the **current project only** (record it under `extra_columns` in `<project>/features-conventions.md`). The change does NOT propagate to other projects.
>
> 🌐 **Promoting to the model:** Only when the user explicitly says something like *"save this template to the model"* / *"lưu mẫu này vào model"* / *"update model_001 defaults"* does the session edit `MasterMind/models/model_001/...` to make the extension a new global default.

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

## Default-forbidden — silent inventions

The following are violations **when invented by the session without an explicit user request**. If the user explicitly asks for any of these, see the *Project extension* section below — do the extension for the current project, do not refuse.

- ❌ **Silently** adding columns like `SRS Feature ID`, `AC count`, `Ref. Req`, `Description`, `Ready?`, `Done?`, `In Scope`, `Owner`, `Sprint`, `Created`, `Updated` because they "seem useful"
- ❌ Reordering canonical columns (e.g. putting `Status` before `Priority`) — even with extensions, canonical order is preserved; extensions append at column J onwards
- ❌ Translating canonical headers (e.g. `Tên Epic` instead of `Epic Name`)
- ❌ Using Excel merge-cells on Epic Name / Feature Name to span story rows — use the 3-row-type pattern instead
- ❌ Putting Feature ID and Story ID in the same row (mashing the Feature row + first Story row together)
- ❌ Color/background as a primary classifier — color is **decoration only**; the row-filled pattern is the actual classifier (so a script reading the sheet can parse it without RGB inspection)
- ❌ Renaming canonical IDs (`STORY-` → `US-`, `Story ID` → `US ID`) — width override is fine via `id_formats`; the prefix and header text are canonical

## Project extension — when the user explicitly asks

When the user says *"add a column X"* / *"thêm cột Y"* / similar:

1. **Do it** — do not argue, do not refuse, do not redirect to "a separate sheet" unless the user themselves chose that option.
2. **Append** the new column at the right end (column J onwards) — never insert in the middle and never reorder the canonical 9.
3. **Record** the extension in `<project-root>/features-conventions.md` under an `extra_columns` block so future sessions of the same project keep it consistent:
   ```yaml
   extra_columns:
     - header: "SRS Feature ID"
       filled_on: feature       # epic | feature | story
       type: text               # text | dropdown | checkbox | date
       # values: [...]          # for dropdown
       notes: "Maps backlog feature to its SRS section anchor"
     - header: "AC count"
       filled_on: story
       type: number
       formula: "=COUNTIF('Acceptance Criteria'!A:A, E{row})"
   ```
4. **Mention** to the user that the change is **project-scoped only** and won't appear in other projects. If they want it everywhere, they can say *"save this to the model"* (see next section).

### Promoting an extension to the model

If the user explicitly says *"save this template to the model"* / *"lưu mẫu này vào model"* / *"update model_001 defaults"*:

1. Edit `MasterMind/models/model_001/document/features/feature-list/feature-list.md` — append the new column to the canonical column set, bumping the canonical count from 9 to 10 (etc.).
2. Update `MasterMind/models/model_001/document/features/conventions-defaults/conventions-defaults.md` to reflect the new default.
3. Update `MasterMind/models/model_001/setup/templates/docs/backlog.md` so future `/set-up` runs use the new layout.
4. Commit to MasterMind with a clear message.

Do steps 1–4 only after explicit promotion intent. **Don't promote based on a single project's needs unless the user asks for it.**

### When to suggest a separate sheet instead

You may *suggest* (not enforce) routing extra fields to a separate sheet keyed by `STORY-XXX`/`FEAT-XXX` when:

- The new data has many values per story (e.g. acceptance criteria, test runs, history entries)
- The new data has its own lifecycle (e.g. QA test status that gets edited independently)
- Adding it as a backlog column would create many empty cells (e.g. a `BR ref` that only applies to a few stories)

If the user agrees, route there. If they still want it inline, add it as a project extension.

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

## Rules

**Non-negotiable** (always apply, even with extensions):

1. Every feature belongs to exactly one epic; every user story belongs to exactly one feature.
2. Codes are sequential, never reused, never hand-assigned.
3. Use only the project's declared dropdown values for Priority / Status / Lifecycle.
4. **Do not merge cells.** The 3-row-type pattern is the layout — no Excel merge across rows.
5. The canonical 9 columns appear in their fixed order at positions A–I.

**Default behavior** (overridable on explicit user request):

6. **Do not silently invent columns.** Default produces only the canonical 9.
7. On explicit user request, append extra columns at column J onwards and record them in `<project>/features-conventions.md` → `extra_columns`. Scoped to that project unless the user asks to promote to the model.

## Cross-references

- [`../conventions-defaults/conventions-defaults.md`](../conventions-defaults/conventions-defaults.md) — defaults including color hex codes
- [`../conventions-defaults/ac-writing.md`](../conventions-defaults/ac-writing.md) — Acceptance Criteria sheet (separate sheet, 5 columns)
- [`../../../integration/google_sheets/examples/lex-walkthrough.md`](../../../integration/google_sheets/examples/lex-walkthrough.md) — canonical worked example
- [`../../../integration/google_sheets/patterns/hierarchical-row-types.md`](../../../integration/google_sheets/patterns/hierarchical-row-types.md) — row classifier code template
