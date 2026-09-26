#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A graph function must compile and run, not merely trace.

The device-free tests stop at the trace: the runlist, the names, the plan.
This file checks the claim that matters -- that a graph traced from
ordinary Python dataflow produces the same numbers as the hand-written
runlist for the same computation -- both ahead of time (``compile()``
before any dispatch) and just in time (dispatching without compiling).
Both must agree with the hand-written sequence bit for bit: a layout
change that quietly aliased two live buffers shows up here and nowhere
else, because it produces wrong values rather than an error.
"""

import pytest

import iron
from iron.common.image import OperatorSequence
from iron.operators import ElementwiseAdd

SIZE = 1024
TILE = 128


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _operator():
    return ElementwiseAdd(size=SIZE, tile_size=TILE)


def _graph(name, **kwargs):
    """X + w + w + w, traced from dataflow, as the sequence it lowers to."""
    add = _operator()

    @iron.graph
    def f(x, w):
        return add(add(add(x, w), w), w)

    traced = f.trace(x=(SIZE,), w=(SIZE,))
    kwargs.setdefault("dispatch", "reference")
    return traced, traced.sequence(name, **kwargs)


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


def test_a_graph_records_the_same_steps_as_a_hand_written_runlist():
    """Same operators, same order, same wiring -- only the names differ."""
    traced, _ = _graph("graph_steps")
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

    assert shape(traced.runlist) == shape(hand.runlist)


def test_a_graph_names_its_io_from_the_function():
    traced, seq = _graph("graph_io")
    assert traced.input_args == ["x", "w"] and traced.output_args == ["out"]
    assert seq.plan_scratch, "the lowered sequence pools intermediates by default"


def _run(sequence, inputs):
    """Fill the named inputs, dispatch, and read the output back."""
    run = sequence.get_callable()
    names, (out_name,) = sequence.input_args, sequence.output_args
    for name, data in zip(names, inputs):
        run.get_buffer(name).torch_view()[: data.numel()] = data.reshape(-1)
    run()
    return run.get_buffer(out_name).torch_view()[: inputs[0].numel()].clone()


@pytest.mark.parametrize("dispatch", ["reference", "fused"])
@pytest.mark.parametrize("precompile", [True, False], ids=["aot", "jit"])
def test_a_graph_matches_the_hand_written_runlist_numerically(precompile, dispatch):
    """The load-bearing claim, both ahead-of-time and just-in-time."""
    import torch

    torch.manual_seed(0)
    x = torch.rand(SIZE, dtype=torch.float32)
    w = torch.rand(SIZE, dtype=torch.float32)

    _, graph_seq = _graph(f"graph_num_{precompile}_{dispatch}", dispatch=dispatch)
    hand = _hand_written(f"hand_num_{precompile}_{dispatch}", dispatch=dispatch)
    if precompile:
        graph_seq.compile()
        hand.compile()

    got = _run(graph_seq, (x, w))
    expected = _run(hand, (x, w))
    assert torch.equal(got, expected), (
        "a graph must compute exactly what the hand-written runlist computes; "
        "a difference here means the traced wiring or the planned layout is wrong"
    )
