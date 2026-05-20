"""
Re-align existing cells in a row so they share uniform width and gap.

USE CASE:
  - You added a new cell to a row · now the existing N cells overlap or have
    irregular gaps
  - Want all cells in the row to have the same width + uniform spacing
  - This script atomically updates the geometry of each named cell

WHY ATOMIC:
  Single read + write to the Drawio file · survives cloud-sync races.
  Re-runnable (idempotent) — running twice produces the same positions.

CONFIGURATION:
  Edit the CONFIG block:
    DRAWIO            — path to the target .drawio file
    PARENT_WIDTH      — inner width of the parent container (for layout calc)
    CELL_IDS          — ordered list of cell IDs to align (left → right)
    GAP, PADDING_L/R  — layout parameters
    Y, HEIGHT         — y position and height (assumed uniform across the row)
"""
import re
from pathlib import Path


# ─── CONFIG ────────────────────────────────────────────────────────────────────

DRAWIO = Path(r"<absolute path to your .drawio>")

PARENT_WIDTH = 720
GAP = 15
PADDING_LEFT = 15
PADDING_RIGHT = 15

# Cells to align, in left-to-right order
CELL_IDS = [
    # "cell_id_1",
    # "cell_id_2",
    # "cell_id_3",
]

# Common y and height (these don't change · only x and width get updated)
Y = 50
HEIGHT = 80


# ─── LOGIC ─────────────────────────────────────────────────────────────────────

def compute_positions(container_width, cell_count, gap, padding_l, padding_r):
    available = container_width - padding_l - padding_r
    total_gap = (cell_count - 1) * gap
    cell_width = int((available - total_gap) / cell_count)
    positions = [padding_l + i * (cell_width + gap) for i in range(cell_count)]
    return cell_width, positions


if __name__ == "__main__":
    if not CELL_IDS:
        raise SystemExit("CELL_IDS is empty — fill in the list of cells to align")

    cell_width, positions = compute_positions(
        PARENT_WIDTH, len(CELL_IDS), GAP, PADDING_LEFT, PADDING_RIGHT
    )

    print(f"Computed cell width: {cell_width}")
    print(f"Positions: {positions}")
    print(f"Updating {len(CELL_IDS)} cells in {DRAWIO}...")

    content = DRAWIO.read_text(encoding="utf-8")
    updated = 0

    for i, cell_id in enumerate(CELL_IDS):
        x = positions[i]
        # Match this cell's mxGeometry · replace x, y, width, height
        pattern = re.compile(
            r'(<mxCell id="' + re.escape(cell_id) + r'"[^>]*>\s*'
            r'<mxGeometry )x="\d+" y="\d+" width="\d+" height="\d+"([^/]*/>)'
        )
        replacement = rf'\g<1>x="{x}" y="{Y}" width="{cell_width}" height="{HEIGHT}"\g<2>'
        new_content, n = pattern.subn(replacement, content)
        if n == 0:
            print(f"  WARN: cell {cell_id} geometry not found · skipping")
        else:
            content = new_content
            updated += n

    DRAWIO.write_text(content, encoding="utf-8")
    print(f"Aligned {updated}/{len(CELL_IDS)} cells")
