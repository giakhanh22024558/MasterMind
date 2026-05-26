# Task structure — main + 3 sub-task

Cấu trúc bắt buộc cho mỗi task khi push lên Jira. Áp dụng cho **mọi nguồn** task (CR, planned story, bug, refactor, hotfix...).

## Main task (1 issue / task source)

| Field | Giá trị |
|---|---|
| **Issue type** | `Task` (hoặc `Story` nếu project conventions override) |
| **Title** | `[FEAT-XXX] [CR-XX]? [<custom>]? <task title> — <scope?>` (xem [tag system](../conventions-defaults/conventions-defaults.md#tag-system--tổng-quan)) |
| **Labels** | `feat-XXX` (default) + `from-gap-analysis`, `cr-XX` (nếu CR tag bật) + topic kebab-case |
| **Priority** | Map từ source: `P0 → Highest`, `P1 → High`, `P2 → Medium` |
| **Estimate** (tổng) | `Est BA + Est FE + Est BE` man-hours |
| **Description** | Theo template bên dưới (rút gọn nếu không có Gap data) |

### Tag system — applied

| Tag | Khi nào xuất hiện |
|---|---|
| `[FEAT-XXX]` | **Default ON** — mọi task. User có thể tắt trong `jira-conventions.md` |
| `[CR-XX]` | Có khi task xuất phát từ Change Request (story name chứa prefix `[CR-XX]`). Không có nếu task không liên quan CR |
| `[BUG-NNN]` / `[HOTFIX]` / `[TECH-DEBT]` / `[SPIKE]` / … | Custom — user định nghĩa trong project conventions hoặc set per-task |

Thứ tự: `[FEAT] [CR] [custom...]` rồi tới title.

### Title — các thành phần

- **Tag block** (đứng đầu, xem trên): `[FEAT-XXX]` + tag optional khác
- **`<task title>`** — tên công việc:
  - Source = CR → `Description` của Gap Analysis
  - Source = planned story → tên User Story (đã rút gọn, bỏ prefix `[CR-XX]` nếu trùng)
  - Source = bug / refactor → mô tả ngắn (1 dòng)
- **`<scope?>`** (optional, sau ` — `):
  - Source = CR → `Criteria` của Gap Analysis (vd `Dashboard — View mode`)
  - Source khác → tên section / màn bị ảnh hưởng, hoặc bỏ qua

### Ví dụ title (theo source)

| Source | Title |
|---|---|
| CR-derived | `[FEAT-001] [CR-01] Bổ sung view mode dạng bảng — Dashboard — View mode` |
| Planned story | `[FEAT-010] Tạo công việc mới cho Admin` |
| Bug | `[FEAT-019] [BUG-512] Xóa tài liệu trả 500` |
| Hotfix (FEAT tag tắt) | `[HOTFIX] Restart queue worker khi memory leak` |

### Description — template

```markdown
## Context

**As-Is:** <Current System Behavior — bỏ nếu không phải CR>

**To-Be:** <Client Expectation — hoặc mô tả mục tiêu>

**Client Note:** <Note từ KH — bỏ nếu không có>

**Impacted Module:** <Module bị ảnh hưởng>

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
- Source: `<CR-XX>` / `<BUG-NNN>` / `manual` (tuỳ nguồn)
```

> Section nào không có data (vd As-Is/To-Be với planned story) thì **bỏ section đó** thay vì để trống.

## Sub-tasks (linh hoạt theo nội dung — không bắt buộc đủ 3)

**Không phải task nào cũng cần đủ 3 role.** Default mode `auto`: chỉ tạo sub-task cho role thực sự có công việc (impl text non-empty HOẶC estimation > 0). Nếu một role không có gì → bỏ luôn sub-task của role đó.

Project có thể chuyển mode `all` (luôn đủ mọi role) hoặc thêm/bớt role trong list (vd thêm `QA`, `Design`). Xem [`conventions-defaults`](../conventions-defaults/conventions-defaults.md#mode-quyết-định-tạo-sub-task).

Mỗi sub-task được tạo:

| Field | Giá trị |
|---|---|
| **Issue type** | `Sub-task` |
| **Parent** | Main task |
| **Title** | `[<ROLE>] <main title>` — vd `[BA] [FEAT-001] [CR-01] Bổ sung view mode dạng bảng — Dashboard — View mode`. **Cùng** title main task, chỉ thêm prefix `[BA]`/`[FE]`/`[BE]` ở đầu (trước tag block) |
| **Assignee** | Để trống (PM gán sau) hoặc default theo role |
| **Estimate** | Est của role đó (man-hours) |
| **Description** | Bullet list công việc của role (lấy từ Impact Analysis cột Impl·BA/FE/BE, hoặc breakdown thủ công) |

### Description sub-task — template

```markdown
## Công việc của <ROLE>

<bullet list — chỉ công việc của role này>

## Estimation

<X> man-hours

## Reference

- Main task: <parent issue key>
- AC liên quan: AC-XXX-01, AC-XXX-02, …
```

### Quy tắc về sub-task

- **Linh hoạt theo nội dung** (mode `auto`): role nào không có việc thì không tạo. Role nào có việc thì tạo đúng 1 sub-task.
- **Mode `all`** (tuỳ chọn): vẫn tạo đủ mọi role trong list — sub-task của role 0h ghi `Không có công việc cho role này`. Dùng khi muốn checklist đầy đủ cho dev confirm "no work needed".
- Title sub-task **phải giống** title main task, chỉ khác prefix `[<ROLE>]`. Đừng paraphrase, đừng bỏ tag.
- Body sub-task **chỉ chứa** công việc của role đó — không nhồi context (đã có ở main task).
- Không tạo sub-task với body rỗng (mode `auto` đã loại; mode `all` có placeholder text).

## Output file format

| File | Mục đích |
|---|---|
| `output/jira/<source-id>-task.json` | Payload cho Jira REST API `POST /rest/api/3/issue` (main) + 3 sub-tasks. Vd: `cr-01-task.json`, `story-034-task.json`, `bug-512-task.json` |
| `output/jira/<source-id>-task.md` | Markdown để paste vào Jira UI |
| `output/jira/all-tasks.csv` | (tuỳ chọn) Bulk CSV import cho nhiều task cùng lúc |
