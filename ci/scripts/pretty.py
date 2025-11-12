#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import csv

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

by_test = {}

with open(args.csv, "r") as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader]

by_test = {}

for row in rows:
    test = row["Test"]
    if test not in by_test:
        by_test[test] = {}
    for k in row:
        if k not in by_test[test]:
            by_test[test][k] = []
        val = None
        try:
            val = float(row[k])
        except ValueError:
            val = row[k]
        by_test[test][k].append(val)


def print_test(test_name, test):
    passed, n_checks = 0, 0
    if "Checks" in test:
        passed, n_checks = map(int, test["Checks"][0].split("/"))

    out = f"""
        <tr>
            <td>
                {test_name}
            </td>
            <td>
                {("✅" if passed == n_checks else "❌" if passed == 0 else "🟠")
                 if "Checks" in test and test["Checks"] else "?"}
                {passed}/{n_checks}
            </td>{"".join(f"""
            <td>
                {f"{test[metric][0]:.2f}" if metric in test and isinstance(test[metric][0], float) else "n/a"}
            </td>""" for metric in args.metric)}
        </tr>"""
    return out


out = f"""
# IRONCLAD

Tested on `{args.date}` at commit `{args.commit}`.

<table>
    <thead>
        <tr>
            <td>Test</td>
            <td>Checks</td>
            {"".join(f"<td>{metric}</td>" for metric in args.metric)}
        </tr>
    </thead>
    <tbody>{"".join(print_test(test, by_test[test]) for test in by_test)}
    </tbody>
</table>
"""

with open(args.output, "w") as f:
    f.write(out)
