# Initialize Cline Memory Bank Structure
$memoryBankDir = "memory-bank"

if (!(Test-Path -Path $memoryBankDir)) {
    New-Item -ItemType Directory -Path $memoryBankDir | Out-Null
    Write-Host "Created memory-bank directory."
} else {
    Write-Host "memory-bank directory already exists."
}

$files = @{
    "projectbrief.md" = "# Project Brief`n`nDefine the core requirements and goals of the project here."
    "productContext.md" = "# Product Context`n`nWhy this project exists, problems it solves, and user experience goals."
    "activeContext.md" = "# Active Context`n`nCurrent work focus, recent changes, and next steps."
    "systemPatterns.md" = "# System Patterns`n`nSystem architecture, key technical decisions, and design patterns in use."
    "techContext.md" = "# Tech Context`n`nTechnologies used, development setup, and technical constraints."
    "progress.md" = "# Progress`n`nWhat works, what's left to build, current status, and known issues."
}

foreach ($file in $files.GetEnumerator()) {
    $filePath = Join-Path -Path $memoryBankDir -ChildPath $file.Key
    if (!(Test-Path -Path $filePath)) {
        Set-Content -Path $filePath -Value $file.Value
        Write-Host "Created $($file.Key)"
    } else {
        Write-Host "$($file.Key) already exists, skipping."
    }
}

Write-Host "Memory Bank initialization complete!"
