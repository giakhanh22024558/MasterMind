---
name: analysis
description: Phân tích Change Request (CR) thành hai artifact — Gap Analysis (so sánh CR với SRS/hệ thống hiện tại theo As-Is / To-Be) và Impact Analysis (phân rã CR thành task BA/FE/BE, estimation man-hours, module bị ảnh hưởng, quyết định sprint). Xuất sheet .xlsx theo chuẩn style chung của repo. Dùng khi khách hàng gửi yêu cầu thay đổi và cần đánh giá khoảng cách + tác động trước khi đưa vào sprint.
---

# analysis — Gap Analysis & Impact Analysis cho Change Request

Khi khách hàng gửi **Change Request (CR)**, không đưa thẳng vào sprint. Skill này tạo hai artifact phân tích để ra quyết định có cơ sở:

| Artifact | Trả lời câu hỏi | Sản phẩm |
|---|---|---|
| **Gap Analysis** | CR khác gì so với hệ thống/SRS hiện tại? | Bảng As-Is → To-Be, Gap Type, Impact Level |
| **Impact Analysis** | Làm CR này tốn gì, đụng tới đâu? | Bảng task BA/FE/BE, Estimation, Impacted Module, Decision |

→ Người dùng **phê duyệt Impact Analysis** rồi mới quyết định CR nào vào sprint.

## Khi nào dùng skill này

Invoke khi:

- Khách hàng gửi **một hoặc nhiều CR / feedback** cần đánh giá
- Cần **so sánh** yêu cầu mới với SRS / hệ thống hiện tại (Gap Analysis)
- Cần **ước lượng công sức + phạm vi ảnh hưởng** của CR (Impact Analysis)
- Cần một sheet quyết định để PM duyệt và phân bổ sprint

## Bước đầu tiên trong mọi công việc

1. **Discover conventions** — tìm `<project-root>/analysis-conventions.md` theo [`core/meta/conventions-as-data-pattern/`](../../../../core/meta/conventions-as-data-pattern/)
2. **Áp convention dự án**; fallback về [`conventions-defaults/`](conventions-defaults/) (gồm **chuẩn style .xlsx chung**)
3. **Acknowledge nguồn** khi giải thích lựa chọn

## Quy trình 2 bước

### Bước 1 · Gap Analysis

1. Thu thập danh sách CR (từ `input/`, Google Sheet, hoặc khách cung cấp)
2. Với mỗi CR: đối chiếu SRS / hệ thống hiện tại → điền **As-Is** (hiện trạng) và **To-Be** (nguyên văn kỳ vọng khách)
3. Phân loại **Gap Type** + đánh **Impact Level**
4. Soạn bảng `.md` theo [`analysis-structure/`](analysis-structure/) → render `.xlsx`:
   `python scripts/analysis_md_to_xlsx.py gap <input.md> <output.xlsx>`

### Bước 2 · Impact Analysis

1. Từ Gap Analysis, với mỗi CR phân rã **Implementation** thành 3 phần — **BA / FE / BE** — mỗi phần ghi nội dung task dạng gạch đầu dòng
2. **Estimation** man-hours cho từng phần BA / FE / BE
3. Xác định **Impacted Module** — các module tính năng bị ảnh hưởng + ghi chú ngắn cần đổi gì
4. Đề xuất **Decision**: This Sprint / Next Sprint / Another Sprint / Invalid · Out-of-scope
5. Soạn bảng `.md` → render `.xlsx`:
   `python scripts/analysis_md_to_xlsx.py impact <input.md> <output.xlsx>`
6. **Trình người dùng phê duyệt** — Decision chỉ là đề xuất; PM quyết định cuối

## Content modules

| Module | Mục đích |
|---|---|
| [`analysis-structure/`](analysis-structure/) | Đặc tả cấu trúc cột bảng Gap Analysis & Impact Analysis |
| [`conventions-schema/`](conventions-schema/) | Convention dự án cần khai (thang estimation, nhãn Decision...) |
| [`conventions-defaults/`](conventions-defaults/) | Mặc định — **chuẩn style .xlsx chung** + Gap Type / Decision mặc định |
| [`patterns/`](patterns/) | Pattern: Gap-then-Impact (gap trước, impact sau) |
| [`examples/`](examples/) | Worked walkthrough phân tích một CR |
| [`scripts/`](scripts/) | `xlsx_style.py` (chuẩn style) + `analysis_md_to_xlsx.py` (renderer) |

## Nguyên tắc cốt lõi

- **Gap trước, Impact sau** — không ước lượng tác động khi chưa rõ khoảng cách
- **To-Be giữ nguyên văn khách** — không diễn giải lại lời khách ở cột kỳ vọng
- **Decision là đề xuất** — quyết định sprint thuộc về người dùng/PM
- **Style .xlsx luôn theo chuẩn chung** — mọi sheet dùng `xlsx_style.py` (header `#1F4E79`, border `#BFBFBF`...)

## Anti-patterns

- ❌ Đưa CR thẳng vào sprint mà bỏ qua Gap + Impact Analysis
- ❌ Tự quyết định sprint thay người dùng — chỉ đề xuất ở cột Decision
- ❌ Viết task Implementation thành một đoạn liền — phải gạch đầu dòng từng việc
- ❌ Tự chế màu header / border riêng cho .xlsx — dùng `xlsx_style.py`

## Cross-references

| Reference | Dùng cho |
|---|---|
| [`core/meta/`](../../../../core/meta/) | Uniform structure · conventions-as-data |
| [`core/meta/atomic-edits-pattern/`](../../../../core/meta/atomic-edits-pattern/) | Renderer ghi `.xlsx` (file sync-prone) — đóng Excel trước khi chạy |
| [`business_analysis` pipeline](../../business_analysis/) | Skill này là nhánh xử lý Change Request của pipeline BA |
| [`features`](../features/) | CR được duyệt → tách thành feature đưa vào sprint |
| [`srs`](../srs/) | Nguồn so sánh As-Is cho Gap Analysis |
