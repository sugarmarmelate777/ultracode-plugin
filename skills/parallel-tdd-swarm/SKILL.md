---
name: Parallel TDD Swarm (Parallel Execution)
description: Optimizes the Test-Driven Development workflow by spawning parallel sub-agents or executing parallel tool calls for tests and implementation logic.
---

# Parallel TDD Swarm (Parallel Execution)

## Directives

1. **Parallel Tooling:**
   - Once a `spec.md` is approved, do not perform file edits one by one if they are independent.
   - Use concurrent execution of your available file creation or editing tools to generate the Test file and the Implementation file at the exact same time in a single thought block.
   - **CRITICAL RACE CONDITION GUARD:** Never assign multiple sub-agents or concurrent tool calls to modify the same file simultaneously. Implement logical file locking.

2. **Synchronization:**
   - After the parallel writes are complete, invoke your available terminal execution tools to run the tests.
   - The test runner acts as the synchronization barrier for the parallel tasks.
