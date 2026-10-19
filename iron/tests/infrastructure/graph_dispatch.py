#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A graph function must compile and run, not merely record.

The device-free tests stop at the recording: the runlist, the names, the plan.
This file checks the claim that matters -- that a graph recorded from
ordinary Python dataflow produces the same numbers as the hand-written
runlist for the same computation -- both ahead of time (``compile()``
before any dispatch) and just in time (dispatching without compiling).
Both must agree with the hand-written sequence bit for bit: a layout
change that quietly aliased two live buffers shows up here and nowhere
else, because it produces wrong values rather than an error.
"""

import logging
import re

import dataclasses

import numpy as np
import pytest
from aie.utils.compile.jit.compilabledesign import CompilableDesign
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.common.image import AdjacentPacking
from iron.common.image.compose import Composition
from iron.common.graph.record import Recording
from iron.common.image.link import FullELF, PerStep
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef
from iron.operators import (
    GEMV,
    Copy,
    ElementwiseAdd,
    Merge,
    PatchPositions,
    Resample,
    ResampleTaps,
)
from iron.operators.magnitude import Magnitude
from iron.operators.merge import GEMMA
from iron.tests.support.graphs import Adds, Chain
from iron.tests.support import sequences

SIZE = 1024
TILE = 128


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _operator():
    return ElementwiseAdd(size=SIZE, tile_size=TILE)


PACKAGINGS = {"separate": PerStep, "composed": FullELF}


def _graph(name, packaging="composed"):
    """X + w + w + w, recorded from dataflow, as the sequence it lowers to."""
    recording = Adds(_operator(), 3).record(x=(SIZE,), w=(SIZE,))
    return recording, Image(
        dataclasses.replace(recording, name=name), PACKAGINGS[packaging]()
    )


def _hand_written(name, packaging="composed"):
    """The same computation, with the buffer names written out."""
    add = _operator()
    runlist = [
        (add, "x", "w", "t0"),
        (add, "t0", "w", "t1"),
        (add, "t1", "w", "out"),
    ]
    recording = Recording.of_steps(name, sequences.steps(*runlist), ["x", "w"], ["out"])
    return Image(recording, PACKAGINGS[packaging]())


def test_a_graph_records_the_same_steps_as_a_hand_written_runlist():
    """Same operators, same order, same wiring -- only the names differ."""
    _, graph = _graph("graph_steps")
    hand = _hand_written("hand_steps")

    def shape(sequence):
        # Compare structure, not generated names: for each step, which earlier
        # step produced each of its inputs (None meaning a graph input).
        produced, shaped = {}, []
        for index, step in enumerate(sequence):
            *reads, write = step.buffers
            shaped.append((type(step.op).__name__, [produced.get(r) for r in reads]))
            produced[write] = index
        return shaped

    assert shape(graph.steps) == shape(hand.steps)


def test_a_graph_names_its_io_from_the_function():
    recording, seq = _graph("graph_io")
    assert [h.name for h in recording.inputs] == ["x", "w"]
    assert [h.name for h in recording.outputs] == ["out"]
    assert seq.inputs == ["x", "w"] and seq.outputs == ["out"]


def _run(sequence, inputs):
    """Fill the named inputs, dispatch, and read the output back."""
    run = sequence.get_callable()
    (out,) = sequence.outputs
    for name, data in zip(sequence.inputs, inputs):
        run.get_buffer(BufferRef(name)).numpy_view()[: data.size] = data.reshape(-1)
    run()
    return run.get_buffer(BufferRef(out)).numpy()[: inputs[0].size].copy()


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("dispatch", PACKAGINGS)
@pytest.mark.parametrize("precompile", [True, False], ids=["aot", "jit"])
def test_a_graph_matches_the_hand_written_runlist_numerically(precompile, dispatch):
    """The load-bearing claim, both ahead-of-time and just-in-time."""
    rng = np.random.default_rng(0)
    x = rng.random(SIZE, dtype=np.float32)
    w = rng.random(SIZE, dtype=np.float32)

    _, graph_seq = _graph(f"graph_num_{precompile}_{dispatch}", dispatch)
    hand = _hand_written(f"hand_num_{precompile}_{dispatch}", dispatch)
    if precompile:
        graph_seq.compile()
        hand.compile()

    got = _run(graph_seq, (x, w))
    expected = _run(hand, (x, w))
    assert np.array_equal(got, expected), (
        "a graph must compute exactly what the hand-written runlist computes; "
        "a difference here means the recorded wiring or the planned layout is wrong"
    )


@pytest.mark.supported_devices("npu2")
def test_check_mode_holds_each_step_to_its_reference(caplog):
    """compile(check=True) dispatches each step on its own and holds what it
    wrote to its reference on the NPU's inputs: a graph within its steps'
    tolerances runs, judges every step, and computes what the full ELF does.
    A step outside its tolerance raises (iron/tests/common/checking.py).
    """
    rng = np.random.default_rng(0)
    a = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    b = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    checked = Chain(SIZE, TILE).compile(check=True, a=(SIZE,), b=(SIZE,))
    assert not checked.plan.full_elf
    with caplog.at_level(logging.INFO, logger="iron.common.image.callable"):
        got = np.array(checked(a, b).numpy()[:SIZE])
    judged = sorted({int(i) for i in re.findall(r"\[check step (\d+)\]", caplog.text)})
    assert judged == list(range(len(checked.recording.steps))), caplog.text
    plain = Chain(SIZE, TILE).compile(full_elf=True, a=(SIZE,), b=(SIZE,))
    want = np.array(plain(a, b).numpy()[:SIZE])
    assert got.view(np.uint16).tolist() == want.view(np.uint16).tolist()


class RoundedMagnitude(Magnitude):
    """Magnitude declared to round correctly, which its kernel does not: it
    comes within 2e-7 of hypot, about a float32 ulp.
    """

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()


class Magnitudes(iron.Graph):
    """Two magnitudes in turn, the second held to a bound its kernel misses."""

    def body(self, x):
        return RoundedMagnitude.step(
            Magnitude.step(x, num_aie_columns=1), num_aie_columns=1
        )


@pytest.mark.supported_devices("npu2")
def test_check_mode_catches_a_step_outside_its_tolerance_at_that_step():
    """A step whose kernel misses its declared bound on the device is caught
    at that step, after the step before it passed.

    A wrong weight cannot stand in here: check mode judges each step against
    its reference on the inputs the NPU gave it, so a wrong weight in a
    device buffer is what both read. What a step catches is a kernel outside
    its operator's tolerance(), as iron/tests/common/checking.py induces on
    the host.
    """
    rows, width = 8, 640
    rng = np.random.default_rng(0)
    x = (rng.standard_normal((rows, width)) * 10.0).astype(np.float32)
    net = Magnitudes().compile(check=True, x=((rows, width), np.float32))
    with pytest.raises(
        RuntimeError, match=r"\[check step 1\] RoundedMagnitude .*deviates"
    ):
        net(x)


@pytest.mark.supported_devices("npu2")
def test_a_packed_graph_computes_what_the_temporal_one_does():
    """compile(coresident=...) changes which device each step runs in, and
    nothing it computes.
    """
    rng = np.random.default_rng(0)
    a = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    b = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    outputs, configures = [], []
    for coresident in (None, AdjacentPacking()):
        version = Chain(SIZE, TILE, columns=2).compile(
            full_elf=True, coresident=coresident, a=(SIZE,), b=(SIZE,)
        )
        text = Composition(version.sequence).text()
        configures.append(len(re.findall(r"aiex\.configure", text)))
        outputs.append(np.array(version(a, b).numpy()[:SIZE]))
    # A configure per change of design and the reset, against one pack and
    # the reset: the policy must have packed, or this compares two temporals.
    assert configures == [6, 2]
    temporal, packed = outputs
    assert temporal.view(np.uint16).tolist() == packed.view(np.uint16).tolist()


class TwoExtents(iron.Graph):
    """One full-width add at two extents: two designs, one array."""

    def body(self, a, b, c, d):
        wide = dict(tile_size=TILE, num_aie_columns=8)
        t = ElementwiseAdd.step(a, b, **wide)
        u = ElementwiseAdd.step(c, d, **wide)
        return ElementwiseAdd.step(t, b, **wide), u


@pytest.mark.supported_devices("npu2")
def test_designs_of_one_array_run_on_one_configure():
    rng = np.random.default_rng(0)
    a, b = ((rng.random(SIZE) * 4 - 2).astype(bfloat16) for _ in range(2))
    c, d = ((rng.random(2 * SIZE) * 4 - 2).astype(bfloat16) for _ in range(2))
    shapes = dict(a=(SIZE,), b=(SIZE,), c=(2 * SIZE,), d=(2 * SIZE,))
    shared = TwoExtents().compile(full_elf=True, **shapes)
    text = Composition(shared.sequence).text()
    # Against small, large, small and the reset, were each design its own device.
    assert len(re.findall(r"aiex\.configure", text)) == 2
    assert len(re.findall(r"aiex\.run", text)) == 3

    alone = TwoExtents().compile(full_elf=False, **shapes)
    tolerance = shared.sequence.steps[0].op.resolved().tolerance()
    want = TwoExtents().reference(a, b, c, d)
    runs = [
        [np.array(t.numpy()[: len(w)]) for t, w in zip(v(a, b, c, d), want)]
        for v in (shared, alone)
    ]
    for got, expected in zip(runs[0], want):
        verdict = compare(got, np.asarray(expected), tolerance)
        assert verdict, verdict.detail
    for got, expected in zip(*runs):
        assert got.view(np.uint16).tolist() == expected.view(np.uint16).tolist()


class TwoProjections(iron.Graph):
    """Two GEMVs of one array, the narrower first, each on a vector of its own."""

    def __init__(self, narrow, wide):
        self.narrow, self.wide = narrow, wide

    def body(self, x, y):
        tiles = dict(num_aie_columns=8, tile_size_input=4, tile_size_output=32)
        return GEMV.step(self.narrow, x, **tiles), GEMV.step(self.wide, y, **tiles)


@pytest.mark.supported_devices("npu2")
def test_each_design_of_one_array_runs_on_its_own_values():
    """The second design's cores read its trip count, not the first's.

    The cores of a shared device are not reset between its sequences, so a
    core that read its values once would run the wide GEMV at the narrow
    one's trip count.
    """
    K = 2048
    rng = np.random.default_rng(0)
    narrow, wide = (
        (rng.standard_normal((m, K)) / np.sqrt(K)).astype(bfloat16) for m in (512, 2048)
    )
    graph = TwoProjections(narrow, wide)
    net = graph.compile(full_elf=True, x=(K,), y=(K,))
    text = Composition(net.sequence).text()
    assert (
        len(re.findall(r"aiex\.configure", text)) == 2
    )  # the shared device, the reset
    assert len(re.findall(r"aiex\.run", text)) == 2
    tolerance = net.sequence.steps[0].op.resolved().tolerance()
    for _ in range(2):
        x, y = (rng.standard_normal(K).astype(bfloat16) for _ in range(2))
        for got, want in zip(net(x, y), graph.reference(x, y)):
            want = np.asarray(want)
            verdict = compare(np.array(got.numpy()[: len(want)]), want, tolerance)
            assert verdict, verdict.detail


class TwoMerges(iron.Graph):
    """Two Merges of one array, the shorter first, each on ids of its own."""

    def body(self, ids, more):
        return Merge.step(ids, placeholders=GEMMA), Merge.step(more, placeholders=GEMMA)


@pytest.mark.supported_devices("npu2")
def test_each_merge_of_one_array_runs_on_its_own_count():
    rng = np.random.default_rng(0)
    graph = TwoMerges()
    net = graph.compile(full_elf=True, ids=((64,), np.int32), more=((192,), np.int32))
    text = Composition(net.sequence).text()
    assert len(re.findall(r"aiex\.configure @(\w+)", text)) == 1
    assert len(re.findall(r"aiex\.run", text)) == 2
    for _ in range(2):
        ids, more = (
            np.where(
                rng.random(n) < 1 / 3,
                rng.choice([t for t, _ in GEMMA], n),
                rng.integers(0, 2**20, n),
            ).astype(np.int32)
            for n in (64, 192)
        )
        for got, want in zip(net(ids, more), graph.reference(ids, more)):
            want = np.asarray(want)
            np.testing.assert_array_equal(np.array(got.numpy()[: len(want)]), want)


class TwoTables(iron.Graph):
    """Two ResampleTaps of one array, the shorter table first."""

    def __init__(self):
        taps = dict(words=356, slots=16)
        self.taps_h = ResampleTaps(in_size=3024, out_size=672, **taps)
        self.taps_w = ResampleTaps(in_size=4032, out_size=912, **taps)

    def body(self):
        return self.taps_h.apply(), self.taps_w.apply()


@pytest.mark.supported_devices("npu2")
def test_each_table_of_one_array_runs_on_its_own_sizes():
    graph = TwoTables()
    net = graph.compile(full_elf=True)
    text = Composition(net.sequence).text()
    assert len(re.findall(r"aiex\.configure @(\w+)", text)) == 1
    assert len(re.findall(r"aiex\.run", text)) == 2
    for _ in range(2):
        for got, want in zip(net(), graph.reference()):
            want = np.asarray(want)
            np.testing.assert_array_equal(
                np.array(got.numpy()).reshape(want.shape), want
            )


class TwoPositions(iron.Graph):
    """Two PatchPositions of one array, the fewer rows first."""

    def __init__(self):
        self.few = PatchPositions(rows=256, out_height=96, out_width=96)
        self.many = PatchPositions(rows=512, out_height=96, out_width=96)

    def body(
        self,
        *,
        out_height: Scratchpad[np.int32],
        out_width: Scratchpad[np.int32],
    ):
        return (
            *self.few.apply(out_rows=out_height, out_columns=out_width),
            *self.many.apply(out_rows=out_height, out_columns=out_width),
        )


@pytest.mark.supported_devices("npu2")
def test_each_position_table_of_one_array_runs_on_its_own_rows():
    graph = TwoPositions()
    net = graph.compile(full_elf=True)
    text = Composition(net.sequence).text()
    assert len(re.findall(r"aiex\.configure @(\w+)", text)) == 1
    assert len(re.findall(r"aiex\.run", text)) == 2
    for sizes in (
        dict(out_height=96, out_width=48),
        dict(out_height=48, out_width=96),
    ):
        for got, want in zip(net(**sizes), graph.reference(**sizes)):
            want = np.asarray(want)
            np.testing.assert_array_equal(
                np.array(got.numpy()).reshape(want.shape), want
            )


class TwoResizes(iron.Graph):
    """Two Resamples of one array, the narrower first, as two images' would be."""

    def __init__(self):
        size = dict(height=37, width=53, out_height=96, num_aie_columns=8)
        self.narrow = dict(size, out_width=144)
        self.wide = dict(size, out_width=256)

    def body(self, rgb, taps_w, taps_h, wide_w):
        return (
            Resample.step(rgb, taps_w, taps_h, **self.narrow),
            Resample.step(rgb, wide_w, taps_h, **self.wide),
        )


