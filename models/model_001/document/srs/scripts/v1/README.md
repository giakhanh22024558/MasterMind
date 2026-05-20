# model_001_srs · scripts

Logic của skill — bộ công cụ sinh tài liệu SRS `.docx`.

## Available scripts

| Script | Mục đích |
|---|---|
| [`srs_format.py`](srs_format.py) | **Chuẩn format** — hằng số màu/font/page, style heading, numbering đa cấp, API dựng trang bìa / TOC / bảng / callout / legend. Là module được `srs_md_to_docx.py` import |
| [`srs_md_to_docx.py`](srs_md_to_docx.py) | **Generator** — parse file `.md`, áp `srs_format`, xử lý merge ô / mã STT-ID / số hình / page break → xuất `.docx` |
| [`assets/srs_logo.png`](assets/srs_logo.png) | Logo trang bìa (asset nhị phân, bắt buộc) |

## Cài đặt

```bash
pip install python-docx
```

## Dùng

```bash
# cú pháp đầy đủ
python srs_md_to_docx.py <input.md> <output.docx>

# không tham số -> dùng file mẫu examples/v1/SRS_Sample.md, xuất SRS_Sample.docx ở thư mục hiện tại
python srs_md_to_docx.py
```

## Smoke test riêng phần format

```bash
python srs_format.py        # sinh _srs_format_smoketest.docx kiểm tra style
```

## Lưu ý (atomic edits)

Generator ghi file `.docx` — có thể là file sync-prone (OneDrive/Drive). Theo [`meta/atomic-edits-pattern/`](../../../../../../core/meta/atomic-edits-pattern/):

- **Đóng Word** trước khi chạy (file đang mở → lỗi `Permission denied`)
- Generator đọc `.md` 1 lần / ghi `.docx` 1 lần — re-run được, idempotent
- `srs_format.py` và `srs_md_to_docx.py` phải nằm **cùng thư mục** (`srs_md_to_docx` import `srs_format`)
- `assets/srs_logo.png` phải nằm cạnh `srs_format.py` (đường dẫn logo tính tương đối theo file script)

## Khi cập nhật format

- Sửa hằng số / style → sửa trong `srs_format.py`
- Sửa cách parse `.md` / quy ước tự sinh → sửa trong `srs_md_to_docx.py`
- Thay đổi phá vỡ tương thích → bump `scripts/v1` → `scripts/v2` theo [`meta/versioning-pattern/`](../../../../../../core/meta/versioning-pattern/)

## How to add a new script

1. Tạo `<verb>-<noun>.py`, có docstring nêu mục đích
2. Cập nhật bảng "Available scripts" ở trên
