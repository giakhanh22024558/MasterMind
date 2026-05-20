"""
Atomically insert a new mxCell (component, store, etc.) into a Drawio file's
parent container.

USE CASE:
  - Adding a new component/store mandated by a spec audit
  - Adding a provisional cylinder for a not-yet-confirmed schema
  - Adding a placeholder cell to flag a future-phase feature

WHY ATOMIC:
  Single read + write to minimize the window for cloud-sync races.

CONFIGURATION:
  Edit the constants below:
    DRAWIO        — path to the target .drawio file
    PARENT_ID     — id of the container the new cell goes inside (e.g. "MOB_DATA" or "65")
    INSERT_AFTER  — id of a sibling cell to insert after (or "" to insert before </root>)
    NEW_CELL_*    — new cell's id, value (HTML-escaped), style, geometry

  Set STYLE to PROVISIONAL_STYLE for "preemptive · pending confirmation" cells.
"""
import re
from pathlib import Path

# ─── EDIT THESE ───────────────────────────────────────────────────────────────

DRAWIO = Path(r"<absolute path to your .drawio>")

# Parent container the new cell is placed inside (e.g. "STORE_GROUP" or numeric)
PARENT_ID = "<parent-cell-id>"

# Insert immediately after this sibling. Leave empty to insert before </root>
# at the end of the diagram.
INSERT_AFTER = "<sibling-cell-id-or-empty>"

# New cell properties
NEW_CELL_ID = "<new-cell-id>"
NEW_CELL_VALUE = (
    "&lt;i&gt;<spec-id>&lt;/i&gt; &#183; &lt;b&gt;<component name>&lt;/b&gt;"
)

# Pick one of the style presets below (or write your own):

# ── Storage cylinder (purple, local-only) ─────────────────────────────────────
CYLINDER_LOCAL_STYLE = (
    "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=10;"
    "fillColor=#ffffff;strokeColor=#6a1b9a;strokeWidth=1.5;"
    "dashed=1;dashPattern=3 2;fontSize=10;spacing=5;"
)

# ── Storage cylinder (blue, cloud / SDK-native) ───────────────────────────────
CYLINDER_CLOUD_STYLE = (
    "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=10;"
    "fillColor=#ffffff;strokeColor=#1976d2;strokeWidth=1.5;fontSize=10;spacing=5;"
)

# ── Component box (white rounded · grey stroke) ───────────────────────────────
COMPONENT_BOX_STYLE = (
    "rounded=1;arcSize=80;whiteSpace=wrap;html=1;"
    "fillColor=#ffffff;strokeColor=#555555;strokeWidth=1;fontSize=10;spacing=5;"
)

# ── PROVISIONAL — pending client/spec confirmation ────────────────────────────
# Use this style when you're preemptively adding a cell but the design choice
# is not yet locked in. Vendor sees the warning style and knows to confirm.
PROVISIONAL_STYLE = (
    "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=10;"
    "fillColor=#fff8e1;"             # pale amber
    "strokeColor=#f57c00;"           # orange (warning)
    "strokeWidth=1.5;"
    "dashed=1;dashPattern=6 3;"
    "fontSize=10;spacing=5;"
    "fontColor=#e65100;"
)

NEW_CELL_STYLE = COMPONENT_BOX_STYLE  # ← change as needed

# Geometry: x, y, width, height (relative to parent container)
NEW_CELL_X = 15
NEW_CELL_Y = 50
NEW_CELL_W = 165
NEW_CELL_H = 80

# ─── EXECUTION ────────────────────────────────────────────────────────────────

content = DRAWIO.read_text(encoding="utf-8")

new_cell_xml = (
    f'                <mxCell id="{NEW_CELL_ID}" value="{NEW_CELL_VALUE}" '
    f'style="{NEW_CELL_STYLE}" vertex="1" parent="{PARENT_ID}">\n'
    f'                    <mxGeometry x="{NEW_CELL_X}" y="{NEW_CELL_Y}" '
    f'width="{NEW_CELL_W}" height="{NEW_CELL_H}" as="geometry"/>\n'
    f'                </mxCell>\n'
)

if INSERT_AFTER:
    # Insert right after the specified sibling cell's closing </mxCell>
    sibling_pattern = re.compile(
        r'(<mxCell id="' + re.escape(INSERT_AFTER) + r'"[^>]*>\s*'
        r'<mxGeometry[^/]*?(?:/>|>.*?</mxGeometry>)\s*'
        r'</mxCell>)',
        re.DOTALL,
    )
    new_content, n = sibling_pattern.subn(r'\g<1>\n' + new_cell_xml, content, count=1)
    if n == 0:
        raise SystemExit(f"Sibling cell id={INSERT_AFTER!r} not found")
else:
    # Insert before </root> (works if file has one diagram; for multi-page,
    # match the specific diagram's closing tag instead)
    root_close = content.rfind('</root>')
    if root_close == -1:
        raise SystemExit("</root> not found")
    new_content = content[:root_close] + new_cell_xml + content[root_close:]
    n = 1

DRAWIO.write_text(new_content, encoding="utf-8")
print(f"Inserted {n} new cell (id={NEW_CELL_ID}) into parent={PARENT_ID}")
