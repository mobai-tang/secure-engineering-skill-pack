#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
NAME_LINE = re.compile(r"^name:\s*([a-z0-9-]+)\s*$")
DESCRIPTION_LINE = re.compile(r"^description:\s*(.+)\s*$")


def error(message: str, errors: list[str]) -> None:
    errors.append(message)
    print(f"ERROR: {message}")


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        error(f"{path.relative_to(ROOT)} must start with YAML frontmatter", errors)
        return {}

    try:
        end = lines.index("---", 1)
    except ValueError:
        error(f"{path.relative_to(ROOT)} has no closing frontmatter delimiter", errors)
        return {}

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        name_match = NAME_LINE.match(line)
        description_match = DESCRIPTION_LINE.match(line)
        if name_match:
            fields["name"] = name_match.group(1)
        elif description_match:
            fields["description"] = description_match.group(1)

    if not fields.get("name"):
        error(f"{path.relative_to(ROOT)} is missing a valid name", errors)
    if not fields.get("description"):
        error(f"{path.relative_to(ROOT)} is missing a description", errors)
    return fields


def validate_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for target in MARKDOWN_LINK.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        clean_target = target.split("#", 1)[0]
        if not clean_target:
            continue
        resolved = (path.parent / clean_target).resolve()
        if not resolved.exists():
            error(
                f"{path.relative_to(ROOT)} references missing path {target}",
                errors,
            )


def validate_openai_yaml(path: Path, skill_name: str, errors: list[str]) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "interface:":
        error(f"{path.relative_to(ROOT)} must start with interface:", errors)
        return

    required = ("display_name:", "short_description:", "default_prompt:")
    for field in required:
        if not any(line.startswith(f"  {field}") for line in lines[1:]):
            error(f"{path.relative_to(ROOT)} is missing {field[:-1]}", errors)

    text = "\n".join(lines)
    if f"${skill_name}" not in text:
        error(
            f"{path.relative_to(ROOT)} default prompt must reference ${skill_name}",
            errors,
        )


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())

    if not skill_dirs:
        error("No skill directories found", errors)

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            error(f"{skill_dir.relative_to(ROOT)} is missing SKILL.md", errors)
            continue

        fields = parse_frontmatter(skill_file, errors)
        skill_name = fields.get("name", "")
        if skill_name and skill_name != skill_dir.name:
            error(
                f"{skill_file.relative_to(ROOT)} name {skill_name!r} "
                f"does not match directory {skill_dir.name!r}",
                errors,
            )

        validate_links(skill_file, errors)

        openai_yaml = skill_dir / "agents" / "openai.yaml"
        if openai_yaml.exists():
            validate_openai_yaml(openai_yaml, skill_dir.name, errors)

    for markdown in sorted(ROOT.rglob("*.md")):
        if ".git" not in markdown.parts:
            validate_links(markdown, errors)

    if errors:
        print(f"\nValidation failed with {len(errors)} error(s).")
        return 1

    print(f"Validated {len(skill_dirs)} skills and all local Markdown links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
