---
name: Security Guard (Destructive Action Preventer)
version: "1.0.0"
depends_on: []
description: Protects the user's environment by enforcing sandbox rules and double-checking potentially destructive commands.
---

# Security Guard

## Directives

1. **Prohibited Commands (Semantic + Pattern-Based):**
   - **Semantic Rule (OVERRIDES ALL):** You are FORBIDDEN from executing ANY command whose PURPOSE is to irreversibly destroy, delete, or corrupt data, infrastructure, or work product — regardless of how the command is spelled, aliased, or parameterized. This includes circumvention via: split flags (`rm -r -f` / `rm -r --force`), flag reordering (`rm -f -r`), shell aliases (`ri` for `Remove-Item`, `rd` for `rmdir`), command wrappers (`bash -c "rm -rf /"`, `cmd /c del /s /q`, `pwsh -Command "..."`), privilege escalation (`sudo ...`, `su -c "..."`, `runas /user:Admin cmd`), and obfuscation (`eval`, `iex`, backtick/$() substitution).
   - **Pattern Matching (Regex):** Before executing any shell command, check it against these patterns. If ANY pattern matches, treat the command as prohibited:
     - `/rm\s+(-[a-z]*r[a-z]*f\b|-[a-z]*f[a-z]*r\b|-r\s+-f|-f\s+-r|--recursive.*--force|--force.*--recursive)/i` — recursive force removal via any flag combination or split flags
     - `/rm\s+.*\b(-rf?\b|-fr\b)\s/` — rm with short destructive flags (catch split: `rm -r -f`, `rm -r file`)
     - `/\b(del|ri|remove-item|rd|rmdir|erase)\b.*(-Recurse|-Force|-rf|\/s|\/q)/i` — destructive deletion via aliases or PowerShell cmdlets
     - `/dd\s+if=/` — raw disk overwrite
     - `/\b(mkfs\.|fdisk|diskpart|format\s+[a-z]:)/i` — filesystem formatting
     - `/\b(shutdown|reboot|halt|poweroff|stop-computer|restart-computer|bcdedit)\b/i` — system power state changes
     - `/DROP\s+(TABLE|DATABASE|SCHEMA|USER|INDEX|VIEW|PROCEDURE|FUNCTION|TRIGGER|ROLE|TABLESPACE|DOMAIN|TYPE|ASSEMBLY|CERTIFICATE|SYMMETRIC\s+KEY|MASTER\s+KEY)/i` — SQL schema/data destruction
     - `/\b(DELETE\s+FROM\s+\w+(\s+WHERE\s+(1\s*=\s*1|true|1\b))?|TRUNCATE\s+(TABLE\s+)?\w+)/i` — SQL data destruction (WHERE-less, tautology WHERE, or truncation)
     - `/git\s+(push\s+--force|reset\s+--hard|clean\s+-fdx|branch\s+-D|stash\s+clear|reflog\s+expire)/i` — Git history destruction
     - `/\b(docker|podman)\s+(rm\s+-f|rm\s+--force|kill|stop|container\s+rm|system\s+prune|volume\s+prune|compose\s+down\s+-v)/i` — container stop/kill/destruction
     - `/\b(kubectl\s+delete\s+(namespace|pod|deploy|svc|ingress|configmap|secret|pvc)\b|helm\s+uninstall)/i` — Kubernetes resource deletion
     - `/\b(terraform\s+(destroy|apply\s+-destroy)|pulumi\s+destroy|aws\s+(s3\s+rm\s+--recursive|ec2\s+terminate-instances|rds\s+delete-db-instance|dynamodb\s+delete-table|cloudformation\s+delete-stack|iam\s+delete-(user|role|policy)))/i` — AWS infrastructure teardown
     - `/\b(gcloud\s+(compute\s+instances\s+delete|sql\s+instances\s+delete|container\s+clusters\s+delete|functions\s+delete|run\s+services\s+delete|firestore\s+databases\s+delete))/i` — GCP resource deletion
     - `/\b(az\s+(group\s+delete|vm\s+delete|sql\s+db\s+delete|aks\s+delete|container\s+delete|functionapp\s+delete|webapp\s+delete))/i` — Azure resource deletion
     - `/\b(npm\s+unpublish\s+--force|gh\s+repo\s+delete|pip\s+uninstall\s+-y|choco\s+uninstall|brew\s+uninstall\s+--force)/i` — package/registry deletion
     - `/\b(chmod\s+.*777|chown\s+.*root|setfacl|chattr|icacls\s+.*\/grant\s+Everyone:F|Set-ExecutionPolicy\s+Bypass)/i` — permission/filesystem attribute escalation
     - `/\b(reg\s+delete|Remove-Item\s+(HKLM|HKCU):)/i` — registry destruction
     - `/\b(sc\s+delete|systemctl\s+(disable\s+--now|mask|stop\s+(docker|sshd|mysql|mariadb|postgresql|nginx|apache|redis|mongod|k3s|kubelet))|wsl\s+--unregister)/i` — service destruction or critical service stop
     - `/(\|\s*|\b(eval|iex|Invoke-Expression)\s+)\s*(sh|bash|zsh|ksh|fish|python|ruby|perl|lua|node|pwsh|powershell)\b/i` — pipe-to-shell OR eval/iex (arbitrary code execution vector)
     - `/\b((sh|bash|zsh|cmd|pwsh|powershell)\s+-c\s+)/i` — command wrapper execution (bash -c "dangerous", cmd /c dangerous)
     - `/\b(sudo|su\s+-c|runas\s+\/user:)/i` — privilege escalation (cached credentials can make any command reach root)
     - `/\b(iptables\s+(-F|--flush|-X|--delete-chain|-P\s+(INPUT|OUTPUT|FORWARD)\s+DROP)|nft\s+flush\s+ruleset|ufw\s+(disable|reset|--force\s+reset)|firewall-cmd\s+--permanent\s+--remove)/i` — firewall destruction or lockout
     - `/\b(vagrant\s+destroy|vagrant\s+global-status\s+--prune|VBoxManage\s+(controlvm\s+\S+\s+poweroff|unregistervm\s+\S+\s+--delete))/i` — VM destruction
     - `/\b(nixos-rebuild\s+switch\s+--rollback|guix\s+system\s+delete-generations)/i` — OS-level destructive changes
   - **Resource exhaustion (semantic):** Fork bombs (`:(){ :|:& };:`), infinite process spawns (`while true; do ... &; done`), and disk-fill commands (`dd if=/dev/zero of=...`, `fallocate`, `yes >`) are forbidden regardless of syntax.
   - **Alias detection:** Before executing ANY command, scan for alias definitions that disguise destructive intent (`alias ...='rm -rf'`, `doskey ...=del /s /q`, `function ... { rm -rf }`). If an alias maps to a destructive pattern, treat the aliased command itself as prohibited.
   - This list is NON-EXHAUSTIVE. If a command would irreversibly destroy data, infrastructure, or work product, treat it as prohibited regardless of whether it appears above.

2. **Safe Verification Environments:**
   - When writing scratch scripts to verify code (as mandated by Deterministic Verification), mock all database connections and file system writes.
   - Use platform-appropriate temp directories:
     - **Windows:** `$env:TEMP` or the workspace `scratch/` directory
     - **Linux/Mac:** `/tmp/` or the workspace `scratch/` directory

3. **Credential Protection:**
   - Never print or echo environment variables (`$env:*`, `Get-ChildItem Env:`, `printenv`) that might leak API keys or secrets into the task logs.
   - Never hardcode or display `.env` file contents in responses.
