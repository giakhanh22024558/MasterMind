# Pattern · Insert row with format inheritance

> **This is the #1 bug for first-time gspread users.** Read this before writing any insert/create method.

## Problem

Vanilla `gspread.Worksheet.insert_row(values, index=N)` — looks simple, but:

- ❌ Does not inherit font / size / background color from the row above
- ❌ Does not inherit data validation (dropdowns disappear)
- ❌ Does not inherit conditional formatting (color chips disappear)

Result: the new row shows up with the Sheet's **default format** (often very different from neighboring rows of the same kind), looking like a "leak" in otherwise clean data.

## Root cause

`gspread.insert_row()` internally calls the Sheets API `insertDimension` with `inheritFromBefore=False` (the default). The Sheets API inserts a blank row and applies no format from neighbors.

## Fix — 3 strategies

### Strategy 1: `insertDimension(inheritFromBefore=True)` — preferred when the row above is the same type

Inherits all format + DV + conditional formatting from the row immediately above.

```python
sheet_id = ws.id  # gid
start_0 = index_1based - 1  # convert 1-based → 0-based

ws.spreadsheet.batch_update({
    "requests": [{
        "insertDimension": {
            "range": {
                "sheetId": sheet_id,
                "dimension": "ROWS",
                "startIndex": start_0,
                "endIndex": start_0 + 1,
            },
            "inheritFromBefore": True,   # ← key
        }
    }]
})

# Then write values into the new row
ws.update(f"A{index_1based}:I{index_1based}",
          [values], value_input_option="USER_ENTERED")
```

**Use when:** the row at `index_1based - 1` is the same type as the row being inserted (e.g. inserting a story after another story).

**Do NOT use when:** the row above is a different type (e.g. inserting a story after a feature header → would inherit the feature's purple bg → WRONG).

### Strategy 2: `copyPaste(PASTE_NORMAL)` — fallback from a same-type template row

When inheriting from the row above is wrong, copy the format from a template row (e.g. the first story row in the sheet).

```python
# Step 1: insert a blank row
ws.spreadsheet.batch_update({"requests": [{
    "insertDimension": {
        "range": {"sheetId": sheet_id, "dimension": "ROWS",
                  "startIndex": start_0, "endIndex": start_0 + 1},
        "inheritFromBefore": False,
    }
}]})

# Step 2: copy format/DV/condFmt from the template
template_0 = template_row_1based - 1
# If the template is below the insert point, it was shifted +1 by step 1
if template_row_1based >= index_1based:
    template_0 += 1

ws.spreadsheet.batch_update({"requests": [{
    "copyPaste": {
        "source": {"sheetId": sheet_id,
                   "startRowIndex": template_0, "endRowIndex": template_0 + 1,
                   "startColumnIndex": 0, "endColumnIndex": ncols},
        "destination": {"sheetId": sheet_id,
                        "startRowIndex": start_0, "endRowIndex": start_0 + 1,
                        "startColumnIndex": 0, "endColumnIndex": ncols},
        "pasteType": "PASTE_NORMAL",   # ← includes format + DV + condFmt + value
    }
}]})

# Step 3: write values (overwrites the template values from step 2)
ws.update(f"A{index_1based}:{end_col}{index_1based}",
          [values], value_input_option="USER_ENTERED")
```

### Strategy 3: Hybrid — prefer `inheritFromBefore`, fall back to copyPaste

Generic logic — decides based on the type of the row above:

```python
def _insert_inheriting(ws, index_1based, values, expected_type=None, classify_fn=None, template_finder=None):
    prev_row = index_1based - 1
    prev_type = classify_fn(ws.get_values()[prev_row - 1]) if prev_row >= 1 else None

    if prev_type == expected_type:
        # Strategy 1
        _do_insert_inherit_before(ws, index_1based)
    else:
        # Strategy 2
        template = template_finder(expected_type)
        _do_insert_with_copypaste(ws, index_1based, template, len(values))

    _write_values(ws, index_1based, values)
```

→ See the full implementation in [`../templates/helpers.py`](../templates/helpers.py).

## `PASTE_NORMAL` paste type — what does it include?

| Paste type | Format | Value | DV | Cond. Format |
|---|---|---|---|---|
| `PASTE_NORMAL` | ✅ | ✅ | ✅ | ✅ |
| `PASTE_FORMAT` | ✅ | ❌ | ❌ | ❌ |
| `PASTE_VALUES` | ❌ | ✅ | ❌ | ❌ |
| `PASTE_DATA_VALIDATION` | ❌ | ❌ | ✅ | ❌ |
| `PASTE_CONDITIONAL_FORMATTING` | ❌ | ❌ | ❌ | ✅ |

→ Using `PASTE_NORMAL` and then overwriting values is the simplest way to get all 4.

## Verify the fix

After inserting, check in the UI:
- ✅ Font / size match other rows of the same kind
- ✅ Background color matches (e.g. story rows are all white)
- ✅ Dropdown chips appear (e.g. Priority has red/orange/yellow chips)
- ✅ Conditional formatting triggers correctly (Status chips change color per value)

If any of those is missing → the strategy is wrong; debug by reading the format of the new row and comparing against the template:

```python
fmt = ws.spreadsheet.fetch_sheet_metadata(params={'fields': 'sheets.data.rowData.values.userEnteredFormat'})
```

## Anti-patterns

- ❌ Vanilla `ws.insert_row(values, index=N)` — loses format
- ❌ Inserting and then manually updating format cell-by-cell — burns API quota
- ❌ Hard-coding the template row number — wrong as soon as the schema shifts; use a dynamic `template_finder()`
- ❌ Skipping the "shift template_0 if template ≥ insert" step — after insertDimension, every row below is +1

## Cross-references

- [`../templates/helpers.py`](../templates/helpers.py) — full implementation of all 3 strategies
- [`hierarchical-row-types.md`](hierarchical-row-types.md) — row classification pattern (needed by strategy 3)
