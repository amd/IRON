# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from pathlib import Path
from ml_dtypes import bfloat16
import argparse

from aie.extras.context import mlir_mod_ctx
from aie.ir import StridedLayoutAttr, ShapedType
import aie.dialects.index as index
import aie.dialects.memref as memref
from aie.dialects.aie import *
from aie.dialects.aiex import *
from aie.helpers.dialects.scf import _for as range_
from aie.helpers.util import try_convert_np_type_to_mlir_type
from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2

"""
Matrix-vector design

Calls into the mv.cc kernel code. That kernel computes `m_input` output rows per call.


 - cols: Number of AIE columns to split work across
 - M: number of rows in the matrix
 - K: number of columns in the matrix == number of rows in the vector
 - m_input: number of input rows stored on each AIE core == chunk size for data movement of input A
 - m_output: number of output rows stored on each AIE core == chunk size for data movement of output C
"""


def my_matvec(dev, cols, M, K, m_input, m_output=None, verbose=False):
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

    if dev == "npu":
        dev_ty = NPU1()
    else:
        dev_ty = NPU2()

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
        (
            M,
            K,
        ),
        dtype_in,
    ]
    L3_B_ty = np.ndarray[(K,), dtype_in]
    L3_C_ty = np.ndarray[(M,), dtype_out]

    func_type = "vectorized" if vectorized else "scalar"
    matvec = Kernel(
        f"matvec_{func_type}_{dtype_in_str}_{dtype_out_str}",
        "mv.o",
        [np.int32, np.int32, np.int32, L1_A_ty, L1_B_ty, L1_C_ty],
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
        for _ in range_(0xFFFFFFFF):
            b = B_L3L1_fifo.acquire(1)
            # The kernel function computes m output rows; each core is responsible for (M/cols) output rows, so we need to call the kernel (M/cols)/m times.
            for i_idx in range_(M // m_output // cols):
                c = C_L1L3_fifo.acquire(1)
                i_i32 = index.casts(T.i32(), i_idx)
                for j_idx in range_(m_output // m_input):
                    j_i32 = index.casts(T.i32(), j_idx)
                    output_row_offset = j_i32 * m_input
                    a = A_L3L1_fifo.acquire(1)
                    matvec(m_input, K, output_row_offset, a, b, c)
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
        TensorAccessPattern(
            tensor_dims=(M, K),
            offset=col * (M // cols) * K,
            sizes=[1, 1, 1, (M // cols) * K],
            strides=[0, 0, 0, 1],
        )
        for col in range(cols)
    ]

    # Every column gets the entirety of the vector B, no TAP needed.
    # This design assumes that all of B fits on the cores.

    # Collection pattern for the output vector C: each AIE core writes back its contiguous chunk of rows.
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
    with rt.sequence(L3_A_ty, L3_B_ty, L3_C_ty) as (A, B, C):
        rt.start(*workers)
        tg = rt.task_group()
        for i in range(cols):
            rt.fill(A_L3L1_fifos[i].prod(), A, A_taps[i], task_group=tg)
            rt.fill(B_L3L1_fifos[i].prod(), B, task_group=tg)
        for i in range(cols):
            rt.drain(C_L1L3_fifos[i].cons(), C, C_taps[i], task_group=tg, wait=True)
        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


def main():
    argparser = argparse.ArgumentParser(
        prog="AIE Matrix Vector Multiplication MLIR Design",
    )
    argparser.add_argument("--dev", type=str, choices=["npu", "npu2"], default="npu")
    argparser.add_argument("-M", type=int)
    argparser.add_argument("-K", type=int)
    argparser.add_argument("-m", type=int)
    argparser.add_argument("--cols", type=int)
    argparser.add_argument(
        "--output-file-path",
        "-o",
        type=str,
        help="Output file path for the generated MLIR module",
    )
    args = argparser.parse_args()
    module = my_matvec(args.dev, args.cols, args.M, args.K, args.m)

    output_file_path = Path(args.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))


if __name__ == "__main__":
    main()
