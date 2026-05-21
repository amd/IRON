#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import csv

from pretty_common import display_name, parse_checks, split_test_path, status_emoji

parser = argparse.ArgumentParser(
    description="Turn CSV of CI results into markdown document"
)
parser.add_argument("csv", help="CSV results file")
parser.add_argument("-o", "--output", default="readme.md")
parser.add_argument("--date", required=True)
parser.add_argument("--commit", required=True)
parser.add_argument("--metric", default=[], action="append")
args = parser.parse_args()


with open(args.csv, "r") as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader]


# Group rows by their test directory. Within each group, collect (display_name, row).
groups = {}
for row in rows:
    test_path = row.get("Test Path", "") or ""
    test_name = row.get("Test", "")
    directory, func = split_test_path(test_path)
    display = display_name(func, test_name, fallback=test_path or "?")
    # Fallback group name when Test Path is missing.
    if not directory:
        directory = "(unknown)"
    groups.setdefault(directory, []).append((display, row))


def print_test(test_name, test):
    passed, n_checks = parse_checks(test.get("Checks", ""))
    status = status_emoji(passed, n_checks, partial=True)
    metric_cells = "".join(
        f"""<td>{f"{float(test[metric]):.2f}" if test.get(metric) not in (None, "", "n/a") else "n/a"}</td>"""
        for metric in args.metric
    )
    return f"""
        <tr><td>{test_name}</td><td>{status} {passed}/{n_checks}</td>{metric_cells}</tr>"""


def render_group(directory, entries):
    header = "".join(f"<td>{metric}</td>" for metric in args.metric)
    body = "".join(print_test(display, row) for display, row in entries)
    return f"""
<details>
<summary>{directory}</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td>{header}</tr>
    </thead>
    <tbody>{body}
    </tbody>
</table>

</details>
"""


sections = "".join(
    render_group(directory, sorted(groups[directory], key=lambda x: x[0]))
    for directory in sorted(groups.keys())
)

out = f"""
# IRON

Tested on `{args.date}` at commit `{args.commit}`.
{sections}
"""

with open(args.output, "w") as f:
    f.write(out)
