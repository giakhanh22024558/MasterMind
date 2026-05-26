# Gap Analysis — Change Requests

> Backed by skill [`document/analysis`](../MasterMind/models/model_001/document/analysis/).
> Gộp Gap + Impact Analysis vào 1 bảng 17 cột.

**Trigger:** project có SRS, khách gửi CR → chạy gap → impact → approval → sync vào backlog → Jira

| CR ID | Topic | Criteria | Description | As-Is | To-Be | Impl·BA | Impl·FE | Impl·BE | Est BA | Est FE | Est BE | Impacted Module | Gap Type | Priority | Decision | Client Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CR-01 |  |  |  |  |  | • |  |  |  |  |  |  |  | P0 |  |  |

## Dropdown values (default)

- **Gap Type**: `Modification` / `Enhancement` / `Missing` / `Missing (New Feature)` / `Behavior Change` / `No Change`
- **Priority**: `P0` (critical) / `P1` (important) / `P2` (nice-to-have)
- **Decision**: `This Sprint` / `Next Sprint` / `Another Sprint` / `Invalid / Out-of-scope`

Override trong `conventions/analysis-conventions.md`.

## Workflow

1. Drop CR list vào `input/` (xlsx, docx, hoặc text)
2. Agent đọc → fill As-Is (từ SRS context) + To-Be (từ CR content)
3. BA fill Impl per role (BA/FE/BE) + Est per role
4. Manager/PO chốt Decision
5. CR có `Decision ∈ {This Sprint, Next Sprint}` → sync thành Story vào `backlog.md` với prefix `[CR-XX]`
6. Push Jira: skill [`integration/jira`](../MasterMind/models/model_001/integration/jira/) → `output/jira/`

## Render lên xlsx

Skill `analysis` có script render md → xlsx (header 2 tầng, dropdown, dòng TỔNG): xem `analysis/scripts/`.

## Sync với Google Sheet (optional)

Nếu project dùng Sheet làm working tool: skill [`integration/google_sheets`](../MasterMind/models/model_001/integration/google_sheets/) → CRUD cell-level, giữ comment/history.
