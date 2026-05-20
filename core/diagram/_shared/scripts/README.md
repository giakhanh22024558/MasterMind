# Script library

Reusable Python templates for atomic Drawio file edits. Each script reads the file, applies targeted regex updates, writes back in a single shot — designed to survive cloud-sync (Google Drive, OneDrive, etc.) races by being idempotent and re-runnable.

## Scripts

| Script | Purpose |
|---|---|
| [`update-cell-value.py`](update-cell-value.py) | Refine a cell's display label without touching style or geometry. |
| [`add-cell.py`](add-cell.py) | Insert a new component, store, or provisional cell into a parent container. |
| [`revert-edges.py`](revert-edges.py) | Roll back a batch of edges, optionally restoring a previous edge set. |

## How to use

1. **Copy the template** to your project's `.scripts/` folder
2. **Rename** to describe what it does (e.g. `wire-payment-pipeline-edges.py`)
3. **Edit the constants** at the top of the file (path, cell IDs, values)
4. **Run** with `python <script>.py`
5. **Keep the script** in `.scripts/` after running — it documents the edit and can be re-run

## Why "atomic" edits

Drawio files are XML. When edited in the desktop/web app while also being synced via cloud storage, race conditions happen:

- You edit cell A → file saved
- Cloud sync uploads · or downloads a slightly older version · or merges
- Your change appears to vanish

These scripts mitigate by:

- **Single read** → process in memory → **single write**. Tiny race window.
- **Targeted regex** — only modify the specific cells/edges, not the whole document
- **Re-runnable** — if first attempt was overwritten, just run again

Always **verify after running** by re-reading the file (or refreshing the Drawio app) before assuming success.

## Common patterns

### Pattern A · adding architecture edge (one-shot)

```python
# Read · build new edge XML · insert before </root> · write
content = DRAWIO.read_text()
new_edge = f'<mxCell id="..." value="..." style="..." parent="1" source="..." target="..." edge="1">...'
content = content.replace('</root>', new_edge + '</root>', 1)
DRAWIO.write_text(content)
```

### Pattern B · refining edge/cell label (one-shot)

Use [`update-cell-value.py`](update-cell-value.py) — regex matches by ID, replaces only the `value="..."` attribute.

### Pattern C · provisional cell (preemptive commit)

Use [`add-cell.py`](add-cell.py) with `NEW_CELL_STYLE = PROVISIONAL_STYLE` (pale amber, dashed, warning font). Vendor sees the warning visual and knows to confirm.

### Pattern D · revert + restore pair

Use [`revert-edges.py`](revert-edges.py) with both `DELETE_EDGE_IDS` and `RESTORE_EDGES` populated. Pair with the original `wire-...` script that added the edges — together they're a reversible operation.

## Encoding the value attribute (HTML in XML)

Drawio mxCell `value` attribute contains HTML, but the entire value lives inside an XML attribute. Triple-escape:

| Want to render | Encode in `value="..."` |
|---|---|
| `<b>Bold</b>` | `&lt;b&gt;Bold&lt;/b&gt;` |
| `<br/>` | `&lt;br/&gt;` |
| `<i>italic</i>` | `&lt;i&gt;italic&lt;/i&gt;` |
| `·` (middle dot) | `&#183;` |
| `"quoted"` (inside HTML attribute inside value) | `&quot;quoted&quot;` |
| `&` (literal ampersand) | `&amp;` |
| `&nbsp;` (HTML non-breaking space, inside value) | `&amp;nbsp;` |
| Inline color: `<font color="#c62828">red</font>` | `&lt;font color=&#39;#c62828&#39;&gt;red&lt;/font&gt;` (use `&#39;` for single quote to avoid double-quote conflict) |

When in doubt, look at how Drawio itself encodes the value when you save a cell from the GUI — open the file and copy the pattern.

## Re-running scripts (safe idempotency)

All scripts in this library are idempotent IF written correctly:

- `update-cell-value.py` — regex matches `<mxCell id="X" value="...">` — re-running replaces the value with the same new content. Safe.
- `grey-out-non-scope.py` — re-running re-applies the same grey style + empty value. Safe.
- `add-cell.py` — regex matches the parent's children — re-running inserts a duplicate. **Add a check** before inserting if you want strict idempotency.
- `revert-edges.py` — delete is safe (no-op if already deleted). Restore inserts duplicates if re-run. **Check first** before re-running with RESTORE_EDGES populated.

For high-confidence operations, run with a quick grep verification after:

```bash
python my-script.py
# verify:
grep -c 'id="new-cell-id"' my-file.drawio  # should be 1
```
