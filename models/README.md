# models

Các **model** — mỗi `model_NNN/` là một cụm skill cụ thể cho một dự án / bối cảnh. Người dùng tạo model mới theo yêu cầu.

## Cấu trúc một model

```
models/model_NNN/
├── diagram/
│   └── <type>/        ← skill diagram cụ thể (vd: architecture)
└── document/
    └── <type>/        ← skill document cụ thể (vd: srs)
```

Mỗi model chứa các bộ skill (`diagram`, `document`...); bên trong là skill specific hơn (`architecture`, `srs`...).

## Model hiện có

| Model | Skill |
|---|---|
| [`model_001/`](model_001/) | `diagram/architecture` · `document/srs` |

## Quy tắc

Dù input context hay định dạng output khác nhau, **mọi model phải tuân [Core Rule](../core/core-rule/)**. Model chỉ chứa phần *specific*; phần *chung* (methodology, versioning, meta) luôn tham chiếu về [`../core/`](../core/).
