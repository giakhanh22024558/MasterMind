# features · conventions schema

What a project declares when using this skill. Filled into `<project-root>/features-conventions.md`; unspecified items fall back to [`conventions-defaults/`](../conventions-defaults/).

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../../core/meta/conventions-as-data-pattern/).)

## 🔒 Default-locked — preserved unless the user explicitly extends

The following stay fixed across every project by default:

- The canonical 9 columns at positions A–I (`Epic ID` · `Epic Name` · `Feature ID` · `Feature Name` · `Story ID` · `User Story` · `Priority` · `Status` · `Lifecycle`)
- Column order of A–I
- Header strings (literal English; no translation)
- Row pattern (Epic row A+B / Feature row C+D / Story row E–I — no merged cells)

The session does **not** silently invent extra columns to "fit" project data.

### Project extension (per-project)

If the user explicitly asks for extra columns, append them at column J onwards and declare in this file:

```yaml
extra_columns:
  - header: "SRS Feature ID"
    filled_on: feature            # epic | feature | story
    type: text                    # text | dropdown | checkbox | date | number | formula
    notes: "Anchor to SRS section"
  - header: "AC count"
    filled_on: story
    type: formula
    formula: "=COUNTIF('Acceptance Criteria'!A:A, E{row})"
  - header: "Sprint"
    filled_on: story
    type: dropdown
    values: ["MVP-1", "MVP-2", "MVP-3", "Backlog"]
```

These extensions are **project-scoped** — they do NOT propagate to other projects.

### Promoting an extension to the model

Only when the user explicitly says *"save this to the model"* / *"lưu mẫu này vào model"*, the session edits `MasterMind/models/model_001/...` so future projects bootstrapped with `/set-up` include the new column as part of the canonical set. See [`../feature-list/feature-list.md`](../feature-list/feature-list.md) §"Promoting an extension to the model" for the exact files to update.

## Conventions (configurable)

| Item | Format | Default | Notes |
|---|---|---|---|
| Epic code prefix | Text + `-` + digits | `EPIC-` (2 digits) | Sequential, never reused |
| Feature code prefix | Text + `-` + digits | `FEAT-` (3 digits) | Sequential, never reused |
| User story code prefix | Text + `-` + digits | `STORY-` (3 digits) | Sequential, never reused |
| Priority values | Ordered list | `Very high`, `High`, `Medium`, `Low` | The `Priority` dropdown |
| Status values | Ordered list | `Backlog`, `Ready`, `In Progress`, `In Review`, `Done` | The `Status` dropdown |
| Lifecycle values | Ordered list | `Active`, `Done`, `Archived`, `Superseded` | The `Lifecycle` dropdown |
| AC writing language | `en` \| `vi` | `en` | Format of Acceptance Criteria in the AC sheet |
| Sheet color palette | Hex codes for header / epic / feature row backgrounds | see [`conventions-defaults.md`](../conventions-defaults/conventions-defaults.md) | Decoration only — parsers use row-filled pattern, not color |
| Feature list pilot file name | File name | `<project>-Backlog.xlsx` | Written to `output/` |

## Checklist (for the skill agent)

Before producing the backlog:

- [ ] Confirm `ac_writing.language` (en vs vi) — major impact on every AC row written
- [ ] Are the dropdown values (Priority / Status / Lifecycle) the defaults, or overridden?
- [ ] Are the `EPIC-` / `FEAT-` / `STORY-` prefix widths default, or overridden?
- [ ] Does the project have `extra_columns` declared? Reproduce them at column J onwards.
- [ ] **Did the user explicitly ask for new columns this session?** → add at column J+, record under `extra_columns`, tell the user it's project-scoped.
- [ ] **Did the user explicitly ask to "save to model" / "lưu mẫu này vào model"?** → only then edit `MasterMind/models/model_001/...`.

If a required item is unclear, **ask the user** before producing the feature list. Never silently invent columns to "fit" extra data — but never refuse if the user explicitly requests them.
