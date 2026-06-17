---
name: Deterministic Verification (TDD-Agent Mode)
description: Forbids "vibe coding" by enforcing strict, deterministic structural tests and automated verification before a task is considered complete.
---

# Deterministic Verification (TDD-Agent Mode)

## Directives

1. **Test-Driven Verification:**
   - You are NOT allowed to mark a coding task as "Done" or create a final Walkthrough report simply because the code "looks right".
   - You MUST run a verification step:
     - Run the linter (`npm run lint`, `flake8`, etc.).
     - Run existing tests (`npm test`, `pytest`, etc.).
     - If no tests exist, write a small temporary test script (e.g., `scratch.py`, `scratch.ts`, `scratch_test.go` — match the project's language) to execute the modified function and prove it returns the expected result.

2. **Self-Correction Loop:**
   - If the verification fails, do not guess the fix. Analyze the error output, apply the Token Economy RCA (Root Cause Analysis) rule, and fix it.

3. **Proof of Work:**
   - Include the output of your successful deterministic verification in your final report to the user.
   - Upon successful verification, explicitly command the creation of a `walkthrough.md` artifact summarizing what was built, what was tested, and the test results.
