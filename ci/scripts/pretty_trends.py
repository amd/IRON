#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: Apache-2.0

"""Report the performance changes a run introduced, as markdown.

Reads a CSV holding the last two runs of each test. Reports the operators the
run added or dropped, and the benched parametrizations whose measurements
moved. A parametrization without the 'bench' marker runs inputs too small to
measure, so this leaves it out.

A percentage gate on its own reports mostly noise. Over one 5-month window of
the results branch, 633 of 1179 consecutive benched Latency pairs moved by 5%
or more, and 17 of those also moved past the spread the runs measured. A change
therefore has to clear both gates.
"""

import argparse
import csv
import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from pretty_common import (
    MEAN_SUFFIX,
    UNKNOWN_OPERATOR,
    operator_name,
    row_key,
    select_bench_rows,
    tracked_metrics,
    try_parse_float,
)

# Metrics that measure work per unit time; every other metric measures time.
HIGHER_IS_BETTER = ("Bandwidth", "Throughput", "TPS")

DATE_FMT = "%Y-%m-%d %H:%M:%S"

# Test names reach a pull request comment. A pull request from a fork chooses
# them, so they are cut to length and stripped of the characters that would end
# the code span or the table cell holding them.
CELL_LIMIT = 160


def cell(value: str) -> str:
    """Render an untrusted value as a markdown table cell."""
    text = re.sub(r"[`|\r\n]", " ", str(value)).strip()
    if len(text) > CELL_LIMIT:
        text = text[: CELL_LIMIT - 1] + "\u2026"
    return f"`{text}`" if text else "`?`"


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "csv", nargs="?", default="all.csv", help="Input CSV (default: all.csv)"
    )
    p.add_argument("-o", "--output", default="trends.md", help="Output markdown file")
    p.add_argument(
        "--threshold",
        type=float,
        default=5.0,
        help="Report a metric once it moves this many percent (default: 5.0)",
    )
    p.add_argument(
        "--sigma",
        type=float,
        default=2.0,
        help="Also require the move to exceed this many standard deviations of "
        "the spread a run measured. Pass 0 to report on the percentage alone. "
        "(default: 2.0)",
    )
    p.add_argument(
        "--round",
        type=int,
        default=2,
        dest="ndigits",
        help="Decimal places for values and percentages (default: 2)",
    )
    p.add_argument("--date-fmt", default=DATE_FMT)
    return p.parse_args()


def parse_date(row: Dict[str, str], date_fmt: str) -> Optional[datetime]:
    try:
        return datetime.strptime((row.get("Date") or "").strip(), date_fmt)
    except (ValueError, TypeError):
        return None


def delta_pct(curr: Optional[float], prev: Optional[float]) -> Optional[float]:
    if curr is None or prev is None or prev == 0:
        return None
    return (curr - prev) / prev * 100.0


def verdict(metric: str, pct: float) -> str:
    improved = pct > 0 if metric.startswith(HIGHER_IS_BETTER) else pct < 0
    return "🟢" if improved else "🔴"


def within_spread(curr, prev, metric, sigma):
    """Report whether the move sits inside the spread the two runs measured.

    Each run repeats its test and records the standard deviation of the repeats.
    A move smaller than that spread says nothing about the code. A run that
    records no spread cannot answer, so it suppresses nothing.
    """
    if not sigma:
        return False
    deviations = [
        try_parse_float(row.get(f"{metric} (stddev)")) for row in (curr, prev)
    ]
    deviations = [d for d in deviations if d is not None]
    if not deviations:
        return False
    curr_v = try_parse_float(curr.get(f"{metric}{MEAN_SUFFIX}"))
    prev_v = try_parse_float(prev.get(f"{metric}{MEAN_SUFFIX}"))
    if curr_v is None or prev_v is None:
        return False
    return abs(curr_v - prev_v) < sigma * max(deviations)


def write(path: str, lines: List[str]):
    with open(path, "w", newline="") as f:
        f.write("\n".join(lines) + "\n")


