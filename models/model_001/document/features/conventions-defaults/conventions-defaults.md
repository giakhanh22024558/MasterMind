# features · conventions defaults

Defaults applied when `<project-root>/features-conventions.md` does not specify a value. A project may override any of these.

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../../core/meta/conventions-as-data-pattern/).)

## Defaults

| Item | Default |
|---|---|
| Epic code | `EPIC-` + 4 digits, sequential from `EPIC-0001`, never reused |
| Feature code | `FEAT-` + 4 digits, sequential from `FEAT-0001`, never reused |
| User story code | `US-` + 4 digits, sequential from `US-0001`, never reused |
| Priority values | `Low` · `Medium` · `High` · `Very high` (lowest → highest) |
| In Scope values | `In scope` · `Out of scope` · `Next phase` · `Undecided` |
| Checkbox display (`.xlsx`) | `Ready?` and `Done?` render as a two-value dropdown: `☐` (default) and `☑` |
| Feature list pilot file | `output/features.xlsx` |
| **`ac_writing.language`** | **`en`** — Acceptance Criteria written as `Given/When/Then`. Set to `vi` for the Vietnamese form `Khi/Nếu… thì…`. See [`ac-writing.md`](ac-writing.md). |

> Most projects override the **In Scope** list — it should match the project's actual delivery phases or scope buckets. A Vietnamese-language project should also override `ac_writing.language: vi` explicitly.

## When defaults apply

Each item the project does not declare takes the value here. The skill **acknowledges the source** when explaining a choice ("per project conventions" / "using default").

## See also

- [`ac-writing.md`](ac-writing.md) — Acceptance Criteria writing convention for each User Story (formats: EN `Given/When/Then` · VI `Khi/Nếu… thì…`, 6 principles, anti-patterns, sheet layout).
