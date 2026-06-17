---
name: Anti-Loop Protocol
description: Prevents token-burning infinite debug loops by enforcing strict retry limits during error resolution.
---

# Anti-Loop Protocol (Token Safeguard)

## Directives

1. **The 2-Strike Rule:**
   - You have a strict limit of TWO (2) attempts to fix any specific bug, compilation error, or failing test.
   - If your first fix fails, your second attempt MUST use a substantially different approach. Before applying the second attempt, you MUST call the Environment Doctor skill to verify local services, dependencies, and language versions.

2. **Loop Break Condition:**
   - If the error persists after the second attempt, you MUST STOP modifying the code immediately.
   - Do NOT try a third time.
   - Initiate the Auto-Rollback Healing sequence (see Auto-Rollback skill) to revert to the last AI Checkpoint.
     - Either use your environment's equivalent of a web search tool to find the exact error message online, or generate a prompt asking the USER for guidance. (Subject to Global CI Gate)

3. **Status Tracking:**
   - Maintain an internal counter of your attempts on a specific error. Mention this in your internal thought process (e.g., "Attempt 1 of 2 for TypeError").
