# История изменений

Все изменения в проекте Ultracode задокументированы ниже.

## [11.8.0] — 2026-06-17 (Security Hardening & Audit Remediation) — UPDATED
### Исправлено (Round 1 — Cross-Audit Synthesis)
- **CRITICAL — Security Guard:** Полностью переработана система запрета команд. Добавлены: семантическое правило (запрет по цели, а не по синтаксису), regex-паттерны для обнаружения обхода через алиасы/флаги (`rm -r -f`, `ri`, `del /f`), недостающие деструктивные команды (`DROP SCHEMA/USER`, pipe-to-shell, `iptables -F`, `vagrant destroy`, `nft flush ruleset`). Закрыт вектор обхода через перестановку флагов и shell-алиасы.
- **CRITICAL — Prompt Injection Guard:** Закрыт вектор RCE через статические файлы — запрещено сохранять внешний код в исполняемые файлы (`.sh`, `.ps1`, `.py`, `.js` и т.д.) с последующим запуском. Внешний код можно только анализировать или сохранять в `.txt`/`.md` для ручного ревью.
- **Security — Agentic Checkpointing:** Post-task commit теперь подчиняется Global CI Gate (строка 20) — предотвращает зависание CI-пайплайна на ожидании подтверждения коммита.
- **Security — .gitignore:** Добавлены паттерны секретных файлов (`.npmrc`, `.git-credentials`, `*.tfstate*`, `kubeconfig*`, `.aws/credentials`, `*.ppk`, `*.pem`, `*.key`, `*.crt`, `*.pfx`, `*.jks`, `*.keystore`, `*.token`, `*.secret`, `credentials*`, `secrets*`, SSH-ключи, `service-account*.json`, `.env` и вариации).
- **Security — Session State Management:** Расширена Secret Protection на `.ultracode/telemetry.jsonl` — телеметрия не должна содержать переменные окружения или содержимое `.env` файлов.
- **Security — Auto-Rollback Healing:** Добавлена обязательная редкация секретов перед сохранением в Dead-Letter Queue (`.ultracode/failed_attempts/`). Секреты заменяются на `[REDACTED]`.
- **Security — Structured Swarm Artifacts:** Добавлен Content Injection Guard для Blackboard (проверка JSON на prompt injection payloads) и Slot Exclusivity (уникальные имена файлов с agent ID, защита от перезаписи между подагентами).
- **Stability — CI/CD Mode:** Телеметрия переведена на JSONL формат (`.ultracode/telemetry.jsonl` вместо `.json`) для предотвращения повреждения JSON при конкурентной записи из параллельных swarm-агентов.
- **Stability — Environment Doctor:** Введён лимит в 1 попытку auto-heal за сессию для предотвращения бесконечного цикла восстановления при сломанной конфигурации Docker/сервисов.
- **Stability — Anti-Loop Protocol:** Закрыт обход через "research delegation" — нельзя обойти 2-attempt limit, делегировав подагенту "исследование" ошибки и применив его готовый фикс.
- **Architecture — Immutable Core SSOT:** Создан `skills/immutable-core.json` как единый источник правды для списка защищённых навыков. `immutable-core-directives`, `environment-doctor`, и `run_tests.ps1` теперь ссылаются на него (с fallback-списками).
- **Documentation — LLMS.md:** Token & Context Economy объявлена преамбулой (активна с шага 0, а не с шага 7). Добавлено CI-исключение для human-readable телеметрии (badge не выводится при `CI=true`).
- **Documentation — CONTRIBUTING.md:** Документированы два формата CI/CD-гейтов: `(Subject to Global CI Gate)` и `[CI/CD Override]:` с правилами использования.
- **IDE-Agnosticism — Background Daemon:** Удалены последние привязки к конкретным IDE-инструментам (schedule/CronCreate), заменены на универсальную проверку наличия scheduling tools.
### Исправлено (Round 2 — Full Re-Audit Remediation)
- **CRITICAL — Security Guard:** Закрыт обход `rm -r -f` (split flags) — regex теперь ловит пробельные разделители. Добавлены: `sudo`/`su -c`/`runas` escalation, `DELETE FROM x WHERE 1=1` (tautology bypass), GCP/Azure cloud destruction (`gcloud compute instances delete`, `az group delete`), AWS EC2/RDS/DynamoDB/CloudFormation/IAM, `docker kill/stop/container rm`, `ufw`/`firewall-cmd`, `VBoxManage`, `eval`/`iex`/`Invoke-Expression`, `cmd /c`/`bash -c`/`pwsh -Command` wrappers, `chown root`/`setfacl`/`chattr`, `systemctl stop` critical services, alias detection directives.
- **CRITICAL — immutable-core.json:** Добавлен в собственный список `immutable_skills` (self-protection) — guard's guard больше нельзя удалить. `immutable-core-directives` обновлён для защиты `immutable-core.json`.
- **CRITICAL — README.md:** Заголовок обновлён с v11.7.1 на v11.8.0.
- **CRITICAL — LLMS.md:** Таблица State Files дополнена `.ultracode/telemetry.jsonl`. Critical Rule 2 (Security Guard) расширен до полного списка категорий. Spec-Driven Dev trigger расширен до 3 условий (>=4 files, new component, user request).
- **CRITICAL — Agentic Checkpointing:** `git add` exclusion patterns синхронизированы с `.gitignore` — добавлены `.npmrc`, `.git-credentials`, `.netrc`, `*.tfstate*`, `*.tfvars`, `kubeconfig*`, `.aws/credentials`, `*.ppk`, `*.pkcs12`, `.pgpass`, `*.keytab`, `.pypirc`, `.dockercfg`, `.docker/config.json`, `.ultracode/`.
- **CRITICAL — Prompt Injection Guard:** Добавлена защита от base64/hex/Unicode/URL-encoded инъекций, leetspeak, homograph attacks, null-byte splitting. Добавлен Re-ingestion Guard для markdown code blocks из внешних источников.
- **HIGH — Structured Swarm Artifacts:** Blackboard injection detection расширен до полного паритета с Prompt Injection Guard (все языки, все obfuscation-векторы, base64/Unicode).
- **HIGH — .gitignore:** Добавлены `.netrc`, `.dockercfg`, `.docker/config.json`, `.pgpass`, `*.keytab`, `.pypirc`, `.htpasswd`, `*.der`, `*.cert`, `*.ca-bundle`, `*.ovpn`, `*.csr`.
- **HIGH — tests/run_tests.ps1:** YAML frontmatter test расширен до валидации `version:` и `depends_on:` полей. Добавлена обработка `immutable-core.json` как self-reference entry в Immutable Core списке.
- **HIGH — Parallel TDD Swarm:** Добавлена Staging Isolation (`.ultracode/staging/<agent-id>/`) — подагенты больше не пишут напрямую в `src/`. Оркестратор валидирует staging-артефакты через Zero-Trust и только потом сливает в проект. Устранена гонка записи между параллельными агентами.

