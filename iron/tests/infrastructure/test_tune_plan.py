# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a tune decides before it searches (``iron.tune.plan``).

Which weights it codes, an array at a time. No device, no toolchain.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile, Scratchpad
from iron.common.graph.compiled import apply_profile
from iron.common.image.step import FusionKind
from iron.lm.tune import contexts
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU
from iron.tune.autotune import Timed, shapes
from iron.tune.plan import coded_seed, searches
from iron.tune.survey import Design, Estimate, Survey

pytestmark = pytest.mark.usefixtures("npu2")

E = 2048


class Projections(iron.Graph):
    """``wide`` (2E x E) and ``square`` (E x E) share one array (their K); ``narrow`` (E x E/2) runs on its own.

    And so does the last GEMV, whose A is an activation.
    """

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
    """Return the normal weights, ``square`` drawn over 2^-60..2^60 where ``spread`` says so.

    Too many exceptions for a coded row.
    """
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
    """``square`` refuses its rows; ``wide`` shares its array, so it stays plain too; ``narrow``'s array is coded alone."""
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
    """The seed's entries match the calls that made them.

    A GEMV call leaves ``num_matrices`` to its operator, so an entry naming it would
    never apply.
    """
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


def plain_packing() -> list:
    """``wide`` and ``square`` packed, each read plain there, as a profile tuned before coding gives them."""
    return [
        (GEMV, {"M": 2 * E, "K": E}, {"tile_size_input": 4, "coded_a": False}),
        (GEMV, {"M": E, "K": E}, {"tile_size_input": 4, "coded_a": False}),
    ]


def test_a_packed_step_reads_its_weight_as_recorded():
    """A packing giving ``coded_a=False`` to a shape its entry codes still reads the coded rows its slot holds, not as bf16."""
    record = recorder("none")
    dev = aie_utils.ensure_current_device()
    profile = coded_seed(record, dev, Profile())
    profile.add_packing(plain_packing())
    [call] = record(profile)
    call.recording.code_weights()
    recording, _, packing = apply_profile(call.recording, profile, dev)
    assert packing.groups
    weights = {h.ref().root for _, h in recording.weights.values()}
    reads = [
        (s.op.M, s.op.K, slot.name, np.dtype(b.host_dtype), np.dtype(slot.dtype))
        for s in recording.steps
        if isinstance(s.op, GEMV)
        for b, slot in zip(s.op.buffers, s.slots)
        if slot.ref().root in weights
    ]
    assert [r for r in reads if r[3] != r[4]] == []
    assert {(r[0], r[1]): r[3] for r in reads} == {
        (2 * E, E): np.dtype(np.uint8),
        (E, E): np.dtype(np.uint8),
        (E, E // 2): np.dtype(np.uint8),
    }


def test_the_seed_codes_a_shape_in_the_packings_and_fusions_naming_it():
    start = Profile()
    start.add_packing(plain_packing())
    start.add_fusion(
        FusionKind.STAGED,
        [(GEMV, {"M": E, "K": E // 2}, {"coded_a": False}), (SiLU, {}, None)],
        [(0, "C", 1, "x")],
    )
    seed = coded_seed(recorder("none"), aie_utils.ensure_current_device(), start)
    [(_, steps, _, _)] = seed.fusions()
    [packing] = seed.packings()
    assert [t for _, _, t in packing.members] == [
        {"tile_size_input": 4, "coded_a": True},
        {"tile_size_input": 4, "coded_a": True},
    ]
    assert [t for _, _, t in steps] == [{"coded_a": True}, None]


def surveyed(
    steps_us: float, switch_us: float, fold_us: float, fusion_us: float = 0.0
) -> Survey:
    design = Design("GEMV M=2048 K=2048", "gemv", 1, steps_us, 0, None, "other")
    estimates = {
        "packing": Estimate(switch_us, "switches"),
        "folds": Estimate(fold_us, "steps"),
        "fusions": Estimate(fusion_us, "edges"),
        "coded": Estimate(0.0, "none"),
    }
    return Survey("v", (design,), 10, switch_us, estimates)


def test_each_search_runs_where_what_it_could_remove_weighs():
    plan = {s.name: s.runs for s in searches([surveyed(1000, 100, 1)])}
    assert plan == {"packing": True, "folds": False, "fusions": False}
    plan = {s.name: s.runs for s in searches([surveyed(1000, 10, 20)])}
    assert plan == {"packing": False, "folds": True, "fusions": False}
    plan = {s.name: s.runs for s in searches([surveyed(10**7, 10, 2000)])}
    assert plan == {"packing": False, "folds": True, "fusions": False}


def test_packing_is_no_reason_to_skip_fusions():
    """Fusions are judged on the packed version, so both run where both could pay."""
    plan = {s.name: s.runs for s in searches([surveyed(1000, 100, 1, 50)])}
    assert plan == {"packing": True, "folds": False, "fusions": True}


def test_a_decoder_is_timed_small_medium_and_large_up_to_its_context():
    """Every doubling of context counts alike.

    Three bands of equal log-width, each at its geometric centre, whole chunks for the
    prompt chunk.
    """
    assert contexts(256, 32768, 3, 1) == [(1 / 3, 575), (1 / 3, 2896), (1 / 3, 14596)]
    assert contexts(2048, 32768, 3, 2048) == [
        (1 / 3, 4096),
        (1 / 3, 8192),
        (1 / 3, 20480),
    ]
    assert contexts(2048, 2048, 3, 2048) == [(1.0, 2048)]


class Gated(iron.Graph):
    """``ElementwiseMul(SiLU(x[:n]), up[:n])``: two steps whose bound ``n`` binds per call."""

    def body(self, x, up, *, n: Scratchpad[np.int32]):
        return ElementwiseMul.step(
            SiLU.step(x[:n], tile_size=256), up[:n], tile_size=256
        )


def test_a_packed_step_is_valued_from_the_recording_its_profile_builds():
    """A packing rebuilds its steps as new operators; the call under the profile values each at the call's bound."""
    profile = Profile()
    profile.add_packing(
        [
            (SiLU, {}, {"num_aie_columns": 1}),
            (ElementwiseMul, {}, {"num_aie_columns": 1}),
        ]
    )
    graph = Gated()
    graph.profile = profile
    call = Timed(graph.record(x=(2048,), up=(2048,)), {"n": 1024})
    built, _, packing = call.under(profile, aie_utils.ensure_current_device())
    assert packing.groups
    assert not {id(s.op) for s in built.recording.steps} & {
        id(s.op) for s in call.recording.steps
    }
    assert [built.op_points(s.op) for s in built.recording.steps] == [
        [(1.0, {"valid": 1024})]
    ] * 2
