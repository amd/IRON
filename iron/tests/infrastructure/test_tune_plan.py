# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a tune decides before it searches (``iron.tune.plan``): which
weights it codes, an array at a time. No device, no toolchain.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU
from iron.tune.autotune import Timed, shapes
from iron.tune.plan import coded_seed

pytestmark = pytest.mark.usefixtures("npu2")

E = 2048


class Projections(iron.Graph):
    """``wide`` (2E x E) and ``square`` (E x E) share one array (their K);
    ``narrow`` (E x E/2) runs on its own, and so does the last GEMV, whose
    A is an activation."""

    def __init__(self, wide, square, narrow, act):
        self.wide = iron.param(wide)
        self.square = iron.param(square)
        self.narrow = iron.param(narrow)
        self.act = iron.param(act)

    def body(self, x):
        y = GEMV.step(self.wide, x, tile_size_input=4)
        z = GEMV.step(self.square, y[:E], tile_size_input=4)
        n = GEMV.step(self.narrow, z[: E // 2], tile_size_input=4)
        return GEMV.step(SiLU.step(self.act), n[: E // 4], tile_size_input=4)


def weights(spread: str) -> tuple[np.ndarray, ...]:
    """Normal weights, ``square`` drawn over 2^-60..2^60 where ``spread``
    says so: too many exceptions for a coded row."""
    rng = np.random.default_rng(0)
    wide = (rng.standard_normal((2 * E, E)) * 0.05).astype(bfloat16)
    square = (rng.standard_normal((E, E)) * 0.05).astype(bfloat16)
    narrow = (rng.standard_normal((E, E // 2)) * 0.05).astype(bfloat16)
    act = (rng.standard_normal((E // 4, E // 4)) * 0.05).astype(bfloat16)
    if spread == "square":
        square = np.exp2(rng.integers(-60, 60, (E, E))).astype(bfloat16)
    return wide, square, narrow, act


def recorder(spread: str):
    graph = Projections(*weights(spread))

    def record(profile: Profile) -> list[Timed]:
        graph.profile = profile
        return [Timed(graph.record(x=(E,)))]

    return record


def coded(profile: Profile) -> dict[tuple[int, int], bool]:
    """Each GEMV entry's (M, K) and its ``coded_a``."""
    return {(d["M"], d["K"]): t["coded_a"] for c, d, t in profile if c is GEMV}


def test_every_array_whose_weights_fit_is_coded_and_the_activation_is_not():
    seed = coded_seed(recorder("none"), aie_utils.ensure_current_device(), Profile())
    assert coded(seed) == {(2 * E, E): True, (E, E): True, (E, E // 2): True}


def test_a_weight_past_capacity_keeps_its_whole_array_plain():
    """``square`` refuses its rows; ``wide`` shares its array, so it stays
    plain too; ``narrow``'s array is coded alone."""
    seed = coded_seed(recorder("square"), aie_utils.ensure_current_device(), Profile())
    assert coded(seed) == {(E, E // 2): True}


def test_the_search_holds_a_coding_tunable_where_the_seed_set_it():
    record = recorder("none")
    dev = aie_utils.ensure_current_device()
    seed = coded_seed(record, dev, Profile())
    for shape in shapes(record(seed), dev):
        if shape.cls is GEMV:
            assert "coded_a" in shape.pinned
