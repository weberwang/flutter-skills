/**
 * 从 Pencil 设计输入导出图片资源。
 */

import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import JSZip from "jszip";

const IMAGE_SUFFIXES = new Set([".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"]);

/**
 * 解析命令行参数。
 * @param {string[]} argv 命令行参数。
 * @returns {{ penFile: string, projectRoot: string, mcpAssets: string }}
 */
function parseArguments(argv) {
  const result = {
    penFile: "",
    projectRoot: "",
    mcpAssets: "",
  };

  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === "--pen-file") {
      result.penFile = argv[index + 1] ?? "";
      index += 1;
    } else if (argument === "--project-root") {
      result.projectRoot = argv[index + 1] ?? "";
      index += 1;
    } else if (argument === "--mcp-assets") {
      result.mcpAssets = argv[index + 1] ?? "";
      index += 1;
    }
  }

  if (!result.penFile) {
    throw new Error("--pen-file is required");
  }
  if (!result.projectRoot) {
    throw new Error("--project-root is required");
  }

  return result;
}

/**
 * 判断条目是否为可导出的图片。
 * @param {string} entryName 压缩包内条目名。
 * @returns {boolean}
 */
function isExportableImage(entryName) {
  return IMAGE_SUFFIXES.has(path.extname(entryName).toLowerCase());
}

/**
 * 组装导出结果。
 * @param {string} sourceId 原始资源标识。
 * @param {string} fileName 导出文件名。
 * @param {string} source 来源。
 * @param {boolean} overwritten 是否覆盖同名文件。
 * @returns {{ source_id: string, file_name: string, flutter_path: string, source: string, status: string }}
 */
function buildExportRecord(sourceId, fileName, source, overwritten) {
  return {
    source_id: sourceId,
    file_name: fileName,
    flutter_path: `assets/images/${fileName}`,
    source,
    status: overwritten ? "overwritten" : "exported",
  };
}

/**
 * 优先从 `.pen` 压缩包中提取可导出的图片资源。
 * @param {string} penFile `.pen` 文件路径。
 * @param {string} outputDir 输出目录。
 * @returns {Promise<Array<{ source_id: string, file_name: string, flutter_path: string, source: string, status: string }>>}
 */
export async function exportFromPenArchive(penFile, outputDir) {
  const zipBuffer = await fs.readFile(penFile);
  const bundle = await JSZip.loadAsync(zipBuffer);
  const exported = [];

  for (const [entryName, entry] of Object.entries(bundle.files)) {
    if (entry.dir || !isExportableImage(entryName)) {
      continue;
    }

    const fileName = path.basename(entryName);
    const targetPath = path.join(outputDir, fileName);
    const overwritten = await fileExists(targetPath);
    const fileBuffer = await entry.async("nodebuffer");
    // 同名文件默认覆盖，确保导出的资源始终反映当前设计输入。
    await fs.writeFile(targetPath, fileBuffer);
    exported.push(buildExportRecord(entryName, fileName, ".pen", overwritten));
  }

  return exported;
}

/**
 * 当 `.pen` 无法提供图片时，回退到 Pencil MCP 资源清单。
 * @param {string} manifestFile MCP 资源清单文件。
 * @param {string} outputDir 输出目录。
 * @returns {Promise<Array<{ source_id: string, file_name: string, flutter_path: string, source: string, status: string }>>}
 */
export async function exportFromMcpManifest(manifestFile, outputDir) {
  const payload = JSON.parse(await fs.readFile(manifestFile, "utf8"));
  const exported = [];

  for (const asset of payload.assets ?? []) {
    const targetPath = path.join(outputDir, asset.file_name);
    const overwritten = await fileExists(targetPath);
    const fileBuffer = Buffer.from(asset.data_base64, "base64");
    await fs.writeFile(targetPath, fileBuffer);
    exported.push(buildExportRecord(asset.id, asset.file_name, "Pencil MCP", overwritten));
  }

  return exported;
}

/**
 * 检查文件是否存在。
 * @param {string} filePath 文件路径。
 * @returns {Promise<boolean>}
 */
async function fileExists(filePath) {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
}

/**
 * CLI 入口。
 * @returns {Promise<number>}
 */
async function main() {
  try {
    const { penFile, projectRoot, mcpAssets } = parseArguments(process.argv.slice(2));
    await fs.access(penFile);

    const outputDir = path.join(projectRoot, "assets", "images");
    await fs.mkdir(outputDir, { recursive: true });

    let exported = await exportFromPenArchive(penFile, outputDir);
    if (exported.length === 0 && mcpAssets) {
      exported = await exportFromMcpManifest(mcpAssets, outputDir);
    }

    if (exported.length === 0) {
      process.stderr.write("No exportable images found in .pen archive\n");
      return 1;
    }

    process.stdout.write(`${JSON.stringify({ exported })}\n`);
    return 0;
  } catch (error) {
    if (error && typeof error === "object" && "code" in error && error.code === "ENOENT") {
      process.stderr.write(`.pen file not found: ${process.argv[process.argv.indexOf("--pen-file") + 1] ?? ""}\n`);
      return 1;
    }
    process.stderr.write(`${error instanceof Error ? error.message : String(error)}\n`);
    return 1;
  }
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  const exitCode = await main();
  process.exit(exitCode);
}
