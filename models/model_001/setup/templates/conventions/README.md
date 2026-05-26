# conventions/

Project-level **overrides** cho defaults của skills MasterMind.

Mỗi file `<skill>-conventions.md` tương ứng 1 skill có conventions-defaults. Bỏ trống = dùng default; fill bằng `yaml` block hoặc bảng để override.

## Files trong folder này

| File | Override defaults của skill |
|---|---|
| `features-conventions.md` | [`document/features`](../MasterMind/models/model_001/document/features/) (ID format, Priority levels, AC writing format) |
| `analysis-conventions.md` | [`document/analysis`](../MasterMind/models/model_001/document/analysis/) (Gap Type / Priority / Decision dropdowns) |
| `jira-conventions.md` | [`integration/jira`](../MasterMind/models/model_001/integration/jira/) (tag system, sub-task roles, mode) |

## Thêm file mới khi cần

Khi dùng skill khác có conventions (vd `srs`, `erd`), tạo `<skill>-conventions.md` tương ứng.

## Pattern (per skill)

```yaml
# Ví dụ features-conventions.md
id_formats:
  epic:  "EPIC-{n:03d}"      # default 2 digits → override 3 digits
  story: "US-{n:04d}"        # default STORY-NNN → override US-NNNN

priority_values:
  - Critical
  - Important
  - Standard
  - Backlog

ac_writing:
  format: en      # vi (default) | en
```

Skill sẽ đọc và merge với defaults — convention thắng nếu conflict.

## Anti-patterns

- ❌ Sửa default trong `MasterMind/` repo — không sustainable, dùng convention ở project
- ❌ Inline convention trong từng file artifact — tập trung 1 chỗ trong `conventions/` cho consistency
- ❌ Fork MasterMind để custom — luôn override qua conventions
