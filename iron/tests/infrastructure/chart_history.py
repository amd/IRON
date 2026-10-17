# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A benchmark's history across a renamed test path or parametrization: CI's
scripts, run as the workflows run them, continue the rows recorded under the
old name as the new name's, in the trends report and on the pages.
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
# (test path and id before the rename, after it, the chart it continues)
RENAMES = [
    (
        "iron/applications/llama_3.2_1b/test.py::test_llama_3_2_1b",
        "llama_3.2_1b_prompt_1024_tokens_40",
        "tests/applications/llama/test.py::test_llama_3_2",
        "llama_3.2_1b-prompt_1024_tokens_40",
        "llama",
    ),
    (
        "iron/applications/embeddinggemma_2/vision/test.py::test_vision_latency",
        "name_cats",
        "tests/applications/embedding_gemma2/test.py::TestVision::test_vision_latency",
        "name_cats",
        "embedding_gemma2",
    ),
    (
        "iron/operators/conv2d/test.py::test_conv2d",
        "case_band-share_1.0",
        "iron/tests/lm/conv2d.py::test_conv2d",
        "case_band-share_1.0",
        "conv2d",
    ),
]


def rows(date: str, value: str, renamed: bool) -> list[dict]:
    return [
        {
            "Commit": date[:10],
            "Date": date,
            "Test Path": path_after if renamed else path_before,
            "Test": test_after if renamed else test_before,
            "Checks": "1/1",
            "Bench": "yes",
            "TTFT (mean)": value,
        }
        for path_before, test_before, path_after, test_after, _ in RENAMES
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
    for *_, test, chart in RENAMES:
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


def test_a_test_renamed_four_times_continues_its_history(tmp_path):
    """Llama's test directory has had four names, and its test and id a
    second; rows under each continue one chart, the newest name's."""
    old, test = (
        "llama_3.2_1b_prompt_1024_tokens_40",
        "llama_3.2_1b-prompt_1024_tokens_40",
    )
    generations = [
        ("2026-10-01 00:00:00", "iron/applications/llama_3.2_1b", "_1b", old, "1.0"),
        ("2026-10-02 00:00:00", "iron/applications/llama3", "_1b", old, "2.0"),
        ("2026-10-03 00:00:00", "iron/applications/llama", "_1b", old, "3.0"),
        ("2026-10-04 00:00:00", "tests/applications/llama", "_1b", old, "4.0"),
        ("2026-10-05 00:00:00", "tests/applications/llama", "", test, "5.0"),
    ]
    history = [
        {
            "Commit": date[:10],
            "Date": date,
            "Test Path": f"{directory}/test.py::test_llama_3_2{size}",
            "Test": params,
            "Checks": "1/1",
            "Bench": "yes",
            "TTFT (mean)": value,
        }
        for date, directory, size, params, value in generations
    ]
    directory = tmp_path / "phoenix" / "examples"
    directory.mkdir(parents=True)
    write_rows(directory / "all.csv", history[:4])
    write_rows(directory / "last_two.csv", history[2:4])
    write_rows(tmp_path / "latest.csv", history[4:])
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
    assert f"| `llama` | `{test}` | `TTFT` | 4.00 | 5.00 |" in trends

    run("build_pages.py", "--results-root", tmp_path, "-o", tmp_path / "site")
    page = (tmp_path / "site" / "index.html").read_text()
    data = json.loads(
        re.search(r'<script id="data" type="application/json">(.*?)</script>', page)[1]
    )
    assert sorted(data) == ["llama"]
    (phoenix,) = data["llama"]["charts"]
    assert phoenix["dates"] == [date for date, *_ in generations]
    (series,) = phoenix["series"]
    assert series["points"]["TTFT"] == [1.0, 2.0, 3.0, 4.0, 5.0]


# Two runs of krackan's example suite as the `ci` branch holds them.
KRACKAN = """\
Commit,Date,Provenance,Test Path,Test,Checks,Bench,TTFT (mean),TTFT (median),TTFT (min),TTFT (max),TTFT (stddev),TPS (mean),TPS (median),TPS (min),TPS (max),TPS (stddev),PrefillKL (mean),PrefillKL (median),PrefillKL (min),PrefillKL (max),PrefillKL (stddev),DecodeMaxKL (mean),DecodeMaxKL (median),DecodeMaxKL (min),DecodeMaxKL (max),DecodeMaxKL (stddev),Top1Mismatches (mean),Top1Mismatches (median),Top1Mismatches (min),Top1Mismatches (max),Top1Mismatches (stddev),DifferingRuns (mean),DifferingRuns (median),DifferingRuns (min),DifferingRuns (max),DifferingRuns (stddev)
15cc99e2b937291afcd80cbc346a9b4c921e54a3,2026-10-16 18:53:19,commit 15cc99e2b9 | peano 22.0.0+0006955e | mlir_aie 1.4.4 | kernels 3f815aa696b3 | runtime CachedXRTRuntime | xdna 2.21.0_20260625 | xrt 2.21.0 | host docker-runner-65e03adde11c | device NPU Krackan 1 | pmode default,iron/applications/llama_3.2_1b/test.py::test_llama_3_2_1b,llama_3.2_1b_prompt_1024_tokens_40,5/5,yes,2.0786,2.054,2.049,2.183,0.058406335272810875,7.6496,7.651,7.619,7.674,0.020107212636265862,,,,,,,,,,,,,,,,,,,,
f280ccf787b2e0e5f8d842118345db78d7047649,2026-10-16 23:19:38,commit f280ccf787 | peano 22.0.0+0006955e | mlir_aie 1.4.4 | kernels 3f815aa696b3 | runtime CachedXRTRuntime | xdna 2.21.0_20260625 | xrt 2.21.0 | host docker-runner-3cad707bfde2 | device NPU Krackan 1 | pmode default,iron/applications/llama_3.2_1b/test.py::test_llama_3_2_1b,llama_3.2_1b_prompt_1024_tokens_40,5/5,yes,2.0808,2.057,2.03,2.203,0.06953560239186828,7.6672,7.662,7.639,7.712,0.028101601377857246,,,,,,,,,,,,,,,,,,,,
"""
# (test path and id before the models' rebase, after it, the chart it continues)
REBASED = [
    (
        "iron/applications/llama_3.2_1b/test.py::test_llama_3_2_1b",
        "llama_3.2_1b_prompt_1024_tokens_40",
        "tests/applications/llama/test.py::test_llama_3_2",
        "llama_3.2_1b-prompt_1024_tokens_40",
        "llama",
    ),
    (
        "tests/applications/llama/test.py::TestEachStep::test_llama_3_2_1b_each_step",
        "llama_3.2_1b_prompt_13_tokens_1",
        "tests/applications/llama/test.py::TestEachStep::test_llama_3_2_each_step",
        "llama_3.2_1b-prompt_13_tokens_1",
        "llama",
    ),
    (
        "tests/applications/llama/test.py::test_llama_3_2_1b_device_loop",
        "test_llama_3_2_1b_device_loop",
        "tests/applications/llama/test.py::test_llama_3_2_device_loop",
        "llama_3.2_1b",
        "llama",
    ),
    (
        "iron/applications/qwen3/test.py::test_qwen3_1_7b",
        "qwen3_1_7b_prompt_1024_tokens_40",
        "tests/applications/qwen3/test.py::test_qwen3",
        "qwen3_1.7b-prompt_1024_tokens_40",
        "qwen3",
    ),
    (
        "tests/applications/qwen3/test.py::test_qwen3_1_7b_device_loop",
        "test_qwen3_1_7b_device_loop",
        "tests/applications/qwen3/test.py::test_qwen3_device_loop",
        "qwen3_1.7b",
        "qwen3",
    ),
    (
        "iron/tests/operators/catalog.py::test_operator",
        "Merge-rows_2048-audio_token_258881-image_token_258880-audio_at_2048-vision_at_2560",
        "iron/tests/operators/catalog.py::test_operator",
        "Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))",
        "Merge",
    ),
]


def test_a_rebased_parametrization_continues_its_history(tmp_path):
    """Each bench row the models' rebase renamed, recorded as krackan records
    it, continues its chart under the new name."""
    before, after = list(csv.DictReader(KRACKAN.splitlines()))
    directory = tmp_path / "krackan" / "examples"
    directory.mkdir(parents=True)
    with open(directory / "all.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, list(before))
        writer.writeheader()
        writer.writerows(
            {**before, "Test Path": path, "Test": test} for path, test, *_ in REBASED
        )
    with open(tmp_path / "latest.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, list(after))
        writer.writeheader()
        writer.writerows(
            {**after, "Test Path": path, "Test": test}
            for _, _, path, test, _ in REBASED
        )
    run(
        "merge_all.py",
        "--all",
        directory / "all.csv",
        "--latest",
        tmp_path / "latest.csv",
        "--limit",
        1000,
    )

    run("pretty_trends.py", directory / "all.csv", "-o", tmp_path / "trends.md")
    trends = (tmp_path / "trends.md").read_text()
    assert "Operators added" not in trends and "Operators dropped" not in trends

    run("build_pages.py", "--results-root", tmp_path, "-o", tmp_path / "site")
    page = (tmp_path / "site" / "index.html").read_text()
    data = json.loads(
        re.search(r'<script id="data" type="application/json">(.*?)</script>', page)[1]
    )
    assert sorted(data) == sorted({chart for *_, chart in REBASED})
    for name, operator in data.items():
        (krackan,) = operator["charts"]
        assert krackan["dates"] == [before["Date"], after["Date"]]
        assert len(krackan["series"]) == sum(chart == name for *_, chart in REBASED)
        for series in krackan["series"]:
            assert series["points"]["TTFT"] == [2.0786, 2.0808]
            assert series["points"]["TPS"] == [7.6496, 7.6672]
