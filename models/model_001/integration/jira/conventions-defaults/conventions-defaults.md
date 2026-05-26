# jira · conventions defaults

Defaults áp dụng khi `<project-root>/jira-conventions.md` không khai báo. Project có thể override bất kỳ giá trị nào.

## Tag system — tổng quan

Mỗi Jira task title bắt đầu bằng một dãy **tag** trong ngoặc vuông. Tag là cách đánh dấu nguồn gốc / loại của task.

| Tag | Default | Mục đích | Khi nào dùng |
|---|---|---|---|
| `[FEAT-XXX]` | **Bật** mặc định ✅ | Đánh dấu task thuộc Feature nào | **Mọi task** đều có (trừ khi user tắt) |
| `[CR-XX]` | Optional | Task xuất phát từ Change Request | Có khi story name chứa prefix `[CR-XX]`; không có nếu task là planned story / bug / refactor |
| `[BUG-XXX]` `[HOTFIX]` `[TECH-DEBT]` `[SPIKE]` … | Optional | Tag custom do project / user định nghĩa | User config trong `jira-conventions.md` hoặc set per-task |

### Thứ tự tag trong title

```
[FEAT-XXX]  [CR-XX]  [<custom tags...>]  <task title>  [— <scope?>]
```

- **Feature tag luôn đứng đầu** (định danh "thuộc về đâu").
- CR tag đứng sau Feature tag (đánh dấu nguồn gốc).
- Custom tag đứng cuối trong dãy tag.
- Sau dãy tag mới tới title + scope.

### Bật / tắt tag

Trong `<project-root>/jira-conventions.md`, ví dụ:

```yaml
tags:
  feature_tag: on          # default; set off để không prepend [FEAT-XXX]
  cr_tag: auto             # auto = bật nếu story có prefix [CR-XX]; off để bỏ
  custom_tags:             # list custom tag mặc định prepend mọi task
    - "MVP-1"
  per_task_override: true  # cho phép script CLI nhận --extra-tag để thêm
```

Khi tag bị tắt, **không** xuất hiện trong title (cũng không hiện ngoặc rỗng).

## Title pattern (sau khi áp dụng tag system)

```
Main:       [FEAT-XXX] [CR-XX]? [custom]? <task title> — <scope?>
Sub BA:     [BA] [FEAT-XXX] [CR-XX]? [custom]? <task title> — <scope?>
Sub FE:     [FE] [FEAT-XXX] [CR-XX]? [custom]? <task title> — <scope?>
Sub BE:     [BE] [FEAT-XXX] [CR-XX]? [custom]? <task title> — <scope?>
```

- Sub-task role prefix (`[BA]/[FE]/[BE]`) đứng **trước cả** Feature tag — dễ filter board theo role.
- `<task title>` = tên công việc:
  - Nếu từ CR → cột `Description` của Gap Analysis
  - Nếu từ planned story → tên user story (đã rút gọn, bỏ prefix `[CR-XX]` nếu trùng)
  - Nếu từ bug / refactor → mô tả ngắn
- `<scope>` (optional): vd `Dashboard — View mode` cho CR (cột `Criteria`), hoặc tên section ảnh hưởng. Bỏ qua nếu task không có scope phụ.
- Separator giữa title và scope: ` — ` (em-dash với 2 space).

### Ví dụ title

| Nguồn task | Title kết quả |
|---|---|
| CR-derived | `[FEAT-001] [CR-01] Bổ sung view mode dạng bảng — Dashboard — View mode` |
| Planned story (không từ CR) | `[FEAT-010] Tạo công việc mới cho Admin` |
| Bug | `[FEAT-019] [BUG-512] Xóa tài liệu trả 500` |
| Hotfix không gắn feature | `[HOTFIX] Restart queue worker khi memory leak` *(feature tag user tắt)* |

## Defaults — các field khác

