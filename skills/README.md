# Skills repository

A collection of reusable, project-agnostic skills for AI agents and human collaborators. Each skill captures a domain's methodology, conventions, patterns, and tooling in a stable folder structure that future sessions can pick up and apply.

## Currently implemented

| Skill | Purpose | Status |
|---|---|---|
| [`diagram/`](diagram/) | Build, audit, and maintain software diagrams (architecture, DFD, future types) | ✅ Architecture sub-skill complete · DFD pending |
| [`_meta/`](_meta/) | **Meta-skill** — how to create any new skill in this repo (mindset · structure · patterns) | ✅ Foundational |
| [`_template/`](_template/) | Copy-paste starter for a new skill | ✅ v1 |

## How to use this repo

### As a reader / consumer of an existing skill

Open the skill's folder (e.g. [`diagram/`](diagram/)) and read its `SKILL.md` (agent-facing) or `README.md` (human-facing). Each skill is self-contained.

### As a creator of a new skill

1. **Read [`_meta/SKILL.md`](_meta/SKILL.md)** first — it explains the meta-pattern (structure, versioning, conventions-as-data, etc.) that every skill in this repo follows
2. **Copy [`_template/v1/`](_template/v1/)** as your starting skeleton — rename to `<your-skill-name>/`
3. **Fill in your skill's content** — keep the uniform folder structure so future readers know where to look
4. **Reference patterns from [`_meta/`](_meta/)** rather than duplicating — versioning model, conventions discovery, etc. are documented once at meta-level

### As an AI agent (any session, any model)

- Default behavior: read the skill's top-level `SKILL.md` to understand when/how to apply it
- For meta-questions about how skills work: read [`_meta/SKILL.md`](_meta/SKILL.md)
- For project-specific overrides: look for `<project-root>/<skill>-conventions.md` (or similar) before applying skill defaults

## Repo-wide conventions

All skills in this repo follow:

1. **Modular sub-skills** when a domain has multiple types (e.g. diagram has architecture, DFD, …)
2. **Uniform folder structure** — every sub-skill has `SKILL.md`, `conventions-schema/`, `conventions-defaults/`, `patterns/`, `examples/`, `scripts/`, type-specific docs
3. **Per-leaf-folder versioning** — every content module is versioned at `vN/` granularity · default = highest `vN`
4. **Conventions as data** — projects provide their own conventions in `<project-root>/<skill>-conventions.md` · skills read + apply
5. **Atomic edits + defer-then-promote** patterns where applicable

See [`_meta/SKILL.md`](_meta/SKILL.md) for the full rationale and how to apply these to a new skill.

## Folder layout

```
skills/
├── README.md                  ← this file
├── _meta/                     ← meta-skill: how to create any skill
├── _template/                 ← starter template for new skills
├── diagram/                   ← skill: software diagrams
└── <future-skills>/           ← e.g. business_analysis · code_review · data_modeling
```

## License

Internal. Adapt freely. No warranty.
