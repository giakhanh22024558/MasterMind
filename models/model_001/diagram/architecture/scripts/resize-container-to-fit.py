"""
Auto-resize a parent container in a Drawio file to encompass its children
plus uniform padding.

USE CASE:
  - After inserting new cells into a zone container · the container's old
    width/height no longer fits the new content
  - Compute the bounding box of all children · add padding · update parent

WHY ATOMIC:
  Single read · single write. Idempotent (re-running with same children
  produces same result).

CONFIGURATION:
  Edit the CONFIG block:
    DRAWIO          — path to the target .drawio file
    PARENT_ID       — the container cell whose geometry will be updated
    PADDING_*       — padding around children
"""
import re
from pathlib import Path


# ─── CONFIG ────────────────────────────────────────────────────────────────────

DRAWIO = Path(r"<absolute path to your .drawio>")

PARENT_ID = "<container-cell-id>"

PADDING_TOP = 50         # extra space above first child (title area)
PADDING_BOTTOM = 15
PADDING_LEFT = 15
PADDING_RIGHT = 15


# ─── LOGIC ─────────────────────────────────────────────────────────────────────

# Match all cells whose parent="<PARENT_ID>" · extract their geometry
def find_children_geometries(content: str, parent_id: str):
    """Return list of (x, y, w, h) tuples for each child of parent_id."""
    # Pattern captures the cell's geometry block
    pattern = re.compile(
        r'<mxCell id="[^"]+"[^>]*parent="' + re.escape(parent_id) + r'"[^>]*>\s*'
        r'<mxGeometry x="(\d+)" y="(\d+)" width="(\d+)" height="(\d+)"[^/]*/>'
    )
    return [(int(m[0]), int(m[1]), int(m[2]), int(m[3])) for m in pattern.findall(content)]


def update_parent_geometry(content: str, parent_id: str, new_w: int, new_h: int) -> tuple[str, int]:
    """Update the parent's mxGeometry width and height. Returns (new_content, n_updated)."""
    pattern = re.compile(
        r'(<mxCell id="' + re.escape(parent_id) + r'"[^>]*>\s*'
        r'<mxGeometry x="\d+" y="\d+" width=")\d+(" height=")\d+("[^/]*/>)'
    )
    return pattern.subn(rf'\g<1>{new_w}\g<2>{new_h}\g<3>', content)


if __name__ == "__main__":
    content = DRAWIO.read_text(encoding="utf-8")

    children = find_children_geometries(content, PARENT_ID)
    if not children:
        raise SystemExit(f"No children found with parent={PARENT_ID!r}")

    # Compute bounding box · each child contributes (x+w, y+h) to max bound
    max_x = max(x + w for x, y, w, h in children)
    max_y = max(y + h for x, y, w, h in children)

    new_w = max_x + PADDING_RIGHT
    new_h = max_y + PADDING_BOTTOM

    print(f"Children of {PARENT_ID}: {len(children)} cells")
    print(f"Max child extent: x={max_x}, y={max_y}")
    print(f"New parent dims: width={new_w}, height={new_h}")

    new_content, n = update_parent_geometry(content, PARENT_ID, new_w, new_h)
    if n == 0:
        raise SystemExit(f"Could not find parent cell {PARENT_ID!r} geometry")

    DRAWIO.write_text(new_content, encoding="utf-8")
    print(f"Resized parent {PARENT_ID} to fit children")
