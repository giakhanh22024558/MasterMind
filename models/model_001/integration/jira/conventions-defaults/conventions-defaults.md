# jira · conventions defaults

Defaults áp dụng khi `<project-root>/jira-conventions.md` không khai báo. Project có thể override bất kỳ giá trị nào.

## Defaults

| Item | Default |
|---|---|
| Jira project key | `<PROJECT>` (project phải override — không có default vì tuỳ instance) |
| Main issue type | `Task` |
| Sub-task issue type | `Sub-task` |
| Priority mapping | `P0 → Highest` · `P1 → High` · `P2 → Medium` · không có → `Medium` |
| Status mặc định khi tạo | `To Do` |
| Role prefix (sub-task) | `[BA]` · `[FE]` · `[BE]` (luôn 3 cái) |
| Estimation field | `customfield_10016` (Story Points) — tuỳ instance |
| Estimation unit | `man-hours` (số trực tiếp, không convert sang Story Point) |
| Label "from CR" | `from-gap-analysis` |
| Label cho mỗi CR | `cr-XX` (vd `cr-01`) |
| Label cho topic | kebab-case của topic (vd `quan-ly-vu-viec`) |
| Output folder | `output/jira/` |
| File naming | `cr-<XX>-task.json` cho từng CR, `all-tasks.csv` cho bulk |
| Markdown trong description | Jira wiki markup hoặc ADF (Atlassian Document Format) — pick theo instance |

## Title pattern

```
Main:       [CR-XX] <Story title> — <scope CR>
Sub BA:     [BA] [CR-XX] <Story title> — <scope CR>
Sub FE:     [FE] [CR-XX] <Story title> — <scope CR>
Sub BE:     [BE] [CR-XX] <Story title> — <scope CR>
```

- `<Story title>` = **Description từ Gap Analysis** (cột `Description`), không phải tên user story trong backlog (đã có prefix `[CR-XX]` rồi).
- `<scope CR>` = cột `Criteria` trong Gap Analysis (vd `Dashboard — View mode`).
- Separator giữa Story title và scope: ` — ` (em-dash với 2 space).

## Sub-task rule

| Rule | Bắt buộc |
|---|---|
| Luôn tạo đủ 3 sub-task (BA / FE / BE) | ✅ — kể cả role có 0h work, description ghi `Không có công việc` |
| Sub-task title = main task title + prefix role | ✅ — không paraphrase, không rút gọn |
| Body sub-task chỉ chứa công việc của role | ✅ — không lặp lại context của main task |
| Sub-task estimate = Est của role tương ứng | ✅ — lấy từ Impact Analysis (cột J/K/L của Gap_Analysis.xlsx) |

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
- [`../patterns/cr-to-task.md`](../patterns/cr-to-task.md) — luồng convert
- [`../../../document/features/conventions-defaults/ac-writing.md`](../../../document/features/conventions-defaults/ac-writing.md) — format AC bị reference vào description
