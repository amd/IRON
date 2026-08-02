#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse, csv, os
from datetime import datetime


def limit_rows_by_date(rows, limit, date_fmt="%Y-%m-%d %H:%M:%S"):
    """Limit rows to the N most recent dates for each test."""
    if not limit or not rows:
        return rows

    # Group rows by test name and sort by date
    test_groups = {}
    for row in rows:
        test_name = row.get("Test", "")
        if test_name not in test_groups:
            test_groups[test_name] = []
        test_groups[test_name].append(row)

    # For each test, sort by date and keep only the latest N entries
    limited_rows = []
    for test_name, test_rows in test_groups.items():
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
    args = parser.parse_args()

    all_rows = (
        get_rows(args.all) if os.path.exists(args.all) else []
    )  # Ignore empty/non-existant all.csv on first run
    latest_rows = get_rows(args.latest)

    with open(args.all, "w", newline="") as f:
        output_rows = all_rows + latest_rows
        add_empty_columns(output_rows)

        # Apply limit if specified
        if args.limit:
            output_rows = limit_rows_by_date(output_rows, args.limit)

        write_results(output_rows, args.all)


if __name__ == "__main__":
    main()
