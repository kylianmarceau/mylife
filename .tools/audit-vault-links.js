#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

const root = process.cwd();
const ignoredDirs = new Set([".git", ".obsidian", ".claudian", "node_modules"]);
const markdownFiles = [];

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (ignoredDirs.has(entry.name)) continue;

    const filePath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(filePath);
    } else if (entry.isFile() && filePath.endsWith(".md")) {
      markdownFiles.push(filePath);
    }
  }
}

function isExternal(target) {
  return (
    target.startsWith("http://") ||
    target.startsWith("https://") ||
    target.startsWith("mailto:") ||
    target.startsWith("app://") ||
    target.startsWith("#")
  );
}

function stripAnchor(target) {
  return target.split("#")[0];
}

walk(root);

const broken = [];
const linkPattern = /!??\[[^\]]*\]\(([^)]+)\)/g;

for (const file of markdownFiles) {
  const text = fs.readFileSync(file, "utf8");
  let match;

  while ((match = linkPattern.exec(text))) {
    let target = match[1].trim();
    if (!target || isExternal(target)) continue;

    target = stripAnchor(target);
    if (!target) continue;

    const decodedTarget = decodeURIComponent(target);
    const resolved = path.resolve(path.dirname(file), decodedTarget);

    if (!fs.existsSync(resolved)) {
      broken.push({
        file: path.relative(root, file),
        target: decodedTarget,
      });
    }
  }
}

console.log(`Markdown files checked: ${markdownFiles.length}`);
console.log(`Broken Markdown links: ${broken.length}`);

for (const item of broken) {
  console.log(`${item.file} -> ${item.target}`);
}

process.exitCode = broken.length ? 1 : 0;
