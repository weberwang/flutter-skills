/**
 * 确保 Flutter 项目声明图片资源目录。
 */

import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ASSET_ENTRY = "    - assets/images/";

/**
 * 解析命令行参数。
 * @param {string[]} argv 命令行参数。
 * @returns {{ projectRoot: string }}
 */
function parseArguments(argv) {
  let projectRoot = "";
  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === "--project-root") {
      projectRoot = argv[index + 1] ?? "";
      index += 1;
    }
  }

  if (!projectRoot) {
    throw new Error("--project-root is required");
  }

  return { projectRoot };
}

/**
 * 确保 `pubspec.yaml` 已声明 `assets/images/` 目录。
 * @param {string} projectRoot Flutter 项目根目录。
 * @returns {Promise<{ changed: boolean, message: string }>}
 */
export async function ensureAssetsDeclared(projectRoot) {
  const pubspecPath = path.join(projectRoot, "pubspec.yaml");
  let content;
  try {
    content = await fs.readFile(pubspecPath, "utf8");
  } catch (error) {
    if (error && typeof error === "object" && "code" in error && error.code === "ENOENT") {
      throw new Error(`pubspec.yaml not found under ${projectRoot}`);
    }
    throw error;
  }

  if (content.includes("    - assets/images/\n") || content.includes("    - assets/images/\r\n")) {
    return { changed: false, message: "assets/images/ already declared" };
  }

  // 按 Flutter 常见结构补齐资源声明，避免无关字段被重写。
  if (!content.includes("flutter:\n")) {
    content = `${content.trimEnd()}\n\nflutter:\n  assets:\n${ASSET_ENTRY}\n`;
  } else if (!content.includes("  assets:\n")) {
    content = content.replace("flutter:\n", `flutter:\n  assets:\n${ASSET_ENTRY}\n`);
  } else {
    content = content.replace("  assets:\n", `  assets:\n${ASSET_ENTRY}\n`);
  }

  await fs.writeFile(pubspecPath, content, "utf8");
  return { changed: true, message: "assets/images/ added" };
}

/**
 * CLI 入口。
 * @returns {Promise<number>}
 */
async function main() {
  try {
    const { projectRoot } = parseArguments(process.argv.slice(2));
    const { message } = await ensureAssetsDeclared(projectRoot);
    process.stdout.write(`${message}\n`);
    return 0;
  } catch (error) {
    process.stderr.write(`${error instanceof Error ? error.message : String(error)}\n`);
    return 1;
  }
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  const exitCode = await main();
  process.exit(exitCode);
}
