---
description: Bootstrap a new BA project workspace using MasterMind model_001 — scaffolds folder layout + drops CLAUDE.md onboarding + artifact templates
---

# /set-up

Invoke the **model_001 setup skill** to bootstrap this working folder for BA work.

## Action

Run:
```bash
python skills/MasterMind/models/model_001/setup/scripts/bootstrap.py
```

This will:
1. Detect the working folder (parent of `MasterMind/`)
2. Create `input/`, `context/`, `output/`, `docs/`, `conventions/` (Core-Rule layout)
3. Drop `CLAUDE.md` at working-folder root — agent + user onboarding
4. Copy artifact templates into `docs/` — requirements, backlog, gap-analysis, ERD
5. Copy convention skeletons into `conventions/` — features / analysis / jira
6. Print summary of created/skipped items

Idempotent — won't overwrite existing files unless `--force` passed.

After running:
- Drop raw materials (SRS docx, CR files, screenshots…) into `input/`
- Open `docs/<artifact>.md` and ask the agent to fill it — agent will pick the right skill
- Optionally fill `conventions/<skill>-conventions.md` to override defaults

## Installation (1 lần)

Copy this file to `~/.claude/commands/set-up.md` (global) or `<working-folder>/.claude/commands/set-up.md` (per-project) to make `/set-up` invokable directly from chat.

## See

- [`SKILL.md`](../SKILL.md) — chi tiết skill
- [`scripts/bootstrap.py`](../scripts/bootstrap.py) — logic