@pytest.mark.supported_devices("npu2")
def test_each_resize_of_one_array_runs_on_its_own_sizes():
    graph = TwoResizes()
    taps = [
        ResampleTaps(
            in_size=n_in, out_size=n_out, words=356, slots=16, chunks=16
        ).reference()
        for n_in, n_out in ((53, 144), (37, 96), (53, 256))
    ]
    rgb = np.random.default_rng(0).integers(0, 256, (37, 4096), dtype=np.uint8)
    net = graph.compile(
        full_elf=True,
        **{
            name: (t.shape, t.dtype.type)
            for name, t in zip(("rgb", "taps_w", "taps_h", "wide_w"), (rgb, *taps))
        },
    )
    text = Composition(net.sequence).text()
    assert len(re.findall(r"aiex\.configure @(\w+)", text)) == 1
    assert len(re.findall(r"aiex\.run", text)) == 2
    for _ in range(2):
        for got, want in zip(net(rgb, *taps), graph.reference(rgb, *taps)):
            want = np.asarray(want)
            np.testing.assert_array_equal(
                np.array(got.numpy()).reshape(want.shape).view(np.uint16),
                want.view(np.uint16),
            )


@pytest.mark.supported_devices("npu2")
def test_a_chain_of_more_designs_than_a_context_configures_runs():
    """Past the kernels one hardware context configures, the steps' designs
    go into a second xclbin, and every step still runs.
    """
    n = CompilableDesign.XCLBIN_KERNELS + 2

    class Prefixes(iron.Graph):
        def body(self, x):
            return tuple(Copy.step(x[: SIZE * (i + 1)]) for i in range(n))

    graph = Prefixes()
    graph.compile(x=(SIZE * n,), full_elf=False)
    x = np.arange(SIZE * n).astype(bfloat16)
    for i, got in enumerate(graph(x)):
        np.testing.assert_array_equal(np.asarray(got), x[: SIZE * (i + 1)])
