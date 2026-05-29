# foundation-sprint · scripts

No dedicated scripts yet. The foundation register + ACs file are Markdown; render to `.xlsx` (if needed) with the shared BA renderer, treating:

- the **register** like the feature backlog (Topic/Concern/Task rows analogous to Epic/Feature/Story rows), and
- the **ACs file** like the Acceptance-Criteria sheet (one row per `AC-FND-{task}-{nn}`).

See [`../../../business_analysis/scripts/ba_md_to_xlsx.py`](../../../business_analysis/scripts/) for the renderer to adapt. Add foundation-specific helpers here if a project needs them (e.g. a Gantt generator for the gate-buffer schedule).
