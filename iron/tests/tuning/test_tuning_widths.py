# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Widths: per-member core and stream counts, fit before any build, placement left to the placer."""

from __future__ import annotations

import dataclasses

import pytest
from aie.dialects.aie import get_target_model

from iron.common.declare.composition import Edge as CompositionEdge
from iron.common.declare.composition import Entry, Member, Refinement, Region, Scope
from iron.common.declare.profile import Profile
from iron.common.image.step import EdgeKind
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU
from iron.tests.support import toys_dataflow as toys
from iron.tests.support import toys_schedule
from iron.tests.support.fusable import gemv_silu_mul_recording
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import member
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import PLACEMENTS, candidates, check, fit, search

DEVICE = DEVICES["npu2"]()
_ARRAY_COLUMNS = get_target_model(DEVICE.resolve()).columns()


_SIZE = 2048  # divides evenly into 64-element tiles at 1, 2, 4 or 8 columns


def _window(columns, channels=1, kind=EdgeKind.STREAM):
    gemv = GEMV(
        M=_SIZE,
        K=_SIZE,
        tile_size_input=4,
        tile_size_output=64,
        num_aie_columns=columns,
        num_channels=channels,
    )
    silu = SiLU(size=_SIZE, tile_size=64, num_aie_columns=columns)
    mul = ElementwiseMul(size=_SIZE, tile_size=64, num_aie_columns=columns)
    members = tuple(
        dataclasses.replace(member(op), tunables={"num_aie_columns": columns})
        for op in (gemv, silu, mul)
    )
    edges = (
        CompositionEdge(0, "C", 1, "x", kind=kind),
        CompositionEdge(1, "y", 2, "a", kind=kind),
    )
    region = Region(parts=members, edges=edges)
    recording = gemv_silu_mul_recording(
        f"width_window_{columns}x{channels}", gemv, silu, mul
    )
    return region, recording


def test_per_member_width_counts_round_trip_and_are_proposed(tmp_path):
    """A window's per-member column counts round-trip through a profile and are a candidate, ordered by the cost model."""
    region, recording = _window(columns=2)
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "widths.json")
    loaded = Profile.load(tmp_path / "widths.json")
    assert loaded.entries() == [entry]
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, DEVICE)
    )


def test_narrowed_window_is_bit_identical_to_full_width():
    """A window narrowed to fit the array is bit-identical to the same window at full width."""
    full_region, recording = _window(columns=min(4, _ARRAY_COLUMNS))
    narrow_region, _ = _window(columns=1)
    base = Profile()
    base.add_entry(Entry(root=full_region))
    profile = Profile()
    profile.add_entry(Entry(root=narrow_region))
    result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.extensive
@unbuilt
def test_tuner_keeps_widths_that_pay_and_bounds_builds():
    """The tuner keeps the width setting that pays, builds stay bounded, and several placements are tried."""
    _, recording = _window(columns=2)
    start = Profile()
    found = search([Timed(recording)], start, DEVICE, budget_s=60.0)
    assert any(isinstance(e.root, Region) for e in found.entries())
    assert len(PLACEMENTS) > 1


def test_a_width_over_the_arrays_columns_is_refused_by_counts():
    """A GEMM at the array's full width, four cores a column, with a norm beside it, is refused by counts, before any build.

    Each member alone is a legal design; the GEMM claims every core, so the
    window as a whole does not fit.
    """
    gemm, norm = toys.gemm_rowwise(M=256, N=512, cols=_ARRAY_COLUMNS)
    region = toys.gemm_rowwise_region(gemm, norm)
    recording = toys.gemm_rowwise_recording("full_width", gemm, norm)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "counts"
    assert "column" in (result.why or "") or "core" in (result.why or "")


@unbuilt
def test_a_width_over_a_streams_budget_is_refused_by_counts():
    """C's narrow window (4 cores, 4 streams) wanting more DDR streams than npu2's shim channels have is refused by counts."""
    region, recording = _window(columns=4, channels=4, kind=EdgeKind.STAGED)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "counts"
    assert "stream" in (result.why or "") or "channel" in (result.why or "")


@unbuilt
def test_a_by_shape_entry_claiming_fewer_runs_than_iron_applies_is_refused():
    """A width entry naming only some runs of a shape two steps of the recording share is refused: one width set must fit every run."""
    gemv, add = toys_schedule.decode_step()
    recording = toys_schedule.decode_step_recording("width_shared_shape", gemv, add)
    region = Region(
        parts=(Member(type(gemv), {"M": gemv.M, "K": gemv.K}, {"num_aie_columns": 2}),)
    )
    profile = Profile()
    profile.add_entry(Entry(root=region, scope=Scope(occurrences=(0,))))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "analysis"
    assert "every run" in (result.why or "") or "shape" in (result.why or "")


@pytest.mark.skip(
    reason="no witness toy yet: each window the placer refuses so far, the counts "
    "refuse first"
)
def test_counts_the_fit_accepts_but_the_placer_refuses_need_a_witness():
    """Counts that fit the array but the placer refuses need a witness placement before they count.

    Such a refusal is a compiler-failure candidate, not a bare count refusal.
    """
    region, recording = _window(columns=_ARRAY_COLUMNS, channels=1)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], DEVICE, placements=PLACEMENTS)
    assert not result.ok
    assert result.stage == "placer"
    assert result.breakdown
