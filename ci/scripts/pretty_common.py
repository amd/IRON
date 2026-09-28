#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Shared helpers for the pretty_* CI report scripts."""

import os
from typing import Any, Dict, Iterable, List, Optional, Tuple

# Columns that identify a row rather than measure it.
NON_METRIC_COLUMNS = {"Commit", "Date", "Test Path", "Test", "Checks", "Bench"}

# Every metric is written out as mean, median, min, max and stddev. Reports and
# charts track the mean.
MEAN_SUFFIX = " (mean)"

# Rows written before the 'Test Path' column existed name no operator.
UNKNOWN_OPERATOR = "(unknown)"


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


def operator_name(test_path: str) -> str:
    """Name the operator a 'Test Path' belongs to.

    'iron/operators/flm/gemm/test.py::test_gemm' names 'flm/gemm', and
    'iron/applications/llama_3.2_1b/test.py::test_llama' names 'llama_3.2_1b'.
    """
    directory, _ = split_test_path(test_path)
    for prefix in ("iron/operators/", "iron/applications/"):
        if directory.startswith(prefix):
            return directory[len(prefix) :] or UNKNOWN_OPERATOR
    return UNKNOWN_OPERATOR


def try_parse_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    text = str(value).strip()
    if text == "" or text.lower() in {"n/a", "na", "none"}:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def row_key(row: Dict[str, str]) -> Tuple[str, str]:
    """Identify the parametrization a row measures."""
    return ((row.get("Test Path") or "").strip(), (row.get("Test") or "").strip())


def select_bench_rows(rows: Iterable[Dict[str, str]]) -> List[Dict[str, str]]:
    """Keep the rows of the parametrizations that carry the 'bench' marker.

    A parametrization qualifies when any one of its rows says so, which gives a
    benched parametrization the history it accumulated before the column
    existed.
    """
    rows = list(rows)
    benched = {
        row_key(row)
        for row in rows
        if (row.get("Bench") or "").strip().lower() == "yes"
    }
    return [row for row in rows if row_key(row) in benched]


def metric_label(column: str) -> Optional[str]:
    """Name the metric a column tracks, or None if the column tracks none."""
    if column in NON_METRIC_COLUMNS or not column.endswith(MEAN_SUFFIX):
        return None
    return column[: -len(MEAN_SUFFIX)]


def tracked_metrics(
    rows: Iterable[Dict[str, str]], field_order: Iterable[str]
) -> List[Tuple[str, str]]:
    """List the (column, metric) pairs holding a number for one of `rows`."""
    rows = list(rows)
    pairs = ((column, metric_label(column)) for column in field_order)
    return [
        (column, metric)
        for column, metric in pairs
        if metric is not None
        and any(try_parse_float(row.get(column)) is not None for row in rows)
    ]
