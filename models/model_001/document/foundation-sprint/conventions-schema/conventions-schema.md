# foundation-sprint · conventions schema

What a project may declare in `<project-root>/foundation-sprint-conventions.md`. Anything omitted falls back to [`../conventions-defaults/`](../conventions-defaults/).

```yaml
# --- ID formats (width only; prefixes are canonical) ---
id_formats:
  topic: "TOPIC-{n:02d}"        # default
  task:  "FND-{n:03d}"          # default
  ac:    "AC-FND-{task}-{n:02d}"# default

# --- AC language ---
ac_writing:
  language: en                  # en (default) | vi

# --- Concern catalogue (override the default 10) ---
# List the concerns this project's foundation actually needs. Keep, drop,
# rename, or add. Order is build order.
concerns:
  - "Architecture & Technical Design"
  - "Infrastructure & CI/CD"
  # - "...project-specific concern..."

# --- Topic grouping (how concerns cluster into topics) ---
topics:
  - id: TOPIC-01
    name: "Architecture & Delivery Platform"
    concerns: ["Architecture & Technical Design", "Infrastructure & CI/CD"]
  # - id: TOPIC-02 ...

# --- Gate scheduling ---
first_gate:
  name: "Discovery"             # the gate the foundation sprint feeds
  date: "YYYY-MM-DD"
  pre_gate_buffer_days: 15      # feature/task freeze this many days before the gate
parallel_tracks: 8              # how many concerns can run concurrently

# --- File locations ---
files:
  register: "docs/planning.md"  # where the register lives
  acs:      "docs/sprint-0-acs.md"  # separate ACs sidecar
```

## What each block controls

| Block | Controls |
|---|---|
| `id_formats` | Suffix width of Topic / Task / AC codes (prefixes `TOPIC-`/`FND-`/`AC-FND-` are canonical) |
| `ac_writing.language` | Language of the Definition-of-Done criteria |
| `concerns` | The concern catalogue for this project (subset/extension of the default 10) |
| `topics` | How concerns group into Topics |
| `first_gate` + `pre_gate_buffer_days` | The pre-gate risk buffer the schedule must honour |
| `parallel_tracks` | Concurrency budget for [parallelisation](../patterns/gate-buffer-and-parallelisation.md) |
| `files` | Where the register and the separate ACs file live |

## Not overridable

- The 3-level hierarchy (Topic → Concern → Task) and the separate-ACs rule.
- The principle that standards/criteria are ACs, not Tasks; and that business-functional capabilities belong in [`features`](../../features/).
