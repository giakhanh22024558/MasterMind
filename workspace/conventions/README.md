# conventions/

Project-level **overrides** for MasterMind skill defaults.

Each `<skill>-conventions.md` file corresponds to one skill that has `conventions-defaults`. Leave it empty to use the defaults; fill in a `yaml` block or a table to override.

## Files in this folder

| File | Overrides defaults of skill |
|---|---|
| `features-conventions.md` | [`document/features`](../MasterMind/models/model_001/document/features/) (ID format, Priority levels, AC writing format) |
| `analysis-conventions.md` | [`document/analysis`](../MasterMind/models/model_001/document/analysis/) (Gap Type / Priority / Decision dropdowns) |
| `jira-conventions.md` | [`integration/jira`](../MasterMind/models/model_001/integration/jira/) (tag system, sub-task roles, mode) |

## Add a new file when needed

When using another skill that has conventions (e.g. `srs`, `erd`), create the matching `<skill>-conventions.md` file.

## Pattern (per skill)

```yaml
# Example: features-conventions.md
id_formats:
  epic:  "EPIC-{n:03d}"      # default uses 2 digits → override to 3 digits
  story: "US-{n:04d}"        # default STORY-NNN → override to US-NNNN

priority_values:
  - Critical
  - Important
  - Standard
  - Backlog

ac_writing:
  format: en      # vi (default) | en
```

The skill reads this file and merges it with the defaults — convention wins on conflict.

## Anti-patterns

- ❌ Editing the defaults inside the `MasterMind/` repo — not sustainable; use a project-level convention instead
- ❌ Inlining conventions inside individual artifact files — keep them centralized in `conventions/` for consistency
- ❌ Forking MasterMind to customize — always override via conventions
