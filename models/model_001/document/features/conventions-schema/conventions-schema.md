# features · conventions schema

What a project declares when using this skill. Filled into `<project-root>/features-conventions.md`; unspecified items fall back to [`conventions-defaults/`](../conventions-defaults/).

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../../core/meta/conventions-as-data-pattern/).)

## Conventions

| Item | Format | Default | Notes |
|---|---|---|---|
| Feature code prefix | Text + `-` + digits | `FEAT-` (4 digits) | Sequential, never reused |
| Priority values | Ordered list | `Low`, `Medium`, `High`, `Very high` | The `Priority` dropdown |
| **In Scope values** | List (project-specific) | `In scope`, `Out of scope`, `Next phase`, `Undecided` | The `In Scope` selection list — **projects usually override this** to match their delivery phases |
| Feature list pilot file name | File name | `features.xlsx` | Written to `output/` |

## Checklist (for the skill agent)

- [ ] Is the `In Scope` value list declared? (This is the one most projects customize.)
- [ ] Are the `Priority` values the default four, or overridden?
- [ ] Is the `FEAT-` prefix default, or overridden?

If a required item is unclear, **ask the user** before producing the feature list.
