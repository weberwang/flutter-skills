param(
    [switch]$SkipCodexInstall
)

$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path (Join-Path $scriptRoot '..')).Path
$pluginName = 'flutter-skills'
$pluginRoot = Join-Path $repoRoot "plugins\$pluginName"
$pluginSkillsRoot = Join-Path $pluginRoot 'skills'
$sourceSkillsRoot = Join-Path $repoRoot 'skills'
$marketplaceRoot = Join-Path $repoRoot '.agents\plugins'
$marketplaceFile = Join-Path $marketplaceRoot 'marketplace.json'
$pluginManifest = Join-Path $pluginRoot '.codex-plugin\plugin.json'

if (-not (Test-Path -LiteralPath $pluginManifest)) {
    throw "未找到插件清单: $pluginManifest"
}

if (-not (Test-Path -LiteralPath $marketplaceFile)) {
    throw "未找到 marketplace 清单: $marketplaceFile"
}

if (-not (Test-Path -LiteralPath $sourceSkillsRoot)) {
    throw "未找到技能源码目录: $sourceSkillsRoot"
}

# 安装前先把仓库 skills 同步到插件目录，确保插件只有一个真实来源。
if (Test-Path -LiteralPath $pluginSkillsRoot) {
    Remove-Item -LiteralPath $pluginSkillsRoot -Recurse -Force
}

New-Item -ItemType Directory -Path $pluginSkillsRoot | Out-Null
Copy-Item -Path (Join-Path $sourceSkillsRoot '*') -Destination $pluginSkillsRoot -Recurse -Force

$skillCount = (Get-ChildItem -LiteralPath $sourceSkillsRoot -Directory).Count
Write-Host "已同步 $skillCount 个 skills 到插件目录: $pluginSkillsRoot"

if ($SkipCodexInstall) {
    Write-Host '已跳过 Codex CLI 安装步骤。'
    exit 0
}

if (-not (Get-Command codex -ErrorAction SilentlyContinue)) {
    throw '未找到 codex 命令，请先安装并确保其在 PATH 中。'
}

# marketplace 名称直接从仓库清单读取，避免脚本与配置手写漂移。
$marketplacePayload = Get-Content -Raw -LiteralPath $marketplaceFile | ConvertFrom-Json
if (-not $marketplacePayload.name) {
    throw "marketplace.json 缺少 name 字段: $marketplaceFile"
}

$marketplaceName = [string]$marketplacePayload.name

# repo-local marketplace 不是隐式发现目标，这里先尝试注册；如果已经存在则继续安装。
& codex plugin marketplace add $marketplaceRoot
if ($LASTEXITCODE -ne 0) {
    Write-Warning "marketplace 注册返回非零退出码，继续尝试安装插件。退出码: $LASTEXITCODE"
}

& codex plugin add "$pluginName@$marketplaceName"
if ($LASTEXITCODE -ne 0) {
    throw "codex plugin add $pluginName@$marketplaceName 执行失败，退出码: $LASTEXITCODE"
}

Write-Host "插件已安装: $pluginName@$marketplaceName"
