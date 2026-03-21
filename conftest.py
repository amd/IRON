# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import csv
import re
import subprocess
from datetime import datetime
from pathlib import Path
import pytest
import sys
import statistics

# Check if AIE toolchain is available (only on Linux with NPU hardware)
AIE_TOOLCHAIN_AVAILABLE = False
AIE_TOOLCHAIN_ERROR = None
try:
    from iron.common import AIEContext
    from iron.common.aie_device_manager import (
        AIE_TOOLCHAIN_AVAILABLE as TOOLCHAIN_AVAILABLE,
    )

    AIE_TOOLCHAIN_AVAILABLE = TOOLCHAIN_AVAILABLE
except ImportError as e:
    AIE_TOOLCHAIN_ERROR = str(e)
    AIEContext = None  # type: ignore

# Skip marker for hardware-dependent tests
skip_if_no_aie = pytest.mark.skipif(
    not AIE_TOOLCHAIN_AVAILABLE,
    reason=f"AIE toolchain not available: {AIE_TOOLCHAIN_ERROR}",
)


@pytest.fixture
def aie_context(request):
    """Create a fresh AIEContext for each test.

    Tests using this fixture will be automatically skipped if the AIE
    toolchain is not available (Windows or Linux without NPU hardware).
    """
    if not AIE_TOOLCHAIN_AVAILABLE:
        raise pytest.skip(
            "AIE toolchain not available - requires Linux with AMD XRT drivers and NPU hardware"
        )
    verbose_mlir = request.config.option.verbose > 0
    return AIEContext(mlir_verbose=verbose_mlir)


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

    def add_result(self, test_name, passed, captured_output, metric_patterns):
        self.test_metrics.setdefault(test_name, {}).setdefault("passed", []).append(
            passed
        )

        for metric_name, pattern in metric_patterns.items():
            match = re.search(pattern, captured_output)
            if not match:
                continue
            value = float(match.group("value"))
            self.test_metrics[test_name].setdefault(metric_name, []).append(value)

    def finalize_results(self):
        """Compute statistics for all collected metrics"""
        for test_name, data in self.test_metrics.items():
            row = {
                "Commit": self.commit,
                "Date": self.date,
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
        self.results.sort(key=lambda x: (x["Test"], x["Date"]))

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
            # Extract only the stem out of that.
            nodeid_components = re.match(
                r"^(.+?)::(.+?)\[(iter\d+-)?(.+?)\]$", item.nodeid
            )
            if not nodeid_components:
                raise RuntimeError(f"Unexpected test nodeid format: {item.nodeid}")
            test_name = nodeid_components.group(4)

            passed = report.outcome == "passed"
            captured = report.capstdout

            # Get metric patterns from test item's markers
            metric_patterns = {}
            for marker in item.iter_markers("metrics"):
                metric_patterns = marker.kwargs
                break

            csv_reporter.add_result(test_name, passed, captured, metric_patterns)


def pytest_configure(config):
    csv_path = config.getoption("--csv-output")
    config._csv_reporter = CSVReporter(csv_path)
    config.addinivalue_line(
        "markers", "metrics(**patterns): specify metric patterns for this test"
    )
    config.addinivalue_line(
        "markers",
        "skip_if_no_aie: skip test if AIE toolchain is not available (Linux NPU hardware required)",
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
