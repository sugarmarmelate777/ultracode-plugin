# ULTRACODE CODE RED PIPELINE
# Kills all related node/python processes and locks the project

Write-Host "========================================" -ForegroundColor Red
Write-Host "[!] INITIATING CODE RED SHUTDOWN PROTOCOL" -ForegroundColor Red
Write-Host "========================================" -ForegroundColor Red

# Create Panic Lock to block Git commits
$panicLockPath = Join-Path (Split-Path -Parent $PSScriptRoot) "panic.lock"
New-Item -Path $panicLockPath -ItemType File -Force | Out-Null
Write-Host " > panic.lock created at root. Commits and pipelines are blocked." -ForegroundColor Yellow

# Terminate processes
Write-Host " > Terminating active runtimes..." -ForegroundColor Yellow
Get-Process node, python, python3, pythonw -ErrorAction SilentlyContinue | Stop-Process -Force
Write-Host " > All local execution runtimes terminated." -ForegroundColor Red

Write-Host "SHUTDOWN COMPLETE." -ForegroundColor Red