## [11.7.1] — 2026-06-17 (IDE-Agnostic Polish & Meta-RSI)
### Исправлено
- **Architecture**: Добавлен `tests/run_tests.ps1` для обеспечения Meta-RSI Regression Suite (проверка YAML frontmatter и целостности Immutable Core).
- **Consistency**: Унифицированы стили проверок CI (`[CI/CD Override]`), `CONTRIBUTING.md` обновлен с правилами использования Global CI Gate.
- **Documentation**: Таблица приоритетов навыков (Skill Priority) в `LLMS.md` расширена с 17 до 23 навыков для устранения слепых зон при конфликтах.
- **IDE-Agnosticism**: Удалены последние IDE-специфики (`/grill-me`, `browser automation`) из `cicd-mode` и `structured-swarm-artifacts`. `background-daemon` использует обобщённые ссылки на инструменты планирования.
- **Typo**: Исправлено повторяющееся слово "Adhere" в `LLMS.md`.

## [11.7.0] — 2026-06-17 (Enterprise Refactoring)
### Добавлено
- Схемы Swarm-артефактов: добавлены JSON-схемы для структурированного взаимодействия по стандартам bug-report и code-review.
- Внедрён **Dead-Letter Queue (DLQ)**: Auto-Rollback теперь сохраняет провальные попытки ИИ в папку `.ultracode/failed_attempts/` перед стиранием (git stash).
- Swarm Blackboard для асинхронной коммуникации агентов.
- Meta-RSI Regression Suite для валидации само-модификаций.
- Мультиязычные примеры в Prompt Injection Guard.
- Внедрён модуль **LLM-тестирования промптов** (папка `tests/`).
### Изменено
- Архитектура CI/CD Gate: устранено дублирование условий `if CI=true` из 6 навыков в пользу глобального **Global Non-Interactive (CI/CD) Gate** в `LLMS.md`.
- Песочница состояний: финальная миграция всех файлов кэша (`.workspace_state.md` и `.agent-memory.md`) в безопасную директорию `.ultracode/`.
- Телеметрия: выводимый бейдж `[Active Skills]` теперь включает только активно сработавшие навыки для снижения шума.
- Имена инструментов: остаточные привязки к IDE (например, `call_mcp_tool` и `search_web`) заменены на агностичные абстракции.
- `CONTRIBUTING.ru.md` очищен от старых команд и помечен как перевод оригинального `CONTRIBUTING.md`.

