#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Write the data the website's Benchmarks page draws, from the results branch.

Reads every ``{arch}/{suite}/all.csv`` under a results root and writes one JSON
file: each suite's latest run on each device, and each benchmark's history,
one series per benched parametrization, one list of runs per device. Only
parametrizations carrying the 'bench' marker appear.

A move between a series' last two runs is judged with the pull request
comment's own gates (``pretty_trends``), so the page and the comment agree on
what moved.
"""

import argparse
import csv
import json
import os
import re
from datetime import datetime, timezone

from pretty_common import (
    ARCHS,
    MEAN_SUFFIX,
    METRICS,
    SUITES,
    UNKNOWN_METRIC,
    metric_label,
    operator_name,
    parse_checks,
    results_dir,
    row_key,
    select_bench_rows,
    split_test_path,
    try_parse_float,
)
from pretty_trends import DATE_FMT, SIGMA, THRESHOLD, delta_pct, within_spread, worse

# How the page names each device and suite.
DEVICES = {"krackan": "Krackan (NPU2)", "phoenix": "Phoenix (NPU1)"}
SUITE_NAMES = {
    "small": ("Operators", "Pull requests"),
    "extensive": ("Operators", "Extensive"),
    "examples": ("Models", "Pull requests"),
    "nightly": ("Models", "Nightly"),
}

# A metric whose figure is another's spread is drawn with it, not on its own.
SPREADS = {"Latency": "Latency MAD"}

# Where a benchmark still run is documented, relative to the Benchmarks page:
# a model on the Models page, an operator in the API reference. A catalog
# benchmark is named for its class; these are named for their test's
# directory.
CATALOG = "iron/tests/operators/test_catalog.py"
OPERATOR_PAGES = {
    "copy_gather": "Gather",
    "flm/gemm": "flm.ProjectionGEMM",
    "flm/layer": "flm.DecodeLayer",
    "flm/prefill_attn": "flm.PrefillAttention",
}


def read_all_csvs(results_root):
    """Map (arch, suite) to the rows of its results CSV, for each CSV under the root."""
    tables = {}
    for arch in ARCHS:
        for suite in SUITES:
            path = os.path.join(results_root, results_dir(arch, suite), "all.csv")
            if os.path.exists(path):
                with open(path, newline="") as f:
                    tables[arch, suite] = list(csv.DictReader(f))
    return tables


def natural_key(text):
    """Sort 'tokens_13' before 'tokens_1024'."""
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", text)]


def shorten_labels(series):
    """Label each series by the parameter components its benchmark's ids do not share.

    A parametrization id names every parameter, so the ids of one benchmark
    agree on most of their length. Only what differs identifies a line. Where
    that leaves two parametrizations one label, each keeps its whole id. A
    parametrization in two suites is one series in each, with one label.
    """
    ids = {(s["test"], s["func"], s["params"]) for s in series}
    components = [set(params.split("-")) for _, _, params in ids]
    shared = set.intersection(*components) if components else set()
    funcs = {func for _, func, _ in ids}
    labels = {}
    for test, func, params in ids:
        kept = [c for c in params.split("-") if c not in shared]
        parts = [func] if len(funcs) > 1 else []
        parts.append("-".join(kept) if kept else params or "default")
        labels[test, func, params] = " · ".join(parts)
    taken = list(labels.values())
    for key, label in labels.items():
        if taken.count(label) > 1:
            labels[key] = " · ".join(p for p in key[1:] if p)
    for s in series:
        s["label"] = labels[s["test"], s["func"], s["params"]]


def passed(row):
    """Whether a row's checks all passed, or None for a row that names none."""
    p, n = parse_checks(row.get("Checks") or "")
    return p == n if n else None


def change(curr, prev, metric):
    """Measure a metric's move from `prev` to `curr`: its percentage and verdict.

    The verdict is 'better' or 'worse' only past both of the pull request
    comment's gates, 'neutral' for a metric with no direction, and None for a
    move inside the gates.
    """
    pct = delta_pct(
        try_parse_float(curr.get(metric + MEAN_SUFFIX)),
        try_parse_float(prev.get(metric + MEAN_SUFFIX)),
    )
    if pct is None:
        return None
    if abs(pct) < THRESHOLD or within_spread(curr, prev, metric, SIGMA):
        return [pct, None]
    if METRICS.get(metric, UNKNOWN_METRIC).higher_is_better is None:
        return [pct, "neutral"]
    return [pct, "worse" if worse(metric, pct) else "better"]


