# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A benchmark's history across a renamed test directory: CI's scripts, run
as the workflows run them, continue the rows recorded under the old name as
the new name's, in the trends report and on the pages.
"""

import csv
import json
import re
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[3] / "ci" / "scripts"

COLUMNS = ["Commit", "Date", "Test Path", "Test", "Checks", "Bench", "TTFT (mean)"]
BEFORE, AFTER = "2026-10-01 00:00:00", "2026-10-02 00:00:00"
# (test path before the rename, after it, the test, the chart it continues)
RENAMES = [
    (
        "iron/applications/llama_3.2_1b/test.py::test_llama_3_2_1b",
        "iron/applications/llama/test.py::test_llama_3_2_1b",
        "llama_3.2_1b_prompt_1024_tokens_40",
        "llama",
    ),
    (
        "iron/applications/embeddinggemma_2/vision/test.py::test_vision_latency",
        "iron/applications/embedding_gemma2/vision/test.py::test_vision_latency",
        "name_image",
        "embedding_gemma2/vision",
    ),
]


def rows(date: str, value: str, renamed: bool) -> list[dict]:
    return [
        {
            "Commit": date[:10],
            "Date": date,
            "Test Path": after if renamed else before,
            "Test": test,
            "Checks": "1/1",
            "Bench": "yes",
            "TTFT (mean)": value,
        }
        for before, after, test, _ in RENAMES
    ]


def write_rows(path: Path, rows: list[dict]):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def run(script: str, *args):
    subprocess.run(
        [sys.executable, str(SCRIPTS / script), *map(str, args)],
        check=True,
        cwd=SCRIPTS,
    )


def test_a_renamed_directory_continues_its_history(tmp_path):
    directory = tmp_path / "phoenix" / "examples"
    directory.mkdir(parents=True)
    write_rows(directory / "all.csv", rows(BEFORE, "1.0", renamed=False))
    write_rows(directory / "last_two.csv", rows(BEFORE, "1.0", renamed=False))
    write_rows(tmp_path / "latest.csv", rows(AFTER, "2.0", renamed=True))
    for name, limit in (("all.csv", 1000), ("last_two.csv", 2)):
        run(
            "merge_all.py",
            "--all",
            directory / name,
            "--latest",
            tmp_path / "latest.csv",
            "--limit",
            limit,
        )

    run("pretty_trends.py", directory / "last_two.csv", "-o", tmp_path / "trends.md")
    trends = (tmp_path / "trends.md").read_text()
    assert "Operators added" not in trends and "Operators dropped" not in trends
    for _, _, test, chart in RENAMES:
        assert f"| `{chart}` | `{test}` | `TTFT` | 1.00 | 2.00 |" in trends

    run("build_pages.py", "--results-root", tmp_path, "-o", tmp_path / "site")
    page = (tmp_path / "site" / "index.html").read_text()
    data = json.loads(
        re.search(r'<script id="data" type="application/json">(.*?)</script>', page)[1]
    )
    assert sorted(data) == sorted(chart for *_, chart in RENAMES)
    for *_, chart in RENAMES:
        (phoenix,) = data[chart]["charts"]
        assert phoenix["dates"] == [BEFORE, AFTER]
        (series,) = phoenix["series"]
        assert series["points"]["TTFT"] == [1.0, 2.0]


def test_a_directory_renamed_twice_continues_its_history(tmp_path):
    """Llama's application directory has had three names; rows under each
    continue one chart, the newest name's."""
    test = "llama_3.2_1b_prompt_1024_tokens_40"
    generations = [
        ("2026-10-01 00:00:00", "iron/applications/llama_3.2_1b", "1.0"),
        ("2026-10-02 00:00:00", "iron/applications/llama3", "2.0"),
        ("2026-10-03 00:00:00", "iron/applications/llama", "3.0"),
    ]
    history = [
        {
            "Commit": date[:10],
            "Date": date,
            "Test Path": f"{directory}/test.py::test_llama_3_2_1b",
            "Test": test,
            "Checks": "1/1",
            "Bench": "yes",
            "TTFT (mean)": value,
        }
        for date, directory, value in generations
    ]
    directory = tmp_path / "phoenix" / "examples"
    directory.mkdir(parents=True)
    write_rows(directory / "all.csv", history[:2])
    write_rows(directory / "last_two.csv", history[:2])
    write_rows(tmp_path / "latest.csv", history[2:])
    for name, limit in (("all.csv", 1000), ("last_two.csv", 2)):
        run(
            "merge_all.py",
            "--all",
            directory / name,
            "--latest",
            tmp_path / "latest.csv",
            "--limit",
            limit,
        )

    run("pretty_trends.py", directory / "last_two.csv", "-o", tmp_path / "trends.md")
    trends = (tmp_path / "trends.md").read_text()
    assert "Operators added" not in trends and "Operators dropped" not in trends
    assert f"| `llama` | `{test}` | `TTFT` | 2.00 | 3.00 |" in trends

    run("build_pages.py", "--results-root", tmp_path, "-o", tmp_path / "site")
    page = (tmp_path / "site" / "index.html").read_text()
    data = json.loads(
        re.search(r'<script id="data" type="application/json">(.*?)</script>', page)[1]
    )
    assert sorted(data) == ["llama"]
    (phoenix,) = data["llama"]["charts"]
    assert phoenix["dates"] == [date for date, _, _ in generations]
    (series,) = phoenix["series"]
    assert series["points"]["TTFT"] == [1.0, 2.0, 3.0]
