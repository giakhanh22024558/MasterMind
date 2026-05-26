---
name: jira
description: Generate Jira issues + sub-tasks from any task source (Change Requests, planned stories, bugs, refactors, hotfixes…). Each main task carries a configurable tag block — `[FEAT-XXX]` by default, plus optional `[CR-XX]` when derived from a Change Request, plus custom tags the project defines. Body contains context + AC table with codes. Sub-tasks are emitted flexibly per role (default `[BA]` / `[FE]` / `[BE]`, configurable): mode `auto` only creates a sub-task for roles that actually have work (skipping zero-work roles); mode `all` always emits the full role list. Reads Gap Analysis + Backlog + Acceptance Criteria sheets. Use this skill whenever the team needs to push refined backlog items onto Jira.
---

# jira — sinh Jira task từ backlog

## Khi nào dùng

Khi cần đẩy story đã refined trên backlog lên Jira. Story có thể đến từ nhiều nguồn:

- **Change Request** đã approve (luồng [`analysis`](../../document/analysis/) → [`features`](../../document/features/))
- **Planned story** trong backlog (không xuất phát từ CR)
- **Bug / Hotfix / Tech-debt / Spike** thêm thủ công

Skill này **đóng gói mỗi story thành Jira issue + 3 sub-task** sẵn sàng import. Tag trên title configurable theo nguồn.

## Tag system

Mỗi title bắt đầu bằng dãy **tag**. Tag report *nguồn gốc* / *loại* của task:

```
[FEAT-XXX]  [CR-XX]?  [<custom>]?  <task title>  [— <scope?>]
```

| Tag | Default | Khi nào |
|---|---|---|
| `[FEAT-XXX]` | **ON** ✅ | Mọi task — định danh feature task thuộc về. Project có thể tắt trong `jira-conventions.md` |
| `[CR-XX]` | optional | Khi story xuất phát từ Change Request (story name có prefix `[CR-XX]`). Bỏ qua nếu task không từ CR |
| `[BUG-NNN]` `[HOTFIX]` `[TECH-DEBT]` `[SPIKE]` … | optional | Custom — project define hoặc per-task |

→ Đầy đủ rule ở [`conventions-defaults/`](conventions-defaults/).

## Cấu trúc output — 1 main task + sub-task linh hoạt

Số lượng sub-task **theo nội dung task**, không cố định. Mode mặc định `auto`: chỉ tạo sub-task cho role có công việc thật. Role list mặc định `[BA, FE, BE]` (project có thể thêm `QA`, `Design`, `Mobile`, `DevOps`…).

```
┌────────────────────────────────────────────────────────────────────────────┐
│ [FEAT-001] [CR-01] Bổ sung view mode dạng bảng — Dashboard — View mode     │  ← Main task
│  context: As-Is / To-Be / Client Note (bỏ section nếu không có data)       │
│  AC table: AC-133-01, AC-133-02, …                                         │
│                                                                            │
│  ├─ [BA] …    (4h) — có việc → có sub-task                                 │
│  ├─ [FE] …   (16h) — có việc → có sub-task                                 │
│  └─ [BE] …    (3h) — có việc → có sub-task                                 │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│ [FEAT-019] [BUG-512] Xóa tài liệu trả 500                                   │  ← Backend-only fix
│                                                                             │
│  └─ [BE] …    (3h) — chỉ BE có việc → chỉ 1 sub-task                       │
└────────────────────────────────────────────────────────────────────────────┘
```

Format đầy đủ ở [`task-structure/`](task-structure/).

## Input → Output

| Input field | Lấy từ | Optional? |
|---|---|---|
| Story ID, Feature ID (cho `[FEAT-XXX]` tag) | Backlog | required |
| Story title | Backlog (đã bỏ prefix `[CR-XX]` để tránh trùng tag) | required |
| AC list + AC IDs | Acceptance Criteria sheet | nên có |
| CR scope, As-Is, To-Be, Decision, Note | Gap Analysis sheet | chỉ khi từ CR |
| Impl·BA / FE / BE + Est | Impact Analysis (gộp trong Gap_Analysis.xlsx) | chỉ khi từ CR; planned story có thể nhập thủ công |
| Custom tags | `jira-conventions.md` hoặc CLI `--extra-tag` | optional |

| Output | Đặt tại |
|---|---|
| Jira import payload | `output/jira/<source-id>-task.json` (vd `cr-01-task.json`, `story-034-task.json`, `bug-512-task.json`) |
| Markdown để paste UI | `output/jira/<source-id>-task.md` |

## Content modules

| Module | Purpose |
|---|---|
| [`task-structure/`](task-structure/) | Schema main + 3 sub-task — áp dụng cho mọi source |
| [`conventions-defaults/`](conventions-defaults/) | Tag system + format defaults; cách override |
| [`patterns/`](patterns/) | Pattern convert mỗi source thành task (CR là một trong nhiều) |
| [`examples/`](examples/) | Worked example (CR-01) |
| [`scripts/`](scripts/) | `cr_to_jira.py` — render task tree từ Gap_Analysis.xlsx + Backlog xlsx |

## Conventions

Project override trong `<project-root>/jira-conventions.md` (Jira project key, issue type, **tag config: bật/tắt feature tag, CR tag, custom tags**, custom field mapping…). Mặc định ở [`conventions-defaults/conventions-defaults.md`](conventions-defaults/conventions-defaults.md).

## Anti-patterns

- ❌ Tạo Jira task **trước khi** story được refined đủ (AC trống, estimation chưa có)
- ❌ Nhồi tất cả role-work vào main task — phải tách thành sub-task để dev claim riêng
- ❌ Cứng nhắc luôn tạo đủ 3 sub-task kể cả role không có việc — mặc định `auto` skip để tránh sub-task ma
- ❌ Sub-task có description trống — phải có ít nhất 1 bullet công việc theo role (hoặc dùng mode `all` với placeholder rõ ràng)
- ❌ Title sub-task khác title main task — phải **cùng** title, chỉ thêm prefix `[BA]/[FE]/[BE]` ở đầu
- ❌ Quên tag — title không có `[FEAT-XXX]` thì dev không biết task thuộc đâu (trừ khi project chủ động tắt feature tag)
- ❌ Trộn nguồn vào tag — `[CR-XX]` chỉ khi task thực sự từ CR; đừng gán bừa cho task planned

## Cross-references

| Reference | Used for |
|---|---|
| [`../../document/features/`](../../document/features/) | Backlog + AC + Feature ID (input cho FEAT tag + title + AC table) |
| [`../../document/analysis/`](../../document/analysis/) | Gap + Impact Analysis (input khi task derive từ CR) |
| [`../../business_analysis/`](../../business_analysis/) | Pipeline upstream — Jira là bước cuối của cả planned flow lẫn CR branch |
| [Core Rule](../../../../core/core-rule/) | input → context → agent → output |
