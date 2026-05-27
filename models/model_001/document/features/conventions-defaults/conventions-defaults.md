# features · conventions defaults

Defaults applied when `<project-root>/features-conventions.md` does not specify a value. A project may override any of these (within the locked layout — see [`../feature-list/feature-list.md`](../feature-list/feature-list.md)).

(For the meta-pattern, see [`conventions-as-data-pattern`](../../../../../core/meta/conventions-as-data-pattern/).)

## 🔒 Locked (NOT overridable)

| Item | Locked value | Why |
|---|---|---|
| Column count | **9** | Every project produces the same shape |
| Column order | `Epic ID` · `Epic Name` · `Feature ID` · `Feature Name` · `Story ID` · `User Story` · `Priority` · `Status` · `Lifecycle` | Cross-project tooling expects this exact order |
| Header strings | Literal English headers above (no translation, no synonyms) | Scripts parse by header text |
| Row pattern | 3-row-type — Epic row (A+B) / Feature row (C+D) / Story row (E–I); no merged cells | Parsers classify rows by filled-column pattern |

See [`../feature-list/feature-list.md`](../feature-list/feature-list.md) for the full canonical-layout spec + anti-patterns.

## Overridable defaults

| Item | Default |
|---|---|
| Epic code | `EPIC-` + 2 digits, sequential from `EPIC-01`, never reused |
| Feature code | `FEAT-` + 3 digits, sequential from `FEAT-001`, never reused |
| User story code | `STORY-` + 3 digits, sequential from `STORY-001`, never reused |
| Priority dropdown values | `Very high` · `High` · `Medium` · `Low` (highest → lowest) |
| Status dropdown values | `Backlog` · `Ready` · `In Progress` · `In Review` · `Done` |
| Lifecycle dropdown values | `Active` · `Done` · `Archived` · `Superseded` |
| Header row background | `#1F4E79` (dark blue) + white bold text |
| Epic row background | `#7030A0` (purple) + white bold text |
| Feature row background | `#BDD7EE` (light blue) |
| Story row background | white (no fill) |
| Feature list pilot file | `output/<project>-Backlog.xlsx` |
| **`ac_writing.language`** | **`en`** — Acceptance Criteria written as `Given/When/Then`. Set to `vi` for the Vietnamese form `Khi/Nếu… thì…`. See [`ac-writing.md`](ac-writing.md). |

> A Vietnamese-language project should override `ac_writing.language: vi` explicitly. Color/dropdown overrides are project-specific but the column set stays locked.

## When defaults apply

Each item the project does not declare takes the value here. The skill **acknowledges the source** when explaining a choice ("per project conventions" / "using default").

## See also

- [`../feature-list/feature-list.md`](../feature-list/feature-list.md) — **the canonical layout** (locked column set + 3-row pattern + anti-patterns)
- [`ac-writing.md`](ac-writing.md) — Acceptance Criteria writing convention (separate AC sheet, formats: EN `Given/When/Then` · VI `Khi/Nếu… thì…`)
