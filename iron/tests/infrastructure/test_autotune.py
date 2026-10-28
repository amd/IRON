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

from iron.tests.support.graphs import Chain
from iron.tune.autotune import Timed, autotune
from iron.tune.measure import Cache, Timing, platform

SIZE = 8192
TILE = 256

pytestmark = [pytest.mark.supported_devices("npu2"), pytest.mark.extensive]


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
    tuned = Chain(SIZE, TILE).compile(
        full_elf=True, profile=profile, a=(SIZE,), b=(SIZE,)
    )
    plain = Chain(SIZE, TILE).compile(full_elf=True, a=(SIZE,), b=(SIZE,))
    rng = np.random.default_rng(0)
    a = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    b = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    want = np.array(plain(a, b).numpy()[:SIZE])
    got = np.array(tuned(a, b).numpy()[:SIZE])
    assert want.view(np.uint16).tolist() == got.view(np.uint16).tolist()


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
