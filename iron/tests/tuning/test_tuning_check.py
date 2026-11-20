# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``check`` and ``measure`` on the NPU: a composition held bit-identical to its steps run apart, and timed against them."""

import numpy as np
import pytest

import iron
from iron import Scratchpad
from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Refinement, Region, Schedule
from iron.common.graph.record import Recording
from iron.common.image.step import Edge
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.rms_norm import RMSNorm
from iron.tests.support import sequences, toys_schedule
from iron.tests.support.toys_check import MulUpToM, MulUpToN
from iron.tests.support.toys_edges import chain, fan_out_norm_qkv, member
from iron.tests.support.toys_settings import shared_kv_state, small_integer_weight
from iron.tune.autotune import Timed
from iron.tune.search import check, measure, search

pytestmark = [
    pytest.mark.usefixtures("device"),
    pytest.mark.supported_devices("npu1", "npu2"),
]


def test_a_stream_window_is_bit_identical_to_its_steps_apart(device):
    """Add, RMSNorm and multiply fused as one stream window, held to the three run apart."""
    recording, region = chain()
    profile = Profile()
    profile.add_entry(Entry(region))
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


def test_a_build_computing_something_else_is_caught(device):
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
        device,
        Refinement.EXACT,
        base_calls=[Timed(other)],
    )
    assert not result.ok
    assert "out" in (result.why or "")


def test_a_window_bit_identical_to_its_steps_is_no_worse(device):
    """The stream window, held to no-worse: every output ties the steps apart on each draw."""
    recording, region = chain()
    profile = Profile()
    profile.add_entry(Entry(region))
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.NO_WORSE)
    assert result.ok, result.why


def test_a_build_computing_something_else_is_worse_against_the_reference(device):
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
        device,
        Refinement.NO_WORSE,
        base_calls=[Timed(other)],
    )
    assert not result.ok
    assert "out is worse" in (result.why or "")


def test_a_base_call_reading_an_input_its_call_does_not_give_is_refused(device):
    """A base call of another version, reading ``bias``, which the chain does not give, is refused before any build.

    Base calls pair with calls by position, so their inputs must still line
    up by name.
    """
    recording, _ = chain()
    add = ElementwiseAdd(size=256, num_aie_columns=1, tile_size=256)
    norm = RMSNorm(rows=1, tile_size=256, num_aie_columns=1)
    last = ElementwiseMul(size=256, num_aie_columns=1, tile_size=256)
    other = Recording.of_steps(
        "toy_chain_renamed",
        sequences.steps(
            (add, "a", "b", "h"), (norm, "h", "n"), (last, "n", "bias", "out")
        ),
        ["a", "b", "bias"],
        ["out"],
    )
    with pytest.raises(ValueError, match="does not give it bias"):
        check(
            Profile(),
            Profile(),
            [Timed(recording)],
            device,
            Refinement.NO_WORSE,
            base_calls=[Timed(other)],
        )


def test_a_build_measured_against_itself_takes_about_as_long(device):
    """The same build timed in pairs against itself: the median paired ratio is near one."""
    recording, _ = chain()
    measured = measure(Profile(), Profile(), [Timed(recording)], device)
    assert 0.8 < measured.ratio < 1.25
    assert measured.seconds > 0 and measured.base_seconds > 0


def test_a_stream_window_measures_faster_than_its_steps_apart(device):
    """Add, RMSNorm and multiply as one stream window take about a third of their time apart (one dispatch, no host round trips)."""
    recording, region = chain()
    profile = Profile()
    profile.add_entry(Entry(region))
    measured = measure(profile, Profile(), [Timed(recording)], device)
    assert measured.ratio < 0.8
    assert measured.seconds < measured.base_seconds


def test_a_window_whose_hand_off_steps_past_it_still_read_keeps_a_tee(device):
    """RMSNorm streamed into Q alone, while K and V read the norm's output from host memory: bit-identical to the steps apart.

    The fused edge keeps the norm's drain to host memory beside Q's on-chip
    read (a tee, ``Fusion.kept``), so K and V read what the norm wrote.
    """
    recording, _ = fan_out_norm_qkv()
    norm, q = (member(recording.steps[s].op) for s in (0, 1))
    profile = Profile()
    profile.add_entry(Entry(Region((norm, q), (Edge(0, "y", 1, "B"),))))
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


