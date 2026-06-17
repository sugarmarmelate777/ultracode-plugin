---
name: Sub-Agent Orchestration (Divide & Conquer)
description: Leverages specialized sub-agents and tool parallelization to tackle complex workflows without overloading a single agent's context.
---

# Sub-Agent Orchestration (Divide & Conquer)

## Directives

1. **Sub-Agent Delegation:**
   - When a task requires visual validation, browser interaction, or complex localized research, use your available sub-agent tools to spawn a specialized agent.
   - Provide the sub-agent with a highly specific, atomic task. Do not give it the entire project scope.

2. **Parallel Tooling:**
   - When gathering context across multiple files, utilize concurrent execution of tools (e.g., executing multiple available file reading or searching calls simultaneously).

3. **Orchestrator Role:**
   - Act as the Tech Lead. Do not get bogged down in the micro-details of a delegated task. Review the sub-agent's return report, verify the output, and integrate it into the main project.
