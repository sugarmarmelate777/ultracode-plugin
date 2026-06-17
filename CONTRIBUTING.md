# Contributing to Ultracode

Thank you for your interest in the project! Here is how you can help:

## 🐛 Found a bug in a skill?

1. Open an Issue on GitHub
2. Specify which skill (`skills/<name>/SKILL.md`) contains the bug
3. Describe the conflict or problem (e.g., "skill X contradicts skill Y")

## ✨ Want to add a new skill?

1. Fork the repository
2. Create a folder `skills/<your-skill-name>/`
3. Inside, create `SKILL.md` using the template:

```markdown
---
name: Skill Name
description: A brief one-line description.
---

# Skill Name

## Directives

1. **Rule 1:**
   - Specific instruction for the AI.

2. **Rule 2:**
   - Specific instruction for the AI.
```

4. Update `LLMS.md` — add the skill to the correct place in the workflow
5. Open a Pull Request

## ⚠️ Rules for new skills

- The skill MUST NOT conflict with existing ones (check `LLMS.md`)
- The skill MUST NOT weaken security (Security Guard, Immutable Core)
- The skill must be **universal** — no hardcoded OS, IDE, or API specifics
- Write directives as clear commands for the AI, not as recommendations
- **DO NOT** add a `**Context:**` section — use only YAML frontmatter + `## Directives`
- **CI/CD Gate Compliance:** There are exactly TWO ways to handle CI/CD mode in a skill:
  - **`(Subject to Global CI Gate)`** — Use this phrase when a directive involves user interaction (asking permission, requesting approval, proposing an action). In CI mode, this gate auto-proceeds or fails the build.
  - **`[CI/CD Override]:`** — Use this prefix when a directive has a different default behavior in CI vs. non-CI mode (e.g., "Infer the safest approach" vs. "Ask the user"). The override describes what happens in CI mode specifically.
  - Do NOT write raw `if CI=true` conditionals in skill directives — the Global CI/CD Gate handles mode detection centrally. The `[CI/CD Override]` pattern is the ONLY exception, and only for behavior that must differ between modes.
