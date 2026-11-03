# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.tune.measure``'s device lock, its cache and the pairing of a setting with its default, device-free."""

import json
import subprocess
import sys

import numpy as np

from iron.operators.silu import SiLU
from iron.tune.measure import Cache, Measurement, NpuLock, standard_error


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
