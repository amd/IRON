# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import csv
import re
import subprocess
from datetime import datetime
from pathlib import Path
import pytest
import sys
import statistics

from iron.common import AIEContext
import aie.utils as aie_utils


@pytest.fixture
def aie_context(request):
    """Create a fresh AIEContext for each test"""
    verbose_mlir = request.config.option.verbose > 0
    compiler = request.config.getoption("--compiler", default="peano")
    ctx = AIEContext(mlir_verbose=verbose_mlir, compiler=compiler)
    yield ctx
    aie_utils.DefaultNPURuntime.cleanup()


def pytest_addoption(parser):
    parser.addoption(
        "--csv-output",
        default="tests_latest.csv",
        help="Output CSV file for test metrics",
    )
    parser.addoption(
        "--iterations",
        type=int,
        default=5,
        help="Number of iterations to run each test for statistics",
    )
    parser.addoption(
        "--compiler",
        default="peano",
        choices=["peano", "chess"],
        help="Kernel compiler: 'peano' (default) or 'chess' (requires Vitis/aietools)",
    )


def get_git_commit():
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        return "unknown"


class CSVReporter:
    """Capture metrics of test runs and write to a CSV file"""

    def __init__(self, csv_path):
        self.csv_path = Path(csv_path)
        self.results = []
        self.commit = get_git_commit()
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.test_metrics = {}  # test_name -> {metric_name -> [values]}

    def add_result(
        self, test_path, test_name, passed, captured_output, metric_patterns
    ):
        key = (test_path, test_name)
        self.test_metrics.setdefault(key, {}).setdefault("passed", []).append(passed)

        for metric_name, pattern in metric_patterns.items():
            match = re.search(pattern, captured_output)
            if not match:
                continue
            value = float(match.group("value"))
            self.test_metrics[key].setdefault(metric_name, []).append(value)

    def finalize_results(self):
        """Compute statistics for all collected metrics"""
        for (test_path, test_name), data in self.test_metrics.items():
            row = {
                "Commit": self.commit,
                "Date": self.date,
                "Test Path": test_path,
                "Test": test_name,
                "Checks": f"{sum(data['passed'])}/{len(data['passed'])}",
            }
            for metric_name, values in data.items():
                if metric_name == "passed":
                    continue
                if values:
                    row[f"{metric_name} (mean)"] = statistics.mean(values)
                    row[f"{metric_name} (median)"] = statistics.median(values)
                    row[f"{metric_name} (min)"] = min(values)
                    row[f"{metric_name} (max)"] = max(values)
                    row[f"{metric_name} (stddev)"] = (
                        statistics.stdev(values) if len(values) > 1 else 0.0
                    )
            self.results.append(row)

    def write_csv(self):
        self.results.sort(key=lambda x: (x.get("Test Path", ""), x["Test"], x["Date"]))

        cols = {}
        for row in self.results:
            cols.update({k: None for k in row.keys()})

        self.csv_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, cols.keys())
            writer.writeheader()
            writer.writerows(self.results)


# Initialize the CSV writer once at test session setup
@pytest.fixture(scope="session")
def csv_reporter(request):
    csv_path = request.config.getoption("--csv-output")
    reporter = CSVReporter(csv_path)
    yield reporter
    reporter.write_csv()


# Hook into test completion to capture metrics in CSVReporter
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        csv_reporter = item.session.config._csv_reporter
        if csv_reporter:
            # The pytest nodeid looks like this:
            # iron/operators/dequant/test.py::test_dequant[iter0-dequant_8_cols_2_channels_2048_tile_128]
            # Split into:
            #   test_path: iron/operators/dequant/test.py::test_dequant
            #   test_name: just the parametrize id (without iter prefix)
            nodeid_components = re.match(
                r"^(.+?::[^\[]+)\[(iter\d+-)?(.+?)\]$", item.nodeid
            )
            if not nodeid_components:
                raise RuntimeError(f"Unexpected test nodeid format: {item.nodeid}")
            test_path = nodeid_components.group(1)
            test_name = nodeid_components.group(3)

            passed = report.outcome == "passed"
            captured = report.capstdout

            # Get metric patterns from test item's markers
            metric_patterns = {}
            for marker in item.iter_markers("metrics"):
                metric_patterns = marker.kwargs
                break

            csv_reporter.add_result(
                test_path, test_name, passed, captured, metric_patterns
            )


def pytest_configure(config):
    csv_path = config.getoption("--csv-output")
    config._csv_reporter = CSVReporter(csv_path)
    config.addinivalue_line(
        "markers", "metrics(**patterns): specify metric patterns for this test"
    )


def pytest_collection_modifyitems(config, items):
    device = aie_utils.DefaultNPURuntime.device().resolve().name
    for item in items:
        marker = item.get_closest_marker("supported_devices")
        if marker and device not in marker.args:
            item.add_marker(
                pytest.mark.skip(
                    reason=f"Not supported on {device} (supported: {', '.join(marker.args)})"
                )
            )


def pytest_sessionfinish(session, exitstatus):
    if hasattr(session.config, "_csv_reporter"):
        session.config._csv_reporter.finalize_results()
        session.config._csv_reporter.write_csv()


# Generate multiple iterations of each test
def pytest_generate_tests(metafunc):
    """Generate multiple iterations of each test for statistics gathering"""
    iterations = metafunc.config.getoption("--iterations")

    if iterations > 1:
        metafunc.fixturenames.append("_iteration")
        metafunc.parametrize("_iteration", range(iterations), ids=lambda i: f"iter{i}")


def pytest_make_parametrize_id(config, val, argname):
    # Required: pytest_runtest_makereport parses test IDs with format "{argname}_{val}" for CSV reporting.
    return f"{argname}_{val}"
