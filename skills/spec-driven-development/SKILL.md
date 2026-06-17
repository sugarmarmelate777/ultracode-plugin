---
name: Spec-Driven Development (Blueprint Mode)
description: Forces the creation of a specification (spec.md) detailing edge cases and business logic before any code is planned or written.
---

# Spec-Driven Development (Blueprint Mode)

## Directives

1. **Complexity Threshold:**
   - A `spec.md` is MANDATORY only when a task meets ANY of these criteria:
     - Modifies 4 or more files (>=4)
     - Introduces a new architectural component (e.g., new database table, new API endpoint, new state management)
     - The user explicitly requests a spec or blueprint
   - For simple tasks (e.g., "add a button", "fix this CSS", "rename a variable"), skip `spec.md` and proceed directly to `implementation_plan.md` or inline execution.

2. **Spec Structure (when required):**
   - The `spec.md` must clearly define:
     - **Business Logic / Intent:** What exactly are we building and why?
     - **Inputs & Outputs:** Data structures, API contracts, or UI states.
     - **Edge Cases & Error Handling:** What happens on null inputs, network failures, or invalid states?
     - **Out of Scope:** Explicitly list what this feature will NOT do.

3. **Approval Gate:**
   - The USER must approve the `spec.md` before you proceed to the technical implementation plan. (Subject to Global CI Gate)

4. **Versioning (CRITICAL):**
   - If a `spec.md` already exists, do NOT silently overwrite it. Version it (e.g. `spec_v2.md`) to maintain a clean history.
