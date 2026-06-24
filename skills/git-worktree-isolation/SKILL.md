---
name: Git Worktree Isolation (Parallel Agents)
description: Изоляция рабочих сред для параллельных субагентов через механизм git worktree, предотвращающая конфликты файлов при одновременном редактировании.
---

# Git Worktree Isolation

**Type**: `Swarm Orchestration / Infrastructure`
**Trigger**: Когда `Multi-Agent Orchestrator` или `Shadow Clone Mode` запускает более одного агента, которые должны модифицировать код.

## The Problem
Если несколько субагентов (например, 3 агента тестируют разные реализации в Shadow Clone Mode) работают в одной директории, они будут перезаписывать файлы друг друга, вызывая гонку данных и фатальные конфликты.

## The Worktree Protocol
Для параллельной работы главный агент (Оркестратор) должен разворачивать изолированные worktree для каждого субагента:

1. **Создание ветки и worktree:**
   ```bash
   git branch clone-agent-alpha
   git worktree add ../clone-alpha-dir clone-agent-alpha
   ```
2. **Маршрутизация:**
   Передать субагенту Alpha директорию `../clone-alpha-dir` в качестве `Cwd` (текущей рабочей директории).
3. **Параллельная работа:**
   Субагенты могут безопасно использовать `write_to_file` или `multi_replace_file_content` в своих изолированных директориях.
4. **Сборка (Teardown):**
   После того как Оркестратор выбрал победителя (Shadow Clone) или завершил параллельную работу:
   ```bash
   # Забрать изменения из нужной ветки
   git merge clone-agent-alpha
   
   # Удалить worktree
   git worktree remove ../clone-alpha-dir
   git branch -d clone-agent-alpha
   ```

## Rules
- Никогда не запускайте параллельных write-агентов в одной папке.
- Worktrees должны создаваться ВНЕ основной папки проекта (или в `scratch`), чтобы IDE или линтеры пользователя не дублировали файлы.
