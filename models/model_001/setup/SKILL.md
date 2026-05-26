---
name: setup
description: Bootstrap a brand-new BA project workspace using model_001. Triggered by the user typing `/set-up` (or "setup", "bootstrap", "new project", "init workspace"). Creates the Core-Rule folder layout (`input/`, `context/`, `output/`), drops a `CLAUDE.md` onboarding guide at working-folder root, and copies ready-to-fill artifact templates for the main BA deliverables (Requirements, Backlog, Gap/Impact Analysis, ERD) plus skeleton `<skill>-conventions.md` files. After running, the user can drop raw input into `input/` and start working on the docs/ templates immediately, with the agent picking the right model_001 skill per task.
---

# setup — `/set-up` command

Một-lệnh scaffold cho project mới dùng model_001.

## Khi nào dùng

- User vừa clone MasterMind vào working folder mới
- User type `/set-up` (hoặc "setup project", "bootstrap", "init workspace")
- Project hiện chưa có `input/`, `context/`, `output/` hoặc templates

## Skill làm gì

1. **Phát hiện working folder** — folder cha của `MasterMind/`
2. **Tạo folder structure** theo Core Rule:
   - `input/` — user drop raw materials (SRS docx, CR files, screenshots…)
   - `context/` — agent-managed `.md` sidecars
   - `output/` — deliverables (.docx, .xlsx, .drawio…)
   - `docs/` — artifact templates user làm việc trực tiếp
   - `conventions/` — project-level convention overrides
3. **Drop CLAUDE.md** tại working folder root — onboarding doc cho agent + user
4. **Copy artifact templates** vào `docs/`:
   - `requirements.md` — bảng requirements
   - `backlog.md` — Epic / Feature / Story / AC skeleton
   - `gap-analysis.md` — Gap + Impact Analysis (17 cột chuẩn)
   - `impact-analysis.md` — nếu tách riêng
   - `erd.md` — Mermaid ERD skeleton
5. **Copy convention skeleton** vào `conventions/`:
   - `features-conventions.md`, `analysis-conventions.md`, `jira-conventions.md`
   - User fill khi muốn override defaults; bỏ trống → defaults áp dụng

Idempotent: chạy lại không ghi đè file đã có (trừ khi `--force`).

## Cách invoke

### Cách 1 — Type `/set-up` trong chat
Agent recognize keyword (qua skill description) → chạy `bootstrap.py`.

### Cách 2 — Slash command file (cho Claude Code)
Copy [`commands/set-up.md`](commands/set-up.md) vào `~/.claude/commands/set-up.md` (global) hoặc `<working-folder>/.claude/commands/set-up.md` (project).

### Cách 3 — Direct CLI
```bash
cd <working-folder>
python skills/MasterMind/models/model_001/setup/scripts/bootstrap.py
```

Flags:
- `--force` — overwrite existing template files
- `--workdir <path>` — override working folder detection

## Output mẫu

```
Working folder: C:\Users\Admin\NewProject

✓ Created 14 items:
  📁 input/
  📁 context/
  📁 output/
  📁 docs/
  📁 conventions/
  📄 CLAUDE.md
  📄 docs/requirements.md
  📄 docs/backlog.md
  📄 docs/gap-analysis.md
  📄 docs/erd.md
  📄 conventions/README.md
  📄 conventions/features-conventions.md
  📄 conventions/analysis-conventions.md
  📄 conventions/jira-conventions.md

📖 Next: read CLAUDE.md
```

## Content modules

| Module | Purpose |
|---|---|
| [`commands/set-up.md`](commands/set-up.md) | Claude Code slash command file |
| [`scripts/bootstrap.py`](scripts/bootstrap.py) | Scaffolding logic (Python, no deps) |
| [`templates/`](templates/) | Tất cả file template được copy |

## Anti-patterns

- ❌ Chạy `/set-up` trong folder đã có project khác — bootstrap không phá data nhưng có thể trộn convention; chạy ở folder mới
- ❌ Edit template trong MasterMind repo — sửa version ở project (sau khi bootstrap copy)
- ❌ Commit `input/`, `context/`, `output/` vào MasterMind repo — chúng là per-project, không phải của repo MasterMind

## Cross-references

- [Core Rule](../../../core/core-rule/) — định nghĩa folder layout
- [`document/requirements/`](../document/requirements/) · [`document/features/`](../document/features/) · [`document/analysis/`](../document/analysis/) · [`diagram/erd/`](../diagram/erd/) — skills tạo từng artifact (templates trỏ về)
- [`business_analysis/`](../business_analysis/) — pipeline orchestrate tất cả
