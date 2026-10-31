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

import iron
from iron import Profile
from iron.operators import ElementwiseAdd
from iron.operators.copy import Copy
from iron.tests.support.graphs import Chain
from iron.tune.autotune import Shape, Timed, autotune, time_shape
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
    tuned_graph = Chain(SIZE, TILE)
    tuned_graph.profile = profile
    tuned = tuned_graph.compile(full_elf=True, a=(SIZE,), b=(SIZE,))
    plain = Chain(SIZE, TILE).compile(full_elf=True, a=(SIZE,), b=(SIZE,))
    rng = np.random.default_rng(0)
    a = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    b = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    want = np.array(plain(a, b).numpy()[:SIZE])
    got = np.array(tuned(a, b).numpy()[:SIZE])
    assert want.view(np.uint16).tolist() == got.view(np.uint16).tolist()


@pytest.mark.supported_devices("npu1", "npu2")
def test_a_tuned_copy_of_a_slice_is_saved(tmp_path):
    """A Copy reading part of a buffer names an access pattern among its
    dimensions, which a profile cannot write: its entry names the rest."""

    class Rows(iron.Graph):
        def body(self, x):
            return Copy.step(Copy.step(x)[:2])

    dev = aie_utils.ensure_current_device()
    report = platform()
    profile = autotune(
        [Timed(Rows().record(x=(64, 2048)))],
        dev,
        full_elf=dev.can_dispatch_full_elf,
        timing=Timing(rounds=2, calls=5),
        cache=Cache(report["Name"], report["Power Mode"], root=tmp_path / "c"),
        log=lambda _: None,
    )
    path = tmp_path / f"{dev.name}.json"
    profile.save(path)
    assert len(Profile.load(path)) == len(profile) > 0


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


def test_a_setting_cached_as_the_default_is_judged_against_the_next_one(tmp_path):
    # Given four columns, the first search records (4 columns, its channels)
    # as its default; given those channels, the second searches the columns
    # from its own recorded width and meets four columns in the cache.
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    first = ElementwiseAdd(size=SIZE, tile_size=TILE, num_aie_columns=4)
    channels = first.resolved(dev).num_channels
    trials = []
    for op in (first, ElementwiseAdd(size=SIZE, tile_size=TILE, num_channels=channels)):
        shape = Shape(op)
        shape.members.append((op, [(1.0, {})], {}))
        trials = time_shape(
            shape,
            dev,
            full_elf=True,
            timing=Timing(rounds=2, calls=5),
            cache=cache,
            log=lambda _: None,
        )
    four = [t for t in trials if t.tunables.get("num_aie_columns") == 4]
    assert four and all(np.isfinite(t.delta_us) for t in four)
