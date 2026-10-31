---
hide:
  - navigation
  - toc
---

<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Benchmarks

Every figure here was measured by CI on a Krackan (NPU2) and a Phoenix (NPU1)
runner. A test marked `@pytest.mark.bench` records its latency, bandwidth or
throughput; a model's test records its time to first token (TTFT) and tokens
per second (TPS), and its accuracy checks' figures beside them. Each run's results are
kept on the [`ci` branch](https://github.com/amd/IRON/tree/ci), and this page
is rebuilt from them after every run.

| Suite | Benchmarks | Runs on | History here |
|---|---|---|---|
| **Pull requests** | Operators, and each model's shortest call | every pull request, and each push to `devel` and `main` | the pushes to `devel` and `main`; a pull request's own figures are in the comment CI posts on it |
| **Extensive** | Operators, the pull request suite's and the extensive ones | each night, and each push to `devel` and `main` | every run |
| **Nightly** | Models, every test on the real checkpoints | each night | every run |

A move between a benchmark's last two runs is called *better* or *worse* only
past the same two gates as the pull request comment: at least 5%, and more than
twice the spread the runs measured. Times are UTC. A run whose checks failed is
drawn with a ✕; its figure is what the test measured, not a result to trust.
Each benchmark links to its operator in the
[operator reference](api/operators.md) or to [Models](models.md).
The history keeps every run of the last 90 days and, before that, the newest
run of each week, at most 400 runs.

## Latest runs

<div id="iron-runs" class="iron-runs" markdown>

!!! info "No benchmark data in this build"
    CI's Publish Pages workflow writes `benchmarks/data.json` from the `ci`
    branch. To preview with real data, check out that branch and run
    `python ci/scripts/build_pages.py --results-root <checkout>` before
    `mkdocs serve`.

</div>

## History

<div id="iron-bench" class="iron-bench" hidden>
  <div class="iron-bench-filters">
    <label>Benchmark <select id="iron-bench-name"></select></label>
    <label>Suite <select id="iron-bench-suite"></select></label>
    <label>Metric <select id="iron-bench-metric"></select></label>
  </div>
  <p id="iron-bench-about" class="iron-bench-about"></p>
  <div id="iron-bench-charts" class="iron-bench-charts"></div>
  <div id="iron-bench-table"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js" integrity="sha384-9nhczxUqK87bcKHh20fSQcTGD4qq5GhayNYSYWqwBkINBhOfQLg/P5HG5lF1urn4" crossorigin="anonymous"></script>
<script src="../assets/javascripts/benchmarks.js"></script>
