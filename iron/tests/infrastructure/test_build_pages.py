# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""CI's Performance Checks page data and the pull request comment, run as CI runs them.

The page's data names each benchmark as the comment does, holds one series
per parametrization with each device's runs, says which ran in each suite's
latest run and which checks failed, and judges a move by the comment's gates;
the comment links each moved benchmark to its history on the page.
"""

import csv
import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

SCRIPTS = Path(__file__).resolve().parents[3] / "ci" / "scripts"
PAGE = "https://amd.github.io/IRON/benchmarks/"

# (test path, test id, the benchmark it belongs to)
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
    (
        "iron/applications/llama_3.2_1b/test.py::test_llama_3_2_1b",
        "llama_3.2_1b_prompt_13_tokens_1",
        "llama_3.2_1b",
    ),
]
GEMV = "iron/tests/operators/test_catalog.py::test_operator"
COLUMNS = ["Commit", "Date", "Test Path", "Test", "Checks", "Bench"]
NIGHTS = ["2026-10-01 10:00:00", "2026-10-02 10:00:00"]


def _row(date, path, test, checks="1/1", **metrics):
    return {
        "Commit": f"{date[8:10]}abcdef12345",
        "Date": date,
        "Test Path": path,
        "Test": test,
        "Checks": checks,
        "Bench": "yes",
    } | {f"{m} (mean)": v for m, v in metrics.items()}


def _write(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = list(dict.fromkeys(COLUMNS + [c for row in rows for c in row]))
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, columns)
        writer.writeheader()
        writer.writerows(rows)


def _page_data(root):
    out = root / "data.json"
    subprocess.run(
        [sys.executable, "build_pages.py", "--results-root", root, "-o", out],
        check=True,
        cwd=SCRIPTS,
    )
    return json.loads(out.read_text())


def test_each_runner_s_nightly_results_are_series_of_their_own(tmp_path):
    for arch, value in (("krackan", 1.0), ("phoenix", 2.0)):
        _write(
            tmp_path / arch / "nightly" / "all.csv",
            [_row(NIGHTS[1], path, test, TTFT=value) for path, test, _ in TESTS],
        )

    data = _page_data(tmp_path)
    for *_, name in TESTS:
        benchmark = data["benchmarks"][name]
        assert benchmark["group"] == "Models" and benchmark["current"]
        assert benchmark["docs"] == "../models/"
        (series,) = benchmark["suites"]["nightly"]["series"]
        for arch, value in (("krackan", 1.0), ("phoenix", 2.0)):
            run = series["devices"][arch]
            assert run["current"]
            assert run["points"] == [[NIGHTS[1], "02abcdef12", True, {"TTFT": value}]]


def test_a_catalog_parametrization_is_one_series_over_its_devices(tmp_path):
    for arch, npu in (("krackan", "npu2"), ("phoenix", "npu1")):
        _write(
            tmp_path / arch / "small" / "all.csv",
            [_row(NIGHTS[1], GEMV, f"{npu}-GEMV-M_2048-K_8192", Latency=10.0)],
        )

    gemv = _page_data(tmp_path)["benchmarks"]["GEMV"]
    (series,) = gemv["suites"]["small"]["series"]
    assert series["label"] == "GEMV-M_2048-K_8192"
    assert set(series["devices"]) == {"krackan", "phoenix"}
    assert gemv["docs"] == "../api/operators/#iron.operators.GEMV"


def test_the_latest_run_says_what_ran_failed_and_moved(tmp_path):
    kept, dropped, failing = "M_2048", "M_4096", "M_8192"
    _write(
        tmp_path / "krackan" / "small" / "all.csv",
        [
            _row(NIGHTS[0], GEMV, f"npu2-GEMV-{kept}", Latency=10.0),
            _row(NIGHTS[0], GEMV, f"npu2-GEMV-{dropped}", Latency=10.0),
            _row(NIGHTS[0], GEMV, f"npu2-GEMV-{failing}", Latency=10.0),
            _row(NIGHTS[1], GEMV, f"npu2-GEMV-{kept}", Latency=15.0),
            _row(NIGHTS[1], GEMV, f"npu2-GEMV-{failing}", "0/1", Latency=10.2),
        ],
    )

    data = _page_data(tmp_path)
    (run,) = data["runs"]
    assert (run["date"], run["tests"], run["failed"]) == (NIGHTS[1], 2, 1)
    assert run["moved"] == [["GEMV", kept, "Latency", 50.0, "worse"]]

    series = {
        s["label"]: s["devices"]["krackan"]
        for s in data["benchmarks"]["GEMV"]["suites"]["small"]["series"]
    }
    assert not series[dropped]["current"]
    assert series[kept]["changes"]["Latency"] == [50.0, "worse"]
    assert series[failing]["changes"]["Latency"][1] is None
    assert series[failing]["points"][-1][2] is False


def test_a_benchmark_no_longer_run_anywhere_is_not_current(tmp_path):
    _write(
        tmp_path / "krackan" / "small" / "all.csv",
        [
            _row(
                NIGHTS[0], "iron/operators/gemv/test.py::test_gemv", "M_2048", Latency=1
            ),
            _row(NIGHTS[1], GEMV, "npu2-GEMV-M_2048", Latency=1.0),
        ],
    )
    benchmarks = _page_data(tmp_path)["benchmarks"]
    assert not benchmarks["gemv"]["current"] and benchmarks["gemv"]["docs"] is None
    assert benchmarks["GEMV"]["current"]


def test_an_operator_named_for_its_test_s_directory_links_its_class(tmp_path):
    _write(
        tmp_path / "krackan" / "extensive" / "all.csv",
        [
            _row(
                NIGHTS[1],
                "iron/operators/flm/gemm/test.py::test_gemm",
                "M_1",
                Latency=1,
            )
        ],
    )
    docs = _page_data(tmp_path)["benchmarks"]["flm/gemm"]["docs"]
    assert docs == "../api/operators/#iron.operators.flm.ProjectionGEMM"


def test_the_comment_links_each_move_to_its_history_on_the_page(tmp_path):
    history = tmp_path / "history"
    artifacts = tmp_path / "artifacts"
    test = "npu2-GEMV-M_2048"
    _write(
        history / "krackan" / "small" / "all.csv",
        [_row(NIGHTS[0], GEMV, test, Bandwidth=100.0)],
    )
    _write(
        artifacts / "krackan" / "small" / "latest.csv",
        [_row(NIGHTS[1], GEMV, test, Bandwidth=50.0)],
    )
    status = tmp_path / "status.json"
    status.write_text(json.dumps({"krackan/small": "success"}))
    comment = tmp_path / "comment.md"
    subprocess.run(
        [sys.executable, "pr_comment.py", "--artifacts", artifacts]
        + ["--history", history, "--status", status, "--commit", "abc1234"]
        + ["--benchmarks-page", PAGE, "-o", comment],
        check=True,
        cwd=SCRIPTS,
    )
    (row,) = [line for line in comment.read_text().splitlines() if "GEMV" in line]
    assert "50.00 GB/s" in row and "🔴 -50.00%" in row
    url = row.split("](", 1)[1].split(")", 1)[0]
    assert url.startswith(PAGE + "#")
    state = {k: v for k, (v,) in parse_qs(urlsplit(url).fragment).items()}
    assert state == {"bench": "GEMV", "suite": "small", "metric": "Bandwidth"}

    _write(
        history / "krackan" / "small" / "all.csv",
        [
            _row(NIGHTS[0], GEMV, test, Bandwidth=100.0),
            _row(NIGHTS[1], GEMV, test, Bandwidth=50.0),
        ],
    )
    page = _page_data(history)["benchmarks"][state["bench"]]["suites"]
    assert state["metric"] in page[state["suite"]]["metrics"]


LLAMA = "tests/applications/llama/test.py"


def test_a_model_s_trend_is_each_checkpoint_s_decode_in_each_device_s_form(tmp_path):
    each_step = f"{LLAMA}::TestEachStep::test_llama_3_2_each_step"
    _write(
        tmp_path / "krackan" / "nightly" / "all.csv",
        [
            _row(night, path, test, TPS=tps, TTFT=0.25)
            for night in NIGHTS
            for path, test, tps in (
                (f"{LLAMA}::test_llama_3_2", "llama_3.2_1b-prompt_13_tokens_40", 14.6),
                (f"{LLAMA}::test_llama_3_2_device_loop", "llama_3.2_1b", 14.5),
                (each_step, "llama_3.2_1b-prompt_13_tokens_40", 5.4),
                (f"{LLAMA}::test_llama_3_2", "llama_3.2_3b-prompt_13_tokens_40", 6.4),
                (each_step, "llama_3.2_3b-prompt_13_tokens_40", 2.8),
            )
        ],
    )
    _write(
        tmp_path / "phoenix" / "nightly" / "all.csv",
        [
            _row(NIGHTS[1], each_step, f"llama_3.2_{size}-prompt_13_tokens_40", TPS=3.0)
            for size in ("1b", "3b")
        ],
    )

    trends = {t["title"]: t for t in _page_data(tmp_path)["trends"]}
    one, three = trends["Llama 3.2 1B"], trends["Llama 3.2 3B"]
    assert (one["suite"], one["metric"], one["also"]) == ("nightly", "TPS", "TTFT")
    assert one["series"] == {
        "krackan": "test_llama_3_2_device_loop · llama_3.2_1b",
        "phoenix": "TestEachStep::test_llama_3_2_each_step · llama_3.2_1b-prompt_13_tokens_40",
    }
    assert three["series"] == {
        "krackan": "test_llama_3_2 · llama_3.2_3b-prompt_13_tokens_40",
        "phoenix": "TestEachStep::test_llama_3_2_each_step · llama_3.2_3b-prompt_13_tokens_40",
    }


def test_an_operator_s_trend_is_its_extensive_throughput_the_devices_share(tmp_path):
    for arch, npu, columns in (("krackan", "npu2", 8), ("phoenix", "npu1", 4)):
        own = f"{npu}-GEMV-M_2048-K_8192-num_aie_columns_{columns}"
        shared = f"{npu}-GEMV-M_1-K_1"
        _write(
            tmp_path / arch / "small" / "all.csv",
            [_row(NIGHTS[1], GEMV, own, Latency=10.0, Throughput=5.0)],
        )
        _write(
            tmp_path / arch / "extensive" / "all.csv",
            [
                _row(night, GEMV, own, Latency=10.0, Bandwidth=2.0, Throughput=5.0)
                for night in NIGHTS
            ]
            + [_row(NIGHTS[1], GEMV, shared, Latency=1.0, Throughput=1.0)],
        )

    (trend,) = _page_data(tmp_path)["trends"]
    assert (trend["title"], trend["group"]) == ("GEMV", "Operators")
    assert (trend["suite"], trend["metric"], trend["also"]) == (
        "extensive",
        "Throughput",
        None,
    )
    assert trend["series"] == {"krackan": "M_1-K_1", "phoenix": "M_1-K_1"}


def test_a_benchmark_no_longer_run_has_no_trend(tmp_path):
    _write(
        tmp_path / "krackan" / "small" / "all.csv",
        [
            _row(NIGHTS[0], "iron/operators/gemv/test.py::test_gemv", "M_1", Latency=1),
            _row(NIGHTS[1], GEMV, "npu2-GEMV-M_2048", Latency=1.0),
        ],
    )
    assert [t["benchmark"] for t in _page_data(tmp_path)["trends"]] == ["GEMV"]


def test_both_devices_trend_the_same_shared_parametrization(tmp_path):
    nights = NIGHTS + ["2026-10-03 10:00:00"]
    for arch, npu, longer in (
        ("krackan", "npu2", "M_2048"),
        ("phoenix", "npu1", "M_4096"),
    ):
        _write(
            tmp_path / arch / "extensive" / "all.csv",
            [
                _row(night, GEMV, f"{npu}-GEMV-{m}-K_8192", Throughput=1.0)
                for m in ("M_2048", "M_4096")
                for night in (nights if m == longer else nights[-1:])
            ],
        )

    (trend,) = _page_data(tmp_path)["trends"]
    assert trend["series"] == {"krackan": "M_2048", "phoenix": "M_2048"}
