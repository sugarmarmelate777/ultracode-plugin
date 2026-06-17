---
name: Deep Planning & Analysis (Architect Mode)
description: Enforces a rigid pre-computation and planning phase for complex tasks to ensure architectural soundness before execution.
---

# Deep Planning & Analysis (Architect Mode)

## Directives

1. **Trigger Condition:**
   Whenever the user requests a new feature, a complex refactor, or a multi-file integration, you MUST enter Planning Mode.

2. **Phase 1: Deep Research:**
   - Read relevant existing code files thoroughly, but strictly follow Token Economy: use JIT reading (e.g., available codebase search tools) to find exact lines. Do NOT read the entire codebase.
   - Map out dependencies and state management.
   - Do NOT write any application code during this phase.

3. **Phase 2: The Implementation Plan:**
   - If Spec-Driven Development is required for this task (4 or more files (>=4)), WAIT for `spec.md` to be created and approved before writing the implementation plan.
   - Create an `implementation_plan.md` artifact based on the approved spec (or directly if no spec is needed).
   - Detail the proposed architecture, breaking changes, and a step-by-step checklist.
   - If there are architectural decisions to be made, ask the user focused, multiple-choice questions about trade-offs before finalizing the plan. (Subject to Global CI Gate)

4. **Phase 3: Execution Checklist:**
   - Wait for the user's explicit approval. (Subject to Global CI Gate)
   - Upon approval, immediately create a `task.md` artifact to track progress.
   - Execute exactly according to the plan, checking off items one by one.
   - If a roadblock is hit, PAUSE, update the plan, and consult the user. Do not silently drift from the approved architecture. (Subject to Global CI Gate)
