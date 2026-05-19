# Atomic edits pattern (general)

How to safely edit files that may be concurrently modified by other tools (cloud-sync clients, GUI editors, other processes). Apply when a skill manipulates sync-prone files like `.drawio`, `.docx`, `.xlsx`, configs in shared folders.

## The problem

Files in sync-prone locations (Google Drive, OneDrive, Dropbox, shared network drives) face race conditions:

- You edit the file → file changes
- Sync client uploads or downloads → overwrites your change
- GUI editor has unsaved changes in memory → saving them overwrites scripted edits
- Multiple scripts running in sequence → second sees stale state

The risk: changes appear to vanish, or the file ends up in an inconsistent state.

## The pattern

Mitigation strategy that works in practice:

1. **Single read** of entire file into memory
2. **Apply changes in memory** via regex / string ops
3. **Single write** back to disk
4. **Verify** after a brief delay (re-read or grep)
5. **Re-run** if verification fails (script must be idempotent)

```python
from pathlib import Path
import re

FILE = Path("...")

# 1. Read once
content = FILE.read_text(encoding="utf-8")

# 2. Apply changes in memory
new_content = re.sub(r'pattern', 'replacement', content)

# 3. Write once
FILE.write_text(new_content, encoding="utf-8")

# 4. Verify externally (grep, re-read, visual)
```

The window between read and write is microseconds — vs. interactive GUI edits that are seconds. Sync rarely interrupts the script window.

## Idempotency requirement

Scripts must be **safe to re-run**. If first attempt was overwritten by sync, running again should produce the same end state without errors or duplicates.

### Idempotent operations

- **Value replacement** (regex by ID, replace value) → re-run produces same result ✅
- **Style replacement** → same pattern ✅
- **Mass updates with conditions** → re-run is no-op for already-updated items ✅

### Operations needing care

- **Cell/element insertion** → regex matches parent's children and appends → re-run **inserts a duplicate**

Solution: check for existing ID before inserting:

```python
if re.search(r'id="' + re.escape(NEW_ID) + r'"', content):
    print(f"{NEW_ID} already exists, skipping")
else:
    # ... insert ...
```

## Verifying after a script run

After running a script, quick check:

```bash
# Did the new content land?
grep -c 'new-id' my-file.<ext>
# Expected: 1
```

If grep returns no match: sync may have reverted. Re-run the script.

## Common race scenarios and recovery

### Scenario A · Script runs · sync immediately reverts

- **Symptom:** script reports success, grep confirms — minutes later change is gone
- **Cause:** Sync client uploaded older version after our write
- **Recovery:** re-run script (it's idempotent)
- **Prevention:** close GUI editors before script runs

### Scenario B · Multiple scripts in sequence · second sees stale state

- **Symptom:** second script's regex doesn't match first script's change
- **Cause:** file got reverted between scripts
- **Recovery:** re-run both
- **Prevention:** batch related changes into one script (atomic multi-edit) instead of chaining

### Scenario C · GUI editor open while script runs

- **Symptom:** undefined behavior — either version might "win"
- **Cause:** GUI has unsaved changes; saving them overwrites script output
- **Recovery:** close GUI, re-run script
- **Prevention:** **always close GUI editors before script-based edits**

## When NOT to script (do interactive instead)

Interactive GUI edits are fine for:

- Visual layout tweaks
- One-off label corrections
- Style adjustments not affecting structure

Scripts are essential for:

- **Atomic batch changes** (e.g. 7 edges added in one operation)
- **Refactoring** (e.g. rename a cell ID across all referencing edges)
- **Reproducibility** (the script documents what was changed)
- **Cross-format sync** (paired edits to .md + .drawio + .docx etc.)

Typical workflow combines both:

- **Scripts** for structural changes (atomic batch)
- **GUI** for visual polish (positioning, label placement)

## Cross-format consistency

When a project has multiple representations (e.g. Mermaid `.md` + Drawio `.drawio` twin), every structural change must update **all** representations.

Pattern:

1. Edit the source-of-truth representation first (often the simpler / smaller one)
2. Run the equivalent script to update other representations
3. Verify all render correctly

If you only update one, the representations drift. At next review, someone notices and has to reconcile manually.

## Script naming + retention

Each per-edit script lives in a `<project>/.scripts/` folder:

- Descriptive name: `<verb>-<noun>.py` (e.g. `wire-payment-pipeline-edges.py`)
- **Keep after running** — script documents the edit
- **Re-runnable** — can recover from sync races

## Generic script library

Each skill that manipulates sync-prone files should provide reusable templates in `<skill>/scripts/v1/` (or in `<skill>/_shared/scripts/v1/` for multi-sub-skill). Examples (from `diagram/`):

- `update-cell-value.py` — atomic value/label update
- `add-cell.py` — atomic cell insertion with idempotency check
- `revert-edges.py` — rollback batch of edges

When creating a new skill that touches sync-prone files, build similar templates.

## When the file is NOT sync-prone

If files are local-only and edited only by your scripts, you don't need full atomic-edits rigor. But the patterns (single-read-single-write, idempotency) are still good hygiene.

## Cross-references from skill content

Skills referencing this pattern should link to it instead of re-explaining:

```markdown
This skill handles sync-prone Drawio files; see [`atomic-edits pattern`](../../../meta/atomic-edits-pattern/) for the general approach.
Domain-specific application: ...
```
