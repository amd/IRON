# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The results branch's retention, run as publish-results.yml runs it.

``merge_results.sh`` keeps a benched test's runs of the last 90 days, the
newest of each ISO week it ran in before that, at most 400; and every other
test's last two runs, all the trends read of it.
"""

import csv
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[3] / "ci" / "scripts"
FMT = "%Y-%m-%d %H:%M:%S"
COLUMNS = ["Commit", "Date", "Test Path", "Test", "Checks", "Bench", "Latency (mean)"]
BENCHED = ("iron/tests/operators/test_catalog.py::test_operator", "npu2-GEMV-M_2048")
PLAIN = ("iron/tests/common/test_graph.py::test_record", "test_record")
OTHER = ("iron/tests/operators/test_catalog.py::test_operator", "npu2-GEMV-M_4096")


def _rows(dates, tests=((BENCHED, "yes"), (PLAIN, "no"))):
    return [
        {
            "Commit": "abc1234",
            "Date": date.strftime(FMT),
            "Test Path": path,
            "Test": test,
            "Checks": "1/1",
            "Bench": bench,
            "Latency (mean)": "1.0",
        }
        for date in dates
        for (path, test), bench in tests
    ]


def _merge(tmp_path, history, latest):
    """Merge `latest`'s run into a suite holding `history`'s, and read the suite back."""
    suite, run = tmp_path / "krackan" / "small", tmp_path / "run"
    suite.mkdir(parents=True)
    run.mkdir()
    (run / "readme.md").write_text("")
    for path, rows in ((suite / "all.csv", history), (run / "latest.csv", latest)):
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, COLUMNS)
            writer.writeheader()
            writer.writerows(rows)
    subprocess.run([SCRIPTS / "merge_results.sh", run, suite], check=True)
    with open(suite / "all.csv", newline="") as f:
        kept = {}
        for row in csv.DictReader(f):
            kept.setdefault(row["Test"], set()).add(datetime.strptime(row["Date"], FMT))
    return kept


def test_a_benched_test_keeps_90_days_then_a_run_a_week(tmp_path):
    newest = datetime(2026, 10, 30, 9, 13)
    days = [newest - timedelta(days=n) for n in range(1, 200)]
    kept = _merge(tmp_path, _rows(days), _rows([newest]))

    cutoff = newest - timedelta(days=90)
    weeks = {}
    for day in sorted(d for d in days if d < cutoff):
        weeks[day.isocalendar()[:2]] = day
    recent = {d for d in days + [newest] if d >= cutoff}
    assert kept[BENCHED[1]] == recent | set(weeks.values())
    assert kept[PLAIN[1]] == {newest, days[0]}


def test_a_benched_test_keeps_at_most_400_runs(tmp_path):
    newest = datetime(2026, 10, 30, 9, 13)
    hours = [newest - timedelta(hours=n) for n in range(1, 500)]
    kept = _merge(tmp_path, _rows(hours), _rows([newest]))
    assert kept[BENCHED[1]] == {newest} | set(hours[:399])


def test_each_benchmark_keeps_its_own_newest_run_of_a_week(tmp_path):
    """A week another benchmark ran later in keeps this one's run too."""
    a, b = ((BENCHED, "yes"),), ((OTHER, "yes"),)
    june = [datetime(2026, 6, d, 10) for d in (1, 7, 8, 14)]
    newest = datetime(2026, 10, 30, 10)
    history = _rows([june[0], june[2]], a) + _rows([june[1], june[3]], b)
    kept = _merge(tmp_path, history, _rows([newest], a + b))
    assert kept[BENCHED[1]] == {june[0], june[2], newest}
    assert kept[OTHER[1]] == {june[1], june[3], newest}
