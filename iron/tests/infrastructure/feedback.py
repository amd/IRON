#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A full ELF's feedback argument, on a device.

The image gathers one row of a table, at a per-call offset, and drains two
words of that row into its feedback argument. Bound to another run's ctrl
scratchpad, those words are that run's per-call values: each row names the
next one's offset, so a chain of runs walks the table with the host seeding
only the first. The table's successor is a single cycle through every row,
so a run that read a stale or misplaced offset lands on the wrong row.
"""

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
from aie.utils.trace import TraceConfig, get_trace_buffer
from ml_dtypes import bfloat16

from iron.common.design import device_symbol
from iron.common.image import Fusion, OperatorSequence
from iron.operators import LayerNorm
from iron.operators.copy import Copy

ROWS, ROW = 8, 8
# Where in a row the next row's offset is, and the word after it (zero): the
# two words the image feeds back.
NEXT = ROW - 2
LN_SIZE = 2048
TRACE_SIZE = 8192


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _copy(n, buffer_in, buffer_out, per_call_input=False):
    """An int32 copy of ``n`` words; with ``per_call_input``, from a per-call
    element offset into its ``buffer_in``-word input.
    """
    copy = Copy(
        input_buffer_size=buffer_in,
        src=TensorAccessPattern((buffer_in,), 0, [1, 1, 1, n], [0, 0, 0, 1]),
        output_buffer_size=buffer_out,
        dst=TensorAccessPattern((buffer_out,), 0, [1, 1, 1, n], [0, 0, 0, 1]),
        dtype=np.int32,
    )
    if per_call_input:
        copy.use_value("in_offset")
    return copy


def _chain_table(seed=0):
    """Row r holds distinct words, with the offset of successor[r] at NEXT;
    successor is one cycle through every row.
    """
    order = np.random.default_rng(seed).permutation(ROWS)
    successor = np.empty(ROWS, dtype=np.int64)
    successor[order] = np.roll(order, -1)
    table = (np.arange(ROWS)[:, None] * 100 + np.arange(ROW)[None, :]).astype(np.int32)
    table[:, NEXT] = successor * ROW
    table[:, NEXT + 1] = 0
    return table, successor


def _feedback_sequence(name, layer_norm=None):
    """Row = table[offset:][:ROW]; next = row[NEXT:NEXT + 2], fed back.

    With ``layer_norm``, a traced step ahead of the two, so the image also
    takes the trace argument, after the feedback one.
    """
    gather = _copy(ROW, ROWS * ROW, ROW, per_call_input=True)
    tail = _copy(2, 2, 2)
    runlist = [
        (gather, "table", "row"),
        (tail, f"row[{NEXT * 4}:{ROW * 4}]", "next"),
    ]
    input_args, output_args = ["table"], ["row"]
    if layer_norm is not None:
        runlist.insert(0, (layer_norm, "x", "y"))
        input_args, output_args = ["x", *input_args], ["y", *output_args]
    seq = OperatorSequence(
        name=name,
        runlist=runlist,
        input_args=input_args,
        output_args=output_args,
        feedback_args=["next"],
        dispatch="fused",
    )
    return seq, gather


def _setup(seq, table):
    seq.compile()
    assert seq.subbuffer_layout["next"] == ("feedback", 0, 8)
    assert seq.buffer_sizes.feedback == 8
    run = seq.get_callable()
    run.get_buffer("table").numpy_view()[:] = table.reshape(-1)
    return run


def _row(run):
    return run.get_buffer("row").numpy()[:ROW]


@pytest.mark.supported_devices("npu2")
def test_feedback_into_plain_buffers(npu_runtime):
    """Unbound, the argument is the callable's own buffer; bound, the caller's."""
    table, successor = _chain_table()
    seq, gather = _feedback_sequence("infra_feedback_plain")
    run = _setup(seq, table)
    offset = device_symbol(gather, gather.values[0])

    run.write_values({offset: np.int32(3 * ROW)})
    run()
    assert np.array_equal(_row(run), table[3])
    fed = run.feedback_buffer.numpy().view(np.int32)
    assert fed.tolist() == [successor[3] * ROW, 0], fed

    mine = XRTTensor((2,), dtype=np.int32)
    mine.numpy_view()[:] = -1
    mine.to("npu")
    run.run.bind_feedback(mine.buffer_object())
    run.write_values({offset: np.int32(6 * ROW)})
    run()
    assert np.array_equal(_row(run), table[6])
    mine.device = "npu"
    assert mine.numpy().tolist() == [successor[6] * ROW, 0]
    # The callable's own buffer was not written by the second run.
    assert run.feedback_buffer.numpy().view(np.int32)[0] == successor[3] * ROW


@pytest.mark.supported_devices("npu2")
def test_feedback_ping_pong(npu_runtime):
    """Two runs feeding each other, dispatched one at a time: the host seeds
    the first run once, and every later offset comes from the device.
    """
    table, successor = _chain_table(seed=1)
    seq, gather = _feedback_sequence("infra_feedback_ping_pong")
    run = _setup(seq, table)
    offset = device_symbol(gather, gather.values[0])

    first, second = run.run, run.new_run()
    first.bind_feedback(second.scratchpad_alias())
    second.bind_feedback(first.scratchpad_alias())
    row = 5
    first.write_values({offset: np.int32(row * ROW)})
    for k in range(2 * ROWS + 1):
        run((first, second)[k % 2])
        assert np.array_equal(_row(run), table[row]), f"dispatch {k}: not row {row}"
        row = successor[row]
        fed_into = (second, first)[k % 2]
        assert fed_into.read_value(offset) == row * ROW


@pytest.mark.supported_devices("npu2")
def test_feedback_chain_queued(npu_runtime):
    """Every run started before any is waited on: each reads the offset the
    one before it drained, with no host step between them.
    """
    table, successor = _chain_table(seed=2)
    seq, gather = _feedback_sequence("infra_feedback_queued")
    run = _setup(seq, table)
    offset = device_symbol(gather, gather.values[0])

    runs = [run.run, *(run.new_run() for _ in range(ROWS + 2))]
    for producer, consumer in zip(runs, runs[1:]):
        producer.bind_feedback(consumer.scratchpad_alias())
    start = 2
    runs[0].write_values({offset: np.int32(start * ROW)})
    run(*runs)

    rows = [start]
    for _ in runs[1:]:
        rows.append(successor[rows[-1]])
    for k, (consumer, row) in enumerate(zip(runs[1:], rows[1:])):
        assert consumer.read_value(offset) == row * ROW, f"run {k + 1}"
    # The runs share the row buffer, so it holds the last one's; the last
    # drains into the callable's own feedback buffer.
    assert np.array_equal(_row(run), table[rows[-1]])
    fed = run.feedback_buffer.numpy().view(np.int32)
    assert fed.tolist() == [successor[rows[-1]] * ROW, 0]


@pytest.mark.supported_devices("npu2")
def test_feedback_with_trace(npu_runtime):
    """The trace argument moves after the feedback one, and both still work."""
    layer_norm = LayerNorm(
        rows=1,
        num_aie_columns=1,
        num_channels=1,
        tile_size=LN_SIZE,
        trace=TraceConfig(TRACE_SIZE),
    )
    table, successor = _chain_table(seed=3)
    seq, gather = _feedback_sequence("infra_feedback_traced", layer_norm)
    run = _setup(seq, table)
    offset = device_symbol(gather, gather.values[0])
    layout = get_trace_buffer(run.lowered_mlir_path.read_text(), "main:sequence")
    assert layout["arg_index"] == 4, layout

    x = np.random.default_rng(0).standard_normal(LN_SIZE).astype(bfloat16)
    run.get_buffer("x").numpy_view()[:] = x
    first, second = run.run, run.new_run()
    first.bind_feedback(second.scratchpad_alias())
    first.write_values({offset: np.int32(1 * ROW)})
    run(first, second)
    assert np.array_equal(_row(run), table[successor[1]])
    assert run.feedback_buffer.numpy().view(np.int32)[0] == (
        successor[successor[1]] * ROW
    )
    assert run.trace_buffer.numpy().view(np.uint32).any(), "no trace data"


def test_feedback_argument_only_when_declared():
    """An image without feedback takes the three arguments it always did."""
    tail = _copy(2, 2, 2)
    for feedback, arguments in (([], 3), (["next"], 4)):
        seq = OperatorSequence(
            name="infra_feedback_arguments",
            runlist=[(tail, "a", "b"), (tail, "b", "next")],
            input_args=["a"],
            output_args=["b"] if feedback else ["b", "next"],
            feedback_args=feedback,
            dispatch="fused",
        )
        seq.subbuffer_layout, seq.buffer_sizes, seq.slice_info = (
            seq.calculate_buffer_layout()
        )
        # The main device's runtime sequence is the last one in the module.
        header = [
            line
            for line in Fusion(seq).text().splitlines()
            if "aie.runtime_sequence" in line
        ][-1]
        assert header.count("memref<") == arguments, header
