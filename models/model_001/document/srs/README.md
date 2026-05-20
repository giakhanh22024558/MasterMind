# model_001_srs — README

Skill sinh tài liệu **Software Requirements Specification (SRS)** chuẩn IEEE 830 / ISO·IEC·IEEE 29148 ở định dạng `.docx`, từ nội dung viết bằng Markdown.

Triết lý: **nội dung viết ở `.md` · hình thức nằm trong code Python**. Người soạn chỉ lo nội dung; generator tự áp toàn bộ format và các quy ước tự sinh.

## Quick start

| Nếu bạn muốn… | Đọc |
|---|---|
| Hiểu skill trong 1 trang | [`SKILL.md`](SKILL.md) |
| Biết cấu trúc nội dung một SRS | [`srs-structure/`](srs-structure/) |
| Biết format chuẩn (font, màu, page, numbering) | [`conventions-defaults/`](conventions-defaults/) |
| Biết dự án cần khai báo gì | [`conventions-schema/`](conventions-schema/) |
| Xem ví dụ sinh SRS đầy đủ | [`examples/`](examples/) |
| Chạy generator | [`scripts/`](scripts/) |

## Sinh một file SRS — 3 bước

1. **Soạn nội dung** ở file `.md` theo cấu trúc [`srs-structure/`](srs-structure/)
2. **Chạy**: `python scripts/v1/srs_md_to_docx.py <input.md> <output.docx>`
3. **Mở** `.docx` trong Word → field Mục lục tự cập nhật

## Bộ công cụ làm gì cho bạn

| Tự động xử lý | Chi tiết |
|---|---|
| Trang bìa | Logo + tên dự án + version + bảng metadata, đứng độc lập 1 trang |
| Mục lục | Field TOC native (cấp 1-3), tự cập nhật khi mở Word |
| Numbering heading | H1-H4 số thập phân `1`/`1.1`/`1.1.1`/`1.1.1.1`; H5 `A. B. C.`; H6 `a. b. c.` |
| Mã STT/ID | Tự sinh `COM-<heading H4>-<NNN>` cho bảng thành phần, `BR-…` cho Business Rules |
| Số hình | Tự đánh `Hình <heading H4>-<n>`, căn giữa |
| Merge ô | Hàng có các ô giống hệt nhau → tự gộp 1 ô |
| Format | Font Mulish, màu `#193D74`, A4, gạch chân Heading 1, footer có số trang |

## Folder layout

```
srs/
├── SKILL.md                       ← agent-facing entry
├── README.md                      ← file này
├── conventions-schema/v1/         ← convention dự án cần khai
├── conventions-defaults/v1/       ← format mặc định (decode từ SRS chuẩn)
├── srs-structure/v1/              ← đặc tả cấu trúc nội dung SRS
├── patterns/v1/                   ← pattern tái sử dụng
├── examples/v1/                   ← walkthrough + file mẫu
└── scripts/v1/                    ← srs_format.py + srs_md_to_docx.py + assets/
```

## Adoption guide cho một dự án

1. Tạo `<project-root>/model_001_srs-conventions.md` theo [`conventions-schema/`](conventions-schema/)
2. Khai: tên dự án, đường dẫn logo, thông tin version; phần nào bỏ trống → dùng default
3. Soạn nội dung SRS ở `.md`, chạy generator

## Stack

- **Markdown** cho nội dung + tài liệu
- **Python** (`python-docx`) cho generator — cài: `pip install python-docx`
- **1 asset nhị phân**: `scripts/v1/assets/srs_logo.png` (logo trang bìa)

## License

Internal. Adapt freely. No warranty.
