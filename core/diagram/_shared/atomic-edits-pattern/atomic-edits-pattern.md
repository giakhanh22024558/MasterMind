# Atomic edits pattern

How to safely edit Drawio (`.drawio`) XML files that may be concurrently synced via cloud storage (Google Drive, OneDrive, Dropbox, etc.).

## The problem

Drawio files are XML. Cloud-sync clients watch for changes and upload them in the background. Race conditions happen when:

- You edit the file in the Drawio app → file changes
- Your script reads the file at the same time → reads partial or stale content
- Cloud sync uploads or downloads → overwrites local changes
- Your change appears to vanish on next inspection

This isn't a bug in any single tool — it's an inherent risk with shared-file collaboration.

## Mitigation: atomic edits

The pattern that works in practice:

1. **Single read** of the entire file into memory
2. **Apply changes in memory** via regex / string ops
3. **Single write** back to disk
4. **Verify** after a brief delay (re-read or grep)
5. **Re-run** if verification fails (the script must be idempotent)

```python
from pathlib import Path
import re

DRAWIO = Path("...")

# 1. Read once
content = DRAWIO.read_text(encoding="utf-8")

# 2. Apply changes
new_content = re.sub(r'(<mxCell id="X" value=")[^"]*(")',
                     r'\1<new value>\2',
                     content)

# 3. Write once
DRAWIO.write_text(new_content, encoding="utf-8")

# 4. (Print summary; verify externally if critical)
```

The window between read and write is microseconds — vs. an interactive Drawio app edit which is seconds. Cloud sync rarely interrupts the script edit window.

## Idempotency

Scripts must be **safe to re-run**. If the first attempt was overwritten by a sync, running again should produce the same end state without errors.

### Idempotent operations

- **Value replacement** (`update-cell-value.py`) — regex matches by ID, replaces value → re-run produces same result. ✅ Idempotent
- **Style replacement** — same pattern as value. ✅ Idempotent
- **Grey-out** — applies the same style to non-keep cells → re-run is no-op for already-greyed cells. ✅ Idempotent

### Operations needing care

- **Cell insertion** (`add-cell.py`) — regex matches parent's children and appends → re-run **inserts a duplicate**.
  - **Solution**: check for existing cell ID before inserting
- **Edge insertion** (`wire-*-edges.py`) — same issue.
  - **Solution**: pair with a delete step or check first

### Idempotency check pattern

```python
# Before inserting
if re.search(r'<mxCell id="' + re.escape(NEW_ID) + r'"', content):
    print(f"Cell {NEW_ID} already exists, skipping insertion")
else:
    # ... insert ...
```

## Verifying after a script run

After running a script, do a quick verification:

```bash
# Check that the new cell exists
grep -c 'id="new-cell-id"' my-file.drawio
# Expected: 1

# Check that the new value is in place
grep 'new label content' my-file.drawio
# Expected: a match
```

If grep returns no match, the sync may have overwritten. Re-run the script.

## Common race scenarios and recovery

### Scenario A · Script runs, sync immediately reverts

- Symptom: script reports success, grep confirms — but minutes later the change is gone
- Cause: Drive client uploaded an older version after our write
- Recovery: re-run the script (it's idempotent)
- Prevention: close the Drawio app before running scripts (so app's last-saved version doesn't overwrite)

### Scenario B · Multiple scripts run in sequence, second one sees stale state

- Symptom: second script's regex doesn't match because first script's change was sync-reverted between runs
- Cause: file got reverted between scripts
- Recovery: re-run both scripts
- Prevention: batch related changes into one script (atomic multi-edit) rather than chaining several scripts

### Scenario C · Drawio app open while script runs

- Symptom: undefined — could be either version "winning"
- Cause: Drawio app has unsaved changes in memory; saving them overwrites script's output
- Recovery: close Drawio app, then re-run script
- Prevention: **always close the Drawio app before script-based edits**

## Why not just edit in Drawio app interactively?

Interactive edits are fine for:
- Layout tweaks
- One-off label corrections
- Visual style adjustments

Scripts are essential for:
- **Atomic batch changes** (e.g. 7 edges added in one operation)
- **Refactoring** (e.g. rename a cell ID across all edges referencing it)
- **Reproducibility** (the script documents what was changed)
- **Cross-format sync** (paired with Mermaid edits in `.md`)

A typical workflow combines both:
- **Scripts** for structural changes (add/remove cells, modify edges, batch label updates)
- **Drawio app** for visual polish (positioning, routing, label placement)

## Pairing scripts with Mermaid edits

When the architecture has both a Drawio `.drawio` twin AND a Mermaid `.md` source, every structural change must update **both**.

Pattern:

1. Edit the Mermaid `.md` first (smaller, easier to test render)
2. Run the equivalent script to apply the same change to Drawio
3. Verify both render correctly

If you only update one, the two go out of sync — at the next review, someone notices a discrepancy and has to reconcile manually.

## Script library

See [`_shared/scripts/`](../scripts/) for reusable templates:

- `update-cell-value.py` — atomic label update
- `add-cell.py` — atomic cell insertion
- `revert-edges.py` — rollback + restore pair

Each project's `.scripts/` folder will accumulate per-edit scripts derived from these templates. Keep them after running — they document the edit history.
