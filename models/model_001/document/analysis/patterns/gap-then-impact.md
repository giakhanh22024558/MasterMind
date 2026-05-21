# Pattern · Gap-then-Impact

## Problem

Khi khách gửi Change Request, cám dỗ thường gặp là **nhảy thẳng vào ước lượng** ("cái này chắc 2 ngày") hoặc **đưa luôn vào sprint**. Hệ quả:

- Ước lượng sai vì chưa rõ thực sự phải đổi những gì so với hiện trạng
- Bỏ sót tác động chéo (CR đụng tới module khác)
- Không có cơ sở rõ ràng để PM/khách phê duyệt
- CR vô nghĩa (hệ thống đã đáp ứng) vẫn bị bỏ công làm

## Solution

Tách việc phân tích CR thành **hai bước tuần tự, không đảo thứ tự**:

```
CR  ──▶  [1] Gap Analysis  ──▶  [2] Impact Analysis  ──▶  Phê duyệt  ──▶  Sprint
         "khác gì hiện tại"     "tốn gì, đụng đâu"        (người dùng)
```

### Bước 1 — Gap Analysis: xác định KHOẢNG CÁCH

Trả lời "CR khác gì so với hệ thống/SRS hiện tại": ghi **As-Is** (hiện trạng) và **To-Be** (nguyên văn kỳ vọng khách), phân loại **Gap Type**. Bước này lọc sớm các CR `No Change` (hệ thống đã đáp ứng) → không cần đi tiếp.

### Bước 2 — Impact Analysis: xác định TÁC ĐỘNG

Chỉ khi đã rõ khoảng cách mới ước lượng được đúng. Phân rã thành task **BA/FE/BE**, estimate **man-hours**, liệt kê **Impacted Module**, đề xuất **Decision**.

### Bước 3 — Phê duyệt

Decision ở Impact Analysis chỉ là **đề xuất**. Người dùng/PM xem sheet, duyệt, quyết định CR nào vào sprint nào.

## Trade-offs

**Ưu:** ước lượng có cơ sở; lọc sớm CR vô nghĩa; PM có sheet rõ ràng để duyệt; truy vết được lý do mỗi quyết định.

**Nhược:** thêm một bước trước khi code — không phù hợp với CR cực nhỏ/hiển nhiên (có thể làm gọn nhưng không bỏ hẳn).

## When NOT to use

- CR là bug fix nhỏ, hiển nhiên, không đụng nhiều module → có thể xử lý nhanh, không cần sheet đầy đủ.
- Yêu cầu mới hoàn toàn ở quy mô dự án (không phải "thay đổi") → đi pipeline BA từ đầu (requirements → …), không phải luồng CR.

## Cross-references

- Là nhánh xử lý Change Request của [pipeline `business_analysis`](../../../business_analysis/).
- CR được duyệt → [`features`](../../features/) tách thành feature đưa vào sprint.
