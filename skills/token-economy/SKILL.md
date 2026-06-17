---
name: Token & Context Economy
version: "1.0.0"
depends_on: []
description: Enforces minimal token usage on both input (file reads, context retrieval) and output (diffs, responses) to minimize API costs without sacrificing correctness.
---

# Token & Context Economy

## Input Discipline (What You Read)

1. **JIT Context Retrieval:**
   - Never read large files without a specific reason. Use search tools to find the exact lines you need first.
   - When N related files each need a narrow piece of information, read them in one batch rather than N sequential turns.

2. **Output Truncation:**
   - If a command outputs massive text (build logs, stack traces), extract the core failure reason. Truncate logs after the first error and last 20 lines. Never truncate error messages, stack traces, or test assertion failures.

3. **Scope Limitation:**
   - Prefer directly related files. If a cross-cutting change touches more than 5 files, announce the scope before proceeding.
   - When the correctness of a change depends on understanding the full file context, read the entire file -- economy rules relax when safety is at stake.

4. **Context Budget Awareness:**
   - After a tool produces more than 100 lines of output, summarize the result in 2-3 sentences before proceeding to the next action.

## Output Discipline (What You Write)

1. **Minimal Diffs:**
   - When editing, target the smallest lexically-independent block that fully captures the change. If the edit spans more than 20% AND >50 lines of a file, ask the user whether a rewrite is warranted rather than patching piecemeal. [CI/CD Override]: Default to a full rewrite to guarantee correctness.
   - Never output entire files when only a few lines changed. Use targeted editing tools.

2. **Ask vs. Infer:**
   - If ambiguity can be resolved by inspecting existing code patterns in 2 or fewer adjacent files -- infer and proceed.
   - If the ambiguity would lead to two substantially different implementations -- ask the user a specific, multiple-choice question. [CI/CD Override]: Infer the safest approach matching existing codebase patterns and document the assumption.
   - Do NOT generate large code blocks when requirements are ambiguous.

3. **Concise Explanations:**
   - Get straight to the point. State what is broken, how you will fix it, and the fix. Avoid verbose pleasantries, apologies, or filler text. One short sentence of context is enough.

4. **Root-Cause Analysis:**
   - When fixing errors, identify the EXACT line causing the issue. Propose a targeted, minimal fix. If the root cause is unclear, write a small debugging snippet to gather information instead of rewriting entire logic blocks.
