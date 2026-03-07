# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from pathlib import Path
from ml_dtypes import bfloat16
import argparse

from aie.dialects.aie import *
from aie.dialects.aiex import *
from aie.helpers.dialects.scf import _for as range_
from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2

"""
FlowKV Decode Attention Design.

Streaming decode attention with online softmax using a 2-tile pipeline per KV
head group. Intermediates (exponentiated scores, correction factors, denominator)
flow tile-to-tile via on-chip ObjectFIFOs and never touch DDR.

Architecture (per KV head group, processing `group_size` query heads):

  Score Tile (CT0):
    Inputs:  Q vector + RoPE angles (group_size * head_dim + head_dim bf16) from DDR
             K chunk  (chunk_size * head_dim bf16) streamed from KV cache
    Compute: RoPE(Q) * K^T / sqrt(d), online softmax tracking
    Output:  Packed [F_c | C_c | l] to Value Tile via on-chip FIFO

  Value Tile (CT1):
    Inputs:  Packed [F_c | C_c | l] from Score Tile (on-chip FIFO)
             V chunk  (chunk_size * head_dim bf16) streamed from KV cache
    Compute: Y = C_c * Y_old + F_c^T * V_c; final O = Y / l
    Output:  Attention output (group_size * head_dim bf16) to DDR

DMA channel budget per tile:
  Score tile: 2 input (Q, K_chunk) + 1 output (inter) = within 2+2 limit
  Value tile: 2 input (inter, V_chunk) + 1 output (O) = within 2+2 limit

Layout: `num_cols` columns, each processing one KV head group. The runtime
sequence iterates over batches of `num_cols` groups.

DDR buffer layout (3 sequence args):
  arg0: KV cache -- interleaved K and V per position per head.
        Shape: (num_kv_heads, seq_len, 2, head_dim) flattened.
  arg1: Q vectors + RoPE angles -- per KV group: Q heads then interleaved cos/sin.
        Layout: [Q_group0 (gs*hd) | angles (hd) | Q_group1 (gs*hd) | angles (hd) | ...]
        Shape: (num_kv_heads * (group_size * head_dim + head_dim),) flattened.
  arg2: Output -- attention result.
        Shape: (num_heads, head_dim) flattened.
"""


