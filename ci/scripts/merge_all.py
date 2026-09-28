#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse, csv, os
from datetime import datetime, timedelta


def drop_rows_older_than(rows, max_age_days, date_fmt="%Y-%m-%d %H:%M:%S"):
    """Drop rows whose date is more than `max_age_days` behind the newest date.

    A skewed clock on one runner can then not empty the file.
    """
    if not max_age_days or not rows:
        return rows

    def parse(row):
        try:
            return datetime.strptime(row.get("Date", ""), date_fmt)
        except (ValueError, TypeError):
            return None

    dated = [(parse(row), row) for row in rows]
    newest = max((d for d, _ in dated if d is not None), default=None)
    if newest is None:
        return rows

    cutoff = newest - timedelta(days=max_age_days)
    return [row for date, row in dated if date is None or date >= cutoff]


def limit_rows_by_date(rows, limit, date_fmt="%Y-%m-%d %H:%M:%S"):
    """Limit rows to the N most recent dates for each test."""
    if not limit or not rows:
        return rows

    # Operators share parametrization names, so the key carries the test path.
    test_groups = {}
    for row in rows:
        key = (row.get("Test Path", ""), row.get("Test", ""))
        test_groups.setdefault(key, []).append(row)

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
        "--max-age-days",
        type=int,
        default=365,
        help="Drop results older than this many days. Pass 0 to keep every result.",
    )
    args = parser.parse_args()

    all_rows = (
        get_rows(args.all) if os.path.exists(args.all) else []
    )  # Ignore empty/non-existant all.csv on first run
    latest_rows = get_rows(args.latest)

    with open(args.all, "w", newline="") as f:
        output_rows = all_rows + latest_rows
        add_empty_columns(output_rows)

        output_rows = drop_rows_older_than(output_rows, args.max_age_days)

        # Apply limit if specified
        if args.limit:
            output_rows = limit_rows_by_date(output_rows, args.limit)

        write_results(output_rows, args.all)


if __name__ == "__main__":
    main()
