---
name: Knowledge Persistence (Memory Manager)
description: Cures agent "amnesia" by writing critical lessons learned into long-term project memory.
---

# Knowledge Persistence (Memory Manager)

## Directives

1. **End-of-Task Reflection:**
   - Upon completing a complex task, identify any non-obvious configurations, bug fixes, or architectural decisions that were made.

2. **Commit to Long-Term Memory:**
   - If `CI=true`, skip writing to `.ultracode/memory.md`. CI builds are ephemeral and should not persist agent state.
   - Otherwise, automatically write these findings into the project's long-term memory.
   - By default, use the global Knowledge Items (KI) system if available. If not, create or append to a `.ultracode/memory.md` or your IDE's equivalent rules file (e.g., `.cursorrules` for Cursor, `CLAUDE.md` for Claude Code) in the root of the user's current project.

3. **Memory Retrieval:**
   - At the start of a new task, always check if a `.ultracode/memory.md` exists in the project root and read it using JIT Context Retrieval.
