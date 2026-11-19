# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Mapping: actors on one worker in a fixed firing order, or split across workers."""

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Member, Refinement, Region
from iron.tests.support import toys_dataflow as toys
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import check, fit, search

pytestmark = pytest.mark.usefixtures("npu2")


def _three_on_one_worker(order: tuple[int, ...]) -> tuple[Region, tuple]:
    add, silu, mul = toys.add_silu_mul()
    members = (
        Member(
            cls=type(add),
            dims={"size": add.size},
            tunables={"tile_size": add.tile_size},
        ),
        Member(
            cls=type(silu),
            dims={"size": silu.size},
            tunables={"tile_size": silu.tile_size},
        ),
        Member(
            cls=type(mul),
            dims={"size": mul.size},
            tunables={"tile_size": mul.tile_size},
        ),
    )
    edges = toys.add_silu_mul_region(add, silu, mul).edges
    region = Region(parts=members, edges=edges, workers=(order,))
    return region, (add, silu, mul)


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_a_valid_firing_order_runs_bit_identical():
    """``add``, ``SiLU``, ``mul`` on one worker, in their dependence order: bit-identical to apart."""
    region, (add, silu, mul) = _three_on_one_worker((0, 1, 2))
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.add_silu_mul_recording("worker-valid", add, silu, mul)
    result = check(profile, Profile(), [Timed(recording)], toys.NPU2, Refinement.EXACT)
    assert result.ok, result.why


def test_an_invalid_firing_order_is_refused_statically():
    """The same three actors fired out of dependence order.

    ``mul`` before ``SiLU`` produces its input: refused by ``fit`` at
    stage ``"analysis"``, before any build, not merely at the wrong answer.
    """
    region, (add, silu, mul) = _three_on_one_worker((0, 2, 1))
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.add_silu_mul_recording("worker-invalid", add, silu, mul)
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert not result.ok
    assert result.stage == "analysis"


@unbuilt
def test_one_actor_split_across_workers_round_trips():
    """``mul``'s work split by rows into two fissioned parts, each on its own worker: a fission named by ``Member.part``, and it fits."""
    add, silu, mul = toys.add_silu_mul(size=512, tile=256)
    lo = Member(
        cls=type(mul),
        dims={"size": mul.size},
        tunables={"tile_size": mul.tile_size},
        part=("rows", 0, 256),
    )
    hi = Member(
        cls=type(mul),
        dims={"size": mul.size},
        tunables={"tile_size": mul.tile_size},
        part=("rows", 256, 512),
    )
    region = Region(parts=(lo, hi), workers=((0,), (1,)))
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.add_silu_mul_recording("split-mul", add, silu, mul)
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert result.ok


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_a_qk_softmax_pv_style_pipeline_on_one_core():
    """``Q·K -> softmax step -> P·V`` on one core, a fixed firing order: bit-identical to apart."""
    add, silu, mul = toys.add_silu_mul(size=256, tile=128)
    members = (
        Member(
            cls=type(add),
            dims={"size": add.size},
            tunables={"tile_size": add.tile_size},
        ),
        Member(
            cls=type(silu),
            dims={"size": silu.size},
            tunables={"tile_size": silu.tile_size},
        ),
        Member(
            cls=type(mul),
            dims={"size": mul.size},
            tunables={"tile_size": mul.tile_size},
        ),
    )
    region = Region(
        parts=members,
        edges=toys.add_silu_mul_region(add, silu, mul).edges,
        workers=((0, 1, 2),),
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.add_silu_mul_recording("qkv-style", add, silu, mul)
    result = check(profile, Profile(), [Timed(recording)], toys.NPU2, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.extensive
@unbuilt
@pytest.mark.supported_devices("npu2")
def test_tuner_keeps_the_mapping_that_pays():
    """``search``, run on the three-actor toy alone, keeps a dependence-respecting order.

    Passes ``check`` against the start, exact.
    """
    region, (add, silu, mul) = _three_on_one_worker((0, 1, 2))
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.add_silu_mul_recording("searched-mapping", add, silu, mul)
    calls = [Timed(recording)]
    tuned = search(calls, profile, toys.NPU2)
    verdict = check(tuned, profile, calls, toys.NPU2, Refinement.EXACT)
    assert verdict.ok, verdict.why
    order = tuned.entries()[0].root.workers[0]
    assert order.index(0) < order.index(1) < order.index(2)
