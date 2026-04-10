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


def read_latest_csv(path):
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
                results[test] = p == n
            except (ValueError, AttributeError):
                results[test] = None
        return results


def status_str(passed):
    if passed is None:
        return "-"
    return "pass" if passed else "no pass"


lines = ["# IRONCLAD - CI Summary", ""]

for suite in SUITES:
    # Collect results for each architecture
    arch_results = {}
    for arch in ARCHS:
        csv_path = os.path.join(args.results_root, arch, suite, "latest.csv")
        arch_results[arch] = read_latest_csv(csv_path)

    # Union of all test names across architectures
    all_tests = sorted(set(arch_results["krackan"]) | set(arch_results["phoenix"]))

    lines += [
        f"## {suite.capitalize()}",
        "",
        "| Test | Krackan | Phoenix |",
        "|---|---|---|",
    ]
    if not all_tests:
        lines.append("| (no data) | - | - |")
    for test in all_tests:
        krackan = status_str(arch_results["krackan"].get(test))
        phoenix = status_str(arch_results["phoenix"].get(test))
        lines.append(f"| {test} | {krackan} | {phoenix} |")
    lines.append("")

output_path = os.path.join(args.results_root, args.output)
with open(output_path, "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"Written: {output_path}")
