# Pattern · Story → Jira Task (general)

Luồng tổng quát convert **bất kỳ backlog story** thành Jira issue tree. Áp dụng cho:

- Planned story (không xuất phát từ CR)
- Story từ CR (xem chi tiết riêng ở [`cr-to-task.md`](cr-to-task.md))
- Bug / Hotfix / Tech-debt / Spike thêm thủ công

Schema main + 3 sub-task giống nhau cho mọi source — chỉ khác **tag block** và **độ giàu của context section**.

## Quyết định nguồn (source resolution)

| Tín hiệu trong backlog | Source được suy ra | Tag bổ sung |
|---|---|---|
| Story name có prefix `[CR-XX]` | CR-derived | `[CR-XX]` |
| Story name có prefix `[BUG-NNN]` / `[HOTFIX]` / … | Bug / Hotfix / … | Tag tương ứng |
| Story name không có prefix tag | Planned story | (chỉ `[FEAT-XXX]`) |

Project có thể config thêm các prefix tag custom trong `<project-root>/jira-conventions.md`.

## Inputs theo source

| Source | Cần data từ | Section description |
|---|---|---|
| **Planned** | Backlog (story + feature) + AC sheet | AC table + Reference (skip As-Is / To-Be / Client Note vì không có) |
| **CR-derived** | Backlog + AC + Gap_Analysis.xlsx (row CR-XX) | Full: As-Is / To-Be / Client Note / Impacted Module + AC table |
| **Bug** | Backlog + AC sheet + (tuỳ chọn) link bug report | AC table + Reproduction steps (nếu có) |

## Filter chung — khi nào tạo task

| Điều kiện | Tạo task? |
|---|---|
| `Status ∈ { Ready, In Progress, In Review, Done }` | ✅ — đã refined đủ |
| `Status = Backlog` | ❌ — chưa refined, dev chưa nên claim |
| `Lifecycle = Active` | ✅ |
| `Lifecycle ∈ { Done, Archived, Superseded }` | ❌ — đã ship/loại bỏ, không tạo task mới |
| Nếu source = CR: `Decision ∈ { This Sprint, Next Sprint }` | ✅ |
| Nếu source = CR: `Decision ∈ { Another Sprint, Invalid / Out-of-scope }` | ❌ |

## Workflow

```
                        Backlog (sheet)
                              │
                              ▼
                  ┌────────────────────────┐
                  │ for each story         │
                  │   - filter by Status   │
                  │   - filter by Lifecycle│
                  │   - resolve source     │
                  └───────────┬────────────┘
                              ▼
                  ┌────────────────────────┐
                  │ resolve tag block      │
                  │  [FEAT-XXX]  always*   │
                  │  [CR-XX] if applicable │
                  │  [custom...] if config │
                  └───────────┬────────────┘
                              ▼
                  ┌────────────────────────┐
                  │ load context           │
                  │  - AC list             │
                  │  - Gap row (nếu CR)    │
                  │  - role impl (nếu CR)  │
                  └───────────┬────────────┘
                              ▼
                  ┌────────────────────────┐
                  │ build main task        │
                  │   title = tags + name  │
                  │   desc = context + AC  │
                  └───────────┬────────────┘
                              ▼
                  ┌────────────────────────┐
                  │ build 3 sub-task       │
                  │   [BA] [FE] [BE]       │
                  │   từ Impl per-role     │
                  │   (manual nếu không CR)│
                  └───────────┬────────────┘
                              ▼
                output/jira/<source-id>-task.{json,md}
```

\* User có thể tắt `[FEAT-XXX]` trong project conventions.

## Sub-task cho story không từ CR

Khi không có Impact Analysis (planned story / bug), không có sẵn role breakdown. Hai cách:

1. **BA tự breakdown** trước khi chạy script — nhập 3 bullet list + 3 estimate vào một file phụ (vd `output/jira/inputs/story-034-impl.json`)
2. **Sinh sub-task rỗng** — description ghi `Cần BA breakdown chi tiết theo role`, estimate = 0. Dev / lead fill sau khi grooming.

## Sequencing trong pipeline

Skill này chạy ở **cuối cả 2 nhánh** của BA pipeline:

```
Planned flow:
   requirements → features → backlog → JIRA TASK

CR flow:
   CRs → gap → impact → approval
        → features (sync story + AC) → erd/srs update
        → JIRA TASK
```

Xem [`../../../business_analysis/SKILL.md`](../../../business_analysis/SKILL.md).
