---
name: Background Daemon (Proactive Polling)
description: Authorizes the agent to use the schedule tool to run as a background daemon, monitoring logs and CI pipelines autonomously.
---

# Background Daemon (Proactive Polling)

## Directives

1. **Safety Checks (MANDATORY):**
   - BEFORE proposing to run in the background, you MUST verify that a background scheduling tool (like `schedule` in Antigravity, `CronCreate` in Claude Code) exists in your environment. If not, silently skip daemon activation.
   - [CI/CD Override]: NEVER activate the daemon in non-interactive CI/CD mode. CI runs are ephemeral.

2. **Asynchronous Monitoring:**
   - The scheduled task should explicitly instruct the agent to run a command to check the tail of a log file or ping a health endpoint.

3. **Anti-Loop Compliance (MANDATORY):**
   - The Daemon is subject to the Anti-Loop Protocol. It may attempt a maximum of ONE (1) autonomous fix per polling cycle.
   - If the fix does not resolve the issue on the next polling cycle, the Daemon MUST stop attempting fixes and instead send a notification to the USER: "Background monitor detected a recurring issue I cannot fix autonomously. Manual intervention required."
   - The Daemon may NEVER enter a fix->break->fix loop.

4. **Kill Switch:**
   - If the user sends any message containing "stop daemon", "cancel daemon", or "kill background", immediately use your environment's equivalent of task cancellation / process termination to stop all scheduled background tasks.
