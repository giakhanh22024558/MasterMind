# Diagram skill (modular · config-driven)

A reusable, extensible toolkit for software diagrams. **Modular per diagram type · conventions configured per project · methodology shared across all types.**

## Why this structure

Earlier versions baked conventions (colors, IDs, spec codes) into the skill itself — every project had to fork or override. This version separates concerns:

| What | Where | Configurability |
|---|---|---|
| **Cross-cutting methodology** | `_shared/` | Stable across projects (folder structure, design-decisions format, audit workflow, atomic edits, defer-then-promote) |
| **Per-diagram-type rules** | `architecture/`, `dfd/`, `<future-type>/` | Stable across projects within a diagram type (Yourdon notation for DFD, layer hierarchy for architecture, etc.) |
| **Project-specific conventions** | `<project-root>/diagram-conventions.md` | Defined fresh per project (color palette, ID prefixes, spec authority codes) |

The skill's sub-skills **read** project conventions and **apply** them; they don't hardcode any specifics. Defaults exist for projects that don't specify everything.

## Layout

```
skills/diagram/
├── SKILL.md                                       ← top-level dispatcher (pick sub-skill by diagram type)
├── README.md                                      ← this file
│
├── _shared/                                       ← cross-diagram methodology (project-agnostic)
│   ├── conventions-discovery.md                   how the skill loads project conventions
│   ├── folder-structure-general.md                4-tier C4-style layout
│   ├── design-decisions-format.md                 row schema + lifecycle
│   ├── spec-driven-audit.md                       per-module verification workflow
│   ├── defer-then-promote-pattern.md              abstract pattern for emerging structural concerns
│   ├── atomic-edits-pattern.md                    script pattern for sync-prone files
│   ├── edge-labels-general.md                     reference-ID + characterization (generic)
│   └── scripts/                                   diagram-type-agnostic scripts (cell update, cell add, revert)
│
├── architecture/                                  ← architecture diagram sub-skill (C4-style)
│   ├── SKILL.md
│   ├── conventions-schema.md                      what an architecture convention must define
│   ├── conventions-defaults.md                    defaults if project doesn't specify
│   ├── edge-labels.md                             architecture-specific edge label rules
│   ├── patterns/
│   │   ├── storage-exception.md
│   │   ├── cross-layer-reads-tracking.md
│   │   └── hardware-gaps-tracking.md
│   ├── scripts/                                   architecture-specific scripts (if any)
│   └── examples/
│       └── audit-workflow-example.md
│
├── dfd/                                           ← Data Flow Diagram sub-skill
│   ├── SKILL.md
│   ├── conventions-schema.md
│   ├── conventions-defaults.md
│   ├── canvas-overlay-method.md                   DFD as overlay on architecture canvas
│   ├── yourdon-notation.md                        process/store/external entity shapes
│   └── scripts/
│       └── grey-out-non-scope.py                  DFD canvas prep
│
└── _project-template/
    └── PROJECT-CONVENTIONS.md                     copy to <project-root>/diagram-conventions.md
```

## How to adopt in a new project

1. **Copy** [`_project-template/PROJECT-CONVENTIONS.md`](_project-template/PROJECT-CONVENTIONS.md) → `<your-project>/diagram-conventions.md`
2. **Fill in** what applies to your project (colors, naming, prefix conventions) — leave the rest at defaults
3. **Pick the diagram type** you're working on (architecture, DFD, etc.) → read that sub-skill's `SKILL.md`
4. The sub-skill loads your project's conventions and applies them

## How to extend with a new diagram type

When you encounter a diagram type not covered (activity, BPMN, sequence, state, ERD, etc.):

1. Create `skills/diagram/<new-type>/` folder
2. Add 4 files following the same pattern:
   - `SKILL.md` — when to use this sub-skill
   - `conventions-schema.md` — what a project's conventions must define for this diagram type
   - `conventions-defaults.md` — sensible defaults
   - `notation.md` (or equivalent) — visual vocabulary
3. Add type-specific patterns + scripts as discovered through use
4. Update `SKILL.md` "Quick dispatch" table at the top level
5. Update `_project-template/PROJECT-CONVENTIONS.md` with a section for the new diagram type

Each sub-skill is **self-contained** — it can reference `_shared/` but shouldn't depend on another sub-skill.

## Stack

- **Mermaid** — text-based diagrams that render in markdown
- **Drawio** (`.drawio` XML files) — visual twin
- **Python** scripts — atomic edits to Drawio XML (regex-based, idempotent)
- **Markdown** — all narrative, conventions, design decisions

No build step, no toolchain — plain text + a free diagram tool.

## License

Internal skill. Adapt freely. No warranty.
