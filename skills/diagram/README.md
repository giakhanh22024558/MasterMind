# Diagram skill (modular · config-driven)

A reusable, extensible toolkit for software diagrams. **Modular per diagram type · uniform folder structure · conventions configured per project · methodology shared across all types.**

## Why this structure

| What | Where | Configurability |
|---|---|---|
| **Cross-cutting methodology** | `_shared/` | Stable across projects (folder structure, design-decisions, audit workflow, atomic edits, defer-then-promote) |
| **Per-diagram-type rules** | `architecture/`, `<future>/` | Stable across projects within a diagram type · uniform folder structure mandated |
| **Project-specific conventions** | `<project-root>/diagram-conventions.md` | Defined fresh per project (color palette, ID prefixes, spec authority codes) |

The sub-skills **read** project conventions and **apply** them; they don't hardcode any specifics. Defaults exist for projects that don't specify everything.

## Layout

```
skills/diagram/
├── SKILL.md                                       ← top-level dispatcher (picks sub-skill by diagram type)
├── README.md                                      ← this file
│
├── _shared/                                       ← cross-diagram methodology (project-agnostic)
│   ├── conventions-discovery.md                   how the skill loads project conventions
│   ├── folder-structure-general.md                4-tier C4-style layout for a project's diagrams
│   ├── design-decisions-format.md                 row schema + lifecycle
│   ├── spec-driven-audit.md                       per-module verification workflow
│   ├── defer-then-promote-pattern.md              abstract pattern for emerging structural concerns
│   ├── atomic-edits-pattern.md                    script pattern for sync-prone files
│   ├── edge-labels-general.md                     reference-ID + characterization (generic)
│   └── scripts/                                   diagram-type-agnostic scripts (cell update, cell add, revert)
│
├── architecture/                                  ← architecture diagram sub-skill (C4-style)
│   ├── SKILL.md                                   entry point
│   ├── conventions-schema.md                      what an architecture convention must define
│   ├── conventions-defaults.md                    defaults if project doesn't specify
│   ├── edge-labels.md                             architecture-specific edge label rules
│   ├── patterns/                                  ← uniform sub-folder
│   │   ├── storage-exception.md
│   │   ├── cross-layer-reads-tracking.md
│   │   └── hardware-gaps-tracking.md
│   ├── examples/                                  ← uniform sub-folder
│   │   └── audit-workflow-example.md
│   └── scripts/                                   ← uniform sub-folder
│       ├── README.md
│       ├── compute-row-layout.py                  pure layout calculator
│       ├── align-cells-in-row.py                  re-align cells after addition
│       ├── add-edge.py                            atomic edge insertion with style presets
│       └── resize-container-to-fit.py             auto-fit container to children
│
└── _project-template/
    └── PROJECT-CONVENTIONS.md                     copy to <project-root>/diagram-conventions.md
```

## Currently implemented sub-skills

| Sub-skill | Status |
|---|---|
| `architecture/` | ✅ Implemented |
| `dfd/` | 📅 To be added later — uniform folder structure mandated per top-level `SKILL.md` |
| `activity/` · `bpmn/` · `sequence/` · `state/` · `erd/` | 📅 Future · add following the uniform structure |

## Uniform folder structure for diagram-type sub-skills (mandatory)

Every `skills/diagram/<type>/` folder MUST have:

```
<type>/
├── SKILL.md                    ← agent-facing entry point
├── conventions-schema.md       ← checklist of conventions to define
├── conventions-defaults.md     ← sensible defaults
├── <type-specific docs>        ← e.g. edge-labels.md, notation.md
├── patterns/                   ← reusable patterns
├── examples/                   ← worked walkthroughs
└── scripts/                    ← type-specific layout/edit helpers + README.md
```

See top-level [`SKILL.md`](SKILL.md) "Adding a new diagram-type sub-skill" for the full 5-step process.

## How to adopt in a new project

1. **Copy** [`_project-template/PROJECT-CONVENTIONS.md`](_project-template/PROJECT-CONVENTIONS.md) → `<your-project>/diagram-conventions.md`
2. **Fill in** what applies to your project (colors, naming, prefix conventions) — leave the rest at defaults
3. **Pick the diagram type** you're working on (currently: architecture) → read that sub-skill's `SKILL.md`
4. The sub-skill loads your project's conventions and applies them

## How to extend with a new diagram type

When you need to add a diagram type not yet covered:

1. Create `skills/diagram/<new-type>/` folder with the uniform structure
2. Write the 4 required top-level docs
3. Populate `patterns/`, `examples/`, `scripts/` (even if initially minimal)
4. Update top-level `SKILL.md` quick-dispatch table
5. Update `_project-template/PROJECT-CONVENTIONS.md` with a section for the new diagram type

See top-level [`SKILL.md`](SKILL.md) for the detailed 5-step process.

## Stack

- **Mermaid** — text-based diagrams that render in markdown
- **Drawio** (`.drawio` XML files) — visual twin
- **Python** scripts — atomic edits to Drawio XML (regex-based, idempotent)
- **Markdown** — all narrative, conventions, design decisions

No build step, no toolchain — plain text + a free diagram tool.

## License

Internal skill. Adapt freely. No warranty.
