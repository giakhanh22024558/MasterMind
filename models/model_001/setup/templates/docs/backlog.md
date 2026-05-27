# Backlog

> Backed by skill [`document/features`](../MasterMind/models/model_001/document/features/).
> 3-level hierarchy: **Epic → Feature → User Story**, with Acceptance Criteria (AC) in a **separate sheet** (`Acceptance Criteria`).

## 🔒 Canonical layout — 9 columns, 3 row types (LOCKED)

The skill enforces ONE canonical layout across every project. **Do not add columns, do not merge cells, do not translate headers.** Extra fields go in a separate sheet keyed by `STORY-XXX`. See [`feature-list.md`](../MasterMind/models/model_001/document/features/feature-list/feature-list.md) for full spec + anti-patterns.

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| `Epic ID` | `Epic Name` | `Feature ID` | `Feature Name` | `Story ID` | `User Story` | `Priority` | `Status` | `Lifecycle` |

| Row type | Filled columns | Notes |
|---|---|---|
| **Epic row** | A + B | C–I stay empty |
| **Feature row** | C + D | A, B, E–I stay empty |
| **Story row** | E + F + G + H + I | A–D stay empty |

**ID format:** `EPIC-XX`, `FEAT-XXX`, `STORY-XXX`, `AC-{storyNum}-NN`
**AC format:** `Given/When/Then` (English) or `Khi/Nếu… thì…` (Vietnamese) — pick one per project in `conventions/features-conventions.md` → `ac_writing.language`. See [ac-writing.md](../MasterMind/models/model_001/document/features/conventions-defaults/ac-writing.md)
**Status:** `Backlog / Ready / In Progress / In Review / Done`
**Lifecycle:** `Active / Done / Archived / Superseded`

## Markdown sidecar form

```markdown
| Epic ID | Epic Name | Feature ID | Feature Name | Story ID | User Story | Priority | Status | Lifecycle |
|---|---|---|---|---|---|---|---|---|
| EPIC-01 | Case Management |  |  |  |  |  |  |  |
|  |  | FEAT-001 | Browse & search |  |  |  |  |  |
|  |  |  |  | STORY-001 | A staff can list matters | High | Ready | Active |
|  |  |  |  | STORY-002 | A staff can sort matters by Updated Time | High | Backlog | Active |
|  |  | FEAT-002 | Create & edit |  |  |  |  |  |
|  |  |  |  | STORY-007 | A staff can create a matter | High | In Progress | Active |
| EPIC-02 | ... |  |  |  |  |  |  |  |
```

---

## Workflow

1. Source: `docs/requirements.md` (the `features` skill reads it and derives stories)
2. Alternative: drop a CR into `input/` → `analysis` skill → approved CRs → add stories here with the `[CR-XX]` prefix
3. Live edit: skill `integration/google_sheets` (cell-level CRUD that preserves dropdown chips + comments)
4. Render to xlsx mirror: `business_analysis/scripts/ba_md_to_xlsx.py` → `output/<project>-Backlog.xlsx`

## Anti-patterns (will be rejected by reviewers)

- ❌ Adding columns like `SRS Feature ID`, `AC count`, `Description`, `Ref. Req`, `Owner`, `Sprint`
- ❌ Merging Epic Name / Feature Name across story rows (use the 3-row-type pattern instead)
- ❌ Translating headers (`Tên Epic` instead of `Epic Name`)
- ❌ Reordering columns
- ❌ Story name contains both the `[CR-XX]` tag and the canonical format — pick one
- ❌ AC longer than one line — split into multiple ACs, one condition each
- ❌ AC describes implementation (DB, API) — only observable behavior is allowed
