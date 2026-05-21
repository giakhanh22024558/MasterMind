# features · conventions defaults

Defaults applied when `<project-root>/features-conventions.md` does not specify a value. A project may override any of these.

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../../core/meta/conventions-as-data-pattern/).)

## Defaults

| Item | Default |
|---|---|
| Feature code | `FEAT-` + 4 digits, sequential from `FEAT-0001`, never reused |
| Priority values | `Low` · `Medium` · `High` · `Very high` (lowest → highest) |
| In Scope values | `In scope` · `Out of scope` · `Next phase` · `Undecided` |
| Checkbox display (`.xlsx`) | `Ready?` and `Done?` render as a two-value dropdown: `☐` (default) and `☑` |
| Feature list pilot file | `output/features.xlsx` |

> Most projects override the **In Scope** list — it is meant to match the project's actual delivery phases or scope buckets.

## When defaults apply

Each item the project does not declare takes the value here. The skill **acknowledges the source** when explaining a choice ("per project conventions" / "using default").
