# История изменений

Все изменения в проекте Ultracode задокументированы ниже.

## [11.7.1] — 2026-06-17 (IDE-Agnostic Polish & Meta-RSI)
### Исправлено
- **Architecture**: Добавлен `tests/run_tests.ps1` для обеспечения Meta-RSI Regression Suite (проверка YAML frontmatter и целостности Immutable Core).
- **Consistency**: Унифицированы стили проверок CI (`[CI/CD Override]`), `CONTRIBUTING.md` обновлен с правилами использования Global CI Gate.
- **Documentation**: Таблица приоритетов навыков (Skill Priority) в `LLMS.md` расширена с 17 до 23 навыков для устранения слепых зон при конфликтах.
- **IDE-Agnosticism**: Удалены последние литералы-специфики (`/grill-me`, `schedule`, `browser automation`) из `cicd-mode`, `background-daemon` и `structured-swarm-artifacts`.
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
