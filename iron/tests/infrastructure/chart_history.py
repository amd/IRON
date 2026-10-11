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
TEST = "llama_3.2_1b_prompt_1024_tokens_40"
BEFORE = {
    "Commit": "1111111",
    "Date": "2026-10-01 00:00:00",
    "Test Path": "iron/applications/llama_3.2_1b/test.py::test_llama_3_2_1b",
    "Test": TEST,
    "Checks": "1/1",
    "Bench": "yes",
    "TTFT (mean)": "1.0",
}
AFTER = {
    **BEFORE,
    "Commit": "2222222",
    "Date": "2026-10-02 00:00:00",
    "Test Path": "iron/applications/llama3/test.py::test_llama_3_2_1b",
    "TTFT (mean)": "2.0",
}


def write_rows(path: Path, *rows: dict):
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
    write_rows(directory / "all.csv", BEFORE)
    write_rows(directory / "last_two.csv", BEFORE)
    write_rows(tmp_path / "latest.csv", AFTER)
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
    assert f"| `llama3` | `{TEST}` | `TTFT` | 1.00 | 2.00 |" in trends

    run("build_pages.py", "--results-root", tmp_path, "-o", tmp_path / "site")
    page = (tmp_path / "site" / "index.html").read_text()
    data = json.loads(
        re.search(r'<script id="data" type="application/json">(.*?)</script>', page)[1]
    )
    assert list(data) == ["llama3"]
    (chart,) = data["llama3"]["charts"]
    assert chart["dates"] == [BEFORE["Date"], AFTER["Date"]]
    (series,) = chart["series"]
    assert series["points"]["TTFT"] == [1.0, 2.0]
