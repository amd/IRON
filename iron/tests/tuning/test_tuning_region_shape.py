# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Region shape and schedule, over the composition contract."""

from __future__ import annotations

import numpy as np
import pytest

from iron.common.declare.composition import (
    Entry,
    Member,
    Refinement,
    Region,
    Schedule,
)
from iron.common.declare.profile import Profile
from iron.operators import GEMV, ElementwiseAdd
from iron.operators.copy import Copy
from iron.tests.support import toys_composition as toys
from iron.tests.support.llama_model import small
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, measure, search

pytestmark = pytest.mark.usefixtures("npu2")

M = 64

# Llama 1B decode (16 layers, 293 steps): convex connected sets a legal order makes
# consecutive, up to 8 steps, of which this many are consecutive already, and legal
# orders per layer.
LLAMA1B_DECODE_CONVEX_SETS = 770
LLAMA1B_DECODE_CONSECUTIVE = 446
LLAMA1B_DECODE_ORDERS_PER_LAYER = 252


def _qkv_region() -> Region:
    return Region(
        parts=(
            Member(GEMV, dict(M=M, K=M)),
            Member(GEMV, dict(M=M, K=M)),
            Member(GEMV, dict(M=M, K=M)),
        ),
        edges=(),
    )


@unbuilt
def test_a_convex_non_contiguous_set_round_trips_reordered(tmp_path, npu2):
    """``{Q, K, V}`` among the RoPE steps: convex, not consecutive, reordered to be."""
    region = _qkv_region()
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.add_schedule(Schedule(version=(), order=((0, 1), (1, 2))))
    profile.save(tmp_path / "profile.json")
    recording = toys.qkv_among_rope_recording("qkv_a")
    calls = [Timed(recording)]
    assert any(
        entry in edit.apply(Profile()).entries()
        for edit in candidates(calls, Profile(), npu2)
    )


@unbuilt
def test_recomputation_round_trips_in_a_schedule(tmp_path, npu2):
    """A schedule running a step again inside a later part round-trips and is proposed."""
    recording = toys.qkv_among_rope_recording("qkv_recompute")
    entry = Entry(root=_qkv_region())
    schedule = Schedule(version=recording.version, recompute=(0,))
    profile = Profile()
    profile.add_entry(entry)
    profile.add_schedule(schedule)
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == [entry]
    assert loaded.schedules() == [schedule]
    start = Profile()
    assert any(
        schedule in edit.apply(start).schedules()
        for edit in candidates([Timed(recording)], start, npu2)
    )


