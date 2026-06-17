---
name: Structured Swarm Artifacts (Swarm Protocols)
description: Enforces strict data formats (JSON or Markdown tables) for communication between sub-agents and the Main Orchestrator to prevent hallucination.
---

# Structured Swarm Artifacts (Swarm Protocols)

## Directives

1. **Format Enforcement:**
   - When delegating a task to a sub-agent (e.g., UI testing, web scraping, or any other specialized sub-agent), you MUST explicitly command it to return its final report in a strict JSON format or a structured Markdown table. Use a catalog of reference JSON schemas for standard scenarios (e.g., `bug-report`, `code-review`, `ui-audit`, `perf-analysis`).
   - Example instruction: "Return your findings ONLY as a JSON object with keys: `error_code`, `line_number`, `suggested_fix`."

2. **Parsing Efficiency:**
   - The Orchestrator must parse these structured artifacts programmatically or logically without engaging in conversational back-and-forth with the sub-agent.

3. **Swarm Blackboard (Asynchronous Communication):**
   - For complex, multi-agent workflows, do not pass massive JSON blocks directly through the Orchestrator's context.
   - Instead, instruct sub-agents to save their output to `.ultracode/blackboard/<filename>.json`. Subsequent sub-agents should read from this blackboard to maintain isolated, token-efficient communication.
