---
name: CI/CD Mode (Non-Interactive)
version: "1.0.0"
depends_on: []
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

5. **Structured Telemetry:**
   - In CI/CD mode, the Skill Telemetry badge format is replaced with machine-readable JSON Lines (JSONL).
   - After task completion (or on failure), append a single line to `.ultracode/telemetry.jsonl` (NOT `.json` — JSONL ensures concurrent writes from parallel swarm agents don't corrupt the file):
     ```jsonl
     {"timestamp":"<ISO 8601>","task_id":"<task description or commit hash>","skills_used":["<skill-name>",...],"exit_code":0|1,"attempts":<count>}
     ```
   - Each record is ONE LINE (no pretty-printing, no trailing comma). Append atomically at end of task. Never read-and-rewrite the file — append only.
   - Do NOT emit the `> [Active Skills: ...]` badge in CI mode — raw logs are parsed by automation, not humans.
