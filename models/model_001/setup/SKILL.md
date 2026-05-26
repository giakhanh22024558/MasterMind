---
name: setup
description: Bootstrap a brand-new BA project workspace using model_001. Triggered by the user typing `/set-up` (or "setup", "bootstrap", "new project", "init workspace"). Creates the Core-Rule folder layout (`input/`, `context/`, `output/`), drops a `CLAUDE.md` onboarding guide at working-folder root, and copies ready-to-fill artifact templates for the main BA deliverables (Requirements, Backlog, Gap/Impact Analysis, ERD) plus skeleton `<skill>-conventions.md` files. After running, the user can drop raw input into `input/` and start working on the docs/ templates immediately, with the agent picking the right model_001 skill per task.
---

# setup — `/set-up` command

One-command scaffold for a new project using model_001.

## When to use

- User has just cloned MasterMind into a fresh working folder
- User types `/set-up` (or "setup project", "bootstrap", "init workspace")
- Project has no `input/`, `context/`, `output/`, or templates yet

## What the skill does

1. **Detect working folder** — the parent folder of `MasterMind/`
2. **Create folder structure** per Core Rule:
   - `input/` — user drops raw materials (SRS docx, CR files, screenshots…)
   - `context/` — agent-managed `.md` sidecars
   - `output/` — deliverables (.docx, .xlsx, .drawio…)
   - `docs/` — artifact templates the user works on directly
   - `conventions/` — project-level convention overrides
3. **Drop CLAUDE.md** at working-folder root — onboarding doc for agent + user
4. **Copy artifact templates** into `docs/`:
   - `requirements.md` — requirements table
   - `backlog.md` — Epic / Feature / Story / AC skeleton
   - `gap-analysis.md` — Gap + Impact Analysis (17-column standard)
   - `erd.md` — Mermaid ERD skeleton
5. **Copy convention skeletons** into `conventions/`:
   - `features-conventions.md`, `analysis-conventions.md`, `jira-conventions.md`
   - User fills these to override defaults; leave empty → skill defaults apply

Idempotent: re-running does not overwrite existing files (unless `--force`).

## How to invoke

### Option 1 — Type `/set-up` in chat
Agent recognizes the keyword (via skill description) and runs `bootstrap.py`.

### Option 2 — Slash command file (for Claude Code)
Copy [`commands/set-up.md`](commands/set-up.md) into `~/.claude/commands/set-up.md` (global) or `<working-folder>/.claude/commands/set-up.md` (per-project).

### Option 3 — Direct CLI
```bash
cd <working-folder>
python skills/MasterMind/models/model_001/setup/scripts/bootstrap.py
```

Flags:
- `--force` — overwrite existing template files
- `--workdir <path>` — override working folder detection

## Sample output

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
| [`templates/`](templates/) | All template files that get copied |

## Anti-patterns

- ❌ Running `/set-up` in a folder that already hosts a different project — the bootstrap won't destroy data but can mix conventions; run it in a fresh folder
- ❌ Editing templates inside the MasterMind repo — edit the project-level copy (the one created after bootstrap)
- ❌ Committing `input/`, `context/`, `output/` into the MasterMind repo — they are per-project, not part of the MasterMind library

## Cross-references

- [Core Rule](../../../core/core-rule/) — defines the folder layout
- [`document/requirements/`](../document/requirements/) · [`document/features/`](../document/features/) · [`document/analysis/`](../document/analysis/) · [`diagram/erd/`](../diagram/erd/) — skills that produce each artifact (templates point back to them)
- [`business_analysis/`](../business_analysis/) — pipeline that orchestrates all of the above
