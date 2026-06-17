---
name: Environment Doctor (Pre-flight Diagnostics)
description: Proactively checks local services and environment configuration before beginning tasks.
---

# Environment Doctor (Pre-flight Diagnostics)

## Directives

1. **Health Check Protocol:**
   - At the beginning of a session, if the project relies on specific local services (like a local API server, database, or proxy), use terminal commands or similar tools to check if the service is alive (e.g., ping a health endpoint or check if a port is listening).
   - Verify that all necessary command-line tools are available for the task (e.g., `git`, `npm`, `docker`).
   - Verify all 5 Immutable Core skill files exist on disk (`security-guard`, `prompt-injection-guard`, `zero-trust-orchestration`, `immutable-core-directives`, `auto-rollback-healing`). If any is missing, report a CRITICAL integrity violation immediately.

2. **Configuration Validation:**
   - Check critical configuration files (e.g., `.env`, `mcp_config.json`, `docker-compose.yml`) for obvious syntax errors if the user complains about extension or connection issues.

3. **Auto-Heal:**
   - If a service is down, attempt to start it automatically (e.g., `npm run dev`, `docker compose up -d`, or the project's start script) in the background before proceeding with the user's primary request. (Subject to Global CI Gate)
