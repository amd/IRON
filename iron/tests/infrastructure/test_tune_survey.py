# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What bounds each version before a tune plans (``iron.tune.survey``).

No NPU above ``# On the device``.
"""

import aie.utils as aie_utils
import pytest

import iron
from iron import Profile
from iron.common.design import OperatorDesign
from iron.common.graph.compiled import apply_profile
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.relu import ReLU
from iron.operators.tanh import Tanh
from iron.tests.support.llama_model import small
from iron.tune.autotune import Shape, Timed, merged, settings, shapes
from iron.tune.costmodel import CostModel
from iron.tune.fold import array_scoped_fold_candidates
from iron.tune.measure import LONG_STEP_US, MIN_CALLS, Cache, Timing, measure, platform
from iron.tune.survey import step_times, survey

pytestmark = pytest.mark.usefixtures("npu2")

# Bytes per us a weight-reading design is given: 50 GB/s.
READ = 50_000


def decode_call() -> Timed:
    model = small()
    model.profile = Profile()
    return Timed(model.record(**model.shapes()[0]))


def given_times(call: Timed, dev) -> dict[str, float]:
    """Each design's time.

    A GEMV's weights at ``READ``, else 10 us a step (a GEMV of attention reads a cache,
    no weight).
    """
    recording, _, _ = apply_profile(call.recording, Profile(), dev)
    times: dict[str, float] = {}
    for step in recording.steps:
        name = OperatorDesign(step.op.resolved(dev)).name
        weight = sum(h.nbytes for h in step.slots if h.role == "weight")
        us = weight / READ if isinstance(step.op, GEMV) and weight else 10.0
        times[name] = times.get(name, 0.0) + us
    return times


def test_a_gemv_reading_its_weights_at_the_rate_is_read_bound_and_codable():
    dev = aie_utils.ensure_current_device()
    call = decode_call()
    times = given_times(call, dev)
    codable = {Shape(s.op).key for s in call.recording.steps if isinstance(s.op, GEMV)}
    found = survey(call, Profile(), dev, times, CostModel(), codable)
    read = [d for d in found.designs if d.name.startswith("GEMV") and d.weight_bytes]
    assert read and all(d.bound == "weight-read" for d in read)
    assert all(d.bound == "other" for d in found.designs if d not in read)
    gemv_us = sum(d.us for d in read)
    assert 0 < found.estimates["coded"].us < 0.3 * gemv_us
    assert survey(call, Profile(), dev, times, CostModel()).estimates["coded"].us == 0


def test_the_switch_and_fold_estimates_follow_the_step_list():
    """Unpacked, every change of design is a switch the cost model prices; each scoped fold removes its consumer's step."""
    dev = aie_utils.ensure_current_device()
    call = decode_call()
    times = given_times(call, dev)
    model = CostModel()
    found = survey(call, Profile(), dev, times, model)
    names = [OperatorDesign(s.op.resolved(dev)).name for s in call.recording.steps]
    changes = sum(1 for a, b in zip(names, names[1:]) if a != b)
    assert found.switches == changes
    assert found.estimates["packing"].us == found.switch_us > 0
    removed = sum(
        len(f.steps) - 1 for f in array_scoped_fold_candidates(call.recording)
    )
    assert removed and found.estimates["folds"].us == pytest.approx(10.0 * removed)
    assert any("folds" in line for line in found.lines())
    # SiLU's output streams into the multiply: its round trip is what a stream saves.
    assert found.estimates["fusions"].us > 0


def test_a_read_bound_shape_is_worth_only_its_time_above_the_fastest_read():
    """A GEMV at the version's fastest read could gain nothing; one a quarter slower, that quarter; any other design its whole time.

    A faster read another version shows lowers every read-bound floor.
    """
    dev = aie_utils.ensure_current_device()
    call = decode_call()
    times = given_times(call, dev)
    first = survey(call, Profile(), dev, times, CostModel())
    gemvs = [d for d in first.designs if d.bound == "weight-read"]
    slow = gemvs[0]
    recording, _, _ = apply_profile(call.recording, Profile(), dev)
    for name in {
        OperatorDesign(s.op.resolved(dev)).name
        for s in recording.steps
        if Shape(s.op).key == slow.shape
    }:
        times[name] *= 1.25
    found = survey(call, Profile(), dev, times, CostModel())
    total = found.steps_us + found.switch_us
    shares = found.shares()
    assert found.read_rate == pytest.approx(READ)
    of = {
        key: sum(d.us for d in first.designs if d.shape == key)
        for key in {d.shape for d in gemvs}
    }
    assert shares[slow.shape] == pytest.approx(0.25 * of[slow.shape] / total)
    fast = [key for key in of if key != slow.shape]
    assert fast and all(shares[key] == pytest.approx(0.0) for key in fast)
    other = next(d for d in found.designs if d.bound == "other")
    assert shares[other.shape] >= other.us / total
    faster = found.shares(read_rate=2 * READ)
    assert faster[fast[0]] == pytest.approx(of[fast[0]] / 2 / total)


