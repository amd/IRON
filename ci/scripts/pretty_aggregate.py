#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Aggregate CI results from Krackan and Phoenix subdirectories into a top-level summary."""

import argparse
import csv
import os

from pretty_common import display_name, parse_checks, split_test_path, status_emoji

parser = argparse.ArgumentParser(
    description="Aggregate CI results from all architecture subdirectories into a top-level readme.md"
)
parser.add_argument(
    "--results-root",
    default=".",
    help="Root directory of the ci branch worktree (default: current directory)",
)
parser.add_argument(
    "-o",
    "--output",
    default="readme.md",
    help="Output markdown file (default: readme.md)",
)
args = parser.parse_args()

SUITES = ["examples", "small", "extensive"]
ARCHS = ["krackan", "phoenix"]

# Benchmark metric columns to include (in order).  For each architecture we
# show the first metric column that exists in the CSV.
METRIC_PREFERENCE = [
    "Latency (mean)",
    "Bandwidth (mean)",
    "Throughput (mean)",
]


def read_latest_csv(path):
    """Return a dict mapping (directory, display_name) -> {checks, passed, metrics}."""
    if not os.path.exists(path):
        return {}
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        results = {}
        for row in reader:
            test_path = row.get("Test Path", "") or ""
            params = row.get("Test", "") or ""
            directory, func = split_test_path(test_path)
            if not directory:
                directory = "(unknown)"
            display = display_name(func, params, fallback=test_path or "?")

            p, n = parse_checks(row.get("Checks", ""))
            passed = (p == n) if n > 0 else None

            metrics = {}
            for m in METRIC_PREFERENCE:
                val = row.get(m, "")
                if val:
                    metrics[m] = val

            results[(directory, display)] = {"passed": passed, "metrics": metrics}
        return results


def status_str(entry):
    if entry is None or entry["passed"] is None:
        return "-"
    return "✅" if entry["passed"] else "❌"


def metric_str(entry):
    """Return the first available metric value, or '-'."""
    if entry is None:
        return "-"
    for m in METRIC_PREFERENCE:
        val = entry["metrics"].get(m, "")
        if val:
            try:
                return f"{float(val):.2f}"
            except ValueError:
                return val
    return "-"


def metric_label(arch_results):
    """Pick the first metric column name present in any entry."""
    for m in METRIC_PREFERENCE:
        for entry in arch_results.values():
            if entry["metrics"].get(m):
                return m
    return ""


lines = ["# IRON - CI Summary", ""]

for suite in SUITES:
    arch_results = {}
    for arch in ARCHS:
        csv_path = os.path.join(args.results_root, arch, suite, "latest.csv")
        arch_results[arch] = read_latest_csv(csv_path)

    all_keys = set(arch_results["krackan"]) | set(arch_results["phoenix"])

    # Skip suite entirely when there is no data
    if not all_keys:
        continue

    # Group keys by directory
    by_dir = {}
    for directory, display in all_keys:
        by_dir.setdefault(directory, []).append(display)

    # Determine metric labels per arch
    k_metric = metric_label(arch_results["krackan"])
    p_metric = metric_label(arch_results["phoenix"])
    k_metric_hdr = f" {k_metric}" if k_metric else ""
    p_metric_hdr = f" {p_metric}" if p_metric else ""

    lines += [f"## {suite.capitalize()}", ""]

    for directory in sorted(by_dir.keys()):
        lines += [
            "<details>",
            f"<summary>{directory}</summary>",
            "",
            f"| Test | Krackan Status | Krackan{k_metric_hdr} | Phoenix Status | Phoenix{p_metric_hdr} |",
            "|---|---|---|---|---|",
        ]
        for display in sorted(by_dir[directory]):
            k = arch_results["krackan"].get((directory, display))
            p = arch_results["phoenix"].get((directory, display))
            lines.append(
                f"| {display} | {status_str(k)} | {metric_str(k)} | {status_str(p)} | {metric_str(p)} |"
            )
        lines += ["", "</details>", ""]

output_path = args.output
with open(output_path, "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"Written: {output_path}")
