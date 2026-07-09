# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
import numpy as np

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker, Buffer
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_


def my_axpy(
    dev,
    num_elements,
    num_columns,
    tile_size,
    trace_size,
    scalar_factor,
    add_y=True,
    mul_x=True,
    causal_mask=False,
    mask_block_dim=0,
    rows_per_block=0,
    row_offset=0,
    func_prefix="",
):
    """AXPY-family element-wise design.

    Modes:
      mul_x=True,  add_y=True  → saxpy:        Z = a*X + Y
      mul_x=True,  add_y=False → scale:        Z = a*X
      mul_x=False, add_y=True  → scalar_add:   Z = a + Y
      mul_x=False, add_y=True, causal_mask=True →
        Z[i,j] = a if (j > i within head)  else  Y[i,j]
        (in-place causal mask; supplies row/col-chunk indices to the kernel
        via an idx_buffer; data is interpreted as (..., S, S) blocks where
        S = mask_block_dim.)
    """
    if causal_mask:
        return _my_axpy_causal_mask(
            dev=dev,
            num_elements=num_elements,
            num_columns=num_columns,
            tile_size=tile_size,
            scalar_factor=scalar_factor,
            mask_block_dim=mask_block_dim,
            rows_per_block=rows_per_block or mask_block_dim,
            row_offset=row_offset,
            func_prefix=func_prefix,
        )

    factor = scalar_factor
    per_tile_elements = 4096 if tile_size > 4096 else tile_size
    n = per_tile_elements * num_columns
    if num_elements % n != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {n}."
        )
    N_div_n = num_elements // n
    chunk = num_elements // num_columns
    dtype = bfloat16

    tensor_ty = np.ndarray[(num_elements,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]

    # Two inputs only when both *X and +Y are kept (saxpy mode).
    has_two_inputs = add_y and mul_x

    # AIE-array data movement with object fifos (one per column)
    of_in1s = [ObjectFifo(tile_ty, name=f"in1_{i}") for i in range(num_columns)]
    if has_two_inputs:
        of_in2s = [ObjectFifo(tile_ty, name=f"in2_{i}") for i in range(num_columns)]
    of_outs = [ObjectFifo(tile_ty, name=f"out_{i}") for i in range(num_columns)]

    # AIE Core Function declaration
    if has_two_inputs:
        kernel = Kernel(
            f"{func_prefix}saxpy",
            f"{func_prefix}axpy.o",
            [tile_ty, tile_ty, np.float32, tile_ty, np.int32],
        )
    elif not add_y:
        # z = a * x  (drop +Y)
        kernel = Kernel(
            f"{func_prefix}scale_bf16",
            f"{func_prefix}axpy.o",
            [tile_ty, tile_ty, np.float32, np.int32],
        )
    else:
        # z = a + y  (drop *X)
        kernel = Kernel(
            f"{func_prefix}scalar_add_bf16",
            f"{func_prefix}axpy.o",
            [tile_ty, tile_ty, np.float32, np.int32],
        )

    if has_two_inputs:

        def core_body(of_in1, of_in2, of_out, k):
            for _ in range_(N_div_n):
                e1 = of_in1.acquire(1)
                e2 = of_in2.acquire(1)
                eo = of_out.acquire(1)
                k(e1, e2, factor, eo, per_tile_elements)
                of_in1.release(1)
                of_in2.release(1)
                of_out.release(1)

    else:

        def core_body(of_in1, of_out, k):
            for _ in range_(N_div_n):
                e1 = of_in1.acquire(1)
                eo = of_out.acquire(1)
                k(e1, eo, factor, per_tile_elements)
                of_in1.release(1)
                of_out.release(1)

    if has_two_inputs:
        my_workers = [
            Worker(
                core_body,
                [of_in1s[i].cons(), of_in2s[i].cons(), of_outs[i].prod(), kernel],
            )
            for i in range(num_columns)
        ]
    else:
        my_workers = [
            Worker(
                core_body,
                [of_in1s[i].cons(), of_outs[i].prod(), kernel],
            )
            for i in range(num_columns)
        ]

    taps = [
        TensorAccessPattern(
            (1, num_elements),
            chunk * i,
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    rt = Runtime()
    sequence_types = (
        (tensor_ty, tensor_ty, tensor_ty) if has_two_inputs else (tensor_ty, tensor_ty)
    )

    with rt.sequence(*sequence_types) as bufs:
        if has_two_inputs:
            A, B, C = bufs
        else:
            A, C = bufs

        rt.start(*my_workers)

        tg = rt.task_group()
        for i in range(num_columns):
            rt.fill(of_in1s[i].prod(), A, taps[i], task_group=tg)
            if has_two_inputs:
                rt.fill(of_in2s[i].prod(), B, taps[i], task_group=tg)
        for i in range(num_columns):
            rt.drain(of_outs[i].cons(), C, taps[i], wait=True, task_group=tg)
        rt.finish_task_group(tg)

    return Program(dev, rt).resolve_program()


def _my_axpy_causal_mask(
    dev,
    num_elements,
    num_columns,
    tile_size,
    scalar_factor,
    mask_block_dim,
    rows_per_block,
    row_offset,
    func_prefix="",
):
    """Single-core in-place causal mask via scalar_add_causal_bf16.

    Walks (blocks × rows_per_block × chunks-per-row) with three nested
    runtime loops and feeds (chunk_start_col, row_in_head) to the kernel via
    an idx buffer.  The kernel applies the scalar `a` to elements strictly
    above the per-head diagonal and copies y → z elsewhere.  Tiles entirely
    below the diagonal still get DMA'd (no per-tile data-movement skip)
    but the kernel does only a copy in that case.

    Two operating modes (selected by the rows_per_block / row_offset args):
    * Multi-block / full-head (rows_per_block = mask_block_dim, row_offset = 0):
      walks ``num_blocks`` whole (S, S) blocks; idx[1] resets to 0 at the
      start of each block.
    * Sub-block (rows_per_block < mask_block_dim or row_offset > 0):
      ``num_blocks`` is typically 1 in the MHA caller; processes a contiguous
      ``rows_per_block``-tall slice of one block starting at row_offset.
      Used at very long S where one (S, S) block exceeds the BD-length cap.
    """
    factor = scalar_factor
    S = mask_block_dim
    per_tile_elements = 4096 if tile_size > 4096 else tile_size
    if S % per_tile_elements != 0:
        raise ValueError(
            f"mask_block_dim ({S}) must be a multiple of per_tile_elements "
            f"({per_tile_elements})"
        )
    chunks_per_row = S // per_tile_elements
    block_elements = rows_per_block * S
    if num_elements % block_elements != 0:
        raise ValueError(
            f"num_elements ({num_elements}) must be a multiple of "
            f"rows_per_block * S ({block_elements})"
        )
    num_blocks = num_elements // block_elements

    # Two parallelisation modes:
    #  * block-aligned (num_blocks >= num_columns): each core handles
    #    blocks_per_core whole (S, S) blocks; idx[1] resets to row_offset at
    #    every block boundary (same value on every core).
    #  * within-block (num_blocks == 1, num_columns > 1): a single block is
    #    too big to split across cores by block, so each core handles a
    #    contiguous row-range slice of that one block; per-core init_row is
    #    row_offset + core_idx * rows_per_iter (different per core).  The
    #    kernel logic is unchanged — it only cares about (chunk_start_col,
    #    row_in_block).
    if num_blocks >= num_columns:
        if num_blocks % num_columns != 0:
            raise ValueError(
                f"num_blocks ({num_blocks}) must be a multiple of num_columns "
                f"({num_columns}); causal_mask multi-core split is block-aligned"
            )
        blocks_per_core = num_blocks // num_columns
        rows_per_iter = rows_per_block
        per_core_init_rows = [row_offset] * num_columns
    else:
        if num_blocks != 1:
            raise ValueError(
                f"causal_mask multi-core within-block split requires "
                f"num_blocks == 1, got {num_blocks}"
            )
        if rows_per_block % num_columns != 0:
            raise ValueError(
                f"rows_per_block ({rows_per_block}) must be a multiple of "
                f"num_columns ({num_columns}) for within-block split"
            )
        blocks_per_core = 1
        rows_per_iter = rows_per_block // num_columns
        per_core_init_rows = [
            row_offset + i * rows_per_iter for i in range(num_columns)
        ]

    elements_per_core = num_elements // num_columns

    dtype = bfloat16
    tensor_ty = np.ndarray[(num_elements,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]
    idx_ty = np.ndarray[(2,), np.dtype[np.int32]]

    of_ins = [ObjectFifo(tile_ty, name=f"in{i}") for i in range(num_columns)]
    of_outs = [ObjectFifo(tile_ty, name=f"out{i}") for i in range(num_columns)]

    kernel = Kernel(
        f"{func_prefix}scalar_add_causal_bf16",
        f"{func_prefix}axpy.o",
        [tile_ty, tile_ty, idx_ty, np.float32, np.int32],
    )

    idx_buffers = [
        Buffer(
            initial_value=np.zeros((2,), dtype=np.int32),
            name=f"causal_mask_idx_{i}",
        )
        for i in range(num_columns)
    ]

    # Build one core_body per worker so the per-core init_row can be baked
    # into the closure (constant within the worker code).
    def make_core_body(my_init_row):
        def core_body(of_in_, of_out_, k, idx):
            # idx[0] = chunk_start_col within the current row of the block
            # idx[1] = current row index within the current block
            idx[0] = 0
            idx[1] = my_init_row
            for _ in range_(blocks_per_core):
                for _ in range_(rows_per_iter):
                    for _ in range_(chunks_per_row):
                        elem_in = of_in_.acquire(1)
                        elem_out = of_out_.acquire(1)
                        k(elem_in, elem_out, idx, factor, per_tile_elements)
                        of_in_.release(1)
                        of_out_.release(1)
                        idx[0] = idx[0] + per_tile_elements
                    idx[0] = 0
                    idx[1] = idx[1] + 1
                idx[1] = my_init_row  # reset for next block

        return core_body

    workers = [
        Worker(
            make_core_body(per_core_init_rows[i]),
            [of_ins[i].cons(), of_outs[i].prod(), kernel, idx_buffers[i]],
        )
        for i in range(num_columns)
    ]

    taps = [
        TensorAccessPattern(
            (1, num_elements),
            i * elements_per_core,
            [1, 1, 1, elements_per_core],
            [0, 0, 0, 1],
        )
        for i in range(num_columns)
    ]

    rt = Runtime()
    with rt.sequence(tensor_ty, tensor_ty) as (A, C):
        rt.start(*workers)
        tg = rt.task_group()
        for i in range(num_columns):
            rt.fill(of_ins[i].prod(), A, taps[i], task_group=tg)
        for i in range(num_columns):
            rt.drain(of_outs[i].cons(), C, taps[i], wait=True, task_group=tg)
        rt.finish_task_group(tg)

    return Program(dev, rt).resolve_program()
