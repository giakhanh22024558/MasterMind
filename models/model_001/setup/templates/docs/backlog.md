# Backlog

> Backed by skill [`document/features`](../MasterMind/models/model_001/document/features/).
> 3 cấp hierarchy: **Epic → Feature → User Story**, mỗi Story kèm Acceptance Criteria (AC).

**ID format:** `EPIC-XX`, `FEAT-XXX`, `STORY-XXX`, `AC-{storyNum}-NN`
**AC format:** `Khi/Nếu… thì…` (tiếng Việt) hoặc `Given/When/Then` (tiếng Anh) — xem [features/conventions-defaults/ac-writing.md](../MasterMind/models/model_001/document/features/conventions-defaults/ac-writing.md)
**Status:** `Backlog / Ready / In Progress / In Review / Done`
**Lifecycle:** `Active / Done / Archived / Superseded`

---

## EPIC-01 — `<Epic name>`

### FEAT-001 — `<Feature name>`

#### STORY-001 — `<User story name>`
*Priority: `<High>` · Status: `Backlog` · Lifecycle: `Active`*

- **AC-001-01**: ☐ `<Khi/Nếu… thì…>`
- **AC-001-02**: ☐ `<Khi/Nếu… thì…>`

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

1. Source: `docs/requirements.md` (skill `features` đọc và derive)
2. Hoặc: drop CR vào `input/` → skill `analysis` → approved CRs → add stories vào đây với prefix `[CR-XX]`
3. Render sang xlsx: `document/features/scripts/...` (deliverable vào `output/`)
4. Hoặc edit live trên Google Sheet: skill `integration/google_sheets` (CRUD cell-level)

## Anti-patterns

- ❌ Story name chứa cả tag `[CR-XX]` ngoài và trong format chuẩn — pick một
- ❌ AC dài hơn 1 dòng — tách thành nhiều AC, mỗi cái 1 điều kiện
- ❌ AC mô tả implementation (DB, API) — chỉ behavior observable
