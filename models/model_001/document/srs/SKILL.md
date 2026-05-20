---
name: model_001_srs
description: Sinh tài liệu Software Requirements Specification (SRS) chuẩn IEEE 830 / ISO-IEC-IEEE 29148 ở định dạng .docx từ nội dung Markdown. Tách bạch nội dung (viết ở .md) và hình thức (code Python). Tự xử lý trang bìa, mục lục native, đánh số heading đa cấp, sinh mã STT/ID & số hình, merge ô header bảng, callout. Dùng khi tạo/cập nhật SRS, chuyển nội dung SRS sang file Word có format chuẩn, hoặc thiết lập quy ước soạn SRS cho một dự án.
---

# model_001_srs — Sinh tài liệu SRS chuẩn IEEE

Skill đóng gói quy trình tạo tài liệu **Software Requirements Specification** chuẩn IEEE ở định dạng `.docx`. Nguyên lý cốt lõi: **nội dung viết ở Markdown, hình thức nằm trong code Python** — người soạn chỉ tập trung vào nội dung, generator tự áp toàn bộ format (font, màu, numbering, trang bìa, mục lục, mã ID...).

> Mọi content module của skill này được versioned ở leaf-folder (`v1/`, `v2/`…). Mặc định dùng `vN` cao nhất. Xem [`meta/versioning-pattern/`](../../../../core/meta/versioning-pattern/).

## Khi nào dùng skill này

Invoke khi người dùng yêu cầu:

- **Tạo mới một tài liệu SRS** cho một hệ thống/sản phẩm
- **Chuyển nội dung SRS** (đã viết ở .md hoặc cần soạn) sang file Word `.docx` có format chuẩn
- **Cập nhật** một SRS đã có và xuất lại bản `.docx`
- **Thiết lập quy ước** soạn SRS cho một dự án (cấu trúc, format, mã ID)
- **Kiểm tra** một tài liệu SRS có khớp template/format chuẩn hay không

## Bước đầu tiên trong mọi công việc

1. **Discover conventions** — tìm `<project-root>/model_001_srs-conventions.md` theo [`meta/conventions-as-data-pattern/`](../../../../core/meta/conventions-as-data-pattern/)
2. **Áp dụng convention dự án** ở những mục đã khai báo (tên dự án, logo, version, màu...)
3. **Fallback về** [`conventions-defaults/`](conventions-defaults/) cho mọi mục chưa khai báo
4. **Acknowledge nguồn** khi giải thích lựa chọn ("theo conventions dự án" / "dùng default")

## Content modules (đều versioned)

| Module | Mục đích |
|---|---|
| [`conventions-schema/`](conventions-schema/) | Checklist convention dự án cần khai khi dùng skill (tên, logo, version, màu) |
| [`conventions-defaults/`](conventions-defaults/) | Format mặc định decode từ SRS chuẩn (font, màu, page, numbering, mã ID) |
| [`srs-structure/`](srs-structure/) | Đặc tả cấu trúc nội dung SRS — 6 phần, khối lặp Đặc tả Chi tiết, legend |
| [`patterns/`](patterns/) | Pattern tái sử dụng — tách content/format, tự sinh ID & số hình |
| [`examples/`](examples/) | Worked walkthrough — sinh SRS hoàn chỉnh từ file mẫu |
| [`scripts/`](scripts/) | `srs_format.py` (chuẩn format) + `srs_md_to_docx.py` (generator) |

## Workflow templates

### Workflow A · Sinh SRS .docx từ nội dung Markdown

1. **Discover conventions** dự án (bước đầu tiên ở trên)
2. **Soạn / chuẩn bị nội dung** ở file `.md` theo cấu trúc tại [`srs-structure/`](srs-structure/):
   - Frontmatter (tên dự án, version, bảng metadata) → trang bìa
   - 6 phần cấp 1; mỗi tính năng = 1 khối `### Đặc tả Chi tiết — … (FEAT-XXX)` gồm 5 khối con
   - Ô STT/ID, Mã BR để **trống** — generator tự sinh
   - Caption hình ghi `Hình [mô tả]` — generator tự đánh số
3. **Chạy generator**: `python scripts/v1/srs_md_to_docx.py <input.md> <output.docx>`
4. **Verify**: mở `.docx`, để Word cập nhật field Mục lục; đối chiếu format với [`conventions-defaults/`](conventions-defaults/)

### Workflow B · Kiểm tra một SRS có khớp chuẩn

1. Đọc [`srs-structure/`](srs-structure/) — checklist cấu trúc
2. Đọc [`conventions-defaults/`](conventions-defaults/) — checklist format
3. Đối chiếu tài liệu đích với từng mục checklist; báo cáo điểm lệch

### Workflow C · Cập nhật / mở rộng format chuẩn

1. Sửa logic format trong [`scripts/`](scripts/) → `srs_format.py` (KHÔNG sửa nội dung)
2. Nếu thay đổi phá vỡ tương thích → bump version module theo [`meta/versioning-pattern/`](../../../../core/meta/versioning-pattern/)
3. Cập nhật [`conventions-defaults/`](conventions-defaults/) cho khớp

## Nguyên tắc cốt lõi

- **Content ở .md, format ở Python** — không trộn lẫn; sửa format không đụng nội dung và ngược lại
- **Quy ước tự sinh, không viết tay** — mã STT/ID, số hình, numbering heading, merge ô do generator lo
- **Tái sử dụng Legend** — chỉ dùng giá trị Loại/Thuộc tính đã định nghĩa, không tự tạo mới
- **Không hard-code project specifics** — tên dự án, logo là biến truyền vào

## Anti-patterns

- ❌ Viết format thủ công trong .md (in đậm tay, canh lề tay) — để generator lo
- ❌ Điền sẵn mã STT/ID, số hình trong .md — generator sẽ ghi đè / sinh trùng
- ❌ Hard-code tên dự án "LEXcentra" vào code — phải là biến `project_name`
- ❌ Tự định nghĩa Loại/Thuộc tính mới ngoài Legend canonical
- ❌ Sửa `.docx` trực tiếp rồi mong đồng bộ ngược về `.md` — nguồn sự thật là `.md`

## Cross-references tới meta-patterns

| Meta-pattern | Skill này dùng khi |
|---|---|
| [Uniform skill structure](../../../../core/meta/uniform-skill-structure/) | Skill theo layout Shape A bắt buộc |
| [Versioning pattern](../../../../core/meta/versioning-pattern/) | Mọi content module versioned ở leaf-folder |
| [Conventions as data](../../../../core/meta/conventions-as-data-pattern/) | Convention dự án ở `<project>/model_001_srs-conventions.md` |
| [Atomic edits](../../../../core/meta/atomic-edits-pattern/) | Generator ghi `.docx` (file sync-prone) — đọc 1 lần / ghi 1 lần, đóng Word trước khi chạy |
| [Defer-then-promote](../../../../core/meta/defer-then-promote-pattern/) | Khi giá trị Loại/Thuộc tính mới lặp lại nhiều lần → cân nhắc bổ sung vào Legend canonical |

## Lưu ý stack

Skill này lệch nhẹ so với stack mặc định của repo (markdown + plain text): thư mục [`scripts/v1/assets/`](scripts/v1/assets/) chứa **1 file ảnh nhị phân** (`srs_logo.png`) — logo bắt buộc cho trang bìa. Đây là asset cần thiết, tương tự diagram export.
