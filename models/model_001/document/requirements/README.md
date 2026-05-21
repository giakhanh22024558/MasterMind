# requirements — README

A skill that consolidates any project input into **one requirements table**.

## Quick start

| If you want to… | Read |
|---|---|
| Understand the skill in one page | [`SKILL.md`](SKILL.md) |
| Know the table structure | [`requirements-table/`](requirements-table/) |
| Know what a project declares | [`conventions-schema/`](conventions-schema/) |
| See a worked example | [`examples/`](examples/) |

## The artifact

| Form | Where |
|---|---|
| Requirements table `.md` (timestamp-batched) — source of truth | `context/` |
| `requirements.xlsx` — manual pilot copy | `output/` |

## Columns

`Req code` (REQ-xxxx) · `Topic` · `Criteria` · `Description` · `Ref. Docs` · `Q&A` *(optional)* · `Remarks` *(optional)*

## Stack

- **Markdown** for the `.md` context table
- **Python** (`openpyxl`) for the `.xlsx` — rendered by the pipeline's `ba_md_to_xlsx.py`

## License

Internal. Adapt freely. No warranty.
