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

# The results branch stores one directory per architecture and suite. The
# workflow that benchmarks each one names its artifact after the pair.
ARCHS = ["krackan", "phoenix"]
SUITES = ["small", "extensive", "examples"]

# What each suite holds, for a reader of the report.
SUITE_LABELS = {
    "small": "Operators",
    "extensive": "Operators, extensive",
    "examples": "Applications",
}

# A pull request runs the default and the example suites. The extensive suite
# runs on a push to a trunk branch, so no pull request reports it.
PR_SUITES = ["small", "examples"]


def results_dir(arch: str, suite: str) -> str:
    """Name the results branch directory holding one suite's CSVs."""
    return f"{arch}/{suite}"


def suite_label(arch: str, suite: str) -> str:
    """Name a suite for a reader."""
    return f"{arch.capitalize()} - {SUITE_LABELS.get(suite, suite)}"


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


EMBEDDING_GEMMA2 = "tests/applications/embedding_gemma2/test.py::"
# The towers' tests that moved into a class of EmbeddingGemma 2's one test.py.
TOWER_CLASSES = {
    "audio": (
        "TestAudio",
        ("test_audio_features", "test_audio_accuracy", "test_audio_latency"),
    ),
    "vision": (
        "TestVision",
        (
            "test_image_processor",
            "test_image_processor_npu2_only",
            "test_vision_accuracy",
            "test_vision_latency",
        ),
    ),
}

LM_HEAD = "iron/operators/flm/lm_head/test.py::"
LLAMA = "tests/applications/llama/test.py::"
QWEN3 = "tests/applications/qwen3/test.py::"
# The module that runs every operator declaring its cases. Its parametrize ids
# lead with the operator: 'GEMV-cols_4-...'.
CATALOG_TEST_FILE = "iron/tests/operators/catalog.py"
CATALOG = f"{CATALOG_TEST_FILE}::test_operator"
# The prompt lengths and token counts a decoder application benches.
PROMPTS = [(p, n) for p in (1024, 13) for n in (40, 1)]

# Test paths renamed since the results branch began, each old prefix straight
# to the newest: row_key maps a path by the first prefix it starts with, so
# a test's own entry goes before its directory's, and no entry chains.
RENAMED_PATHS = {
    **{
        f"iron/applications/{old}/{tower}/test.py::{test}": f"{EMBEDDING_GEMMA2}{cls}::{test}"
        for old in ("embeddinggemma_2", "embeddinggemma2", "embedding_gemma2")
        for tower, (cls, tests) in TOWER_CLASSES.items()
        for test in tests
    },
    **{
        f"iron/applications/{old}/{tower}/test.py::": EMBEDDING_GEMMA2
        for old in ("embeddinggemma_2", "embeddinggemma2", "embedding_gemma2")
        for tower in TOWER_CLASSES
    },
    "iron/applications/embeddinggemma_2/": "tests/applications/embedding_gemma2/",
    "iron/applications/embeddinggemma2/": "tests/applications/embedding_gemma2/",
    "iron/applications/embedding_gemma2/": "tests/applications/embedding_gemma2/",
    "iron/applications/llama_3.2_1b/": "tests/applications/llama/",
    "iron/applications/llama3/": "tests/applications/llama/",
    "iron/applications/llama/": "tests/applications/llama/",
    "iron/applications/gemma4_flm/": "tests/applications/gemma4_flm/",
    "iron/applications/qwen3/": "tests/applications/qwen3/",
    **{
        f"iron/operators/{block}/test.py::": f"iron/tests/lm/{block}.py::"
        for block in (
            "concat_channels",
            "conv1d",
            "conv2d",
            "image_patches",
            "log_mel",
            "max_pool2d",
            "swiglu",
        )
    },
}

# Parametrizations renamed since the results branch began, by their key after
# RENAMED_PATHS:
# - flm's LMHead whole-vocabulary bench became a case of its softcap test over
#   (dim, vocab);
# - a decoder application's tests became one per family, its size the first id
#   (Llama 3.2 1B, Qwen3 1.7B);
# - Merge's placeholders became one parameter;
# - RoPE's method_type=0 became the default two_halves=True.
RENAMED_TESTS = {
    **{
        (f"{LM_HEAD}test_gemma4_vocabulary", f"dim_{dim}"): (
            f"{LM_HEAD}test_gemma4_softcap",
            f"dim_{dim}-vocab_262144",
        )
        for dim in (1536, 2560)
    },
    **{
        (f"{path}{test}{old}", f"{old_id}_prompt_{p}_tokens_{n}"): (
            f"{path}{test}{new}",
            f"{size}-prompt_{p}_tokens_{n}",
        )
        for path, test, old, new, old_id, size in (
            (LLAMA, "test_llama_3_2", "_1b", "", "llama_3.2_1b", "llama_3.2_1b"),
            (
                LLAMA,
                "TestEachStep::test_llama_3_2",
                "_1b_each_step",
                "_each_step",
                "llama_3.2_1b",
                "llama_3.2_1b",
            ),
            (QWEN3, "test_qwen3", "_1_7b", "", "qwen3_1_7b", "qwen3_1.7b"),
        )
        for p, n in PROMPTS
    },
    (f"{LLAMA}test_llama_3_2_1b_device_loop", "test_llama_3_2_1b_device_loop"): (
        f"{LLAMA}test_llama_3_2_device_loop",
        "llama_3.2_1b",
    ),
    (f"{QWEN3}test_qwen3_1_7b_device_loop", "test_qwen3_1_7b_device_loop"): (
        f"{QWEN3}test_qwen3_device_loop",
        "qwen3_1.7b",
    ),
    (
        CATALOG,
        "Merge-rows_2048-audio_token_258881-image_token_258880-audio_at_2048-"
        "vision_at_2560",
    ): (CATALOG, "Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))"),
    (CATALOG, "RoPE-rows_4096-cols_512-angle_rows_8-method_type_0"): (
        CATALOG,
        "RoPE-rows_4096-cols_512-angle_rows_8",
    ),
}


def operator_name(test_path: str, test_name: str = "") -> str:
    """Name the operator a row of 'Test Path' and 'Test' belongs to.

    'iron/operators/flm/gemm/test.py::test_gemm' names 'flm/gemm', and
    'tests/applications/llama/test.py::test_llama' names 'llama'. A
    catalog row is named by its test's leading id:
    'iron/tests/operators/catalog.py::test_operator' with test
    'GEMV-cols_4' names 'GEMV'. Any other test is named by its module.
    """
    file_part = test_path.split("::", 1)[0]
    if file_part == CATALOG_TEST_FILE:
        return test_name.split("-", 1)[0] or UNKNOWN_OPERATOR
    directory, _ = split_test_path(test_path)
    for prefix in ("iron/operators/", "tests/applications/"):
        if directory.startswith(prefix):
            return directory[len(prefix) :] or UNKNOWN_OPERATOR
    stem = os.path.splitext(os.path.basename(file_part))[0]
    return stem or UNKNOWN_OPERATOR


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
    """Identify the parametrization a row measures, by its test's path and id
    now: a row recorded under a renamed path or parametrization continues its
    history.
    """
    test_path = (row.get("Test Path") or "").strip()
    for old, new in RENAMED_PATHS.items():
        if test_path.startswith(old):
            test_path = new + test_path[len(old) :]
            break
    key = (test_path, (row.get("Test") or "").strip())
    return RENAMED_TESTS.get(key, key)


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
