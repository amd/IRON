#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Buffers keep their own dtype in a full ELF.

The fused runtime sequence takes each argument as bytes and hands every
buffer to its sub-design as a view of the type that design declares. Here an
int32 gather runs after a bf16 add, so its buffers sit at non-zero offsets of
the input and output arguments, and its per-call offsets are element counts
the lowering scales by the view's element size: a buffer viewed as bf16 would
move them by half, and every row check below would miss.
"""

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

from iron.common.graph.trace import TracedGraph
from iron.common.image.fusion import Fusion
from iron.common.image.sequence import OperatorSequence
from iron.common.image.step import BufferRef
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.tests.common import sequences

ROWS, ROW, SLOTS = 16, 32, 4
TABLE_BYTES = ROWS * ROW * 4
ADD_SIZE = 4096


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _gather():
    """rows[out_offset:][:ROW] = table[in_offset:][:ROW], both per call, int32."""
    gather = Copy(
        input_buffer_size=ROWS * ROW,
        src=TensorAccessPattern((ROWS * ROW,), 0, [1, 1, 1, ROW], [0, 0, 0, 1]),
        output_buffer_size=SLOTS * ROW,
        dst=TensorAccessPattern((SLOTS * ROW,), 0, [1, 1, 1, ROW], [0, 0, 0, 1]),
        dtype=np.int32,
    )
    gather.use_value("in_offset")
    gather.use_value("out_offset")
    return gather


def _symbols(op):
    return {value.name: value.symbol for value in op.values}


def _check_gathers(run, gather, table):
    """Gather rows of ``table`` (what the device holds) into slots, one call
    at a time, checking every slot each time.
    """
    symbols = _symbols(gather)
    rows = run.get_buffer(BufferRef("rows"))
    rows.numpy_view()[:] = -1
    rows.to("npu")
    expected = np.full((SLOTS, ROW), -1, dtype=np.int32)
    for row, slot in ((0, 0), (5, 3), (ROWS - 1, 1), (7, 2)):
        run.write_values(
            {
                symbols["in_offset"]: np.int32(row * ROW),
                symbols["out_offset"]: np.int32(slot * ROW),
            }
        )
        run()
        expected[slot] = table[row]
        got = (
            run.get_buffer(BufferRef("rows")).numpy()[: SLOTS * ROW].reshape(SLOTS, ROW)
        )
        assert np.array_equal(got, expected), (
            f"row {row} into slot {slot}: slots hold {got[:, 0].tolist()}, "
            f"expected {expected[:, 0].tolist()}"
        )


@pytest.mark.supported_devices("npu2")
def test_int32_step_at_nonzero_offsets():
    add = ElementwiseAdd(size=ADD_SIZE, tile_size=1024, num_aie_columns=4)
    gather = _gather()
    traced = TracedGraph.of_steps(
        "infra_fused_int32_gather",
        sequences.steps((add, "a", "b", "c"), (gather, "table", "rows")),
        ["a", "b", "table"],
        ["c", "rows"],
    )
    seq = OperatorSequence(traced, full_elf=True).compile()
    kinds = {name: seq.layout[name][:2] for name in ("table", "rows")}
    assert kinds["table"][0] == "input" and kinds["table"][1] > 0, kinds
    assert kinds["rows"][0] == "output" and kinds["rows"][1] > 0, kinds

    run = seq.get_callable()
    assert run.get_buffer(BufferRef("table")).dtype == np.int32
    assert run.get_buffer(BufferRef("c")).dtype == bfloat16

    rng = np.random.default_rng(0)
    a = rng.standard_normal(ADD_SIZE).astype(bfloat16)
    b = rng.standard_normal(ADD_SIZE).astype(bfloat16)
    run.get_buffer(BufferRef("a")).numpy_view()[:] = a
    run.get_buffer(BufferRef("b")).numpy_view()[:] = b
    # Every value distinct, so a row landing anywhere else shows.
    table = np.arange(ROWS * ROW, dtype=np.int32).reshape(ROWS, ROW)
    run.get_buffer(BufferRef("table")).numpy_view()[:] = table.reshape(-1)
    _check_gathers(run, gather, table)

    c = run.get_buffer(BufferRef("c")).numpy()[:ADD_SIZE]
    verdict = compare(c, a + b, Tolerance.relative(0.04, 1e-6))
    assert verdict, f"the bf16 step beside the int32 one: {verdict.detail}"


@pytest.mark.supported_devices("npu2")
def test_int32_slice_at_word_offset():
    """A slice starting 36 bytes into its parent: a whole number of int32
    words, and not on the 64-byte granule an arena buffer is placed at.
    """
    start = 36
    gather = _gather()
    traced = TracedGraph.of_steps(
        "infra_fused_int32_slice",
        sequences.steps((gather, BufferRef("packed", start, TABLE_BYTES), "rows")),
        ["packed"],
        ["rows"],
        pinned={"packed": TABLE_BYTES + 64},
    )
    seq = OperatorSequence(traced, full_elf=True).compile()
    run = seq.get_callable()
    packed = run.get_buffer(BufferRef("packed"))
    assert packed.dtype == np.int32, "a parent of int32 slices is viewed as int32"
    words = start // 4
    table = np.arange(ROWS * ROW, dtype=np.int32).reshape(ROWS, ROW)
    packed.numpy_view()[:] = -7
    packed.numpy_view()[words : words + ROWS * ROW] = table.reshape(-1)
    _check_gathers(run, gather, table)


def test_misaligned_buffer_is_rejected():
    """A buffer the shim DMA cannot start on fails at fusion, not silently on
    the device (whose descriptor would drop the low address bits).
    """
    gather = _gather()
    traced = TracedGraph.of_steps(
        "infra_fused_int32_misaligned",
        sequences.steps((gather, BufferRef("packed", 34, TABLE_BYTES), "rows")),
        ["packed"],
        ["rows"],
        pinned={"packed": TABLE_BYTES + 64},
    )
    seq = OperatorSequence(traced, full_elf=True)
    seq.prepare()
    with pytest.raises(ValueError, match="not a multiple of 4"):
        Fusion(seq).text()
