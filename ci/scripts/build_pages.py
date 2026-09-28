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
    """Yield (arch, suite, row) for every row of every results CSV under the root."""
    for arch in ARCHS:
        for suite in SUITES:
            path = os.path.join(results_root, arch, suite, "all.csv")
            if not os.path.exists(path):
                continue
            with open(path, newline="") as f:
                for row in csv.DictReader(f):
                    yield arch, suite, row


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
        parts = [s["func"]] if len(funcs) > 1 else []
        parts.append("-".join(kept) if kept else s["params"] or "default")
        s["label"] = " · ".join(parts)


def build_data(results_root):
    """Group the benched rows into {operator: {metrics, groups}}.

    The extensive suite runs the default suite's tests too, so one commit
    carries two measurements of the same parametrization. Each suite therefore
    gets its own chart, with its own runs along the x axis.
    """
    rows = [(arch, suite, row) for arch, suite, row in read_all_csvs(results_root)]
    benched = {row_key(row) for row in select_bench_rows(row for _, _, row in rows)}

    operators = {}
    for arch, suite, row in rows:
        key = row_key(row)
        if key not in benched:
            continue
        test_path, params = key
        date = (row.get("Date") or "").strip()
        if not date:
            continue

        groups = operators.setdefault(operator_name(test_path), {})
        bucket = groups.setdefault((arch, suite), {"commits": {}, "series": {}})
        bucket["commits"][date] = (row.get("Commit") or "").strip()[:7] or "unknown"

        _, func = split_test_path(test_path)
        series = bucket["series"].setdefault(
            (test_path, params), {"func": func, "params": params, "points": {}}
        )
        for column, raw in row.items():
            metric = metric_label(column)
            value = try_parse_float(raw) if metric else None
            if value is None:
                continue
            series["points"].setdefault(metric, {})[date] = value

    out = {}
    for name, groups in sorted(operators.items()):
        every_series = [s for b in groups.values() for s in b["series"].values()]
        shorten_labels(every_series)
        metrics = sorted({m for s in every_series for m in s["points"]})
        if not metrics:
            continue
        # One colour per parametrization, so the charts agree.
        colours = sorted({s["label"] for s in every_series})

        charts = []
        for arch in ARCHS:
            for suite in SUITES:
                bucket = groups.get((arch, suite))
                if not bucket:
                    continue
                dates = sorted(bucket["commits"])
                charts.append(
                    {
                        "name": f"{arch} \u2014 {suite}",
                        "dates": dates,
                        "commits": [bucket["commits"][d] for d in dates],
                        "series": [
                            {
                                "label": s["label"],
                                "colour": colours.index(s["label"]),
                                "points": {
                                    metric: [
                                        s["points"].get(metric, {}).get(d)
                                        for d in dates
                                    ]
                                    for metric in metrics
                                },
                            }
                            for s in sorted(
                                bucket["series"].values(), key=lambda s: s["label"]
                            )
                        ],
                    }
                )
        out[name] = {"metrics": metrics, "charts": charts}
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
  h3 { margin: 1.25rem 0 0; font-size: 1rem; }
  select { padding: .3rem; }
  .meta { color: #888; font-size: .85rem; margin-top: .5rem; }
  .chart { position: relative; height: 38vh; min-height: 17rem; }
  .empty { color: #888; font-size: .9rem; margin: .5rem 0 0; }
</style>
</head>
<body>
<nav><h1>Operators</h1><div id="operators"></div></nav>
<main>
  <header>
    <h2 id="title"></h2>
    <label>Metric <select id="metric"></select></label>
  </header>
  <div id="charts"></div>
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
let charts = [];

function colour(i) { return `hsl(${(i * 137.508) % 360} 65% 50%)`; }

function chartFor(spec, metric, host) {
  const series = spec.series.filter(s => s.points[metric].some(v => v !== null));
  const heading = document.createElement('h3');
  heading.textContent = spec.name;
  host.appendChild(heading);
  if (!series.length) {
    const note = document.createElement('p');
    note.className = 'empty';
    note.textContent = `No ${metric} measurements.`;
    host.appendChild(note);
    return 0;
  }
  const box = document.createElement('div');
  box.className = 'chart';
  const canvas = document.createElement('canvas');
  box.appendChild(canvas);
  host.appendChild(box);

  const unit = UNITS[metric];
  charts.push(new Chart(canvas, {
    type: 'line',
    data: {
      labels: spec.commits,
      datasets: series.map(s => ({
        label: s.label,
        data: s.points[metric],
        borderColor: colour(s.colour),
        backgroundColor: colour(s.colour),
        spanGaps: true,
        tension: 0.1,
        pointRadius: 2,
      })),
    },
    options: {
      maintainAspectRatio: false,
      interaction: { mode: 'nearest', intersect: false },
      scales: {
        x: { ticks: { maxRotation: 60, autoSkipPadding: 20 } },
        y: { title: { display: true, text: unit ? `${metric} (${unit})` : metric },
             beginAtZero: true },
      },
      plugins: {
        legend: { position: 'bottom' },
        tooltip: { callbacks: { title: (items) =>
          `${spec.commits[items[0].dataIndex]} — ${spec.dates[items[0].dataIndex]}` } },
      },
    },
  }));
  return series.length;
}

function draw(name, metric) {
  const op = DATA[name];
  charts.forEach(c => c.destroy());
  charts = [];
  const host = document.getElementById('charts');
  host.textContent = '';

  const counts = op.charts.map(spec =>
    `${spec.name}: ${chartFor(spec, metric, host)} parametrization(s),` +
    ` ${spec.commits.length} run(s)`);
  document.getElementById('meta').textContent =
    `${counts.join('. ')}. Page built ${GENERATED}.`;
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
