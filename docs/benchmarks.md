<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Benchmarks

Every pull request to `devel` and `main` benches each operator marked
`@pytest.mark.bench`; `publish-results.yml` merges the results into the `ci`
branch, and the chart below is rebuilt from that history after every run.

Each operator gets one chart per architecture and test suite, one line per
parametrization, with a metric selector (`ci/scripts/build_pages.py`).

!!! note "Opens in a new tab"
    The chart page is a self-contained static build, refreshed independently
    of this site.

[Open the benchmark history](charts/index.html){ .md-button .md-button--primary target="_blank" }
