# Architecture sub-skill · scripts

Layout calculation + Drawio edit helpers specific to architecture diagrams. For diagram-type-agnostic scripts (cell updates, cell insertion, edge revert), see [`_shared/scripts`](../../../../../../core/diagram/_shared/scripts/).

## Available scripts

| Script | Purpose |
|---|---|
| [`compute-row-layout.py`](compute-row-layout.py) | Pure calculation · given container width + cell count + gap → returns cell width and x positions. Useful for planning before applying. No Drawio file edits. |
| [`align-cells-in-row.py`](align-cells-in-row.py) | Re-align existing cells in a row to share uniform width + spacing. Atomic Drawio edit. Re-runnable. |
| [`add-edge.py`](add-edge.py) | Insert a new edge with one of 5 style presets (solid operational · bidirectional · dotted purple data · red prohibited · orange consent-gated). Idempotency check optional. |
| [`resize-container-to-fit.py`](resize-container-to-fit.py) | Auto-resize a zone/sub-zone container to encompass all its children + padding. Useful after inserting new cells. |

## When to use which script

| Scenario | Script |
|---|---|
| "Plan layout · how wide should cells be in a 720w row of 5?" | `compute-row-layout.py` |
| "I added a 5th cell to a row that had 4 · the existing ones now overlap" | `align-cells-in-row.py` |
| "Spec audit revealed a new relationship · add an edge between component A and B" | `add-edge.py` |
| "Inserted a new component into zone X · zone container is too small now" | `resize-container-to-fit.py` |

## Generic shared scripts (for any diagram type)

When you need:

- Atomic update of a cell's display label → `update-cell-value.py` in [`_shared/scripts`](../../../../../../core/diagram/_shared/scripts/)
- Atomic insertion of a new cell → `add-cell.py` in [`_shared/scripts`](../../../../../../core/diagram/_shared/scripts/)
- Rollback a batch of edges → `revert-edges.py` in [`_shared/scripts`](../../../../../../core/diagram/_shared/scripts/)

## Pattern · combining scripts

A typical "add a new component" workflow uses multiple scripts:

```
1. compute-row-layout.py     → plan the new layout (paper exercise)
2. add-cell.py               → insert the new component cell
3. align-cells-in-row.py     → re-align existing siblings to share space
4. resize-container-to-fit.py → ensure parent container fits the new bounds
5. add-edge.py               → wire up any new relationships involving the new cell
```

Each step is a separate atomic write — safer than one mega-script when iterating.

## Common conventions

All scripts in this folder:

- **Single read · single write** pattern (atomic edits)
- **Idempotent re-run** where possible (or include `SKIP_IF_EXISTS` check)
- **CONFIG block at top** — edit values, don't touch logic
- **Drawio path as `Path(r"...")`** — supports Windows backslashes via raw string
- **UTF-8 encoding** for read/write
- **Verify after running** via grep or visual inspection

See [`atomic-edits-pattern`](../../../../../../core/diagram/_shared/atomic-edits-pattern/) for the broader pattern.

## Adapting templates to your project

Each script has a `CONFIG` block at the top. Replace placeholders:

- `<absolute path to your .drawio>` → actual file path
- `<cell-id>` → your project's actual cell IDs (numeric or named per project convention)
- `<container-cell-id>` → ID of the zone/container cell

If you find yourself running the same script with similar config repeatedly, **copy it to your project's `.scripts/` folder** with a descriptive name and the config pre-filled. The template stays here as a reference.