def build_data(results_root, repository):
    """Gather the page's data: the suites' latest runs, and every benchmark's history.

    The extensive suite runs the default suite's tests too, so one commit
    carries two measurements of the same parametrization. Each suite therefore
    keeps its own history, with its own runs.
    """
    tables = read_all_csvs(results_root)
    benched = {
        row_key(row)
        for row in select_bench_rows(r for rows in tables.values() for r in rows)
    }

    runs = []
    benchmarks = {}
    for (arch, suite), rows in tables.items():
        dated = [r for r in rows if (r.get("Date") or "").strip()]
        if not dated:
            continue
        latest = max(r["Date"] for r in dated)
        in_run = [r for r in dated if r["Date"] == latest]
        verdicts = [passed(r) for r in in_run]
        run = {
            "device": arch,
            "suite": suite,
            "date": latest,
            "commit": (in_run[0].get("Commit") or "")[:10],
            "tests": len(in_run),
            "failed": verdicts.count(False),
            "moved": [],
        }
        runs.append(run)

        by_series = {}
        for row in dated:
            if row_key(row) in benched:
                by_series.setdefault(row_key(row), []).append(row)

        for (test_path, params), series_rows in by_series.items():
            series_rows.sort(key=lambda r: r["Date"])
            name = operator_name(test_path, params)
            _, func = split_test_path(test_path)
            # The catalog prefixes each id with its device; without it, one
            # parametrization's runs on each device are one series.
            params = re.sub(r"^npu\d+-", "", params)
            benchmark = benchmarks.setdefault(name, {"suites": {}})
            history = benchmark["suites"].setdefault(suite, {})
            series = history.setdefault(
                (test_path, params),
                {"func": func, "params": params, "test": test_path, "devices": {}},
            )
            points = []
            for row in series_rows:
                values = {}
                for column, raw in row.items():
                    metric = metric_label(column or "")
                    value = try_parse_float(raw) if metric else None
                    if value is not None:
                        values[metric] = value
                points.append(
                    [row["Date"], (row.get("Commit") or "")[:10], passed(row), values]
                )
            changes = {}
            if len(series_rows) > 1:
                prev, curr = series_rows[-2], series_rows[-1]
                for metric in points[-1][3].keys() - SPREADS.values():
                    moved = change(curr, prev, metric)
                    if moved is not None:
                        changes[metric] = moved
            current = series_rows[-1]["Date"] == latest
            series["devices"][arch] = {
                "points": points,
                "current": current,
                "changes": changes,
            }
            if current:
                run["moved"] += [
                    (name, series, metric, pct, verdict)
                    for metric, (pct, verdict) in changes.items()
                    if verdict in ("better", "worse")
                ]

    for benchmark in benchmarks.values():
        shorten_labels([s for h in benchmark["suites"].values() for s in h.values()])
    for run in runs:
        run["moved"] = sorted(
            [name, series["label"], metric, pct, verdict]
            for name, series, metric, pct, verdict in run["moved"]
        )

    metric_order = list(METRICS)
    out = {}
    for name, benchmark in benchmarks.items():
        suites = {}
        for suite in SUITES:
            history = benchmark["suites"].get(suite)
            if not history:
                continue
            series = sorted(history.values(), key=lambda s: natural_key(s["label"]))
            metrics = {
                m
                for s in series
                for d in s["devices"].values()
                for _, _, _, values in d["points"]
                for m in values
            } - set(SPREADS.values())
            suites[suite] = {
                "metrics": sorted(
                    metrics,
                    key=lambda m: (
                        metric_order.index(m) if m in METRICS else len(metric_order),
                        m,
                    ),
                ),
                "series": [
                    {
                        "label": s["label"],
                        "test": f"{s['test']}[{s['params']}]",
                        "devices": s["devices"],
                    }
                    for s in series
                ],
            }
        if not any(suite["metrics"] for suite in suites.values()):
            continue
        group = SUITE_NAMES[next(iter(suites))][0]
        current = any(
            d["current"]
            for suite in suites.values()
            for s in suite["series"]
            for d in s["devices"].values()
        )
        catalogued = any(
            s["test"].startswith(f"{CATALOG}::")
            for suite in suites.values()
            for s in suite["series"]
        )
        anchor = name if catalogued else OPERATOR_PAGES.get(name)
        docs = None
        if current and group == "Models":
            docs = "../models/"
        elif current and anchor:
            docs = f"../api/operators/#iron.operators.{anchor}"
        out[name] = {"group": group, "current": current, "docs": docs, "suites": suites}

    return {
        "generated": datetime.now(timezone.utc).strftime(DATE_FMT),
        "repository": repository,
        "gates": {"threshold": THRESHOLD, "sigma": SIGMA},
        "devices": DEVICES,
        "suites": {
            suite: {"group": group, "name": name}
            for suite, (group, name) in SUITE_NAMES.items()
        },
        "metrics": {
            name: {"unit": m.unit, "higher_is_better": m.higher_is_better}
            for name, m in METRICS.items()
        },
        "spreads": SPREADS,
        "runs": runs,
        "benchmarks": dict(sorted(out.items(), key=lambda kv: natural_key(kv[0]))),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--results-root",
        default=".",
        help="Root of the results branch worktree (default: current directory)",
    )
    parser.add_argument(
        "--repository",
        default="https://github.com/amd/IRON",
        help="The repository the results' commits link to",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="docs/benchmarks/data.json",
        help="The JSON file to write (default: docs/benchmarks/data.json, "
        "beside the Benchmarks page)",
    )
    args = parser.parse_args()

    data = build_data(args.results_root, args.repository)
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(data, f, separators=(",", ":"))
    print(f"Written: {args.output} ({len(data['benchmarks'])} benchmarks)")


if __name__ == "__main__":
    main()
