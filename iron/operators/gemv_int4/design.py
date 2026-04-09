# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Fused INT4 dequantization matrix-vector design.

Performs a fused dequantize-GEMV where the weight matrix is stored in packed
INT4 format (two 4-bit values per uint8 byte) with per-group bfloat16 scale
factors.  The activation vector and output are bfloat16.

Each AIE column processes a contiguous block of output rows.  Within a column,
the worker iterates over tiles of packed weight rows, acquires the full
activation vector once per outer iteration, and calls the fused dequant-matvec
kernel which unpacks, dequantizes, and accumulates in a single pass.

Buffer layout for A (packed weights, uint8):
    For each tile of m_input rows: [m_input * K / 2 bytes of packed weights]
                                   [m_input * (K / group_size) * 2 bytes of scales]
"""

import numpy as np
from ml_dtypes import bfloat16

import aie.dialects.index as index
from aie.dialects.aie import T
from aie.helpers.dialects.scf import _for as range_
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer


def my_fused_dequant_matvec(
    dev, cols, M, K, m_input, m_output=None, group_size=32
):
    if m_output is None:
        m_output = m_input

    # --- Assertions ---
    assert (
        m_output % m_input == 0 and m_output >= m_input
    ), "m_output must be a multiple of m_input"
    assert m_output <= M // cols, "m_output must be less than or equal to M/cols"
    assert (M // cols) % m_output == 0, "m_output must evenly divide M/cols"
    assert m_input <= M // cols, "m_input must be less than or equal to M/cols"
    assert (M // cols) % m_input == 0, "m_input must evenly divide M/cols"
    assert K % group_size == 0, "K must be divisible by group_size"
    assert group_size % 32 == 0, "group_size must be a multiple of 32"
    assert M % cols == 0, "M must be divisible by cols"

    # --- Data types ---
    dtype_in = np.dtype[np.uint8]
    dtype_vec = np.dtype[bfloat16]
    dtype_out = np.dtype[bfloat16]

    # --- Per-tile sizes (in uint8 bytes) ---
    num_groups_per_row = K // group_size
    packed_tile_bytes = m_input * K // 2 + m_input * num_groups_per_row * 2
    rows_per_col = M // cols
    tiles_per_col = rows_per_col // m_input
    bytes_per_col = tiles_per_col * packed_tile_bytes
    packed_total_bytes = cols * bytes_per_col

    # --- L1 (on-chip) tensor types ---
    L1_A_ty = np.ndarray[(packed_tile_bytes,), dtype_in]
    L1_B_ty = np.ndarray[(K,), dtype_vec]
    L1_C_ty = np.ndarray[(m_output,), dtype_out]

    # --- L3 (DDR) tensor types ---
    L3_A_ty = np.ndarray[(packed_total_bytes,), dtype_in]
    L3_B_ty = np.ndarray[(K,), dtype_vec]
    L3_C_ty = np.ndarray[(M,), dtype_out]

    # --- Kernel declaration ---
    fused_matvec = Kernel(
        "fused_dequant_matvec_bf16",
        "fused_dequant_gemv.o",
        [np.int32, np.int32, np.int32, L1_A_ty, L1_B_ty, L1_C_ty, np.int32],
    )

    # --- ObjectFIFOs ---
    A_L3L1_fifos = [
        ObjectFifo(L1_A_ty, name=f"A_L3L1_{i}", depth=2) for i in range(cols)
    ]
    B_L3L1_fifos = [
        ObjectFifo(L1_B_ty, name=f"B_L3L1_{i}", depth=1) for i in range(cols)
    ]
    C_L1L3_fifos = [
        ObjectFifo(L1_C_ty, name=f"C_L1L3_{i}", depth=2) for i in range(cols)
    ]

    # --- Worker core body ---
    N_div_n = tiles_per_col // (m_output // m_input)

    def core_body(A_L3L1_fifo, B_L3L1_fifo, C_L1L3_fifo, fused_matvec_fn):
        for _ in range_(0xFFFFFFFF):
            b = B_L3L1_fifo.acquire(1)
            for i_idx in range_(N_div_n):
                c = C_L1L3_fifo.acquire(1)
                for j_idx in range_(m_output // m_input):
                    j_i32 = index.casts(T.i32(), j_idx)
                    output_row_offset = j_i32 * m_input
                    a = A_L3L1_fifo.acquire(1)
                    fused_matvec_fn(
                        m_input, K, output_row_offset, a, b, c, group_size
                    )
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
                fused_matvec,
            ],
        )
        for i in range(cols)
    ]

    # --- TensorAccessPatterns ---
    # A: each column gets a contiguous chunk of bytes_per_col packed bytes
    A_taps = [
        TensorAccessPattern(
            tensor_dims=L3_A_ty.__args__[0],
            offset=col * bytes_per_col,
            sizes=[1, 1, 1, bytes_per_col],
            strides=[0, 0, 0, 1],
        )
        for col in range(cols)
    ]

    # C: each column writes contiguous rows_per_col bfloat16 values
    C_taps = [
        TensorAccessPattern(
            tensor_dims=L3_C_ty.__args__[0],
            offset=col * rows_per_col,
            sizes=[1, 1, 1, rows_per_col],
            strides=[0, 0, 0, 1],
        )
        for col in range(cols)
    ]

    # --- Runtime sequence ---
    rt = Runtime()
    with rt.sequence(L3_A_ty, L3_B_ty, L3_C_ty) as (A, B, C):
        rt.start(*workers)
        tg = rt.task_group()
        for i in range(cols):
            rt.fill(A_L3L1_fifos[i].prod(), A, A_taps[i], task_group=tg)
            rt.fill(B_L3L1_fifos[i].prod(), B, task_group=tg)
        for i in range(cols):
            rt.drain(
                C_L1L3_fifos[i].cons(), C, C_taps[i], task_group=tg, wait=True
            )
        rt.finish_task_group(tg)

    return Program(dev, rt).resolve_program(SequentialPlacer())
