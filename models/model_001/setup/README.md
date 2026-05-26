# setup — README

`/set-up` slash command — bootstrap a BA project workspace in one shot.

## TL;DR

```bash
# From the working folder (parent of MasterMind/)
python skills/MasterMind/models/model_001/setup/scripts/bootstrap.py
```

→ Creates `input/`, `context/`, `output/`, `docs/`, `conventions/` + drops `CLAUDE.md` + templates.

Or in a chat with Claude: type `/set-up`.

## Files created

```
<working-folder>/
├── CLAUDE.md                        ← onboarding for agent + user
├── input/                           ← user drops raw materials
├── context/                         ← agent-managed .md sidecars
├── output/                          ← deliverables
├── docs/
│   ├── requirements.md              ← requirements table template
│   ├── backlog.md                   ← Epic/Feature/Story skeleton
│   ├── gap-analysis.md              ← 17-column Gap+Impact
│   └── erd.md                       ← Mermaid ERD skeleton
└── conventions/
    ├── README.md
    ├── features-conventions.md       ← override defaults for features skill
    ├── analysis-conventions.md       ← override defaults for analysis skill
    └── jira-conventions.md           ← override defaults for jira skill
```

## Read more

- [`SKILL.md`](SKILL.md) — skill details + 3 ways to invoke
- [`commands/set-up.md`](commands/set-up.md) — Claude Code slash command file (copy into `.claude/commands/`)
- [`scripts/bootstrap.py`](scripts/bootstrap.py) — main script
- [`templates/`](templates/) — full set of templates copied
