---
name: Dark Quant Agent (Forward Walk Backtesting)
description: Архитектура для алготрейдинговых ботов с использованием "скользящего окна" (Sliding Window Forward Walk) и кастомных функций вознаграждения для Reinforcement Learning.
---

# Dark Quant Agent (Forward Walk Backtesting)

**Type**: `Domain Expert / Algorithmic Trading`
**Trigger**: Создание торговых алгоритмов, бектестинг, Reinforcement Learning для трейдинга.

## 1. Sliding Window / Forward Walk
Обычное разбиение данных на `Train/Validation/Test` в трейдинге не работает из-за нестационарности рынков. Агент ОБЯЗАН реализовывать алгоритм "скользящего окна" (Forward Walk):
- **Окно обучения (In-Sample):** Например, 1 год (2020).
- **Окно тестирования (Out-of-Sample):** Например, 3 месяца (Янв-Мар 2021).
- После тестирования окно смещается на 3 месяца вперед (Обучение: Апр 2020 - Мар 2021, Тест: Апр-Июн 2021) и модель переобучается.

## 2. RL Reward Function
При обучении RL-агентов (Reinforcement Learning) для трейдинга запрещено использовать простую функцию PnL (Profit and Loss). Агент должен проектировать `Reward Function` так, чтобы:
1. **Penalize Drawdowns:** Штрафовать агента за глубокие просадки (Drawdown Penalty).
2. **Time in Market:** Штрафовать за слишком долгое удержание позиции без прибыли (предотвращает застревание в убыточных трейдах).
3. **Unrealized PnL:** Вознаграждать агента за плавающую прибыль (Unrealized PnL), а не только за закрытые сделки, чтобы сглаживать обучение.
