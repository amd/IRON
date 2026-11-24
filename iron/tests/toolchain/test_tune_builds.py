# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The builds a tune times (``iron.tune.fusions.built``) and compares, each device's, compiled without one."""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile
from iron.operators.gemv import GEMV
from iron.operators.relu import ReLU
from iron.tests.support.tools import requires
from iron.tune.autotune import Timed
from iron.tune.fusions import Applied, compare_graphs
from iron.tune.measure import Timing
from iron.tune.plan import coded_seed

pytestmark = requires("xclbinutil", "peano")

E = 512


class Projection(iron.Graph):
    def __init__(self, w):
        self.w = iron.param(w)

    def body(self, x):
        return GEMV.step(self.w, x, tile_size_input=4, num_batches=1)


class Rectify(iron.Graph):
    def body(self, x):
        return ReLU.step(x, num_aie_columns=1)


def test_a_tuned_build_holds_a_coded_weight_coded_only(device):
    """``w``'s plain bf16 copy, which no step of the coded build reads, is not laid out (nor uploaded) beside its coded rows."""
    rng = np.random.default_rng(0)
    graph = Projection((rng.standard_normal((E, E)) * 0.05).astype(bfloat16))

    def record(profile: Profile) -> list[Timed]:
        graph.profile = profile
        return [Timed(graph.record(x=(1, E)))]

    seed = coded_seed(record, device, Profile())
    [call] = record(seed)
    layout = Applied.of(call, seed, device).built(device).sequence.layout
    assert {"w", "w.coded"} & layout.keys() == {"w.coded"}


def test_compare_graphs_names_the_input_two_builds_take_differently(device):
    call = Timed(Rectify().record(x=(4096,)))
    other = Timed(Rectify().record(x=(8192,)))
    before = Applied.of(call, Profile(), device).built(device)
    after = Applied.of(other, Profile(), device).built(device)
    with pytest.raises(ValueError, match=r"after .*'input 0', \(4096,\).*\(8192,\)"):
        compare_graphs(call, before, after, timing=Timing(rounds=1, calls=1))
