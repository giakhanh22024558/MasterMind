# google_sheets — README

Edit Google Sheets **live via API** while preserving comments / history / dropdowns / conditional formatting.

## TL;DR

```bash
# 1. Copy templates
cp -r templates/ <project-root>/sheets_api/

# 2. Edit config.py (IDs, cols, dropdowns)
# 3. Edit backlog.py (entity CRUD per project schema)
# 4. pip install gspread
# 5. Create OAuth credentials → place in project root → run verify
python -m sheets_api.verify_setup
```

## Golden rule — always use `insertDimension(inheritFromBefore=True)`

Vanilla `gspread.Worksheet.insert_row()` **loses format/DV**. Use the helper in [`templates/helpers.py`](templates/helpers.py):

```python
from sheets_api.helpers import insert_inheriting
insert_inheriting(ws, index=11, values=[...])  # ✓ preserves format
```

If the row above is NOT the same type (e.g. inserting a STORY right after a FEAT row), fall back to `copyPaste(PASTE_NORMAL)` from a template — see [insert-with-format-inheritance pattern](patterns/insert-with-format-inheritance.md).

## Read more

- [`SKILL.md`](SKILL.md) — full entry point
- [`patterns/cell-level-edit.md`](patterns/cell-level-edit.md) — philosophy
- [`patterns/insert-with-format-inheritance.md`](patterns/insert-with-format-inheritance.md) — most important bug + fix
- [`patterns/hierarchical-row-types.md`](patterns/hierarchical-row-types.md) — Backlog Epic→Feature→Story style
- [`examples/lex-walkthrough.md`](examples/lex-walkthrough.md) — worked example from the LEX project
- [`templates/SETUP.md`](templates/SETUP.md) — 5-minute OAuth setup
