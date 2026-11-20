# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Mapping: actors on one worker in a fixed firing order, or split across workers."""

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Member, Refinement, Region
from iron.common.graph.record import Recording
from iron.common.image.step import Edge
from iron.tests.support import toys_composition as composition
from iron.tests.support import toys_dataflow as toys
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import member
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import check, fit, search

pytestmark = pytest.mark.usefixtures("device")


# Where N actors on one worker build. npu1's wait on host 203.
_ONE_WORKER_BUILT = [
    pytest.param(name, id=f"device_{name}", marks=() if name == "npu2" else unbuilt)
    for name in sorted(DEVICES)
]


def _three_on_one_worker(order: tuple[int, ...]) -> tuple[Region, tuple]:
    """``add -> SiLU -> ReLU`` on one worker, fired in ``order``.

    Two host inputs: a core takes two streams in (``add -> SiLU -> mul``
    reads three, which no placement of one core gives).
    """
    add, silu, relu = toys.add_silu_relu()
    members = tuple(
        Member(
            cls=type(op),
            dims={"size": op.size},
            tunables={"tile_size": op.tile_size},
        )
        for op in (add, silu, relu)
    )
    edges = (Edge(0, "y", 1, "x"), Edge(1, "y", 2, "x"))
    region = Region(parts=members, edges=edges, workers=(order,))
    return region, (add, silu, relu)


def _attention_on_one_worker(
    order: tuple[int, ...],
) -> tuple[Region, Recording]:
    """Decode attention, ``K q -> Softmax -> V^T p``, on one worker fired in ``order``: PLAN's E example.

    One column, a score row an object: QK^T's output tile is a key row, as
    the softmax reads it, and P V's vector is the softmax's row, fed.
    """
    qk, softmax, pv = composition.decode_attention_ops(kv_len=128, rows=16)
    qk = qk.replace(num_aie_columns=1, num_channels=1, tile_size_output=128)
    pv = pv.replace(num_aie_columns=1, num_channels=1)
    softmax = softmax.replace(num_aie_columns=1)
    recording = composition.decode_attention_recording(
        "attention_on_one_worker", qk, softmax, pv
    )
    region = Region(
        (member(qk), member(softmax), member(pv)),
        (Edge(0, "C", 1, "x"), Edge(1, "y", 2, "B")),
        workers=(order,),
    )
    return region, recording


@pytest.mark.parametrize("device", _ONE_WORKER_BUILT, indirect=True)
@pytest.mark.supported_devices("npu1", "npu2")
def test_a_valid_firing_order_runs_bit_identical(device):
    """``add``, ``SiLU``, ``ReLU`` on one worker, in their dependence order: bit-identical to apart."""
    region, (add, silu, relu) = _three_on_one_worker((0, 1, 2))
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.add_silu_relu_recording("worker-valid", add, silu, relu)
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


def test_an_invalid_firing_order_is_refused_statically(device):
    """The same three actors fired out of dependence order.

    ``ReLU`` before ``SiLU`` produces its input: refused by ``fit`` at
    stage ``"analysis"``, before any build, not merely at the wrong answer.
    """
    region, (add, silu, relu) = _three_on_one_worker((0, 2, 1))
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.add_silu_relu_recording("worker-invalid", add, silu, relu)
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "deadlocks" in result.why


def test_attention_fired_out_of_order_on_one_worker_is_refused_statically(device):
    """``V^T p`` fired before the softmax gives it ``p``: refused by ``fit`` at the analysis, before any build."""
    region, recording = _attention_on_one_worker((0, 2, 1))
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "deadlocks" in result.why


@unbuilt
def test_one_actor_split_across_workers_round_trips(device):
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
    result = fit(profile, [Timed(recording)], device)
    assert result.ok


@pytest.mark.parametrize("device", _ONE_WORKER_BUILT, indirect=True)
@pytest.mark.supported_devices("npu1", "npu2")
def test_a_qk_softmax_pv_style_pipeline_on_one_core(device):
    """``K q -> Softmax -> V^T p`` on one core, a fixed firing order: bit-identical to apart."""
    region, recording = _attention_on_one_worker((0, 1, 2))
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.extensive
@pytest.mark.parametrize("device", _ONE_WORKER_BUILT, indirect=True)
@pytest.mark.supported_devices("npu1", "npu2")
def test_tuner_keeps_the_mapping_that_pays(device):
    """``search``, run on the three-actor toy alone, keeps a dependence-respecting order.

    Passes ``check`` against the start, exact.
    """
    region, (add, silu, relu) = _three_on_one_worker((0, 1, 2))
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.add_silu_relu_recording("searched-mapping", add, silu, relu)
    calls = [Timed(recording)]
    tuned = search(calls, profile, device)
    verdict = check(tuned, profile, calls, device, Refinement.EXACT)
    assert verdict.ok, verdict.why
    order = tuned.entries()[0].root.workers[0]
    assert order.index(0) < order.index(1) < order.index(2)
