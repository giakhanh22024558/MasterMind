# Cross-reference technique

> **Status: STUB — detailed specification pending.**
> This folder is created up front to reserve a place for the cross-reference technique. The detailed specification will be provided by the user later.

## Scope

The technique an agent uses to edit **User-layer** files (`.docx`, `.drawio`) after reading content from the **Agent layer** (`.md`) — see [`core-rule`](../../core-rule/).

Goal: every element in the User layer (paragraph, table cell, figure, draw.io node) must be traceable back to its exact source position in the Agent layer, so that every edit stays consistent and never drifts between the two layers.

## To be specified (TODO)

- [ ] Anchor / identification mechanism between `.md` and `.docx` / `.drawio`
- [ ] Procedure for resolving a cross-reference during an edit
- [ ] Handling divergence between the Agent layer and the User layer
- [ ] Concrete examples for documents (`.docx`) and diagrams (`.drawio`)

*When the specification is complete: update this file, remove the STUB label, and bump the version if needed per [`versioning-pattern`](../../meta/versioning-pattern/).*
