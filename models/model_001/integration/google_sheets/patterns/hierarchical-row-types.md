# Pattern · Hierarchical row types

> For backlog-style sheets where one sheet holds multiple **levels** of entity (e.g. Epic → Feature → Story).

## Problem

Many projects manage a hierarchy in a single sheet by:
- Epic row: fill only columns A+B
- Feature row: fill only columns C+D
- Story row: fill only columns E+F+G+H+I

```
| A      | B               | C        | D                  | E         | F         | G       | H      | I        |
|--------|-----------------|----------|--------------------|-----------|-----------|---------|--------|----------|
| EPIC-01| Case Management |          |                    |           |           |         |        |          |
|        |                 | FEAT-001 | Browse & search    |           |           |         |        |          |
|        |                 |          |                    | STORY-001 | name      | High    | Ready  | Active   |
|        |                 |          |                    | STORY-002 | name      | High    | Ready  | Active   |
|        |                 | FEAT-002 | Create & edit      |           |           |         |        |          |
|        |                 |          |                    | STORY-007 | name      | Med     | Backlog| Active   |
```

→ The hierarchy is encoded in **row position** (order) + **which columns are filled**.

## Pattern — Row classifier function

```python
def classify_row(row):
    """Return ('epic' | 'feature' | 'story' | 'other', dict|None)."""
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

This pattern applies to any hierarchical sheet — just adjust column indexes + ID prefixes.

## CRUD operations that need the classifier

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
Scan backward from the entity's row → the first row of the parent type → that's the parent.

### 3. Find end-of-section (insert position)
```python
def end_of_section(rows, start_row, allow_types):
    """Return the last row that belongs to the section starting at start_row.
    Stop when a row whose type is NOT in allow_types is encountered."""
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

Used for **inserting at the right position**:
- Insert a story at the end of a feature → `end_of_section(rows, feat_row, allow_types={"story"}) + 1`
- Insert a feature at the end of an epic → `end_of_section(rows, epic_row, allow_types={"feature", "story"}) + 1`

### 4. Auto-generate the next ID
```python
def next_id(prefix, digits, existing_items):
    nums = [int(item["id"].split("-")[-1]) for item in existing_items]
    return f"{prefix}{max(nums, default=0) + 1:0{digits}d}"

# e.g.: next_id("STORY-", 3, self.stories())  → "STORY-142"
```

IDs are not reused (even when entities are deleted) → keeps history traceable.

## Variants for other projects

### Project with different entities (Task / Ticket / Issue)
Same pattern, just change:
- Column mapping (e.g. Ticket has columns: Type, Assignee, Sprint, Estimate, Status)
- ID prefix (`TICKET-` instead of `STORY-`)
- Allowed dropdown values
- Number of levels (e.g. 2 levels Epic-Story instead of 3 levels Epic-Feature-Story)

### Project using a 2-sheet hierarchy
- Sheet 1: parent entities (flat list)
- Sheet 2: child entities with a `parent_id` column
→ No classifier needed; each sheet is flat. Simpler but worse UX (BA can't easily see the hierarchy).

### Project with polymorphic rows (the AC sheet in LEX)
The AC sheet has 2 types:
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

Same principle.

## Anti-patterns

- ❌ Encoding the hierarchy with indented text (`"  STORY-001"`) — not parseable
- ❌ Using row color instead of column-filled to classify — color is not reliable for parsing
- ❌ Mixing multiple entity types into one row (e.g. a row that is both a feature and a story) — breaks the pattern
- ❌ Skipping `"other"` rows (empty/separator) when scanning — fine to skip, but remember the position for inserts

## Cross-references

- [`insert-with-format-inheritance.md`](insert-with-format-inheritance.md) — the classifier helps pick the right template row
- [`../templates/helpers.py`](../templates/helpers.py) — `classify_row()` example implementation
- [`../templates/backlog.py`](../templates/backlog.py) — full CRUD class using this pattern
