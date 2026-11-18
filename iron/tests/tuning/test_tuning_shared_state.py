# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Transformation tests for shared persistent state across versions (the KV cache, an SSM state)."""

import pytest
from aie.iron.device import NPU2

from iron.common.declare import Profile
from iron.common.declare.composition import Refinement, StateLayout
from iron.tests.support.toys_settings import shared_kv_state
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, measure, search

NPU2_DEVICE = NPU2()

pytestmark = pytest.mark.usefixtures("npu2")


@unbuilt
def test_a_state_layout_round_trips_and_applies_to_every_version(tmp_path):
    """One ``StateLayout`` for the persistent buffer every version that writes or reads it round-trips, and ``candidates`` proposes it."""
    graph = shared_kv_state()
    prefill = graph.record(x=(256,))
    decode = graph.record(x=(512,))
    assert prefill.residents["kv"] == decode.residents["kv"]
    layout = StateLayout(buffer="kv", order=("position", "element"), tile=(64,))
    profile = Profile()
    profile.add_state_layout(layout)
    path = tmp_path / "profile.json"
    profile.save(path)
    loaded = Profile.load(path)
    assert loaded.state_layouts() == [layout]
    found_prefill = list(candidates([Timed(prefill)], loaded, NPU2_DEVICE))
    found_decode = list(candidates([Timed(decode)], loaded, NPU2_DEVICE))
    assert any(layout in e.apply(Profile()).state_layouts() for e in found_prefill)
    assert any(layout in e.apply(Profile()).state_layouts() for e in found_decode)


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_the_layout_holds_end_to_end_over_prefill_then_decode():
    """The chosen layout is bit-identical to the untuned build over one real prefill-then-decode call sequence, state carried between them.

    ``check`` takes the graph's calls in order, state carried between them, so the real
    two-version graph's prefill call and its decode call are held to the untuned build in
    one end-to-end check rather than apart.
    """
    graph = shared_kv_state()
    prefill = graph.record(x=(256,))
    decode = graph.record(x=(512,))
    layout = StateLayout(buffer="kv", order=("position", "element"))
    base = Profile()
    tuned = Profile()
    tuned.add_state_layout(layout)
    result = check(
        tuned,
        base,
        [Timed(prefill), Timed(decode)],
        NPU2_DEVICE,
        refinement=Refinement.EXACT,
    )
    assert result.ok, result.why


@unbuilt
def test_the_tuner_prices_both_versions_jointly_and_keeps_one_layout_for_both():
    """The tuner, searching over the prefill and decode calls together, keeps one ``StateLayout`` for ``kv``.

    The joint search serves both versions, no worse than where it started.
    """
    graph = shared_kv_state()
    prefill = graph.record(x=(256,))
    decode = graph.record(x=(512,))
    start = Profile()
    calls = [Timed(prefill), Timed(decode)]
    tuned = search(calls, start, NPU2_DEVICE, budget_s=5.0)
    kv_layouts = [layout for layout in tuned.state_layouts() if layout.buffer == "kv"]
    assert len(kv_layouts) == 1
    assert check(tuned, start, calls, NPU2_DEVICE, refinement=Refinement.NO_WORSE).ok
    assert measure(tuned, start, calls, NPU2_DEVICE).ratio < 1.05


@unbuilt
def test_two_layouts_naming_one_buffer_are_refused(tmp_path):
    """``StateLayout`` has no scope of its own: two layouts naming the same buffer are refused on save, naming the buffer."""
    profile = Profile()
    profile.add_state_layout(StateLayout(buffer="kv", order=("position", "element")))
    profile.add_state_layout(StateLayout(buffer="kv", order=("element", "position")))
    profile.save(tmp_path / "profile.json")
