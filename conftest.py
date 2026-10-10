# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import csv
import numbers
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path
import pytest
import statistics

import aie.utils as aie_utils
from aie.iron.device import from_name
from aie.utils.benchmark import preflight, provenance
from aie.utils.probe import npu_unavailable_reason
from aie.utils.trace import TraceConfig


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


def _bound_device(name: str, n_cols: int):
    """A fixture binding an ``n_cols``-column ``name`` NPU as the current
    device, the previous one restored after: what a test that resolves or
    compiles device-free needs.
    """

    def bound():
        previous = aie_utils.get_current_device()
        device = from_name(name, n_cols=n_cols)
        aie_utils.set_current_device(device)
        yield device
        aie_utils.set_current_device(previous)

    return pytest.fixture(bound, name=name)


npu2 = _bound_device("npu2", 8)
npu1 = _bound_device("npu1", 4)


@pytest.fixture
def trace(request, tmp_path):
    """The trace a run asks for, or None: ``IRON_TRACE_SIZE`` bytes of trace
    buffer, written to a file named after the test in ``IRON_TRACE_DIR``
    (the test's ``tmp_path`` unless set).
    """
    size = int(os.environ.get("IRON_TRACE_SIZE", "0"))
    if not size:
        return None
    directory = Path(os.environ.get("IRON_TRACE_DIR", tmp_path))
    name = re.sub(r"[^\w.-]", "_", request.node.name)
    return TraceConfig(size, trace_file=str(directory / f"{name}.txt"))


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
        "--cost-table",
        type=Path,
        default=None,
        help="Fold, narrow and pack a language model's versions by this "
        "measured cost table (iron.lm.tune)",
    )
    parser.addoption(
        "--random-weights",
        type=int,
        default=None,
        metavar="SEED",
        help="Run a language model's tests on weights drawn at SEED and random "
        "prompts, in place of its checkpoint and tokenizer",
    )
    parser.addoption(
        "--max-seq-len",
        type=int,
        default=None,
        help="The rows a language model's caches hold, in place of its config's",
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
        self.bench = {}  # test_name -> bool
        self.unmeasured = set()  # (test_path, test_name) a pass recorded nothing

    def add_result(self, test_path, test_name, passed, metrics, bench):
        key = (test_path, test_name)
        self.test_metrics.setdefault(key, {}).setdefault("passed", []).append(passed)
        self.bench[key] = bench
        if passed and not metrics:
            self.unmeasured.add(key)
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
                "Bench": "yes" if self.bench.get((test_path, test_name)) else "no",
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

    def report_unmeasured(self):
        """Name the benched tests that passed without recording a metric.

        A benched test that records nothing leaves its columns empty, and an
        empty column drops out of the charts without any test failing.
        """
        return sorted(
            f"{path}[{name}]"
            for path, name in self.unmeasured
            if self.bench[path, name]
        )

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
            # The figures the test gave record_property (run_test's latency,
            # bandwidth and throughput; a test's own, e.g. TTFT).
            metrics = [
                (name, float(value))
                for name, value in item.user_properties
                if isinstance(value, numbers.Real)
            ]
            csv_reporter.add_result(
                test_path,
                test_name,
                passed,
                metrics,
                item.get_closest_marker("bench") is not None,
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
        reporter = session.config._csv_reporter
        reporter.finalize_results()
        reporter.write_csv()
        unmeasured = reporter.report_unmeasured()
        if unmeasured:
            reporter.csv_path.with_suffix(".unmatched").write_text(
                "\n".join(unmeasured) + "\n"
            )
            print(
                "\nBenched tests passed without recording a metric:\n  "
                + "\n  ".join(unmeasured)
            )


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
