# ERD · conventions defaults

Defaults applied when `<project-root>/diagram-conventions.md` does not specify an ERD value. A project may override any of these.

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../../core/meta/conventions-as-data-pattern/).)

## Defaults

| Item | Default |
|---|---|
| Entity name style | `UPPER_SNAKE_CASE`, singular (`USER`, `BILLING_PLAN`) |
| Relationship label | Short verb phrase, read source → target (`"has"`, `"issued for"`) |
| Cardinality notation | Crow's-foot |
| Authoring form | Mermaid `erDiagram` inside a `.md` context file |
| `.drawio` render | Produced only on explicit request, written to `output/erd.drawio` |

## When defaults apply

Each item the project does not declare takes the value here. The skill **acknowledges the source** when explaining a choice ("per project conventions" / "using default").
