"""
Atomically update one cell's `value` (its display label / HTML) in a Drawio
file WITHOUT touching its style or geometry.

USE CASE:
  - Refining an edge label to add a reference-ID + characterization
  - Renaming a component's display name (e.g. after a design-decision rename)
  - Expanding a label to mention an additional schema or use case

WHY ATOMIC:
  Drawio files synced via cloud (Google Drive, OneDrive) are prone to race
  conditions during edits. This script reads + writes the entire file in one
  shot via Path.read_text / write_text, minimizing the window.

If a sync overwrites your change, just re-run the script — it's idempotent
(regex matches the cell ID, not the old value).

CONFIGURATION:
  Edit the constants below:
    DRAWIO    — path to the target .drawio file
    CELL_ID   — the mxCell id to update (e.g. "e_layer_a_to_store_x" or "98")
    NEW_VALUE — HTML-escaped new label content
"""
import re
from pathlib import Path

# ─── EDIT THESE ───────────────────────────────────────────────────────────────

DRAWIO = Path(r"<absolute path to your .drawio>")

CELL_ID = "<cell-id-here>"

# HTML-escaped label content. Drawio mxCell values use entity-encoded HTML:
#   < → &lt;     > → &gt;     " → &quot;     & → &amp;     · → &#183;
#
# Example: to render "<b>Bold</b><br/><i>italic · note</i>"
# Encode as: "&lt;b&gt;Bold&lt;/b&gt;&lt;br/&gt;&lt;i&gt;italic &#183; note&lt;/i&gt;"
NEW_VALUE = (
    "&lt;b&gt;Header text&lt;/b&gt;&lt;br/&gt;"
    "&lt;i&gt;(reference-ID &#183; characterization)&lt;/i&gt;"
)

# ─── EXECUTION ────────────────────────────────────────────────────────────────

content = DRAWIO.read_text(encoding="utf-8")

# Match the cell's value="..." (preserves style + everything else)
pattern = re.compile(
    r'(<mxCell id="' + re.escape(CELL_ID) + r'" value=")[^"]*(")'
)

new_content, n = pattern.subn(rf'\g<1>{NEW_VALUE}\g<2>', content)

if n == 0:
    raise SystemExit(f"Cell id={CELL_ID!r} not found in {DRAWIO}")

DRAWIO.write_text(new_content, encoding="utf-8")
print(f"Updated {n} cell ({CELL_ID}) value")
