# MasterMind

A repository of reusable **skills** for AI agents. Two-tier structure: an invariant core (`core/`) and concrete per-project models (`models/`).

## Working folder

Clone MasterMind into a **working folder**. Two sibling folders — created at session start and managed by the user — sit outside the repo:

```
<working-folder>/
├── MasterMind/   ← this repo (the skills)
├── input/        ← raw context files the user provides (any format)
├── context/      ← analyzed context.md mirror of input/ (built by the model)
└── output/       ← finished deliverables (.docx, .xlsx, .drawio...)
```

## Structure

```
MasterMind/
├── core/        ← invariant core — shared across projects, unchanged when models are added
│   ├── core-rule/        the 3-layer core rule + session workflow
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

A model holds **only its skill definition** — no runtime data. The user's `input/`, the analyzed `context/`, and the `output/` all live outside MasterMind.

## Core Rule (invariant)

Every model — however different its input or output format — follows the 3-layer rule:

1. **Input → context** — analyze the files in `input/` into `context.md` files (the source of truth for content)
2. **Agent layer** — normalize format into Python code (`context.md` + Python = source of truth)
3. **User layer** — deliverables in `output/`: when editing, **always grep the context first**, then edit via cross-reference

Full rule + session workflow: [`core/core-rule/`](core/core-rule/).

## Session start

When a session begins in a working folder containing MasterMind:

1. Ensure `input/` and `output/` exist (create if missing).
2. Choose a model under `models/` — or create a new one per the Core Rule.
3. The model ingests `input/` → mirrors it into the `context/` folder as `context.md` files.
4. Deliverables are written to `output/`.

## Using the repo

- **Apply an existing skill** → open `models/model_NNN/<category>/<skill>/SKILL.md`
- **Create a new skill** → read [`core/meta/SKILL.md`](core/meta/SKILL.md), scaffold from [`core/template/`](core/template/), place it under `models/model_NNN/`
- **Understand the core** → [`core/README.md`](core/README.md)

## License

Internal. Adapt freely. No warranty.
