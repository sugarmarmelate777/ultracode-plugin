$ErrorActionPreference = "Stop"

$skillsDir = (Resolve-Path (Join-Path $PSScriptRoot "..\skills")).Path
$skills = Get-ChildItem -Path $skillsDir -Directory

$failed = 0

Write-Host "Running Meta-RSI Regression Suite..."

# Test 1: YAML Frontmatter (name, version, depends_on, description)
foreach ($skill in $skills) {
    $skillFile = Join-Path $skill.FullName "SKILL.md"
    if (Test-Path $skillFile) {
        $content = Get-Content $skillFile -Raw
        if ($content -notmatch '(?s)^---\r?\nname:\s*(.+?)\r?\nversion:\s*(.+?)\r?\ndepends_on:\s*(.+?)\r?\ndescription:\s*(.+?)\r?\n---') {
            Write-Host "FAIL: Missing or invalid YAML frontmatter in $($skill.Name)" -ForegroundColor Red
            $failed++
        }
    } else {
        Write-Host "FAIL: Missing SKILL.md in $($skill.Name)" -ForegroundColor Red
        $failed++
    }
}

# Test 2: Immutable Core Exists (reads canonical list from immutable-core.json)
$immutableCoreJson = Join-Path $skillsDir "immutable-core.json"
if (Test-Path $immutableCoreJson) {
    try {
        $coreConfig = Get-Content $immutableCoreJson -Raw | ConvertFrom-Json
        $immutableCore = $coreConfig.immutable_skills
    } catch {
        Write-Host "FAIL: Cannot parse immutable-core.json" -ForegroundColor Red
        $failed++
        $immutableCore = @()  # fallback to hardcoded list
    }
}
if (-not $immutableCore -or $immutableCore.Count -eq 0) {
    # Fallback if core.json missing or unparseable
    $immutableCore = @(
        "security-guard",
        "prompt-injection-guard",
        "zero-trust-orchestration",
        "immutable-core-directives",
        "auto-rollback-healing",
        "recursive-self-improvement"
    )
}

foreach ($core in $immutableCore) {
    # immutable-core.json is the SSOT itself, not a skill directory
    if ($core -eq "immutable-core.json") {
        $coreFilePath = Join-Path $skillsDir "immutable-core.json"
        if (-not (Test-Path $coreFilePath)) {
            Write-Host "FAIL: Immutable Core SSOT missing: skills/immutable-core.json" -ForegroundColor Red
            $failed++
        }
        continue
    }
    $coreDir = Join-Path $skillsDir $core
    $coreFile = Join-Path $coreDir "SKILL.md"
    if (-not (Test-Path $coreDir)) {
        Write-Host "FAIL: Immutable Core directory missing: $core" -ForegroundColor Red
        $failed++
    } elseif (-not (Test-Path $coreFile)) {
        Write-Host "FAIL: Immutable Core SKILL.md missing: $core/SKILL.md" -ForegroundColor Red
        $failed++
    }
}

# Test 3: JSON Schemas Validation
$schemasDir = (Resolve-Path (Join-Path $PSScriptRoot "..\skills\structured-swarm-artifacts\schemas")).Path
if (Test-Path $schemasDir) {
    $schemaFiles = Get-ChildItem -Path $schemasDir -Filter "*.json"
    foreach ($schema in $schemaFiles) {
        try {
            $content = Get-Content $schema.FullName -Raw
            $parsed = ConvertFrom-Json $content -ErrorAction Stop
            if (-not $parsed.type -and -not $parsed.'$schema') {
                Write-Host "FAIL: Missing schema structure in $($schema.Name)" -ForegroundColor Red
                $failed++
            }
        } catch {
            Write-Host "FAIL: Invalid JSON in schema $($schema.Name)" -ForegroundColor Red
            $failed++
        }
    }
}

if ($failed -gt 0) {
    Write-Host "Meta-RSI Regression Suite FAILED with $failed errors." -ForegroundColor Red
    exit 1
} else {
    Write-Host "Meta-RSI Regression Suite PASSED." -ForegroundColor Green
    exit 0
}
