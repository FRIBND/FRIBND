[CmdletBinding()]
param(
    [string]$SourceGitHubPath = 'D:\X\ND\ENSDF\.github',
    [string]$PluginRoot = (Join-Path $PSScriptRoot 'plugins\ensdf-agent'),
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$managedEntries = @(
    'agents',
    'copilot-instructions.md',
    'hooks',
    'prompts',
    'scripts',
    'skills'
)

$excludedSegments = @(
    'docs',
    'temp',
    '__pycache__'
)

$preservedPluginFiles = @(
    'README.md',
    'plugin.json',
    'hooks.json',
    'hooks/scripts/block_git_revert.py'
)

function Normalize-RelativePath {
    param([string]$Path)

    return ($Path -replace '/', '\').TrimStart('\')
}
$preservedPluginFiles = $preservedPluginFiles | ForEach-Object { Normalize-RelativePath $_ }

function Test-ExcludedRelativePath {
    param([string]$RelativePath)

    $normalized = Normalize-RelativePath $RelativePath
    foreach ($segment in $excludedSegments) {
        if ($normalized -eq $segment -or $normalized.StartsWith("$segment\", [System.StringComparison]::OrdinalIgnoreCase)) {
            return $true
        }

        if ($normalized -match "(^|\\)$([regex]::Escape($segment))(\\|$)") {
            return $true
        }
    }

    return $false
}

function Get-ManagedSourceFiles {
    param([string]$SourceRoot)

    $result = [System.Collections.Generic.List[string]]::new()

    foreach ($entry in $managedEntries) {
        $fullPath = Join-Path $SourceRoot $entry
        if (-not (Test-Path $fullPath)) {
            continue
        }

        if ((Get-Item $fullPath) -is [System.IO.DirectoryInfo]) {
            Get-ChildItem -Path $fullPath -Recurse -File | ForEach-Object {
                $relative = $_.FullName.Substring($SourceRoot.Length + 1)
                if (-not (Test-ExcludedRelativePath $relative)) {
                    $result.Add((Normalize-RelativePath $relative))
                }
            }
            continue
        }

        $relativeFile = Normalize-RelativePath $entry
        if (-not (Test-ExcludedRelativePath $relativeFile)) {
            $result.Add($relativeFile)
        }
    }

    return $result | Sort-Object -Unique
}

function Get-ManagedTargetFiles {
    param([string]$TargetRoot)

    $result = [System.Collections.Generic.List[string]]::new()

    foreach ($entry in $managedEntries) {
        $fullPath = Join-Path $TargetRoot $entry
        if (-not (Test-Path $fullPath)) {
            continue
        }

        if ((Get-Item $fullPath) -is [System.IO.DirectoryInfo]) {
            Get-ChildItem -Path $fullPath -Recurse -File | ForEach-Object {
                $relative = $_.FullName.Substring($TargetRoot.Length + 1)
                $normalized = Normalize-RelativePath $relative
                if ((-not (Test-ExcludedRelativePath $normalized)) -and ($preservedPluginFiles -notcontains $normalized)) {
                    $result.Add($normalized)
                }
            }
            continue
        }

        $relativeFile = Normalize-RelativePath $entry
        if ((-not (Test-ExcludedRelativePath $relativeFile)) -and ($preservedPluginFiles -notcontains $relativeFile)) {
            $result.Add($relativeFile)
        }
    }

    return $result | Sort-Object -Unique
}

function Ensure-Directory {
    param([string]$DirectoryPath)

    if (-not (Test-Path $DirectoryPath)) {
        New-Item -ItemType Directory -Path $DirectoryPath -Force | Out-Null
    }
}

function Remove-ExcludedDirectories {
    param(
        [string]$RootPath,
        [bool]$PreviewOnly
    )

    $excludedDirectories = Get-ChildItem -Path $RootPath -Directory -Recurse -Force |
        Where-Object { $excludedSegments -contains $_.Name } |
        Sort-Object FullName -Descending

    foreach ($directory in $excludedDirectories) {
        $relative = $directory.FullName.Substring($RootPath.Length + 1)
        if ($PreviewOnly) {
            Write-Host "REMOVE $relative"
        } else {
            Remove-Item -Path $directory.FullName -Force -Recurse
            Write-Host "REMOVED $relative"
        }
    }
}

if (-not (Test-Path $SourceGitHubPath -PathType Container)) {
    throw "Source .github path not found: $SourceGitHubPath"
}

if (-not (Test-Path $PluginRoot -PathType Container)) {
    throw "Plugin root not found: $PluginRoot"
}

$sourceFiles = Get-ManagedSourceFiles -SourceRoot $SourceGitHubPath
$targetFiles = Get-ManagedTargetFiles -TargetRoot $PluginRoot
$sourceSet = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$copied = 0
$removed = 0
$skipped = 0

foreach ($relative in $sourceFiles) {
    [void]$sourceSet.Add($relative)

    $sourcePath = Join-Path $SourceGitHubPath $relative
    $targetPath = Join-Path $PluginRoot $relative

    Ensure-Directory -DirectoryPath (Split-Path $targetPath -Parent)

    $copyNeeded = $true
    if (Test-Path $targetPath -PathType Leaf) {
        $sourceHash = (Get-FileHash -Path $sourcePath -Algorithm SHA256).Hash
        $targetHash = (Get-FileHash -Path $targetPath -Algorithm SHA256).Hash
        if ($sourceHash -eq $targetHash) {
            $copyNeeded = $false
        }
    }

    if (-not $copyNeeded) {
        Write-Host "SKIP   $relative"
        $skipped++
        continue
    }

    if ($DryRun) {
        Write-Host "COPY   $relative"
    } else {
        Copy-Item -Path $sourcePath -Destination $targetPath -Force
        Write-Host "COPIED $relative"
    }
    $copied++
}

foreach ($relative in $targetFiles) {
    if ($sourceSet.Contains($relative)) {
        continue
    }

    $targetPath = Join-Path $PluginRoot $relative
    if ($DryRun) {
        Write-Host "REMOVE $relative"
    } else {
        Remove-Item -Path $targetPath -Force
        Write-Host "REMOVED $relative"
    }
    $removed++
}

Remove-ExcludedDirectories -RootPath $PluginRoot -PreviewOnly ([bool]$DryRun)

if (-not $DryRun) {
    Get-ChildItem -Path $PluginRoot -Directory -Recurse |
        Sort-Object FullName -Descending |
        ForEach-Object {
            if (-not (Get-ChildItem -Path $_.FullName -Force)) {
                Remove-Item -Path $_.FullName -Force
            }
        }
}

Write-Host ''
Write-Host 'Sync Summary'
Write-Host "  Source:  $SourceGitHubPath"
Write-Host "  Target:  $PluginRoot"
Write-Host "  Copied:  $copied"
Write-Host "  Removed: $removed"
Write-Host "  Skipped: $skipped"
if ($DryRun) {
    Write-Host '  Mode:    dry-run'
}