def test_search_keeps_the_stream_window_on_the_chain(device):
    """The tuner, on the chain alone, keeps a window of all three steps: it measures about a third of the steps apart."""
    recording, _ = chain()
    found = search([Timed(recording)], Profile(), device, budget_s=60.0)
    assert any(len(e.root.steps()) == 3 for e in found.entries())
    assert measure(found, Profile(), [Timed(recording)], device).ratio < 0.8


def test_prefill_composed_with_a_tee_carries_the_state_decode_reads(device):
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
        profile, Profile(), [Timed(prefill), Timed(decode)], device, Refinement.EXACT
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


def test_a_state_written_wrong_is_caught_after_the_call_that_writes_it(device):
    """A prefill returning what the base's returns but writing another ``kv`` (a product, not a sum) is caught after prefill, by the states compared."""
    graph, other = _writes_kv(ElementwiseAdd), _writes_kv(ElementwiseMul)
    result = check(
        Profile(),
        Profile(),
        [Timed(graph.record(x=(256,))), Timed(graph.record(x=(512,)))],
        device,
        Refinement.EXACT,
        base_calls=[Timed(other.record(x=(256,))), Timed(other.record(x=(512,)))],
    )
    assert not result.ok
    assert "call 0" in (result.why or "") and "kv" in (result.why or "")


class _Mul(iron.Graph):
    """``x * y`` whole, with no per-call value."""

    def body(self, x, y):
        return ElementwiseMul.step(x, y, size=256, tile_size=64)


@pytest.mark.parametrize("refinement", [Refinement.EXACT, Refinement.NO_WORSE])
def test_a_call_and_its_base_call_each_run_at_their_own_values(device, refinement):
    """A call bound by ``n`` held to a base call bound by ``m``: each runs at its own values and its own bound halved, paired in order."""
    shapes = dict(x=(256,), y=(256,))
    result = check(
        Profile(),
        Profile(),
        [Timed(MulUpToN().record(**shapes), values={"n": 256})],
        device,
        refinement,
        base_calls=[Timed(MulUpToM().record(**shapes), values={"m": 256})],
    )
    assert result.ok, result.why


@pytest.mark.parametrize("refinement", [Refinement.EXACT, Refinement.NO_WORSE])
def test_a_base_call_cutting_its_output_otherwise_than_its_call_is_refused(
    device, refinement
):
    """The base call at ``m=128`` against its call at ``n=256``: their points cut ``out`` to other lengths, refused before any build."""
    shapes = dict(x=(256,), y=(256,))
    with pytest.raises(ValueError, match="select other extents of out"):
        check(
            Profile(),
            Profile(),
            [Timed(MulUpToN().record(**shapes), values={"n": 256})],
            device,
            refinement,
            base_calls=[Timed(MulUpToM().record(**shapes), values={"m": 128})],
        )


class _WindowAtI(iron.Graph):
    """Rows ``i`` to ``i + 4`` of ``x``, ``i`` per call."""

    def body(self, x, *, i: Scratchpad[np.int32]):
        return Copy.step(x[i : i + 4])


class _WindowAtJ(iron.Graph):
    """``_WindowAtI`` with its per-call start named ``j``."""

    def body(self, x, *, j: Scratchpad[np.int32]):
        return Copy.step(x[j : j + 4])


@pytest.mark.parametrize("start", [2, 5])
def test_a_base_call_at_its_own_window_reaches_the_device_run(device, start):
    """The call's window starting at row 2, the base's at ``start``: one extent, so only the values tell them apart on the device."""
    call = Timed(_WindowAtI().record(x=(16, 64)), values={"i": 2})
    base = Timed(_WindowAtJ().record(x=(16, 64)), values={"j": start})
    result = check(
        Profile(), Profile(), [call], device, Refinement.EXACT, base_calls=[base]
    )
    if start == 2:
        assert result.ok, result.why
    else:
        assert not result.ok
        assert "out not bit-identical" in (result.why or "")


