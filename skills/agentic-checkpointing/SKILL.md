---
name: Agentic Checkpointing (Git Safenets)
version: "1.0.0"
depends_on: []
description: Creates atomic Git commits before executing risky code changes to allow rapid rollback.
---

# Agentic Checkpointing (Git Safenets)

## Directives

1. **Pre-Flight Check:**
   - Before editing existing source code files in a project, check if it's a Git repository using `git status`.
   - If it is NOT a Git repository, silently execute `git init` and `git commit --allow-empty -m "Initial commit"` before proceeding.

 2. **Atomic Snapshots:**
    - If there are uncommitted changes, ask the USER if they want to commit them, OR create an automatic checkpoint commit excluding ALL secret/credential files (`git add -A -- ':!.ultracode/' ':!*.env*' ':!.npmrc' ':!.git-credentials' ':!*.tfstate*' ':!*.tfvars' ':!kubeconfig*' ':!.aws/credentials' ':!*.pem' ':!*.key' ':!*.crt' ':!*.pfx' ':!*.jks' ':!*.keystore' ':!*.cer' ':!*.token' ':!*.secret' ':!credentials*' ':!secrets*' ':!id_rsa*' ':!id_ed25519*' ':!id_ecdsa*' ':!service-account*.json' ':!*.p12' ':!*.pkcs12' ':!*.ppk' ':!.netrc' ':!.pgpass' ':!*.keytab' ':!.pypirc' ':!.dockercfg' ':!.docker/config.json' && git commit -m "AI Checkpoint: pre-<feature_name>"`). (Subject to Global CI Gate)

3. **Post-Task Commit:**
   - After successfully completing a task and verifying it (Deterministic Verification), propose to commit the working state. (Subject to Global CI Gate)
