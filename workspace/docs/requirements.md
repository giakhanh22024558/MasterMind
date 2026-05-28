# Requirements

> Backed by skill [`document/requirements`](../MasterMind/models/model_001/document/requirements/).
> Each requirement is one row, ID auto-generated as `REQ-XXXX`. Every REQ's Source must be traceable back to a file/page in `input/`.

**Source materials:** `<list the files in input/ used as source>`
**Last updated:** `<YYYY-MM-DD>`

| REQ ID | Topic | Description | Source | Priority | Status |
|---|---|---|---|---|---|
| REQ-0001 |  |  | input/<file>.docx p.<n> |  | Draft |
| REQ-0002 |  |  |  |  |  |

## How to fill

1. Agent reads `input/*.docx` / `input/*.xlsx` / `input/*.pdf` → generates `context/<file>.md`
2. Agent extracts requirement statements → fills the table above
3. Each REQ keeps a clear Source (e.g. `input/SRS_v1.docx Section 3.2.1`)
4. Priority: `Critical / High / Medium / Low` (override in `conventions/requirements-conventions.md`)
5. Status: `Draft / Reviewed / Approved / Deprecated`

## Downstream output

- `document/features` reads this table → derives Epic / Feature / Story
- `document/srs` reads this table + ERD → produces use-case specs
