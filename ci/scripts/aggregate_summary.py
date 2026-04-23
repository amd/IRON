#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Aggregate CI results from Krackan and Phoenix subdirectories into a top-level summary."""

import argparse
import csv
import os

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
    """Return a dict mapping test name -> {checks, passed, metrics}."""
    if not os.path.exists(path):
        return {}
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        results = {}
        for row in reader:
            test = row.get("Test", "")
            checks = row.get("Checks", "")
            try:
                p, n = map(int, checks.split("/"))
                passed = p == n
            except (ValueError, AttributeError):
                passed = None

            metrics = {}
            for m in METRIC_PREFERENCE:
                val = row.get(m, "")
                if val:
                    metrics[m] = val

            results[test] = {"passed": passed, "metrics": metrics}
        return results


def status_str(entry):
    if entry is None:
        return "-"
    if entry["passed"] is None:
        return "-"
    return "pass" if entry["passed"] else "**FAIL**"


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
    """Pick the metric column name present in most entries."""
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

    all_tests = sorted(set(arch_results["krackan"]) | set(arch_results["phoenix"]))

    # Skip suite entirely when there is no data
    if not all_tests:
        continue

    # Determine metric labels per arch
    k_metric = metric_label(arch_results["krackan"])
    p_metric = metric_label(arch_results["phoenix"])

    # Build header with merged arch columns
    k_metric_hdr = f" {k_metric}" if k_metric else ""
    p_metric_hdr = f" {p_metric}" if p_metric else ""

    lines += [
        f"## {suite.capitalize()}",
        "",
        f"| Test | Krackan Status | Krackan{k_metric_hdr} | Phoenix Status | Phoenix{p_metric_hdr} |",
        "|---|---|---|---|---|",
    ]
    for test in all_tests:
        k = arch_results["krackan"].get(test)
        p = arch_results["phoenix"].get(test)
        lines.append(
            f"| {test} | {status_str(k)} | {metric_str(k)} | {status_str(p)} | {metric_str(p)} |"
        )
    lines.append("")

output_path = args.output
with open(output_path, "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"Written: {output_path}")
