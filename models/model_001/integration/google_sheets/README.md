# google_sheets — README

Edit Google Sheet **live qua API**, giữ comment / history / dropdown / conditional formatting.

## TL;DR

```bash
# 1. Copy templates
cp -r templates/ <project-root>/sheets_api/

# 2. Sửa config.py (IDs, cols, dropdowns)
# 3. Sửa backlog.py (entity CRUD theo schema project)
# 4. pip install gspread
# 5. Tạo OAuth credentials → đặt vào project root → run verify
python -m sheets_api.verify_setup
```

## Quy tắc vàng — luôn dùng `insertDimension(inheritFromBefore=True)`

`gspread.Worksheet.insert_row()` thuần **mất format/DV**. Dùng helper trong [`templates/helpers.py`](templates/helpers.py):

```python
from sheets_api.helpers import insert_inheriting
insert_inheriting(ws, index=11, values=[...])  # ✓ giữ format
```

Nếu row trên KHÔNG cùng type (vd insert STORY ngay sau FEAT row), fallback `copyPaste(PASTE_NORMAL)` từ template — xem [pattern insert-with-format-inheritance](patterns/insert-with-format-inheritance.md).

## Đọc thêm

- [`SKILL.md`](SKILL.md) — Entry point đầy đủ
- [`patterns/cell-level-edit.md`](patterns/cell-level-edit.md) — Philosophy
- [`patterns/insert-with-format-inheritance.md`](patterns/insert-with-format-inheritance.md) — Bug quan trọng nhất + fix
- [`patterns/hierarchical-row-types.md`](patterns/hierarchical-row-types.md) — Backlog Epic→Feature→Story style
- [`examples/lex-walkthrough.md`](examples/lex-walkthrough.md) — Worked example từ project LEX
- [`templates/SETUP.md`](templates/SETUP.md) — Setup OAuth 5 phút
