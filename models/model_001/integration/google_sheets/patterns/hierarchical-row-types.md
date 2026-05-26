# Pattern · Hierarchical row types

> Cho backlog-style sheets nơi 1 sheet chứa nhiều **cấp** entity (vd Epic → Feature → Story).

## Vấn đề

Nhiều project quản lý hierarchy trong 1 sheet duy nhất bằng cách:
- Row Epic: chỉ điền cột A+B
- Row Feature: chỉ điền cột C+D
- Row Story: chỉ điền cột E+F+G+H+I

```
| A      | B               | C        | D                  | E         | F         | G       | H      | I        |
|--------|-----------------|----------|--------------------|-----------|-----------|---------|--------|----------|
| EPIC-01| Quản lý vụ việc |          |                    |           |           |         |        |          |
|        |                 | FEAT-001 | Duyệt & tìm vụ việc|           |           |         |        |          |
|        |                 |          |                    | STORY-001 | name      | High    | Ready  | Active   |
|        |                 |          |                    | STORY-002 | name      | High    | Ready  | Active   |
|        |                 | FEAT-002 | Tạo & sửa          |           |           |         |        |          |
|        |                 |          |                    | STORY-007 | name      | Med     | Backlog| Active   |
```

→ Hierarchy được encode trong **vị trí row** (thứ tự) + **column nào filled**.

## Pattern — Row classifier function

```python
def classify_row(row):
    """Trả về ('epic' | 'feature' | 'story' | 'other', dict|None)."""
    pad = list(row) + [""] * 9  # pad to handle short rows
    if pad[0] and pad[1] and not pad[2]:
        return "epic", {"id": pad[0], "name": pad[1]}
    if pad[2] and pad[3]:
        return "feature", {"id": pad[2], "name": pad[3]}
    if pad[4] and str(pad[4]).startswith("STORY-"):
        return "story", {"id": pad[4], "name": pad[5],
                         "priority": pad[6], "status": pad[7], "lifecycle": pad[8]}
    return "other", None
```

Pattern này áp dụng được cho mọi hierarchical sheet — chỉ cần điều chỉnh column indexes + ID prefix.

## CRUD operations cần dùng classifier

### 1. List entities by level
```python
def stories(self, feature_id=None):
    out = []; cur_epic = cur_feat = None
    for r in self.ws.get_all_values()[1:]:
        t, m = classify_row(r)
        if t == "epic": cur_epic = m["id"]
        elif t == "feature": cur_feat = m["id"]
        elif t == "story":
            if feature_id and cur_feat != feature_id: continue
            out.append({**m, "feature_id": cur_feat, "epic_id": cur_epic})
    return out
```

### 2. Find parent (epic of a feature, feature of a story)
Scan backward từ row của entity → row đầu tiên có type cha → đó là parent.

### 3. Find end-of-section (insert position)
```python
def end_of_section(rows, start_row, allow_types):
    """Return row cuối thuộc section bắt đầu từ start_row.
    Stop khi gặp row có type KHÔNG nằm trong allow_types."""
    last = start_row
    for i in range(start_row + 1, len(rows) + 1):
        t, _ = classify_row(rows[i - 1])
        if t in allow_types:
            last = i
        elif t == "other":
            continue
        else:
            break
    return last
```

Dùng cho **insert đúng vị trí**:
- Insert story vào cuối feature → `end_of_section(rows, feat_row, allow_types={"story"}) + 1`
- Insert feature vào cuối epic → `end_of_section(rows, epic_row, allow_types={"feature", "story"}) + 1`

### 4. Auto-generate next ID
```python
def next_id(prefix, digits, existing_items):
    nums = [int(item["id"].split("-")[-1]) for item in existing_items]
    return f"{prefix}{max(nums, default=0) + 1:0{digits}d}"

# vd: next_id("STORY-", 3, self.stories())  → "STORY-142"
```

ID không tái sử dụng (dù entity bị xóa) → giữ truy vết history.

## Variants cho project khác

### Project có entity khác (Task / Ticket / Issue)
Cùng pattern, chỉ đổi:
- Column mapping (vd Ticket có cột: Type, Assignee, Sprint, Estimate, Status)
- ID prefix (`TICKET-` thay vì `STORY-`)
- Allowed dropdown values
- Số cấp (vd 2 cấp Epic-Story thay vì 3 cấp Epic-Feature-Story)

### Project dùng 2-sheet hierarchy
- Sheet 1: parent entities (flat list)
- Sheet 2: child entities có `parent_id` column
→ Không cần classifier; mỗi sheet là flat. Đơn giản hơn nhưng UX kém (BA khó nhìn hierarchy).

### Project có polymorphic rows (AC sheet trong LEX)
AC sheet có 2 type:
- Story header: A=Story ID, C=name (B/D/E empty)
- AC row: A=Story ID, B=AC-ID, C="☐ ...", D/E filled

Classifier:
```python
def classify_ac(row):
    pad = list(row) + [""] * 5
    sid, aid = pad[0], pad[1]
    if sid and sid.startswith("STORY-") and not aid:
        return "story_header", {"story_id": sid, "name": pad[2]}
    if sid and aid and aid.startswith("AC-"):
        return "ac", {...}
    return "other", None
```

Cùng nguyên tắc.

## Anti-patterns

- ❌ Lưu hierarchy bằng cách indent text (`"  STORY-001"`) — không parse được
- ❌ Dùng row color thay vì column-filled để classify — color không reliable cho parse
- ❌ Trộn nhiều entity type vào 1 row (vd 1 row vừa là feature vừa là story) — phá pattern
- ❌ Bỏ qua row `"other"` (empty/separator) khi scan — fine to skip nhưng phải remember vị trí cho insert

## Cross-references

- [`insert-with-format-inheritance.md`](insert-with-format-inheritance.md) — classifier giúp chọn template row đúng type
- [`../templates/helpers.py`](../templates/helpers.py) — `classify_row()` example implementation
- [`../templates/backlog.py`](../templates/backlog.py) — đầy đủ CRUD class dùng pattern này
