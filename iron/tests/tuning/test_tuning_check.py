# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``check`` and ``measure`` on the NPU: a composition held bit-identical to its steps run apart, and timed against them."""

import pytest

import iron
from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Refinement, Region
from iron.common.graph.record import Recording
from iron.common.image.step import Edge
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.rms_norm import RMSNorm
from iron.tests.support import sequences
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import chain, fan_out_norm_qkv, member
from iron.tests.support.toys_settings import shared_kv_state, small_integer_weight
from iron.tune.autotune import Timed
from iron.tune.search import check, measure, search

DEVICE = DEVICES["npu2"]()

pytestmark = [pytest.mark.usefixtures("npu2"), pytest.mark.supported_devices("npu2")]


def test_a_stream_window_is_bit_identical_to_its_steps_apart():
    """Add, RMSNorm and multiply fused as one stream window, held to the three run apart."""
    recording, region = chain()
    profile = Profile()
    profile.add_entry(Entry(region))
    result = check(profile, Profile(), [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


def test_a_build_computing_something_else_is_caught():
    """The same chain held to one ending in an add, not a multiply: its ``out`` differs, and the check names it."""
    recording, region = chain()
    add = ElementwiseAdd(size=256, num_aie_columns=1, tile_size=256)
    norm = RMSNorm(rows=1, tile_size=256, num_aie_columns=1)
    last = ElementwiseAdd(size=256, num_aie_columns=1, tile_size=256)
    other = Recording.of_steps(
        "toy_chain",
        sequences.steps(
            (add, "a", "b", "h"), (norm, "h", "n"), (last, "n", "up", "out")
        ),
        ["a", "b", "up"],
        ["out"],
    )
    assert isinstance(recording.steps[2].op, ElementwiseMul)
    profile = Profile()
    profile.add_entry(Entry(region))
    result = check(
        profile,
        Profile(),
        [Timed(recording)],
        DEVICE,
        Refinement.EXACT,
        base_calls=[Timed(other)],
    )
    assert not result.ok
    assert "out" in (result.why or "")


def test_a_window_bit_identical_to_its_steps_is_no_worse():
    """The stream window, held to no-worse: every output ties the steps apart on each draw."""
    recording, region = chain()
    profile = Profile()
    profile.add_entry(Entry(region))
    result = check(profile, Profile(), [Timed(recording)], DEVICE, Refinement.NO_WORSE)
    assert result.ok, result.why


def test_a_build_computing_something_else_is_worse_against_the_reference():
    """A chain ending in a multiply, held no-worse to one ending in an add: against the add's reference its ``out`` is worse, and the check names it."""
    recording, _ = chain()
    add = ElementwiseAdd(size=256, num_aie_columns=1, tile_size=256)
    norm = RMSNorm(rows=1, tile_size=256, num_aie_columns=1)
    last = ElementwiseAdd(size=256, num_aie_columns=1, tile_size=256)
    other = Recording.of_steps(
        "toy_chain",
        sequences.steps(
            (add, "a", "b", "h"), (norm, "h", "n"), (last, "n", "up", "out")
        ),
        ["a", "b", "up"],
        ["out"],
    )
    result = check(
        Profile(),
        Profile(),
        [Timed(recording)],
        DEVICE,
        Refinement.NO_WORSE,
        base_calls=[Timed(other)],
    )
    assert not result.ok
    assert "out is worse" in (result.why or "")


def test_a_build_measured_against_itself_takes_about_as_long():
    """The same build timed in pairs against itself: the median paired ratio is near one."""
    recording, _ = chain()
    measured = measure(Profile(), Profile(), [Timed(recording)], DEVICE)
    assert 0.8 < measured.ratio < 1.25
    assert measured.seconds > 0 and measured.base_seconds > 0


def test_a_stream_window_measures_faster_than_its_steps_apart():
    """Add, RMSNorm and multiply as one stream window take about a third of their time apart (one dispatch, no host round trips)."""
    recording, region = chain()
    profile = Profile()
    profile.add_entry(Entry(region))
    measured = measure(profile, Profile(), [Timed(recording)], DEVICE)
    assert measured.ratio < 0.8
    assert measured.seconds < measured.base_seconds


def test_a_window_whose_hand_off_steps_past_it_still_read_keeps_a_tee():
    """RMSNorm streamed into Q alone, while K and V read the norm's output from host memory: bit-identical to the steps apart.

    The fused edge keeps the norm's drain to host memory beside Q's on-chip
    read (a tee, ``Fusion.kept``), so K and V read what the norm wrote.
    """
    recording, _ = fan_out_norm_qkv()
    norm, q = (member(recording.steps[s].op) for s in (0, 1))
    profile = Profile()
    profile.add_entry(Entry(Region((norm, q), (Edge(0, "y", 1, "B"),))))
    result = check(profile, Profile(), [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


def test_search_keeps_the_stream_window_on_the_chain():
    """The tuner, on the chain alone, keeps a window of all three steps: it measures about a third of the steps apart."""
    recording, _ = chain()
    found = search([Timed(recording)], Profile(), DEVICE, budget_s=60.0)
    assert any(len(e.root.steps()) == 3 for e in found.entries())
    assert measure(found, Profile(), [Timed(recording)], DEVICE).ratio < 0.8


def test_prefill_composed_with_a_tee_carries_the_state_decode_reads():
    """Prefill's two adds composed into one window, run then decode, state carried: bit-identical to the steps apart.

    Prefill writes ``kv`` (a state, so the window keeps its host copy) and
    decode multiplies by it, so decode agrees only where the composed
    prefill wrote ``kv`` right and it was carried into decode's build.
    """
    graph = shared_kv_state()
    prefill, decode = graph.record(x=(256,)), graph.record(x=(512,))
    first, second = (member(s.op) for s in prefill.steps)
    profile = Profile()
    profile.add_entry(Entry(Region((first, second), (Edge(0, "y", 1, "a"),))))
    result = check(
        profile, Profile(), [Timed(prefill), Timed(decode)], DEVICE, Refinement.EXACT
    )
    assert result.ok, result.why


def _writes_kv(writer: type) -> iron.Graph:
    """Return a graph whose prefill writes ``kv`` with ``writer`` and returns ``x + bias``, and whose decode multiplies by ``kv``."""
    bias = small_integer_weight((256,), 1)
    kv = iron.state((256,), name="kv")

    class WritesKV(iron.Graph):
        def body(self, x):
            if x.shape[0] == 256:
                writer.step(x, bias, kv, tile_size=64)
                return ElementwiseAdd.step(x, bias, tile_size=64)
            return ElementwiseMul.step(kv, x[:256], tile_size=64)

    return WritesKV()


def test_a_state_written_wrong_is_caught_after_the_call_that_writes_it():
    """A prefill returning what the base's returns but writing another ``kv`` (a product, not a sum) is caught after prefill, by the states compared."""
    graph, other = _writes_kv(ElementwiseAdd), _writes_kv(ElementwiseMul)
    result = check(
        Profile(),
        Profile(),
        [Timed(graph.record(x=(256,))), Timed(graph.record(x=(512,)))],
        DEVICE,
        Refinement.EXACT,
        base_calls=[Timed(other.record(x=(256,))), Timed(other.record(x=(512,)))],
    )
    assert not result.ok
    assert "call 0" in (result.why or "") and "kv" in (result.why or "")
