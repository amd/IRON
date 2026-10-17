# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""run_test's timing (S3: --iterations and the repeated-process sampling it
drove are gone; run_test(timed_iters=20) records the median and median
absolute deviation of its own 20 timed runs instead). The statistics
themselves are mlir-aie's (``aie.utils.benchmark.run_iters``), over NPU
times a real callable reports; this checks that pipeline, device-free, on
timed samples whose median and MAD are known, against numpy's.
"""

from types import SimpleNamespace

import numpy as np
from aie.utils.benchmark import run_iters

# 20 NPU times (ns), as run_test's default timed_iters draws: mostly near
# 1000ns with one outlier, so the median and MAD differ from the mean.
SAMPLES_NS = [
    1000.0,
    1200.0,
    980.0,
    1050.0,
    5000.0,
    1010.0,
    990.0,
    1030.0,
    1005.0,
    995.0,
    1015.0,
    1025.0,
    975.0,
    1040.0,
    960.0,
    1060.0,
    1000.0,
    1020.0,
    985.0,
    1035.0,
]


def test_run_tests_timed_samples_give_numpys_median_and_mad():
    samples = iter(SAMPLES_NS)

    def fn():
        # The ``(handle, KernelResult)`` shape run_test's compiled callable
        # returns; only ``npu_time`` (ns) matters to run_iters.
        return None, SimpleNamespace(npu_time=next(samples))

    benchmark = run_iters(fn, iters=len(SAMPLES_NS))

    samples_us = np.asarray(SAMPLES_NS, dtype=np.float64) / 1000.0
    expected_median = np.median(samples_us)
    expected_mad = np.median(np.abs(samples_us - expected_median))
    assert benchmark.npu.median_us == expected_median
    assert benchmark.npu.mad_us == expected_mad
    assert benchmark.npu.n == len(SAMPLES_NS)
