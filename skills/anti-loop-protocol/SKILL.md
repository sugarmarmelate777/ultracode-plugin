---
name: Anti-Loop Protocol
version: "1.0.0"
depends_on: []
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

4. **Sub-Agent Loop Prevention:**
   - The 2-strike limit applies to the ENTIRE task, including any sub-agents you spawn.
   - You are FORBIDDEN from spawning a fresh sub-agent to attempt fix #3 after you have exhausted your own 2 attempts. A sub-agent with a clean context does NOT reset the attempt counter.
   - If you delegate a fix attempt to a sub-agent, that attempt counts toward the global 2-strike limit for the task.
   - **Research Delegation Blocked:** You are FORBIDDEN from circumventing the 2-strike limit by delegating "research" or "analysis" of the error to a sub-agent and then applying its suggested fix. If a sub-agent returns a concrete code change — whether labeled "research," "analysis," "suggestion," or "recommendation" — applying it counts as a fix attempt. After 2 failed fix attempts, you may NOT apply any sub-agent-suggested fixes for that error.
