# features-conventions.md

Override defaults của skill [`document/features`](../MasterMind/models/model_001/document/features/conventions-defaults/).

> Bỏ trống = dùng defaults skill. Uncomment + fill các block dưới khi cần override.

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
#   - Very high     # default order: cao → thấp
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

```yaml
# ac_writing:
#   language: vi              # vi | en (default vi cho project tiếng Việt)
#   format_vi: "Khi/Nếu… thì…"
#   format_en: "Given/When/Then"
#   max_per_story: 10         # gợi ý max AC mỗi story
```

## Sheet layout (nếu render xlsx)

```yaml
# sheet_layout:
#   epic_color:    "7030A0"     # purple (default)
#   feature_color: "BDD7EE"     # light blue (default)
#   story_color:   ""           # white = no fill (default)
#   header_color:  "1F4E79"     # canonical dark blue
```
