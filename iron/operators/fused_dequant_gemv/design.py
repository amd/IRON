# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from pathlib import Path
from ml_dtypes import bfloat16
import argparse

import aie.dialects.index as index
from aie.dialects.aie import *
from aie.dialects.aiex import *
from aie.helpers.dialects.scf import _for as range_
from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2

"""
Fused INT4 dequantization + matrix-vector multiplication design.

Loads INT4-packed weights from DDR, dequantizes in-register, and performs
matrix-vector multiplication in a single pass, achieving 4x DDR bandwidth
reduction compared to bf16 weight streaming.

DDR buffer layout (tile-based, matching the kernel expectation):
  Each "tile" covers m_input rows of the weight matrix.
  Tiles for column 0 are first, then column 1, etc.
  Within each tile:
    [m_input * K / 2 bytes]  packed uint4 weights (row-major)
    [m_input * (K / G) * 2 bytes]  bf16 scale factors (row-major)

The fused kernel receives one tile per FIFO acquire and locates the scale
factors at offset ``m * k / 2`` within the tile.

DMA budget per compute tile:
  1 input FIFO (packed weights) + 1 input FIFO (vector) +
  1 output FIFO (result) = 3 channels <= 4 max.

Parameters:
  - cols: Number of AIE columns to split work across
  - M: Total output rows
  - K: Input vector length (== weight matrix columns)
  - m_input: Rows per kernel invocation (FIFO tile granularity)
  - m_output: Rows per C FIFO buffer (>= m_input, multiple of m_input)
  - group_size: Quantization group size (default 32, must be multiple of 32)
"""


def my_fused_dequant_matvec(dev, cols, M, K, m_input, m_output=None, group_size=32):
    if m_output is None:
        m_output = m_input

    assert (
        m_output % m_input == 0 and m_output >= m_input
    ), "m_output must be a multiple of m_input"
    assert m_output <= M // cols, "m_output must be <= M/cols"
    assert (M // cols) % m_output == 0, "m_output must evenly divide M/cols"
    assert m_input <= M // cols, "m_input must be <= M/cols"
    assert (M // cols) % m_input == 0, "m_input must evenly divide M/cols"
    assert K % group_size == 0, "K must be a multiple of group_size"
    assert group_size % 32 == 0, "group_size must be a multiple of 32"
    assert M % cols == 0, "M must be a multiple of cols"

    dtype_in = np.dtype[np.uint8]
    dtype_vec = np.dtype[bfloat16]
    dtype_out = np.dtype[bfloat16]

    dev_ty = NPU1() if dev == "npu" else NPU2()

    # Per-tile sizes (in uint8 bytes)
    num_groups_per_row = K // group_size
    packed_tile_bytes = m_input * K // 2 + m_input * num_groups_per_row * 2

    # Per-column sizes
    rows_per_col = M // cols
    tiles_per_col = rows_per_col // m_input
    bytes_per_col = tiles_per_col * packed_tile_bytes

    # Total DDR buffer size
    packed_total_bytes = cols * bytes_per_col

    # L1 types
    L1_A_ty = np.ndarray[(packed_tile_bytes,), dtype_in]
    L1_B_ty = np.ndarray[(K,), dtype_vec]
    L1_C_ty = np.ndarray[(m_output,), dtype_out]

    # L3 (DDR) types
    L3_A_ty = np.ndarray[(packed_total_bytes,), dtype_in]
    L3_B_ty = np.ndarray[(K,), dtype_vec]
    L3_C_ty = np.ndarray[(M,), dtype_out]

    # Kernel declaration
    fused_matvec = Kernel(
        "fused_dequant_matvec_bf16",
        "fused_dequant_gemv.o",
        [
            np.int32,
            np.int32,
            np.int32,
            L1_A_ty,
            L1_B_ty,
            L1_C_ty,
            np.int32,
        ],
    )

    # ObjectFIFOs
    A_L3L1_fifos = [
        ObjectFifo(L1_A_ty, name=f"A_L3L1_{i}", depth=2) for i in range(cols)
    ]
    B_L3L1_fifos = [
        ObjectFifo(L1_B_ty, name=f"B_L3L1_{i}", depth=1) for i in range(cols)
    ]
    C_L1L3_fifos = [
        ObjectFifo(L1_C_ty, name=f"C_L1L3_{i}", depth=2) for i in range(cols)
    ]

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
                        m_input,
                        K,
                        output_row_offset,
                        a,
                        b,
                        c,
                        group_size,
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

    # Weight distribution TAPs: each column gets a contiguous chunk.
    # The DDR buffer is laid out as:
    #   [col 0 tiles] [col 1 tiles] ... [col N-1 tiles]
    # Each column's region is bytes_per_col bytes.
    A_taps = [
        TensorAccessPattern(
            tensor_dims=(1, packed_total_bytes),
            offset=col * bytes_per_col,
            sizes=[1, 1, 1, bytes_per_col],
            strides=[0, 0, 0, 1],
        )
        for col in range(cols)
    ]

    # Output collection TAPs: contiguous chunks of M/cols bf16 values
    C_taps = [
        TensorAccessPattern(
            tensor_dims=(1, M),
            offset=col * rows_per_col,
            sizes=[1, 1, 1, rows_per_col],
            strides=[0, 0, 0, 1],
        )
        for col in range(cols)
    ]

    rt = Runtime()
    with rt.sequence(L3_A_ty, L3_B_ty, L3_C_ty) as (A, B, C):
        rt.start(*workers)
        tg = rt.task_group()
        for i in range(cols):
            rt.fill(A_L3L1_fifos[i].prod(), A, A_taps[i], task_group=tg)
            rt.fill(B_L3L1_fifos[i].prod(), B, task_group=tg)
        for i in range(cols):
            rt.drain(
                C_L1L3_fifos[i].cons(),
                C,
                C_taps[i],
                task_group=tg,
                wait=True,
            )
        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        prog="AIE Fused Dequant GEMV MLIR Design",
    )
    argparser.add_argument("--dev", type=str, choices=["npu", "npu2"], default="npu")
    argparser.add_argument("-M", type=int, required=True)
    argparser.add_argument("-K", type=int, required=True)
    argparser.add_argument("-m", type=int, required=True, dest="m_input")
    argparser.add_argument("--m-output", type=int, default=None, dest="m_output")
    argparser.add_argument("--cols", type=int, required=True)
    argparser.add_argument("--group-size", type=int, default=32, dest="group_size")
    argparser.add_argument(
        "--output-file-path",
        "-o",
        type=str,
        help="Output file path for the generated MLIR module",
    )
    args = argparser.parse_args()
    module = my_fused_dequant_matvec(
        args.dev,
        args.cols,
        args.M,
        args.K,
        args.m_input,
        args.m_output,
        args.group_size,
    )

    output_file_path = Path(args.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
