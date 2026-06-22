# Конвенции Кода и Git-Флоу (CONVENTIONS.md)

## Стиль кода (Code Style)
- **Именование:** `camelCase` для переменных и функций, `PascalCase` для классов и компонентов React.
- **Типизация:** Строгий TypeScript. Никаких `any` без явного `// eslint-disable-next-line` с комментарием причины.
- **Компоненты:** Функциональные компоненты. Выносить логику в кастомные хуки.

## Обработка ошибок (Error Handling)
1. Все API-ошибки должны перехватываться глобальным Error Boundary (для UI) и глобальным обработчиком в Axios/Fetch.
2. Не подавлять ошибки (`try { ... } catch (e) {}` запрещено). Логировать через настроенный логгер.

## Git Конвенции (Git Flow)
- Ветка `main` всегда должна быть рабочей (deployable).
- Ветки фич: `feature/short-description`.
- Ветки багов: `fix/issue-description`.
- **Коммиты:** Используем Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`).
- Agentic Checkpointing: AI-агенты должны делать атомарные коммиты перед любыми деструктивными операциями.
