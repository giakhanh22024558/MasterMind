# Pattern · Insert row with format inheritance

> **Đây là bug số 1 khi mới dùng gspread.** Read this trước khi viết bất kỳ insert/create method nào.

## Vấn đề

`gspread.Worksheet.insert_row(values, index=N)` thuần — tưởng đơn giản nhưng:

- ❌ Không kế thừa font / size / màu nền từ row trên
- ❌ Không kế thừa data validation (dropdown biến mất)
- ❌ Không kế thừa conditional formatting (chip màu biến mất)

Kết quả: row mới hiện lên với format **default của Sheet** (thường khác hẳn các row cùng loại), trông như "rò" giữa dữ liệu sạch.

## Root cause

`gspread.insert_row()` internally gọi `insertDimension` của Sheets API với `inheritFromBefore=False` (mặc định). Sheet API insert blank row, không apply bất kỳ format nào từ neighbor.

## Fix — 3 chiến lược

### Strategy 1: `insertDimension(inheritFromBefore=True)` — preferred khi row trên cùng type

Inherit toàn bộ format + DV + conditional formatting từ row ngay trên.

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

# Sau đó write values vào row mới
ws.update(f"A{index_1based}:I{index_1based}",
          [values], value_input_option="USER_ENTERED")
```

**Khi dùng:** row tại `index_1based - 1` cùng type với row sắp insert (vd insert story sau story khác).

**Không dùng khi:** row trên khác type (vd insert story sau feature header → inherit purple bg của feature → WRONG).

### Strategy 2: `copyPaste(PASTE_NORMAL)` — fallback từ template row cùng type

Khi không inherit được từ row trên, copy format từ row template (vd story đầu tiên trong sheet).

```python
# Bước 1: insert blank row
ws.spreadsheet.batch_update({"requests": [{
    "insertDimension": {
        "range": {"sheetId": sheet_id, "dimension": "ROWS",
                  "startIndex": start_0, "endIndex": start_0 + 1},
        "inheritFromBefore": False,
    }
}]})

# Bước 2: copy format/DV/condFmt từ template
template_0 = template_row_1based - 1
# Nếu template ở dưới insert point, nó bị shift +1 sau bước 1
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
        "pasteType": "PASTE_NORMAL",   # ← bao gồm format + DV + condFmt + value
    }
}]})

# Bước 3: write values (overwrite template values từ bước 2)
ws.update(f"A{index_1based}:{end_col}{index_1based}",
          [values], value_input_option="USER_ENTERED")
```

### Strategy 3: Hybrid — `inheritFromBefore` ưu tiên, fallback copyPaste

Logic generic — tự quyết định dựa trên type của row trên:

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

→ Xem implement đầy đủ trong [`../templates/helpers.py`](../templates/helpers.py).

## `PASTE_NORMAL` paste type — bao gồm gì?

| Paste type | Format | Value | DV | Cond. Format |
|---|---|---|---|---|
| `PASTE_NORMAL` | ✅ | ✅ | ✅ | ✅ |
| `PASTE_FORMAT` | ✅ | ❌ | ❌ | ❌ |
| `PASTE_VALUES` | ❌ | ✅ | ❌ | ❌ |
| `PASTE_DATA_VALIDATION` | ❌ | ❌ | ✅ | ❌ |
| `PASTE_CONDITIONAL_FORMATTING` | ❌ | ❌ | ❌ | ✅ |

→ Dùng `PASTE_NORMAL` rồi overwrite values là cách đơn giản nhất để get all 4.

## Verify đã fix

Sau khi insert, check trên UI:
- ✅ Font / size khớp với row cùng loại
- ✅ Background color khớp (vd story rows đều white)
- ✅ Dropdown chip xuất hiện (vd Priority có chip màu đỏ/cam/vàng)
- ✅ Conditional formatting trigger đúng (chip Status đổi màu theo value)

Nếu thiếu bất kỳ thứ nào → strategy chưa đúng, debug bằng cách đọc format của row mới so với template:

```python
fmt = ws.spreadsheet.fetch_sheet_metadata(params={'fields': 'sheets.data.rowData.values.userEnteredFormat'})
```

## Anti-patterns

- ❌ `ws.insert_row(values, index=N)` thuần — mất format
- ❌ Insert rồi update format thủ công từng cell — tốn API quota
- ❌ Hard-code template row number — schema thay đổi là sai; dùng `template_finder()` dynamic
- ❌ Bỏ bước "shift template_0 nếu template ≥ insert" — sau insertDimension, mọi row dưới bị +1

## Cross-references

- [`../templates/helpers.py`](../templates/helpers.py) — implement đầy đủ 3 strategies
- [`hierarchical-row-types.md`](hierarchical-row-types.md) — classify row pattern (cần cho strategy 3)
