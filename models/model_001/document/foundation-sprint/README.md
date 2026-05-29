# foundation-sprint (human overview)

The **Sprint 0 / foundation** companion to [`features`](../features/). Where `features` decomposes business capability into **Epic → Feature → User Story**, this skill decomposes the **cross-cutting foundation** into **Topic → Concern → Task → ACs**.

- **Topic** ≈ Epic — a theme grouping concerns
- **Concern** ≈ Feature — a technical area of foundation
- **Task** (`FND-`) ≈ User Story — a buildable enabler
- **ACs** — Definition-of-Done per task, in a **separate** file

Use it for the work that serves *every* module and must exist before feature build: architecture, infra/CI-CD, data model, auth/RBAC, design system, UX guidelines, business-rule baselines, inert scaffolds, public site. It also carries the **gate-buffer + parallelisation** scheduling pattern: finish ~15 days before each gate, run concerns in parallel.

Start at [`SKILL.md`](SKILL.md). Canonical structure: [`foundation-register/`](foundation-register/). Patterns: [`patterns/`](patterns/). Example: [`examples/walkthrough.md`](examples/walkthrough.md).
