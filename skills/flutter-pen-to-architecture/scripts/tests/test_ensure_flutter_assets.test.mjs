import assert from "node:assert/strict";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { describe, test } from "node:test";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";

const CURRENT_FILE = fileURLToPath(import.meta.url);
const SCRIPT = path.resolve(path.dirname(CURRENT_FILE), "..", "ensure_flutter_assets.mjs");

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

describe("ensure_flutter_assets CLI", () => {
  test("missing pubspec returns non-zero", async () => {
    const tempDir = await fs.mkdtemp(path.join(os.tmpdir(), "ensure-assets-"));
    const result = await runCli(["--project-root", tempDir]);
    assert.notEqual(result.code, 0);
    assert.match(result.stderr, /pubspec\.yaml/);
    await fs.rm(tempDir, { recursive: true, force: true });
  });

  test("adds assets images once", async () => {
    const tempDir = await fs.mkdtemp(path.join(os.tmpdir(), "ensure-assets-"));
    const pubspecPath = path.join(tempDir, "pubspec.yaml");
    await fs.writeFile(
      pubspecPath,
      "name: demo\nflutter:\n  uses-material-design: true\n",
      "utf8",
    );

    const first = await runCli(["--project-root", tempDir]);
    const second = await runCli(["--project-root", tempDir]);
    const content = await fs.readFile(pubspecPath, "utf8");

    assert.equal(first.code, 0, first.stderr);
    assert.equal(second.code, 0, second.stderr);
    assert.equal((content.match(/assets\/images\//g) ?? []).length, 1);

    await fs.rm(tempDir, { recursive: true, force: true });
  });
});
