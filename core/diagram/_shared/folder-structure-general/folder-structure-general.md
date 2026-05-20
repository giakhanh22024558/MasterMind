# Folder structure (C4-style, 4-tier)

Adapted from the C4 model — each tier zooms one level deeper. Reusable across any software project.

## Top-level layout

```
<project-root>/
├── CLAUDE.md                              ← AI agent conventions + project-specific style guide
├── diagrams/
│   ├── README.md                          ← navigation map (read this first)
│   │
│   ├── 1-overview/                        ← TIER 1 · Master architecture (exec-readable)
│   │   ├── <project>-architecture.md      Mermaid source · stripped 1-line components
│   │   └── <project>-architecture.drawio  Drawio twin (multi-page · Architecture + Legend + …)
│   │
│   ├── 2-subsystems/                      ← TIER 2 · Per-zone deep-dives
│   │   ├── <zone-prefix>-<feature>.md
│   │   └── …
│   │
│   ├── 3-flows/                           ← Behavioral views (how data/state moves)
│   │   ├── data-flow/                     Yourdon-notation DFDs
│   │   │   ├── dfd-<scope>.md
│   │   │   └── dfd-<scope>.drawio
│   │   ├── sequence/                      seq-<scenario>.md
│   │   └── state/
│   │       └── state-<entity>.md
│   │
│   └── 4-cross-cutting/                   ← TIER 3 · System-wide concerns
│       ├── compliance-matrix.md           all prohibitions + enforcement
│       ├── performance-targets.md         all numeric SLAs in one place
│       └── …
│
├── research/                              ← External knowledge + decision history
│   ├── design-decisions.md                authoritative decision rows · cross-ref'd
│   ├── tech-stack-inventory.md
│   ├── spec-authority-stack.md
│   └── …
│
└── .scripts/                              ← Per-edit atomic Python scripts
    ├── grey-out-non-<scope>.py
    ├── wire-<feature>-edges.py
    ├── update-<aspect>-label.py
    └── …
```

## The 4 tiers — what goes where

| Tier | Folder | Purpose | Audience |
|---|---|---|---|
| **1** | `1-overview/` | One bird's-eye picture. Zones + 1-line component names. No implementation detail. | Execs · vendors at first contact · onboarding |
| **2** | `2-subsystems/` | Deep-dive one zone at a time (C4 Level 3). Schemas, internal flows. | Devs · vendor implementers · spec reviewers |
| **3** | `3-flows/` | Behavioral views — how data/state moves at runtime. | Devs · QA · integration testers |
| **3** | `4-cross-cutting/` | Concerns spanning multiple zones — prohibitions, SLAs, artifact lifecycles. | Auditors · compliance · architects |

**Rule of thumb:** if info applies to **>1 zone**, it belongs in `4-cross-cutting/`, NOT bolted onto each subsystem diagram.

## File naming (kebab-case)

| Diagram type | Pattern | Example shape |
|---|---|---|
| Subsystem deep-dives | `<zone-prefix>-<descriptor>.md` | `<zone>-<feature>.md` |
| DFDs | `dfd-<scope>.md` | `dfd-<subsystem>.md` |
| Sequence | `seq-<scenario>.md` | `seq-<scenario>.md` |
| State | `state-<entity>.md` | `state-<entity>.md` |
| ERD | `erd-<domain>.md` | `erd-<domain>.md` |
| Cross-cutting | descriptive noun | `compliance-matrix.md`, `performance-targets.md`, `<artifact>-lifecycle.md` |

## Conventions for adding new diagrams

| Adding… | Where |
|---|---|
| Higher-level summary | `1-overview/` (rare — usually one master only) |
| New zone deep-dive | `2-subsystems/<zone-prefix>-<short-name>.md` |
| New flow type (sequence, ERD) | New sub-folder under `3-flows/` with 1+ files |
| New cross-cutting concern | Single file in `4-cross-cutting/` named after the concern |
| One-off Python edit | `.scripts/<descriptive-verb-noun>.py` |

**Always keep `diagrams/README.md` navigation map in sync** with new files.

## Tier-1 master diagram conventions

The single source of truth at executive level:

- One `.md` file (Mermaid source)
- One `.drawio` twin (visual reference for those who don't render Mermaid)
- Multi-page Drawio: Architecture · Legend · (optional dedicated subsystem pages)
- **Layer-level edges only** (with explicit storage exception — see `patterns/storage-exception.md`)
- Components shown as 1–2 line cells; deep detail lives in Tier-2

## Tier-2 subsystem deep-dive structure (template)

Each `<zone>-<feature>.md` file follows this skeleton:

```markdown
# <Spec-ID> · <Name> — Subsystem Deep-Dive

**Status:** 🚧 Stub · 🟡 Partial · ✅ Filled
**Tier:** 2 (Subsystem / C4 Component level)
**Zone in master:** `<zone container ID>` (...)

## Scope
Brief description of what this subsystem owns.

## What this diagram will show (TODO)
- [ ] Component listing with internal structure
- [ ] Schema details
- [ ] Boundaries with adjacent zones
- [ ] Spec mandates list

## Per-module audit findings (added as specs land)
### `<Spec-ID>` — audited (date)
- [ ] Inputs · outputs · capability · access controls
- [ ] Architecture status: gap dispositions + design-decision references

## Diagram type
Brief description of what graph layout best suits this.

## Cross-references
- Master: `...`
- Compliance: `...`
- Performance: `...`
- Design decisions: `...`
- Navigation: `../README.md`
```

## Cross-cutting docs structure

Each `4-cross-cutting/*.md` file aggregates info from multiple zones:

| File | Aggregates |
|---|---|
| `compliance-matrix.md` | All `[X] PROHIBITED` paths + rejection triggers + enforcement points |
| `performance-targets.md` | All numeric SLAs in one master table |
| `<artifact>-lifecycle.md` | Single-artifact journey across multiple subsystems |

Single canonical source per concern — subsystem docs **reference rows** here instead of repeating.

## Design-decisions doc

Lives at `research/design-decisions.md` (not under `diagrams/`).

Structured as a master table where every architectural choice (whether applied or deferred) is captured as a row with: choice · alternatives · rationale · revisit trigger · status · spec authority.

See [`../design-decisions-format/`](../design-decisions-format/) for the full row format.

## Scripts folder

`.scripts/` holds per-edit atomic Python scripts. Each script:

- Has a docstring explaining what it does and why
- Reads a Drawio file
- Applies targeted regex updates
- Writes back atomically (single `write_text` call)
- Prints a summary (cells touched, edges added, etc.)

These scripts are **kept after running** — they document the edit history and can be re-run to recover from sync races.
