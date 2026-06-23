param (
    [Parameter(Mandatory=$true)]
    [string]$TargetDir
)

Write-Host "===============================================" -ForegroundColor Magenta
Write-Host "CORE INJECTOR SPIKE DEPLOYMENT INITIATED" -ForegroundColor Magenta
Write-Host "Target: $TargetDir" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Magenta

# 1. Resolve Target Dir
if (-not (Test-Path $TargetDir)) {
    Write-Host "Target directory does not exist! Aborting." -ForegroundColor Red
    exit 1
}

$payloadsDir = Join-Path $PSScriptRoot "payloads"

# 2. Inject God-Mode Rules
$cursorRulesDest = Join-Path $TargetDir ".cursorrules"
Copy-Item (Join-Path $payloadsDir "rules.template") -Destination $cursorRulesDest -Force
Write-Host " [v] Injected .cursorrules (God-Mode Directives)" -ForegroundColor Green

$windsurfRulesDest = Join-Path $TargetDir ".windsurfrules"
Copy-Item (Join-Path $payloadsDir "rules.template") -Destination $windsurfRulesDest -Force
Write-Host " [v] Injected .windsurfrules" -ForegroundColor Green

# 3. Deploy Immune System
$defenseDir = Join-Path $TargetDir ".ultracode\defense"
if (-not (Test-Path $defenseDir)) {
    New-Item -Path $defenseDir -ItemType Directory -Force | Out-Null
}
Copy-Item (Join-Path $payloadsDir "code_red.ps1") -Destination (Join-Path $defenseDir "code_red.ps1") -Force
Write-Host " [v] Deployed Immune System (code_red.ps1)" -ForegroundColor Green

# 4. Inject Git Safenets (Pre-commit hook)
$gitHooksDir = Join-Path $TargetDir ".git\hooks"
if (Test-Path $gitHooksDir) {
    $preCommitDest = Join-Path $gitHooksDir "pre-commit"
    Copy-Item (Join-Path $payloadsDir "pre-commit.template") -Destination $preCommitDest -Force
    Write-Host " [v] Injected Git Pre-Commit Hook (Safenet)" -ForegroundColor Green
} else {
    Write-Host " [!] No .git folder found in target. Skipping Git hooks injection." -ForegroundColor Yellow
}

Write-Host "===============================================" -ForegroundColor Magenta
Write-Host "ASSIMILATION COMPLETE. Target is now part of the Leviathan network." -ForegroundColor Magenta
