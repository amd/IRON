#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import csv
import os
from datetime import datetime, timedelta

from pretty_common import row_key, select_bench_rows

# The retention mlir-aie keeps its kernel checks' history to.
KEEP_DAYS = 90
MAX_RUNS = 400


def prune(rows, date_fmt="%Y-%m-%d %H:%M:%S"):
    """Keep the runs the reports and the Benchmarks page read.

    A run is the rows of one date. Each benched parametrization keeps its own
    runs of the last `KEEP_DAYS` before the suite's newest, its newest run of
    each ISO week before that, and at most `MAX_RUNS` runs: a week another
    test ran later in keeps this one's run too. The trends compare a run with
    the one before it, so every other row keeps the suite's last two runs.
    Measured from the newest run, a skewed clock on one runner cannot empty
    the file.
    """
    dated = []
    for row in rows:
        try:
            dated.append((datetime.strptime(row.get("Date", ""), date_fmt), row))
        except (ValueError, TypeError):
            continue
    runs = sorted({date for date, _ in dated})
    if not runs:
        return []
    cutoff = runs[-1] - timedelta(days=KEEP_DAYS)
    last_two = set(runs[-2:])

    benched = {row_key(row) for row in select_bench_rows(rows)}
    runs_of = {}
    for date, row in dated:
        if row_key(row) in benched:
            runs_of.setdefault(row_key(row), set()).add(date)
    kept = {}
    for key, dates in runs_of.items():
        weekly = {}
        for date in sorted(dates):
            if date < cutoff:
                weekly[date.isocalendar()[:2]] = date
        recent = {date for date in dates if date >= cutoff}
        kept[key] = set(sorted(recent | set(weekly.values()))[-MAX_RUNS:])

    return [
        row
        for date, row in dated
        if date in last_two or date in kept.get(row_key(row), ())
    ]


def limit_rows_by_date(rows, limit, date_fmt="%Y-%m-%d %H:%M:%S"):
    """Limit rows to the N most recent dates for each test."""
    if not limit or not rows:
        return rows

    # Operators share parametrization names, so the key carries the test path.
    test_groups = {}
    for row in rows:
        test_groups.setdefault(row_key(row), []).append(row)

    # For each test, sort by date and keep only the latest N entries
    limited_rows = []
    for test_rows in test_groups.values():
        # Sort by date (assuming date format is sortable as string, e.g., YYYY-MM-DD)
        try:
            test_rows.sort(
                key=lambda r: datetime.strptime(
                    r.get("Date", ""), date_fmt
                ).timestamp(),
                reverse=True,
            )
        except (ValueError, TypeError):
            # Fallback to string sorting if date parsing fails
            test_rows.sort(key=lambda x: x.get("Date", ""), reverse=True)

        # Keep only the most recent N entries
        limited_rows.extend(test_rows[:limit])

    return limited_rows


def add_empty_columns(rows, empty_val="n/a"):
    columns = set()
    for row in rows:
        columns.update(row.keys())
    for row in rows:
        for column in columns:
            if column not in row:
                row[column] = empty_val


def write_results(output_rows, path):
    output_rows.sort(key=lambda x: (x["Test"], x["Date"]))
    cols = {}  # we use a dict rather than a set because it guarantees insertion order
    for row in output_rows:
        cols.update({k: None for k in row.keys()})
    with open(path, "w", newline="") as f:
        if output_rows:
            writer = csv.DictWriter(f, cols.keys())
            writer.writeheader()
            writer.writerows(output_rows)


def get_rows(path):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--latest",
        default="latest.csv",
        help="Path to output CSV for this runs results.",
    )
    parser.add_argument(
        "--all",
        default="all.csv",
        help="Path to output CSV of all previous runs to which these runs results will be appended.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit to only the N latest results by date for each test. If not specified, all results are kept.",
    )
    parser.add_argument(
        "--prune",
        action="store_true",
        help=f"Keep a benched test's runs of the last {KEEP_DAYS} days, then its "
        f"newest of each week, at most {MAX_RUNS}; and every other test's last two",
    )
    args = parser.parse_args()

    all_rows = (
        get_rows(args.all) if os.path.exists(args.all) else []
    )  # Ignore empty/non-existant all.csv on first run
    latest_rows = get_rows(args.latest)

    output_rows = all_rows + latest_rows
    add_empty_columns(output_rows)

    if args.prune:
        output_rows = prune(output_rows)

    # Apply limit if specified
    if args.limit:
        output_rows = limit_rows_by_date(output_rows, args.limit)

    write_results(output_rows, args.all)


if __name__ == "__main__":
    main()
