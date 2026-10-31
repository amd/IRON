# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Autotuning on the NPU, end to end.

An operator timed from the command line, and a tuned profile a graph
then runs bit-identically with.
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
from iron.operators import ElementwiseAdd, SiLU
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
    """A Copy reading part of a buffer names an access pattern among its dimensions, which a profile cannot write.

    Its entry names the rest.
    """

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


@pytest.mark.supported_devices("npu1", "npu2")
def test_a_tuned_entry_names_no_dimension_a_host_sizes(tmp_path):
    """A model fitted to another host's context sizes its caches and attention otherwise (``Timed.varying``).

    An entry naming that dimension would match there no longer, so it is left out.
    """
    recording = Chain(SIZE, TILE).record(a=(SIZE,), b=(SIZE,))
    dev = aie_utils.ensure_current_device()
    [silu] = {
        Shape(s.op.resolved()).key for s in recording.steps if isinstance(s.op, SiLU)
    }
    report = platform()
    profile = autotune(
        [Timed(recording, varying={silu: frozenset({"size"})})],
        dev,
        full_elf=dev.can_dispatch_full_elf,
        timing=Timing(rounds=2, calls=5),
        cache=Cache(report["Name"], report["Power Mode"], root=tmp_path / "c"),
        log=lambda _: None,
    )
    named = {cls: dims for cls, dims, _ in profile}
    assert "size" not in named[SiLU]
    assert named[ElementwiseAdd]["size"] == SIZE


@pytest.mark.supported_devices("npu1", "npu2")
def test_an_entry_a_tune_only_outranks_still_serves_what_it_did_not_time(tmp_path):
    """A tune of one version (``--versions decode``) writes its shapes' own entries; a broader one they outrank still matches another version's shapes.

    Which keep what it gave them rather than their defaults.
    """
    recording = Chain(SIZE, TILE).record(a=(SIZE,), b=(SIZE,))
    dev = aie_utils.ensure_current_device()
    stock = Profile()
    stock.add(SiLU, tile_size=TILE)
    report = platform()
    profile = autotune(
        [Timed(recording)],
        dev,
        stock,
        full_elf=dev.can_dispatch_full_elf,
        timing=Timing(rounds=2, calls=5),
        cache=Cache(report["Name"], report["Power Mode"], root=tmp_path / "c"),
        log=lambda _: None,
    )
    assert profile.tunables_for(SiLU, {"size": 4 * SIZE}) == {"tile_size": TILE}


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


def test_only_a_shape_that_weighs_in_a_version_is_searched(tmp_path):
    """Given each shape's share of its version, a tune searches the shapes at ``SHAPE_SHARE`` or more and writes no entry for the rest."""
    recording = Chain(SIZE, TILE).record(a=(SIZE,), b=(SIZE,))
    dev = aie_utils.ensure_current_device()
    keys = {type(s.op): Shape(s.op).key for s in recording.steps}
    report = platform()
    profile = autotune(
        [Timed(recording)],
        dev,
        full_elf=True,
        timing=Timing(rounds=2, calls=10),
        cache=Cache(report["Name"], report["Power Mode"], root=tmp_path / "c"),
        shares={keys[SiLU]: 0.5, keys[ElementwiseAdd]: 0.001},
        log=lambda _: None,
    )
    assert {cls for cls, _, _ in profile} == {SiLU}
