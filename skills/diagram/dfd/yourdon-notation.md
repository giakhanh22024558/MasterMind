# Yourdon DFD notation

Quick reference for the four core DFD elements. Projects may customize the visual representation (see [`conventions-schema.md`](conventions-schema.md)) — what stays constant is the **conceptual model**.

## The four DFD elements

### 1 · Process (active behavior)

**What it is:** A unit of work that transforms inputs into outputs. Has a number (Yourdon `N.M`) and a name (verb-phrase ideal).

**Classical Yourdon shape:** Circle / bubble.

**This skill's default:** Rounded box (matching architecture component cells) for visual cross-mapping with the master diagram.

**Mermaid:** `((Process name))` (circle) or `[Process name]` (rounded box) depending on convention chosen.

**Drawio:** `shape=ellipse` (circle) or `rounded=1;arcSize=80` (rounded box).

### 2 · Data store (passive state)

**What it is:** A place where data persists between processes — a database, file, queue, in-memory cache.

**Classical Yourdon shape:** Open rectangle (two horizontal lines bracketing the name).

**This skill's default:** Cylinder (matching architecture's storage cells).

**Mermaid:** `[(Store name)]` (cylinder shape).

**Drawio:** `shape=cylinder3`.

### 3 · External entity (boundary actor)

**What it is:** A source or sink outside the system being modeled — a user, an external system, a hardware sensor.

**Classical Yourdon shape:** Rectangle (or square).

**This skill's default:** Rounded box in the external zone color (matching architecture's external entity cells).

**Mermaid:** `[Entity name]` (rectangle).

**Drawio:** Rectangle with external-zone-style fill (peach color by default).

### 4 · Data flow (relationship)

**What it is:** Movement of data from one element to another. Has a direction and a **payload label** (noun phrase — what's flowing, not what action is happening).

**Classical Yourdon shape:** Arrow with payload label.

**This skill's default:** Dotted purple arrow (`stroke-dasharray:2 3`, `strokeColor=#6a1b9a`) with noun label · matching architecture's data-payload edge style.

**Mermaid:** `A -.->|"<b>payload</b>"| B` (dashed arrow with bold noun label).

## Process numbering rules

- Top-level processes: `1.0`, `2.0`, `3.0`, …
- Sub-processes within a parent: `2.1`, `2.2`, … (decomposition)
- Sub-sub-processes: `2.1.1`, `2.1.2`, … (rare in practice)

Numbering is sequential per DFD scope · doesn't need to match component IDs. Same component can have a different process number in different DFDs.

## Data flow label rules

Labels on data-flow edges are **nouns** (the payload name) — not verbs.

| ✅ Good (noun) | ❌ Bad (verb) |
|---|---|
| `Vector tiles` | `Writes tiles` |
| `Position fix` | `Sends position` |
| `Hazard records` | `Pushes hazards` |
| `Reverse path` | `Calculates path` |

The arrow already conveys direction · the label names what's flowing.

**Exception:** `TRIGGER:` prefix on edges that initiate the destination process. The prefix is allowed even though "TRIGGER" itself is action-ish, because it's a *meta-label* about the edge's purpose.

## Naming conventions

- **Process names:** verb-phrase ideal (`Calculate route`, `Render map`) but noun phrases acceptable (`Navigation Engine`, `Trail Recorder`) — match project convention
- **Data stores:** noun, often plural (`breadcrumb_log`, `anchor_points`)
- **External entities:** noun (`User`, `GNSS Sensor`, `Cloud Sync`)
- **Data flows:** noun payload (`position_fix(lat,lon,ts)`, `hazard_overlay`)

## Conventions vs classical Yourdon

Classical Yourdon DFDs use specific shapes (circle for process, open rectangle for store, square for entity). This skill **prefers visual consistency with the architecture canvas** over classical-shape orthodoxy — because the canvas-overlay method requires DFDs to map 1:1 with the master diagram.

If your project wants classical Yourdon shapes (for textbook compliance or vendor familiarity), document that choice in `diagram-conventions.md` and the sub-skill will apply your shapes.

## Multi-level DFDs (context · level-0 · level-1 · …)

Classical DFDs come in levels:
- **Context diagram (level 0)** — the whole system as one process · only external entities visible
- **Level-1 DFD** — top-level decomposition · processes `1.0`, `2.0`, …
- **Level-N DFD** — further decomposition of a single process

This skill's **canvas-overlay method** typically targets **one DFD per subsystem** at a single level. If you need multi-level DFDs:

- Multiple files: `dfd-<subsystem>-level-0.drawio`, `dfd-<subsystem>-level-1.drawio`, …
- Sub-process numbering: `2.1`, `2.2`, … inside the level-1 DFD for process `2.0`
- Each level still overlays the master canvas (process zoom isn't done by stripping context)

## What DFDs are NOT for

- ❌ Showing control flow (use a sequence or state diagram instead)
- ❌ Showing how processes are deployed (use the architecture diagram)
- ❌ Showing data schemas in detail (use an ERD)
- ❌ Showing timing or performance (use a sequence diagram or performance-targets doc)

DFDs answer: **what data exists, where it lives, where it flows, who triggers what**. Other concerns belong elsewhere.
