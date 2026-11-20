# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hand-off shapes: how a producer's lanes map onto a consumer's.

Every ``HandOff`` value, both directions where a direction is meaningful, over
the stream window's chains. A toy realizes its named shape with real lane
counts; the dataflow analysis is what derives that the hand-off is this
shape (``Analysis.hand_off``), never the toy. Every check calls the
composition contract before any compile, build or device use; a test is ``@unbuilt`` while what it calls raises ``NotImplementedError`` (not built yet).
"""

from __future__ import annotations

import dataclasses

import pytest
from aie.dialects.aie import WireBundle, get_target_model

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Refinement, Region
from iron.common.design import OperatorDesign
from iron.common.graph.sdf import analyze
from iron.common.image.compose import fits, transported
from iron.common.image.step import Edge, EdgeKind, Fusion, FusionKind, HandOff
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import (
    broadcast_weight_to_columns,
    fan_out_norm_qkv,
    join_in_pairs,
    layout_transpose,
    ratio_three_into_two,
    ratio_two_into_three,
    slices_qkv,
    split_in_two,
)
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, search

SHAPES = {
    "join_in_pairs": join_in_pairs,
    "split_in_two": split_in_two,
    "ratio_two_into_three": ratio_two_into_three,
    "ratio_three_into_two": ratio_three_into_two,
    "broadcast": broadcast_weight_to_columns,
    "slices_qkv": slices_qkv,
    "layout_transpose": layout_transpose,
}

# The toys whose lane counts are the device's columns', so take the device.
SIZED = {
    "join_in_pairs",
    "split_in_two",
    "ratio_two_into_three",
    "ratio_three_into_two",
    "broadcast",
}

# A name's edges and the HandOff every one of them realizes.
_REALIZES = {
    "join_in_pairs": HandOff.JOIN,
    "split_in_two": HandOff.SPLIT,
    "ratio_two_into_three": HandOff.RATIO,
    "ratio_three_into_two": HandOff.RATIO,
    "broadcast": HandOff.BROADCAST,
    "slices_qkv": HandOff.SLICES,
    "layout_transpose": HandOff.LAYOUT,
}

# The hand-offs the analysis derives today; a slice's objects are not
# modelled yet, so its case stays strict xfail.
_DERIVED = set(SHAPES) - {"slices_qkv"}

# Any ratio and broadcast are representable gaps today (operand.py:260-299):
# searchable, strict xfail, compiler-failure entries once the hardware could
# run them and the compiler refuses.
REPRESENTABLE_GAPS = {"ratio_two_into_three", "ratio_three_into_two", "broadcast"}


@pytest.mark.parametrize(
    "shape",
    [
        # An edge reading part of a buffer (a slice) is not proposed yet.
        pytest.param(s, marks=unbuilt) if s == "slices_qkv" else s
        for s in sorted(SHAPES)
    ],
)
@pytest.mark.usefixtures("device")
def test_a_hand_off_shape_round_trips_through_the_profile(shape, tmp_path, device):
    """Each hand-off shape round-trips through the profile, and ``candidates`` proposes it."""
    recording, region = SHAPES[shape](device) if shape in SIZED else SHAPES[shape]()
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / f"handoff_{shape}.json")
    loaded = Profile.load(tmp_path / f"handoff_{shape}.json")
    assert loaded.entries() == [entry]
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, device)
    )


@pytest.mark.usefixtures("device")
@pytest.mark.parametrize(
    "shape",
    [
        pytest.param(name, marks=() if name in _DERIVED else unbuilt)
        for name in sorted(SHAPES)
    ],
)
def test_the_analysis_derives_the_named_hand_off(shape, device):
    """The dataflow analysis derives every edge of each toy as the hand-off its lane counts realize; the toy never states it."""
    recording, region = SHAPES[shape](device) if shape in SIZED else SHAPES[shape]()
    analysis = analyze(region, recording, device)
    assert all(analysis.hand_off[edge] is _REALIZES[shape] for edge in region.edges)


# Each device's shapes the composer builds bit-identical there; npu1's
# restages wait on host 203.
_BUILT = {
    "npu1": {"broadcast", "join_in_pairs"},
    "npu2": {
        "broadcast",
        "join_in_pairs",
        "ratio_three_into_two",
        "ratio_two_into_three",
        "split_in_two",
    },
}


@pytest.mark.parametrize(
    ("device", "shape"),
    [
        pytest.param(
            name,
            s,
            id=f"device_{name}-shape_{s}",
            marks=() if s in _BUILT[name] else unbuilt,
        )
        for name in sorted(DEVICES)
        for s in sorted(SHAPES)
    ],
    indirect=["device"],
)
@pytest.mark.supported_devices("npu1", "npu2")
def test_a_hand_off_shape_is_bit_identical_to_the_steps_run_apart(shape, device):
    """Each hand-off shape is bit-identical to the same steps run apart."""
    recording, region = SHAPES[shape](device) if shape in SIZED else SHAPES[shape]()
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.parametrize(
    "device",
    [
        pytest.param(
            name,
            id=f"device_{name}",
            marks=() if "split_in_two" in _BUILT[name] else unbuilt,
        )
        for name in sorted(DEVICES)
    ],
    indirect=True,
)
@pytest.mark.supported_devices("npu1", "npu2")
def test_a_split_into_every_column_builds_correctly_or_is_refused_statically_never_hangs(
    device,
):
    """A split from half the columns into all of them (npu2's 4 -> 8, which once hung) either builds correctly or ``fit`` refuses it before any build."""
    recording, region = split_in_two(device)
    profile = Profile()
    profile.add_entry(Entry(region))
    verdict = fit(profile, [Timed(recording)], device)
    if verdict.ok:
        base = Profile()
        result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
        assert result.ok, result.why


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
def test_tuner_keeps_the_shape_that_pays_against_narrowing_to_equal_lanes(device):
    """The tuner keeps the join/split shape where it pays, priced against narrowing to equal lanes."""
    recording, _ = join_in_pairs(device)
    start = Profile()
    found = search([Timed(recording)], start, device, budget_s=60.0)
    assert any(isinstance(e.root, Region) and e.root.edges for e in found.entries())


def test_a_restage_over_a_memtiles_memory_is_refused_before_any_build(device):
    """A join restaged through a memtile and held deeper than the memtile's memory is refused before any build."""
    recording, region = join_in_pairs(device)
    (edge,) = region.edges
    region = dataclasses.replace(
        region,
        edges=(dataclasses.replace(edge, kind=EdgeKind.STAGED, depth=1 << 10),),
    )
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "counts"
    assert "memtile" in (result.why or "")


def _memtile_receives(device) -> int:
    """Return the lanes one of ``device``'s memtiles receives: its stream switch's DMA destinations."""
    model = get_target_model(device.resolve())
    row = next(r for r in range(model.rows()) if model.is_mem_tile(0, r))
    return model.get_num_dest_switchbox_connections(0, row, WireBundle.DMA)


# The devices where a GEMV at the array's full width drains more lanes than a
# memtile receives.
PAST_A_MEMTILE = [
    pytest.param(name, id=f"device_{name}")
    for name in sorted(DEVICES)
    if DEVICES[name]().cols > _memtile_receives(DEVICES[name]())
]


@pytest.mark.parametrize("device", PAST_A_MEMTILE, indirect=True)
def test_a_restage_over_a_memtiles_channels_is_refused_before_any_build(device):
    """A drain join restages a projection's lanes through a memtile, which joins only as many as it receives.

    All of a full-width projection's lanes joined into one are refused
    before any build; the build joins its drains in runs within them.
    """
    recording, _ = fan_out_norm_qkv(columns=(device.cols,) * 3)
    designs = [OperatorDesign(step.op.resolved()) for step in recording.steps]
    fusion = Fusion(
        FusionKind.STREAM,
        (0, 1, 2, 3),
        tuple(Edge(0, "y", c, "B") for c in (1, 2, 3)),
        packets=True,
    )
    members = {str(j): d for j, d in enumerate(designs)}
    refused = fits(members, fusion=dataclasses.replace(fusion, drains=device.cols))
    assert refused is not None and "MemTile" in refused
    assert 1 < transported(fusion, designs).drains <= _memtile_receives(device)


@pytest.mark.parametrize("shape", sorted(REPRESENTABLE_GAPS))
def test_any_ratio_and_broadcast_are_representable_but_unbuilt(shape, device):
    """Any-ratio and broadcast hand-offs round-trip and are proposed (searchable), but IRON does not build them yet."""
    recording, region = SHAPES[shape](device) if shape in SIZED else SHAPES[shape]()
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, device)
    )


@pytest.mark.supported_devices("npu1", "npu2")
def test_feed_refuses_a_held_input_broadcast_flips_it(device):
    """Broadcast flips ``test_operand_lanes.py``'s ``feed_refuses_a_held_input``: a replicated input is fed where a plain stream is refused."""
    recording, region = broadcast_weight_to_columns(device)
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why
