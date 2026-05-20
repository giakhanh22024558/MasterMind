# MasterMind

A repository of reusable **skills** for AI agents. Two-tier structure: an invariant core (`core/`) and concrete per-project models (`models/`).

## Structure

```
MasterMind/
├── core/        ← invariant core — shared across projects, unchanged when models are added
│   ├── core-rule/        the 3-layer core rule
│   ├── cross-reference/  cross-reference technique (stub)
│   ├── diagram/          diagram-skill framework
│   ├── document/         document-skill framework
│   ├── meta/             how to create a new skill
│   └── template/         scaffold for a new skill
└── models/      ← concrete per-project skills
    └── model_NNN/
        ├── diagram/<type>/    e.g. architecture
        └── document/<type>/   e.g. srs
```

## Core Rule (invariant)

Every model — however different its input or output format — follows the 3-layer rule:

1. **Input → `.md`** — analyze raw input into Markdown as context
2. **Agent layer** — normalize format into Python code (`.md` + Python = source of truth)
3. **User layer** — `.docx` / `.drawio`: when editing, **always grep `.md` first**, then edit via cross-reference

Details: [`core/core-rule/`](core/core-rule/).

## Using the repo

- **Apply an existing skill** → open `models/model_NNN/<category>/<skill>/SKILL.md`
- **Create a new skill** → read [`core/meta/SKILL.md`](core/meta/SKILL.md), scaffold from [`core/template/`](core/template/), place it under `models/model_NNN/`
- **Understand the core** → [`core/README.md`](core/README.md)

## License

Internal. Adapt freely. No warranty.
