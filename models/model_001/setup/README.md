# setup — README

`/set-up` slash command — bootstrap BA project workspace 1 phát.

## TL;DR

```bash
# Trong working folder (cha của MasterMind/)
python skills/MasterMind/models/model_001/setup/scripts/bootstrap.py
```

→ Tạo `input/`, `context/`, `output/`, `docs/`, `conventions/` + drop `CLAUDE.md` + templates.

Hoặc trong chat với Claude: type `/set-up`.

## Files được tạo

```
<working-folder>/
├── CLAUDE.md                        ← onboarding cho agent + user
├── input/                           ← user drop raw materials
├── context/                         ← agent-managed .md sidecars
├── output/                          ← deliverables
├── docs/
│   ├── requirements.md              ← template requirements
│   ├── backlog.md                   ← Epic/Feature/Story skeleton
│   ├── gap-analysis.md              ← Gap+Impact 17 cột
│   └── erd.md                       ← Mermaid ERD skeleton
└── conventions/
    ├── README.md
    ├── features-conventions.md       ← override defaults skill features
    ├── analysis-conventions.md       ← override defaults skill analysis
    └── jira-conventions.md           ← override defaults skill jira
```

## Đọc thêm

- [`SKILL.md`](SKILL.md) — chi tiết skill + 3 cách invoke
- [`commands/set-up.md`](commands/set-up.md) — Claude Code slash command file (copy vào `.claude/commands/`)
- [`scripts/bootstrap.py`](scripts/bootstrap.py) — script chính
- [`templates/`](templates/) — toàn bộ template được copy
