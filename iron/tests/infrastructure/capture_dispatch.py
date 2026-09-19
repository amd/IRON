#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A captured graph must compile and run, not merely record.

Every other capture test stops at the recording: it checks the runlist, the
inferred I/O, the plan. Those are all statements about bookkeeping. This file
checks the claim that actually matters -- that a graph recorded from ordinary
Python dataflow produces the same numbers as the hand-written runlist for the
same computation -- and it checks it both ways a caller can get there:

* **ahead of time**, by calling ``compile()`` before any dispatch, and
* **just in time**, by dispatching without compiling first.

Both must work, and both must agree with the hand-written sequence bit for
bit. A layout change that quietly aliased two live buffers would show up here
and nowhere else, because it produces wrong values rather than an error.
"""

import numpy as np
import pytest

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.common.capture import capture
from iron.common.context import AIEContext
from iron.common.sequence import OperatorSequence
from iron.operators import ElementwiseAdd

SIZE = 1024
TILE = 128


@pytest.fixture(autouse=True)
def device():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


def _operator():
    return ElementwiseAdd(size=SIZE, tile_size=TILE, context=AIEContext())


def _captured(name, **kwargs):
    """x + w + w + w, recorded from dataflow."""
    add = _operator()
    with capture() as g:
        x = g.input("x")
        w = g.input("w")
        value = g(add, x, w)
        value = g(add, value, w)
        value = g(add, value, w)
    kwargs.setdefault("dispatch", "reference")
    return g, g.build(name, **kwargs)


def _hand_written(name, **kwargs):
    """The same computation, with the buffer names written out."""
    add = _operator()
    runlist = [
        (add, "x", "w", "t0"),
        (add, "t0", "w", "t1"),
        (add, "t1", "w", "out"),
    ]
    return OperatorSequence(
        name,
        runlist,
        input_args=["x", "w"],
        output_args=["out"],
        **{"dispatch": "reference", **kwargs},
    )


def test_capture_records_the_same_steps_as_a_hand_written_runlist():
    """Same operators, same order, same wiring -- only the names differ."""
    graph, _ = _captured("cap_steps")
    hand = _hand_written("hand_steps")

    def shape(runlist):
        # Compare structure, not generated names: for each step, which earlier
        # step produced each of its inputs (None meaning a graph input).
        produced, steps = {}, []
        for index, (operator, *buffers) in enumerate(runlist):
            *reads, write = buffers
            steps.append((type(operator).__name__, [produced.get(r) for r in reads]))
            produced[write] = index
        return steps

    assert shape(graph.runlist) == shape(hand.runlist)


def test_capture_infers_the_same_io():
    graph, _ = _captured("cap_io")
    inputs, outputs = graph.infer_io()
    assert len(inputs) == 2 and len(outputs) == 1


def test_capture_plans_scratch_by_default():
    """build() pools intermediates unless asked not to."""
    _, pooled = _captured("cap_pooled")
    _, unpooled = _captured("cap_unpooled", pool_scratch=False)
    assert pooled.buffer_offsets, "build() should plan scratch by default"
    assert unpooled.buffer_offsets is None


def _run(sequence, inputs):
    """Fill the named inputs, dispatch, and read the output back.

    Buffers are addressed by name even for a captured graph -- the names are
    generated rather than typed, but the host still writes and reads through
    them, so a test has to ask the sequence which ones they are.
    """
    run = sequence.get_callable()
    names, (out_name,) = sequence.input_args, sequence.output_args
    for name, data in zip(names, inputs):
        run.get_buffer(name).torch_view()[: data.numel()] = data.reshape(-1)
    run()
    return run.get_buffer(out_name).torch_view()[: inputs[0].numel()].clone()


@pytest.mark.parametrize("dispatch", ["reference", "fused"])
@pytest.mark.parametrize("precompile", [True, False], ids=["aot", "jit"])
def test_captured_graph_matches_hand_written_numerically(precompile, dispatch):
    """The load-bearing claim, both ahead-of-time and just-in-time.

    ``precompile=True`` compiles before any dispatch; ``False`` leaves it to
    the first call. Neither may change the answer.
    """
    import torch

    torch.manual_seed(0)
    x = torch.rand(SIZE, dtype=torch.float32)
    w = torch.rand(SIZE, dtype=torch.float32)

    _, captured = _captured(f"cap_num_{precompile}_{dispatch}", dispatch=dispatch)
    hand = _hand_written(f"hand_num_{precompile}_{dispatch}", dispatch=dispatch)
    if precompile:
        captured.compile()
        hand.compile()

    got = _run(captured, (x, w))
    expected = _run(hand, (x, w))
    import torch as _t

    assert _t.equal(got, expected), (
        "a captured graph must compute exactly what the hand-written "
        "runlist computes; a difference here means the recorded wiring or the "
        "planned layout is wrong",
    )
