# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from ml_dtypes import bfloat16

import aie.dialects.index as index
from aie.dialects.aie import T
from aie.helpers.dialects.scf import _for as range_
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Kernel, ObjectFifo, Program, Runtime, TaskGroup, Worker

"""
int8-weight matvec design (W8A16, in-kernel dequant).

The fused-sequence layer models every buffer as one of THREE consolidated bf16
memrefs (input/output/scratch; compilation/sequence.py hardcodes ir.BF16Type),
so this operator sticks to the standard 3-arg GEMV shape (W, x, y) and packs
the per-channel group scales INTO the weight buffer:

    per m_input-row tile: [ m_input*K int8 weights | m_input*G bf16 scales ]

(The checkpoint's (K/4, M)-packed int32 qweight and (G, M) fp16 scales are
repacked host-side into this row-major layout, with the sym zero-point 127
already subtracted so the payload is plain int8.)

The C kernel reinterprets the bf16-typed pointers as int8/bf16 byte streams;
dequant happens in registers, so dequantized weights never touch DRAM.
"""

GROUP_SIZE = 128


def my_matvec_int8(
    dev,
    cols,
    M,
    K,
    m_input,
    m_output=None,
    num_batches=1,
    kernel_object="mv_int8.o",
    func_prefix="",
    verbose=False,
    n_aie_rows=1,
    weight_depth=2,
):
    if m_output is None:
        m_output = m_input

    if verbose:
        print(f"Device: {dev}")
        print(f"Matrix dimensions: M={M}, K={K} (int8 weights)")
        print(f"Tiling: m_input={m_input}, m_output={m_output}")
        print(f"Columns: {cols}")

    assert (
        m_output % m_input == 0 and m_output >= m_input
    ), "m_output must be a multiple of m_input"
    assert m_output <= M // cols, "m_output must be less than or equal to M/cols"
    assert (M // cols) % m_output == 0, "m_output must evenly divide M/cols"
    assert m_input <= M // cols, "m_input must be less than or equal to M/cols"
    assert (M // cols) % m_input == 0, "m_input must evenly divide M/cols"
    assert M % cols == 0
    # NOTE on the weight-fifo depth: there is deliberately NO L1 assert here. An early attempt
    # modelled it as `cols * depth * tile_bytes + L1_B + L1_C + scratch` and that model REJECTED
    # depth=2, which is the shipped, working configuration -- so the model's absolute scale is
    # wrong (whatever the placer really charges for a double-buffered fifo, it is not
    # cols*depth*tile_bytes of L1) and it cannot gate anything. Depth is therefore checked
    # NUMERICALLY (the chain's cosine gate) rather than by an assert: an overrun in this design is
    # silent corruption, not a fault, so a deeper fifo must always be validated by the gate.
    assert K % GROUP_SIZE == 0, f"K={K} must be a multiple of GROUP_SIZE={GROUP_SIZE}"
    n_groups = K // GROUP_SIZE

    # Per m_input-row tile payload: int8 weights + bf16 scales, viewed as bf16
    # elements (bytes / 2). Both parts are even-byte so the view is exact.
    tile_bytes = m_input * K + m_input * n_groups * 2
    assert tile_bytes % 2 == 0
    L1_W_ty = np.ndarray[(tile_bytes // 2,), np.dtype[bfloat16]]
    L1_B_ty = np.ndarray[(K,), np.dtype[bfloat16]]
    L1_C_ty = np.ndarray[(m_output,), np.dtype[bfloat16]]

    total_bytes = num_batches * M * tile_bytes // m_input * m_input  # = num_batches * (M/m_input) * tile_bytes
    L3_W_ty = np.ndarray[(num_batches * (M // m_input) * tile_bytes // 2,), np.dtype[bfloat16]]
    L3_B_ty = np.ndarray[(num_batches * K,), np.dtype[bfloat16]]
    L3_C_ty = np.ndarray[(num_batches * M,), np.dtype[bfloat16]]

    matvec = Kernel(
        f"{func_prefix}matvec_vectorized_int8_bf16",
        f"{func_prefix}{kernel_object}",
        [np.int32, np.int32, L1_W_ty, L1_B_ty, L1_C_ty],
    )

    W_L3L1_fifos = [
        [
            ObjectFifo(L1_W_ty, name=f"W_L3L1_{rg}_{i}", depth=weight_depth)
            for i in range(cols)
        ]
        for rg in range(n_aie_rows)
    ]
    B_L3L1_fifos = [
        [
            ObjectFifo(L1_B_ty, name=f"B_L3L1_{rg}_{i}", depth=1)
            for i in range(cols)
        ]
        for rg in range(n_aie_rows)
    ]
    C_L1L3_fifos = [
        [
            ObjectFifo(L1_C_ty, name=f"C_L1L3_{rg}_{i}", depth=2)
            for i in range(cols)
        ]
        for rg in range(n_aie_rows)
    ]

    # M 行按 (col, row) 二维分发：每核 rows_per_core 行（m_input 行/tile）
    rows_per_core = (M // cols) // n_aie_rows
    cchunks_per_core = rows_per_core // m_output

    def core_body(W_L3L1_fifo, B_L3L1_fifo, C_L1L3_fifo, matvec):
        one_idx = index.constant(1)
        for _ in range_(0xFFFFFFFF):  # batch dim handled as part of this loop
            b = B_L3L1_fifo.acquire(1)
            for i_idx in range_(cchunks_per_core):
                c = C_L1L3_fifo.acquire(1)
                i_i32 = index.casts(T.i32(), i_idx)
                for j_idx in range_(m_output // m_input):
                    j_i32 = index.casts(T.i32(), j_idx)
                    output_row_offset = j_i32 * m_input
                    a = W_L3L1_fifo.acquire(1)
                    matvec(m_input, output_row_offset, a, b, c)
                    W_L3L1_fifo.release(1)
                Cf_local = C_L1L3_fifo
                Cf_local = C_L1L3_fifo
                C_L1L3_fifo.release(1)
            B_L3L1_fifo.release(1)

    # WORKER_PIN_ROW: see qkv_head_dp/design_ours_kvlayout.py -- default 2 pins each
    # worker to Tile(col=i, row=2); 0 restores the shipped column-major fold.
    import os as _pin_os
    _WORKER_PIN_ROW = int(_pin_os.environ.get("WORKER_PIN_ROW", "2"))
    from aie.iron.device import Tile as _PinTile
    workers = [
        Worker(
            core_body,
            [
                W_L3L1_fifos[rg][i].cons(),
                B_L3L1_fifos[rg][i].cons(),
                C_L1L3_fifos[rg][i].prod(),
                matvec,
            ],
            **({"tile": _PinTile(col=i, row=_WORKER_PIN_ROW)} if _WORKER_PIN_ROW else {}),
        )
        for rg in range(n_aie_rows)
        for i in range(cols)
    ]

    # Weight stream: one whole-column contiguous fill per column (1-D tap).
    # NOTE: the whole-column run exceeds the shim 16383-word BD cap at
    # M>=1024, where aiecc auto-splits the BD — earlier experiments with
    # manual splits (2-D BD, multi-BD, dual FIFO) all failed differently;
    # the reference "known good" configuration is M<=512 (<=32 sub-tiles).
    W_elems_per_col = (M // cols) // m_input * tile_bytes // 2
    W_elems_per_core = rows_per_core // m_input * tile_bytes // 2
    W_taps = [
        [
            [
                TensorAccessPattern(
                    tensor_dims=L3_W_ty.__args__[0],
                    offset=(col * (M // cols) + rg * rows_per_core) // m_input
                    * tile_bytes // 2
                    + batch * W_elems_per_col * cols,
                    sizes=[1, 1, 1, W_elems_per_col],
                    strides=[0, 0, 0, 1],
                )
                for batch in range(num_batches)
            ]
            for col in range(cols)
        ]
        for rg in range(n_aie_rows)
    ]
    B_tap = TensorAccessPattern(
        tensor_dims=L3_B_ty.__args__[0],
        offset=0,
        sizes=[1, 1, 1, num_batches * K],
        strides=[0, 0, 0, 1],
    )
    C_taps = [
        [
            [
                TensorAccessPattern(
                    tensor_dims=L3_C_ty.__args__[0],
                    offset=col * (M // cols) + rg * rows_per_core + batch * M,
                    sizes=[1, 1, 1, rows_per_core],
                    strides=[0, 0, 0, 1],
                )
                for batch in range(num_batches)
            ]
            for col in range(cols)
        ]
        for rg in range(n_aie_rows)
    ]

    def sequence(W, B, C, W_prods, B_prods, C_cons):
        tg_b = TaskGroup()
        for rg in range(n_aie_rows):
            for col in range(cols):
                B_prods[rg][col].fill(B, B_tap, group=tg_b)
        tg_ac = TaskGroup()
        for rg in range(n_aie_rows):
            for col in range(cols):
                W_prods[rg][col].fill(W, W_taps[rg][col][0], group=tg_ac)
        for rg in range(n_aie_rows):
            for col in range(cols):
                C_cons[rg][col].drain(
                    C,
                    C_taps[rg][col][0],
                    group=tg_ac,
                    wait=True,
                )
        tg_ac.finish()
        tg_b.finish()

    rt = Runtime(
        sequence,
        [
            L3_W_ty,
            L3_B_ty,
            L3_C_ty,
            [[f.prod() for f in row] for row in W_L3L1_fifos],
            [[f.prod() for f in row] for row in B_L3L1_fifos],
            [[f.cons() for f in row] for row in C_L1L3_fifos],
        ],
    )
    return Program(dev, rt, workers=workers).resolve_program()
