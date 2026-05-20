# models

Nhóm các skill được tổ chức theo "model" — mỗi `model_NNN/` là một cụm skill đánh số tuần tự.

## Currently implemented

| Model | Nội dung |
|---|---|
| [`model_001/`](model_001/) | Cụm skill số 001 — chứa `model_001_srs` (sinh tài liệu SRS) |

## Cấu trúc

```
models/
└── model_NNN/
    └── model_NNN_<domain>/      ← skill thực tế, theo uniform structure
```

Mỗi skill bên trong `model_NNN/` tuân theo cấu trúc skill chuẩn của repo — xem [`../../meta/uniform-skill-structure/`](../../meta/uniform-skill-structure/).
