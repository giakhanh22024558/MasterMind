# business_analysis · conventions schema

The checklist of conventions a project should declare when using this skill. A project fills these into `<project-root>/business_analysis-conventions.md`; anything left unspecified falls back to [`conventions-defaults/`](../conventions-defaults/).

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../core/meta/conventions-as-data-pattern/).)

## Conventions

| Item | Format | Default | Notes |
|---|---|---|---|
| Requirement code prefix | Text + `-` + digits | `REQ-` (4 digits) | Codes are sequential and never reused |
| Feature code prefix | Text + `-` + digits | `FEAT-` (4 digits) | Sequential and never reused |
| Priority values | Ordered list | `Low`, `Medium`, `High`, `Very high` | Used for the `Priority` dropdown in the feature list |
| **In Scope values** | List (project-specific) | `In scope`, `Out of scope`, `Next phase`, `Undecided` | The selection list for the feature list's `In Scope` column — **projects usually override this** |
| Ref. Docs citation style | Text rule | `<doc name> §<section> "<heading>"` | How a source is cited in the `Ref. Docs` column |
| Output file names | File names | `requirements.xlsx`, `features.xlsx`, `erd.drawio` | The pilot/render files written to `output/` |

## Checklist (for the skill agent)

When loading a project's conventions file for the first time:

- [ ] Is the `In Scope` value list declared? (This is the one most projects customize.)
- [ ] Are the `Priority` values the default four, or overridden?
- [ ] Are the `REQ-` / `FEAT-` prefixes default, or overridden?
- [ ] Is a citation style for `Ref. Docs` specified?

If a required item is unclear and not optional → **ask the user** before producing artifacts.
