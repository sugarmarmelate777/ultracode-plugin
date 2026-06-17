---
name: Parallel TDD Swarm (Parallel Execution)
version: "1.0.0"
depends_on: []
description: Optimizes the Test-Driven Development workflow by spawning parallel sub-agents or executing parallel tool calls for tests and implementation logic.
---

# Parallel TDD Swarm (Parallel Execution)

## Directives

1. **Parallel Tooling:**
   - Once a `spec.md` is approved, do not perform file edits one by one if they are independent.
   - Use concurrent execution of your available file creation or editing tools to generate the Test file and the Implementation file at the exact same time in a single thought block.
   - **CRITICAL RACE CONDITION GUARD:** Never assign multiple sub-agents or concurrent tool calls to modify the same file simultaneously. Implement logical file locking.
   - **Staging Isolation (MANDATORY):** Sub-agents MUST NOT write directly to `src/` or the project source tree. Instead:
     - Each sub-agent writes its output to `.ultracode/staging/<agent-id>/` (e.g., `.ultracode/staging/code-writer/component.ts`, `.ultracode/staging/test-writer/component.test.ts`).
     - The Orchestrator (or main agent) reads from staging, applies Zero-Trust validation on each artifact, and only then copies validated files to their final locations in the project tree.
     - If any sub-agent artifact fails validation, do NOT merge any files — discard all staging artifacts for that round and re-spawn with corrected instructions.

2. **Synchronization:**
   - After ALL parallel sub-agents complete and their staging artifacts are validated, copy the validated files from `.ultracode/staging/` to their target locations in the project tree.
   - Invoke your available terminal execution tools to run the tests against the merged files.
   - The test runner acts as the synchronization barrier for the parallel tasks.

3. **Cleanup:**
   - After tests pass and files are merged, delete the `.ultracode/staging/` directory to prevent stale artifacts from contaminating future rounds.
