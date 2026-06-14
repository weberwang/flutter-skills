#!/usr/bin/env node

/**
 * 解析命令行参数，并把 skills 安装到目标目录。
 * 这里默认覆盖目标目录，避免用户每次手工清理旧副本。
 */

const fs = require("node:fs/promises");
const path = require("node:path");

/**
 * 打印简洁帮助，避免误用时只能看到 Node 堆栈。
 */
function printHelp() {
  console.log(`用法:
  flutter-skills install [--target <目录>]

说明:
  install                 把当前包内的 skills 安装到目标目录的 .agents/skills
  --target <目录>         指定安装根目录，默认使用当前执行目录
`);
}

/**
 * 解析 install 命令的目标目录。
 * 保持参数模型极简，只支持当前需求需要的一个可选目标参数。
 */
function parseInstallTarget(argv) {
  const targetFlagIndex = argv.indexOf("--target");
  if (targetFlagIndex === -1) {
    return process.cwd();
  }

  const targetRoot = argv[targetFlagIndex + 1];
  if (!targetRoot) {
    throw new Error("--target 需要一个目录参数");
  }

  return path.resolve(targetRoot);
}

/**
 * 执行安装时始终从包自身目录复制 skills，保证来源稳定且不依赖调用方仓库结构。
 */
async function installSkills(targetRoot) {
  const packageRoot = path.resolve(__dirname, "..");
  const sourceSkillsRoot = path.join(packageRoot, "skills");
  const targetSkillsRoot = path.join(targetRoot, ".agents", "skills");

  await fs.access(sourceSkillsRoot);
  await fs.rm(targetSkillsRoot, { recursive: true, force: true });
  await fs.mkdir(targetSkillsRoot, { recursive: true });
  await fs.cp(sourceSkillsRoot, targetSkillsRoot, { recursive: true });

  const copiedEntries = await fs.readdir(targetSkillsRoot, { withFileTypes: true });
  const skillCount = copiedEntries.filter((entry) => entry.isDirectory()).length;
  console.log(`已安装 ${skillCount} 个 skills 到 ${targetSkillsRoot}`);
}

/**
 * 主入口只负责命令分发，让安装逻辑保持可读和可测试。
 */
async function main() {
  const [, , command, ...restArgs] = process.argv;

  if (!command || command === "--help" || command === "-h") {
    printHelp();
    return;
  }

  if (command !== "install") {
    throw new Error(`不支持的命令: ${command}`);
  }

  const targetRoot = parseInstallTarget(restArgs);
  await installSkills(targetRoot);
}

main().catch((error) => {
  console.error(error.message);
  printHelp();
  process.exit(1);
});
