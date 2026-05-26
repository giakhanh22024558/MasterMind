# Pattern · Cell-level edit (vs file-replace)

## Vấn đề

Project có data sống trên Google Sheets:
- Khách / team edit hằng ngày qua UI
- Có comment ô, version history, filter view, conditional formatting, dropdown
- Claude / script cần update field theo lệnh user

**❌ Cách sai phổ biến:** download `.xlsx` → modify với openpyxl → upload đè qua Drive API → **MẤT TẤT CẢ** comment, history, filter view.

**✅ Cách đúng:** Google Sheets API → edit từng ô (`update_cell`, `batch_update`) hoặc thao tác row (`insertDimension`, `deleteDimension`, `copyPaste`) → Sheet vẫn giữ nguyên mọi metadata UI.

## So sánh

| Tiêu chí | File-replace (upload đè) | Cell-level (API) |
|---|---|---|
| Comment ô | ❌ Mất | ✅ Giữ |
| Version history | ❌ Reset thành 1 version mới | ✅ Mỗi edit là 1 revision có thể restore |
| Filter view | ❌ Mất | ✅ Giữ |
| Conditional formatting | ❌ Mất nếu file không cùng schema | ✅ Giữ |
| Data validation (dropdown) | ❌ Có thể mất nếu range mismatch | ✅ Giữ nếu insert đúng cách |
| Setup | Không cần (chỉ Drive write) | OAuth 5 phút 1 lần |
| Conflict với user đang edit | Risk: ghi đè edit live | An toàn — chỉ ô đụng |

## Khi nào file-replace vẫn ổn

- Sheet là output 1 chiều (generate từ data source khác, không ai edit thủ công)
- Project chấp nhận mất history (lý do business)
- Không có comment / filter view nào quan trọng

→ Các case khác **phải** dùng cell-level.

## Implementation tóm tắt

```python
import gspread

gc = gspread.oauth(credentials_filename='credentials.json',
                   authorized_user_filename='token.json')
sh = gc.open_by_key('<spreadsheet_id>')
ws = sh.worksheet('<sheet_name>')

# Edit 1 ô
ws.update_cell(row=11, col=8, value='In Review')

# Edit batch (nhiều ô 1 lần — đỡ quota)
ws.batch_update([
    {'range': 'H11', 'values': [['In Review']]},
    {'range': 'I11', 'values': [['Active']]},
])

# Insert row (PHẢI dùng inheritFromBefore — xem pattern khác)
sh.batch_update({'requests': [{
    'insertDimension': {
        'range': {'sheetId': ws.id, 'dimension': 'ROWS',
                  'startIndex': 10, 'endIndex': 11},
        'inheritFromBefore': True,
    }
}]})
```

## Pitfalls

1. **`gspread.Worksheet.insert_row()` thuần làm mất format** — xem [`insert-with-format-inheritance.md`](insert-with-format-inheritance.md)
2. **Quota 60 write/phút/user** — nếu bulk thì batch lại
3. **Race condition với user đang edit** — API edit có thể trigger Apps Script `onEdit` của project; lưu ý loop
4. **`value_input_option`** — dùng `USER_ENTERED` (Sheet parse formula/date) thay vì `RAW`; `RAW` bị treat as plain string

## Cross-references

- [`insert-with-format-inheritance.md`](insert-with-format-inheritance.md) — bug critical khi insert row
- [`../templates/helpers.py`](../templates/helpers.py) — code ready
