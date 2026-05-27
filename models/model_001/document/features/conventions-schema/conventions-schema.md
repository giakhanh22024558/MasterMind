# features · conventions schema

What a project declares when using this skill. Filled into `<project-root>/features-conventions.md`; unspecified items fall back to [`conventions-defaults/`](../conventions-defaults/).

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../../core/meta/conventions-as-data-pattern/).)

## 🔒 NOT in the schema — locked layout

The following are **NOT configurable** — every project produces the same shape:

- Column count (always **9**)
- Column order (always: `Epic ID` · `Epic Name` · `Feature ID` · `Feature Name` · `Story ID` · `User Story` · `Priority` · `Status` · `Lifecycle`)
- Header strings (literal English; no translation)
- Row pattern (Epic row A+B / Feature row C+D / Story row E–I — no merged cells)

Anything outside this list — extra columns like `SRS Feature ID`, `AC count`, `Description`, `Ref. Req`, `Owner`, `Sprint`, etc. — is a **layout violation**, regardless of what the project requests. Put extra fields in a separate sheet keyed by `STORY-XXX`. See [`../feature-list/feature-list.md`](../feature-list/feature-list.md).

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
- [ ] **Re-check the canonical column set** — DO NOT add columns even if the project mentions extra fields; route those to a separate sheet.

If a required item is unclear, **ask the user** before producing the feature list. Never invent columns to "fit" extra data.
