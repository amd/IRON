# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""CI's pages script, run as publish-pages.yml runs it, draws one chart per
runner for each operator's, or each shared-test decoder's, nightly results.
"""

import csv
import json
import re
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[3] / "ci" / "scripts"

# (test path, test id, the chart it belongs to)
TESTS = [
    (
        "tests/applications/llama/test.py::test_llama_3_2",
        "llama_3.2_1b-prompt_1024_tokens_40",
        "llama",
    ),
    (
        "tests/applications/embedding_gemma2/test.py::TestVision::test_vision_latency",
        "name_cats",
        "embedding_gemma2",
    ),
    ("iron/tests/lm/test_conv2d.py::test_conv2d", "case_band-share_1.0", "conv2d"),
    (
        "tests/applications/decoders/test.py::test_generation",
        "gemma3-long-40",
        "gemma3",
    ),
]
COLUMNS = ["Commit", "Date", "Test Path", "Test", "Checks", "Bench", "TTFT (mean)"]


def test_each_runner_s_nightly_results_get_charts_of_their_own(tmp_path):
    for arch, value in (("krackan", "1.0"), ("phoenix", "2.0")):
        directory = tmp_path / arch / "nightly"
        directory.mkdir(parents=True)
        with open(directory / "all.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, COLUMNS)
            writer.writeheader()
            for path, test, _ in TESTS:
                writer.writerow(
                    dict(zip(COLUMNS, ("2026-10-02", "2026-10-02 00:00:00")))
                    | {"Test Path": path, "Test": test, "Checks": "1/1"}
                    | {"Bench": "yes", "TTFT (mean)": value}
                )

    script = SCRIPTS / "build_pages.py"
    site = tmp_path / "site"
    subprocess.run(
        [sys.executable, script, "--results-root", tmp_path, "-o", site],
        check=True,
        cwd=SCRIPTS,
    )
    page = (site / "index.html").read_text()
    data = json.loads(
        re.search(r'<script id="data" type="application/json">(.*?)</script>', page)[1]
    )
    for *_, chart in TESTS:
        krackan, phoenix = data[chart]["charts"]
        assert krackan["name"] == "krackan — nightly"
        assert phoenix["name"] == "phoenix — nightly"
        assert phoenix["series"][0]["points"]["TTFT"] == [2.0]
