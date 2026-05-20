# MasterMind

Kho **skill** tái sử dụng cho agent AI. Cấu trúc 2 tầng: phần lõi bất biến (`core/`) và các model cụ thể theo dự án (`models/`).

## Cấu trúc

```
MasterMind/
├── core/        ← lõi bất biến — chung cho mọi dự án, không đổi khi thêm model
│   ├── core-rule/        quy tắc lõi 3 tầng
│   ├── cross-reference/  kỹ thuật tham chiếu chéo (stub)
│   ├── diagram/          khung lõi skill diagram
│   ├── document/         khung lõi skill document
│   ├── meta/             cách tạo skill mới
│   └── template/         scaffold skill mới
└── models/      ← skill cụ thể theo dự án
    └── model_NNN/
        ├── diagram/<type>/    vd: architecture
        └── document/<type>/   vd: srs
```

## Core Rule (bất biến)

Mọi model — dù input hay định dạng output khác nhau — đều tuân quy tắc 3 tầng:

1. **Input → `.md`** — phân tích input thô thành Markdown làm context
2. **Agent layer** — chuẩn hóa format thành code Python (`.md` + Python = nguồn sự thật)
3. **User layer** — `.docx` / `.drawio`: khi sửa, **luôn grep `.md` trước**, rồi mới chỉnh sửa bằng cross-reference

Chi tiết: [`core/core-rule/`](core/core-rule/).

## Dùng repo

- **Áp dụng skill có sẵn** → mở `models/model_NNN/<bộ>/<skill>/SKILL.md`
- **Tạo skill mới** → đọc [`core/meta/SKILL.md`](core/meta/SKILL.md), scaffold từ [`core/template/`](core/template/), đặt vào `models/model_NNN/`
- **Hiểu phần lõi** → [`core/README.md`](core/README.md)

## License

Internal. Adapt freely. No warranty.