| Item | Default |
|---|---|
| Jira project key | `<PROJECT>` (project phải override — không có default vì tuỳ instance) |
| Main issue type | `Task` |
| Sub-task issue type | `Sub-task` |
| Priority mapping | `P0 → Highest` · `P1 → High` · `P2 → Medium` · không có → `Medium` |
| Status mặc định khi tạo | `To Do` |
| Role list (sub-task) | `[BA]` · `[FE]` · `[BE]` (default; project có thể thêm QA / Design / Mobile / DevOps) |
| Sub-task creation mode | `auto` — chỉ tạo sub-task cho role có công việc; `all` — luôn tạo đủ mọi role trong list |
| Ngưỡng "không có công việc" | `impl text rỗng` AND `estimation == 0` |
| Estimation field | `customfield_10016` (Story Points) — tuỳ instance |
| Estimation unit | `man-hours` (số trực tiếp, không convert sang Story Point) |
| Label "from CR" | `from-gap-analysis` (chỉ gắn nếu CR tag bật) |
| Label cho mỗi CR | `cr-XX` (vd `cr-01`) — chỉ gắn nếu CR tag bật |
| Label cho mỗi feature | `feat-XXX` (vd `feat-001`) — gắn cùng feature tag |
| Label cho topic | kebab-case của topic / epic name (vd `quan-ly-vu-viec`) |
| Output folder | `output/jira/` |
| File naming | `<source-id>-task.json` (vd `cr-01-task.json`, `story-034-task.json`) |
| Markdown trong description | Jira wiki markup hoặc ADF — pick theo instance |

## Sub-task rule

| Rule | Bắt buộc |
|---|---|
| **Sub-task tạo linh hoạt theo nội dung** | ✅ — không phải task nào cũng cần đủ 3 role. Mặc định `mode: auto` → chỉ tạo sub-task cho role thực sự có công việc. |
| Sub-task title = main task title + prefix role | ✅ — không paraphrase, không rút gọn |
| Body sub-task chỉ chứa công việc của role | ✅ — không lặp lại context của main task |
| Sub-task có nội dung thực (body không rỗng) | ✅ — nếu vô tình tạo sub-task không có gì → phải xoá hoặc fill manual |
| Sub-task estimate = Est của role tương ứng | ✅ — lấy từ Impact Analysis hoặc estimation field của story |

### Mode quyết định tạo sub-task

| Mode | Hành vi | Khi dùng |
|---|---|---|
| `auto` *(default)* | Skip role nếu **cả** impl text rỗng **và** estimation = 0 | Hầu hết case — để tránh sub-task ma |
| `all` | Luôn tạo đủ mọi role trong list (kể cả 0h) | Project muốn checklist đủ 3 role để dev tự confirm "no work needed" |
| `explicit` | Chỉ tạo các role list ra qua flag `--roles` / config | Khi BA muốn lock cứng |

### Override mặc định trong `jira-conventions.md`

```yaml
sub_tasks:
  roles: [BA, FE, BE]          # list role mặc định. Project có thể thêm: [BA, FE, BE, QA, Design]
  mode: auto                   # auto / all / explicit
  zero_work_label: "Không có công việc cho role này"   # text khi force-tạo sub-task rỗng
```

### Ví dụ skip role

| Task | Est BA · FE · BE | Sub-task được tạo |
|---|---|---|
| CR-01 (Bổ sung view mode) | 4 · 16 · 3 | **BA + FE + BE** (cả 3 có work) |
| CR-06 (Ẩn 6 option dropdown — UI fix) | 1 · 2 · 0 | **BA + FE** (skip BE vì 0h) |
| Backend-only: refactor cache layer | 0 · 0 · 8 | **BE** only |
| Frontend bug fix | 0 · 4 · 0 | **FE** only |
| Spike research | 4 · 0 · 0 | **BA** only |
| Cross-cutting (mode `all`) | 4 · 16 · 0 | **BA + FE + BE** (BE description = "Không có công việc cho role này") |

## AC table trong main description

```markdown
| AC ID | Tiêu chí | Test status |
|---|---|---|
| AC-XXX-NN | ☐ <nội dung AC, format Khi/Nếu… thì…> | Not tested |
```

- AC ID lấy từ sheet `Acceptance Criteria` trong `LEX Features list.xlsx`.
- Mỗi AC ghi đúng một row, **không gộp**.
- Test status default `Not tested` — QA sẽ update.

## See also

- [`../task-structure/task-structure.md`](../task-structure/task-structure.md) — schema đầy đủ
- [`../patterns/cr-to-task.md`](../patterns/cr-to-task.md) — luồng CR → task (một trong nhiều source)
- [`../../../document/features/conventions-defaults/ac-writing.md`](../../../document/features/conventions-defaults/ac-writing.md) — format AC bị reference vào description
