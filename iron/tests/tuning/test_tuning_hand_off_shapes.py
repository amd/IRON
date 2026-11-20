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
from iron.common.graph.fusion import composed
from iron.common.graph.sdf import analyze
from iron.common.image.compose import fits, fused_configuration, transported
from iron.common.image.step import Edge, EdgeKind, Fusion, FusionKind, HandOff
from iron.tests.support import toys_dataflow
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import (
    broadcast_weight_to_columns,
    fan_out_norm_qkv,
    held_in_l1,
    join_in_pairs,
    join_of_two_streams,
    join_rows_after_rows,
    join_rows_into_one,
    layout_transpose,
    ratio_three_into_two,
    ratio_two_into_three,
    ratio_two_into_three_rows,
    slices_qkv,
    split_in_two,
    split_into_rows,
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
        "layout_transpose",
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


# Hand-off shapes held in L1, restaged on the cores their two steps share,
# each step taking one input, so each restage fits a core. GEMM's tiles join
# their cores in a memtile, so its layout held in L1 is RMSNorm spliced into
# GEMM's cores; QKV's slices held in L1 are views of one core's buffer.
HELD_IN_L1 = {
    "join_rows_into_one": join_rows_into_one,
    "split_into_rows": split_into_rows,
    "ratio_two_into_three_rows": ratio_two_into_three_rows,
    "layout_transpose": layout_transpose,
    "slices_qkv": slices_qkv,
}

# Each device's L1-held shapes the composer builds bit-identical there.
_BUILT_IN_L1: dict[str, set[str]] = {
    "npu1": set(),
    "npu2": {"join_rows_into_one", "ratio_two_into_three_rows", "split_into_rows"},
}


@pytest.mark.parametrize(
    ("device", "shape"),
    [
        pytest.param(
            name,
            s,
            id=f"device_{name}-shape_{s}",
            marks=() if s in _BUILT_IN_L1[name] else unbuilt,
        )
        for name in sorted(DEVICES)
        for s in sorted(HELD_IN_L1)
    ],
    indirect=["device"],
)
@pytest.mark.supported_devices("npu1", "npu2")
def test_a_hand_off_shape_held_in_l1_is_bit_identical_to_the_steps_run_apart(
    shape, device
):
    """Each hand-off shape held in L1, on the cores its steps share, is bit-identical to the steps run apart."""
    recording, region = held_in_l1(*HELD_IN_L1[shape]())
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


def _refused_in_l1(recording, region, device, past):
    """Assert ``fit`` refuses ``region`` by the counts, a restage held in L1 ``past`` a core tile's budget."""
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "counts"
    assert "restaged in L1" in (result.why or "")
    assert past in (result.why or "")


def test_a_restage_held_in_l1_past_a_cores_input_channels_is_refused_before_any_build(
    device,
):
    """A ratio held in L1 whose core already takes three inputs (GEMV's two, the multiply's other) is refused before any build, however it is placed."""
    _refused_in_l1(*held_in_l1(*ratio_two_into_three(device)), device, "input channels")


def test_a_restage_held_in_l1_past_a_cores_memory_is_refused_before_any_build(
    device,
):
    """A join held in L1 whose rounds, deep enough, outgrow the joining core's memory is refused before any build."""
    _refused_in_l1(
        *held_in_l1(*join_rows_into_one(size=1024), depth=14), device, "bytes"
    )


# A split as wide as npu2's array.
WIDE = [pytest.param("npu2", id="device_npu2")]


@pytest.mark.parametrize("device", WIDE, indirect=True)
def test_a_split_held_in_l1_past_a_cores_output_channels_is_refused_before_any_build(
    device,
):
    """One lane split into eight held in L1 sends every lane but the leading one on a channel of its own, more than a core has."""
    _refused_in_l1(
        *held_in_l1(*split_into_rows(size=64, rows=8)), device, "output channels"
    )


def test_a_join_held_in_l1_past_a_cores_buffer_descriptors_is_refused_before_any_build(
    device,
):
    """Two lanes joined into one held in L1, deep: the lane arriving by DMA takes a buffer descriptor a round, past the core's."""
    _refused_in_l1(
        *held_in_l1(*join_rows_into_one(size=64), depth=13),
        device,
        "buffer descriptors",
    )


def _composed_in_l1(recording, region):
    """Compose ``region``'s one fusion as the build does; return its arrays."""
    profile = Profile()
    profile.add_entry(Entry(region))
    _, (fusion,) = composed(recording, profile)
    designs = [OperatorDesign(recording.steps[s].op.resolved()) for s in fusion.steps]
    _, arrays = fused_configuration("l1", fusion, designs)
    return arrays


def test_a_restage_held_in_l1_is_as_deep_as_its_chosen_depth(device):
    """A join held in L1 three deep builds its pool three rounds deep, as fit counts it."""
    recording, region = held_in_l1(*join_rows_into_one(), depth=3)
    arrays = _composed_in_l1(recording, region)
    (sink,) = [b for b in arrays[1].op.buffers if b.name == "x"]
    assert [f.depth for f in sink.staged] == [3]


def test_a_restage_held_in_l1_links_on_the_core_its_reader_runs_on(device):
    """A join held in L1 whose producer shares its cores with an earlier step links on the core the three run on, whichever body leads it."""
    recording, region = held_in_l1(*join_rows_after_rows())
    arrays = _composed_in_l1(recording, region)
    (sink,) = [b for b in arrays[2].op.buffers if b.name == "x"]
    (fifo,) = sink.staged
    (core,) = [
        w
        for a in arrays
        for w in a.workers
        if any(h.object_fifo is fifo for h in w.fifos)
    ]
    assert fifo.delegate_tile is core.tile


def test_a_restage_held_in_l1_counts_no_channel_for_edges_on_chip(device):
    """An add fed core to core by two SiLUs, its lanes joined in L1: the add's streamed inputs may be its neighbours' memory, so the counts do not refuse it."""
    recording, region = join_of_two_streams()
    profile = Profile()
    profile.add_entry(Entry(region))
    try:
        result = fit(profile, [Timed(recording)], device)
    except NotImplementedError as e:
        assert "restage held in L1" not in str(e)
        return
    assert result.ok, result.why


def test_a_restage_held_in_l1_of_an_output_kept_too_waits(device):
    """A split held in L1 of an output the host also drains is not built yet: fit waits rather than counting it."""
    recording, region = held_in_l1(*split_into_rows(keep=True))
    profile = Profile()
    profile.add_entry(Entry(region))
    with pytest.raises(NotImplementedError, match="read elsewhere too"):
        fit(profile, [Timed(recording)], device)


@pytest.mark.parametrize(
    "device",
    [pytest.param("npu2", id="device_npu2")],
    indirect=True,
)
@pytest.mark.supported_devices("npu2")
def test_a_gemms_output_streams_into_anothers_a(device):
    """One GEMM's C streamed into another's A, tile for tile, is bit-identical to the two run apart.

    The consumer's memtile splits the producer's lanes through their bound
    ends, so no end of theirs is left without a reader.
    """
    producer, consumer = toys_dataflow.gemm_into_gemm(
        device, M=256, width=64, producer_tile=64, consumer_tile=64
    )
    recording = toys_dataflow.gemm_into_gemm_recording(
        "gemm_into_gemm", producer, consumer
    )
    profile = Profile()
    profile.add_entry(Entry(toys_dataflow.gemm_into_gemm_region(producer, consumer)))
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why
