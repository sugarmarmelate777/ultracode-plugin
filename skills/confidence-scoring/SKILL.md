---
name: Confidence Scoring (Graceful Degradation)
description: Prevents AI hallucinations and blind coding by forcing the agent to pass a binary checklist before writing code.
---

# Confidence Scoring (Graceful Degradation)

## Directives

1. **Evaluation Timing (CRITICAL):**
   - Complete the Confidence Checklist AFTER Phase 1 (Deep Research) of Deep Planning.
   - Do NOT evaluate confidence before reading files.

2. **Confidence Checklist (3 Questions):**
   Answer each with YES or NO only:
   1. Do I understand the business goal / user intent?
   2. Have I read the relevant sections of all files this change touches (using JIT/search where appropriate)?
   3. Do I know the framework/library version and its API?

3. **Checklist Gate:**
   - 3/3 YES → proceed to code.
   - <3 YES → FORBIDDEN from writing code. 
     - [CI/CD Override]: FAIL the build immediately with exit code 1.
     - Otherwise, ask the user specific questions for each NO item. Ask focused, multiple-choice questions for ambiguous cases.

4. **State Your Confidence:**
   - Always state your checklist score (e.g., "Confidence: 2/3 — missing business goal and framework version") before action.
