# analysis-conventions.md

Override defaults của skill [`document/analysis`](../MasterMind/models/model_001/document/analysis/conventions-defaults/).

## Dropdown values

```yaml
# gap_type_values:
#   - Modification
#   - Enhancement
#   - Missing
#   - Missing (New Feature)
#   - Behavior Change
#   - No Change

# priority_values:
#   - P0
#   - P1
#   - P2

# decision_values:
#   - This Sprint
#   - Next Sprint
#   - Another Sprint
#   - Invalid / Out-of-scope
```

## CR ID format

```yaml
# cr_id_format: "CR-{n:02d}"     # default: CR-01, CR-02, ...
```

## Estimation unit

```yaml
# estimation_unit: man-hours     # default | story-points | days
```

## Auto-bump P0 to This Sprint?

```yaml
# auto_bump_p0:
#   enabled: false               # nếu true: mọi CR P0 tự set Decision=This Sprint khi approve
```
