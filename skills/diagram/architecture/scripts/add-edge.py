"""
Atomically insert a new edge (mxCell with edge="1") into a Drawio file.

USE CASE:
  - Adding a new architecture relationship after a spec audit reveals it
  - Wiring up data-flow / control-flow / prohibited edges between cells
  - Batch-adding several edges in one atomic write

WHY ATOMIC:
  Single read · single write · survives cloud-sync races. Re-runnable
  (the script can check for existing edge ID before inserting).

CONFIGURATION:
  Edit the CONFIG block:
    DRAWIO         — path to the target .drawio file
    EDGE_ID        — new edge's mxCell id (must be unique)
    EDGE_VALUE     — HTML-escaped label content
    EDGE_STYLE     — Drawio style string (pick a preset below)
    SOURCE         — source cell id
    TARGET         — target cell id

  Pick a STYLE preset:
    SOLID_OPERATIONAL_STYLE — solid grey, verb-form label
    DOTTED_PURPLE_STYLE     — data-payload edge, noun-form label
    RED_PROHIBITED_STYLE    — prohibited path
    ORANGE_CONSENT_STYLE    — consent-gated / conditional
"""
import re
from pathlib import Path

# ─── CONFIG ────────────────────────────────────────────────────────────────────

DRAWIO = Path(r"<absolute path to your .drawio>")

EDGE_ID = "<unique-edge-id>"
EDGE_VALUE = (
    "&lt;b&gt;Verb action&lt;/b&gt;&lt;br/&gt;"
    "&lt;i&gt;(<reference-id> &#183; <characterization>)&lt;/i&gt;"
)
SOURCE = "<source-cell-id>"
TARGET = "<target-cell-id>"

# ─── EDGE STYLE PRESETS ───────────────────────────────────────────────────────

SOLID_OPERATIONAL_STYLE = (
    'style="endArrow=classic;html=1;edgeStyle=orthogonalEdgeStyle;'
    'rounded=0;jettySize=auto;orthogonalLoop=1;strokeColor=#555555;'
    'strokeWidth=1.5;fontSize=11;labelBackgroundColor=#ffffff;"'
)

SOLID_BIDIRECTIONAL_STYLE = (
    'style="endArrow=classic;startArrow=classic;html=1;'
    'edgeStyle=orthogonalEdgeStyle;rounded=0;jettySize=auto;orthogonalLoop=1;'
    'strokeColor=#555555;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#ffffff;"'
)

DOTTED_PURPLE_STYLE = (
    'style="endArrow=classic;html=1;edgeStyle=orthogonalEdgeStyle;'
    'rounded=0;jettySize=auto;orthogonalLoop=1;dashed=1;dashPattern=2 3;'
    'strokeColor=#6a1b9a;strokeWidth=2;fontColor=#6a1b9a;fontSize=11;'
    'labelBackgroundColor=#ffffff;"'
)

RED_PROHIBITED_STYLE = (
    'style="endArrow=classic;html=1;edgeStyle=orthogonalEdgeStyle;'
    'rounded=0;jettySize=auto;orthogonalLoop=1;dashed=1;dashPattern=5 5;'
    'strokeColor=#c62828;strokeWidth=2;fontColor=#c62828;fontSize=10;'
    'labelBackgroundColor=#ffffff;"'
)

ORANGE_CONSENT_STYLE = (
    'style="endArrow=classic;html=1;edgeStyle=orthogonalEdgeStyle;'
    'rounded=0;jettySize=auto;orthogonalLoop=1;dashed=1;dashPattern=5 3;'
    'strokeColor=#f57c00;strokeWidth=2;fontColor=#e65100;fontSize=10;'
    'labelBackgroundColor=#ffffff;"'
)

EDGE_STYLE = SOLID_OPERATIONAL_STYLE   # ← change per use case

# Idempotency: skip insertion if edge already exists
SKIP_IF_EXISTS = True


# ─── EXECUTION ────────────────────────────────────────────────────────────────

content = DRAWIO.read_text(encoding="utf-8")

if SKIP_IF_EXISTS and re.search(r'<mxCell id="' + re.escape(EDGE_ID) + r'"', content):
    print(f"Edge id={EDGE_ID!r} already exists · skipping insertion (idempotent re-run)")
    raise SystemExit(0)

# Find </root> of the first diagram (or all-diagram fallback)
# For multi-page Drawio · adjust to the target diagram's </root>
root_close = content.rfind('</root>')
if root_close == -1:
    raise SystemExit("</root> not found")

new_edge_xml = (
    f'                <mxCell id="{EDGE_ID}" value="{EDGE_VALUE}" '
    f'{EDGE_STYLE} parent="1" source="{SOURCE}" target="{TARGET}" edge="1">\n'
    f'                    <mxGeometry relative="1" as="geometry"/>\n'
    f'                </mxCell>\n'
)

new_content = content[:root_close] + new_edge_xml + content[root_close:]
DRAWIO.write_text(new_content, encoding="utf-8")
print(f"Inserted edge id={EDGE_ID} : {SOURCE} → {TARGET}")
