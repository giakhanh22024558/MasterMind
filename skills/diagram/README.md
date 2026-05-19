# Diagram skill

A reusable methodology + tooling kit for software architecture diagrams that stay in sync with their specifications. **Domain-agnostic** — applies to any software project (mobile, web, distributed systems, microservices, embedded).

## Quickstart

| If you want to… | Read |
|---|---|
| Understand the skill in one page | [`SKILL.md`](SKILL.md) |
| Apply the visual style (colors, shapes, edges) | [`conventions/visual-style-guide.md`](conventions/visual-style-guide.md) |
| Format edge labels with reference IDs | [`conventions/edge-labels.md`](conventions/edge-labels.md) |
| Set up the folder structure for a new project | [`conventions/folder-structure.md`](conventions/folder-structure.md) |
| Build a DFD overlaid on a master architecture canvas | [`conventions/dfd-authoring.md`](conventions/dfd-authoring.md) |
| Decide layer-level vs component-level edges | [`patterns/storage-exception.md`](patterns/storage-exception.md) |
| Track cross-layer reads (defer-then-promote) | [`patterns/cross-layer-reads-tracking.md`](patterns/cross-layer-reads-tracking.md) |
| Track hardware access gaps | [`patterns/hardware-gaps-tracking.md`](patterns/hardware-gaps-tracking.md) |
| Capture an architectural decision | [`patterns/design-decisions-format.md`](patterns/design-decisions-format.md) |
| Run a spec-driven audit | [`patterns/spec-driven-audit.md`](patterns/spec-driven-audit.md) |
| See a worked walkthrough | [`examples/audit-workflow-example.md`](examples/audit-workflow-example.md) |
| Use a reusable Python script | [`scripts/`](scripts/) |

## Folder layout

```
skills/diagram/
├── SKILL.md                                    ← agent-facing skill definition
├── README.md                                   ← this file
├── conventions/
│   ├── visual-style-guide.md                   colors · shapes · edge styles
│   ├── edge-labels.md                          verb-form rule · reference-ID format
│   ├── folder-structure.md                     C4 4-tier model
│   └── dfd-authoring.md                        canvas-overlay convention
├── patterns/
│   ├── storage-exception.md                    hybrid edge granularity
│   ├── cross-layer-reads-tracking.md           defer-then-promote
│   ├── hardware-gaps-tracking.md               defer-then-resolve
│   ├── design-decisions-format.md              decision row template + lifecycle
│   └── spec-driven-audit.md                    per-module verification workflow
├── scripts/
│   ├── grey-out-non-scope.py                   DFD canvas prep
│   ├── update-cell-value.py                    atomic label updates
│   ├── add-cell.py                             atomic cell insertion
│   └── revert-edges.py                         rollback pattern
└── examples/
    └── audit-workflow-example.md               worked example
```

## Core principles (one-liner version)

1. **Architecture as canvas, DFD as overlay** — never redraw a stripped-down subsystem view
2. **Spec-driven audit** — coverage tables, not opinion
3. **Defer-then-promote** — accumulate enough surfaces of a pattern before structural commit
4. **Hybrid edge granularity** — layer-level default, component-level only where data integrity matters
5. **Reference-ID + characterization** in edge labels — audit trail + self-explanation
6. **Atomic script-driven edits** — survive sync races, batch related changes

## Stack

- **Mermaid** — text-based diagrams that render in markdown (architecture master + DFDs)
- **Drawio** (`.drawio` XML files) — visual twin
- **Python** scripts — atomic edits to Drawio XML (regex-based, idempotent)
- **Markdown** — all narrative, conventions, design decisions

No build step, no toolchain — plain text + a free diagram tool.

## How to adopt in a new project

1. Read [`conventions/folder-structure.md`](conventions/folder-structure.md) and create the tier-0 folder layout
2. Apply [`conventions/visual-style-guide.md`](conventions/visual-style-guide.md) when drafting your first master diagram
3. Whenever someone gives you a module spec, run the workflow in [`patterns/spec-driven-audit.md`](patterns/spec-driven-audit.md)
4. Capture every architectural choice as a row per [`patterns/design-decisions-format.md`](patterns/design-decisions-format.md)
5. When a recurring pattern emerges (cross-layer reads, hardware gaps, etc.), use defer-then-promote per [`patterns/cross-layer-reads-tracking.md`](patterns/cross-layer-reads-tracking.md)
6. When you need a DFD for a subsystem, copy the master canvas + overlay per [`conventions/dfd-authoring.md`](conventions/dfd-authoring.md)
7. Use [`scripts/`](scripts/) templates for batched Drawio edits

## License

Internal skill. Adapt freely. No warranty.
