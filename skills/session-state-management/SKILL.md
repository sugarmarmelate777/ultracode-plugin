---
name: Session State Management
version: "1.0.0"
depends_on: []
description: Manages cross-conversation state persistence: writes workspace snapshots on rotation boundaries, rehydrates context on session start, and detects when the chat is too long.
---

# Session State Management

## Phase 1: Write (State Snapshot)

**Trigger:** When the conversation exceeds the adaptive message threshold (e.g. 70% of the context window limit, with an absolute maximum of 60 messages) OR the agent receives context-length warnings.

**Before writing, check:**
- Is an Anti-Loop escalation active? If yes, include loop state in the snapshot.
- Is the agent mid-debug on a single file, or has the user asked an unanswered question? If yes, defer the snapshot.
- If the `.ultracode/` directory does not exist, you MUST create it before writing state files. If `.ultracode/blackboard/` does not exist, create it alongside `state.md`.
- Is the project root writable? If not, gracefully fallback to writing `.ultracode/state.md` to a system temp directory.

**Write `.ultracode/state.md` in the project root with these sections:**
- **Project Path:** The absolute path of the current working directory (to prevent state mismatch).
- **Active Task/Goal:** One sentence summarizing the current objective.
- **Decisions Made & Why:** Key architectural or design decisions and their rationale.
- **Files Modified:** List of files changed with the last edit applied to each.
- **Known Issues/Blockers:** Open questions, failing tests, missing dependencies.
- **Next Immediate Action:** The single next step to take on resume.
- **Loop Status:** If Anti-Loop triggered, include error signature and attempt count.

Use the available file-editing tool to update the file at natural task boundaries — after completing a file, fixing a bug, or finishing a logical milestone. Do NOT update more frequently than once per 3-5 significant actions.

**Secret Protection (MANDATORY):** NEVER write API keys, passwords, tokens, connection strings with credentials, or any secret values into `.ultracode/state.md`, `.ultracode/memory.md`, or `.ultracode/telemetry.jsonl`. If a decision or blocker involves secrets, describe it generically (e.g., "AWS auth configured" not "AWS_ACCESS_KEY_ID=AKIA..."). The Security Guard prohibits echoing secrets — state files are no exception. Telemetry records may contain skill names and task IDs but MUST NOT include environment variable values, command outputs that may leak credentials, or file contents from `.env` files.

**Concurrency:** If sub-agents are active, the orchestrating agent is the sole writer; sub-agents are readers only.

## Phase 2: Read/Rehydrate (Session Start)

**Sub-Agent Guardian Check (MANDATORY):**
- Before proceeding with rehydration, check your designated role. If you are a SUB-AGENT (spawned by the Main Orchestrator for a micro-task), skip Phase 2 and Phase 3 entirely. Sub-agents do NOT read, write, or manage workspace state — they return their results directly to the Orchestrator.

At the beginning of ANY new conversation (as the Main Orchestrator), before asking the user for context:

1. Silently attempt to read `.ultracode/state.md` and `.ultracode/memory.md` from the project root (search subdirectories `src/`, `app/`, `packages/` if not found).
2. **Staleness check:** If `.ultracode/state.md` was last modified more than 7 days ago, display its contents but ASK: "I found a workspace state from [date]. Is this task still active, or should I start fresh?"
3. **Partial results:** If `.ultracode/state.md` exists but `.ultracode/memory.md` does not — proceed with workspace state only. If neither exists — proceed without comment. Do NOT report the absence of state files.
4. **Validation:** After rehydrating, summarize the recovered state. Wait for confirmation before taking action. (Subject to Global CI Gate)

**Acknowledgment format:** "I have restored context from [date]. Current objective: [summary]. Last completed: [step]. Ready to continue."

## Phase 3: Rotation Detection

- Monitor conversation length. When approaching the adaptive message threshold (e.g. 70% of the context window limit, with an absolute maximum of 60 messages) or receiving context-length warnings, initiate Phase 1 (Write).
- Advise the user: "To save tokens and keep my reasoning sharp, please start a new chat. I will automatically restore my context from the workspace state file." (Subject to Global CI Gate)
- Do NOT initiate rotation during an active debugging session, mid-edit on a single file, or when the user has an unanswered question.

## Completion

When the Global Objective is fully achieved:
1. DELETE `.ultracode/state.md` (or the temp file if fallback was used).
2. DELETE all files in `.ultracode/blackboard/` (clean up swarm artifacts from this task).
3. Inform the user the workspace has been cleaned.
