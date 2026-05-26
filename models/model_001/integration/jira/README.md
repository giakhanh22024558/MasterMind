# jira — README

Sinh **Jira issue + sub-task** từ Change Requests đã approve.

## TL;DR

Mỗi CR → **1 task lớn** + **3 sub-task** ([BA]/[FE]/[BE]).

```
[CR-XX] <Story title> — <scope CR>            ← main task
├─ [BA] [CR-XX] <Story title> — <scope CR>    ← chỉ work của BA
├─ [FE] [CR-XX] <Story title> — <scope CR>    ← chỉ work của FE
└─ [BE] [CR-XX] <Story title> — <scope CR>    ← chỉ work của BE
```

- Main task description = context (As-Is/To-Be/Client Note) + bảng AC có code (`AC-XXX-NN`).
- Mỗi sub-task description = bullet list công việc cụ thể của role đó (lấy từ Impact Analysis), + estimation man-hours của role.

## Đầu vào

- `output/Gap_Analysis.xlsx` (CR + scope + impl breakdown per role + estimation + decision)
- `output/LEX Features list.xlsx` (Backlog: Story title đã tag `[CR-XX]` + Acceptance Criteria sheet)

## Đầu ra

- `output/jira/cr-<XX>-task.json` (cho Jira REST API import)
- hoặc `output/jira/cr-<XX>-task.md` (paste vào Jira UI)

## Khi nào dùng

Sau khi:
1. Gap + Impact Analysis xong
2. CR được approve (Decision = `This Sprint` hoặc `Next Sprint`)
3. Story đã thêm vào backlog với AC đầy đủ

→ Chạy skill này để bundle thành Jira task.

## Đọc thêm

- [`SKILL.md`](SKILL.md) — entry point đầy đủ
- [`task-structure/task-structure.md`](task-structure/task-structure.md) — schema chi tiết
- [`conventions-defaults/conventions-defaults.md`](conventions-defaults/conventions-defaults.md) — format mặc định
- [`patterns/cr-to-task.md`](patterns/cr-to-task.md) — luồng convert
- [`examples/example-cr-01.md`](examples/example-cr-01.md) — worked example
