# DFD authoring convention

How to build Data Flow Diagrams that visually anchor to the master architecture for trivial cross-mapping.

## Core principle — "Architecture as canvas, DFD as overlay"

Every DFD `.drawio` file is built on top of a **full copy of the master architecture canvas**. Do NOT redraw a stripped-down subsystem view.

### Why

- **Same component IDs, same colors, same positions** → vendor maps DFD ↔ architecture by sight, no mental translation
- **Stays in sync** when architecture evolves (re-copy canvas, re-apply overlays)
- **Out-of-scope components remain visible** as architectural context, not deleted

## The 5-step recipe

### 1. Copy canvas

Duplicate the full architecture file to `diagrams/3-flows/data-flow/dfd-<scope>.drawio`. Preserve every layer, component, zone, and existing edge.

```bash
cp diagrams/1-overview/<project>-architecture.drawio diagrams/3-flows/data-flow/dfd-<scope>.drawio
```

### 2. Copy DFD_LEGEND cell

Copy the reusable legend block (see template below) into the new file. Update the `► SCOPE OF THIS FILE` line to name the subsystem in scope.

### 3. Grey out non-scope cells

Run a per-DFD grey-out script (template at [`scripts/grey-out-non-scope.py`](../scripts/grey-out-non-scope.py)):

- Define `KEEP_IDS` set = in-scope subsystem cells + direct touchpoints + the legend
- Everything else: `fillColor=#f5f5f5`, `strokeColor=#bdbdbd`, `fontColor=#bdbdbd`, `strokeWidth=1`, `value=""` (text cleared)
- Preserve structural style attrs (`shape`, `container=1`, `dashed`, `rounded`, `arcSize`) — only swap color properties

### 4. Add process-number prefix

To in-scope component labels, prepend Yourdon-style number (`1.0`, `2.0`, …) before the existing component ID and name.

Example: `<i>MOB-2001</i> · <b>NAV Engine</b>` becomes `<b>1.0</b> · <i>MOB-2001</i><br/><b>NAV Engine</b>`

### 5. Overlay DFD edges

- **Purple dotted** for data flow (`strokeColor=#6a1b9a`, `dashPattern=2 3`) with noun labels
- **Red dashed** for prohibited paths (`strokeColor=#c62828`, `dashPattern=5 5`) labeled `[X] PROHIBITED · (named RT)`
- **`TRIGGER:` prefix** on labels of edges that initiate process execution

## What counts as "in scope" for KEEP_IDS

- The subsystem container itself
- All subsystem components (e.g. all MOB-2xxx for a Survival Core DFD)
- **Direct touchpoints** the subsystem reads/writes:
  - Data stores it accesses
  - External entities it consumes from
  - External entities it produces to (rare — most Core outputs are local-only)
  - Background-sync sources that legitimately feed in-scope stores
- Architecture barriers / boundaries that frame the subsystem
- The `DFD_LEGEND` cell

Everything else → grey + empty.

## DFD overlay legend (reusable template)

Copy this block into every DFD `.drawio` file. Update the `► SCOPE OF THIS FILE` line.

```
━━━ DFD OVERLAY LEGEND ━━━
Template convention for all Tier-3 data-flow diagrams (3-flows/data-flow/).

► CANVAS PRINCIPLE
This DFD uses the full master architecture as visual canvas (every layer,
component, zone preserved 1:1). Do NOT modify architecture cells —
only add overlays on top.

► SCOPE OF THIS FILE
<Subsystem name> (<SPEC-ID>) · processes 1.0–N.0 mapped to <COMPONENT-ID-RANGE>.
Out-of-scope components stay rendered as context but receive no DFD overlay.

► OVERLAYS ADDED ON TOP OF CANVAS
  • Process number prefix — Yourdon-style numbering (1.0, 2.0…) prepended to in-scope components
  • Data-flow edges — purple dotted (strokeColor=#6a1b9a, dashPattern=2 3) with NOUN labels
  • Prohibited paths — red dashed (strokeColor=#c62828, dashPattern=5 5) labeled [X] PROHIBITED + named RT
  • Control/operational edges — solid grey/black with VERB labels

► EDGE LABEL CONVENTIONS
  • TRIGGER: prefix = event that initiates the destination process
  • Bold = primary noun/verb · Italic = context (timing · constraint · classification)

► WHEN TO USE THIS TEMPLATE
Each subsystem needing data-flow visualisation gets its own DFD .drawio file
in 3-flows/data-flow/. Steps: (1) copy canvas, (2) copy legend, (3) update
SCOPE line, (4) add process numbers, (5) overlay edges.

► CROSS-REFS
Master: ../../1-overview/<project>-architecture.drawio
Narrative: ./dfd-<scope>.md
Style guide: ../../../CLAUDE.md
```

## Reusable script pattern

Each DFD gets its own grey-out script at `.scripts/grey-out-non-<scope>.py`. The script:

- Reads the target `.drawio`
- Defines `KEEP_IDS` set (numeric cell IDs as strings + named IDs like `DFD_LEGEND`)
- Iterates `ALL_CELL_IDS` (numeric range covering the architecture cells)
- For each non-KEEP cell: rewrites style via `restyle_to_grey()` helper and clears `value=""`
- Prints `GREYED OUT / KEPT` counts for verification

Full template: [`scripts/grey-out-non-scope.py`](../scripts/grey-out-non-scope.py).

## Why this convention exists

- **Cross-mapping**: vendors open master + DFD side-by-side, same cell positions = trivial comparison
- **Overlay readability**: greyed-out out-of-scope cells provide architectural context without competing visually with DFD overlays
- **Maintainability**: re-runs of grey-out scripts handle architecture changes idempotently
- **Separation of concerns**: structural changes happen in master architecture; behavioral views live in their own files but stay visually anchored

## Companion `.md` narrative

Each DFD `.drawio` has a matching `dfd-<scope>.md` file with:

- Notation explanation (Yourdon shapes · edge styles · TRIGGER prefix)
- Mermaid version of the DFD (for markdown rendering)
- **Process catalogue table** (# · Process · TRIGGER · Inputs · Outputs · Stores)
- **Trigger inventory** (what causes each process to run)
- **Storage tech mapping** (logical → physical)
- **Process independence/dependency map** (which processes are independent vs coupled)
- **Architectural constraints visualised** (compliance bullets)
- **Cross-references** to master, subsystem deep-dive, compliance matrix
