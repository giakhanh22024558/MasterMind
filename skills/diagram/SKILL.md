---
name: diagram
description: Build, audit, and maintain software architecture diagrams (C4-style, Mermaid + Drawio twin) that stay in sync with their specifications. Use when drafting a master architecture diagram, running spec-driven audits of any module, designing Data Flow Diagrams overlaid on architecture canvases, refining edge labels, escalating gaps to design decisions, or greying out out-of-scope components for focused sub-views. Domain-agnostic — applies to any software system (mobile, web, distributed, microservices, embedded).
---

# Diagram skill

A complete methodology + tooling for software architecture diagrams that stay in sync with their specifications.

## When to use

Invoke this skill when the user asks you to:

- **Draft** or **extend** a master architecture diagram (C4-style)
- **Audit a module against its spec** — verify the diagram covers what the spec mandates
- Add **data-flow arrows / relationships** between components
- Build a **DFD (Data Flow Diagram)** for a subsystem
- **Refine edge labels** (add reference IDs, characterizations, prohibited markers)
- **Grey out** out-of-scope components for a focused view
- **Escalate a gap** to a tracked design decision row
- Decide between **layer-level vs component-level** edge granularity
- Apply the **storage exception** pattern (component-level edges only where data integrity matters)
- Set up **deferred-decision tracking** for emerging patterns

## Core philosophy

1. **One master diagram + DFD overlays** — the architecture is the canvas; behavioral views live in their own files but visually anchor to the master.
2. **Spec-driven audit** — each module spec is checked against the diagram. Gaps become tracked design decisions, not silent omissions.
3. **Defer-then-promote tracking** — when a pattern emerges (cross-layer reads, hardware access gaps, etc.), log surfaces locally; promote to canonical doc + architecture edge only when enough surfaces accumulate.
4. **Hybrid edge granularity** — default layer-level, with explicit exceptions where data-integrity classification matters.
5. **Reference-ID + characterization** in edge labels — balances compact audit trail with self-explanation.
6. **Atomic script-driven edits** — survive sync races, batch related changes, document edit history.

## Folder structure (C4-style 4-tier model)

```
<project-root>/
├── CLAUDE.md                                    ← project-specific conventions
├── diagrams/
│   ├── README.md                                ← navigation map
│   ├── 1-overview/                              ← Tier 1 · Master architecture
│   │   ├── <project>-architecture.md            (Mermaid)
│   │   └── <project>-architecture.drawio        (Drawio twin)
│   ├── 2-subsystems/                            ← Tier 2 · Per-zone deep-dives
│   │   └── <zone>-<feature>.md
│   ├── 3-flows/                                 ← Behavioral views
│   │   ├── data-flow/                           DFDs
│   │   ├── sequence/
│   │   └── state/
│   └── 4-cross-cutting/                         ← Tier 3 · System-wide concerns
│       ├── compliance-matrix.md
│       └── performance-targets.md
├── research/
│   └── design-decisions.md                      ← authoritative decision rows
└── .scripts/                                    ← atomic Python edits
```

See [`conventions/folder-structure.md`](conventions/folder-structure.md).

## Workflow templates

### Workflow A · Spec-driven audit

When a user provides a module spec and asks for a coverage check:

1. **Read spec carefully** — list every input, output, storage target, constraint, mandate
2. **Build coverage table** (3 columns: spec item → current edge/element → status)
3. **Classify each gap**:
   - ✅ Covered (no action)
   - 🟡 Partial (label refinement or content update)
   - 🔴 Missing (new edge / cell / cylinder needed)
4. **Recommend options** per gap (A/B/C/D with trade-offs)
5. **Apply** chosen options + **log** non-applied gaps as deferred design decisions

See [`patterns/spec-driven-audit.md`](patterns/spec-driven-audit.md) and [`examples/audit-workflow-example.md`](examples/audit-workflow-example.md).

### Workflow B · New DFD authoring

When user asks to create a DFD for a subsystem:

1. **Copy full master architecture canvas** to `3-flows/data-flow/dfd-<scope>.drawio`
2. **Add DFD overlay legend block** (template in `conventions/dfd-authoring.md`)
3. **Run grey-out script** — keep only in-scope cells colored + textual; everything else greyed + empty
4. **Add Yourdon process numbers** (`1.0`, `2.0`, …) to in-scope cells
5. **Overlay edges** — purple dotted (data flow) + red dashed (prohibited) + `TRIGGER:` prefix on initiating edges

See [`conventions/dfd-authoring.md`](conventions/dfd-authoring.md).

### Workflow C · Adding architecture edge

1. **Decide granularity** — layer-level (default) or component-level (storage exception only)
2. **Pick label form** — verb form for operational edges, noun form for data-payload edges
3. **Add reference-ID + characterization** if citing a design-decision or spec authority
4. **Update both Mermaid + Drawio atomically** — use a Python script to avoid sync race
5. **Log design decision** if architectural significance is non-trivial

See [`conventions/edge-labels.md`](conventions/edge-labels.md) and [`scripts/`](scripts/).

## Key patterns

| Pattern | When | Doc |
|---|---|---|
| Storage exception | Edge touches a storage cell — render at component level | [`patterns/storage-exception.md`](patterns/storage-exception.md) |
| Cross-layer reads (defer-then-promote) | One layer reads from another — defer master visualization until N surfaces | [`patterns/cross-layer-reads-tracking.md`](patterns/cross-layer-reads-tracking.md) |
| Hardware access gaps (defer-then-resolve) | Feature needs hardware not modeled in architecture · spec ambiguous about access pattern | [`patterns/hardware-gaps-tracking.md`](patterns/hardware-gaps-tracking.md) |
| Design-decisions row format | Capture every architectural choice with rationale + revisit trigger | [`patterns/design-decisions-format.md`](patterns/design-decisions-format.md) |
| Spec-driven audit | Per-module verification workflow | [`patterns/spec-driven-audit.md`](patterns/spec-driven-audit.md) |

## Script library

| Script | Use case |
|---|---|
| `grey-out-non-scope.py` | DFD canvas prep — keep in-scope cells, grey out + empty everything else |
| `update-cell-value.py` | Atomic update of a cell's label without touching style/geometry |
| `add-cell.py` | Atomic insertion of a new cell with provisional or normal style |
| `revert-edges.py` | Roll back a batch of edges and restore previous state |

All scripts: read a Drawio file, apply targeted regex updates, write back atomically. Designed to survive cloud-sync races (re-run if first attempt was overwritten).

See [`scripts/`](scripts/).

## Anti-patterns

- ❌ Generate edges from spec wording without confirming destination → imaginary architecture
- ❌ Skip the audit coverage table → incomplete check, silent omissions
- ❌ Apply all gaps at once → design decisions should be staged with explicit options + rationale
- ❌ Mix Mermaid + Drawio out of sync → always update both atomically
- ❌ Add component-level edges everywhere → hybrid keeps default at layer-level for readability
- ❌ Delete a cell when scope changes → grey it out + empty label preserves canvas-mapping
