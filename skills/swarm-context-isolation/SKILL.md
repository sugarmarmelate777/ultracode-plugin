---
name: Swarm Context Isolation (Least-Privilege Context)
version: "1.0.0"
depends_on: []
description: Enforces the principle of least privilege when spawning sub-agents, providing them only with the exact files and instructions needed for their specific micro-task.
---

# Swarm Context Isolation (Least-Privilege Context)

## Directives

1. **Micro-Task Delegation:**
   - When invoking a sub-agent (e.g., browser automation or any other specialized agent), define its task as an atomic, highly specific directive.
   - Do NOT say: "Fix the bug in the project." 
   - DO say: "Navigate to http://localhost:3000/login, click 'Submit' with empty fields, and return the exact text of the error banner."

2. **File Isolation:**
   - Only pass the absolute minimum file references required for the sub-agent to perform its job.
   - Never pass `.env` files, database credentials, or global `mcp_config.json` files to sub-agents unless explicitly necessary for their micro-task.

3. **Sub-Agent State Boundary (CRITICAL):**
   - You are designated as a SUB-AGENT with a strictly scoped micro-task. You are FORBIDDEN from:
     - Writing, modifying, or deleting `.ultracode/state.md`
     - Initiating context rotation or session state snapshots
     - Modifying any `.ultracode/` files except `.ultracode/blackboard/<your-task-id>.json` (your designated output slot)
   - Only the Main Orchestrator manages session state, rotation, and the global workspace lifecycle.
   - If you approach a context limit, return your partial results to the Orchestrator — do NOT attempt self-rotation.
