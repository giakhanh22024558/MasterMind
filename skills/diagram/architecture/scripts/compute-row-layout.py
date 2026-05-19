"""
Compute uniform cell positions for a horizontal row inside a container.

USE CASE:
  - Architecture row with N components (e.g. 5 features side-by-side)
  - Want all cells same width · uniform gap · left/right padding
  - Need exact x positions to insert via add-cell.py or set via update-cell-geometry

INPUT:
  container_width (int)   — inner width of the parent container
  cell_count (int)        — how many cells to fit
  gap (int)               — gap between adjacent cells (default 15)
  padding_left (int)      — left padding (default 15)
  padding_right (int)     — right padding (default 15)

OUTPUT:
  cell_width (int)        — computed width per cell (fills available space)
  positions: list[int]    — x position for each cell (cell index 0..N-1)

FORMULA:
  available = container_width - padding_left - padding_right
  cell_width = (available - (cell_count - 1) * gap) / cell_count
  positions[i] = padding_left + i * (cell_width + gap)

USAGE:
  python compute-row-layout.py
  → prints cell_width + x positions

EDIT the CONFIG block below for your specific row.
"""
from dataclasses import dataclass


# ─── CONFIG ────────────────────────────────────────────────────────────────────

CONTAINER_WIDTH = 720   # inner width of the parent container
CELL_COUNT = 5          # number of cells in this row
GAP = 15                # gap between adjacent cells
PADDING_LEFT = 15       # left padding inside container
PADDING_RIGHT = 15      # right padding inside container

# Optional: enforce integer cell width (truncate fractional pixels)
INTEGER_WIDTH = True


# ─── LOGIC ─────────────────────────────────────────────────────────────────────

@dataclass
class RowLayout:
    cell_width: int
    positions: list[int]
    leftover: int      # leftover pixels after rounding (distributed as right slack)


def compute_row_layout(
    container_width: int,
    cell_count: int,
    gap: int = 15,
    padding_left: int = 15,
    padding_right: int = 15,
    integer_width: bool = True,
) -> RowLayout:
    if cell_count <= 0:
        raise ValueError("cell_count must be >= 1")

    available = container_width - padding_left - padding_right
    total_gap = (cell_count - 1) * gap
    width_per_cell_raw = (available - total_gap) / cell_count

    if width_per_cell_raw < 1:
        raise ValueError(
            f"Not enough room: container_width={container_width}, "
            f"cell_count={cell_count}, gap={gap}, padding={padding_left}+{padding_right}"
        )

    if integer_width:
        cell_width = int(width_per_cell_raw)
    else:
        cell_width = width_per_cell_raw

    positions = [padding_left + i * (cell_width + gap) for i in range(cell_count)]
    used = padding_left + cell_count * cell_width + (cell_count - 1) * gap + padding_right
    leftover = container_width - used

    return RowLayout(cell_width=cell_width, positions=positions, leftover=leftover)


if __name__ == "__main__":
    layout = compute_row_layout(
        container_width=CONTAINER_WIDTH,
        cell_count=CELL_COUNT,
        gap=GAP,
        padding_left=PADDING_LEFT,
        padding_right=PADDING_RIGHT,
        integer_width=INTEGER_WIDTH,
    )

    print(f"Container width : {CONTAINER_WIDTH}")
    print(f"Cell count      : {CELL_COUNT}")
    print(f"Gap             : {GAP}")
    print(f"Padding L/R     : {PADDING_LEFT} / {PADDING_RIGHT}")
    print(f"")
    print(f"Cell width      : {layout.cell_width}")
    print(f"Right slack     : {layout.leftover} px")
    print(f"")
    print(f"Positions (x):")
    for i, x in enumerate(layout.positions):
        end_x = x + layout.cell_width
        print(f"  cell {i+1}: x={x}, ends at x={end_x}")
