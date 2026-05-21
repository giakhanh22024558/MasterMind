# requirements · conventions defaults

Defaults applied when `<project-root>/requirements-conventions.md` does not specify a value. A project may override any of these.

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../../core/meta/conventions-as-data-pattern/).)

## Defaults

| Item | Default |
|---|---|
| Requirement code | `REQ-` + 4 digits, sequential from `REQ-0001`, never reused |
| Ref. Docs citation style | `<doc name> §<section> "<heading>"` — e.g. `Vendor SRS §3.1 "Sign in"`. With no sections, cite the document name plus a locating phrase. |
| Requirements pilot file | `output/requirements.xlsx` |

## When defaults apply

Each item the project does not declare takes the value here. The skill **acknowledges the source** when explaining a choice ("per project conventions" / "using default").
