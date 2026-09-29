#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Build the pull request comment from this run's results.

A pull request from a fork controls everything its own jobs produce, and the
job that posts the comment holds a write token. So this reads one file per
suite, ``latest.csv``, treats it as data alone, and renders the report with the
code in this checkout. It compares against ``all.csv`` on the results branch,
which only a push to a trunk branch can write.

A suite that reported nothing is named in the comment. Without that, a suite
that crashed reads the same as a suite that moved no benchmark.
"""

import argparse
import csv
import json
import os
from typing import Dict, List, Tuple

from merge_all import limit_rows_by_date
from pretty_common import ARCHS, PR_SUITES, results_dir, suite_label
from pretty_trends import build_report

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


def suite_report(artifacts: str, history: str, directory: str, args) -> List[str]:
    """Render one suite, comparing its run against the results branch."""
    latest, latest_columns = read_csv(os.path.join(artifacts, directory, "latest.csv"))
    if not latest:
        return []
    previous, previous_columns = read_csv(os.path.join(history, directory, "all.csv"))

    columns = list(dict.fromkeys(previous_columns + latest_columns))
    rows = limit_rows_by_date(previous + latest, 2)
    return build_report(
        rows, columns, threshold=args.threshold, sigma=args.sigma, ndigits=args.ndigits
    )


def strip_title(lines: List[str]) -> str:
    """Drop the report's own heading, and report whether anything is left."""
    body = "\n".join(l for l in lines if not l.startswith("# ")).strip()
    return "" if body.startswith("No benchmark moved") else body


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
    parser.add_argument("--threshold", type=float, default=5.0)
    parser.add_argument("--sigma", type=float, default=2.0)
    parser.add_argument("--round", type=int, default=2, dest="ndigits")
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
    reported = []
    missing = []
    for arch in ARCHS:
        for suite in PR_SUITES:
            directory = results_dir(arch, suite)
            label = suite_label(arch, suite)
            body = strip_title(
                suite_report(args.artifacts, args.history, directory, args)
            )
            conclusion = status.get(directory, "missing")
            if conclusion != "success" or not os.path.exists(
                os.path.join(args.artifacts, directory, "latest.csv")
            ):
                missing.append(f"{label} ({conclusion})")
                continue
            reported.append(label)
            if body:
                sections += [
                    "<details open>",
                    f"<summary><b>{label}</b></summary>",
                    "",
                    body,
                    "",
                    "</details>",
                    "",
                ]

    if sections:
        lines += sections
    elif reported:
        lines += ["No benchmark moved past the reporting threshold.", ""]

    if missing:
        lines += [
            f"⚠️ No results from: {', '.join(missing)}. "
            "This comment covers the remaining suites only.",
            "",
        ]

    with open(args.output, "w") as f:
        f.write("\n".join(lines))
    print(f"Written: {args.output}")


if __name__ == "__main__":
    main()
