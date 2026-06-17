$skillsDir = Join-Path $PSScriptRoot "skills"
$skills = Get-ChildItem -Path $skillsDir -Directory

foreach ($skill in $skills) {
    $skillFile = Join-Path $skill.FullName "SKILL.md"
    if (Test-Path $skillFile) {
        $content = Get-Content $skillFile -Raw
        
        # Check if version already exists
        if ($content -notmatch "version: ") {
            # Inject version and depends_on after name
            $newContent = $content -replace "(name:\s*[^\r\n]+)", "`$1`nversion: `"1.0.0`"`ndepends_on: []"
            Set-Content -Path $skillFile -Value $newContent -NoNewline
        }
    }
}
Write-Host "Injected version and depends_on."
