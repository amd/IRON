# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The pull request comment, run as CI runs it over artifacts, the results branch and the suites' status."""

import csv
import json
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[3] / "ci" / "scripts"

LLAMA = ("tests/applications/llama/test.py::test_llama_3_2", "prompt_13_tokens_40")
GEMV = ("iron/tests/operators/test_catalog.py::test_operator", "npu2-GEMV-M_2048")
BASELINE = ("2026-10-30 03:00:00", "1234567890abcdef")
RUN = ("2026-11-02 10:00:00", "fedcba0987654321")


def _write(path, run, test, **metrics):
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "Commit": run[1],
        "Date": run[0],
        "Test Path": test[0],
        "Test": test[1],
        "Checks": "1/1",
        "Bench": "yes",
    } | {f"{m} (mean)": v for m, v in metrics.items()}
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, list(row))
        writer.writeheader()
        writer.writerow(row)


def _comment(tmp_path, status, moved, quiet=()):
    """Render the comment: `moved` suites' TPS halves, `quiet` suites' holds."""
    for directory in (*moved, *quiet):
        test = LLAMA if directory.endswith("examples") else GEMV
        _write(tmp_path / "history" / directory / "all.csv", BASELINE, test, TPS=20.0)
        tps = 10.0 if directory in moved else 20.0
        _write(tmp_path / "artifacts" / directory / "latest.csv", RUN, test, TPS=tps)
    (tmp_path / "status.json").write_text(json.dumps(status))
    out = tmp_path / "comment.md"
    subprocess.run(
        [sys.executable, "pr_comment.py", "--artifacts", tmp_path / "artifacts"]
        + ["--history", tmp_path / "history", "--status", tmp_path / "status.json"]
        + ["--commit", "abc1234", "-o", out],
        check=True,
        cwd=SCRIPTS,
    )
    return out.read_text()


def test_a_suite_that_moved_nothing_keeps_its_section_beside_one_that_moved(
    tmp_path,
):
    status = {"krackan/examples": "success", "phoenix/examples": "success"}
    comment = _comment(tmp_path, status, ["krackan/examples"], ["phoenix/examples"])
    assert "<summary><b>Krackan - Applications</b></summary>" in comment
    (quiet,) = [
        line for line in comment.splitlines() if "Phoenix - Applications" in line
    ]
    assert "no benchmark moved" in quiet


def test_a_suite_still_running_is_pending_not_missing(tmp_path):
    status = {"krackan/examples": "success", "phoenix/small": "pending"}
    comment = _comment(tmp_path, status, ["krackan/examples"])
    assert "Still running: Phoenix - Operators." in comment
    assert "Phoenix - Operators (pending)" not in comment
    assert "Krackan - Operators (missing)" in comment


def test_each_suite_s_table_names_what_its_rows_are(tmp_path):
    status = {"krackan/examples": "success", "krackan/small": "success"}
    comment = _comment(tmp_path, status, ["krackan/examples", "krackan/small"])
    operators, applications = comment.split("Krackan - Applications")
    assert "| Model | Parametrization |" in applications
    assert "| Operator | Parametrization |" in operators


def test_each_suite_names_the_run_it_compares_with(tmp_path):
    status = {"krackan/examples": "success", "phoenix/examples": "success"}
    comment = _comment(tmp_path, status, ["krackan/examples"], ["phoenix/examples"])
    previous = "Previous: `1234567` (2026-10-30 03:00)"
    assert comment.count(previous) == 2
