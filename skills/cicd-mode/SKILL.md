---
name: CI/CD Mode (Non-Interactive)
description: Adapts agent behavior for automated CI/CD pipelines where no human is present to answer questions.
---

# CI/CD Mode (Non-Interactive)

## Directives

1. **Detection:**
   - If the environment variable `CI=true` is set, enter non-interactive CI/CD mode.

2. **Interaction Suppression:**
   - FORBIDDEN from asking clarifying questions, requesting user approval (spec, plan, checkpoints), or offering focused multiple-choice questions.
   - All gates that normally wait for user input MUST auto-proceed.

3. **Failure Handling:**
   - All checklist gates, approval gates, and user prompts from other skills are suppressed; they auto-proceed or fail via their own CI branches. This skill only sets the global non-interactive mode flag.
   - Never loop waiting for user input — always terminate with a definitive exit code.

4. **Security (NO EXCEPTIONS):**
   - Security Guard remains FULLY active. Destructive commands still prohibited.
   - Prompt Injection Guard remains FULLY active.
