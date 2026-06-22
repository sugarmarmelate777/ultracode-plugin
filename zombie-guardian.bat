@echo off
REM Zombie Process Guardian — kills Python processes older than 2 hours
REM Run before starting Claude Code sessions to prevent zombie accumulation.
powershell -ExecutionPolicy Bypass -File "%~dp0zombie-guardian.ps1" %*
