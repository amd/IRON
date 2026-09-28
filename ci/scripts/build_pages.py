#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Build the benchmark history site from the CSVs on the results branch.

Reads every ``{arch}/{suite}/all.csv`` under a results root and writes a single
self-contained ``index.html``: one chart per operator, one line per
parametrization, with a metric selector. Only parametrizations carrying the
'bench' marker appear.
"""

import argparse
import csv
import json
import os
from datetime import datetime, timezone

from pretty_common import (
    metric_label,
    operator_name,
    row_key,
    select_bench_rows,
    split_test_path,
    try_parse_float,
)

SUITES = ["small", "extensive", "examples"]
ARCHS = ["krackan", "phoenix"]


def read_all_csvs(results_root):
    """Yield (arch, row) for every row of every results CSV under the root."""
    for arch in ARCHS:
        for suite in SUITES:
            path = os.path.join(results_root, arch, suite, "all.csv")
            if not os.path.exists(path):
                continue
            with open(path, newline="") as f:
                for row in csv.DictReader(f):
                    yield arch, row


def shorten_labels(series):
    """Drop the parameter components every series of an operator shares.

    A parametrization id names every parameter, so the ids of one operator agree
    on most of their length. Only what differs identifies a line.
    """
    components = [set(s["params"].split("-")) for s in series]
    shared = set.intersection(*components) if components else set()
    funcs = {s["func"] for s in series}
    for s in series:
        kept = [c for c in s["params"].split("-") if c not in shared]
        parts = [s["arch"]]
        if len(funcs) > 1:
            parts.append(s["func"])
        parts.append("-".join(kept) if kept else s["params"] or "default")
        s["label"] = " · ".join(parts)


def build_data(results_root):
    """Group the benched rows into {operator: {series, dates, metrics}}."""
    rows = [(arch, row) for arch, row in read_all_csvs(results_root)]
    benched = {row_key(row) for row in select_bench_rows(row for _, row in rows)}

    operators = {}
    for arch, row in rows:
        key = row_key(row)
        if key not in benched:
            continue
        test_path, params = key
        date = (row.get("Date") or "").strip()
        if not date:
            continue

        operator = operators.setdefault(
            operator_name(test_path), {"series": {}, "dates": set()}
        )
        operator["dates"].add(date)

        _, func = split_test_path(test_path)
        series_key = f"{arch}\u0000{test_path}\u0000{params}"
        series = operator["series"].setdefault(
            series_key,
            {"arch": arch, "func": func, "params": params, "points": {}},
        )
        for column, raw in row.items():
            metric = metric_label(column)
            value = try_parse_float(raw) if metric else None
            if value is None:
                continue
            series["points"].setdefault(metric, {})[date] = value

    out = {}
    for name, operator in sorted(operators.items()):
        dates = sorted(operator["dates"])
        metrics = sorted({m for s in operator["series"].values() for m in s["points"]})
        if not metrics:
            continue
        series = list(operator["series"].values())
        shorten_labels(series)
        series.sort(key=lambda s: s["label"])
        out[name] = {
            "dates": dates,
            "metrics": metrics,
            "series": [
                {
                    "label": s["label"],
                    "points": {
                        metric: [s["points"].get(metric, {}).get(d) for d in dates]
                        for metric in metrics
                    },
                }
                for s in series
            ],
        }
    return out


PAGE = """<!DOCTYPE html>
<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>IRON benchmark history</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<style>
  :root { color-scheme: light dark; }
  body { font-family: system-ui, sans-serif; margin: 0; display: flex; min-height: 100vh; }
  nav { width: 15rem; flex: none; border-right: 1px solid #8884; padding: 1rem; overflow-y: auto; }
  nav h1 { font-size: 1rem; margin: 0 0 .75rem; }
  nav a { display: block; padding: .3rem .5rem; border-radius: .25rem; color: inherit;
          text-decoration: none; font-size: .9rem; }
  nav a:hover { background: #8882; }
  nav a.active { background: #2563eb; color: #fff; }
  main { flex: 1; padding: 1.5rem 2rem; min-width: 0; }
  header { display: flex; align-items: baseline; gap: 1rem; flex-wrap: wrap; }
  h2 { margin: 0; }
  select { padding: .3rem; }
  .meta { color: #888; font-size: .85rem; margin-top: .5rem; }
  .chart { position: relative; height: 70vh; margin-top: 1rem; }
</style>
</head>
<body>
<nav><h1>Operators</h1><div id="operators"></div></nav>
<main>
  <header>
    <h2 id="title"></h2>
    <label>Metric <select id="metric"></select></label>
  </header>
  <div class="chart"><canvas id="chart"></canvas></div>
  <p class="meta" id="meta"></p>
</main>
<script id="data" type="application/json">__DATA__</script>
<script>
const DATA = JSON.parse(document.getElementById('data').textContent);
const GENERATED = "__GENERATED__";
// The CSV carries no units, so name them here.
const UNITS = {Latency: 'us', Bandwidth: 'GB/s', Throughput: 'GFLOP/s',
               TTFT: 's', TPS: 'tokens/s'};
const names = Object.keys(DATA);
let chart = null;

function colour(i) { return `hsl(${(i * 137.508) % 360} 65% 50%)`; }

function draw(name, metric) {
  const op = DATA[name];
  const series = op.series.filter(s => s.points[metric]);
  const unit = UNITS[metric];
  if (chart) chart.destroy();
  chart = new Chart(document.getElementById('chart'), {
    type: 'line',
    data: {
      labels: op.dates,
      datasets: series.map((s, i) => ({
        label: s.label,
        data: s.points[metric],
        borderColor: colour(i),
        backgroundColor: colour(i),
        spanGaps: true,
        tension: 0.1,
        pointRadius: 2,
      })),
    },
    options: {
      maintainAspectRatio: false,
      interaction: { mode: 'nearest', intersect: false },
      scales: {
        x: { ticks: { maxRotation: 60, autoSkipPadding: 20,
                      callback(i) { return op.dates[i].slice(0, 10); } } },
        y: { title: { display: true, text: unit ? `${metric} (${unit})` : metric },
             beginAtZero: false },
      },
      plugins: { legend: { position: 'bottom' } },
    },
  });
  document.getElementById('meta').textContent =
    `${series.length} parametrization(s), ${op.dates.length} run(s). Page built ${GENERATED}.`;
}

function select(name) {
  const op = DATA[name];
  location.hash = name;
  document.getElementById('title').textContent = name;
  document.querySelectorAll('#operators a').forEach(
    a => a.classList.toggle('active', a.dataset.name === name));

  const picker = document.getElementById('metric');
  const keep = op.metrics.includes(picker.value) ? picker.value : op.metrics[0];
  picker.innerHTML = '';
  for (const m of op.metrics) {
    const option = document.createElement('option');
    option.value = option.textContent = m;
    picker.appendChild(option);
  }
  picker.value = keep;
  draw(name, keep);
}

for (const name of names) {
  const a = document.createElement('a');
  a.href = '#' + name;
  a.textContent = name;
  a.dataset.name = name;
  a.onclick = e => { e.preventDefault(); select(name); };
  document.getElementById('operators').appendChild(a);
}
document.getElementById('metric').onchange =
  e => draw(document.getElementById('title').textContent, e.target.value);

if (names.length) {
  select(names.includes(decodeURIComponent(location.hash.slice(1)))
    ? decodeURIComponent(location.hash.slice(1)) : names[0]);
} else {
  document.getElementById('title').textContent = 'No benchmark results yet';
}
</script>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--results-root",
        default=".",
        help="Root of the results branch worktree (default: current directory)",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="site",
        help="Directory to write the site into (default: site)",
    )
    args = parser.parse_args()

    data = build_data(args.results_root)
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    # Escaping '<' keeps a test name that happens to spell a closing tag from
    # ending the script element early.
    payload = json.dumps(data, separators=(",", ":")).replace("<", "\\u003c")
    page = PAGE.replace("__GENERATED__", generated).replace("__DATA__", payload)

    os.makedirs(args.output_dir, exist_ok=True)
    out_path = os.path.join(args.output_dir, "index.html")
    with open(out_path, "w") as f:
        f.write(page)
    print(f"Written: {out_path} ({len(data)} operators)")


if __name__ == "__main__":
    main()
