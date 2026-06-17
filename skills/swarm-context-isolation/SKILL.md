---
name: Swarm Context Isolation (Least-Privilege Context)
description: Enforces the principle of least privilege when spawning sub-agents, providing them only with the exact files and instructions needed for their specific micro-task.
---

# Swarm Context Isolation (Least-Privilege Context)

## Directives

1. **Micro-Task Delegation:**
   - When invoking a sub-agent (e.g., browser automation or any other specialized agent), define its task as an atomic, highly specific directive.
   - Do NOT say: "Fix the bug in the project." 
   - DO say: "Navigate to http://localhost:3000/login, click 'Submit' with empty fields, and return the exact text of the error banner."

2. **File Isolation:**
   - Only pass the absolute minimum `MediaPaths` or file references required for the sub-agent to perform its job.
   - Never pass `.env` files, database credentials, or global `mcp_config.json` files to sub-agents unless explicitly necessary for their micro-task.
