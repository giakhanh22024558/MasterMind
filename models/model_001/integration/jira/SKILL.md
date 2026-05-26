---
name: jira
description: Generate Jira issues + sub-tasks from approved Change Requests. Reads Gap Analysis (CR scope, As-Is/To-Be, Decision) + Backlog (Story title + AC list) + Impact Analysis (per-role implementation breakdown), then emits one main task per CR with title `[CR-XX] <Story title> — <scope CR>`, body containing context + AC table with codes, plus 3 sub-tasks [BA] / [FE] / [BE] each listing only that role's concrete work. Use this skill after the change-request branch (gap → impact → approval → backlog) is complete and tasks need to be created on Jira.
---

# jira — sinh Jira task từ Change Requests

## Khi nào dùng

Sau khi luồng change-request đã chốt:
1. CR đã có Gap Analysis + Impact Analysis (skill [`analysis`](../../document/analysis/))
2. CR đã được approve (Decision = `This Sprint` / `Next Sprint`)
3. CR đã được đẩy thành User Story trong backlog với AC đầy đủ (skill [`features`](../../document/features/))

→ Skill này **đóng gói các CR đã approve thành Jira issue + sub-task** sẵn sàng import.

## Cấu trúc output — 1 task lớn + 3 sub-task

```
┌─────────────────────────────────────────────────────────────┐
│ [CR-01] Bổ sung view mode dạng bảng — Dashboard — View mode │  ← Main task
│  context: As-Is / To-Be / Client Note                       │
│  AC table: AC-133-01, AC-133-02, …                          │
│                                                             │
│  ├─ [BA] [CR-01] Bổ sung view mode … — Dashboard — View mode│  ← Sub-task 1
│  │      Chỉ liệt kê công việc của BA                        │
│  │                                                          │
│  ├─ [FE] [CR-01] Bổ sung view mode … — Dashboard — View mode│  ← Sub-task 2
│  │      Chỉ liệt kê công việc của FE                        │
│  │                                                          │
│  └─ [BE] [CR-01] Bổ sung view mode … — Dashboard — View mode│  ← Sub-task 3
│         Chỉ liệt kê công việc của BE                        │
└─────────────────────────────────────────────────────────────┘
```

Xem chi tiết format ở [`task-structure/`](task-structure/) và [`conventions-defaults/`](conventions-defaults/).

## Input → Output

| Input | Lấy từ |
|---|---|
| CR scope, As-Is, To-Be, Decision, Note | Gap Analysis sheet |
| Impl·BA / FE / BE (gạch đầu dòng) | Impact Analysis (gộp trong Gap_Analysis.xlsx) |
| Estimation BA/FE/BE (man-hours) | Impact Analysis |
| Story title (đã tag `[CR-XX]`) | Backlog (LEX Features list.xlsx) |
| AC list + AC IDs | Acceptance Criteria sheet |

| Output | Đặt tại |
|---|---|
| Jira import payload | `output/jira/cr-<XX>-task.json` (hoặc `.md` để paste) |

## Content modules

| Module | Purpose |
|---|---|
| [`task-structure/`](task-structure/) | Định nghĩa cấu trúc 1 task lớn + 3 sub-task |
| [`conventions-defaults/`](conventions-defaults/) | Format title / description / sub-task body (mặc định) |
| [`patterns/`](patterns/) | Pattern `CR → Task` — luồng đọc Gap+Backlog+AC sinh task |
| [`examples/`](examples/) | Worked example (CR-01) |
| [`scripts/`](scripts/) | `cr_to_jira.py` — render task tree từ Gap_Analysis.xlsx + Backlog xlsx |

## Conventions

Project có thể override trong `<project-root>/jira-conventions.md` (Jira project key, issue type, custom field mapping…). Mặc định ở [`conventions-defaults/conventions-defaults.md`](conventions-defaults/conventions-defaults.md).

## Anti-patterns

- ❌ Tạo Jira task **trước khi** CR được approve (Decision còn `Pending`)
- ❌ Nhồi tất cả role-work vào main task — phải tách thành 3 sub-task để dev claim riêng
- ❌ Sub-task có description trống — phải có ít nhất 1 bullet công việc theo role
- ❌ Title sub-task khác title main task — phải **cùng** title, chỉ thêm prefix `[BA]/[FE]/[BE]`
- ❌ Quên đối chiếu AC ID trong description — QA cần để test

## Cross-references

| Reference | Used for |
|---|---|
| [`../../document/analysis/`](../../document/analysis/) | Gap + Impact Analysis (input chính) |
| [`../../document/features/`](../../document/features/) | Backlog + AC (input cho title + AC table) |
| [`../../business_analysis/`](../../business_analysis/) | Pipeline upstream — Jira sinh ở cuối CR branch |
| [Core Rule](../../../../core/core-rule/) | input → context → agent → output |
