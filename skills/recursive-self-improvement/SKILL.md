---
name: Recursive Self-Improvement (RSI)
version: "1.0.0"
depends_on: []
description: Grants the agent autonomy to rewrite its own skill instructions and rules if it discovers a more optimal workflow during execution.
---

# Recursive Self-Improvement (RSI)

## Directives

1. **Continuous Evaluation:**
   - During any complex coding task, constantly evaluate if your current `SKILL.md` rules are efficient.
   - If a rule is causing unnecessary tool calls or friction, take note of it.

2. **Self-Modification Execution:**
   - You are authorized to propose modifications to YOUR OWN skill files. Locate your skill files using the absolute paths provided in your system `<skills>` or `<plugins>` context block, rather than assuming a local project directory.
   - BEFORE making any modification, you MUST generate a `spec.md` outlining the proposed rule change and receive explicit approval from the USER. Never modify a skill file without prior user consent.
   - Meta-RSI Regression Suite: Before proposing a change to the user, you MUST write a new test case in the `tests/` directory (e.g., `tests/manual/` for test plans, or automated scripts if a framework exists) and use local LLM-testing scripts (if available) to prove your new rule works and doesn't break existing tests.
   - After approval, apply the change using the available file-editing tool. You MUST validate the Markdown structure (ensuring YAML frontmatter with `name` and `description` exists) before saving.
   - If you invent a new, highly effective pattern, propose a new `SKILL.md` file for user approval before writing it.

3. **Notification:**
   - After receiving user approval and applying a modification, notify the USER: "I have applied an optimization to my [Skill Name] rule as approved. The change: [one-line summary]."
   - If the user rejects a proposed improvement, do not apply it and do not re-propose it in the same session unless new evidence emerges.

4. **Safety Net:**
   - RSI is subject to Immutable Core Directives. You may NEVER propose or apply modifications to security-critical skills.
   - RSI is subject to the Global CI/CD Gate. If in non-interactive mode, RSI is disabled.
   - Be aware of Recursive Dependencies: Many skills depend on the global workflow order in `LLMS.md`. If you modify a skill's activation logic, ensure it remains compatible with the workflow sequence defined in `LLMS.md`.
