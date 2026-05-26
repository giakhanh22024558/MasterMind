# Task structure — main + 3 sub-task

Cấu trúc bắt buộc cho mỗi CR khi push lên Jira.

## Main task (1 issue / CR)

| Field | Giá trị |
|---|---|
| **Issue type** | `Task` (hoặc `Story` nếu project conventions override) |
| **Title** | `[CR-XX] <Story title> — <scope CR>` |
| **Labels** | `cr-XX`, `from-gap-analysis`, scope topic (vd `quan-ly-vu-viec`) |
| **Priority** | Map từ CR Priority: `P0 → Highest`, `P1 → High`, `P2 → Medium` |
| **Estimate** (tổng) | `Est BA + Est FE + Est BE` man-hours |
| **Description** | Theo template bên dưới |

### Title — giải thích các thành phần

- `[CR-XX]` — mã CR từ Gap Analysis (vd `[CR-01]`)
- `<Story title>` — Description của CR (cột Description ở Gap Analysis); **không** dùng nguyên Story title trong Backlog vì đã có prefix `[CR-XX]` trùng
- `<scope CR>` — cột Criteria của Gap Analysis (vd `Dashboard — View mode`)

**Ví dụ:** `[CR-01] Bổ sung chế độ xem dạng danh sách bảng cho vụ việc — Dashboard — View mode`

### Description — template

```markdown
## Context

**As-Is:** <Current System Behavior từ Gap Analysis>

**To-Be:** <Client Expectation từ Gap Analysis>

**Client Note:** <Client Note cột Q của Gap_Analysis>

**Impacted Module:** <Impacted Module>

**Decision:** <Decision> · **Priority:** <P0/P1/P2>

## Acceptance Criteria

| AC ID | Tiêu chí | Test status |
|---|---|---|
| AC-XXX-01 | ☐ <AC content 1> | Not tested |
| AC-XXX-02 | ☐ <AC content 2> | Not tested |
| … | … | … |

> Mỗi AC = một điều kiện QA test pass/fail. Format `Khi/Nếu… thì…` (xem [features/conventions-defaults/ac-writing.md](../../../document/features/conventions-defaults/ac-writing.md))

## Implementation breakdown

Xem 3 sub-task: `[BA]`, `[FE]`, `[BE]`.

## Reference

- Backlog: `<Story ID>` (vd STORY-133)
- Gap Analysis: row CR-XX
```

## Sub-tasks (3 issue / CR — luôn đủ cả 3)

Mỗi sub-task:

| Field | Giá trị |
|---|---|
| **Issue type** | `Sub-task` |
| **Parent** | Main task |
| **Title** | `[<ROLE>] [CR-XX] <Story title> — <scope CR>` — **cùng title main task**, chỉ thêm prefix `[BA]`/`[FE]`/`[BE]` |
| **Assignee** | Để trống (PM gán sau) hoặc default theo role |
| **Estimate** | Est của role đó (man-hours) |
| **Description** | Bullet list công việc của role (lấy từ Impact Analysis cột Impl·BA/FE/BE) |

### Description sub-task — template

```markdown
## Công việc của <ROLE>

<bullet list từ Impact Analysis Impl·BA / Impl·FE / Impl·BE>

## Estimation

<X> man-hours

## Reference

- Main task: <parent issue key>
- AC liên quan: AC-XXX-01, AC-XXX-02, …
```

### Quy tắc về 3 sub-task

- **Luôn tạo đủ 3** — kể cả role có 0h work (description = `Không có`). Tránh role bị bỏ sót.
- Title sub-task **phải giống** title main task, chỉ khác prefix `[BA]/[FE]/[BE]`. Đừng paraphrase.
- Body sub-task **chỉ chứa** công việc của role đó — không nhồi context (đã có ở main task).

## Output file format

| File | Mục đích |
|---|---|
| `output/jira/cr-<XX>-task.json` | Payload cho Jira REST API `POST /rest/api/3/issue` (main) + `POST /rest/api/3/issue` (3 sub-tasks) |
| `output/jira/cr-<XX>-task.md` | Markdown để paste vào Jira UI (description hỗ trợ markdown) |
| `output/jira/all-tasks.csv` | (tuỳ chọn) Bulk CSV import cho nhiều CR cùng lúc |
