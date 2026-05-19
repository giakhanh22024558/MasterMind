"""
Grey out (+ remove text from) all cells in a Drawio file that are NOT in the
specified scope.

USE CASE:
  Building a DFD (Data Flow Diagram) overlaid on the master architecture canvas.
  Keep in-scope cells visible + textual; everything else greyed + empty so DFD
  overlays (edges, process numbers) read clearly without competing with
  out-of-scope detail.

CONFIGURATION:
  Edit the constants below for each new DFD:
    DRAWIO    — path to the target .drawio file
    KEEP_IDS  — set of cell IDs to preserve as-is (in-scope + direct touchpoints + legend)
    ALL_CELL_IDS — numeric range covering the architecture's cells (plus named IDs)

GREY STYLE APPLIED to out-of-scope cells:
  fillColor   = #f5f5f5  (very light grey)
  strokeColor = #bdbdbd
  fontColor   = #bdbdbd
  strokeWidth = 1
  value=""    (text cleared)

Other style properties (shape, container, dashed, rounded, arcSize, etc.) are
PRESERVED — only color properties are swapped.
"""
import re
from pathlib import Path

# ─── EDIT THESE PER DFD ───────────────────────────────────────────────────────

DRAWIO = Path(r"<absolute path to your dfd-<scope>.drawio>")

# In-scope cell IDs · keep these AS-IS (no grey-out, no text clear)
# Add:
#   - Numeric IDs of subsystem container + components
#   - Direct touchpoints (stores · external entities · architecture barriers)
#   - "DFD_LEGEND" (the overlay legend cell)
#   - System root IDs "0" and "1"
KEEP_IDS = {
    "0", "1",          # drawio root cells (always keep)
    "DFD_LEGEND",      # overlay legend cell

    # Add your in-scope cell IDs here, e.g.:
    # "97",            # subsystem container
    # "98", "99", ...  # subsystem components
    # "108", "110",    # stores the subsystem reads/writes
    # "113",           # hardware sensor feeding the subsystem
}

# Range of numeric IDs to iterate · adjust to cover your architecture's cells.
# IDs not in this list will not be touched (e.g. user-added decorations).
ALL_CELL_IDS = [str(i) for i in range(50, 200)] + ["DFD_LEGEND"]

# ─── GREY STYLE CONSTANTS ─────────────────────────────────────────────────────

GREY_FILL = "#f5f5f5"
GREY_STROKE = "#bdbdbd"
GREY_FONT = "#bdbdbd"


def restyle_to_grey(style: str) -> str:
    """
    Rewrite a drawio style string to grey-out colors while preserving
    structural attrs (shape · container · dashed · rounded · arcSize · etc.).
    """
    # Parse "key=value;key=value;..." into ordered dict
    parts = [p for p in style.split(";") if p]
    props = {}
    order = []
    for part in parts:
        if "=" in part:
            k, v = part.split("=", 1)
            if k not in props:
                order.append(k)
            props[k] = v
        else:
            # bare attribute (no =) — keep
            if part not in props:
                order.append(part)
            props[part] = None

    # Override color-related properties
    props["fillColor"] = GREY_FILL
    props["strokeColor"] = GREY_STROKE
    props["fontColor"] = GREY_FONT
    props["strokeWidth"] = "1"
    for k in ("fillColor", "strokeColor", "fontColor", "strokeWidth"):
        if k not in order:
            order.append(k)

    # Rebuild
    out = []
    for k in order:
        v = props[k]
        if v is None:
            out.append(k)
        else:
            out.append(f"{k}={v}")
    return ";".join(out) + ";"


def process(content: str) -> tuple[str, int, int]:
    """Returns (new_content, n_greyed, n_kept)."""
    n_greyed = 0
    n_kept = 0

    for cid in ALL_CELL_IDS:
        # Match the opening <mxCell ...> tag for this id (value + style only)
        pattern = re.compile(
            r'(<mxCell id="' + re.escape(cid) + r'") value="[^"]*" style="([^"]*)"'
        )
        m = pattern.search(content)
        if not m:
            continue

        if cid in KEEP_IDS:
            n_kept += 1
            continue

        old_style = m.group(2)
        new_style = restyle_to_grey(old_style)
        replacement = f'{m.group(1)} value="" style="{new_style}"'
        content = content[:m.start()] + replacement + content[m.end():]
        n_greyed += 1

    return content, n_greyed, n_kept


if __name__ == "__main__":
    content = DRAWIO.read_text(encoding="utf-8")
    new_content, n_greyed, n_kept = process(content)
    DRAWIO.write_text(new_content, encoding="utf-8")
    print(f"GREYED OUT (+ text removed) : {n_greyed} cells")
    print(f"KEPT (in scope)             : {n_kept} cells")
