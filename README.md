# MasterMind

A repository of reusable, project-agnostic **skills** for AI agents and human collaborators. Each skill captures a domain's methodology, conventions, patterns, and tooling in a stable, versioned, modular structure that any future session — any model, any contributor — can pick up and apply.

## Top-level layout

```
MasterMind/
├── README.md                 ← this file
├── meta/                     ← meta-skill: how to create any new skill
├── template/                 ← starter scaffold for new skills
└── skills/
    └── diagram/              ← actual created skills live here
        └── …
```

### Three sibling components

| Folder | Purpose | When to read |
|---|---|---|
| [`meta/`](meta/) | **Meta-skill** — the mindset, conventions, and patterns every skill in this repo follows | When creating a new skill, or reviewing existing skills for consistency |
| [`template/`](template/) | **Starter scaffold** — copy this to create a new skill with the uniform structure pre-built | When starting from scratch (or use `meta/scripts/v1/scaffold-new-skill.py` to automate) |
| [`skills/`](skills/) | **Created skills** — each subfolder is one skill (e.g. `diagram/`) | When applying a skill to a project |

## How to use this repo

### As an AI agent (any session, any model)

1. **Read** [`meta/SKILL.md`](meta/SKILL.md) to understand the conventions of this repo
2. **Find the skill** for the user's request — look in [`skills/`](skills/) for an existing one
3. **Apply** the skill by reading its top-level `SKILL.md`
4. **For project-specific overrides** — look for `<project-root>/<skill>-conventions.md` before applying skill defaults

### As a creator of a new skill

1. Read [`meta/SKILL.md`](meta/SKILL.md) for the patterns to follow
2. Run [`meta/scripts/v1/scaffold-new-skill.py`](meta/scripts/v1/scaffold-new-skill.py) (after editing CONFIG block) to scaffold a new skill from [`template/v1/`](template/v1/)
3. Fill in content for your domain following the uniform structure
4. Update [`skills/README.md`](skills/README.md) to add your skill to the table

### As a consumer of an existing skill

Open the skill's folder (e.g. [`skills/diagram/`](skills/diagram/)) and read its top-level `SKILL.md` or `README.md`.

## Repo-wide conventions (apply to ALL skills)

1. **Uniform folder structure** — every skill follows the same shape (`SKILL.md`, `conventions-schema/`, `conventions-defaults/`, `patterns/`, `examples/`, `scripts/`, type-specific docs)
2. **Per-leaf-folder versioning** — every content module is versioned at `vN/` grain · default = latest
3. **Conventions as data** — projects provide their own conventions in `<project-root>/<skill>-conventions.md`
4. **Defer-then-promote** — emerging structural concerns accumulate locally before being promoted to canonical
5. **Atomic edits** when manipulating sync-prone files

See [`meta/SKILL.md`](meta/SKILL.md) for the full rationale.

## License

Internal. Adapt freely. No warranty.
