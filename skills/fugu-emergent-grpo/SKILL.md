---
name: "Обучение на основе результатов (Emergent GRPO)"
description: "Сохранение и анализ успешных связок 'Задача-Агент' для улучшения будущей маршрутизации."
---
# Outcome-Based Policy (GRPO Emulation)

Оркестратор должен сохранять результаты каждой задачи в файл `.ultracode/routing_policy.json`.
Формат: `{"task_type": "frontend", "model": "claude-sonnet-4", "success": true}`.
Перед выбором подагента, оркестратор обязан свериться с этой базой знаний.
