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
- Use `if CI=true` ONLY for environment checks that skip actions unconditionally. For user-interaction gates that auto-proceed or fail, use the `(Subject to Global CI Gate)` phrase instead.
