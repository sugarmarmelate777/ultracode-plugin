---
name: Audio Notification Hook (Task Completion Chime)
description: Включает звуковое уведомление (PowerShell chime) при завершении длительных фоновых задач или компиляции, чтобы разработчик мог отойти от экрана.
---

# Audio Notification Hook (Task Completion Chime)

**Type**: `Workflow Quality of Life`
**Trigger**: Long-running background tasks, compilation, or test suites completing.

## Directive
Агенты **обязаны** использовать этот хук для уведомления пользователя о завершении длительных фоновых процессов (которые занимают более 1 минуты), чтобы пользователь не сидел и не смотрел в терминал в ожидании.

## Implementation Details
После завершения команды, которая выполнялась асинхронно или в фоне, агент должен запустить следующую команду:

```powershell
powershell -c "(New-Object System.Media.SoundPlayer 'C:\Windows\Media\tada.wav').PlaySync()"
```
*Альтернативно:*
```powershell
powershell -c "[System.Media.SystemSounds]::Asterisk.Play()"
```

Это привлечет внимание пользователя к тому, что задача (например, генерация большого отчета, сборка проекта, или завершение параллельного скрапинга) выполнена.

## Example Usage
1. Агент запускает `npm run build` с таймингом в фоне.
2. При получении уведомления об успешном завершении `manage_task status == completed`, агент запускает `run_command`:
   `powershell -c "[System.Media.SystemSounds]::Exclamation.Play()"`
3. Агент пишет пользователю: "Сборка завершена, я подал звуковой сигнал."
