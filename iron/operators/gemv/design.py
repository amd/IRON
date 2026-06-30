# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from ml_dtypes import bfloat16

import aie.dialects.index as index
from aie.dialects.aie import T
from aie.helpers.dialects.scf import _for as range_
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker

"""
Matrix-vector design

Calls into the mv.cc kernel code. That kernel computes `m_input` output rows per call.


 - cols: Number of AIE columns to split work across
 - M: number of rows in the matrix
 - K: number of columns in the matrix == number of rows in the vector
 - m_input: number of input rows stored on each AIE core == chunk size for data movement of input A
 - m_output: number of output rows stored on each AIE core == chunk size for data movement of output C
 - num_batches: number of iterations of this mat-vec to perform on contiguous matrices and vectors in memory (results concatenated)
"""


def my_matvec(
    dev,
    cols,
    M,
    K,
    m_input,
    m_output=None,
    num_batches=1,
    kernel_object="mv.o",
    func_prefix="",
    verbose=False,
):
    if m_output is None:
        m_output = m_input

    if verbose:
        print(f"Device: {dev}")
        print(f"Matrix dimensions: M={M}, K={K}")
        print(f"Tiling: m_input={m_input}, m_output={m_output}")
        print(f"Columns: {cols}")

    # The reason for the following requirement is because we first acquire output rows from the C FIFO, then fill those acquiring rows of the A input.
    assert (
        m_output % m_input == 0 and m_output >= m_input
    ), "m_output must be a multiple of m_input"
    assert m_output <= M // cols, "m_output must be less than or equal to M/cols"
    assert (M // cols) % m_output == 0, "m_output must evenly divide M/cols"
    assert m_input <= M // cols, "m_input must be less than or equal to M/cols"
    assert (M // cols) % m_input == 0, "m_input must evenly divide M/cols"

    vectorized = True
    dtype_in = np.dtype[bfloat16]
    dtype_in_str = "bf16"
    dtype_out = np.dtype[bfloat16]
    dtype_out_str = "bf16"

    assert M % cols == 0

    L1_A_ty = np.ndarray[
        (
            m_input,
            K,
        ),
        dtype_in,
    ]
    L1_B_ty = np.ndarray[(K,), dtype_in]
    L1_C_ty = np.ndarray[(m_output,), dtype_out]
    L3_A_ty = np.ndarray[
        (num_batches * M * K,),
        dtype_in,
    ]
    L3_B_ty = np.ndarray[(num_batches * K,), dtype_in]
    L3_C_ty = np.ndarray[(num_batches * M,), dtype_out]

    func_type = "vectorized" if vectorized else "scalar"
    matvec = Kernel(
        f"{func_prefix}matvec_{func_type}_{dtype_in_str}_{dtype_out_str}",
        f"{func_prefix}{kernel_object}",
        [np.int32, np.int32, L1_A_ty, L1_B_ty, L1_C_ty],
    )

    A_L3L1_fifos = [
        ObjectFifo(L1_A_ty, name=f"A_L3L1_{i}", depth=2) for i in range(cols)
    ]
    B_L3L1_fifos = [
        ObjectFifo(L1_B_ty, name=f"B_L3L1_{i}", depth=1) for i in range(cols)
    ]
    C_L1L3_fifos = [
        ObjectFifo(L1_C_ty, name=f"C_L1L3_{i}", depth=2) for i in range(cols)
    ]

    def core_body(A_L3L1_fifo, B_L3L1_fifo, C_L1L3_fifo, matvec):
        one_idx = index.constant(1)
        for _ in range_(0xFFFFFFFF):  # batch dim handled as part of this loop
            b = B_L3L1_fifo.acquire(1)
            # The kernel function computes m output rows; each core is responsible for (M/cols) output rows, so we need to call the kernel (M/cols)/m times.
            for i_idx in range_(M // m_output // cols):
                c = C_L1L3_fifo.acquire(1)
                i_i32 = index.casts(T.i32(), i_idx)
                for j_idx in range_(m_output // m_input):
                    j_i32 = index.casts(T.i32(), j_idx)
                    output_row_offset = j_i32 * m_input
                    a = A_L3L1_fifo.acquire(1)
                    matvec(m_input, output_row_offset, a, b, c)
                    A_L3L1_fifo.release(1)
                C_L1L3_fifo.release(1)
            B_L3L1_fifo.release(1)

    workers = [
        Worker(
            core_body,
            [
                A_L3L1_fifos[i].cons(),
                B_L3L1_fifos[i].cons(),
                C_L1L3_fifos[i].prod(),
                matvec,
            ],
        )
        for i in range(cols)
    ]

    # Distribution pattern for the input matrix A: each AIE core gets a contiguous chunk of rows.
    # The input matrix in DDR is MxK-sized (row-major); each core processes (M/cols)xK-sized matrices in chunks of mxK-sized tiles.
    # The chunking into mxK-sized tiles happens in the ObjectFIFO; the shim puts all data on the stream in sequence.
    A_taps = [
        [
            TensorAccessPattern(
                tensor_dims=L3_A_ty.__args__[0],
                offset=col * (M // cols) * K + batch * M * K,
                sizes=[1, 1, 1, (M // cols) * K],
                strides=[0, 0, 0, 1],
            )
            for batch in range(num_batches)
        ]
        for col in range(cols)
    ]

    # Every column gets the entirety of the vector B.
    # This design assumes that all of B fits on the cores.
    B_tap = TensorAccessPattern(
        tensor_dims=L3_B_ty.__args__[0],
        offset=0,
        sizes=[1, 1, 1, num_batches * K],
        strides=[0, 0, 0, 1],
    )

    # Collection pattern for the output vector C: each AIE core writes back its contiguous chunk of rows.
    C_taps = [
        [
            TensorAccessPattern(
                tensor_dims=L3_C_ty.__args__[0],
                offset=col * (M // cols) + batch * M,
                sizes=[1, 1, 1, (M // cols)],
                strides=[0, 0, 0, 1],
            )
            for batch in range(num_batches)
        ]
        for col in range(cols)
    ]

    # --- Batch-coalesce (default): one BD per column over all batches. ---
    # Replaces the per-batch unroll with a single iterated BD; the stock A_taps/C_taps
    # above remain the fallback (and the num_batches==1 path). Access-equivalent to the
    # unroll (covered by test_gemv_batched).
    #
    # This is NOT a single linear transfer. Within one batch the run is contiguous
    # (A_run = (M//cols)*K elements), but the batch stride is the full matrix
    # (A_bstride = M*K), so for cols>1 each column gathers its own slice out of every
    # batch with a gap in between. Only cols==1 degenerates to bstride==run. So the
    # batch dim is a genuine size-uncapped iteration dim and the TAP is required.
    #
    # The contiguous run is then split into two wrap dims [run_hi, run_lo] ONLY to fit
    # the AIE shim's 10-bit (1023) wrap-size cap. TAP sizes are outermost-first and the
    # verifier reverses them, so [1, num_batches, run_hi, run_lo] puts num_batches in the
    # size-uncapped dim and the contiguous run in the two capped wrap dims. The shim also
    # enforces a 4-byte address granularity on every size and stride (not skipped, even
    # for linear transfers); for bf16 (2 bytes) that means run_lo and the batch stride
    # must be even, so split_run only yields an even run_lo and the predicate requires
    # even strides.
    #
    # FUTURE: this manual split is only needed on the current mlir_aie pin. Once IRON's
    # pin moves past Xilinx/mlir-aie #3036 (LinearizeContiguousBDTransfer for the
    # iteration dim, on top of #2924 which canonicalizes a contiguous run to linear form
    # and bypasses the 1023 cap via the hardware buffer-length register), split_run /
    # MAX_WRAP / GRAN_ELEMS can be dropped and the run supplied as one inner dim
    # [num_batches, A_run]. The pin is currently frozen at the last pre-#3016 release.
    # FIXME: pull these shim BD bounds from the MLIR-AIE target model rather than
    # hard-coding them; they live in verifyStridesWraps in
    # https://github.com/Xilinx/mlir-aie/blob/main/lib/Dialect/AIEX/IR/AIEXDialect.cpp
    MAX_WRAP = 1023
    MAX_STRIDE = (1 << 20) - 1  # conservative element-stride bound for the wrap dims
    GRAN_ELEMS = 2  # 4-byte shim granularity / 2-byte bf16 element

    def split_run(run, lim=MAX_WRAP, gran=GRAN_ELEMS):
        """Factor a contiguous run into (hi, lo), both <= lim and lo a multiple of gran
        (the address-granularity-aligned inner size), lo maximal. None if no such
        split exists (caller then falls back to the per-batch path)."""
        lo_start = (lim // gran) * gran
        for lo in range(lo_start, 0, -gran):
            if run % lo == 0 and (run // lo) <= lim:
                return (run // lo, lo)
        return None

    A_run, A_bstride = (M // cols) * K, M * K
    C_run, C_bstride = (M // cols), M
    A_split, C_split = split_run(A_run), split_run(C_run)
    coalesce = (
        num_batches > 1
        and A_bstride <= MAX_STRIDE
        and C_bstride <= MAX_STRIDE
        and A_bstride % GRAN_ELEMS == 0
        and C_bstride % GRAN_ELEMS == 0
        and A_split is not None
        and C_split is not None
    )

    def coalesced_tap(L3_ty, col_off, split, bstride):
        run_hi, run_lo = split
        return TensorAccessPattern(
            tensor_dims=L3_ty.__args__[0],
            offset=col_off,
            sizes=[1, num_batches, run_hi, run_lo],
            strides=[0, bstride, run_lo, 1],
        )

    if coalesce:
        # Dropping the per-batch drain wait lets the single iterated fill BD run ahead of
        # the core. ObjectFifo lock backpressure keeps that safe: a producer that gets
        # ahead BLOCKS on the buffer lock (worst case a stall, never a corrupting
        # overrun). depth>=2 only buys OVERLAP of fill with compute, so it is a
        # performance guard here, not a correctness requirement (depth==1 is correct but
        # fully serial).
        assert all(f.depth >= 2 for f in A_L3L1_fifos) and all(
            f.depth >= 2 for f in C_L1L3_fifos
        ), "coalesced GEMV wants A/C ObjectFifo depth>=2 for fill/compute overlap"
        A_taps_coalesced = [
            coalesced_tap(L3_A_ty, col * (M // cols) * K, A_split, A_bstride)
            for col in range(cols)
        ]
        C_taps_coalesced = [
            coalesced_tap(L3_C_ty, col * (M // cols), C_split, C_bstride)
            for col in range(cols)
        ]

    rt = Runtime()
    with rt.sequence(L3_A_ty, L3_B_ty, L3_C_ty) as (A, B, C):
        rt.start(*workers)
        tg_b = rt.task_group()
        for col in range(cols):
            # Simple linear transfer of B, includes all batches in sequence
            rt.fill(B_L3L1_fifos[col].prod(), B, B_tap, task_group=tg_b)
        # Coalesced: one iterated BD per column covers all batches (num_waits==1, a
        # single drain wait for the whole column). Fallback (incl. num_batches==1): the
        # stock per-batch unroll (num_waits==num_batches, one wait per batch). The fills
        # and drains are otherwise identical; only the TAP and the wait count differ.
        num_waits = 1 if coalesce else num_batches
        for w in range(num_waits):
            tg_ac = rt.task_group()
            for col in range(cols):
                a_tap = A_taps_coalesced[col] if coalesce else A_taps[col][w]
                rt.fill(A_L3L1_fifos[col].prod(), A, a_tap, task_group=tg_ac)
            for col in range(cols):
                c_tap = C_taps_coalesced[col] if coalesce else C_taps[col][w]
                rt.drain(
                    C_L1L3_fifos[col].cons(),
                    C,
                    c_tap,
                    task_group=tg_ac,
                    wait=True,
                )
            rt.finish_task_group(tg_ac)
        rt.finish_task_group(tg_b)

    return Program(dev, rt).resolve_program()
