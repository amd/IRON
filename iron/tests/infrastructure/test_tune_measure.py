# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.tune.measure``'s device lock, its cache and the pairing of a setting with its default, device-free."""

import json
import subprocess
import sys

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.common.image.callable import WAIT_PER_DISPATCH_US
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.silu import SiLU
from iron.tests.support.graphs import Adds
from iron.tune.measure import (
    Cache,
    Measurement,
    NpuLock,
    Timing,
    standard_error,
    time_interleaved,
)


def test_npu_lock_keeps_another_process_out_until_its_outermost_exit(tmp_path):
    path = tmp_path / "npu.lock"
    probe = [
        sys.executable,
        "-c",
        "import fcntl\n"
        f"f = open({str(path)!r}, 'a+')\n"
        "fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)",
    ]
    lock = NpuLock(path)
    with lock:
        with lock:
            assert lock.depth == 2
        held = subprocess.run(probe, capture_output=True).returncode
    released = subprocess.run(probe, capture_output=True).returncode
    assert held != 0 and released == 0
    assert lock.depth == 0 and lock.file is None


def test_a_setting_pairs_with_the_default_timed_in_its_own_batch():
    """Another batch's default, timed later on a drifted clock, does not enter its delta."""
    rounds = np.array([101.0, 103.0, 102.0, 104.0])
    beside = np.array([100.0, 101.0, 101.5, 102.0])
    setting = Measurement(
        float(np.median(rounds)), tuple(rounds), "o", "first", "p", 50, tuple(beside)
    )
    last_default = Measurement(
        200.0, (199.0, 200.0, 201.0, 202.0), "o", "last", "p", 50
    )
    delta, noise = setting.against_default(last_default)
    assert delta == np.median(rounds) - np.median(beside)
    assert noise == standard_error(list(rounds - beside))


def test_a_figure_with_no_default_beside_it_pairs_with_the_given_one():
    own = Measurement(5.0, (4.0, 5.0, 6.0), "o", "a", "p", 50)
    default = Measurement(3.0, (3.0, 3.5, 2.5), "o", "b", "p", 50)
    assert own.against_default(default) == own.difference(default)


def test_a_cached_measurement_names_the_operator_it_timed(tmp_path, npu2):
    cache = Cache("Test NPU", "default", root=tmp_path)
    m = Measurement(3.0, (2.9, 3.1), "abc", "run", "default", 50)
    op = SiLU(size=2048, tile_size=256, num_aie_columns=2).resolved()
    cache.put("k", m, op)
    assert cache.get("k") == m
    (path,) = tmp_path.rglob("k.json")
    named = json.loads(path.read_text())["op"]
    assert named["class"] == "SiLU" and "tile_size" in named["tunables"]
    assert named["params"]["size"] == 2048 and named["params"]["tile_size"] == 256
    cache.put("plain", m)
    assert cache.get("plain") == m


@pytest.mark.supported_devices("npu1", "npu2")
def test_a_per_step_call_is_timed_with_a_cpu_wait_cap_its_dispatches_earn():
    x, w = (np.full(1024, v, bfloat16) for v in (1.0, 0.5))
    graph = Adds(ElementwiseAdd(size=1024, tile_size=128), 64)
    per_step = graph.compile(full_elf=False, x=(1024,), w=(1024,))
    whole = graph.compile(full_elf=True, x=(1024,), w=(1024,))
    assert per_step.callable.dispatches == 64 and whole.callable.dispatches == 1
    extra = per_step.callable.cpu_wait_cap_us() - whole.callable.cpu_wait_cap_us()
    assert extra == 63 * WAIT_PER_DISPATCH_US
    expected = (x.astype(np.float32) + 64 * 0.5).astype(bfloat16)
    assert np.array_equal(np.asarray(per_step(x, w)), expected)
    (stats,) = time_interleaved([per_step.callable], Timing(rounds=2, calls=5), log=lambda _: None)
    assert stats.median_us > 0
