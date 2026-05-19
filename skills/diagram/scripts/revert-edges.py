"""
Roll back a batch of edges in a Drawio file by deleting them and (optionally)
restoring previous edges that were replaced.

USE CASE:
  - Architecture experiment didn't work · revert to prior state
  - User asked to undo a previous batch of edge additions
  - Spec clarification changed the architectural choice · roll back preemptive commit

WHY PAIRED WITH WIRING SCRIPTS:
  Pair this script with the corresponding "wire-..." script that originally
  added the edges. Together they form a reversible pair · re-running either
  recovers from cloud-sync races.

CONFIGURATION:
  Edit the constants below:
    DRAWIO             — path to the target .drawio file
    DELETE_EDGE_IDS    — list of edge IDs to remove
    RESTORE_EDGES      — list of (id, value, source, target) tuples to add back
    EDGE_STYLE         — Drawio style string for restored edges

  If RESTORE_EDGES is empty, this script only deletes.
"""
import re
from pathlib import Path

# ─── EDIT THESE ───────────────────────────────────────────────────────────────

DRAWIO = Path(r"<absolute path to your .drawio>")

# Edge IDs to delete from the Drawio file
DELETE_EDGE_IDS = [
    # "e_layer_a_to_store_x",
    # "e_layer_b_to_store_y",
]

# Edge style for restored edges (purple dotted data-flow, default)
PURPLE_DATA_STYLE = (
    'style="endArrow=classic;html=1;edgeStyle=orthogonalEdgeStyle;'
    'rounded=0;jettySize=auto;orthogonalLoop=1;dashed=1;dashPattern=2 3;'
    'strokeColor=#6a1b9a;strokeWidth=2;fontColor=#6a1b9a;fontSize=11;'
    'labelBackgroundColor=#ffffff;"'
)

# Solid grey operational edge style (alternative)
SOLID_GREY_STYLE = (
    'style="endArrow=classic;html=1;edgeStyle=orthogonalEdgeStyle;'
    'rounded=0;jettySize=auto;orthogonalLoop=1;strokeColor=#555555;'
    'strokeWidth=1.5;fontSize=11;labelBackgroundColor=#ffffff;"'
)

# Edges to restore (added back after deletion)
# Tuples: (edge_id, value_html_escaped, source_cell_id, target_cell_id, style)
RESTORE_EDGES = [
    # ("e_layer_to_store_group",
    #  "&lt;b&gt;R/W data&lt;/b&gt;",
    #  "LAYER_A", "STORE_GROUP", SOLID_GREY_STYLE),
]

# Diagram-specific anchor for inserting restored edges (before </root>)
# Edit the regex if your file has multiple <diagram> pages.
DIAGRAM_ROOT_ANCHOR = r'<diagram id="[^"]*"'

# ─── EXECUTION ────────────────────────────────────────────────────────────────

content = DRAWIO.read_text(encoding="utf-8")

# Step 1 — delete edges
deleted = 0
for eid in DELETE_EDGE_IDS:
    pattern = re.compile(
        r'\s*<mxCell id="' + re.escape(eid) + r'"[^>]*?>\s*'
        r'<mxGeometry[^/]*?(?:/>|>.*?</mxGeometry>)\s*'
        r'</mxCell>',
        re.DOTALL,
    )
    new_content, n = pattern.subn("", content)
    if n:
        content = new_content
        deleted += n
    else:
        print(f"  WARN: edge id={eid!r} not found (may already be removed)")

# Step 2 — insert restored edges before </root> of the first diagram
if RESTORE_EDGES:
    diagram_start = content.find('<diagram id=')
    if diagram_start == -1:
        diagram_start = 0
    diagram_end = content.find('</diagram>', diagram_start)
    if diagram_end == -1:
        diagram_end = len(content)
    root_close = content.rfind('</root>', diagram_start, diagram_end)
    if root_close == -1:
        raise SystemExit("</root> not found in diagram")

    restored_xml = ""
    for eid, value, src, tgt, style in RESTORE_EDGES:
        restored_xml += (
            f'                <mxCell id="{eid}" value="{value}" '
            f'{style} parent="1" source="{src}" target="{tgt}" edge="1">\n'
            f'                    <mxGeometry relative="1" as="geometry"/>\n'
            f'                </mxCell>\n'
        )

    content = content[:root_close] + restored_xml + content[root_close:]

DRAWIO.write_text(content, encoding="utf-8")

print(f"DELETED {deleted}/{len(DELETE_EDGE_IDS)} edges")
print(f"RESTORED {len(RESTORE_EDGES)} edges")
