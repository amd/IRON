#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Shared helpers for the pretty_* CI report scripts."""

import os
from typing import Tuple


def split_test_path(test_path: str) -> Tuple[str, str]:
    """Split a 'Test Path' value of the form 'dir/.../test.py::funcname'
    into (directory, funcname). Returns ('', '') style fallbacks if parts
    are missing.
    """
    if "::" in test_path:
        file_part, func = test_path.split("::", 1)
    else:
        file_part, func = test_path, ""
    directory = os.path.dirname(file_part).rstrip("/")
    return directory, func


def display_name(func: str, params: str, fallback: str = "?") -> str:
    """Build a 'funcname[params]' display string with sensible fallbacks."""
    if func and params:
        return f"{func}[{params}]"
    if func:
        return func
    return params or fallback


def parse_checks(checks: str) -> Tuple[int, int]:
    """Parse a 'p/n' checks string into (passed, total). Returns (0, 0) on
    malformed input.
    """
    if not checks:
        return 0, 0
    try:
        p, n = map(int, checks.split("/"))
        return p, n
    except (ValueError, AttributeError):
        return 0, 0


def status_emoji(passed: int, total: int, partial: bool = True) -> str:
    """Render pass/fail status as an emoji.

    - ✅ when all checks pass
    - ❌ when none pass
    - 🟠 when some pass (only if `partial` is True; otherwise ❌)
    - '?' when there are no checks at all
    """
    if total == 0:
        return "?"
    if passed == total:
        return "✅"
    if passed == 0:
        return "❌"
    return "🟠" if partial else "❌"
