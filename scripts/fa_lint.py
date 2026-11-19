#!/usr/bin/env python3
"""Lint Persian prose for common document errors.

Usage:
    python scripts/fa_lint.py FILE [FILE ...]
    python scripts/fa_lint.py --stdin

Checks: Arabic glyphs, double ZWNJ, missing ZWNJ in common compounds,
mixed Persian/ASCII digits, replacement characters. Exit 1 on errors.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ZWNJ = "\u200c"
ARABIC_GLYPHS = "ىكؤة"
HAMZA = "أ"
INVERTED_HAMZA = "إ"
ALLOWED_HAMZA = re.compile(r"(?:تأخیر|سؤال|مسئله|مسائل|أسئلة)")
COMPOUNDS = (
    (re.compile(r"\bمی\s+شود\b"), "می‌شود"),
    (re.compile(r"\bنیمه\s+ساختاریافته\b"), "نیمه‌ساختاریافته"),
    (re.compile(r"\bکلان\s+داده\b"), "کلان‌داده"),
    (re.compile(r"\bداده\s+های\b"), "داده‌های"),
)
MIXED_DIGITS = re.compile(r"(?:[\u06f0-\u06f9]\d|\d[\u06f0-\u06f9])")
REPLACEMENT = "\ufffd"


def lint_line(line: str, line_no: int) -> tuple[list[dict], list[dict]]:
    errors: list[dict] = []
    warnings: list[dict] = []

    for m in re.finditer(f"[{ARABIC_GLYPHS}]", line):
        errors.append({"line": line_no, "column": m.start() + 1, "type": "arabic-glyph", "text": m.group()})

    for m in re.finditer(INVERTED_HAMZA, line):
        errors.append({"line": line_no, "column": m.start() + 1, "type": "inverted-hamza", "text": m.group()})

    for m in re.finditer(HAMZA, line):
        if not ALLOWED_HAMZA.search(line):
            warnings.append({"line": line_no, "column": m.start() + 1, "type": "hamza-check", "text": m.group()})

    for m in re.finditer(ZWNJ + "{2,}", line):
        errors.append({"line": line_no, "column": m.start() + 1, "type": "double-zwnj", "text": m.group()})

    for pattern, fix in COMPOUNDS:
        for m in pattern.finditer(line):
            errors.append({"line": line_no, "column": m.start() + 1, "type": "missing-zwnj", "text": m.group(), "fix": fix})

    for m in MIXED_DIGITS.finditer(line):
        errors.append({"line": line_no, "column": m.start() + 1, "type": "mixed-digits", "text": m.group()})

    if REPLACEMENT in line:
        errors.append({"line": line_no, "column": line.index(REPLACEMENT) + 1, "type": "replacement-char", "text": REPLACEMENT})

    return errors, warnings


def lint_text(text: str) -> dict:
    errors: list[dict] = []
    warnings: list[dict] = []
    in_fence = False
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line_errors, line_warnings = lint_line(line, line_no)
        errors.extend(line_errors)
        warnings.extend(line_warnings)
    return {"errors": errors, "warnings": warnings}


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0 if argv else 2

    if argv[0] == "--stdin":
        result = lint_text(sys.stdin.read())
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if result["errors"] else 0

    total_errors = 0
    total_warnings = 0
    for name in argv:
        path = Path(name)
        if not path.exists():
            print(json.dumps({"file": name, "error": "not-found"}, ensure_ascii=False))
            return 2
        result = lint_text(path.read_text(encoding="utf-8"))
        result["file"] = name
        print(json.dumps(result, ensure_ascii=False, indent=2))
        total_errors += len(result["errors"])
        total_warnings += len(result["warnings"])
    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
