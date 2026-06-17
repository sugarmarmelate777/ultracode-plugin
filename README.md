# 🧠 Ultracode v11.7 — AI Agent Enhancement Plugin

**Ultracode** — это комплексный набор системных навыков (skills), которые превращают любую языковую модель (ChatGPT, Claude, Gemini, DeepSeek и др.) из простого чат-бота в **автономного, безопасного и экономичного ИИ-разработчика**.

> Навыки работают как "внутренние инстинкты" — ИИ автоматически применяет их при каждом разговоре. Пользователю не нужно вызывать их вручную.

---

## 🚀 Быстрая установка

### Для Antigravity IDE / Gemini CLI
Скопируйте папку `ultracode-plugin` в директорию плагинов:

```bash
# Windows
xcopy /E /I ultracode-plugin "%USERPROFILE%\.gemini\config\plugins\ultracode-plugin"

# macOS / Linux
cp -r ultracode-plugin ~/.gemini/config/plugins/ultracode-plugin
```

### Для Cursor / Windsurf / VS Code
Скопируйте содержимое каждого `SKILL.md` файла в ваш файл `.cursorrules` или `.windsurfrules` в корне проекта.

### Для Claude Code
Скопируйте содержимое навыков в файл `CLAUDE.md` в корне вашего проекта:

```bash
# Автоматическая сборка всех навыков в один файл
cat skills/*/SKILL.md > CLAUDE.md
```

### Для любой другой LLM
Просто вставьте содержимое нужных `SKILL.md` файлов в системный промпт вашего чат-бота или API-вызова.

---

## 📦 Структура проекта

```
ultracode-plugin/
├── plugin.json              # Манифест плагина (версия, описание)
├── README.md                # Этот файл
├── LLMS.md                  # Инструкция для языковых моделей
├── skills/                  # Навыки агента
    ├── cicd-mode/           # Неинтерактивный CI/CD режим
    ├── token-economy/       # Экономия токенов и контекста
    ├── deep-planning/       # Глубокое планирование
    ├── spec-driven-development/  # Разработка по спецификациям
    ├── confidence-scoring/  # Чеклист уверенности
    ├── deterministic-verification/  # Тест-Driven верификация
    ├── anti-loop-protocol/  # Защита от зацикливания
    ├── auto-rollback-healing/  # Авто-откат через Git
    ├── agentic-checkpointing/  # Безопасные Git-чекпоинты
    ├── security-guard/      # Блокировка опасных команд
    ├── prompt-injection-guard/  # Защита от инъекций
    ├── immutable-core-directives/  # "Законы робототехники"
    ├── zero-trust-orchestration/  # Нулевое доверие к подагентам
    ├── agent-orchestration/ # Делегирование подагентам
    ├── swarm-context-isolation/  # Изоляция контекста Роя
    ├── structured-swarm-artifacts/  # Протоколы связи Роя
    ├── parallel-tdd-swarm/  # Параллельное программирование
    ├── session-state-management/  # Управление состоянием между сессиями
    ├── knowledge-persistence/  # Долгосрочная память
    ├── environment-doctor/  # Диагностика окружения
    ├── mcp-mastery/         # Приоритет MCP-протоколов
    ├── recursive-self-improvement/  # Само-эволюция ИИ
    └── background-daemon/   # Фоновый мониторинг
├── .ultracode/              # Runtime sandbox (created by agent)
│   ├── state.md             # Working memory
│   ├── memory.md            # Long-term memory
│   ├── blackboard/          # Swarm asynchronous communication
│   └── failed_attempts/     # Dead-Letter Queue
```

---

## 🧩 Как это работает

Ultracode — это **не приложение** и **не программа**. Это набор текстовых инструкций (`.md` файлы), которые загружаются в контекст языковой модели и определяют её поведение.

### Без Ultracode:
```
Пользователь: "Почини баг"
ИИ: *переписывает весь файл на 500 строк, ломает 3 других файла, тратит 50 000 токенов*
```

### С Ultracode:
```
Пользователь: "Почини баг"
ИИ: 
  1. [Token Economy] → Нахожу точную строку бага
  2. [Confidence: 3/3] → Прошёл чеклист
  3. [Agentic Checkpoint] → Создаю git commit перед изменением
  4. [Minimal Diff] → Меняю только 2 строки
  5. [Deterministic Verification] → Запускаю тест
  6. [Anti-Loop] → Тест прошёл с 1-й попытки ✅
```

---

## 📋 Полный список навыков

### 🪙 Экономия и Эффективность
| Навык | Что делает |
|---|---|
| **Token & Context Economy** | Минимальные диффы, JIT-чтение файлов, RCA при дебаге, без воды |
| **MCP Mastery** | Приоритет нативных MCP-инструментов над скриптами |

### 🧠 Планирование и Качество
| Навык | Что делает |
|---|---|
| **Deep Planning** | Режим Архитектора: план → утверждение → выполнение |
| **Spec-Driven Development** | Спецификация (`spec.md`) перед сложными фичами |
| **Confidence Scoring** | 3-point бинарный чеклист перед кодом |
| **Deterministic Verification** | Запрет "vibe coding" — обязательные тесты |
| **Parallel TDD Swarm** | Параллельное написание кода и тестов |

### 🛡️ Безопасность
| Навык | Что делает |
|---|---|
| **Security Guard** | Блокировка `rm -rf`, `DROP TABLE` и утечек ключей |
| **Prompt Injection Guard** | Защита от вредоносного кода в логах и на сайтах |
| **Immutable Core Directives** | "Законы робототехники" — ИИ не может отключить свою защиту |
| **Zero-Trust Orchestration** | Проверка результатов работы подагентов |

### 🔄 Устойчивость и Восстановление
| Навык | Что делает |
|---|---|
| **CI/CD Mode** | Неинтерактивный режим для CI/CD пайплайнов |
| **Anti-Loop Protocol** | Максимум 2 попытки на один баг, потом стоп |
| **Auto-Rollback** | Автоматический откат к Git-чекпоинту при провале |
| **Agentic Checkpointing** | Создание безопасных `git commit` перед изменениями |
| **Session State Management** | Сохранение, восстановление и ротация контекста между сессиями |
| **Knowledge Persistence** | Долгосрочная память между сессиями |
| **Environment Doctor** | Диагностика серверов/портов/конфигов перед работой |
| **Background Daemon** | Фоновый мониторинг серверов и CI/CD |

### 🐝 Мульти-агентный Рой (Swarm)
| Навык | Что делает |
|---|---|
| **Agent Orchestration** | Делегирование задач подагентам |
| **Swarm Context Isolation** | Минимальный контекст для каждого подагента |
| **Structured Swarm Artifacts** | Общение агентов строго через JSON |

### 🧬 Само-Эволюция
| Навык | Что делает |
|---|---|
| **Recursive Self-Improvement** | ИИ может улучшать свои собственные навыки (с одобрения пользователя) |

---

## 📄 Лицензия

MIT License. Используйте свободно.

---

## 🤝 Автор

Создано совместно человеком и ИИ в среде Antigravity IDE.