def gate(sigma: float) -> str:
    """Name the second gate, for the sentence that introduces the table."""
    if not sigma:
        return ""
    return f" and by more than {sigma:g}x the spread the runs measured"


def build_report(
    all_rows: List[Dict[str, str]],
    field_order: List[str],
    threshold: float = 5.0,
    sigma: float = 2.0,
    ndigits: int = 2,
    date_fmt: str = DATE_FMT,
) -> List[str]:
    """Render the markdown lines for one suite's results.

    `all_rows` holds the last two runs of each test. Their values reach a pull
    request comment, so every cell passes through `cell`.
    """
    dates = [d for d in (parse_date(r, date_fmt) for r in all_rows) if d is not None]
    if not dates:
        return ["# Performance trends", "", "_No results._"]
    run_date = max(dates)

    # Every row counts here, benched or not. An operator arrives with its whole
    # test module, and a rename of its benched parametrization must not read as
    # a new operator.
    operators_now = set()
    operators_before = set()
    for row in all_rows:
        date = parse_date(row, date_fmt)
        operator = operator_name(*row_key(row))
        if date == run_date:
            operators_now.add(operator)
        else:
            operators_before.add(operator)

    # Group the benched parametrizations, newest row first.
    by_test: Dict[Tuple[str, str], List[Dict[str, str]]] = {}
    for row in select_bench_rows(all_rows):
        by_test.setdefault(row_key(row), []).append(row)
    for test_rows in by_test.values():
        test_rows.sort(
            key=lambda r: parse_date(r, date_fmt) or datetime.min, reverse=True
        )

    changes = []
    for (test_path, params), test_rows in by_test.items():
        if len(test_rows) < 2:
            continue
        curr, prev = test_rows[0], test_rows[1]
        if parse_date(curr, date_fmt) != run_date:
            continue

        operator = operator_name(test_path, params)
        for column, metric in tracked_metrics([curr, prev], field_order):
            prev_v = try_parse_float(prev.get(column))
            curr_v = try_parse_float(curr.get(column))
            pct = delta_pct(curr_v, prev_v)
            if pct is None or abs(pct) < threshold:
                continue
            if within_spread(curr, prev, metric, sigma):
                continue
            changes.append((operator, params, metric, prev_v, curr_v, pct))

    added = sorted(operators_now - operators_before - {UNKNOWN_OPERATOR})
    dropped = sorted(operators_before - operators_now - {UNKNOWN_OPERATOR})

    out = ["# Performance trends", ""]
    if added:
        out += [f"**Operators added:** {', '.join(cell(o) for o in added)}", ""]
    if dropped:
        out += [f"**Operators dropped:** {', '.join(cell(o) for o in dropped)}", ""]

    if changes:
        fmt = f"{{:.{ndigits}f}}"
        out += [
            f"Benchmarks that moved by at least {threshold:g}%{gate(sigma)}:",
            "",
            "| Operator | Parametrization | Metric | Previous | Current | Change |",
            "|---|---|---|---|---|---|",
        ]
        for operator, params, metric, prev_v, curr_v, pct in sorted(changes):
            out.append(
                f"| {cell(operator)} | {cell(params)} | {cell(metric)} "
                f"| {fmt.format(prev_v)} | {fmt.format(curr_v)} "
                f"| {verdict(metric, pct)} {pct:+.{ndigits}f}% |"
            )
        out.append("")
    elif not added and not dropped:
        out += [f"No benchmark moved by {threshold:g}%{gate(sigma)}.", ""]

    return out


def main():
    args = parse_args()

    with open(args.csv, "r", newline="") as f:
        reader = csv.DictReader(f)
        all_rows = list(reader)
        field_order = reader.fieldnames or []

    write(
        args.output,
        build_report(
            all_rows,
            field_order,
            threshold=args.threshold,
            sigma=args.sigma,
            ndigits=args.ndigits,
            date_fmt=args.date_fmt,
        ),
    )


if __name__ == "__main__":
    main()
