# Requirements

> Backed by skill [`document/requirements`](../MasterMind/models/model_001/document/requirements/).
> Mỗi requirement là 1 row, ID auto `REQ-XXXX`. Source mỗi REQ phải truy được về file/page trong `input/`.

**Source materials:** `<liệt kê file trong input/ làm source>`
**Last updated:** `<YYYY-MM-DD>`

| REQ ID | Topic | Description | Source | Priority | Status |
|---|---|---|---|---|---|
| REQ-0001 |  |  | input/<file>.docx p.<n> |  | Draft |
| REQ-0002 |  |  |  |  |  |

## Cách điền

1. Agent đọc `input/*.docx` / `input/*.xlsx` / `input/*.pdf` → sinh `context/<file>.md`
2. Agent extract requirement statements → fill bảng trên
3. Mỗi REQ giữ Source rõ ràng (vd `input/SRS_v1.docx Section 3.2.1`)
4. Priority: `Critical / High / Medium / Low` (override trong `conventions/requirements-conventions.md`)
5. Status: `Draft / Reviewed / Approved / Deprecated`

## Output downstream

- `document/features` đọc bảng này → derive Epic / Feature / Story
- `document/srs` đọc bảng này + ERD → sinh use-case spec
