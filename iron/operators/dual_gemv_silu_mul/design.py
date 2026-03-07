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
Dual matrix-vector + SiLU + elementwise multiply design.

Computes: output = silu(W1 @ x) * (W2 @ x)

W1 and W2 rows are pre-interleaved in DDR by the operator (op.py).
GEMV phases write to kernel-internal static buffers (left_buf, right_buf)
controlled by a phase parameter. The silu_mul phase reads from those
buffers and writes the result to the output C FIFO.

Each AIE core:
  1. Acquires vector x (held in L1 for both GEMV passes)
  2. Consumes W1 rows from A FIFO, writes dot products to left_buf (phase=0)
  3. Consumes W2 rows from A FIFO, writes dot products to right_buf (phase=1)
  4. Computes silu(left_buf) * right_buf -> C FIFO output
"""


def my_dual_gemv_silu_mul(dev, cols, M, K, m_input, m_output=None):
    if m_output is None:
        m_output = m_input

    assert m_output % m_input == 0 and m_output >= m_input
    assert m_output <= M // cols
    assert (M // cols) % m_output == 0
    assert m_input <= M // cols
    assert (M // cols) % m_input == 0

    dtype_in = np.dtype[bfloat16]
    dtype_out = np.dtype[bfloat16]

    assert M % cols == 0

    dev_ty = NPU1() if dev == "npu" else NPU2()

    # L1 tile types
    L1_A_ty = np.ndarray[(m_input, K), dtype_in]
    L1_B_ty = np.ndarray[(K,), dtype_in]
    L1_C_ty = np.ndarray[(m_output,), dtype_out]

    # L3 (DDR) buffer types
    L3_W_ty = np.ndarray[(2 * M, K), dtype_in]
    L3_B_ty = np.ndarray[(K,), dtype_in]
    L3_C_ty = np.ndarray[(M,), dtype_out]

    # GEMV: writes to left_buf (phase=0) or right_buf (phase=1)
    matvec = Kernel(
        "dual_gemv_matvec_bf16",
        "dual_gemv_silu_mul.o",
        [np.int32, np.int32, np.int32, L1_A_ty, L1_B_ty, np.int32],
    )

    # SiLU+Mul: reads from static left_buf/right_buf, writes to C FIFO
    silu_mul_fn = Kernel(
        "dual_gemv_silu_mul_bf16",
        "dual_gemv_silu_mul.o",
        [L1_C_ty, np.int32],
    )

    # ObjectFIFOs: 2 inputs + 1 output = fits AIE DMA channel limits
    A_fifos = [ObjectFifo(L1_A_ty, name=f"A_{i}", depth=2) for i in range(cols)]
    B_fifos = [ObjectFifo(L1_B_ty, name=f"B_{i}", depth=1) for i in range(cols)]
    C_fifos = [ObjectFifo(L1_C_ty, name=f"C_{i}", depth=2) for i in range(cols)]

    def core_body(A_fifo, B_fifo, C_fifo, matvec_fn, silu_mul):
        for _ in range_(0xFFFFFFFF):
            b = B_fifo.acquire(1)
            for i_idx in range_(M // m_output // cols):
                # Phase 1: W1 rows -> left_buf (phase=0)
                for j_idx in range_(m_output // m_input):
                    j_i32 = index.casts(T.i32(), j_idx)
                    row_offset = j_i32 * m_input
                    a = A_fifo.acquire(1)
                    matvec_fn(m_input, K, row_offset, a, b, 0)
                    A_fifo.release(1)
                # Phase 2: W2 rows -> right_buf (phase=1)
                for j_idx in range_(m_output // m_input):
                    j_i32 = index.casts(T.i32(), j_idx)
                    row_offset = j_i32 * m_input
                    a = A_fifo.acquire(1)
                    matvec_fn(m_input, K, row_offset, a, b, 1)
                    A_fifo.release(1)
                # Phase 3: silu(left_buf) * right_buf -> output
                c = C_fifo.acquire(1)
                silu_mul(c, m_output)
                C_fifo.release(1)
            B_fifo.release(1)

    workers = [
        Worker(
            core_body,
            [
                A_fifos[i].cons(),
                B_fifos[i].cons(),
                C_fifos[i].prod(),
                matvec,
                silu_mul_fn,
            ],
        )
        for i in range(cols)
    ]

    # Interleaved weight distribution per column
    rows_per_col = M // cols
    A_taps = [
        TensorAccessPattern(
            tensor_dims=(2 * M, K),
            offset=col * 2 * rows_per_col * K,
            sizes=[1, 1, 1, 2 * rows_per_col * K],
            strides=[0, 0, 0, 1],
        )
        for col in range(cols)
    ]

    # Output collection
    C_taps = [
        TensorAccessPattern(
            tensor_dims=(1, M),
            offset=col * (M // cols),
            sizes=[1, 1, 1, (M // cols)],
            strides=[0, 0, 0, 1],
        )
        for col in range(cols)
    ]

    rt = Runtime()
    with rt.sequence(L3_W_ty, L3_B_ty, L3_C_ty) as (W, B, C):
        rt.start(*workers)
        tg = rt.task_group()
        for i in range(cols):
            rt.fill(A_fifos[i].prod(), W, A_taps[i], task_group=tg)
            rt.fill(B_fifos[i].prod(), B, task_group=tg)
        for i in range(cols):
            rt.drain(C_fifos[i].cons(), C, C_taps[i], task_group=tg, wait=True)
        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        prog="AIE Dual GEMV + SiLU + Mul Design",
    )
    argparser.add_argument("--dev", type=str, choices=["npu", "npu2"], default="npu")
    argparser.add_argument("-M", type=int, required=True)
    argparser.add_argument("-K", type=int, required=True)
    argparser.add_argument("-m", type=int, required=True, dest="m_input")
    argparser.add_argument("--m-output", type=int, default=None, dest="m_output")
    argparser.add_argument("--cols", type=int, required=True)
    argparser.add_argument(
        "--output-file-path",
        "-o",
        type=str,
        help="Output file path for the generated MLIR module",
    )
    args = argparser.parse_args()
    module = my_dual_gemv_silu_mul(
        args.dev, args.cols, args.M, args.K, args.m_input, args.m_output
    )

    output_file_path = Path(args.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
