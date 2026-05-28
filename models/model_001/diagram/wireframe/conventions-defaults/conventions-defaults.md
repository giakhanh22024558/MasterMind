# wireframe · conventions defaults

Applied when `<project-root>/wireframe-conventions.md` does not specify a value.

| Item | Default | Notes |
|---|---|---|
| `format` | `html` | Single self-contained HTML file (no external assets). |
| `output_dir` | `output/wireframes/` | One file per screen. |
| `file_name` | `WF-{nn:02d}-{slug}.html` | e.g. `WF-01-create-quotation-standalone.html`. The `WF-NN` ties to the change tracker. |
| `language` | `en` | Client-facing wireframes default to English so they can be sent for sign-off. Switch to the client's language only if the project says so. |
| `assumptions_tracker.kind` | `qa_sheet` | Log assumptions to a `WF Assumptions` sheet in the project Q&A workbook; fall back to `docs/wireframe-changes.md` if no Q&A workbook exists. |
| `assumptions_tracker.id_format` | `A-WF{wf_nn}-{nn:02d}` | e.g. `A-WF01-04`. |
| Sheet / page width | ~1180px centered | Low-fi sheet on a gray page. |
| Palette | grayscale + amber `#b8860b` badges + green `#1a7f37` "NEW" flag | Color is structural/annotation only. |
| Sidecar | `context/wireframes.md` (or per-file `context/<name>.html.md`) | Token-cheap description per the Core Rule. |
| Status values (change tracker) | `To-do / In-design / Review / Done` | For the **wireframe** change tracker (per-screen progress). |
| Assumption status | **none** | Assumptions have no approval workflow — dev builds against them; later feedback is absorbed on the relevant US. Tracker columns: `ID · Wireframe · Field/Area · Assumption · Client feedback`. |

## Defaults rationale

- **HTML + self-contained**: opens offline in any browser, exports to PDF/screenshot, diff-able in git, fast to iterate.
- **English default**: wireframes are usually produced to send to a client for awareness; English is the safe lingua franca unless the project states otherwise.
- **Build against assumptions, don't block**: a badge on the screen is paired with a tracker row so the client is aware — but dev proceeds immediately. There is no "confirm/approve" gate; client feedback becomes a change on the affected user story.
