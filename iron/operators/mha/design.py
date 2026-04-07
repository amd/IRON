# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import sys
import math
import copy
from pathlib import Path

from ml_dtypes import bfloat16
import numpy as np

from aie.iron import (
    Kernel,
    ObjectFifo,
    Program,
    Runtime,
    Worker,
    Buffer,
    WorkerRuntimeBarrier,
)
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU2, Tile
from aie.iron.controlflow import range_
from aie.helpers.taplib import TensorTiler2D, TensorAccessSequence, TensorAccessPattern
from aie.helpers.dialects.scf import if_, else_

dtype_map = {
    "bf16": bfloat16,
    "f32": np.float32,
}

microkernel_mac_dim_map = {
    "npu": {
        "bf16": (4, 8, 4),
    },
    "npu1": {
        "bf16": (4, 8, 4),
    },
    "npu2": {
        "bf16": {
            # emulate_bf16_mmul_with_bfp16
            True: (8, 8, 8),
            False: (4, 8, 8),
        },
    },
}


def main():
    argparser = argparse.ArgumentParser(
        prog="AIE Matrix Multiplication MLIR Design (Single Core)",
        description="Emits MLIR code for a matrix multiplication design of the given input size",
    )
    argparser.add_argument("--heads", type=int, default=1)
    argparser.add_argument("--S_q", type=int, default=256)
    argparser.add_argument("--S_kv", type=int, default=256)
    argparser.add_argument("-d", type=int, default=64)
    argparser.add_argument("--B_q", type=int, default=64)
    argparser.add_argument("--B_kv", type=int, default=64)
    argparser.add_argument(
        "--num_KV_heads",
        type=int,
        default=2,
        help="Number of heads for Key-Value pairs",
    )
    argparser.add_argument("--number-of-pipeline", type=int, default=1)
    argparser.add_argument("--emulate-bf16-mmul-with-bfp16", type=bool, default=False)
    argparser.add_argument("--trace_size", type=int, default=0)
    argparser.add_argument(
        "--output-file-path",
        "-o",
        type=str,
        default="my_mha.mlir",
        help="Output file path for the generated MLIR module",
    )
    argparser.add_argument(
        "--verbose", action="store_true", help="Enable verbose output"
    )

    args = argparser.parse_args()
    dev = NPU2()

    maybe_module = fused_mha(
        dev=dev,
        heads=args.heads,
        S_q=args.S_q,
        S_kv=args.S_kv,
        d=args.d,
        B_q=args.B_q,
        B_kv=args.B_kv,
        number_of_pipelines=args.number_of_pipeline,
        num_KV_heads=args.num_KV_heads,
        emulate_bf16_mmul_with_bfp16=args.emulate_bf16_mmul_with_bfp16,
        trace_size=args.trace_size,
        verbose=args.verbose,
    )

    output_file_path = Path(args.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(maybe_module))

    if args.verbose:
        print(f"MLIR module written to {output_file_path}")


