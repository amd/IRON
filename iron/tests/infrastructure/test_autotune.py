# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Autotuning on the NPU, end to end: an operator timed from the command
line, and a tuned profile a graph then runs bit-identically with.
"""

import os
import subprocess
import sys

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.common.declare import Profile
from iron.tests.support.graphs import Chain
from iron.tune.autotune import Timed, autotune, shapes
from iron.tune.measure import Cache, Timing, platform

SIZE = 8192
TILE = 256


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_a_tuned_profile_runs_bit_identically(tmp_path):
    recording = Chain(SIZE, TILE).record(a=(SIZE,), b=(SIZE,))
    report = platform()
    profile = autotune(
        [Timed(recording)],
        aie_utils.ensure_current_device(),
        full_elf=True,
        timing=Timing(rounds=2, calls=10),
        cache=Cache(report["Name"], report["Power Mode"], root=tmp_path / "c"),
        log=lambda _: None,
    )
    assert len(profile)
    graph = Chain(SIZE, TILE)
    graph.profile = profile
    tuned = graph.compile(full_elf=True, a=(SIZE,), b=(SIZE,))
    plain = Chain(SIZE, TILE).compile(full_elf=True, a=(SIZE,), b=(SIZE,))
    rng = np.random.default_rng(0)
    a = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    b = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    want = np.array(plain(a, b).numpy()[:SIZE])
    got = np.array(tuned(a, b).numpy()[:SIZE])
    assert want.view(np.uint16).tolist() == got.view(np.uint16).tolist()


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_one_operator_is_timed_from_the_command_line(tmp_path):
    run = subprocess.run(
        [
            sys.executable,
            "-m",
            "iron.tune.cli",
            "ElementwiseAdd",
            f"size={SIZE}",
            f"tile_size={TILE}",
            "--rounds=1",
            "--calls=5",
        ],
        env=os.environ | {"NPU_CACHE_HOME": str(tmp_path / "cache")},
        capture_output=True,
        text=True,
    )
    assert run.returncode == 0, run.stderr
    printed = [line for line in run.stdout.splitlines() if " us" in line]
    assert len(printed) > 1
    assert sum("(recorded)" in line for line in printed) == 1


def test_autotune_resumes_a_profile_s_finished_shapes(npu2, tmp_path):
    """A profile already naming every tunable a shape searches is reused
    rather than timed again, so a killed run's own saved profile (``path``)
    resumes from what it already finished: device-free, since no ``cache``
    is given here, a shape that fell through to ``time_shape`` would have to
    build and dispatch for real to be timed at all.
    """
    recording = Chain(SIZE, TILE).record(a=(SIZE,), b=(SIZE,))
    found = shapes([Timed(recording)], npu2)
    assert found
    prior = Profile()
    for shape in found:
        resolved = shape.members[0][0].resolved(npu2)
        tunables = {n: vars(resolved)[n] for n in resolved.declaration.tunables}
        prior.add(shape.cls, **shape.named(()), **tunables)
    path = tmp_path / "npu2.json"
    logged = []
    tuned = autotune(
        [Timed(recording)],
        npu2,
        prior,
        full_elf=True,
        path=path,
        log=logged.append,
    )
    assert len(tuned) == len(prior)
    # time_shape logs "[i/n] <shape>" for one it actually times; none here.
    assert not any(line.startswith("[") for line in logged)
    # Saved after each shape resumed, same as one actually timed.
    assert len(Profile.load(path)) == len(prior)
