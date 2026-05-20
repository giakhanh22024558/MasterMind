# Core Rule — Quy tắc lõi bất biến (3 tầng)

Quy tắc nền tảng mà **mọi model** trong MasterMind phải tuân thủ — bất kể input context hay định dạng tài liệu đầu ra khác nhau thế nào. Đây là phần lõi (`core/`): không thay đổi khi thêm dự án/model mới.

## Ba tầng

| Tầng | Vai trò | Sống ở đâu |
|---|---|---|
| **1 · Input → Context** | Phân tích mọi input thô (yêu cầu, tài liệu nguồn, ảnh...) thành Markdown có cấu trúc. File `.md` này là **context** — nguồn sự thật về *nội dung*. | File `.md` |
| **2 · Agent layer** | Chuẩn hóa *định dạng / hình thức* thành code Python. Tầng do máy quản lý: nội dung ở `.md`, format ở Python. | File `.md` + code Python |
| **3 · User layer** | Bản giao cho người dùng — file `.docx`, `.drawio`. Đây là tầng "hiển thị", **không** phải nguồn sự thật. | `.docx`, `.drawio` |

```
[input thô] ──phân tích──▶  .md (context)  ─┐
                                             ├──▶  AGENT LAYER  (nguồn sự thật)
            format ──chuẩn hóa──▶  Python   ─┘          │
                                                  render │
                                                         ▼
                                            USER LAYER  (.docx / .drawio)
```

## Quy tắc bắt buộc khi chỉnh sửa User layer

Khi agent được yêu cầu chỉnh sửa `.docx` hoặc `.drawio`:

1. **Luôn grep nội dung từ Agent layer trước** — đọc file `.md` (và code Python format) để lấy nội dung/ngữ cảnh authoritative.
2. **Sau đó mới chỉnh sửa** `.docx` / `.drawio` bằng **kỹ thuật cross-reference** — xem [`cross-reference`](../../cross-reference/).
3. **Không bao giờ** sửa thẳng `.docx`/`.drawio` rồi mong đồng bộ ngược về `.md`. Nguồn sự thật luôn là Agent layer.

## Vì sao

- Tách **nội dung** (`.md`) khỏi **hình thức** (Python) → sửa cái này không đụng cái kia.
- User layer là output dẫn xuất → tái sinh được, không giữ trạng thái độc nhất.
- Mọi model dù khác domain (SRS, architecture diagram...) đều quy về cùng một dòng chảy → tái sử dụng được phần `core/`.

## Áp dụng

Mọi skill trong `models/model_NNN/` — diagram, document, hay loại mới — phải nêu rõ trong `SKILL.md` của nó: đâu là `.md` context, đâu là code Python format, đâu là file User layer, và tuân đúng dòng chảy 3 tầng trên.
