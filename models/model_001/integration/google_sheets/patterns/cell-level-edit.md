# Pattern · Cell-level edit (vs file-replace)

## Problem

A project has live data in Google Sheets:
- Client / team edit daily through the UI
- The sheet has cell comments, version history, filter views, conditional formatting, dropdowns
- Claude / scripts need to update fields on command

**❌ Common wrong approach:** download `.xlsx` → modify with openpyxl → upload-overwrite via Drive API → **EVERYTHING IS LOST**: comments, history, filter views.

**✅ Right approach:** Google Sheets API → edit each cell (`update_cell`, `batch_update`) or perform row operations (`insertDimension`, `deleteDimension`, `copyPaste`) → the Sheet keeps all UI metadata intact.

## Comparison

| Criterion | File-replace (upload overwrite) | Cell-level (API) |
|---|---|---|
| Cell comments | ❌ Lost | ✅ Preserved |
| Version history | ❌ Reset to a single new version | ✅ Each edit is one restorable revision |
| Filter views | ❌ Lost | ✅ Preserved |
| Conditional formatting | ❌ Lost if file schema doesn't match | ✅ Preserved |
| Data validation (dropdowns) | ❌ May be lost if range mismatches | ✅ Preserved when inserted correctly |
| Setup | None (Drive write only) | OAuth once, 5 min |
| Conflict with live user edits | Risk: overwrites live edits | Safe — only touches affected cells |

## When file-replace is still acceptable

- The Sheet is a one-way output (generated from another data source, never edited by hand)
- The project accepts history loss (business reason)
- No critical comments / filter views exist

→ Any other case **must** use cell-level.

## Implementation summary

```python
import gspread

gc = gspread.oauth(credentials_filename='credentials.json',
                   authorized_user_filename='token.json')
sh = gc.open_by_key('<spreadsheet_id>')
ws = sh.worksheet('<sheet_name>')

# Edit one cell
ws.update_cell(row=11, col=8, value='In Review')

# Edit batch (multiple cells in one call — saves quota)
ws.batch_update([
    {'range': 'H11', 'values': [['In Review']]},
    {'range': 'I11', 'values': [['Active']]},
])

# Insert row (MUST use inheritFromBefore — see the other pattern)
sh.batch_update({'requests': [{
    'insertDimension': {
        'range': {'sheetId': ws.id, 'dimension': 'ROWS',
                  'startIndex': 10, 'endIndex': 11},
        'inheritFromBefore': True,
    }
}]})
```

## Pitfalls

1. **Vanilla `gspread.Worksheet.insert_row()` drops format** — see [`insert-with-format-inheritance.md`](insert-with-format-inheritance.md)
2. **Quota 60 writes/minute/user** — batch them for bulk operations
3. **Race condition with live user edits** — an API edit may trigger the project's Apps Script `onEdit`; watch for loops
4. **`value_input_option`** — use `USER_ENTERED` (Sheet parses formulas/dates) instead of `RAW`; `RAW` is treated as a plain string

## Cross-references

- [`insert-with-format-inheritance.md`](insert-with-format-inheritance.md) — critical bug when inserting rows
- [`../templates/helpers.py`](../templates/helpers.py) — ready-to-use code
