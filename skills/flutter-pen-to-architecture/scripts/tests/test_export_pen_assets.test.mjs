import assert from "node:assert/strict";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { describe, test } from "node:test";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";
import JSZip from "jszip";

const CURRENT_FILE = fileURLToPath(import.meta.url);
const SCRIPT = path.resolve(path.dirname(CURRENT_FILE), "..", "export_pen_assets.mjs");
const PNG_BASE64 =
  "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9WnWZJ4AAAAASUVORK5CYII=";
const PNG_BUFFER = Buffer.from(PNG_BASE64, "base64");

/**
 * 运行 Node CLI 脚本并收集输出。
 * @param {string[]} args 参数列表。
 * @returns {Promise<{ code: number, stdout: string, stderr: string }>}
 */
function runCli(args) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [SCRIPT, ...args], {
      stdio: ["ignore", "pipe", "pipe"],
    });

    let stdout = "";
    let stderr = "";

    child.stdout.on("data", (chunk) => {
      stdout += chunk.toString();
    });
    child.stderr.on("data", (chunk) => {
      stderr += chunk.toString();
    });
    child.on("error", reject);
    child.on("close", (code) => {
      resolve({ code: code ?? 1, stdout, stderr });
    });
  });
}

/**
 * 创建用于测试的 `.pen` ZIP 文件。
 * @param {string} filePath 输出路径。
 * @param {Record<string, Buffer>} entries ZIP 条目。
 * @returns {Promise<void>}
 */
async function createPenArchive(filePath, entries) {
  const zip = new JSZip();
  for (const [entryName, content] of Object.entries(entries)) {
    zip.file(entryName, content);
  }
  const buffer = await zip.generateAsync({ type: "nodebuffer" });
  await fs.writeFile(filePath, buffer);
}

describe("export_pen_assets CLI", () => {
  test("exports image from pen archive", async () => {
    const tempDir = await fs.mkdtemp(path.join(os.tmpdir(), "export-assets-"));
    const penPath = path.join(tempDir, "sample.pen");
    const projectRoot = path.join(tempDir, "flutter_app");
    await fs.mkdir(path.join(projectRoot, "assets", "images"), { recursive: true });
    await createPenArchive(penPath, { "images/hero.png": PNG_BUFFER });

    const result = await runCli(["--pen-file", penPath, "--project-root", projectRoot]);
    const outputPath = path.join(projectRoot, "assets", "images", "hero.png");

    assert.equal(result.code, 0, result.stderr);
    assert.deepEqual(await fs.readFile(outputPath), PNG_BUFFER);
    assert.equal(JSON.parse(result.stdout).exported[0].source, ".pen");

    await fs.rm(tempDir, { recursive: true, force: true });
  });

  test("falls back to mcp manifest", async () => {
    const tempDir = await fs.mkdtemp(path.join(os.tmpdir(), "export-assets-"));
    const penPath = path.join(tempDir, "empty.pen");
    const projectRoot = path.join(tempDir, "flutter_app");
    const manifestPath = path.join(tempDir, "mcp_assets.json");
    await fs.mkdir(path.join(projectRoot, "assets", "images"), { recursive: true });
    await createPenArchive(penPath, {});
    await fs.writeFile(
      manifestPath,
      JSON.stringify({
        assets: [
          {
            id: "hero-banner",
            file_name: "hero-banner.png",
            data_base64: PNG_BASE64,
          },
        ],
      }),
      "utf8",
    );

    const result = await runCli([
      "--pen-file",
      penPath,
      "--project-root",
      projectRoot,
      "--mcp-assets",
      manifestPath,
    ]);
    const outputPath = path.join(projectRoot, "assets", "images", "hero-banner.png");

    assert.equal(result.code, 0, result.stderr);
    assert.deepEqual(await fs.readFile(outputPath), PNG_BUFFER);
    assert.equal(JSON.parse(result.stdout).exported[0].source, "Pencil MCP");

    await fs.rm(tempDir, { recursive: true, force: true });
  });

  test("overwrites existing file with same name", async () => {
    const tempDir = await fs.mkdtemp(path.join(os.tmpdir(), "export-assets-"));
    const penPath = path.join(tempDir, "sample.pen");
    const projectRoot = path.join(tempDir, "flutter_app");
    const imagePath = path.join(projectRoot, "assets", "images", "hero.png");
    await fs.mkdir(path.dirname(imagePath), { recursive: true });
    await fs.writeFile(imagePath, Buffer.from("old-image"));
    await createPenArchive(penPath, { "images/hero.png": PNG_BUFFER });

    const result = await runCli(["--pen-file", penPath, "--project-root", projectRoot]);

    assert.equal(result.code, 0, result.stderr);
    assert.deepEqual(await fs.readFile(imagePath), PNG_BUFFER);
    assert.equal(JSON.parse(result.stdout).exported[0].status, "overwritten");

    await fs.rm(tempDir, { recursive: true, force: true });
  });
});
