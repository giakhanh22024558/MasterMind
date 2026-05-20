# Example · Sinh SRS hoàn chỉnh cho hệ thống "RoomBooking"

Walkthrough sinh một tài liệu SRS `.docx` đầy đủ từ file Markdown, dùng skill `model_001_srs`. File nội dung mẫu: [`SRS_Sample.md`](SRS_Sample.md).

## Setup · kịch bản

Cần tạo SRS cho hệ thống `RoomBooking` — quản lý đặt phòng họp nội bộ. Phạm vi: 1 module (`Quản lý đặt phòng họp`) với 3 tính năng (`FEAT-001` xem lịch, `FEAT-002` tạo booking, `FEAT-003` hủy booking).

## Step-by-step

### 1 · Discover conventions

Tìm `<project-root>/model_001_srs-conventions.md`. Dự án demo này không có → dùng toàn bộ default từ [`../../conventions-defaults/`](../../conventions-defaults/). Tên dự án lấy từ tiêu đề trang bìa trong `.md` (`RoomBooking`).

### 2 · Soạn nội dung `.md`

Theo cấu trúc tại [`../../srs-structure/`](../../srs-structure/):

- **Frontmatter** — tên dự án, phụ đề, version, bảng metadata → generator dựng trang bìa
- **6 phần cấp 1** — Lịch sử Phiên bản · Giới thiệu · Mô tả Tổng quan · Yêu cầu Cụ thể · Yêu cầu Phi chức năng
- **Mỗi tính năng** = `### Đặc tả Chi tiết — … (FEAT-XXX)` gồm 5 khối con: Use Case · Sơ đồ luồng · Wireframe · Đặc tả thành phần · Business Rules
- Ô **STT/ID để trống**, caption ghi `Hình [mô tả]` không số, marker `{{LEGEND}}` cho bảng chú giải

### 3 · Chạy generator

```bash
python ../../scripts/v1/srs_md_to_docx.py SRS_Sample.md RoomBooking_SRS.docx
```

Output mong đợi:

```
Built: .../RoomBooking_SRS.docx
  headings=40, tables=21, total blocks=92
```

### 4 · Mở & verify

Mở `.docx` trong Word — field Mục lục tự cập nhật. Đối chiếu:

- Trang bìa độc lập (logo + "RoomBooking" + version + metadata)
- Mục lục độc lập, cấp 1-3
- "Lịch sử Phiên bản" độc lập 1 trang, không numbering
- Heading numbering: `1 Giới thiệu` … `3.1.2.1 Sơ đồ luồng`; sub-mục `A. / B.`
- Bảng Use Case có header merge 1 ô; bảng thành phần có STT/ID `COM-3123-001`…
- Hình căn giữa, đánh số `Hình 3.1.2.2-1`
- Footer `RoomBooking · Software Requirements Specification    Trang X / Y`

## Patterns demonstrated

- [`content-format-separation`](../../patterns/v1/content-format-separation.md) — nội dung `.md` thuần, format do `srs_format.py` áp, generator lo mã ID & số hình & numbering & merge ô.

## What went right · what to avoid

| ✅ Nên | ❌ Tránh |
|---|---|
| Để trống ô STT/ID — generator tự sinh | Điền sẵn `COM-…` trong .md (sẽ bị ghi đè / trùng) |
| Ghi caption `Hình [mô tả]` không số | Đánh số hình thủ công `Hình 1.` |
| Đóng Word trước khi chạy generator | Chạy generator khi `.docx` đang mở (lỗi Permission denied) |
| Dùng giá trị Loại/Thuộc tính trong Legend | Tự chế Loại component mới ngoài Legend |
