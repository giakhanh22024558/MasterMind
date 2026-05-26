# -*- coding: utf-8 -*-
"""Generic helpers — KHÔNG cần sửa cho hầu hết project.

Cung cấp:
- `insert_inheriting()`        — insert row giữ format/DV/condFmt (xem pattern insert-with-format-inheritance.md)
- `copy_row_format()`          — copy format từ row template tới row đích
- `validate_dropdown()`        — check value thuộc allowed list trước khi push
- `next_sequential_id()`       — auto-gen ID kiểu "PREFIX-NNN"
- `find_row_index()`           — search row theo predicate
"""
from gspread.utils import rowcol_to_a1

# ─── INSERT row với format inheritance ────────────────────────────────────────
def insert_inheriting(ws, index_1based, values, template_row=None):
    """Insert row tại index (1-based), giữ format / DV / conditional formatting.

    Strategy:
    - Nếu `template_row` None: `insertDimension(inheritFromBefore=True)` — kế thừa từ row trên.
      Dùng khi row trên CÙNG TYPE với row sắp insert.
    - Nếu `template_row` cho trước: insert blank + `copyPaste(PASTE_NORMAL)` từ template.
      Dùng khi row trên KHÁC TYPE (vd insert story sau feature header).

    Sau đó write values vào row mới.

    Args:
        ws: gspread.Worksheet
        index_1based: int — vị trí insert (1-based)
        values: list[str] — giá trị mỗi cột
        template_row: Optional[int] — row 1-based để copy format
    """
    sheet_id = ws.id
    start_0 = index_1based - 1
    inherit = (index_1based >= 2 and template_row is None)

    # Bước 1: insert blank row
    ws.spreadsheet.batch_update({
        "requests": [{
            "insertDimension": {
                "range": {"sheetId": sheet_id, "dimension": "ROWS",
                          "startIndex": start_0, "endIndex": start_0 + 1},
                "inheritFromBefore": inherit,
            }
        }]
    })

    # Bước 2: copy format từ template (nếu cung cấp)
    if template_row is not None:
        # Sau insert, template row >= insert sẽ bị shift +1
        src = template_row + 1 if template_row >= index_1based else template_row
        copy_row_format(ws, src_row=src, dst_row=index_1based, ncols=len(values))

    # Bước 3: write values (overwrite content nhưng giữ format)
    end_col = _col_letter(len(values))
    ws.update(f"A{index_1based}:{end_col}{index_1based}",
              [values], value_input_option="USER_ENTERED")


def copy_row_format(ws, src_row, dst_row, ncols, paste_type="PASTE_NORMAL"):
    """Copy format + DV + conditional formatting từ src_row → dst_row.

    paste_type options:
      - PASTE_NORMAL: tất cả (format + value + DV + condFmt)  ← default
      - PASTE_FORMAT: chỉ format (cell color, font, border)
      - PASTE_DATA_VALIDATION: chỉ dropdown
      - PASTE_CONDITIONAL_FORMATTING: chỉ rule format
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
    """Raise ValueError nếu value không thuộc allowed list. Skip nếu value is None."""
    if value is None: return
    if value not in allowed:
        raise ValueError(f"{field_name}={value!r}; allowed: {allowed}")


# ─── ID generation ────────────────────────────────────────────────────────────
def next_sequential_id(prefix, digits, existing_items, id_key="id"):
    """Auto-gen next ID kiểu PREFIX + zero-padded number.

    existing_items: list of dicts có key 'id' (vd [{"id": "STORY-005"}, ...])
    Trả về vd "STORY-006" (max+1).
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
    """Return 1-based row index of first row matching predicate(row). None nếu không có."""
    for i, row in enumerate(rows, start=1):
        if predicate(row):
            return i
    return None


def find_section_end(rows, start_row_1based, classify_fn, allow_types):
    """Quét từ start_row+1, trả row cuối thuộc section (type ∈ allow_types).
    Stop khi gặp row có type KHÁC (vd next epic/feature)."""
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
