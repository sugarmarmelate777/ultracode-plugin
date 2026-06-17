---
name: Auto-Rollback (Self-Healing)
description: Mandates that the agent automatically reverts its own failed code modifications using Git rather than leaving broken state for the user.
---

# Auto-Rollback & Self-Healing

## Directives

1. **Prerequisite — AI Checkpoint Must Exist:**
   - Auto-Rollback may ONLY be triggered if an AI Checkpoint commit was previously created by the Agentic Checkpointing skill.
   - If no AI Checkpoint exists for this task, DO NOT run `git reset`. Instead, use `git diff` to show the user what you changed, and ask them to manually decide what to revert. (Subject to Global CI Gate)

2. **Trigger Condition:**
   - If you fail to resolve a bug or compilation error after 2 attempts (as per the Anti-Loop Protocol), you MUST initiate the Auto-Rollback sequence.

3. **The Safe Rollback Sequence:**
   - FIRST: Create a `.ultracode/failed_attempts/` directory if it doesn't exist, and write the currently broken files or diffs there as a "Dead-Letter Queue" for the human developer to inspect later.
   - SECOND: Execute `git stash push --include-untracked -m "AI: pre-rollback safety stash"` to preserve ALL uncommitted work (including anything the user added since the checkpoint).
   - THIRD: Execute `git log --grep="AI Checkpoint: pre-" --oneline -1` to find the most recent AI Checkpoint commit.
   - FOURTH: Verify the commit hash is not empty using a shell-appropriate null check before proceeding. If no checkpoint commit is found, abort the rollback and report to the user.
   - FIFTH: Use `git reset --hard <checkpoint_commit_hash>` to revert ONLY to the AI Checkpoint, NOT to an arbitrary HEAD.
   - This ensures that the user's own uncommitted work (made before or after the AI started) is safely preserved in the stash and NOT destroyed.

4. **Reporting:**
   - Inform the USER: "I have hit the Anti-Loop threshold. I have stashed all uncommitted work and reverted my changes to the AI Checkpoint `<hash>`. Your work is preserved in the stash (run `git stash list` to see it). We need a new approach."
