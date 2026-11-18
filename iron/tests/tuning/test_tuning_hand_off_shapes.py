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

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Refinement, Region
from iron.common.graph.sdf import analyze
from iron.common.image.step import EdgeKind, HandOff
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import (
    broadcast_weight_to_columns,
    fan_out_norm_qkv,
    join_8_into_4,
    layout_transpose,
    ratio_4_into_6,
    ratio_6_into_4,
    slices_qkv,
    split_4_into_8,
)
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, search

DEVICE = DEVICES["npu2"]()

SHAPES = {
    "join_8_into_4": join_8_into_4,
    "split_4_into_8": split_4_into_8,
    "ratio_4_into_6": ratio_4_into_6,
    "ratio_6_into_4": ratio_6_into_4,
    "broadcast": broadcast_weight_to_columns,
    "slices_qkv": slices_qkv,
    "layout_transpose": layout_transpose,
}

# A name's edges and the HandOff every one of them realizes.
_REALIZES = {
    "join_8_into_4": HandOff.JOIN,
    "split_4_into_8": HandOff.SPLIT,
    "ratio_4_into_6": HandOff.RATIO,
    "ratio_6_into_4": HandOff.RATIO,
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
REPRESENTABLE_GAPS = {"ratio_4_into_6", "ratio_6_into_4", "broadcast"}


@unbuilt
@pytest.mark.parametrize("shape", sorted(SHAPES))
def test_a_hand_off_shape_round_trips_through_the_profile(shape, tmp_path):
    """Each hand-off shape round-trips through the profile, and ``candidates`` proposes it."""
    recording, region = SHAPES[shape]()
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / f"handoff_{shape}.json")
    loaded = Profile.load(tmp_path / f"handoff_{shape}.json")
    assert loaded.entries() == [entry]
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, DEVICE)
    )


@pytest.mark.usefixtures("npu2")
@pytest.mark.parametrize(
    "shape",
    [
        pytest.param(name, marks=() if name in _DERIVED else unbuilt)
        for name in sorted(SHAPES)
    ],
)
def test_the_analysis_derives_the_named_hand_off(shape):
    """The dataflow analysis derives every edge of each toy as the hand-off its lane counts realize; the toy never states it."""
    recording, region = SHAPES[shape]()
    analysis = analyze(region, recording, DEVICE)
    assert all(analysis.hand_off[edge] is _REALIZES[shape] for edge in region.edges)


@unbuilt
@pytest.mark.parametrize("shape", sorted(SHAPES))
@pytest.mark.supported_devices("npu2")
def test_a_hand_off_shape_is_bit_identical_to_the_steps_run_apart(shape):
    """Each hand-off shape is bit-identical to the same steps run apart."""
    recording, region = SHAPES[shape]()
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_the_4_into_8_split_builds_correctly_or_is_refused_statically_never_hangs():
    """A 4 -> 8 split that once hung either builds correctly or ``fit`` refuses it before any build."""
    recording, region = split_4_into_8()
    profile = Profile()
    profile.add_entry(Entry(region))
    verdict = fit(profile, [Timed(recording)], DEVICE)
    if verdict.ok:
        base = Profile()
        result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
        assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_tuner_keeps_the_shape_that_pays_against_narrowing_to_equal_lanes():
    """The tuner keeps the join/split shape where it pays, priced against narrowing to equal lanes."""
    recording, _ = join_8_into_4()
    start = Profile()
    found = search([Timed(recording)], start, DEVICE, budget_s=60.0)
    assert any(isinstance(e.root, Region) and e.root.edges for e in found.entries())


def test_a_restage_over_a_memtiles_memory_is_refused_before_any_build():
    """A join restaged through a memtile and held deeper than the memtile's memory is refused before any build."""
    recording, region = join_8_into_4()
    (edge,) = region.edges
    region = dataclasses.replace(
        region,
        edges=(dataclasses.replace(edge, kind=EdgeKind.STAGED, depth=1 << 10),),
    )
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "counts"
    assert "memtile" in (result.why or "")


@unbuilt
def test_a_restage_over_a_memtiles_channels_is_refused_before_any_build():
    """A restage past a memtile's channel budget is refused before any build."""
    recording, region = fan_out_norm_qkv(columns=(8, 8, 8))
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "counts"
    assert "channel" in (result.why or "")


@unbuilt
@pytest.mark.parametrize("shape", sorted(REPRESENTABLE_GAPS))
def test_any_ratio_and_broadcast_are_representable_but_unbuilt(shape):
    """Any-ratio and broadcast hand-offs round-trip and are proposed (searchable), but IRON does not build them yet."""
    recording, region = SHAPES[shape]()
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, DEVICE)
    )


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_feed_refuses_a_held_input_broadcast_flips_it():
    """Broadcast flips ``test_operand_lanes.py``'s ``feed_refuses_a_held_input``: a replicated input is fed where a plain stream is refused."""
    recording, region = broadcast_weight_to_columns()
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why
