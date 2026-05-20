# Pattern · Tách Content / Format (content-in-md, format-in-python)

Pattern nền tảng của skill `model_001_srs`.

## Problem

Khi soạn tài liệu kỹ thuật trực tiếp trong Word:

- Người soạn vừa lo nội dung vừa lo format → mất tập trung, format không đồng nhất
- Sửa format toàn cục (đổi màu heading, đổi font) phải sửa thủ công từng chỗ
- Mã định danh (STT/ID, số hình), numbering heading viết tay → dễ trùng, dễ lệch
- Khó review nội dung vì lẫn với markup trình bày
- Mỗi tài liệu mới phải dựng lại format từ đầu

## Solution

Tách hai mối quan tâm thành hai tầng độc lập:

| Tầng | Nơi sống | Chứa gì |
|---|---|---|
| **Content** | File `.md` | Chữ nghĩa, cấu trúc heading, bảng, bullet — KHÔNG format trình bày |
| **Format** | Code Python | Font, màu, page, numbering, trang bìa, mục lục, quy ước tự sinh |

Một **generator** ghép 2 tầng → xuất `.docx`:

```
content.md  ──┐
              ├──▶  srs_md_to_docx.py  ──▶  output.docx
srs_format.py ┘     (generator)            (đúng chuẩn format)
```

- `srs_format.py` — chuẩn format: hằng số màu/font/page, style heading, numbering đa cấp, API dựng trang bìa / TOC / bảng / callout.
- `srs_md_to_docx.py` — generator: parse `.md`, áp format, xử lý các quy ước tự sinh.

### Hệ quả: các quy ước "tự sinh"

Vì format là code, generator tự lo những thứ trước đây viết tay:

| Quy ước | Cơ chế |
|---|---|
| Numbering heading | Multilevel list native — `1`/`1.1`/`1.1.1`/`1.1.1.1`, H5 `A.B.C.` |
| Mã STT/ID | `COM-<heading H4>-<NNN>` — sinh từ vị trí bảng, nối tiếp trong cùng H4 |
| Số hình | `Hình <heading H4>-<n>` — đếm theo mục |
| Merge ô | Hàng có mọi ô giống hệt → gộp 1 ô |
| Trang bìa / TOC | Dựng từ frontmatter `.md` + field TOC native |

→ Người soạn để **trống** ô STT/ID, ghi caption `Hình [mô tả]` không số — generator điền.

## Trade-offs

**Ưu:**
- Người soạn chỉ tập trung nội dung; format luôn đồng nhất
- Đổi format toàn cục = sửa 1 chỗ trong Python, build lại
- Không bao giờ trùng/lệch mã ID, số hình, numbering
- File `.md` dễ review, dễ diff, dễ version-control

**Nhược:**
- Cần bước build (chạy script) — không WYSIWYG tức thì
- Người soạn phải tuân cấu trúc `.md` quy ước (xem [`../../srs-structure/`](../../srs-structure/))
- Sửa tinh chỉnh visual cuối cùng (vị trí ảnh…) vẫn cần mở Word

## Worked example

Tham chiếu [`../../examples/`](../../examples/) — sinh một SRS hoàn chỉnh từ `SRS_Sample.md`.

## When NOT to use

- Tài liệu một lần, ngắn, không cần format chuẩn lặp lại → soạn thẳng Word nhanh hơn
- Tài liệu cần cộng tác realtime nhiều người trên cùng bản Word

## Cross-references

- Generator ghi file `.docx` sync-prone → áp [`meta/atomic-edits-pattern/`](../../../../../../core/meta/atomic-edits-pattern/): đóng Word trước khi build, build = đọc/ghi 1 lần, re-run được.
- Nếu giá trị Loại/Thuộc tính mới lặp lại ≥3 lần → cân nhắc promote vào Legend canonical theo [`meta/defer-then-promote-pattern/`](../../../../../../core/meta/defer-then-promote-pattern/).