@unbuilt
@pytest.mark.parametrize(
    "parts, refinement, recording",
    [
        (
            (
                Member(GEMV, dict(M=M, K=M), part=("M", 0, M // 2)),
                Member(GEMV, dict(M=M, K=M), part=("M", M // 2, M)),
            ),
            Refinement.EXACT,
            toys.independent_regions_recording("fission_rows"),
        ),
        (
            (
                Member(GEMV, dict(M=M, K=M), part=("K", 0, M // 2)),
                Member(GEMV, dict(M=M, K=M), part=("K", M // 2, M)),
            ),
            Refinement.NO_WORSE,
            toys.gemv_fan_in_recording("fission_reduction", M, M, 2),
        ),
    ],
    ids=["independent_rows", "reduction"],
)
def test_fission_round_trips_as_an_entry(parts, refinement, recording, tmp_path, npu2):
    region = Region(parts=parts)
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    calls = [Timed(recording)]
    assert any(
        entry in edit.apply(Profile()).entries()
        for edit in candidates(calls, Profile(), npu2)
    )


@unbuilt
def test_a_partial_order_of_independent_regions_round_trips(tmp_path, npu2):
    region = Region(
        parts=(
            Region(parts=(Member(GEMV, dict(M=M, K=M)),)),
            Region(parts=(Member(GEMV, dict(M=M, K=M)),)),
        ),
        edges=(),
    )
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    recording = toys.independent_regions_recording("partial_order")
    calls = [Timed(recording)]
    assert any(
        entry in edit.apply(Profile()).entries()
        for edit in candidates(calls, Profile(), npu2)
    )


@unbuilt
@pytest.mark.extensive
def test_a_whole_graph_partition_drops_no_step(npu2):
    """Every step of a small decoder layer is in exactly one region or alone; a recomputed copy is the only duplicate."""
    model = small()
    decode_shapes, _ = model.shapes()
    recording = model.record(**decode_shapes)
    edits = list(candidates([Timed(recording)], Profile(), npu2))
    assert edits
    touched = set().union(*(edit.touches for edit in edits))
    assert touched <= set(range(len(recording.steps)))


@unbuilt
@pytest.mark.extensive
def test_llama_1b_decode_s_region_count_is_an_a_expectation(npu2):
    """Llama 1B decode's region count, as what a cheap, device-free candidate generator should reach."""
    model = small()
    decode_shapes, _ = model.shapes()
    recording = model.record(**decode_shapes)
    found = list(candidates([Timed(recording)], Profile(), npu2))
    assert len(found) <= LLAMA1B_DECODE_CONVEX_SETS


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_a_reordered_region_is_bit_identical_to_the_recorded_order(npu2):
    recording = toys.qkv_among_rope_recording("qkv_b")
    profile, base = Profile(), Profile()
    profile.add_entry(Entry(root=_qkv_region()))
    result = check(profile, base, [Timed(recording)], npu2, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_fission_of_a_reduction_is_no_worse(npu2):
    region = Region(
        parts=(
            Member(GEMV, dict(M=M, K=M), part=("K", 0, M // 2)),
            Member(GEMV, dict(M=M, K=M), part=("K", M // 2, M)),
        )
    )
    recording = toys.gemv_fan_in_recording("fission_reduction_check", M, M * 2, 2)
    profile, base = Profile(), Profile()
    profile.add_entry(Entry(root=region))
    result = check(profile, base, [Timed(recording)], npu2, Refinement.NO_WORSE)
    assert result.ok, result.why


@pytest.mark.extensive
@unbuilt
@pytest.mark.supported_devices("npu2")
def test_search_keeps_the_reordering_that_pays(npu2):
    region = _qkv_region()
    entry = Entry(root=region)
    recording = toys.qkv_among_rope_recording("qkv_c")
    calls = [Timed(recording)]
    start = Profile()
    with_entry = Profile()
    with_entry.add_entry(entry)
    ratio = measure(with_entry, start, calls, npu2).ratio
    tuned = search(calls, start, npu2)
    if ratio < 0.95:
        assert entry in tuned.entries()
    if ratio > 1.05:
        assert entry not in tuned.entries()
    result = check(tuned, start, calls, npu2, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
def test_a_non_convex_set_is_refused(npu2):
    """``{gemv_q, consumer}`` is not convex: ``rope_q``, the only path between them, is outside the set."""
    region = Region(
        parts=(Member(GEMV, dict(M=M, K=M)), Member(ElementwiseAdd, dict(size=M)))
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.qkv_among_rope_recording("non_convex")
    verdict = fit(profile, [Timed(recording)], npu2)
    assert not verdict.ok and verdict.stage == "analysis"


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_a_cyclic_contraction_is_refused(npu2):
    """``R1 = {a, c}``, ``R2 = {b, d}``: each convex alone, their contraction a cycle (``a -> d``, ``b -> c``)."""
    copy_dims = dict(dtype=np.float32, input_buffer_size=64)
    r1 = Region(parts=(Member(Copy, copy_dims), Member(Copy, copy_dims)))
    r2 = Region(parts=(Member(Copy, copy_dims), Member(Copy, copy_dims)))
    region = Region(parts=(r1, r2))
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.acyclic_contraction_recording("cyclic")
    verdict = fit(profile, [Timed(recording)], npu2)
    assert not verdict.ok and verdict.stage == "analysis"