def my_flowkv_decode(
    dev,
    num_heads,
    num_kv_heads,
    head_dim,
    seq_len,
    chunk_size=32,
    num_cols=4,
):
    group_size = num_heads // num_kv_heads
    num_chunks = seq_len // chunk_size
    assert seq_len % chunk_size == 0, "seq_len must be divisible by chunk_size"
    assert num_kv_heads % num_cols == 0, "num_kv_heads must be divisible by num_cols"

    dtype_in = np.dtype[bfloat16]

    dev_ty = NPU1() if dev == "npu" else NPU2()

    # -------------------------------------------------------------------------
    # L1 tile types
    # -------------------------------------------------------------------------
    # Query vectors for one KV group, plus RoPE angles (head_dim interleaved
    # cos/sin values) packed at the end.
    L1_Q_ty = np.ndarray[(group_size * head_dim + head_dim,), dtype_in]

    # K or V chunk
    L1_KV_chunk_ty = np.ndarray[(chunk_size * head_dim,), dtype_in]

    # Packed inter-tile buffer:
    # [F_c(chunk_size * group_size) | C_c(group_size) | l(group_size)]
    inter_tile_size = chunk_size * group_size + 2 * group_size
    L1_inter_ty = np.ndarray[(inter_tile_size,), dtype_in]

    # Output for one KV group
    L1_out_ty = np.ndarray[(group_size * head_dim,), dtype_in]

    # -------------------------------------------------------------------------
    # L3 (DDR) buffer types
    # -------------------------------------------------------------------------
    L3_KV_ty = np.ndarray[(num_kv_heads * seq_len * 2 * head_dim,), dtype_in]
    # Q DDR layout: [Q_group0 (gs*hd) | angles (hd) | Q_group1 (gs*hd) | angles (hd) | ...]
    # Each group block = group_size * head_dim + head_dim contiguous bf16 values.
    q_group_stride = group_size * head_dim + head_dim
    L3_Q_ty = np.ndarray[(num_kv_heads * q_group_stride,), dtype_in]
    L3_O_ty = np.ndarray[(num_heads * head_dim,), dtype_in]

    # -------------------------------------------------------------------------
    # Kernel declarations (all from flowkv.o)
    # -------------------------------------------------------------------------
    score_init = Kernel(
        "flowkv_score_init_bf16",
        "flowkv.o",
        [np.int32],
    )

    score_rope_q = Kernel(
        "flowkv_score_rope_q_bf16",
        "flowkv.o",
        [
            L1_Q_ty,  # q_in (Q heads + packed angles)
            np.int32,  # num_q_heads
            np.int32,  # head_dim
        ],
    )

    score_chunk = Kernel(
        "flowkv_score_chunk_bf16",
        "flowkv.o",
        [
            L1_Q_ty,  # q_in
            L1_KV_chunk_ty,  # k_chunk
            L1_inter_ty,  # packed_out
            np.int32,  # num_q_heads
            np.int32,  # head_dim
            np.int32,  # chunk_size
        ],
    )

    value_init = Kernel(
        "flowkv_value_init_bf16",
        "flowkv.o",
        [np.int32, np.int32],
    )

    value_accum_fn = Kernel(
        "flowkv_value_accum_bf16",
        "flowkv.o",
        [
            L1_inter_ty,  # packed_in
            L1_KV_chunk_ty,  # v_chunk
            np.int32,  # num_q_heads
            np.int32,  # head_dim
            np.int32,  # chunk_size
        ],
    )

    value_normalize = Kernel(
        "flowkv_value_normalize_bf16",
        "flowkv.o",
        [
            L1_out_ty,  # output
            np.int32,  # num_q_heads
            np.int32,  # head_dim
        ],
    )

    # -------------------------------------------------------------------------
    # ObjectFIFOs per column
    # -------------------------------------------------------------------------
    Q_fifos = [ObjectFifo(L1_Q_ty, name=f"Q_{i}", depth=1) for i in range(num_cols)]
    K_fifos = [
        ObjectFifo(L1_KV_chunk_ty, name=f"K_{i}", depth=2) for i in range(num_cols)
    ]
    V_fifos = [
        ObjectFifo(L1_KV_chunk_ty, name=f"V_{i}", depth=2) for i in range(num_cols)
    ]
    inter_fifos = [
        ObjectFifo(L1_inter_ty, name=f"inter_{i}", depth=2) for i in range(num_cols)
    ]
    O_fifos = [ObjectFifo(L1_out_ty, name=f"O_{i}", depth=2) for i in range(num_cols)]

    # -------------------------------------------------------------------------
    # Score tile core body
    # -------------------------------------------------------------------------
    def score_core_body(
        q_fifo, k_fifo, inter_fifo, score_init_fn, score_rope_q_fn, score_chunk_fn
    ):
        for _ in range_(0xFFFFFFFF):
            # Initialize softmax state
            score_init_fn(group_size)

            # Acquire Q (held for all chunks in this attention computation)
            q = q_fifo.acquire(1)

            # Apply RoPE rotation to Q and store in static buffer
            score_rope_q_fn(q, group_size, head_dim)

            # Stream through K chunks
            for _ in range_(num_chunks):
                k = k_fifo.acquire(1)
                inter = inter_fifo.acquire(1)

                score_chunk_fn(
                    q,
                    k,
                    inter,
                    group_size,
                    head_dim,
                    chunk_size,
                )

                k_fifo.release(1)
                inter_fifo.release(1)

            q_fifo.release(1)

    # -------------------------------------------------------------------------
    # Value tile core body
    # -------------------------------------------------------------------------
    def value_core_body(
        inter_fifo,
        v_fifo,
        o_fifo,
        value_init_fn,
        value_accum_fn_arg,
        value_normalize_fn,
    ):
        for _ in range_(0xFFFFFFFF):
            # Initialize accumulator
            value_init_fn(group_size, head_dim)

            # Stream through V chunks, accumulating weighted values
            for _ in range_(num_chunks):
                inter = inter_fifo.acquire(1)
                v = v_fifo.acquire(1)

                value_accum_fn_arg(
                    inter,
                    v,
                    group_size,
                    head_dim,
                    chunk_size,
                )

                inter_fifo.release(1)
                v_fifo.release(1)

            # Normalize and write output
            # The denominator was saved in the kernel's static buffer by the
            # last accum call.
            o = o_fifo.acquire(1)
            value_normalize_fn(o, group_size, head_dim)
            o_fifo.release(1)

    # -------------------------------------------------------------------------
    # Create Workers
    # -------------------------------------------------------------------------
    score_workers = [
        Worker(
            score_core_body,
            [
                Q_fifos[i].cons(),
                K_fifos[i].cons(),
                inter_fifos[i].prod(),
                score_init,
                score_rope_q,
                score_chunk,
            ],
        )
        for i in range(num_cols)
    ]

    value_workers = [
        Worker(
            value_core_body,
            [
                inter_fifos[i].cons(),
                V_fifos[i].cons(),
                O_fifos[i].prod(),
                value_init,
                value_accum_fn,
                value_normalize,
            ],
        )
        for i in range(num_cols)
    ]

    # -------------------------------------------------------------------------
    # Tensor Access Patterns
    # -------------------------------------------------------------------------
    # KV cache DDR layout: interleaved K and V per head per position.
    # For KV head h, position p:
    #   K[h, p, :] at offset (h * seq_len * 2 + p * 2) * head_dim
    #   V[h, p, :] at offset (h * seq_len * 2 + p * 2 + 1) * head_dim
    #
    # DMA streams chunk_size K rows (every other row in the interleaved layout)
    # followed by chunk_size V rows.

    def make_q_tap(kv_head_idx):
        """Q tap: select group_size query heads + RoPE angles for this KV group.

        DDR layout: [Q_group0 (gs*hd) | angles (hd) | Q_group1 ...].
        Each group block is q_group_stride contiguous bf16 values.
        """
        q_offset = kv_head_idx * q_group_stride
        return TensorAccessPattern(
            tensor_dims=(num_kv_heads * q_group_stride,),
            offset=q_offset,
            sizes=[1, 1, 1, q_group_stride],
            strides=[0, 0, 0, 1],
        )

    def make_k_tap(kv_head_idx):
        """K tap: stream K rows from interleaved KV cache."""
        base = kv_head_idx * seq_len * 2 * head_dim
        return TensorAccessPattern(
            tensor_dims=(num_kv_heads * seq_len * 2 * head_dim,),
            offset=base,
            # Read seq_len K rows (stride 2*head_dim to skip V rows)
            sizes=[1, seq_len, 1, head_dim],
            strides=[0, 2 * head_dim, 0, 1],
        )

    def make_v_tap(kv_head_idx):
        """V tap: stream V rows from interleaved KV cache."""
        base = kv_head_idx * seq_len * 2 * head_dim + head_dim
        return TensorAccessPattern(
            tensor_dims=(num_kv_heads * seq_len * 2 * head_dim,),
            offset=base,
            sizes=[1, seq_len, 1, head_dim],
            strides=[0, 2 * head_dim, 0, 1],
        )

    def make_o_tap(kv_head_idx):
        """Output tap: write group_size heads of attention output."""
        o_offset = kv_head_idx * group_size * head_dim
        return TensorAccessPattern(
            tensor_dims=(num_heads * head_dim,),
            offset=o_offset,
            sizes=[1, 1, 1, group_size * head_dim],
            strides=[0, 0, 0, 1],
        )

    # -------------------------------------------------------------------------
    # Runtime sequence
    # -------------------------------------------------------------------------
    all_workers = score_workers + value_workers
    num_batches = num_kv_heads // num_cols

    rt = Runtime()
    with rt.sequence(L3_KV_ty, L3_Q_ty, L3_O_ty) as (KV, Q, O):
        rt.start(*all_workers)

        for batch_idx in range(num_batches):
            tg = rt.task_group()

            for col in range(num_cols):
                kv_head_idx = batch_idx * num_cols + col

                rt.fill(
                    Q_fifos[col].prod(),
                    Q,
                    make_q_tap(kv_head_idx),
                    task_group=tg,
                )
                rt.fill(
                    K_fifos[col].prod(),
                    KV,
                    make_k_tap(kv_head_idx),
                    task_group=tg,
                )
                rt.fill(
                    V_fifos[col].prod(),
                    KV,
                    make_v_tap(kv_head_idx),
                    task_group=tg,
                )

            for col in range(num_cols):
                kv_head_idx = batch_idx * num_cols + col

                rt.drain(
                    O_fifos[col].cons(),
                    O,
                    make_o_tap(kv_head_idx),
                    task_group=tg,
                    wait=True,
                )

            rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        prog="AIE FlowKV Decode Attention Design",
    )
    argparser.add_argument("--dev", type=str, choices=["npu", "npu2"], default="npu2")
    argparser.add_argument("--num-heads", type=int, default=32)
    argparser.add_argument("--num-kv-heads", type=int, default=8)
    argparser.add_argument("--head-dim", type=int, default=64)
    argparser.add_argument("--seq-len", type=int, required=True)
    argparser.add_argument("--chunk-size", type=int, default=32)
    argparser.add_argument("--num-cols", type=int, default=4)
    argparser.add_argument(
        "--output-file-path",
        "-o",
        type=str,
        help="Output file path for the generated MLIR module",
    )
    args = argparser.parse_args()
    module = my_flowkv_decode(
        args.dev,
        args.num_heads,
        args.num_kv_heads,
        args.head_dim,
        args.seq_len,
        args.chunk_size,
        args.num_cols,
    )

    output_file_path = Path(args.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
