# Example — LEX project walkthrough

Showcase đầy đủ skill `google_sheets` applied vào project LEX (legal case management). Project có 2 Sheet quản lý song song trên Drive: **Features list** (Backlog + AC) + **Gap Analysis** (CR tracking).

## Schema project

**Sheet `Backlog`** — 3-level hierarchy:

| Cột | Field | Type |
|---|---|---|
| A | Epic ID | `EPIC-XX` |
| B | Epic name | text |
| C | Feature ID | `FEAT-XXX` |
| D | Feature name | text |
| E | Story ID | `STORY-XXX` |
| F | User Story | text |
| G | Priority | dropdown: Very high / High / Medium / Low |
| H | Status | dropdown: Backlog / Ready / In Progress / In Review / Done |
| I | Lifecycle | dropdown: Active / Done / Archived / Superseded |

**Sheet `Acceptance Criteria`** — polymorphic (story header rows + AC rows):

| Cột | Story header row | AC row |
|---|---|---|
| A | Story ID (bold) | Story ID |
| B | (empty) | AC ID `AC-XXX-NN` |
| C | User story name (bold) | `☐ <criteria>` |
| D | (empty) | BR ref |
| E | (empty) | Test status (dropdown) |

## Setup

```bash
# 1. Copy template từ MasterMind
cp -r mastermind/models/model_001/integration/google_sheets/templates/ \
      LEX-SLI-SRS/sheets_api/

# 2. Sửa config.py — điền SPREADSHEET_ID = "198n3cwq..." (Features list 2)

# 3. Tạo OAuth credentials → credentials.json ở project root

# 4. pip install gspread

# 5. Verify
cd LEX-SLI-SRS
python -m sheets_api.verify_setup
# → Connected to sheet 'Backlog' — 11 epic · 43 feature · 136 story
```

## Customize cho LEX

Vì LEX có thêm sheet `Acceptance Criteria` (không chuẩn template), thêm module `ac.py`:

```python
# sheets_api/ac.py
from .auth import get_client
from . import config as C
from .helpers import insert_inheriting, validate_dropdown, find_row_index

TEST_STATUS_VALUES = ["Not tested", "Passed", "Failed", "Blocked"]

def classify_ac_row(row):
    pad = list(row) + [""] * 5
    sid, aid = pad[0], pad[1]
    if sid and sid.startswith("STORY-") and not aid:
        return "story_header", {"story_id": sid, "name": pad[2]}
    if sid and aid and aid.startswith("AC-"):
        return "ac", {"story_id": sid, "id": aid, "text": pad[2],
                      "br_ref": pad[3], "test_status": pad[4]}
    return "other", None

class ACAPI:
    def __init__(self):
        self.gc = get_client()
        self.ws = self.gc.open_by_key(C.SPREADSHEET_ID).worksheet("Acceptance Criteria")
        self._cache = None
    # ... (similar pattern: _all, _template_row_of, list_for_story, create, update, delete)
```

→ Full code trong [LEX project: `sheets_api/ac.py`](../../../../../../../sheets_api/ac.py).

## Usage examples trong project

### Update story status
```python
from sheets_api import BacklogAPI
BacklogAPI().update_story("STORY-013", status="In Review")
```

### Tạo story mới + AC trong 1 lệnh
```python
from sheets_api import BacklogAPI, ACAPI
bk, ac = BacklogAPI(), ACAPI()

new_id = bk.create_story("FEAT-001",
    "[CR-19] User filter vụ việc theo Tag",
    priority="High", status="Ready", lifecycle="Active")

ac.create_story_header(new_id, "[CR-19] User filter vụ việc theo Tag")
ac.create(new_id, "Khi user chọn ≥1 Tag, thì list lọc theo logic OR giữa các Tag")
ac.create(new_id, "Nếu chọn 0 Tag, thì filter Tag không áp dụng (giữ kết quả filter khác)")
```

### Mark AC pass sau QA
```python
ACAPI().update_test_status("AC-013-02", "Passed")
```

### Bulk update — đổi tất cả story trong feature từ Backlog → Ready
```python
bk = BacklogAPI()
for s in bk.stories(feature_id="FEAT-001"):
    if s["status"] == "Backlog":
        bk.update_story(s["id"], status="Ready")
```

## Kết quả

- ✅ Mỗi edit là **1 revision** trên Sheet (Drive Activity panel thấy đủ)
- ✅ Comment, filter view, conditional formatting **giữ nguyên**
- ✅ Dropdown chip màu (Very high = đỏ, Done = xám…) **giữ nguyên** khi insert row mới
- ✅ Apps Script `onEdit` trigger → tự re-export `.xlsx` → Drive Desktop sync về local `~3s`

## Pitfalls đã hit trong LEX project

| Bug | Fix |
|---|---|
| Insert row mất dropdown + bg yellow | `insertDimension(inheritFromBefore=True)` + fallback `copyPaste(PASTE_NORMAL)` từ template — đã encode trong `helpers.insert_inheriting()` |
| Apps Script `onEdit` tạo file `.xlsx (1)` duplicate | Thêm `Utilities.sleep(800)` giữa delete cũ + create mới trong script |
| Token expired sau ~3 tháng | Xóa `token.json` → run lại verify_setup → re-authorize browser |

## Cross-references

- [Pattern · cell-level-edit](../patterns/cell-level-edit.md)
- [Pattern · insert-with-format-inheritance](../patterns/insert-with-format-inheritance.md)
- [Pattern · hierarchical-row-types](../patterns/hierarchical-row-types.md)
- [Setup guide](../templates/SETUP.md)
