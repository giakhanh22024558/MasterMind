# ERD · conventions schema

What a project should declare for ERD work. A project fills these into `<project-root>/diagram-conventions.md`; unspecified items fall back to [`conventions-defaults/`](../conventions-defaults/).

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../../core/meta/conventions-as-data-pattern/).)

## Conventions

| Item | Format | Default | Notes |
|---|---|---|---|
| Entity name style | Casing rule | `UPPER_SNAKE_CASE`, singular | e.g. `BILLING_PLAN` |
| Relationship label style | Text rule | short verb phrase, read source → target | e.g. `"issued for"` |
| Cardinality notation | Enum | crow's-foot | The skill assumes crow's-foot; do not mix notations |
| ERD render file name | File name | `erd.drawio` | The `.drawio` written to `output/` on request |

## Checklist (for the skill agent)

- [ ] Is the entity-name casing the default, or overridden?
- [ ] Does the project keep one ERD or several views?
- [ ] Has the user asked for a `.drawio` render, or is Mermaid `.md` sufficient?
