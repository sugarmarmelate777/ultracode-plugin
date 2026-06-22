# Инфраструктура и CI/CD (INFRA.md)

## Среды окружения (Environments)
- **Local:** `localhost:3000` (development)
- **Staging:** `staging.example.com` (preview)
- **Production:** `example.com` (live)

## Деплой (Deployment)
- **Провайдер:** Vercel / Railway / AWS.
- Автоматический деплой настроен при пуше в ветку `main`.
- Preview-деплои генерируются для всех Pull Requests.

## CI пайплайн (GitHub Actions)
При каждом PR выполняются:
1. `npm run lint` (Проверка стиля)
2. `npm run typecheck` (Проверка типов TypeScript)
3. `npm run test` (Unit тесты)
4. Сборка проекта (Build Test)

## Инфраструктура как код (IaC)
- Используется Docker (см. `Dockerfile` в корне).
- Контейнеризация для локальных сервисов через `docker-compose.yml`.
