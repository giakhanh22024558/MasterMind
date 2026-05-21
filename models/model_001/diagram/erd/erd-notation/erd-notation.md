# ERD conventions

The Entity-Relationship Diagram models the system's **entities** and the **relationships** between them, so the team can later spot edge cases and business rules — and so the analyst can explain to the user how parts of the system affect one another.

## Notation — crow's foot

Relationships use **crow's-foot notation** for cardinality:

| Cardinality | Meaning |
|---|---|
| `||--||` | exactly one ↔ exactly one |
| `||--o{` | one ↔ zero-or-many |
| `||--|{` | one ↔ one-or-many |
| `}o--o{` | zero-or-many ↔ zero-or-many |

## Form — Mermaid in `.md` (default)

The ERD is authored as a **Mermaid `erDiagram`** inside a `.md` context file. Mermaid is the default because it is text — diffable, reviewable, and editable alongside the requirements.

```markdown
## ERD

\`\`\`mermaid
erDiagram
    ACCOUNT  ||--o{ INVOICE   : "issued for"
    ACCOUNT  ||--|{ USER      : "has"
    USER     ||--o{ REPORT    : "creates"
    INVOICE  }o--|| BILLING_PLAN : "priced by"
\`\`\`
```

### Conventions

- **Entity names** — `UPPER_SNAKE_CASE`, singular (`USER`, `BILLING_PLAN`).
- **Relationship labels** — a short verb phrase read source → target (`"issued for"`, `"has"`).
- List key **attributes** inside an entity block when they matter to a relationship or a business rule.
- Keep one ERD per system view; split into multiple `erDiagram` blocks if a single one becomes unreadable.

## Rendering to `.drawio`

Render the ERD to a `.drawio` file (in `output/`) **only when the user explicitly asks**. Until then, the Mermaid `.md` is the single representation. When a `.drawio` is produced, the Mermaid `.md` stays the source of truth — re-render, do not hand-edit the `.drawio` as the master.

## How the ERD is used afterward

- **Edge cases** — walk each relationship's cardinality (especially `zero-or-many`) to surface cases the requirements missed.
- **Business rules** — relationships and cardinalities expose rules to confirm with the user (e.g. "can an INVOICE exist without an ACCOUNT?").
- **Explaining impact** — use the ERD to show the user how a change to one entity ripples to connected entities.

## Rules

- The ERD is **derived from the requirements table** — every entity should trace to requirements.
- Do not invent entities the requirements do not support; if the ERD needs something new, raise it as a question (and likely a new requirement).
