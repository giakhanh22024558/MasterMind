# core/diagram — khung lõi skill diagram

Phần **bất biến** của skill diagram: methodology dùng chung (`_shared/`), mô hình versioning, và template project-conventions. **Skill diagram cụ thể** (architecture, dfd...) sống trong từng model tại `models/model_NNN/diagram/<type>/`.

## Layout

```
core/diagram/
├── SKILL.md            ← dispatcher (unversioned)
├── README.md           ← file này
├── VERSIONING.md       ← mô hình versioning
├── _shared/            ← methodology dùng chung mọi loại diagram
│   ├── conventions-discovery/v1/
│   ├── folder-structure-general/v1/
│   ├── design-decisions-format/v1/
│   ├── spec-driven-audit/v1/
│   ├── defer-then-promote-pattern/v1/
│   ├── atomic-edits-pattern/v1/
│   ├── edge-labels-general/v1/
│   └── scripts/v1/
└── _project-template/v1/   ← PROJECT-CONVENTIONS.md template
```

## Skill diagram cụ thể

| Model | Sub-skill | Vị trí |
|---|---|---|
| model_001 | architecture | [`models/model_001/diagram/architecture/`](../../models/model_001/diagram/architecture/) |

## Tạo sub-skill diagram mới

Tạo `models/model_NNN/diagram/<type>/` theo uniform structure — xem [`SKILL.md`](SKILL.md) phần "Adding a new diagram-type sub-skill". Sub-skill tham chiếu ngược về `core/diagram/_shared/` cho methodology chung.

## Nguyên tắc

- **Conventions là data** — dự án khai ở `<project>/diagram-conventions.md`, skill đọc & áp.
- **Versioning theo leaf-folder** — xem [`VERSIONING.md`](VERSIONING.md).
- Tuân [Core Rule](../core-rule/) — `.drawio` là user layer, `.md` / Mermaid là agent layer.

## Stack

Mermaid (diagram dạng text) · Drawio `.drawio` XML · Python scripts (atomic edits) · Markdown (narrative).
