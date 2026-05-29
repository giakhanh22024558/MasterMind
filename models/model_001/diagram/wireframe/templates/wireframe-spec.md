# WF-NN — <Screen name> · Component spec & assumptions

> Companion doc for `WF-NN-<slug>.html` (same folder, same base name).
> Source: <STORY-xxx / CR / SRS figure / legacy doc>. Screen type: <full-page redirect | pop-up | list | detail>. Path: `<breadcrumb>`.
>
> The dev team builds against the assumptions below — no client pre-approval required. Client flags anything that should differ → recorded as a change on the relevant US.

## Component specification

Group components by on-screen section (A, B, C…). One table per section. Columns are the SRS component-spec set:

### A. <Section name>

| No./ID | Name / Label | Type | Attribute | Description |
|---|---|---|---|---|
| A1 | <label> | <Button / Text input / Number input / Dropdown (single) / Date input / Text area / Icon button / Number (computed) / Display> | <Required · Read-only · Disabled · Auto · Computed · Conditional · Default: x · > 0 · …> | <behavior; cross-ref an assumption with "(Assumption n.)" when relevant> |

*(Add B, C, … sections. If the screen has status-based locking or other conditional behavior, add a small "Status-based locking" / "Conditional behavior" table.)*

## Design Assumptions

Plain list — no status column (dev builds against these; client feedback → change on the relevant US). Mark the least-certain rows with *(please flag if different)*. Mirror to the project assumptions tracker (`A-WFNN-nn`).

| # | Assumption |
|---|---|
| 1 | <assumption — matches badge ① on the HTML> |
| 2 | <…> |

## Linked artifacts

- User story: <STORY-xxx> in `docs/backlog.md`
- Q&A / assumptions: `output/<project>-SRS-QA.xlsx` (sheet `WF Assumptions`)
- Change tracker: `docs/wireframe-changes.md`
