# =============================================================================
# ZOMBIE PROCESS GUARDIAN v1.0 — Ultracode Plugin v14.0+
# Prevents Python subprocess accumulation from crashed/interrupted sessions.
# Kills Python processes older than the current session.
# =============================================================================
# Usage:
#   powershell -ExecutionPolicy Bypass -File zombie-guardian.ps1
#   powershell -ExecutionPolicy Bypass -File zombie-guardian.ps1 -DryRun
#   powershell -ExecutionPolicy Bypass -File zombie-guardian.ps1 -MaxAgeMinutes 60
# =============================================================================

param(
    [switch]$DryRun,
    [int]$MaxAgeMinutes = 120  # Kill processes older than this
)

$ErrorActionPreference = "SilentlyContinue"
$Now = Get-Date
$Cutoff = $Now.AddMinutes(-$MaxAgeMinutes)
$Killed = 0
$TotalCPU = 0
$TotalMem = 0

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " ZOMBIE PROCESS GUARDIAN v1.0" -ForegroundColor Cyan
Write-Host " Time: $($Now.ToString('yyyy-MM-dd HH:mm:ss'))" -ForegroundColor Cyan
Write-Host " Cutoff: processes started before $($Cutoff.ToString('yyyy-MM-dd HH:mm:ss'))" -ForegroundColor Cyan
if ($DryRun) { Write-Host " MODE: DRY RUN (no processes will be killed)" -ForegroundColor Yellow }
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Protect current session processes
$MyPid = $PID
$ParentPid = (Get-Process -Id $MyPid -ErrorAction SilentlyContinue).Parent?.Id

# Collect stats
$Zombies = Get-Process python -ErrorAction SilentlyContinue | Where-Object {
    $_.StartTime -lt $Cutoff -and
    $_.Id -ne $MyPid -and
    $_.Id -ne $ParentPid
}

if (-not $Zombies) {
    Write-Host "No zombie Python processes found." -ForegroundColor Green
    exit 0
}

Write-Host "Found $($Zombies.Count) potential zombie(s):" -ForegroundColor Yellow
Write-Host ""

foreach ($z in $Zombies) {
    $cpu = [math]::Round($z.CPU, 1)
    $mem = [math]::Round($z.WorkingSet64 / 1MB, 1)
    $age = [math]::Round(($Now - $z.StartTime).TotalHours, 1)
    Write-Host "  PID $($z.Id) | CPU: ${cpu}s | Mem: ${mem}MB | Age: ${age}h | Started: $($z.StartTime)"
    $TotalCPU += $cpu
    $TotalMem += $mem
}

Write-Host ""
Write-Host "Total: $($Zombies.Count) processes, ${TotalCPU}s CPU, ${TotalMem}MB RAM" -ForegroundColor Yellow
Write-Host ""

if ($DryRun) {
    Write-Host "DRY RUN — no processes killed. Remove -DryRun to execute." -ForegroundColor Yellow
    exit 0
}

foreach ($z in $Zombies) {
    try {
        Stop-Process -Id $z.Id -Force -ErrorAction Stop
        Write-Host "  KILLED PID $($z.Id)" -ForegroundColor Red
        $Killed++
    } catch {
        Write-Host "  FAILED to kill PID $($z.Id): $_" -ForegroundColor DarkRed
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " GUARDIAN COMPLETE: $Killed / $($Zombies.Count) killed" -ForegroundColor Green
Write-Host " Reclaimed: ~${TotalCPU}s CPU, ~${TotalMem}MB RAM" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
