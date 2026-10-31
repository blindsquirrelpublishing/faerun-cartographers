#!/usr/bin/env python3
"""Check engineering package files. This is not a host installation test."""
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = "faerun-engineering-blueprints"
PLUGIN = ROOT / "plugins" / NAME
EXPECTED = {
    "faerun-engineering-base",
    "faerun-city-master-blueprint",
    "faerun-cadastral-property-blueprint",
    "faerun-topographical-engineering-blueprint",
    "faerun-civil-infrastructure-blueprint",
    "faerun-arcane-leyline-blueprint",
}


def check(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    portable = read_json(PLUGIN / "plugin.json")
    codex = read_json(PLUGIN / ".codex-plugin/plugin.json")
    claude = read_json(PLUGIN / ".claude-plugin/plugin.json")
    for manifest in (portable, codex, claude):
        check(manifest["name"] == NAME, "Plugin name mismatch")
        check(manifest["version"] == "1.0.0", "Plugin version mismatch")
        for key in ("description", "author", "repository"):
            check(manifest[key] == claude[key], f"Metadata mismatch: {key}")
    check(portable["$schema"] ==
          "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "Wrong schema")
    check(not {"skills", "mcpServers", "apps", "interface"} & portable.keys(),
          "Nonportable root fields")
    face = portable["extensions"]["com.openai"]["interface"]
    check(face == codex["interface"], "OpenAI display metadata mismatch")
    check(len(face["shortDescription"]) <= 30, "Subtitle too long")
    check(face["category"] == "Creativity", "Unexpected category")
    check(codex["skills"] == "./skills/", "Wrong Codex skill path")

    for catalog_path in (".agents/plugins/marketplace.json",
                         ".claude-plugin/marketplace.json"):
        catalog = read_json(ROOT / catalog_path)
        entries = [p for p in catalog["plugins"] if p["name"] == NAME]
        check(len(entries) == 1, f"Missing or duplicate entry: {catalog_path}")
        source = entries[0]["source"]
        path = source["path"] if isinstance(source, dict) else source
        check((ROOT / path).resolve() == PLUGIN, f"Wrong source: {catalog_path}")

    # Each format uses this same skill tree, not a copied or filtered tree.
    skill_files = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    check({s.parent.name for s in skill_files} == EXPECTED, "Wrong six skill folders")
    for skill in skill_files:
        text = skill.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        check(len(parts) == 3 and not parts[0].strip(), f"No frontmatter: {skill}")
        name = re.search(r"^name: (.+)$", parts[1], re.M)
        desc = re.search(r"^description: (.+)$", parts[1], re.M)
        check(name and name[1] == skill.parent.name and desc,
              f"Bad skill metadata: {skill}")
        check("../../references/common-standard.md" in text,
              f"Missing shared standard: {skill}")
        for relative in re.findall(r"`(\.\./[^`]+)`", text):
            target = (skill.parent / relative).resolve()
            check(target.is_relative_to(PLUGIN) and target.is_file(),
                  f"Missing or external file: {skill}: {relative}")
            target.read_text(encoding="utf-8")
        print(f"PASS shared skill and files: {skill.parent.name}")

    for relative in ("references/master-schema.json", "examples/illustrative-master.json"):
        read_json(PLUGIN / relative)
    subprocess.run([sys.executable, str(PLUGIN / "scripts/validate_master.py"),
                    str(PLUGIN / "examples/illustrative-master.json")], check=True)
    print("PASS package metadata, both catalogs, six skills and shared files")
    print("This script does not test host installation or skill loading; see VERIFICATION.md")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        sys.exit(f"FAIL: {error}")
