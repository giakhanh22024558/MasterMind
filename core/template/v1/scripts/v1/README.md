# <skill-name> · scripts

Helper scripts for this skill — atomic edits, calculations, scaffolding, etc.

## Available scripts

| Script | Purpose |
|---|---|
| (Add your first script here, OR delete this row if no scripts needed) | (one line) |

## When this skill needs scripts

Scripts are appropriate when the skill manipulates:

- Sync-prone files (cloud-synced .drawio, .docx, .xlsx) — use [atomic edits pattern](../../../../meta/atomic-edits-pattern/)
- Repeatable structural operations (refactoring, batch updates)
- Calculations that humans shouldn't do by hand (layouts, lookups)

If this skill is **pure narrative** (no file manipulation), this folder MUST still exist (per the uniform structure) but can contain only this README explaining "no scripts required".

## How to add a new script

1. Create `<verb>-<noun>.py` (e.g. `scaffold-stakeholder-list.py`)
2. Include a docstring explaining purpose · use case · why atomic if applicable
3. CONFIG block at top with placeholders the user fills in
4. Update this README to list the new script

See [`meta/atomic-edits-pattern/`](../../../../meta/atomic-edits-pattern/) for the atomic-edit pattern when applicable.