class _TwoUpToCR(iron.Graph):
    """``x * y`` over the first ``c`` elements and ``x * w`` over the first ``r``."""

    def body(self, x, y, w, *, c: Scratchpad[np.int32], r: Scratchpad[np.int32]):
        return (
            ElementwiseMul.step(x, y[:c], size=256, tile_size=64),
            ElementwiseMul.step(x, w[:r], size=256, tile_size=64),
        )


class _TwoUpToZM(iron.Graph):
    """``_TwoUpToCR`` with its bounds named ``z`` and ``m``, which sort the other way round."""

    def body(self, x, y, w, *, z: Scratchpad[np.int32], m: Scratchpad[np.int32]):
        return (
            ElementwiseMul.step(x, y[:z], size=256, tile_size=64),
            ElementwiseMul.step(x, w[:m], size=256, tile_size=64),
        )


def test_halved_bounds_pair_by_the_output_extent_they_cut(device):
    """Each halved bound pairs with the other side's that cuts the same output, whatever their names' order.

    The call halves ``c`` then ``r`` (cutting ``out0`` then ``out1``), the
    base ``m`` then ``z`` (``out1`` then ``out0``).
    """
    shapes = dict(x=(256,), y=(256,), w=(256,))
    result = check(
        Profile(),
        Profile(),
        [Timed(_TwoUpToCR().record(**shapes), values={"c": 256, "r": 256})],
        device,
        Refinement.EXACT,
        base_calls=[Timed(_TwoUpToZM().record(**shapes), values={"z": 256, "m": 256})],
    )
    assert result.ok, result.why


class _AddUpToM(iron.Graph):
    """``x + y`` over the first ``m`` elements, ``m`` per call."""

    def body(self, x, y, *, m: Scratchpad[np.int32]):
        return ElementwiseAdd.step(x, y[:m], size=256, tile_size=64)


def test_a_no_worse_call_is_held_to_its_base_s_reference_at_the_base_s_values(device):
    """A multiply bound by ``n`` held no-worse to an add bound by ``m``: worse against the add's reference.

    The outputs differ, so the reference is taken, at the base's own ``m``.
    """
    shapes = dict(x=(256,), y=(256,))
    result = check(
        Profile(),
        Profile(),
        [Timed(MulUpToN().record(**shapes), values={"n": 256})],
        device,
        Refinement.NO_WORSE,
        base_calls=[Timed(_AddUpToM().record(**shapes), values={"m": 256})],
    )
    assert not result.ok
    assert "out is worse" in (result.why or "")


def test_an_exact_base_batching_what_its_call_runs_one_at_a_time_is_refused(device):
    """A base running two decode steps a command, held exact to a profile running them one a command: refused before any build."""
    gemv, add = toys_schedule.decode_step()
    recording = toys_schedule.decode_step_recording("check_batched_base", gemv, add)
    base = Profile()
    base.add_schedule(Schedule(version=recording.version, calls_per_command=2))
    with pytest.raises(ValueError, match="the base batches its calls"):
        check(Profile(), base, [Timed(recording)], device, Refinement.EXACT)


def test_an_exact_base_keeping_commands_in_flight_is_held_to_calls_one_at_a_time(
    device,
):
    """A base keeping two decode commands in flight, one call each, against a profile running them one at a time: its calls run apart, bit-identical."""
    gemv, add = toys_schedule.decode_step()
    recording = toys_schedule.decode_step_recording("check_in_flight_base", gemv, add)
    base = Profile()
    base.add_schedule(Schedule(version=recording.version, commands_in_flight=2))
    result = check(Profile(), base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


def test_a_base_call_checked_at_another_count_of_points_is_refused(device):
    """A call bound per call (its values and its bound halved, two points) held to a base call with no bound (one point): refused before any build."""
    shapes = dict(x=(256,), y=(256,))
    with pytest.raises(ValueError, match="points pair with its call's in order"):
        check(
            Profile(),
            Profile(),
            [Timed(MulUpToN().record(**shapes), values={"n": 256})],
            device,
            Refinement.EXACT,
            base_calls=[Timed(_Mul().record(**shapes))],
        )
