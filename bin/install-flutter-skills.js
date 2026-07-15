#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

const SKILL_NAMES = [
  "grilling",
  "flutter-app-orchestrator",
  "flutter-product-spec",
  "flutter-ux-ui-quality",
  "flutter-hifi-mockup",
  "flutter-asset-atlas",
  "flutter-pencil-design",
  "flutter-tech-design",
  "flutter-project-init",
  "flutter-implementation-plan",
  "flutter-subagent-delivery",
  "flutter-quality-review",
  "flutter-release-readiness",
];

// 解析安装器支持的最小命令行参数集合。
function parseArgs(argv) {
  const options = {
    dest: process.env.FLUTTER_SKILLS_DEST || path.join(process.cwd(), ".agents", "skills"),
    force: false,
    dryRun: false,
    help: false,
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];

    if (arg === "--") {
      continue;
    } else if (arg === "--help" || arg === "-h") {
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

// 输出可复制的安装命令和参数说明。
function printHelp() {
  console.log(`Flutter Skills installer

Usage:
  npx -y github:weberwang/flutter-skills

Options:
  --dest <path>   Install target. Defaults to ./.agents/skills under the current directory.
  --force         Replace existing installed skill directories.
  --dry-run       Print actions without writing files.
  -h, --help      Show this help.

Environment:
  FLUTTER_SKILLS_DEST can override the default install target.
`);
}

// 解析目标目录，避免空路径导致写入位置不可控。
function resolveInstallRoot(dest) {
  if (!dest || !dest.trim()) {
    throw new Error("Install target is empty.");
  }

  return path.resolve(dest);
}

// 判断目标子路径是否仍在安装根目录下，用于限制覆盖删除范围。
function isInside(parent, child) {
  const relative = path.relative(parent, child);
  return relative === "" || (!relative.startsWith("..") && !path.isAbsolute(relative));
}

// 兼容旧版 Node：没有 fs.cpSync 时手动递归复制目录。
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

// 校验 npx 下载的包内确实包含全部 skill，避免写入半成品。
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

// 执行安装；默认拒绝覆盖，只有显式 --force 才替换同名目录。
function installSkills(options) {
  const packageRoot = path.resolve(__dirname, "..");
  const installRoot = resolveInstallRoot(options.dest);
  const sources = collectSources(packageRoot);

  console.log(`Installing Flutter skills to ${installRoot}`);

  if (options.dryRun) {
    for (const { name } of sources) {
      console.log(`[dry-run] ${name}`);
    }
    return;
  }

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

// 统一入口，确保错误以非零退出码返回给 npx。
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
