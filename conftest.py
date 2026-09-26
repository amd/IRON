# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import csv
import re
import subprocess
from datetime import datetime
from pathlib import Path
import pytest
import statistics

from iron.common import harness
import aie.utils as aie_utils
from aie.utils.benchmark import preflight, provenance
from aie.utils.probe import npu_unavailable_reason


@pytest.fixture
def npu_runtime():
    """Release the loaded NPU runtime after a test that ran on hardware.

    ``DefaultNPURuntime`` is None until something loads an image, so a test
    that only compiled has nothing to release, and must not be reported as
    an error for it.
    """
    yield
    if aie_utils.DefaultNPURuntime is not None:
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

    def add_result(self, test_path, test_name, passed, metrics):
        key = (test_path, test_name)
        self.test_metrics.setdefault(key, {}).setdefault("passed", []).append(passed)
        for metric_name, value in metrics:
            self.test_metrics[key].setdefault(metric_name, []).append(value)

    def finalize_results(self):
        """Compute statistics for all collected metrics"""
        # The commit alone does not say which toolchain and kernel sources
        # produced a number; mlir-aie's provenance line does. Only a run that
        # measured something has used the NPU, so only then is it described:
        # opening it otherwise would contend for the single-tenant device.
        measured = any(len(data) > 1 for data in self.test_metrics.values())
        if measured and aie_utils.DefaultNPURuntime is not None:
            npu = preflight()
            source = provenance(device=npu.device, pmode=npu.pmode)
        else:
            source = provenance()
        for (test_path, test_name), data in self.test_metrics.items():
            row = {
                "Commit": self.commit,
                "Date": self.date,
                "Provenance": source,
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


# Hook into test completion to collect each test's metrics into the CSVReporter
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
            if nodeid_components:
                test_path = nodeid_components.group(1)
                test_name = nodeid_components.group(3)
            else:
                # A test with no parameters carries no [...] suffix, so won't
                # match the regex above.
                test_path = item.nodeid
                test_name = item.nodeid.rsplit("::", 1)[-1]

            passed = report.outcome == "passed"
            # What the test reported through harness.record_metric (run_test
            # records latency and bandwidth; a test adds its own, e.g. throughput).
            csv_reporter.add_result(
                test_path, test_name, passed, harness.take_metrics()
            )


def pytest_configure(config):
    csv_path = config.getoption("--csv-output")
    config._csv_reporter = CSVReporter(csv_path)


def pytest_collection_modifyitems(config, items):
    marked_items = [
        (item, item.get_closest_marker("supported_devices")) for item in items
    ]
    marked_items = [(item, marker) for item, marker in marked_items if marker]
    if not marked_items:
        # Nothing collected needs the NPU. Resolving one here would open the
        # single-tenant device at collection time, contending with whatever
        # else holds it and erroring out when none is attached.
        return

    if aie_utils.DefaultNPURuntime is None:
        # A host without an NPU runs everything else: the device tests are
        # skipped, each saying why (most often no NPU, or an unsourced XRT,
        # which would otherwise look like a pile of toolchain regressions).
        reason = f"No NPU runtime: {npu_unavailable_reason()}"
        for item, _ in marked_items:
            item.add_marker(pytest.mark.skip(reason=reason))
        return
    device = aie_utils.DefaultNPURuntime.device().resolve().name
    for item, marker in marked_items:
        if device not in marker.args:
            item.add_marker(
                pytest.mark.skip(
                    reason=f"Not supported on {device} (supported: {', '.join(marker.args)})"
                )
            )


def pytest_sessionfinish(session, exitstatus):
    if hasattr(session.config, "_csv_reporter"):
        session.config._csv_reporter.finalize_results()
        session.config._csv_reporter.write_csv()


def pytest_generate_tests(metafunc):
    """Repeat each device test ``--iterations`` times for statistics.

    A test that measures takes the ``npu_runtime`` fixture; the rest of the
    tree runs once, since a repeat of a device-free test records nothing.
    """
    iterations = metafunc.config.getoption("--iterations")

    if iterations > 1 and "npu_runtime" in metafunc.fixturenames:
        metafunc.fixturenames.append("_iteration")
        metafunc.parametrize("_iteration", range(iterations), ids=lambda i: f"iter{i}")


def pytest_make_parametrize_id(config, val, argname):
    # Required: pytest_runtest_makereport parses test IDs with format "{argname}_{val}" for CSV reporting.
    return f"{argname}_{val}"
