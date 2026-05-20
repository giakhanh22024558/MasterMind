# models

The **models** — each `model_NNN/` is a cluster of concrete skills for one project / context. Users create new models on demand.

## Structure of a model

```
models/model_NNN/
├── context/           ← runtime — the user's input/ ingested as context.md (git-ignored)
├── diagram/
│   └── <type>/        ← concrete diagram skill (e.g. architecture)
└── document/
    └── <type>/        ← concrete document skill (e.g. srs)
```

Each model holds skill categories (`diagram`, `document`...); inside each category are more specific skills (`architecture`, `srs`...). The `context/` folder is created at runtime when the model ingests the user's `input/` — see the [Core Rule](../core/core-rule/).

## Existing models

| Model | Skills |
|---|---|
| [`model_001/`](model_001/) | `diagram/architecture` · `document/srs` |

## Rule

However different the input context or output format, **every model must follow the [Core Rule](../core/core-rule/)**. A model holds only the *specific* part; the *shared* part (methodology, meta) always references back to [`../core/`](../core/).
