# Diagram skill (modular · config-driven · versioned)

A reusable, extensible toolkit for software diagrams. **Modular per diagram type · uniform folder structure · conventions configured per project · methodology shared across all types · every content module versioned independently.**

## Why this structure

| What | Where | Configurability |
|---|---|---|
| **Cross-cutting methodology** | `_shared/<module>/v<N>/` | Stable across projects · versioned per module |
| **Per-diagram-type rules** | `<type>/<module>/v<N>/` | Stable across projects within a diagram type · versioned per module |
| **Project-specific conventions** | `<project-root>/diagram-conventions.md` | Defined fresh per project (color palette, ID prefixes, spec codes) |

The sub-skills **read** project conventions and **apply** them. Each content module is versioned at the leaf-folder grain — bumping one module doesn't force siblings to bump.

## Layout

```
skills/diagram/
├── SKILL.md                                       ← unversioned dispatcher
├── README.md                                      ← unversioned (this file)
├── VERSIONING.md                                  ← unversioned · explains the versioning model
│
├── _shared/                                       ← cross-diagram methodology
│   ├── conventions-discovery/v1/                  how the skill loads project conventions
│   ├── folder-structure-general/v1/               4-tier C4-style layout for a project's diagrams
│   ├── design-decisions-format/v1/                row schema + lifecycle
│   ├── spec-driven-audit/v1/                      per-module verification workflow
│   ├── defer-then-promote-pattern/v1/             abstract pattern for emerging structural concerns
│   ├── atomic-edits-pattern/v1/                   script pattern for sync-prone files
│   ├── edge-labels-general/v1/                    reference-ID + characterization (generic)
│   └── scripts/v1/                                diagram-type-agnostic scripts
│
├── architecture/                                  ← architecture diagram sub-skill
│   ├── SKILL.md                                   unversioned entry point
│   ├── conventions-schema/v1/                     what an architecture convention must define
│   ├── conventions-defaults/v1/                   defaults if project doesn't specify
│   ├── edge-labels/v1/                            architecture-specific edge label rules
│   ├── patterns/v1/                               reusable patterns
│   │   ├── storage-exception.md
│   │   ├── cross-layer-reads-tracking.md
│   │   └── hardware-gaps-tracking.md
│   ├── examples/v1/                               worked walkthrough(s)
│   │   └── audit-workflow-example.md
│   └── scripts/v1/                                architecture-specific layout helpers
│       ├── README.md
│       ├── compute-row-layout.py
│       ├── align-cells-in-row.py
│       ├── add-edge.py
│       └── resize-container-to-fit.py
│
└── _project-template/v1/                          PROJECT-CONVENTIONS.md template
```

## Versioning

Every content module (leaf folder) has versioned subfolders: `v1/`, `v2/`, …

**Default: latest = highest `vN`.** Override via `<project-root>/diagram-conventions.md` Pinning section.

See [`VERSIONING.md`](VERSIONING.md) for the full model.

## Currently implemented sub-skills

| Sub-skill | Status |
|---|---|
| `architecture/` | ✅ Implemented (all modules at v1) |
| `dfd/` | 📅 To be added later — uniform folder structure mandated per top-level `SKILL.md` |
| `activity/` · `bpmn/` · `sequence/` · `state/` · `erd/` | 📅 Future · add following the uniform structure |

## How to adopt in a new project

1. **Copy** [`_project-template/v1/PROJECT-CONVENTIONS.md`](_project-template/v1/PROJECT-CONVENTIONS.md) → `<your-project>/diagram-conventions.md`
2. **Fill in** what applies to your project (colors, naming, prefix conventions) — leave the rest at defaults
3. **Optionally pin module versions** in the Pinning section if your project depends on older behavior
4. **Pick the diagram type** you're working on (currently: architecture) → read that sub-skill's `SKILL.md`
5. The sub-skill loads your project's conventions, resolves module versions per pinning (or defaults to latest), and applies them

## How to extend with a new diagram type

When you need to add a diagram type not yet covered:

1. Create `skills/diagram/<new-type>/` folder with versioned sub-folders (`patterns/v1/`, `scripts/v1/`, etc.)
2. Write the unversioned `SKILL.md` and required versioned content modules
3. Populate at least one item in `patterns/v1/`, `examples/v1/`, `scripts/v1/`
4. Update top-level `SKILL.md` quick-dispatch table
5. Update `_project-template/v<latest>/PROJECT-CONVENTIONS.md` with a section for the new diagram type

See top-level [`SKILL.md`](SKILL.md) for the detailed 5-step process.

## How to bump a module version

1. Copy `<module>/v(N)/` to `<module>/v(N+1)/`
2. Modify files in v(N+1)/ only
3. Add/update `<module>/CHANGELOG.md` (next to vN subfolders)
4. Don't delete old versions — projects pinned to them still need access

See [`VERSIONING.md`](VERSIONING.md) "How to bump a version" for full detail.

## Stack

- **Mermaid** — text-based diagrams that render in markdown
- **Drawio** (`.drawio` XML files) — visual twin
- **Python** scripts — atomic edits to Drawio XML (regex-based, idempotent)
- **Markdown** — all narrative, conventions, design decisions

No build step, no toolchain — plain text + a free diagram tool.

## License

Internal skill. Adapt freely. No warranty.