## [11.6.0] — 2026-06-17 (IDE-Agnostic Polish)
### Исправлено
- **Архитектура:** произведена полная отвязка навыков от IDE-специфичных имён инструментов (например, `write_to_file`, `run_command`). Теперь плагин на 100% универсален и адаптируется под любой редактор (Cursor, Claude Code, Antigravity).
- session-state-management: проверка на запись (writability check) перенесена в самое начало процесса (Phase 1), чтобы безопасно переключаться на временные директории до сбоя.
- background-daemon: добавлена безопасная проверка доступности инструмента `schedule` перед активацией.
- LLMS.md: расширено правило Security Guard, чтобы ИИ понимал, что список опасных команд не ограничивается четырьмя базовыми.
- spec-driven-development: порог сложности уточнён с `>3 files` до абсолютного `4 or more files (>=4)`.

## [11.5.0] — 2026-06-17 (Final CI Polish)
- **CRITICAL:** auto-rollback-healing: добавлена остановка сборки (fail build) в CI, если отсутствует чекпоинт, чтобы избежать зависания пайплайна на ручном вопросе пользователю.
- deep-planning: добавлено немедленное падение сборки при столкновении с roadblocks в CI-режиме вместо ожидания ответа пользователя.
- token-economy: разрешена неоднозначность в CI. Установлено дефолтное поведение: всегда переписывать (вместо вопроса при 20% diff) и автоматически додумывать решение при неясностях (infer).
- background-daemon: строгий запрет активации демона в CI-окружении (оно эфемерно).
- spec-driven-development: убрана двусмысленность между "append" и "version", теперь строго требуется версионирование `spec_v2.md`.

## [11.4.0] — 2026-06-17 (Deep Research Patch)
- **CRITICAL:** auto-rollback-healing: `git stash push` теперь использует флаг `--include-untracked`, предотвращая утечку сломанных файлов ИИ в рабочий каталог при откате.
- agentic-checkpointing: заменена команда `git commit -am` на `git add . && git commit -m` для гарантированного захвата новых файлов в safety net.
- session-state-management: добавлено условие полного пропуска записи `.workspace_state.md` в режиме `CI=true` для предотвращения загрязнения эфемерных сборок.
- recursive-self-improvement: исправлена "слепота" путей навыков — агент теперь использует системные пути (context blocks) вместо хардкода директории проекта.
- LLMS.md полностью переведён на английский язык для предотвращения фрагментации контекста (переводных галлюцинаций) и экономии токенов у языковых моделей.

## [11.3.0] — 2026-06-17 (Universal Polish)
- **CRITICAL:** Повреждённая кодировка (corrupted em-dash, arrows) в token-economy, background-daemon, immutable-core-directives — перезаписано чистым ASCII
- **CRITICAL:** security-guard содержал жёсткую привязку к Windows ("Since the USER's OS is Windows") — удалена, навык теперь кроссплатформенный
- **CRITICAL:** README.md заголовок рассинхронизирован с plugin.json — синхронизировано до v11.3
- environment-doctor: добавлена CI-ветка (запрет auto-heal в CI/CD)
- knowledge-persistence: добавлена CI-ветка (запрет записи .agent-memory.md в CI)
- deep-planning: /grill-me обёрнут в условие "NOT in CI/CD mode"
- auto-rollback-healing: Bash-специфичный пример заменён на универсальную директиву
- 3 Swarm-навыка: ссылки на `browser_subagent` заменены на универсальные "sub-agent tools"
- mcp-mastery: добавлена проверка наличия MCP-серверов перед активацией
- CONTRIBUTING.md: удалён устаревший шаблон с `**Context:**`, добавлено правило CI-gate для новых навыков

## [11.2.0] — 2026-06-17 (Enterprise CI/CD Ready)
### Исправлено
- CI/CD hang prevention: deep-planning, spec-driven-development, anti-loop-protocol, session-state-management, agentic-checkpointing — все получили `if CI=true` ветки
- RSI полностью запрещён в CI/CD режиме
- Race Condition Guard добавлен в parallel-tdd-swarm
- Git Init Fallback добавлен в agentic-checkpointing (greenfield проекты)
- Bash Hash Safety добавлена в auto-rollback-healing
- LLMS.md: добавлены 6 недостающих навыков в таблицу приоритетов
- deterministic-verification: явная команда создания walkthrough.md
- session-state-management: Project Path в state snapshot для предотвращения state mismatch

