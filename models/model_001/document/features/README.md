# features — README

A skill that derives a **feature backlog** from a requirements table, organized as **Epic → Feature → User Story**.

## Quick start

| If you want to… | Read |
|---|---|
| Understand the skill in one page | [`SKILL.md`](SKILL.md) |
| Know the table structure | [`feature-list/`](feature-list/) |
| Know what a project declares | [`conventions-schema/`](conventions-schema/) |
| See a worked example | [`examples/`](examples/) |

## The artifact

| Form | Where |
|---|---|
| Feature list `.md` (Epic → Feature → User Story; one row per story) — source of truth | `context/` |
| `features.xlsx` — manual pilot copy, with dropdowns + checkboxes | `output/` |

## The hierarchy

`EPIC-xxxx` → `FEAT-xxxx` → `US-xxxx` — every level coded for exact traceability.

## Columns

`Epic ID` · `Epic Name` · `Feature ID` · `Feature Name` · `Ref. Req (Feature)` · `Description (Feature)` · `Story ID` · `User Story` · `Ref. Req (Story)` · `Description (Story)` · `Priority` · `Ready?` · `Done?` · `In Scope`

## Stack

- **Markdown** for the `.md` context table
- **Python** (`openpyxl`) for the `.xlsx` — rendered by the pipeline's `ba_md_to_xlsx.py`

## License

Internal. Adapt freely. No warranty.
