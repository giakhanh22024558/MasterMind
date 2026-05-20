---
name: document
description: Khung lõi (core framework) cho các skill sinh tài liệu văn bản — .docx và các định dạng tương tự. Định nghĩa phần bất biến: nội dung ở .md, format ở code Python, tuân Core Rule 3 tầng. Skill document cụ thể (srs...) sống trong models/model_NNN/document/.
---

# Document — khung lõi sinh tài liệu

`core/document/` giữ phần **bất biến** của mọi skill sinh tài liệu văn bản (`.docx`...). Skill document **cụ thể** sống trong từng model tại `models/model_NNN/document/<type>/` (ví dụ: `srs`).

> **Trạng thái:** khung + stub. Phần lõi sẽ được tách dần (defer-then-promote) khi có từ 2 skill document trở lên.

## Nguyên tắc bất biến

Mọi skill document phải tuân:

1. **[Core Rule](../core-rule/)** — input → `.md` context → Python format (agent layer) → `.docx` (user layer). Sửa user layer phải grep agent layer trước.
2. **Tách content / format** — nội dung ở `.md`, hình thức ở code Python; không trộn lẫn.
3. **[Cross-reference](../cross-reference/)** — kỹ thuật áp dụng khi chỉnh sửa `.docx` đã sinh.
4. **[Atomic edits](../meta/atomic-edits-pattern/)** — `.docx` là file sync-prone: đóng Word trước khi ghi, đọc/ghi một lần.
5. **[Conventions as data](../meta/conventions-as-data-pattern/)** — quy ước dự án ở `<project>/<skill>-conventions.md`.

## Skill document hiện có

| Model | Skill | Vị trí |
|---|---|---|
| model_001 | `srs` — sinh tài liệu IEEE SRS `.docx` | [`models/model_001/document/srs/`](../../models/model_001/document/srs/) |

## Tạo skill document mới

Tạo trong một model: `models/model_NNN/document/<type>/`, theo uniform structure ([`uniform-skill-structure`](../meta/uniform-skill-structure/)) và tuân toàn bộ nguyên tắc bất biến ở trên.
