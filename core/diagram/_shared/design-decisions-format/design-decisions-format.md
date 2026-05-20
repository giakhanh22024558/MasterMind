# Design-decisions row format

The canonical row template for `research/design-decisions.md`. Every architectural choice (whether applied or deferred) becomes one row.

## Why a master table

Architecture evolves. Without a master log of "we chose X over Y because Z", every refactor relitigates the same questions. The design-decisions table is the institutional memory.

## Row schema (8 columns)

```
| ID | Decision point | Chosen | Alternatives | Rationale | Trigger to revisit | Status | Spec Authority |
```

### Column meanings

| Column | Content |
|---|---|
| **ID** | Stable identifier · grouped by category prefix (see below) |
| **Decision point** | Bold question being answered. Frame as a *question*, not a noun. |
| **Chosen** | The committed answer. Bold if highly relevant. Include "REVISED YYYY-MM-DD" prefix when overturning a prior choice. |
| **Alternatives** | Numbered list A/B/C with each option's trade-off. The chosen one is also listed (marked "chosen"). |
| **Rationale** | Why this option wins. Cite spec mandates · vendor proposals · audit findings. |
| **Trigger to revisit** | What event/discovery would re-open this decision. "Vendor proposal" · "Audit feedback" · "Phase 2 kickoff" · "Spec clarification on X". |
| **Status** | 🟢 Locked-in · 🟡 Provisional · 🔴 Blocker · 🔵 Phase 2 placeholder |
| **Spec Authority** | Doc/section/standard IDs that gate this decision. |

## ID category prefixes (suggested taxonomy)

Pick prefixes that match your project's domain. Example taxonomy:

| Prefix | Category | Example use |
|---|---|---|
| `S<n>` | System-wide / infra | audit log backend, retention policy |
| `B<n>` | Backend (cloud-side) | tile pricing tier, max device count |
| `M<n>` | Mobile / client | OS versions, framework choice |
| `M0<a-z>` | Mobile architecture sub-decisions | structural choices within a single component |
| `O<n>` | Operations console / admin web | RBAC, sub-zone grouping |
| `F<n>` | Sync / Firestore-equivalent | write semantics, security rules |
| `V<n>` | Visual / diagram conventions | edge granularity, layout |
| `C<n>` | Compliance interpretation | how to operationalize a mandate |

Adapt to your project's structure. Use `<prefix><number>` for top-level · `<prefix>0<letter>` for sub-decisions to a category.

## Status semantics

| Status | Meaning |
|---|---|
| 🟢 **Locked-in** | Spec-mandated or client-confirmed. Don't re-decide without escalation. |
| 🟡 **Provisional** | Defensible choice but reversible. Most rows start here. |
| 🔴 **Blocker** | Open question blocking next milestone. Needs vendor input or client decision. |
| 🔵 **Phase 2 placeholder** | Deferred to future phase. Track for visibility. |

Status moves left → right (typically `🟡 Provisional → 🟢 Locked-in`) or right → left when audits reveal new conflicts.

## Revision protocol

When a row changes after first commit:

1. **Add date marker** in "Chosen" column: `REVISED YYYY-MM-DD: <new choice>`
2. **Move old choice to Alternatives** marked "rejected after audit/spec clarification"
3. **Update Status** if escalation needed
4. **Add to Rationale** what triggered revision

Never delete a row · revisions are part of the audit trail.

## Numbered list at bottom

Below the table, maintain a flat numbered list grouped by Status:

```markdown
## Decisions to confirm with client (sorted by urgency)

### 🔴 Blocker (need before next milestone)
1. **<row-ID>** — short description (one line)
2. ...

### 🟡 Provisional (confirm during proposal review)
N. ...

### 🟢 Locked-in (spec or client confirmed)
N. ...

### 🔵 Phase 2 placeholders
N. ...
```

Why: the table is dense; the list is glanceable for status meetings. Both stay in sync.

## Row template (copy-paste)

```markdown
| <prefix><number> | **<question being decided>** | **<chosen answer>** | A) <option> (chosen)<br/>B) <option><br/>C) <option> | <why chosen wins · spec citations · audit context> | <event that re-opens this> | 🟡 Provisional | **<SPEC-ID>** · **<SPEC-ID>** · related to **<other-decision-id>** |
```

## When to create a new row

- Spec audit reveals an architectural choice not yet captured → create row
- Two valid options identified · need to pick one → create row with both options
- Existing row needs amendment → revise existing row (don't create duplicate)
- "Should we do X?" question from team → row with status 🟡 Provisional

## When NOT to create a row

- Implementation detail (which library version, file naming) — code/comments handle it
- One-time tactical choice (renaming a variable, fixing a typo)
- Choices fully determined by spec (no real alternatives) — note in compliance matrix instead

## Cross-referencing from other docs

Edge labels, subsystem docs, and compliance rules reference design-decisions by ID:

- **Edge labels**: `(<decision-id> <characterization>)` style (see [`../edge-labels-general/`](../edge-labels-general/))
- **Subsystem docs**: cite IDs in "Per-module audit findings" sections
- **Compliance matrix**: link rows to their authoritative design decisions

The decision table is the **single source of truth**. Every other doc references it; none of them duplicate the decision content.

## Worked example sequence

A new audit reveals a conflict:
1. Spec says X · current architecture says Y · they contradict
2. Create new row capturing the conflict with both X and Y as options
3. Status `🔴 Blocker` because architecture can't proceed without resolution
4. Update existing related rows to note dependency
5. Update numbered list at bottom to reflect Blocker status

When client/vendor responds:
6. Update "Chosen" with date marker: `REVISED YYYY-MM-DD: <X>`
7. Move Y to alternatives as rejected
8. Status → 🟢 Locked-in
9. Apply architecture changes (new edges, label updates, etc.) referencing this row ID
