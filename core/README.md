# core

Phần **lõi bất biến** của MasterMind. Mọi thứ trong `core/` dùng chung cho mọi dự án và **không thay đổi** khi thêm model mới.

## Nội dung

| Folder | Vai trò |
|---|---|
| [`core-rule/`](core-rule/) | Quy tắc lõi 3 tầng (input → `.md` → Python → `.docx`/`.drawio`) — mọi model phải tuân |
| [`cross-reference/`](cross-reference/) | Kỹ thuật tham chiếu chéo khi sửa file user layer *(stub — chờ chi tiết)* |
| [`diagram/`](diagram/) | Khung lõi skill diagram — methodology `_shared/`, versioning, project template |
| [`document/`](document/) | Khung lõi skill sinh tài liệu `.docx` |
| [`meta/`](meta/) | Meta-skill — cách tạo một skill mới (folder structure, versioning, patterns) |
| [`template/`](template/) | Scaffold khởi tạo skill mới |

## Nguyên tắc

- `core/` **không** chứa skill cụ thể của dự án — skill cụ thể sống ở [`../models/`](../models/).
- `core/` **không** bị sửa khi thêm dự án/model mới. Nếu buộc phải sửa core → đó là thay đổi toàn cục, cân nhắc kỹ tác động lên mọi model.
- Mọi skill trong `models/` tham chiếu ngược về `core/` cho phần methodology dùng chung.
