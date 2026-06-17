---
name: Environment Doctor (Pre-flight Diagnostics)
version: "1.0.0"
depends_on: []
description: Proactively checks local services and environment configuration before beginning tasks.
---

# Environment Doctor (Pre-flight Diagnostics)

## Directives

1. **Health Check Protocol:**
   - At the beginning of a session, if the project relies on specific local services (like a local API server, database, or proxy), use terminal commands or similar tools to check if the service is alive (e.g., ping a health endpoint or check if a port is listening).
   - Verify that all necessary command-line tools are available for the task (e.g., `git`, `npm`, `docker`).
   - Verify all Immutable Core skill files exist on disk (see `skills/immutable-core.json` for the canonical list): `security-guard/SKILL.md`, `prompt-injection-guard/SKILL.md`, `zero-trust-orchestration/SKILL.md`, `immutable-core-directives/SKILL.md`, `auto-rollback-healing/SKILL.md`, `recursive-self-improvement/SKILL.md`. If any is missing, report a CRITICAL integrity violation immediately.

2. **Configuration Validation:**
   - Check critical configuration files (e.g., `.env`, `mcp_config.json`, `docker-compose.yml`) for obvious syntax errors if the user complains about extension or connection issues.

3. **Auto-Heal (Limited Retry):**
   - If a service is down, attempt to start it automatically (e.g., `npm run dev`, `docker compose up -d`, or the project's start script) in the background before proceeding with the user's primary request. (Subject to Global CI Gate)
   - **One-Shot Limit:** You may attempt to start a service a MAXIMUM of ONE (1) time per session. If the service fails to start or crashes again after the auto-heal attempt, do NOT retry — report the failure to the user and proceed without that service. The Anti-Loop Protocol governs code fixes; a broken Docker configuration or missing dependency is not a fixable code bug and must not trigger a repair loop.
   - Before auto-healing, record the attempt in `.ultracode/state.md` under "Known Issues/Blockers" so subsequent rotations don't re-attempt the same failed service.
