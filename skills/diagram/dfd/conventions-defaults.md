# DFD · conventions defaults

Default conventions applied by the DFD sub-skill when a project hasn't specified its own. **Project conventions** in `<project-root>/diagram-conventions.md` always override these defaults.

## Yourdon notation defaults

For visual consistency with the master architecture canvas (canvas-overlay method), DFDs reuse architecture's shapes rather than classical Yourdon:

| Element | Classical Yourdon | Default in this skill | Why |
|---|---|---|---|
| Process | Circle | **Rounded box** (matching architecture component cells) | Visual cross-mapping with master |
| Data store | Open rectangle / cylinder | **Cylinder** (matching architecture storage cells) | Same as architecture |
| External entity | Rectangle | **Rounded box** in external zone color | Same as architecture |
| Data flow | Arrow | **Dotted purple arrow** (`stroke-dasharray:2 3`) | Matches architecture data-payload edges |

Projects may choose classical Yourdon shapes if they prefer (e.g. circles for processes) — document choice in `diagram-conventions.md`.

## Process numbering default

Yourdon `N.M` numbering, prepended to component labels:

```
<b>1.0</b> · <i><Component-ID></i> · <b><Component Name></b>
```

Examples:
- `<b>1.0</b> · <i>MOD-2001</i> · <b>Navigation Engine</b>`
- `<b>2.0</b> · <i>MOD-2002</i> · <b>Trail Recorder</b>`

Sub-processes use `N.M.K` (e.g. `2.1`, `2.2` for sub-processes of process 2).

## Edge styles default

| Edge type | Style |
|---|---|
| Data flow | `endArrow=classic;edgeStyle=orthogonalEdgeStyle;dashed=1;dashPattern=2 3;strokeColor=#6a1b9a;strokeWidth=2;fontColor=#6a1b9a;fontSize=11` |
| Trigger flow | Same as data flow + `TRIGGER:` prefix on label |
| Prohibited flow | `dashed=1;dashPattern=5 5;strokeColor=#c62828;strokeWidth=2;fontColor=#c62828` + label `[X] PROHIBITED ...` |

## Grey-out style for out-of-scope cells

| Property | Default value |
|---|---|
| `fillColor` | `#f5f5f5` |
| `strokeColor` | `#bdbdbd` |
| `strokeWidth` | `1` |
| `fontColor` | `#bdbdbd` |
| `value` | `""` (empty string) |

Structural properties preserved (not modified by grey-out):
- `shape` (cylinder, line, ellipse, etc.)
- `container` (whether the cell holds children)
- `dashed`, `dashPattern` (border style)
- `rounded`, `arcSize`
- `verticalAlign`, `align`

See [`scripts/grey-out-non-scope.py`](scripts/grey-out-non-scope.py) for the implementation.

## DFD legend block default

Every DFD `.drawio` includes a legend cell at the bottom (full-width banner):

```
fillColor=#fafafa
strokeColor=#616161
strokeWidth=1.5
dashed=1; dashPattern=5 3
```

Content sections (replace project-specifics with your values):

```
━━━ DFD OVERLAY LEGEND ━━━
Template convention for all Tier-3 data-flow diagrams (3-flows/data-flow/).

► CANVAS PRINCIPLE
This DFD uses the full master architecture as visual canvas. All layers,
components, zones preserved 1:1 from <master-architecture-file>.drawio.
Do NOT modify architecture cells — only add overlays on top.

► SCOPE OF THIS FILE
<Subsystem name> (<SPEC-ID>) · processes 1.0–N.0 mapped to <COMPONENT-ID-RANGE>.
Out-of-scope components stay rendered as context but receive no DFD overlay.

► OVERLAYS ADDED ON TOP OF CANVAS
  • Process number prefix — Yourdon-style numbering prepended to in-scope components
  • Data-flow edges — purple dotted (dashPattern=2 3) with NOUN labels (payload)
  • Prohibited paths — red dashed (dashPattern=5 5) labeled [X] PROHIBITED + named RT
  • Control/operational edges — solid grey/black with VERB labels (action)

► EDGE LABEL CONVENTIONS
  • TRIGGER: prefix = event that initiates the destination process
  • Bold <b> = primary noun/verb · Italic <i> = context

► WHEN TO USE THIS TEMPLATE
Each subsystem needing data-flow visualisation gets its own DFD .drawio file
in 3-flows/data-flow/.

► CROSS-REFS
Master: <path to master architecture>
Narrative: ./dfd-<scope>.md
Style guide: <project root>/diagram-conventions.md
```

## Canvas-overlay source default

If the project doesn't specify, default canvas source is:

```
diagrams/1-overview/<project>-architecture.drawio
```

## TRIGGER prefix usage default

Apply `TRIGGER:` to edges that **initiate execution** of the destination process. Not every data-flow edge.

Initiation examples (use TRIGGER):
- User action → Process (`TRIGGER: select region`)
- Sensor pulse → Process (`TRIGGER: position_fix`)
- Sibling event → Process (`TRIGGER: hazard_intersect_alert`)
- Timer tick → Process (`TRIGGER: scheduled_refresh`)

Non-initiation examples (just data-flow noun, no TRIGGER):
- Process A → Store (`writes records`)
- Process A → Process B (`current_route`)
- Process A → User (`rendered_map`)

## Companion markdown structure default

Each `dfd-<scope>.md` should include:

1. Title + scope statement
2. Notation key (shapes · edge styles · TRIGGER prefix)
3. Storage-tech mapping (logical D1-DN → physical store cylinders)
4. Mermaid version of the DFD
5. Process catalogue table (# · Process · TRIGGER · Inputs · Outputs · Stores)
6. Trigger inventory (what causes each process to run · grouped by type)
7. Process independence/dependency map (which processes are independent vs coupled)
8. Architectural constraints visualised (compliance bullets + ❌/✅ icons)
9. Cross-references (master · subsystem doc · compliance matrix · perf targets · design decisions)
