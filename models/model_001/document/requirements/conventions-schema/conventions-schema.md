# requirements · conventions schema

What a project declares when using this skill. Filled into `<project-root>/requirements-conventions.md`; unspecified items fall back to [`conventions-defaults/`](../conventions-defaults/).

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../../core/meta/conventions-as-data-pattern/).)

## Conventions

| Item | Format | Default | Notes |
|---|---|---|---|
| Requirement code prefix | Text + `-` + digits | `REQ-` (4 digits) | Sequential, never reused |
| Ref. Docs citation style | Text rule | `<doc name> §<section> "<heading>"` | How a source is cited |
| Requirements pilot file name | File name | `requirements.xlsx` | Written to `output/` |

## Checklist (for the skill agent)

- [ ] Is the `REQ-` prefix the default, or overridden?
- [ ] Is a citation style for `Ref. Docs` specified?

If a required item is unclear, **ask the user** before producing the table.
