#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "meta-ads-mcp"
SKILL = SKILL_DIR / "SKILL.md"

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


if not SKILL.exists():
    fail("missing meta-ads-mcp/SKILL.md")
else:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    for field in ["name: meta-ads-mcp", "version:", "license:", "description:"]:
        if field not in text:
            fail(f"SKILL.md missing frontmatter field: {field}")

    refs = re.findall(r"\[`[^`]+`\]\((references/[^)]+)\)", text)
    if not refs:
        fail("SKILL.md should link reference files")
    for ref in refs:
        if not (SKILL_DIR / ref).exists():
            fail(f"SKILL.md links missing reference: {ref}")

for forbidden in ["README.md", "CHANGELOG.md", "LICENSE.txt", "package.json"]:
    if (SKILL_DIR / forbidden).exists():
        fail(f"repo-only file must stay outside skill dir: meta-ads-mcp/{forbidden}")

for path in sorted(SKILL_DIR.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    if "�" in text:
        fail(f"encoding replacement character found in {rel}")
    if re.search(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*[\"'][^\"']{8,}[\"']", text):
        fail(f"hardcoded-looking secret placeholder found in {rel}")
    if re.search(r'"username"\s*:\s*"admin"', text):
        fail(f"admin username example found in {rel}")
    if re.search(r"xxxx\s+xxxx|yyyy\s+yyyy", text, re.I):
        fail(f"hardcoded-looking credential placeholder found in {rel}")

pkg_path = ROOT / "package.json"
if not pkg_path.exists():
    fail("missing package.json")
else:
    pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
    if pkg.get("name") != "meta-ads-mcp":
        fail("package.json name must be meta-ads-mcp")
    if pkg.get("license") != "MIT-0":
        fail("package.json license must be MIT-0")
    files = pkg.get("files", [])
    broad = [f for f in files if f.rstrip("/") in {"meta-ads-mcp", "meta-ads-mcp/**"}]
    if broad:
        fail(f"package.json files should be explicit, not broad: {broad}")

if errors:
    print("Validation failed:")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("Skill validation passed")
