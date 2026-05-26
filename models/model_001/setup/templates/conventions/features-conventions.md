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

```yaml
# ac_writing:
#   language: en              # en (default) | vi
#   format_en: "Given/When/Then"
#   format_vi: "Khi/Nếu… thì…"
#   max_per_story: 10         # suggested max ACs per story
```

## Sheet layout (when rendering xlsx)

```yaml
# sheet_layout:
#   epic_color:    "7030A0"     # purple (default)
#   feature_color: "BDD7EE"     # light blue (default)
#   story_color:   ""           # white = no fill (default)
#   header_color:  "1F4E79"     # canonical dark blue
```
