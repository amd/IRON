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
from iron.tune.plan import coded_seed, searches
from iron.tune.survey import Design, Estimate, Survey

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

    def body(self, x, half, quarter):
        # A batch of one, as a decoder's calls give it: num_matrices is left
        # to GEMV, so an entry naming it would never match these calls.
        return (
            GEMV.step(self.wide, x, tile_size_input=4, num_batches=1),
            GEMV.step(self.square, x, tile_size_input=4, num_batches=1),
            GEMV.step(self.narrow, half, tile_size_input=4, num_batches=1),
            GEMV.step(SiLU.step(self.act), quarter, tile_size_input=4, num_batches=1),
        )


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
        return [Timed(graph.record(x=(1, E), half=(1, E // 2), quarter=(1, E // 4)))]

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


def test_a_seeded_shape_records_coded():
    """The seed's entries match the calls that made them: a GEMV call
    leaves ``num_matrices`` to its operator, so an entry naming it would
    never apply."""
    record = recorder("none")
    seed = coded_seed(record, aie_utils.ensure_current_device(), Profile())
    [call] = record(seed)
    flags = {
        (s.op.M, s.op.K): s.op.coded_a
        for s in call.recording.steps
        if isinstance(s.op, GEMV)
    }
    assert flags == {
        (2 * E, E): True,
        (E, E): True,
        (E, E // 2): True,
        (E // 4, E // 4): False,
    }


def surveyed(steps_us: float, switch_us: float, fold_us: float) -> Survey:
    design = Design("GEMV M=2048 K=2048", "gemv", 1, steps_us, 0, None, "other")
    estimates = {
        "packing": Estimate(switch_us, "switches"),
        "folds": Estimate(fold_us, "steps"),
        "coded": Estimate(0.0, "none"),
    }
    return Survey("v", (design,), 10, switch_us, estimates)


def test_a_full_elf_packs_where_switches_weigh_and_never_prices_fusions():
    plan = {s.name: s.runs for s in searches([surveyed(1000, 100, 1)], True)}
    assert plan == {"packing": True, "folds": False, "fusions": False}
    plan = {s.name: s.runs for s in searches([surveyed(1000, 10, 20)], True)}
    assert plan == {"packing": False, "folds": True, "fusions": False}
    plan = {s.name: s.runs for s in searches([surveyed(10**7, 10, 2000)], True)}
    assert plan == {"packing": False, "folds": True, "fusions": False}


def test_an_xclbin_per_step_packs_nothing_and_prices_merges():
    plan = {s.name: s.runs for s in searches([surveyed(1000, 100, 1)], False)}
    assert plan == {"packing": False, "folds": False, "fusions": True}
