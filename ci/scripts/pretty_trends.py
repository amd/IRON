#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: Apache-2.0

import argparse
import csv
from datetime import datetime
from typing import Any, Dict, List, Optional

from pretty_common import display_name, split_test_path


def parse_args():
    p = argparse.ArgumentParser(
        description="Create per-test trend tables from CI CSV results"
    )
    p.add_argument(
        "csv", nargs="?", default="all.csv", help="Input CSV (default: all.csv)"
    )
    p.add_argument("-o", "--output", default="trends.md", help="Output markdown file")
    p.add_argument(
        "--threshold",
        type=float,
        default=20.0,
        help="Highlight threshold for absolute percentage change (default: 10.0)",
    )
    p.add_argument(
        "--date-column", default="Date", help="Date column name (default: Date)"
    )
    p.add_argument(
        "--commit-column", default="Commit", help="Commit column name (default: Commit)"
    )
    p.add_argument(
        "--test-column", default="Test", help="Test column name (default: Test)"
    )
    p.add_argument(
        "--test-path-column",
        default="Test Path",
        help="Test path column name (default: 'Test Path')",
    )
    p.add_argument(
        "--round",
        type=int,
        default=2,
        dest="ndigits",
        help="Decimal places for values and percentages (default: 2)",
    )
    p.add_argument("--date-fmt", default="%Y-%m-%d %H:%M:%S")
    return p.parse_args()


def try_parse_float(x: Any) -> Optional[float]:
    if x is None:
        return None
    s = str(x).strip()
    if s == "" or s.lower() in {"n/a", "na", "none"}:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def format_val(v: Optional[float], ndigits: int) -> str:
    if v is None:
        return "n/a"
    f = f"{{:.{ndigits}f}}"
    return f.format(v)


def format_pct(delta_pct: Optional[float], ndigits: int, bold: bool) -> str:
    if delta_pct is None:
        return "(n/a)"
    sign = "+" if delta_pct >= 0 else ""
    f = f"{{:{'+'}0.{ndigits}f}}%" if ndigits > 0 else "{:+.0f}%"
    txt = (
        f"({sign}{abs(delta_pct):.{ndigits}f}%)"
        if False
        else f"({f.format(delta_pct)})"
    )
    return f"<b>{txt}</b>" if bold else txt


def compute_delta_pct(curr: Optional[float], prev: Optional[float]) -> Optional[float]:
    if curr is None or prev is None:
        return None
    if prev == 0:
        return None
    return (curr - prev) / prev * 100.0


def build_table_for_test(
    test_name: str,
    rows: List[Dict[str, str]],
    metrics: List[str],
    date_col: str,
    commit_col: str,
    ndigits: int,
    threshold: float,
    date_fmt: str,
) -> str:

    # Sort newest  to oldest
    rows.sort(
        key=lambda r: datetime.strptime(r.get(date_col, ""), date_fmt).timestamp(),
        reverse=True,
    )

    header_cols = "".join(f"<th>{m}</th>" for m in metrics)
    out = []
    out.append(f"\n### {test_name}\n")
    if len(metrics) == 0:
        out.append("_No metrics available._\n")
        return "\n".join(out)

    out.append("<table>")
    out.append("<thead>")
    out.append("<tr>")
    out.append("<th>Commit/Date</th>")
    out.append(header_cols)
    out.append("</tr>")
    out.append("</thead>")
    out.append("<tbody>")

    # Track previous values for delta computation (previous = next older in sorted list)
    # For each row, compare to the next row in time (older) at the same index+1
    for i, r in enumerate(rows):
        commit = (r.get(commit_col) or "").strip()
        date_s = (r.get(date_col) or "").strip()
        commit_short = commit[:7] if commit else "unknown"
        prev = rows[i + 1] if i + 1 < len(rows) else None

        row_cells = []

        for m in metrics:
            curr_v = try_parse_float(r.get(m))
            prev_v = try_parse_float(prev.get(m)) if prev else None
            delta_pct = compute_delta_pct(curr_v, prev_v)
            highlight = (delta_pct is not None) and (abs(delta_pct) >= threshold)

            val_txt = format_val(curr_v, ndigits)
            pct_txt = format_pct(delta_pct, ndigits, bold=highlight)
            cell_html = f"<td>{val_txt} {pct_txt}</td>"
            row_cells.append(cell_html)

        first_col = f"<td><code>{commit_short}</code> — {date_s}</td>"
        out.append("<tr>")
        out.append(first_col + "".join(row_cells))
        out.append("</tr>")

    out.append("</tbody>")
    out.append("</table>\n")
    return "\n".join(out)


def main():
    args = parse_args()

    with open(args.csv, "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
        field_order = reader.fieldnames or []

    test_col = args.test_column
    test_path_col = args.test_path_column
    commit_col = args.commit_column
    date_col = args.date_column

    # Group rows by (directory, display_name). The display_name is
    # 'funcname[params]' derived from Test Path + Test.
    by_dir: Dict[str, Dict[str, List[Dict[str, str]]]] = {}
    for row in rows:
        test_path = (row.get(test_path_col) or "").strip()
        params = (row.get(test_col) or "").strip()
        directory, func = split_test_path(test_path)
        if not directory:
            directory = "(unknown)"
        display = display_name(func, params, fallback=test_path or "UNNAMED_TEST")
        by_dir.setdefault(directory, {}).setdefault(display, []).append(row)

    # Build output
    out_parts = []
    out_parts.append("# IRON Trends\n")

    exclude_cols = {test_col, test_path_col, commit_col, date_col, "Checks"}

    for directory in sorted(by_dir.keys()):
        out_parts.append(f"\n<details>\n<summary>{directory}</summary>\n")
        tests_in_dir = by_dir[directory]
        for test in sorted(tests_in_dir.keys()):
            test_rows = tests_in_dir[test]
            metrics = [
                k
                for k in field_order
                if k not in exclude_cols
                and any(try_parse_float(r.get(k)) is not None for r in test_rows)
            ]
            metrics.sort()
            section = build_table_for_test(
                test_name=test,
                rows=test_rows,
                metrics=metrics,
                date_col=date_col,
                commit_col=commit_col,
                ndigits=args.ndigits,
                threshold=args.threshold,
                date_fmt=args.date_fmt,
            )
            out_parts.append(section)
        out_parts.append("\n</details>\n")

    with open(args.output, "w", newline="") as f:
        f.write("\n".join(out_parts))


if __name__ == "__main__":
    main()
