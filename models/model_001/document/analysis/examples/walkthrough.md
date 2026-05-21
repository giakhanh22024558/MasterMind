# Example · Phân tích một Change Request

Walkthrough áp dụng skill `analysis` cho một CR giả định. Dùng placeholder generic.

## Setup

Khách gửi CR: *"Thêm chế độ xem danh sách dạng bảng cho màn dashboard"* — đặt mã `CR-01`.

## Bước 1 · Gap Analysis

Đối chiếu CR với SRS hiện tại, điền một hàng:

| CR ID | Topic | As-Is | To-Be (nguyên văn khách) | Gap Type | Impact Level |
|---|---|---|---|---|---|
| CR-01 | `<Module>` Dashboard | Dashboard chỉ có chế độ xem dạng thẻ | "Thêm chế độ xem dạng danh sách bảng" | Enhancement | P0 |

Render: `python scripts/analysis_md_to_xlsx.py gap gap.md output/gap.xlsx`

→ Lọc được: CR-01 là `Enhancement` thật sự (không phải `No Change`) → đi tiếp Bước 2.

## Bước 2 · Impact Analysis

Phân rã CR-01 thành task BA/FE/BE, estimate, module ảnh hưởng:

| CR ID | Impl · BA | Impl · FE | Impl · BE | Est BA | Est FE | Est BE | Impacted Module | Decision |
|---|---|---|---|---|---|---|---|---|
| CR-01 | • Cập nhật đặc tả view mode<br>• Soạn đặc tả cột bảng | • Implement table view<br>• Toggle Thẻ ↔ Bảng | • Đảm bảo API trả đủ field cho cột | 4 | 16 | 3 | `<Module>` Dashboard — thêm view mode; component toggle dùng chung | Next Sprint |

Render: `python scripts/analysis_md_to_xlsx.py impact impact.md output/impact.xlsx`

→ Sheet tự dựng header 2 tầng, tách bullet, cộng dòng TỔNG, gắn dropdown Decision.

## Bước 3 · Phê duyệt

Trình sheet Impact Analysis cho PM. PM xem estimation (BA 4h · FE 16h · BE 3h = 23h), tác động, rồi chốt cột Decision. CR được chọn → chuyển sang skill [`features`](../../features/) để tách thành feature đưa vào sprint.

## Patterns demonstrated

- [`gap-then-impact`](../patterns/gap-then-impact.md) — Gap trước, Impact sau, rồi mới phê duyệt.

## What went right · what to avoid

| ✅ Nên | ❌ Tránh |
|---|---|
| Ghi To-Be nguyên văn lời khách | Diễn giải lại kỳ vọng khách |
| Task Implementation gạch đầu dòng | Viết task thành một đoạn liền |
| Để PM chốt Decision | BA tự quyết CR vào sprint |
| Render .xlsx bằng `analysis_md_to_xlsx.py` | Tự định dạng .xlsx thủ công |
