# Cross-reference — Kỹ thuật tham chiếu chéo

> **Trạng thái: STUB — chờ bổ sung chi tiết.**
> Folder này được tạo trước để giữ chỗ cho kỹ thuật cross-reference. Đặc tả chi tiết sẽ được người dùng cung cấp sau.

## Phạm vi

Kỹ thuật mà agent dùng để chỉnh sửa file **User layer** (`.docx`, `.drawio`) sau khi đã đọc nội dung từ **Agent layer** (`.md`) — xem [`core-rule`](../../core-rule/).

Mục tiêu: mỗi phần tử ở User layer (đoạn văn, ô bảng, hình, node draw.io) phải truy vết được về đúng vị trí nguồn ở Agent layer, để mọi chỉnh sửa luôn nhất quán và không lệch giữa hai tầng.

## Cần đặc tả (TODO)

- [ ] Cơ chế định danh / neo (anchor) giữa `.md` và `.docx` / `.drawio`
- [ ] Quy trình resolve một cross-reference khi chỉnh sửa
- [ ] Xử lý khi Agent layer và User layer lệch nhau
- [ ] Ví dụ minh họa cụ thể cho document (`.docx`) và diagram (`.drawio`)

*Khi hoàn thiện đặc tả: cập nhật file này, bỏ nhãn STUB, và bump version nếu cần theo [`versioning-pattern`](../../meta/versioning-pattern/).*
