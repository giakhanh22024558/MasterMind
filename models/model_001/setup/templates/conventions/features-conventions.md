# features-conventions.md

Overrides defaults of skill [`document/features`](../MasterMind/models/model_001/document/features/conventions-defaults/).

> Leave empty to use skill defaults. Uncomment + fill the blocks below to override.

## ID formats

```yaml
# id_formats:
#   epic:  "EPIC-{n:02d}"      # default
#   feature: "FEAT-{n:03d}"    # default
#   story: "STORY-{n:03d}"     # default
#   ac:    "AC-{story_num}-{n:02d}"  # default
```

## Priority levels

```yaml
# priority_values:
#   - Very high     # default order: highest → lowest
#   - High
#   - Medium
#   - Low
```

## Status / Lifecycle

```yaml
# status_values:
#   - Backlog
#   - Ready
#   - In Progress
#   - In Review
#   - Done

# lifecycle_values:
#   - Active
#   - Done
#   - Archived
#   - Superseded
```

## AC writing format

Pick **one** language per project — never mix within a file.
See [`ac-writing.md`](../../MasterMind/models/model_001/document/features/conventions-defaults/ac-writing.md) for full guidance and examples.

```yaml
ac_writing:
  language: en              # en (default) → "Given/When/Then"
                            # vi           → "Nếu/Khi… thì…"
  # max_per_story: 10       # optional — suggested max ACs per story
```

Reference patterns:
- **EN (GWT):** `Given a missing required field, when clicking Save, then the Save button is disabled`
- **VI:** `Nếu thiếu field bắt buộc, thì nút Lưu disable`

## Sheet layout (when rendering xlsx)

```yaml
# sheet_layout:
#   epic_color:    "7030A0"     # purple (default)
#   feature_color: "BDD7EE"     # light blue (default)
#   story_color:   ""           # white = no fill (default)
#   header_color:  "1F4E79"     # canonical dark blue
```
