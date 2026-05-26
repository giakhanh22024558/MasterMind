# Backlog

> Backed by skill [`document/features`](../MasterMind/models/model_001/document/features/).
> 3-level hierarchy: **Epic → Feature → User Story**, with Acceptance Criteria (AC) attached to each Story.

**ID format:** `EPIC-XX`, `FEAT-XXX`, `STORY-XXX`, `AC-{storyNum}-NN`
**AC format:** `Given/When/Then` (English) or `Khi/Nếu… thì…` (Vietnamese) — see [features/conventions-defaults/ac-writing.md](../MasterMind/models/model_001/document/features/conventions-defaults/ac-writing.md)
**Status:** `Backlog / Ready / In Progress / In Review / Done`
**Lifecycle:** `Active / Done / Archived / Superseded`

---

## EPIC-01 — `<Epic name>`

### FEAT-001 — `<Feature name>`

#### STORY-001 — `<User story name>`
*Priority: `<High>` · Status: `Backlog` · Lifecycle: `Active`*

- **AC-001-01**: ☐ `<Given/When/Then>`
- **AC-001-02**: ☐ `<Given/When/Then>`

#### STORY-002 — `<User story name>`
*Priority: ... · Status: Backlog · Lifecycle: Active*

- **AC-002-01**: ☐ ...

### FEAT-002 — `<Feature name>`

#### STORY-003 — ...

---

## EPIC-02 — `<Epic name>`
...

---

## Workflow

1. Source: `docs/requirements.md` (the `features` skill reads it and derives stories)
2. Alternative: drop a CR into `input/` → `analysis` skill → approved CRs → add stories here with the `[CR-XX]` prefix
3. Render to xlsx: `document/features/scripts/...` (deliverable goes into `output/`)
4. Or edit live in Google Sheets: skill `integration/google_sheets` (cell-level CRUD)

## Anti-patterns

- ❌ Story name contains both the `[CR-XX]` tag and the canonical format — pick one
- ❌ AC longer than one line — split into multiple ACs, one condition each
- ❌ AC describes implementation (DB, API) — only observable behavior is allowed
