# Pattern · CR → Jira Task

Luồng convert 1 Change Request thành Jira issue tree. **Đây là một trong nhiều source** — xem [`story-to-task.md`](story-to-task.md) cho luồng tổng quát (planned story / bug / refactor cũng cùng schema).

Phần đặc biệt của CR-derived: tự động prepend `[CR-XX]` tag và pull As-Is / To-Be / Impl per-role / Est per-role từ Gap Analysis.

## Inputs (3 sources)

| Source | File | Cột dùng |
|---|---|---|
| **Gap Analysis** | `output/Gap_Analysis.xlsx` | CR ID · Description · Criteria · As-Is · To-Be · Gap Type · Priority · Decision · Client Note · Impacted Module |
| **Gap Analysis** (Impact phần) | (cùng file, cùng row) | Impl·BA · Impl·FE · Impl·BE · Est BA · Est FE · Est BE |
| **Backlog** | `output/LEX Features list.xlsx` sheet `Backlog` | Story ID (story có prefix `[CR-XX]` để map về CR) |
| **AC** | `output/LEX Features list.xlsx` sheet `Acceptance Criteria` | Story ID · AC ID · Tiêu chí (text) |

## Filter input

Chỉ tạo Jira task cho CR có:

- `Decision ∈ { This Sprint, Next Sprint }` *(skip `Another Sprint` và `Invalid / Out-of-scope`)*
- CR phải đã được sync vào backlog thành story `[CR-XX] …` *(nếu chưa có, raise warning)*

## Workflow

```
       Gap_Analysis.xlsx                LEX Features list.xlsx
              │                                   │
              ▼                                   ▼
    ┌─────────────────┐                ┌───────────────────┐
    │ for each CR     │                │ map CR-XX → STORY │
    │   if Decision   │                │   theo prefix     │
    │   ∈ {This,Next} │                │   [CR-XX] in name │
    └────────┬────────┘                └─────────┬─────────┘
             │                                   │
             └──────────────┬────────────────────┘
                            ▼
                ┌───────────────────────┐
                │ build main task       │
                │   title = [CR-XX] …   │
                │   desc  = context+AC  │
                └───────────┬───────────┘
                            ▼
                ┌───────────────────────┐
                │ build 3 sub-task      │
                │   [BA] / [FE] / [BE]  │
                │   desc = role bullets │
                └───────────┬───────────┘
                            ▼
              output/jira/cr-<XX>-task.{json,md}
```

## Step-by-step

1. **Load Gap_Analysis.xlsx** → dict `{CR-XX: { ...gap+impact fields... }}`
2. **Load Backlog** → tìm story có `name.startswith("[CR-XX]")` → lấy Story ID
3. **Load Acceptance Criteria sheet** → lấy list AC cho Story ID đó
4. Với mỗi CR có `Decision ∈ {This Sprint, Next Sprint}`:
   - **Resolve tag block**: `[FEAT-XXX] [CR-XX]` + custom tags từ `jira-conventions.md` (xem [tag system](../conventions-defaults/conventions-defaults.md#tag-system--tổng-quan))
     - Lookup `FEAT-XXX` từ story → Feature ID trong Backlog
     - `[CR-XX]` auto-prepend vì story name có prefix tương ứng
     - Skip `[FEAT-XXX]` nếu user tắt feature tag trong project conventions
   - **Main task title** = `<tag block> <Description> — <Criteria>`
   - **Main task desc** = template (context + AC table) — xem [`../task-structure/task-structure.md`](../task-structure/task-structure.md)
   - **3 sub-tasks** = `[BA]` `[FE]` `[BE]` với title cùng main + prefix role ở đầu, desc = bullets từ Impl·<role>, estimate = Est <role>
5. **Serialize** ra JSON (cho REST API) hoặc Markdown (cho UI paste)
6. **Lưu** `output/jira/cr-<XX>-task.json` / `.md`

## Edge cases

| Tình huống | Xử lý |
|---|---|
| CR không có story tương ứng trong backlog | Raise warning, skip CR đó (không tạo task) |
| Story có AC = 0 | Tạo main task nhưng bảng AC trống + cảnh báo |
| Role có Est = 0 | Vẫn tạo sub-task, description ghi `Không có công việc cho role này` |
| CR `Decision = Invalid / Out-of-scope` | Skip hoàn toàn |
| Story `Lifecycle = Done/Archived` | Skip — đã ship rồi, không tạo task mới |

## Sequencing trong BA pipeline

Skill này chạy **sau** change-request branch:

```
CR → gap → impact → user approval
  → features (story + AC) → erd/srs update
  → JIRA TASK CREATION (skill này)
```

Xem [`../../../business_analysis/SKILL.md`](../../../business_analysis/SKILL.md) cho pipeline đầy đủ.
