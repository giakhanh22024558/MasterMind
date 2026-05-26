# Gap Analysis — Change Requests

> Backed by skill [`document/analysis`](../MasterMind/models/model_001/document/analysis/).
> Merges Gap + Impact Analysis into one 17-column table.

**Trigger:** project has an SRS, a client sends in a CR → run gap → impact → approval → sync into backlog → Jira

| CR ID | Topic | Criteria | Description | As-Is | To-Be | Impl·BA | Impl·FE | Impl·BE | Est BA | Est FE | Est BE | Impacted Module | Gap Type | Priority | Decision | Client Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CR-01 |  |  |  |  |  | • |  |  |  |  |  |  |  | P0 |  |  |

## Dropdown values (default)

- **Gap Type**: `Modification` / `Enhancement` / `Missing` / `Missing (New Feature)` / `Behavior Change` / `No Change`
- **Priority**: `P0` (critical) / `P1` (important) / `P2` (nice-to-have)
- **Decision**: `This Sprint` / `Next Sprint` / `Another Sprint` / `Invalid / Out-of-scope`

Override in `conventions/analysis-conventions.md`.

## Workflow

1. Drop the CR list into `input/` (xlsx, docx, or text)
2. Agent reads it → fills As-Is (from SRS context) + To-Be (from CR content)
3. BA fills Impl per role (BA/FE/BE) + Est per role
4. Manager/PO locks in the Decision
5. CRs with `Decision ∈ {This Sprint, Next Sprint}` → sync as Stories into `backlog.md` with the `[CR-XX]` prefix
6. Push to Jira: skill [`integration/jira`](../MasterMind/models/model_001/integration/jira/) → `output/jira/`

## Render to xlsx

The `analysis` skill has a script that renders md → xlsx (two-tier header, dropdowns, totals row): see `analysis/scripts/`.

## Sync with Google Sheets (optional)

If the project uses Sheets as the working tool: skill [`integration/google_sheets`](../MasterMind/models/model_001/integration/google_sheets/) → cell-level CRUD that preserves comments/history.