def test_a_tuned_attention_entry_applies_to_the_calls_it_was_tuned_for():
    """The decode step's and the prompt chunk's MHA differ only in what their calls derive.

    An entry without those would name both; one naming a derived dimension no call
    gives (``packed``) would name neither. Each entry names what its calls gave.
    """
    dev = aie_utils.ensure_current_device()
    model = small()
    model.profile = Profile()
    C = model.config.prefill_chunk
    decode, prompt = model.shapes()
    calls = [
        Timed(model.record(**decode), dict(position=0, token=0)),
        Timed(
            model.record(**prompt),
            dict(
                position=C - 1,
                token=0,
                start=0,
                rows=C,
                rope_start=model.rope_row(C, 0),
            ),
        ),
    ]
    resolved = [s.op.resolved(dev) for c in calls for s in c.recording.steps]
    found = [s for s in shapes(calls, dev) if s.cls is MHA]
    assert len(found) == 2
    for shape in found:
        recorded, *others = settings(shape.members[0][0], dev, shape.pinned)
        moved = next(s for s in others if s != recorded)
        model.profile = merged(
            Profile(), [(MHA, shape.entry([], frozenset(), resolved), moved)]
        )
        again = [
            s.op
            for shapes_ in model.shapes()
            for s in model.record(**shapes_).steps
            if isinstance(s.op, MHA)
        ]
        mine = [op for op in again if Shape(op).key == shape.key]
        assert mine and all(vars(op)[k] == v for op in mine for k, v in moved.items())
        assert all(
            any(vars(op)[k] != v for k, v in moved.items())
            for op in again
            if Shape(op).key != shape.key
        )


# ---------------------------------------------------------------------------
# On the device
# ---------------------------------------------------------------------------


class Chain(iron.Graph):
    def body(self, x):
        return Tanh.step(ReLU.step(x))


@pytest.mark.supported_devices("npu2")
def test_a_survey_times_each_design_of_a_version(tmp_path):
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    call = Timed(Chain().record(x=(2**20,)))
    times = step_times(
        call,
        Profile(),
        dev,
        full_elf=True,
        timing=Timing(rounds=2),
        repeats=5,
        cache=cache,
    )
    assert len(times) == 2 and all(t > 0 for t in times.values())
    found = survey(call, Profile(), dev, times, CostModel())
    assert {d.bound for d in found.designs} == {"other"} and found.switches == 1


@pytest.mark.supported_devices("npu2")
def test_a_long_step_is_timed_in_fewer_calls_a_round():
    """A survey times a prompt chunk's steps, hundreds of ms each.

    A round of one is sized by its duration, not a fixed call count.
    """
    timing = Timing(rounds=2)
    [long_step] = measure([ReLU(size=2**27)], full_elf=True, timing=timing).values()
    [short_step] = measure([ReLU(size=2**12)], full_elf=True, timing=timing).values()
    assert MIN_CALLS <= long_step.calls < timing.calls == short_step.calls


@pytest.mark.supported_devices("npu2")
def test_a_long_step_is_the_excess_of_two_runs_over_one():
    """A step past ``LONG_STEP_US`` dwarfs the dispatch the repeats cancel: its probes are two runs, not nine."""
    logged: list[str] = []
    op = GEMM(M=2048, K=4096, N=4096, precision="highest", num_aie_columns=1)
    [step] = measure(
        [op], full_elf=True, timing=Timing(rounds=2), log=logged.append
    ).values()
    assert any("probes of 2 runs" in line for line in logged), logged
    assert step.t_step_us > LONG_STEP_US / 2