## [11.1.0] — 2026-06-17 (Flawless)
### Исправлено
- Удалён мёртвый навык skill-hunter (npx skills не существует)
- RSI: добавлено требование spec.md Pre-Approval
- Конфликт confidence-scoring vs cicd-mode: добавлена CI-ветка в Checklist Gate
- zero-trust-orchestration: абстрагированы IDE-специфичные инструменты

## [11.0.0] — 2026-06-17 (CI/CD Ready)
### Добавлено
- **CI/CD Mode** — новый навык для неинтерактивных CI/CD пайплайнов
- Confidence Scoring переделан: проценты заменены на 3-point бинарный чеклист
### Исправлено
- Token Trimming: удалены все секции `**Context:**` из 23 навыков (~500 токенов экономии)

## [10.0.0] — 2026-06-17 (Consolidated)
### Изменено
- Объединены 3 навыка состояния (Working Memory, Context Rotation, Stateful Rehydration) в единый Session State Management
- Количество навыков: 26 -> 24

## [9.0.0] — 2026-06-17 (Hardened)
### Исправлено
- **CRITICAL:** Auto-Rollback больше не уничтожает незакоммиченную работу пользователя — откат только к AI Checkpoint
- **CRITICAL:** Immutable Core Directives теперь защищает сам себя от перезаписи через RSI
- **CRITICAL:** Background Daemon подчинён Anti-Loop Protocol (макс. 1 фикс за цикл) + добавлен Kill Switch
- Security Guard: замена `/tmp/` на кроссплатформенные пути
- Confidence Scoring: оценка теперь происходит ПОСЛЕ Deep Research, а не до
- Spec-Driven Dev: добавлен порог сложности (>3 файлов), мелкие задачи не требуют spec.md
- Context Rotation: убрана ручная копипаста — интеграция со Stateful Rehydration

## [8.0.0] — 2026-06-17 (Absolute Synthesis)
### Добавлено
- Stateful Rehydration — автоматическое восстановление контекста без участия пользователя
- Immutable Core Directives — "Законы робототехники" для защиты ядра безопасности
- Structured Swarm Artifacts — строгие JSON-протоколы общения между агентами
- Parallel TDD Swarm — параллельное написание кода и тестов

## [7.0.0] — 2026-06-17 (The Swarm)
### Добавлено
- Swarm Context Isolation — принцип наименьших привилегий для подагентов
- Zero-Trust Orchestration — проверка результатов работы подагентов
- Prompt Injection Guard — защита от вредоносного кода во внешних источниках

## [6.0.0] — 2026-06-17 (RSI Architecture)
### Добавлено
- Recursive Self-Improvement (RSI) — агент может улучшать свои собственные навыки
- Auto-Rollback — автоматический откат при провале через Git
- Background Daemon — фоновый мониторинг серверов по расписанию
- Working Memory State — оперативная память для предотвращения "горизонтного дефицита"

## [5.0.0] — 2026-06-17 (Architecture of Autonomy)
### Добавлено
- Confidence Scoring — оценка уверенности ИИ перед написанием кода
- Spec-Driven Development — создание спецификаций перед кодингом
- MCP Mastery — приоритет нативных MCP-инструментов IDE

## [4.0.0] — 2026-06-17 (Resilience)
### Добавлено
- Agentic Checkpointing — автоматические Git-чекпоинты перед изменениями
- Context Rotation — управление длиной чатов для экономии токенов
- Environment Doctor — превентивная диагностика окружения

## [3.0.0] — 2026-06-17 (Security Patch)
### Добавлено
- Anti-Loop Protocol — жёсткий лимит 2 попытки на баг
- Knowledge Persistence — долгосрочная память между сессиями
- Security Guard — блокировка деструктивных команд

## [2.0.0] — 2026-06-17 (SOTA)
### Добавлено
- Context Engineering — JIT-загрузка файлов, защита окна внимания
- Deterministic Verification — обязательные тесты, отказ от "vibe coding"
- Sub-Agent Orchestration — делегирование задач подагентам

## [1.0.0] — 2026-06-17 (Initial Release)
### Добавлено
- Token Economy — экономия токенов, минимальные диффы, RCA
- Skill Hunter — автоматический поиск Vercel Skills [REMOVED in v11.1]
- Deep Planning — режим Архитектора с обязательным планированием