def fused_mha(
    dev,
    heads: int,
    S_q: int,
    S_kv: int,
    d: int,
    B_q: int,
    B_kv: int,
    number_of_pipelines: int,
    num_KV_heads: int,
    emulate_bf16_mmul_with_bfp16: bool,
    trace_size: int = 0,
    verbose: bool = False,
):

    of_depth = 2
    vectorized = True
    enable_tracing = trace_size > 0
    dtype_str = "bf16"

    if number_of_pipelines > 6:
        number_of_pipelines_join_distribute = number_of_pipelines // 2
    else:
        number_of_pipelines_join_distribute = number_of_pipelines

    S_q_eff = S_q
    S_kv_eff = S_kv
    S_q_pad = (
        (S_q_eff + (B_q * number_of_pipelines - 1)) // (B_q * number_of_pipelines)
    ) * (B_q * number_of_pipelines)
    S_kv_pad = (
        (S_kv_eff + (B_kv * number_of_pipelines - 1)) // (B_kv * number_of_pipelines)
    ) * (B_kv * number_of_pipelines)
    num_q_blocks = S_q_pad // B_q
    num_kv_blocks = S_kv_pad // B_kv
    num_q_block_per_pipeline = num_q_blocks // number_of_pipelines

    # VJUNG: When the number of KV heads is 0, treat it as regular MHA (num_KV_heads == heads).
    # Otherwise, num_KV_heads < heads indicates GQA.
    if num_KV_heads == 0:
        num_KV_heads = heads

    assert (
        emulate_bf16_mmul_with_bfp16
    ), "Only emulate_bf16_mmul_with_bfp16=True is supported"

    # r, s, t are the dimensions required by the microkernel MAC instructions.
    mac_dims = microkernel_mac_dim_map["npu2"][dtype_str]
    r, s, t = mac_dims[emulate_bf16_mmul_with_bfp16]

    if verbose:
        print(f"Device: {dev}")
        print(f"Number of heads: {heads}")
        print(f"MHA Dimensions: S_q={S_q}, S_kv={S_kv}, d={d}, B_q={B_q}, B_kv={B_kv}")
        print(f"Padded Dimensions: S_q_pad={S_q_pad}, S_kv_pad={S_kv_pad}")
        print(f"Data type: {dtype_str}")
        print(f"Microkernel MAC dimensions: r={r}, s={s}, t={t}")
        print(f"Vectorized: {vectorized}")
        print(f"Enable tracing: {enable_tracing}")

    assert num_KV_heads > 0, "Number of KV heads must be greater than 0"
    assert heads > 0, "Number of heads must be greater than 0"
    assert (
        num_KV_heads <= heads
    ), "Number of KV heads must be less than or equal to number of heads"
    assert (
        heads % num_KV_heads == 0
    ), f"Number of heads ({heads}) must be divisible by number of KV heads ({num_KV_heads})"

    assert B_q % r == 0, f"B_q must be divisible by r ({B_q} % {r} != 0)"
    assert B_kv % t == 0, f"B_kv must be divisible by t ({B_kv} % {t} != 0)"
    assert d % s == 0, f"d must be divisible by s ({d} % {s} != 0)"

    assert S_q_pad % B_q == 0, "Padded S_q must be divisible by B_q"
    assert S_kv_pad % B_kv == 0, "Padded S_kv must be divisible by B_kv"

    dtype = dtype_map[dtype_str]

    inv_scale = (
        1 / np.sqrt(d)
    ) * 1.4453125  # 1.4453125 ≈ log2(e), converts softmax base

    # Tensors living in DRAM
    Q_ty = np.ndarray[
        (
            heads,
            S_q_pad,
            d,
        ),
        np.dtype[dtype],
    ]
    KV_ty = np.ndarray[
        (
            num_KV_heads,
            S_kv_pad * d,
        ),
        np.dtype[dtype],
    ]

    # Tensors living on the AIE-array
    q_ty = np.ndarray[(B_q, d), np.dtype[dtype]]
    k_ty = np.ndarray[(d, B_kv), np.dtype[dtype]]
    qk_ty = np.ndarray[(B_q, B_kv), np.dtype[dtype]]
    s_ty = np.ndarray[(4 * B_q,), np.dtype[dtype]]

    # AIE kernel declarations
    func_type = "" if vectorized else "_scalar"
    zero_kernel = Kernel(f"zero_{dtype_str}", "mha.o", [qk_ty])

    memcopy_kernel_scale = Kernel(
        f"passThroughLine", "mha_passThrough.o", [s_ty, s_ty, np.int32]
    )

    scale_buffer_init_kernel = Kernel("init_scale_buffer", "mha.o", [s_ty, np.int32])

    partial_softmax_kernel = Kernel(
        "partial_softmax",
        "mha.o",
        [
            qk_ty,
            qk_ty,
            s_ty,
            np.ndarray[(2,), np.dtype[np.int32]],
            dtype,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    matmul_QK = Kernel(
        f"matmul_bf16_bf16_wrapper{func_type}",
        "mha.o",
        [q_ty, k_ty, qk_ty, np.ndarray[(2,), np.dtype[np.int32]]],
    )

    matmul_PV = Kernel(
        "matmul_PV",
        "mha.o",
        [
            qk_ty,
            k_ty,
            qk_ty,
            s_ty,
            np.int32,
            np.int32,
            np.ndarray[(2,), np.dtype[np.int32]],
        ],
    )

    rescale_O = Kernel(
        "rescale_O",
        "mha.o",
        [qk_ty, s_ty, np.int32, np.ndarray[(2,), np.dtype[np.int32]]],
    )

    # AIE-array data movement with object fifos
    q_dims = None
    if vectorized:
        q_dims = [(B_q // r, r * d), (d // s, s), (r, d), (s, 1)]

    inQ = ObjectFifo(
        np.ndarray[(number_of_pipelines_join_distribute * B_q, d), np.dtype[dtype]],
        name="inQ",
    )
    memQ = inQ.cons().split(
        offsets=[B_q * d * i for i in range(number_of_pipelines_join_distribute)],
        obj_types=[q_ty] * number_of_pipelines_join_distribute,
        names=[f"memQ{i}" for i in range(number_of_pipelines_join_distribute)],
        dims_to_stream=[q_dims] * number_of_pipelines_join_distribute,
        depths=[of_depth] * number_of_pipelines_join_distribute,
        placement=Tile(col=6, row=1),
    )  # Split between N pipelines
    if number_of_pipelines > 6:
        inQ2 = ObjectFifo(
            np.ndarray[(number_of_pipelines_join_distribute * B_q, d), np.dtype[dtype]],
            name="inQ2",
        )
        memQ += inQ2.cons().split(
            offsets=[B_q * d * i for i in range(number_of_pipelines_join_distribute)],
            obj_types=[q_ty] * number_of_pipelines_join_distribute,
            names=[f"memQ2{i}" for i in range(number_of_pipelines_join_distribute)],
            dims_to_stream=[q_dims] * number_of_pipelines_join_distribute,
            depths=[of_depth] * number_of_pipelines_join_distribute,
            placement=Tile(col=7, row=1),
        )  # Split between N pipelines

    # VJUNG: The SequentialPlacer will place all of these on the same MemTile if Placement is specified. We would need a list of placement in case of one-many or many-one.
    # I think the Sequential Placer will fail if we do a split/join with more than 6 I/Os cuz it tries to place them all on the same tile.

    # K is stored in column-major order
    k_dims = None
    if vectorized:
        k_dims = [(B_kv // t, t * d), (d // s, s), (t, d), (s, 1)]
    inK = ObjectFifo(
        k_ty,
        name="inK",
        depth=of_depth,
    )
    memK = inK.cons().forward(
        name="memK",
        dims_to_stream=k_dims,
        placement=Tile(col=3, row=1),
        depth=of_depth,
    )  # Broadcast, give this handle to N pipelines

    v_dims = None
    if vectorized:
        v_dims = [(B_kv // s, s * B_kv), (B_kv // t, t), (s, B_kv), (t, 1)]

    inV = ObjectFifo(
        k_ty,
        name="inV",
        depth=of_depth,
    )
    memV = inV.cons().forward(
        name="memV",
        dims_to_stream=v_dims,
        placement=Tile(col=4, row=1),
        depth=of_depth,
    )  # Broadcast, give this handle to N pipelines

    a_dims = None
    if vectorized:
        a_dims = [(B_q // r, r * B_kv), (r, t), (B_kv // t, r * t), (t, 1)]
    memA = []
    outA = []
    for i in range(number_of_pipelines):
        memA.append(ObjectFifo(qk_ty, depth=of_depth, name=f"memA{i}"))
        outA.append(
            memA[i]
            .cons()
            .forward(
                name=f"outA{i}",
                dims_to_stream=a_dims,
                depth=of_depth,
                # placement=Tile(col=i, row=1))
            )
        )  # Local to 1 pipeline

    memP = []
    outP = []
    for i in range(number_of_pipelines):
        memP.append(ObjectFifo(qk_ty, depth=of_depth, name=f"memP{i}"))
        outP.append(
            memP[i]
            .cons()
            .forward(
                name=f"outP{i}",
                dims_to_stream=q_dims,
                depth=of_depth,
                # placement=Tile(col=i, row=1)
            )
        )  # Local to 1 pipeline

    # Scale buffer for partial softmax
    scaleOF = []
    for i in range(number_of_pipelines):
        scaleOF.append(
            ObjectFifo(s_ty, depth=of_depth, name=f"scaleOF{i}")
        )  # Local to 1 pipeline

    o_dims = None
    if vectorized:
        o_dims = [(B_q // r, r * B_kv), (r, t), (B_kv // t, r * t), (t, 1)]
    memO = ObjectFifo(
        np.ndarray[(number_of_pipelines_join_distribute * B_q, d), np.dtype[dtype]],
        name="memO",
        dims_to_stream=o_dims,
    )
    outO = memO.prod().join(
        offsets=[B_q * d * i for i in range(number_of_pipelines_join_distribute)],
        obj_types=[q_ty] * number_of_pipelines_join_distribute,
        names=[f"outO{i}" for i in range(number_of_pipelines_join_distribute)],
        depths=[of_depth] * number_of_pipelines_join_distribute,
        placement=Tile(col=6, row=1),
    )  # Join onto the output OF
    if number_of_pipelines > 6:
        memO2 = ObjectFifo(
            np.ndarray[(number_of_pipelines_join_distribute * B_q, d), np.dtype[dtype]],
            name="memO2",
            dims_to_stream=o_dims,
        )
        outO += memO2.prod().join(
            offsets=[B_q * d * i for i in range(number_of_pipelines_join_distribute)],
            obj_types=[q_ty] * number_of_pipelines_join_distribute,
            names=[f"outO2{i}" for i in range(number_of_pipelines_join_distribute)],
            depths=[of_depth] * number_of_pipelines_join_distribute,
            placement=Tile(col=7, row=1),
        )

    def batched_matmul_qk(
        of_q,
        of_k,
        of_a_out,
        zero,
        matmul_QK,
        q_block_bias,
        mha_rtps,
        barrier,
        idx_buffer,
    ):

        barrier.wait_for_value(1)

        loop_idx_q = mha_rtps[0]
        loop_idx_kv = mha_rtps[1]

        for _ in range_(sys.maxsize):

            idx_buffer[0] = 0
            idx_buffer[1] = q_block_bias

            for _ in range_(loop_idx_q):

                elem_in_q = of_q.acquire(1)

                for _ in range_(loop_idx_kv):

                    elem_in_k = of_k.acquire(1)
                    elem_a_out = of_a_out.acquire(1)

                    zero(elem_a_out)
                    matmul_QK(elem_in_q, elem_in_k, elem_a_out, idx_buffer)

                    of_k.release(1)
                    of_a_out.release(1)

                    idx_buffer[0] += 1
                idx_buffer[0] = 0
                idx_buffer[1] += number_of_pipelines

                of_q.release(1)

    def softmax(
        of_in_a,
        of_out_p,
        of_out_scale,
        partial_softmax,
        init_scale_buffer,
        memcopy_kernel_scale,
        q_block_bias,
        mha_rtps,
        barrier,
        idx_buffer,
        scale_buffer,
    ):

        # VJUNG: The index buffer count how many Q and KV block this worker has processed
        # From this info we can infer the position in A and P

        barrier.wait_for_value(1)

        loop_idx_q = mha_rtps[0]
        loop_idx_kv = mha_rtps[1]

        S_q_effective = mha_rtps[2]
        S_kv_effective = mha_rtps[3]

        for _ in range_(sys.maxsize):

            # VJUNG: Required otherwise the buffer is maintained when doing warmup!
            idx_buffer[0] = 0
            idx_buffer[1] = q_block_bias

            for _ in range_(loop_idx_q):

                init_scale_buffer(scale_buffer, B_q)

                for _ in range_(loop_idx_kv):

                    elt_of_out_p = of_out_p.acquire(1)
                    elt_of_in_a = of_in_a.acquire(1)
                    elt_of_out_scale = of_out_scale.acquire(1)

                    partial_softmax(
                        elt_of_in_a,
                        elt_of_out_p,
                        scale_buffer,
                        idx_buffer,
                        inv_scale,
                        B_q,
                        B_kv,
                        S_q_effective,
                        S_kv_effective,
                    )
                    memcopy_kernel_scale(scale_buffer, elt_of_out_scale, 4 * B_q)

                    of_in_a.release(1)
                    of_out_p.release(1)
                    of_out_scale.release(1)

                    idx_buffer[0] += 1
                idx_buffer[0] = 0
                idx_buffer[1] += number_of_pipelines

    def batched_matmul_pv(
        of_p,
        of_v,
        of_scale,
        of_o_out,
        zero,
        matmul_PV,
        rescale_O,
        q_block_bias,
        mha_rtps,
        barrier,
        idx_buffer,
    ):

        barrier.wait_for_value(1)

        loop_idx_q = mha_rtps[0]
        loop_idx_kv = mha_rtps[1]

        for _ in range_(sys.maxsize):

            # VJUNG: Required otherwise the buffer is maintained when doing warmup!
            idx_buffer[0] = 0
            idx_buffer[1] = q_block_bias

            for _ in range_(loop_idx_q):

                elem_o_out = of_o_out.acquire(1)

                zero(elem_o_out)

                ### First iteration, don't rescale O_{i-1}
                elem_in_p = of_p.acquire(1)
                elem_in_v = of_v.acquire(1)
                elt_of_out_scale = of_scale.acquire(1)

                matmul_PV(
                    elem_in_p,
                    elem_in_v,
                    elem_o_out,
                    elt_of_out_scale,
                    B_q,
                    0,
                    idx_buffer,
                )

                of_p.release(1)
                of_v.release(1)
                of_scale.release(1)

                idx_buffer[0] += 1
                ###

                with if_(loop_idx_kv > 2) as if_op:
                    for _ in range_(loop_idx_kv - 2):
                        elem_in_p = of_p.acquire(1)
                        elem_in_v = of_v.acquire(1)
                        elt_of_out_scale2 = of_scale.acquire(1)

                        matmul_PV(
                            elem_in_p,
                            elem_in_v,
                            elem_o_out,
                            elt_of_out_scale2,
                            B_q,
                            1,
                            idx_buffer,
                        )

                        of_p.release(1)
                        of_v.release(1)
                        of_scale.release(1)

                        idx_buffer[0] += 1

                ### Last iteration, final rescaling
                with if_(loop_idx_kv > 1) as if_op:
                    elem_in_p = of_p.acquire(1)
                    elem_in_v = of_v.acquire(1)
                    elt_of_out_scale3 = of_scale.acquire(1)

                    matmul_PV(
                        elem_in_p,
                        elem_in_v,
                        elem_o_out,
                        elt_of_out_scale3,
                        B_q,
                        1,
                        idx_buffer,
                    )
                    rescale_O(elem_o_out, elt_of_out_scale3, B_q, idx_buffer)

                    of_p.release(1)
                    of_v.release(1)
                    of_scale.release(1)

                    idx_buffer[0] += 1
                # else:
                with else_(if_op):
                    rescale_O(elem_o_out, elt_of_out_scale, B_q, idx_buffer)
                    idx_buffer[0] += 1
                ###

                idx_buffer[0] = 0
                idx_buffer[1] += number_of_pipelines

                of_o_out.release(1)

    # Runtime parameter for workers loop index
    # VJUNG: We need one Buffer per worker since they need to be placed
    mha_rtps_list = [
        [
            Buffer(
                np.ndarray[(4,), np.dtype[np.int32]],
                name=f"mha_rtpss_{i}_stage{j}",
                initial_value=None,
                use_write_rtp=True,
            )
            for i in range(number_of_pipelines)
        ]
        for j in range(3)
    ]

    worker_barrier_list = [
        [WorkerRuntimeBarrier(initial_value=0) for i in range(number_of_pipelines)]
        for j in range(3)
    ]

    # Create worker from task
    matmul_workers = []
    softmax_workers = []
    matmul_pv_workers = []
    for i in range(number_of_pipelines):
        idx_buffer_qk = Buffer(
            initial_value=np.zeros(shape=(2,), dtype=np.int32),
            name=f"idx_buffer_qk_{i}",
        )
        matmul_workers.append(
            Worker(
                batched_matmul_qk,
                fn_args=[
                    memQ[i].cons(),
                    memK.cons(),
                    memA[i].prod(),
                    zero_kernel,
                    matmul_QK,
                    i,
                    mha_rtps_list[0][i],
                    worker_barrier_list[0][i],
                    idx_buffer_qk,
                ],
                stack_size=0xD00,
                placement=Tile(col=i, row=2),
                while_true=False,
            )
        )
        idx_buffer_softmax = Buffer(
            initial_value=np.zeros(shape=(2,), dtype=np.int32),
            name=f"idx_buffer_softmax_{i}",
        )
        scale_buffer_softmax = Buffer(
            initial_value=np.zeros(shape=(4 * B_q,), dtype=dtype),
            name=f"scale_buffer_softmax_{i}",
        )
        softmax_workers.append(
            Worker(
                softmax,
                fn_args=[
                    outA[i].cons(),
                    memP[i].prod(),
                    scaleOF[i].prod(),
                    partial_softmax_kernel,
                    scale_buffer_init_kernel,
                    memcopy_kernel_scale,
                    i,
                    mha_rtps_list[1][i],
                    worker_barrier_list[1][i],
                    idx_buffer_softmax,
                    scale_buffer_softmax,
                ],
                stack_size=0xD00,
                placement=Tile(col=i, row=3),
                while_true=False,
            )
        )
        idx_buffer_pv = Buffer(
            initial_value=np.zeros(shape=(2,), dtype=np.int32),
            name=f"idx_buffer_pv_{i}",
        )
        matmul_pv_workers.append(
            Worker(
                batched_matmul_pv,
                fn_args=[
                    outP[i].cons(),
                    memV.cons(),
                    scaleOF[i].cons(),
                    outO[i].prod(),
                    zero_kernel,
                    matmul_PV,
                    rescale_O,
                    i,
                    mha_rtps_list[2][i],
                    worker_barrier_list[2][i],
                    idx_buffer_pv,
                ],
                stack_size=0xD00,
                placement=Tile(col=i, row=4),
                while_true=False,
            )
        )

    # Define tensor access patterns for inputs/outputs
    # A and B are tiled across M and N respectively, while C is tiled across M and N
    Q_tiles = TensorTiler2D.group_tiler(
        (heads * S_q_pad, d), (number_of_pipelines_join_distribute * B_q, d), (1, 1)
    )

    K_tiles = TensorTiler2D.group_tiler(
        (num_KV_heads * S_kv_pad, d), (S_kv_pad, d), (1, 1)
    )

    V_tiles = TensorTiler2D.group_tiler(
        (num_KV_heads * S_kv_pad, d), (S_kv_pad, d), (1, 1)
    )

    O_tiles = TensorTiler2D.group_tiler(
        (heads * S_q_pad, d), (number_of_pipelines_join_distribute * B_q, d), (1, 1)
    )

    def print_tap_seq_info(tap_seq, name):
        for idx, tap in enumerate(tap_seq):
            print(f"{name} tile {idx}:")
            print(f"  Offset: {tap.offset}")
            print(f"  Sizes: {tap.sizes}")
            print(f"  Strides: {tap.strides}")

    def legalize_tap(tap: TensorAccessPattern, max_dim_size: int):

        sizes = copy.deepcopy(tap._sizes)

        # Skip is no need to legalize
        if all(size <= max_dim_size for size in sizes):
            return tap

        # Check that the transfer is continuous
        for idx, stride in enumerate(tap._strides[:-1]):
            if stride != 0 and stride != tap._sizes[idx + 1]:
                raise ValueError(f"Cannot legalize DMA non-contiguous DMA transfer")
        assert tap._strides[-1] == 1, f"Cannot legalize DMA non-contiguous DMA transfer"

        tap._sizes = [1, 1, 1, math.prod(sizes)]
        tap._strides = [0, 0, 0, 1]

        return tap

    def legalize_tas(tas: TensorAccessSequence):

        max_dim_size = 1023  # Max DMA dimension size for memTile DMA on NPU2

        for tap in tas:
            tap = legalize_tap(tap, max_dim_size)

    legalize_tas(K_tiles)
    legalize_tas(V_tiles)

    if verbose:
        print(f"DMA Transfer Configuration: DRAM <-> Mem tile")
        # print_tap_seq_info(Q_tiles, "Q")
        print_tap_seq_info(K_tiles, "K")
        print_tap_seq_info(V_tiles, "V")
        # print_tap_seq_info(O_tiles, "O")

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(Q_ty, KV_ty, KV_ty, Q_ty) as (Q, K, V, O):

        def set_mha_rtps():
            for j in range(3):
                for i in range(number_of_pipelines):
                    mha_rtps_list[j][i][0] = num_q_block_per_pipeline
                    mha_rtps_list[j][i][1] = num_kv_blocks
                    mha_rtps_list[j][i][2] = S_q_eff
                    mha_rtps_list[j][i][3] = S_kv_eff

        rt.inline_ops(set_mha_rtps, ())

        for j in range(3):
            for i in range(number_of_pipelines):
                rt.set_barrier(worker_barrier_list[j][i], 1)

        for i in range(number_of_pipelines):
            rt.start(matmul_workers[i])
            rt.start(softmax_workers[i])
            rt.start(matmul_pv_workers[i])

        for head_idx in range(heads):

            kv_head_idx = head_idx // (heads // num_KV_heads)

            for q_block_idx in range(num_q_block_per_pipeline):

                # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
                tg = rt.task_group()

                if number_of_pipelines > 6:
                    rt.fill(
                        inQ.prod(),
                        Q,
                        tap=Q_tiles[
                            2 * head_idx * num_q_block_per_pipeline + q_block_idx * 2
                        ],
                        placement=Tile(col=4, row=0),
                        task_group=tg,
                    )
                    rt.fill(
                        inQ2.prod(),
                        Q,
                        tap=Q_tiles[
                            2 * head_idx * num_q_block_per_pipeline
                            + q_block_idx * 2
                            + 1
                        ],
                        placement=Tile(col=4, row=0),
                        task_group=tg,
                    )
                else:
                    rt.fill(
                        inQ.prod(),
                        Q,
                        tap=Q_tiles[head_idx * num_q_block_per_pipeline + q_block_idx],
                        placement=Tile(col=4, row=0),
                        task_group=tg,
                    )

                # Thow on bd containing the full K and V in the object fifo, then does it transfer cunks of inKV size at the time?
                rt.fill(
                    inK.prod(),
                    K,
                    tap=K_tiles[kv_head_idx],
                    placement=Tile(col=5, row=0),
                    task_group=tg,
                )
                rt.fill(
                    inV.prod(),
                    V,
                    tap=V_tiles[kv_head_idx],
                    placement=Tile(col=6, row=0),
                    task_group=tg,
                )

                if number_of_pipelines > 6:
                    rt.drain(
                        memO.cons(),
                        O,
                        tap=O_tiles[
                            2 * head_idx * num_q_block_per_pipeline + q_block_idx * 2
                        ],
                        wait=True,
                        placement=Tile(col=7, row=0),
                        task_group=tg,
                    )
                    rt.drain(
                        memO2.cons(),
                        O,
                        tap=O_tiles[
                            2 * head_idx * num_q_block_per_pipeline
                            + q_block_idx * 2
                            + 1
                        ],
                        wait=True,
                        placement=Tile(col=7, row=0),
                        task_group=tg,
                    )
                else:
                    rt.drain(
                        memO.cons(),
                        O,
                        tap=O_tiles[head_idx * num_q_block_per_pipeline + q_block_idx],
                        wait=True,
                        placement=Tile(col=7, row=0),
                        task_group=tg,
                    )

                rt.finish_task_group(tg)

    # Create the program from the device type and runtime
    dev_ty = NPU2()
    my_program = Program(dev_ty, rt)

    # Place components (assign them resources on the device) and generate an MLIR module
    module = my_program.resolve_program(SequentialPlacer())
    return module
