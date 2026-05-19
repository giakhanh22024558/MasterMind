---
name: diagram/dfd
description: Build Data Flow Diagrams overlaid on a master architecture canvas. Use for visualizing how data flows through a subsystem at runtime — triggers, processes, data stores, data flows, prohibited paths. Loads project conventions from `<project-root>/diagram-conventions.md` and applies them; falls back to sub-skill defaults.
---

# DFD sub-skill

For Data Flow Diagrams (Yourdon-style) overlaid on a master architecture canvas.

## When to use this sub-skill

Invoke when the user asks you to:

- **Create a DFD** for a specific subsystem
- **Add data-flow arrows** with payload labels (nouns)
- **Mark process triggers** (`TRIGGER:` prefix on initiating edges)
- **Grey out out-of-scope** components on a copy of the architecture canvas
- **Add Yourdon process numbers** (`1.0`, `2.0`, …)
- **Add prohibited paths** (red dashed `[X] PROHIBITED`)

For the master architecture diagram itself, use the `architecture/` sub-skill instead.

## First step in any DFD work

1. **Discover conventions** — read `<project-root>/diagram-conventions.md` per [`../_shared/conventions-discovery.md`](../_shared/conventions-discovery.md)
2. **Confirm the architecture-canvas source** — which master `.drawio` to overlay on
3. **Apply project conventions** where defined
4. **Fall back to** [`conventions-defaults.md`](conventions-defaults.md) for anything unspecified

## Sub-skill contents

| File | Purpose |
|---|---|
| [`conventions-schema.md`](conventions-schema.md) | What a DFD convention must define (used as checklist when reading project file or asking user) |
| [`conventions-defaults.md`](conventions-defaults.md) | Sensible defaults used when project doesn't specify |
| [`canvas-overlay-method.md`](canvas-overlay-method.md) | The 5-step recipe — copy architecture canvas, add overlay legend, grey out non-scope, add process numbers, overlay edges |
| [`yourdon-notation.md`](yourdon-notation.md) | Visual vocabulary — process (circle), store (cylinder), external entity (rectangle), data-flow (arrow) |
| [`scripts/grey-out-non-scope.py`](scripts/grey-out-non-scope.py) | DFD canvas prep — grey out + empty all non-scope cells |

## Workflow · creating a new DFD

The complete 5-step recipe (see [`canvas-overlay-method.md`](canvas-overlay-method.md) for details):

1. **Copy** master architecture canvas to `diagrams/3-flows/data-flow/dfd-<scope>.drawio`
2. **Copy the DFD legend block** from a reference DFD (or create from template if first DFD in project) · update `► SCOPE OF THIS FILE` line
3. **Run grey-out script** — keep in-scope cells colored + textual; everything else grey + empty
4. **Add Yourdon process numbers** to in-scope component labels (e.g. `1.0 · <Component>`)
5. **Overlay DFD edges** — purple dotted (data) · red dashed (prohibited) · `TRIGGER:` prefix on initiating edges

## Why "canvas-overlay" method

A DFD built as an overlay on the architecture canvas (rather than a stripped subsystem view) gives:

- **1:1 visual mapping** to the master diagram — vendors open both side by side
- **Resilience to architecture changes** — re-copy the canvas, re-apply overlays
- **Out-of-scope context preserved** — greyed cells are still visible, just de-emphasized

See [`canvas-overlay-method.md`](canvas-overlay-method.md) for the full rationale.

## Companion markdown narrative

Each DFD `.drawio` has a matching `.md` file with:

- Notation key (Yourdon shapes + edge styles + `TRIGGER:` prefix)
- Mermaid version of the DFD (for markdown rendering)
- **Process catalogue table** (# · Process · TRIGGER · Inputs · Outputs · Stores)
- **Trigger inventory** (what causes each process to run)
- **Storage tech mapping** (logical → physical)
- **Process independence/dependency map**
- **Architectural constraints visualised** (compliance bullets)
- **Cross-references** to master, subsystem deep-dive, compliance matrix

## Anti-patterns

- ❌ Redrawing a stripped subsystem view → loses 1:1 mapping to master
- ❌ Deleting out-of-scope cells → can't re-apply overlays when master changes
- ❌ Using verb labels for data-flow edges (purple dotted) → noun labels are correct for payloads
- ❌ Skipping `TRIGGER:` prefix → loses semantic distinction between "what initiates" vs "what data flows"
- ❌ Adding edges before greying out → visual clutter during prep
