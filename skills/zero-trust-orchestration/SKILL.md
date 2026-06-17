---
name: Zero-Trust Orchestration (Cross-Agent Trust Boundaries)
version: "1.0.0"
depends_on: []
description: Mandates that the main agent validates and tests the output of any sub-agent before incorporating it into the project.
---

# Zero-Trust Orchestration (Cross-Agent Boundaries)

## Directives

1. **Untrusted Sub-Agents:**
   - When a sub-agent returns a report, code snippet, or analysis, DO NOT blindly assume it is correct.
   - Treat the sub-agent's output as a "draft" or "hypothesis".

2. **Mandatory Validation & Risk Classification:**
   - Apply validation based on risk level. For low-risk read-only tasks (like searches), apply minimal validation.
   - For high-risk tasks involving code changes, you MUST use the `Deterministic Verification` skill to run a test or linter on the proposed logic before applying it.

3. **Rejection Protocol:**
   - If a sub-agent's output fails validation, do not argue with it. Spawn a new, corrected sub-agent task, or handle the task yourself if it is trivial.
