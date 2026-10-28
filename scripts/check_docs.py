#!/usr/bin/env python3
"""Portable, dependency-free checks for public toolkit text.

This is a first-pass guard, not a substitute for a historical secret scan
or a security-owner review of newly added diagrams/screenshots.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "docs/CHARTER.md", "docs/GOVERNANCE.md",
    "docs/SECURITY.md", "docs/COVERAGE.md",
    "playbooks/internet/README.md",
    "playbooks/website/README.md",
    "playbooks/app-development/README.md",
    "launch/README.md", "launch/CERTIFICATION.md",
    "training/README.md", "templates/README.md",
]
SECRET_PATTERNS = {
    "private key block": re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    "GitHub credential": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Slack credential": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "Stripe secret key": re.compile(r"\bsk_(?:live|test)_[A-Za-z0-9]{20,}\b"),
    "password assignment": re.compile(r"(?im)^\s*(?:password|passwd|api[_-]?key|access[_-]?token)\s*[:=]\s*[^#\s\[][\S]{7,}"),
}
LINK_PATTERN = re.compile(r"\[[^\]\n]+\]\(([^)\n]+)\)")


def main() -> int:
    problems: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            problems.append(f"required file missing: {rel}")
    docs = sorted(ROOT.rglob("*.md"))
    documents = [
        p for p in docs if ".git" not in p.parts
    ]
    for path in documents:
        data = path.read_text(encoding="utf-8")
        relative_name = str(path.relative_to(ROOT))
        if not data.strip().startswith("#"):
            problems.append(f"{relative_name}: no Markdown heading")
        for label, pattern in SECRET_PATTERNS.items():
            # Skip script source itself; scanned docs must not contain real secret patterns.
            if pattern.search(data):
                problems.append(f"{relative_name}: possible {label}")
        for match in LINK_PATTERN.finditer(data):
            href = match.group(1).strip()
            if href.startswith(("https://", "http://", "mailto:", "#")):
                continue
            href = unquote(href.split("#", 1)[0].split("?", 1)[0])
            if not href:
                continue
            target = (path.parent / href).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                problems.append(f"{relative_name}: link escapes repository: {href}")
                continue
            if not target.exists():
                problems.append(f"{relative_name}: broken link: {href}")
    for path in sorted(ROOT.rglob("*.csv")):
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.reader(handle)
            rows = list(reader)
        if not rows or len(rows[0]) < 2:
            problems.append(f"{path.relative_to(ROOT)}: invalid CSV template")
        elif len(set(rows[0])) != len(rows[0]):
            problems.append(f"{path.relative_to(ROOT)}: duplicate CSV header")
        elif any(len(row) != len(rows[0]) for row in rows[1:]):
            problems.append(f"{path.relative_to(ROOT)}: inconsistent CSV columns")
    coverage = (ROOT / "docs/COVERAGE.md").read_text(encoding="utf-8")
    for n in range(1, 11):
        if not re.search(rf"\|\s*{n}\.\s", coverage):
            problems.append(f"coverage crosswalk missing required category {n}")
    if problems:
        print("Toolbox validation FAILED:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print(
        f"Toolkit validation OK: {len(documents)} Markdown files; "
        f"{len(list(ROOT.rglob('*.csv')))} CSV templates; "
        "required guides, links, content categories and high-confidence secret checks passed."
    )
    print("Note: this is not a full security/history/link-availability audit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
