# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The nightly's timing gate.

``pretty_trends.py --fail-on`` exits 1 when a named metric of a
benched test got worse than in the run before it past the percentage
gate, and 0 when it got better, moved less, or is not named. The report
marks each move by whether the metric is better higher or lower.
"""

import csv
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[3] / "ci" / "scripts"


def _write(path, metric, before, after):
    """Write two nights of one benched llama test's `metric`."""
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(
            f, ["Date", "Test Path", "Test", "Bench", f"{metric} (mean)"]
        )
        writer.writeheader()
        for date, value in (("2026-10-01", before), ("2026-10-02", after)):
            writer.writerow(
                {
                    "Date": f"{date} 00:00:00",
                    "Test Path": "tests/applications/llama/test.py::test_llama_3_2",
                    "Test": "llama_3.2_1b-prompt_1024_tokens_40",
                    "Bench": "yes",
                    f"{metric} (mean)": value,
                }
            )


@pytest.mark.parametrize(
    "metric,before,after,fails",
    [
        ("TTFT", 1.0, 1.2, True),
        ("TPS", 20.0, 17.0, True),
        ("TTFT", 1.0, 0.8, False),
        ("TPS", 20.0, 19.0, False),
        ("MeanKL", 0.01, 0.02, False),
    ],
    ids=["slower_first_token", "fewer_tokens_a_second", "faster", "within", "kl"],
)
def test_a_worse_time_fails_the_run(tmp_path, metric, before, after, fails):
    path = tmp_path / "all.csv"
    _write(path, metric, before, after)
    gate = ["--fail-on", "TTFT", "--fail-on", "TPS", "--threshold", "10"]
    run = subprocess.run(
        [sys.executable, "pretty_trends.py", path, "-o", tmp_path / "trends.md", *gate],
        cwd=SCRIPTS,
        capture_output=True,
        text=True,
    )
    assert run.returncode == int(fails), run.stdout + run.stderr
    assert ("llama [llama_3.2_1b-prompt_1024_tokens_40]" in run.stdout) == fails


@pytest.mark.parametrize(
    "metric,before,after,mark",
    [
        ("GenerateTPS", 20.0, 17.0, "🔴"),
        ("StreamTPS", 17.0, 20.0, "🟢"),
        ("Cosine", 0.999, 0.9, "🔴"),
        ("MaxKL", 0.2, 0.1, "🟢"),
        ("Tokens", 1024, 2048, "⚪"),
    ],
)
def test_the_report_judges_each_metric_by_its_direction(
    tmp_path, metric, before, after, mark
):
    path = tmp_path / "all.csv"
    _write(path, metric, before, after)
    subprocess.run(
        [sys.executable, "pretty_trends.py", path, "-o", tmp_path / "trends.md"],
        cwd=SCRIPTS,
        check=True,
    )
    row = next(
        line
        for line in (tmp_path / "trends.md").read_text().splitlines()
        if f"`{metric}`" in line
    )
    assert row.endswith(f"| {mark} {(after - before) / before * 100:+.2f}% |"), row
