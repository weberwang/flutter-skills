#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

const SKILL_NAMES = [
  "flutter-app-orchestrator",
  "flutter-product-spec",
  "flutter-ux-ui-quality",
  "flutter-hifi-mockup",
  "flutter-pencil-design",
  "flutter-tech-design",
  "flutter-project-init",
  "flutter-implementation-plan",
  "flutter-subagent-delivery",
  "flutter-quality-review",
  "flutter-release-readiness",
];

// 解析命令行参数，只保留安装所需的最小选项。
function parseArgs(argv) {
  const options = {
    dest: process.env.FLUTTER_SKILLS_DEST || path.join(os.homedir(), ".agents", "skills"),
    force: false,
    dryRun: false,
    help: false,
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];

    if (arg === "--help" || arg === "-h") {
      options.help = true;
    } else if (arg === "--force") {
      options.force = true;
    } else if (arg === "--dry-run") {
      options.dryRun = true;
    } else if (arg === "--dest" || arg === "-d") {
      i += 1;
      if (!argv[i]) {
        throw new Error("Missing value for --dest.");
      }
      options.dest = argv[i];
    } else if (arg.startsWith("--dest=")) {
      options.dest = arg.slice("--dest=".length);
    } else {
      throw new Error(`Unknown option: ${arg}`);
    }
  }

  return options;
}

// 输出可复制的使用说明。
function printHelp() {
  console.log(`Flutter Skills installer

Usage:
  npx --yes --package https://github.com/weberwang/flutter-skills/archive/refs/heads/master.tar.gz flutter-skills

Options:
  --dest <path>   Install target. Defaults to ~/.agents/skills.
  --force         Replace existing installed skill directories.
  --dry-run       Print actions without writing files.
  -h, --help      Show this help.

Environment:
  FLUTTER_SKILLS_DEST can override the default install target.
`);
}

// 确保目标路径不会因为空值或相对路径导致误删。
function resolveInstallRoot(dest) {
  if (!dest || !dest.trim()) {
    throw new Error("Install target is empty.");
  }

  return path.resolve(dest);
}

// 判断子路径是否仍在安装根目录下，用于限制 force 删除范围。
function isInside(parent, child) {
  const relative = path.relative(parent, child);
  return relative === "" || (!relative.startsWith("..") && !path.isAbsolute(relative));
}

// 在旧版 Node 没有 fs.cpSync 时提供递归复制实现。
function copyDirectory(source, target) {
  if (typeof fs.cpSync === "function") {
    fs.cpSync(source, target, { recursive: true });
    return;
  }

  fs.mkdirSync(target, { recursive: true });

  for (const entry of fs.readdirSync(source, { withFileTypes: true })) {
    const from = path.join(source, entry.name);
    const to = path.join(target, entry.name);

    if (entry.isDirectory()) {
      copyDirectory(from, to);
    } else if (entry.isSymbolicLink()) {
      fs.symlinkSync(fs.readlinkSync(from), to);
    } else {
      fs.copyFileSync(from, to);
    }
  }
}

// 校验仓库包内确实包含所有 skill，避免 npx 缓存不完整时写入半成品。
function collectSources(packageRoot) {
  return SKILL_NAMES.map((name) => {
    const source = path.join(packageRoot, name);
    const skillFile = path.join(source, "SKILL.md");

    if (!fs.existsSync(skillFile)) {
      throw new Error(`Missing skill source: ${skillFile}`);
    }

    return { name, source };
  });
}

// 安装所有 skill；默认拒绝覆盖，只有显式 --force 才替换。
function installSkills(options) {
  const packageRoot = path.resolve(__dirname, "..");
  const installRoot = resolveInstallRoot(options.dest);
  const sources = collectSources(packageRoot);

  const conflicts = sources
    .map(({ name }) => path.join(installRoot, name))
    .filter((target) => fs.existsSync(target));

  if (conflicts.length > 0 && !options.force) {
    console.error("Install stopped because these skills already exist:");
    for (const conflict of conflicts) {
      console.error(`- ${conflict}`);
    }
    console.error("Run again with --force to replace them.");
    process.exitCode = 1;
    return;
  }

  console.log(`Installing Flutter skills to ${installRoot}`);

  if (options.dryRun) {
    for (const { name } of sources) {
      console.log(`[dry-run] ${name}`);
    }
    return;
  }

  fs.mkdirSync(installRoot, { recursive: true });

  for (const { name, source } of sources) {
    const target = path.join(installRoot, name);

    if (!isInside(installRoot, target)) {
      throw new Error(`Refusing to write outside install root: ${target}`);
    }

    if (fs.existsSync(target)) {
      fs.rmSync(target, { recursive: true, force: true });
    }

    copyDirectory(source, target);
    console.log(`Installed ${name}`);
  }

  console.log("Install complete. Restart Codex to pick up new skills.");
}

// 统一入口，保证错误以非零退出码返回给 npx。
function main() {
  try {
    const options = parseArgs(process.argv.slice(2));

    if (options.help) {
      printHelp();
      return;
    }

    installSkills(options);
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}

main();
