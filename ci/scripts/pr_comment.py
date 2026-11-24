# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Build the pull request comment from this run's results.

A pull request from a fork controls everything its own jobs produce, and the
job that posts the comment holds a write token. So this reads one file per
suite, ``latest.csv``, treats it as data alone, and renders the report with the
code in this checkout. It compares against ``all.csv`` on the results branch,
which only a push to a trunk branch can write.

Every suite is named in the comment: one that moved no benchmark says so, one
whose workflow is still running is pending, and one that reported nothing is
missing. Without that, a suite that crashed reads the same as a quiet one.
"""

import argparse
import csv
import json
import os
from typing import Dict, List, Tuple

from merge_all import limit_rows_by_date
from pretty_common import ARCHS, PR_SUITES, results_dir, suite_label
from pretty_trends import (
    DATE_FMT,
    SIGMA,
    THRESHOLD,
    build_report,
    cell,
    gate,
    parse_date,
)

# The posting step matches this to update its own comment.
MARKER = "<!-- iron-ci-aggregate -->"

# A run reports a few hundred rows. A fork could upload millions.
MAX_ROWS = 20000


def read_csv(path: str) -> Tuple[List[Dict[str, str]], List[str]]:
    if not os.path.exists(path):
        return [], []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            if len(rows) >= MAX_ROWS:
                break
            # csv puts the overflow of a ragged row under None. Drop it: every
            # consumer addresses columns by name.
            row.pop(None, None)
            rows.append({k: v for k, v in row.items() if k is not None})
        return rows, [c for c in (reader.fieldnames or []) if c]


def read_status(path: str) -> Dict[str, str]:
    """Read what the collecting step found for each suite."""
    try:
        with open(path) as f:
            status = json.load(f)
    except (OSError, ValueError):
        return {}
    return (
        {str(k): str(v) for k, v in status.items()} if isinstance(status, dict) else {}
    )


def suite_report(
    artifacts: str, history: str, directory: str, suite: str, args
) -> Tuple[str, str]:
    """Render one suite against the results branch: the body and the run it compares with.

    The body is empty when no benchmark moved; the run is its commit and date,
    or empty when the results branch holds none of this suite.
    """
    latest, latest_columns = read_csv(os.path.join(artifacts, directory, "latest.csv"))
    previous, previous_columns = read_csv(os.path.join(history, directory, "all.csv"))

    dated = [(parse_date(row, DATE_FMT), row) for row in previous]
    dated = [(date, row) for date, row in dated if date is not None]
    baseline = ""
    if dated:
        date, row = max(dated, key=lambda pair: pair[0])
        baseline = f"{cell((row.get('Commit') or '')[:7])} ({date:%Y-%m-%d %H:%M})"
    if not latest:
        return "", baseline

    columns = list(dict.fromkeys(previous_columns + latest_columns))
    rows = limit_rows_by_date(previous + latest, 2)
    lines = build_report(
        rows,
        columns,
        threshold=args.threshold,
        sigma=args.sigma,
        ndigits=args.ndigits,
        history=args.performance_checks_page,
        suite=suite,
    )
    body = "\n".join(line for line in lines if not line.startswith("# ")).strip()
    return ("" if body.startswith("No benchmark moved") else body), baseline


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--artifacts", required=True, help="Root of this run's downloaded artifacts"
    )
    parser.add_argument(
        "--history", required=True, help="Checkout of the results branch"
    )
    parser.add_argument(
        "--status", default="", help="JSON of suite -> workflow conclusion"
    )
    parser.add_argument("--commit", default="")
    parser.add_argument("--date", default="")
    parser.add_argument("--commit-url", default="")
    parser.add_argument("--threshold", type=float, default=THRESHOLD)
    parser.add_argument("--sigma", type=float, default=SIGMA)
    parser.add_argument("--round", type=int, default=2, dest="ndigits")
    parser.add_argument(
        "--performance-checks-page",
        default="",
        help="The website's Performance Checks page, which each moved benchmark links to",
    )
    parser.add_argument("-o", "--output", default="comment.md")
    args = parser.parse_args()

    status = read_status(args.status) if args.status else {}

    commit = (
        f"[`{args.commit}`]({args.commit_url})"
        if args.commit_url
        else f"`{args.commit}`"
    )
    lines = [MARKER, "## CI performance trends", "", f"{commit} ({args.date})", ""]

    sections = []
    pending = []
    missing = []
    for arch in ARCHS:
        for suite in PR_SUITES:
            directory = results_dir(arch, suite)
            label = suite_label(arch, suite)
            conclusion = status.get(directory, "missing")
            if conclusion == "pending":
                pending.append(label)
                continue
            if conclusion != "success" or not os.path.exists(
                os.path.join(args.artifacts, directory, "latest.csv")
            ):
                missing.append(f"{label} ({conclusion})")
                continue
            body, baseline = suite_report(
                args.artifacts, args.history, directory, suite, args
            )
            against = (
                f"Previous: {baseline}, this suite's newest run on the results branch."
                if baseline
                else "Previous: none, the results branch holds no run of this suite."
            )
            if body:
                sections += [
                    "<details open>",
                    f"<summary><b>{label}</b></summary>",
                    "",
                    against,
                    "",
                    body,
                    "",
                    "</details>",
                    "",
                ]
            else:
                sections += [
                    f"**{label}**: no benchmark moved by {args.threshold:g}%"
                    f"{gate(args.sigma)}. {against}",
                    "",
                ]

    lines += sections

    if pending:
        lines += [
            f"⏳ Still running: {', '.join(pending)}. "
            "This comment updates when each finishes.",
            "",
        ]
    if missing:
        lines += [
            f"⚠️ No results from: {', '.join(missing)}. "
            "This comment covers the remaining suites only.",
            "",
        ]

    if args.performance_checks_page:
        lines += [
            f"Every benchmark's history: [Performance Checks]({args.performance_checks_page}).",
            "",
        ]

    with open(args.output, "w") as f:
        f.write("\n".join(lines))
    print(f"Written: {args.output}")


if __name__ == "__main__":
    main()
