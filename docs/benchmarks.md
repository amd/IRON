<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Benchmarks

IRON's performance figures come from CI, not from the documentation. Every
test marked `@pytest.mark.bench` records its latency, bandwidth or
throughput, and for a model its time to first token and tokens per second.

- **Pull requests:** CI runs the operator and application suites on Phoenix
  (NPU1) and Krackan (NPU2) and posts the figures as a comment on the pull
  request.
- **History:** runs on `main` and `devel`, and the nightly application
  suite, are merged into the
  [`ci` branch](https://github.com/amd/IRON/tree/ci) as
  `{arch}/{suite}/all.csv` by `publish-results.yml`.
- **Charts:** the page below is rebuilt from that history after each run
  (`ci/scripts/build_pages.py`). It has one chart per operator or model,
  architecture and suite, one line per parametrization, and a metric
  selector.

!!! note "Opens in a new tab"
    The chart page is a self-contained static build, refreshed independently
    of this site.

[Open the benchmark history](charts/index.html){ .md-button .md-button--primary target="_blank" }
