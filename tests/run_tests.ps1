$ErrorActionPreference = "Stop"

$skillsDir = "c:\Projects\ultracode-plugin\skills"
$skills = Get-ChildItem -Path $skillsDir -Directory

$failed = 0

Write-Host "Running Meta-RSI Regression Suite..."

# Test 1: YAML Frontmatter
foreach ($skill in $skills) {
    $skillFile = Join-Path $skill.FullName "SKILL.md"
    if (Test-Path $skillFile) {
        $content = Get-Content $skillFile -Raw
        if ($content -notmatch '(?s)^---\r?\nname:\s*(.+?)\r?\ndescription:\s*(.+?)\r?\n---') {
            Write-Host "FAIL: Missing or invalid YAML frontmatter in $($skill.Name)" -ForegroundColor Red
            $failed++
        }
    } else {
        Write-Host "FAIL: Missing SKILL.md in $($skill.Name)" -ForegroundColor Red
        $failed++
    }
}

# Test 2: Immutable Core Exists
$immutableCore = @(
    "security-guard",
    "prompt-injection-guard",
    "zero-trust-orchestration",
    "immutable-core-directives",
    "auto-rollback-healing"
)

foreach ($core in $immutableCore) {
    $corePath = Join-Path $skillsDir $core
    if (-not (Test-Path $corePath)) {
        Write-Host "FAIL: Immutable Core file missing: $core" -ForegroundColor Red
        $failed++
    }
}

if ($failed -gt 0) {
    Write-Host "Meta-RSI Regression Suite FAILED with $failed errors." -ForegroundColor Red
    exit 1
} else {
    Write-Host "Meta-RSI Regression Suite PASSED." -ForegroundColor Green
    exit 0
}
