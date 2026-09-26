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
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.common.design import device_symbol
from iron.common.harness import verify_buffer
from iron.common.image import OperatorSequence, build_fused_mlir
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.strided_copy import StridedCopy

ROWS, ROW, SLOTS = 16, 32, 4
TABLE_BYTES = ROWS * ROW * 4
ADD_SIZE = 4096


@pytest.fixture(autouse=True)
def device():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


def _gather():
    """rows[out_offset:][:ROW] = table[in_offset:][:ROW], both per call, int32."""
    gather = StridedCopy(
        input_sizes=[ROW],
        input_strides=[1],
        input_offset=0,
        input_buffer_size=ROWS * ROW,
        output_sizes=[ROW],
        output_strides=[1],
        output_offset=0,
        output_buffer_size=SLOTS * ROW,
        dtype=np.int32,
    )
    gather.use_value("in_offset")
    gather.use_value("out_offset")
    return gather


def _symbols(op):
    return {value.name: device_symbol(op, value) for value in op.values}


def _check_gathers(run, gather, table):
    """Gather rows of ``table`` (what the device holds) into slots, one call
    at a time, checking every slot each time."""
    symbols = _symbols(gather)
    rows = run.get_buffer("rows")
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
        got = run.get_buffer("rows").numpy()[: SLOTS * ROW].reshape(SLOTS, ROW)
        assert np.array_equal(got, expected), (
            f"row {row} into slot {slot}: slots hold {got[:, 0].tolist()}, "
            f"expected {expected[:, 0].tolist()}"
        )


@pytest.mark.supported_devices("npu2")
def test_int32_step_at_nonzero_offsets(npu_runtime):
    add = ElementwiseAdd(size=ADD_SIZE, tile_size=1024, num_aie_columns=4)
    gather = _gather()
    seq = OperatorSequence(
        name="infra_fused_int32_gather",
        runlist=[(add, "a", "b", "c"), (gather, "table", "rows")],
        input_args=["a", "b", "table"],
        output_args=["c", "rows"],
        dispatch="fused",
    ).compile()
    kinds = {name: seq.subbuffer_layout[name][:2] for name in ("table", "rows")}
    assert kinds["table"][0] == "input" and kinds["table"][1] > 0, kinds
    assert kinds["rows"][0] == "output" and kinds["rows"][1] > 0, kinds

    run = seq.get_callable()
    assert run.get_buffer("table").dtype == np.int32
    assert run.get_buffer("c").dtype == bfloat16

    rng = np.random.default_rng(0)
    a = rng.standard_normal(ADD_SIZE).astype(bfloat16)
    b = rng.standard_normal(ADD_SIZE).astype(bfloat16)
    run.get_buffer("a").numpy_view()[:] = a
    run.get_buffer("b").numpy_view()[:] = b
    # Every value distinct, so a row landing anywhere else shows.
    table = np.arange(ROWS * ROW, dtype=np.int32).reshape(ROWS, ROW)
    run.get_buffer("table").numpy_view()[:] = table.reshape(-1)
    _check_gathers(run, gather, table)

    c = run.get_buffer("c").numpy()[:ADD_SIZE]
    errors = verify_buffer(c, "c", a + b, rel_tol=0.04, abs_tol=1e-6)
    assert not errors, f"the bf16 step beside the int32 one: {len(errors)} mismatches"


@pytest.mark.supported_devices("npu2")
def test_int32_slice_at_word_offset(npu_runtime):
    """A slice starting 36 bytes into its parent: a whole number of int32
    words, and not on the 64-byte granule an arena buffer is placed at."""
    start = 36
    gather = _gather()
    seq = OperatorSequence(
        name="infra_fused_int32_slice",
        runlist=[(gather, f"packed[{start}:{start + TABLE_BYTES}]", "rows")],
        input_args=["packed"],
        output_args=["rows"],
        buffer_sizes={"packed": TABLE_BYTES + 64},
        dispatch="fused",
    ).compile()
    run = seq.get_callable()
    packed = run.get_buffer("packed")
    assert packed.dtype == np.int32, "a parent of int32 slices is viewed as int32"
    words = start // 4
    table = np.arange(ROWS * ROW, dtype=np.int32).reshape(ROWS, ROW)
    packed.numpy_view()[:] = -7
    packed.numpy_view()[words : words + ROWS * ROW] = table.reshape(-1)
    _check_gathers(run, gather, table)


def test_misaligned_buffer_is_rejected():
    """A buffer the shim DMA cannot start on fails at fusion, not silently on
    the device (whose descriptor would drop the low address bits)."""
    gather = _gather()
    seq = OperatorSequence(
        name="infra_fused_int32_misaligned",
        runlist=[(gather, f"packed[34:{34 + TABLE_BYTES}]", "rows")],
        input_args=["packed"],
        output_args=["rows"],
        buffer_sizes={"packed": TABLE_BYTES + 64},
        dispatch="fused",
    )
    seq.subbuffer_layout, seq.buffer_sizes, seq.slice_info = (
        seq.calculate_buffer_layout()
    )
    with pytest.raises(ValueError, match="not a multiple of 4"):
        build_fused_mlir(seq)
