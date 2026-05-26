# -*- coding: utf-8 -*-
"""Generic helpers — DO NOT need to be edited for most projects.

Provides:
- `insert_inheriting()`        — insert a row preserving format/DV/condFmt (see pattern insert-with-format-inheritance.md)
- `copy_row_format()`          — copy format from a template row to a target row
- `validate_dropdown()`        — check a value is in the allowed list before pushing
- `next_sequential_id()`       — auto-generate IDs of the form "PREFIX-NNN"
- `find_row_index()`           — search for a row by predicate
"""
from gspread.utils import rowcol_to_a1

# ─── INSERT row with format inheritance ───────────────────────────────────────
def insert_inheriting(ws, index_1based, values, template_row=None):
    """Insert a row at `index_1based`, preserving format / DV / conditional formatting.

    Strategy:
    - If `template_row` is None: `insertDimension(inheritFromBefore=True)` — inherits from the row above.
      Use when the row above is the SAME TYPE as the row being inserted.
    - If `template_row` is provided: insert a blank row + `copyPaste(PASTE_NORMAL)` from the template.
      Use when the row above is a DIFFERENT TYPE (e.g. inserting a story after a feature header).

    Then writes `values` into the new row.

    Args:
        ws: gspread.Worksheet
        index_1based: int — insert position (1-based)
        values: list[str] — value per column
        template_row: Optional[int] — 1-based row to copy format from
    """
    sheet_id = ws.id
    start_0 = index_1based - 1
    inherit = (index_1based >= 2 and template_row is None)

    # Step 1: insert a blank row
    ws.spreadsheet.batch_update({
        "requests": [{
            "insertDimension": {
                "range": {"sheetId": sheet_id, "dimension": "ROWS",
                          "startIndex": start_0, "endIndex": start_0 + 1},
                "inheritFromBefore": inherit,
            }
        }]
    })

    # Step 2: copy format from template (if provided)
    if template_row is not None:
        # After insert, a template row at or below the insert point is shifted +1
        src = template_row + 1 if template_row >= index_1based else template_row
        copy_row_format(ws, src_row=src, dst_row=index_1based, ncols=len(values))

    # Step 3: write values (overwrites template content but preserves format)
    end_col = _col_letter(len(values))
    ws.update(f"A{index_1based}:{end_col}{index_1based}",
              [values], value_input_option="USER_ENTERED")


def copy_row_format(ws, src_row, dst_row, ncols, paste_type="PASTE_NORMAL"):
    """Copy format + DV + conditional formatting from src_row → dst_row.

    paste_type options:
      - PASTE_NORMAL: everything (format + value + DV + condFmt)  ← default
      - PASTE_FORMAT: format only (cell color, font, border)
      - PASTE_DATA_VALIDATION: dropdowns only
      - PASTE_CONDITIONAL_FORMATTING: format rules only
    """
    sheet_id = ws.id
    src_0 = src_row - 1
    dst_0 = dst_row - 1
    ws.spreadsheet.batch_update({
        "requests": [{
            "copyPaste": {
                "source": {"sheetId": sheet_id,
                           "startRowIndex": src_0, "endRowIndex": src_0 + 1,
                           "startColumnIndex": 0, "endColumnIndex": ncols},
                "destination": {"sheetId": sheet_id,
                                "startRowIndex": dst_0, "endRowIndex": dst_0 + 1,
                                "startColumnIndex": 0, "endColumnIndex": ncols},
                "pasteType": paste_type,
            }
        }]
    })


# ─── VALIDATION ───────────────────────────────────────────────────────────────
def validate_dropdown(value, allowed, field_name="value"):
    """Raise ValueError if value is not in the allowed list. Skip if value is None."""
    if value is None: return
    if value not in allowed:
        raise ValueError(f"{field_name}={value!r}; allowed: {allowed}")


# ─── ID generation ────────────────────────────────────────────────────────────
def next_sequential_id(prefix, digits, existing_items, id_key="id"):
    """Auto-generate the next ID as PREFIX + zero-padded number.

    existing_items: list of dicts that have an 'id' key (e.g. [{"id": "STORY-005"}, ...])
    Returns e.g. "STORY-006" (max+1).
    """
    nums = []
    for item in existing_items:
        try:
            nums.append(int(item[id_key].split("-")[-1]))
        except (ValueError, KeyError, AttributeError):
            continue
    return f"{prefix}{max(nums, default=0) + 1:0{digits}d}"


# ─── Row search ───────────────────────────────────────────────────────────────
def find_row_index(rows, predicate):
    """Return the 1-based row index of the first row matching predicate(row). None if not found."""
    for i, row in enumerate(rows, start=1):
        if predicate(row):
            return i
    return None


def find_section_end(rows, start_row_1based, classify_fn, allow_types):
    """Scan from start_row+1; return the last row that belongs to the section (type ∈ allow_types).
    Stop when a row of a different type is encountered (e.g. the next epic/feature)."""
    last = start_row_1based
    for i in range(start_row_1based + 1, len(rows) + 1):
        t, _ = classify_fn(rows[i - 1])
        if t in allow_types:
            last = i
        elif t == "other":
            continue
        else:
            break
    return last


# ─── Internal ─────────────────────────────────────────────────────────────────
def _col_letter(n):
    """1 → 'A', 26 → 'Z', 27 → 'AA'..."""
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(ord("A") + r) + s
    return s
