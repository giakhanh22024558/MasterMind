# business_analysis · conventions defaults

Defaults applied when `<project-root>/business_analysis-conventions.md` does not specify a value. A project may override any of these.

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../core/meta/conventions-as-data-pattern/).)

## Codes

| Item | Default |
|---|---|
| Requirement code | `REQ-` + 4 digits, sequential from `REQ-0001` |
| Feature code | `FEAT-` + 4 digits, sequential from `FEAT-0001` |

Codes are **globally sequential and never reused** — a retired requirement keeps its code so traceability holds.

## Priority values (feature list)

Ordered, lowest → highest:

`Low` · `Medium` · `High` · `Very high`

## In Scope values (feature list)

Default selection list:

`In scope` · `Out of scope` · `Next phase` · `Undecided`

> Most projects override this — the In Scope list is meant to match the project's actual delivery phases or scope buckets.

## Ref. Docs citation style

`<doc name> §<section> "<heading>"` — e.g. `Vendor SRS §3.1 "Sign in"`. When the source has no sections, cite the document name plus a locating phrase (e.g. `Kickoff notes, "Billing" topic`).

## Checkbox display (feature list `.xlsx`)

`Ready?` and `Done?` render as a two-value dropdown: `☐` (default) and `☑`.

## Output file names

| Artifact | File in `output/` |
|---|---|
| Requirements pilot | `requirements.xlsx` |
| Feature list pilot | `features.xlsx` |
| ERD render (on request) | `erd.drawio` |

## When defaults apply

Each item the project does not declare in `business_analysis-conventions.md` takes the value here. The skill **acknowledges the source** when explaining a choice:

- "Per the project's `business_analysis-conventions.md`, used X"
- "The project didn't specify Y, used the default from `conventions-defaults/`"
