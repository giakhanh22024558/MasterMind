# analysis · scripts

| Script | Mục đích |
|---|---|
| [`xlsx_style.py`](xlsx_style.py) | **Chuẩn style .xlsx chung** — hằng số màu/border/độ rộng + hàm style header, viền, freeze, dropdown, combo-box. Mọi script sinh `.xlsx` import module này để đảm bảo format đồng nhất |
| [`analysis_md_to_xlsx.py`](analysis_md_to_xlsx.py) | Renderer — đọc bảng Markdown, xuất `.xlsx` Gap Analysis hoặc Impact Analysis theo `xlsx_style.py` |

## Cài đặt

```bash
pip install openpyxl
```

## Dùng

```bash
# Gap Analysis: bảng phẳng 1 hàng header
python analysis_md_to_xlsx.py gap     <input.md> <output.xlsx>

# Impact Analysis: bảng phẳng 9 cột -> header 2 tầng (Implementation/Estimation merge)
python analysis_md_to_xlsx.py impact  <input.md> <output.xlsx>
```

`<input.md>` theo format tại [`../analysis-structure/`](../analysis-structure/).

## Chuẩn style .xlsx — vì sao dùng `xlsx_style.py`

Để **mọi file .xlsx trong repo trông giống nhau** (cùng màu header `#1F4E79`, cùng viền `#BFBFBF`, cùng freeze/filter, cùng thang độ rộng cột). Bất kỳ script mới nào sinh `.xlsx` (kể cả ngoài skill này) nên `import xlsx_style` thay vì tự đặt màu/viền — xem [`../conventions-defaults/`](../conventions-defaults/).

## Lưu ý (atomic edits)

Renderer ghi file `.xlsx` — có thể sync-prone. Theo [`core/meta/atomic-edits-pattern/`](../../../../../core/meta/atomic-edits-pattern/):

- **Đóng Excel** trước khi chạy (file đang mở → lỗi `Permission denied`)
- `xlsx_style.py` và `analysis_md_to_xlsx.py` phải nằm **cùng thư mục**
- Script đọc/ghi 1 lần, re-run được

## How to add a new script

1. Tạo `<verb>-<noun>.py`, `import xlsx_style` cho mọi định dạng `.xlsx`
2. Cập nhật bảng "Available scripts" ở trên
