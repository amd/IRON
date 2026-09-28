# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Fused multi-head attention, in the declared form.

The array is ``num_pipelines`` three-stage pipelines (QK matmul, partial
softmax, PV matmul), one per column, fed by a Q stream split across the
pipelines on a memtile and by K and V streams every pipeline consumes. The
block sizes, the head dimension and the pipeline count configure it; the
sequence length and the head counts do not. The cores loop forever and
read their trip counts from four values the sequence writes.

The host ABI is Q and O as ``(num_heads, seq_pad, d)``, K and V as
``(num_KV_heads, seq_pad, d)`` with the sequence padded to a multiple of
``B_q * num_pipelines``. The sequence is an override: one task group per
KV group that fills Q for every shim, fills that group's K and V, and
drains O.
"""

import dataclasses
import sys

import numpy as np
from aie.dialects.aie import AIEArch
from aie.helpers.dialects.scf import else_, if_
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, ObjectFifo, Worker, ceildiv, kernels
from aie.iron.controlflow import range_
from aie.iron.device import Tile
from aie.iron.kernels.linalg import mm_stream_dims
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import (
    Extent,
    In,
    Operator,
    Out,
    Shim,
    Unresolvable,
    Value,
    auto,
    param,
    select,
)
from iron.common.testing import Case, Testing


class MHA(Operator):
    """AIE-accelerated Multi-Head Attention operator: fused attention over
    ``(B_q, d)`` Q blocks and ``(d, B_kv)`` K/V blocks.

    More than six pipelines split the Q and O traffic over two shims (each
    memtile split serves at most six pipelines), so the Q and O streams have
    ``q_shims`` lanes, each carrying ``join_rows`` rows per block, ``B_q``
    for each of its pipelines.
    """

    # Several kernels and no one contract to judge by: 4% or 0.15, with
    # 0.5% of the outputs allowed past it.
    test = Testing(
        [
            Case(dict(num_heads=1, seq_len=16384, num_pipelines=8)),
            # Grouped-query: 8 query heads over 2 KV heads.
            Case(
                dict(num_heads=8, num_KV_heads=2, seq_len=16384, num_pipelines=8),
                extensive=True,
            ),
            Case(dict(num_heads=1, seq_len=16384, num_pipelines=4), extensive=True),
        ],
        tolerance=Tolerance(rtol=0.04, atol=0.15, max_mismatch_frac=0.005),
    )

    num_heads: int = param()
    # The K/V head count: fewer than num_heads is grouped-query attention;
    # left out, plain MHA.
    num_KV_heads: int = param(default=lambda op: op.num_heads)
    # seq_pad is seq_len rounded up to a multiple of B_q * num_pipelines;
    # a shape gives seq_pad, from which seq_len follows when it is not given.
    seq_len: int = param(default=lambda op: op.seq_pad)
    seq_pad: int = param(default=lambda op: op.seq_padding(op.seq_len), repr=False)
    # The layout a projection GEMM produces, ``(seq, heads, d)`` with the
    # heads interleaved per token, read and written as it is: a head's block
    # is then a strided slice, and no copy reorders the heads to the front.
    heads_interleaved: bool = param(default=False)
    # The head dimension: the width of every tile and the kernel's DIM_K.
    d: int = param(default=64)
    B_q: int = auto(64, array=True)
    B_kv: int = auto(64)
    num_pipelines: int = auto(1, array=True)
    emulate_bf16_mmul_with_bfp16: bool = param(default=True, repr=False)
    # Filled by resolve: how the pipelines are split across shims.
    q_shims: int = auto(repr=False)
    join_rows: int = auto(repr=False)

    Q = In(
        select(heads_interleaved, (seq_pad, num_heads, d), (num_heads, seq_pad, d)),
        tile=(join_rows, d),
        per=(q_shims,),
        via=Shim(4),
    )
    K = In(
        select(
            heads_interleaved, (seq_pad, num_KV_heads, d), (num_KV_heads, seq_pad, d)
        ),
        tile=(d, B_kv),
        via=Shim(5),
    )
    V = In(
        select(
            heads_interleaved, (seq_pad, num_KV_heads, d), (num_KV_heads, seq_pad, d)
        ),
        tile=(d, B_kv),
        via=Shim(6),
    )
    O = Out(  # noqa: E741  (the operand's name)
        select(heads_interleaved, (seq_pad, num_heads, d), (num_heads, seq_pad, d)),
        tile=(join_rows, d),
        per=(q_shims,),
        via=Shim(7),
    )
    # The padded length, or fewer rows per call (``Q[:n]`` in a graph). The
    # DMAs stream every row either way; the cores attend over the blocks the
    # bound covers and pass the rest through, so the quadratic work follows
    # the call.
    valid = Extent(seq_pad)
    # The cores' trip counts, and the unpadded lengths for masking.
    q_blocks_per_pipeline = Value(
        np.int32, derive=lambda op: op.seq_pad // (op.B_q * op.num_pipelines)
    )
    kv_blocks = Value(np.int32, derive=lambda op: op.seq_pad // op.B_kv)
    s_q = Value(np.int32, derive=lambda op: op.valid_tokens)
    s_kv = Value(np.int32, derive=lambda op: op.valid_tokens)
    # Under a bound: the Q blocks per pipeline and the KV blocks per Q block
    # the cores compute; the totals above are what they pass through.
    q_blocks_valid = Value(
        np.int32,
        derive=lambda op: op.seq_padding(op.valid_tokens)
        // (op.B_q * op.num_pipelines),
        optional=True,  # nothing reads it unbounded
    )
    kv_blocks_valid = Value(
        np.int32, derive=lambda op: ceildiv(op.valid_tokens, op.B_kv), optional=True
    )

    @property
    def valid_tokens(self) -> int:
        """The rows attended over: the call's bound, else ``seq_len``."""
        return self.valid if "valid" in self.bound_extents else self.seq_len

    def extent_unit(self, buffer: str) -> int:
        return 0  # nothing is shortened: the cores bound their compute

    # -- checks ----------------------------------------------------------------

    def validate(self) -> None:
        if self.d != 64:
            raise ValueError(f"Only d=64 is supported in this version, got d={self.d}")
        if not self.emulate_bf16_mmul_with_bfp16:
            raise ValueError("Only emulate_bf16_mmul_with_bfp16=True is supported")
        if self.num_pipelines < 1:
            raise ValueError("num_pipelines must be at least 1")
        if self.num_pipelines > 6 and self.num_pipelines % 2:
            raise ValueError(
                f"num_pipelines ({self.num_pipelines}) above 6 must be even: "
                f"the pipelines are split over two shims"
            )
        # Each product's micro-tile must divide its operands: QK^T, (B_q, d)
        # by (d, B_kv), bfp16-emulated, the only one supported, on NPU2, the
        # only array MHA fits; P*V, (B_q, B_kv) by (B_kv, d).
        for pv, dims in ((False, ("B_q", "d", "B_kv")), (True, ("B_q", "B_kv", "d"))):
            mac = kernels.linalg.mha.mac_dims(
                pv=pv, arch="aie2p", emulate_bf16_mmul_with_bfp16=True
            )
            for name, m in zip(dims, mac):
                if getattr(self, name) % m:
                    raise ValueError(
                        f"{name}={getattr(self, name)} must be a multiple of "
                        f"{'P*V' if pv else 'QK^T'}'s micro-tile {mac}"
                    )
        if self.num_heads <= 0:
            raise ValueError("Number of num_heads must be greater than 0")
        if self.num_KV_heads <= 0:
            raise ValueError("Number of KV num_heads must be greater than 0")
        if self.num_KV_heads > self.num_heads:
            raise ValueError(
                "Number of KV num_heads must be less than or equal to number of num_heads"
            )
        if self.num_heads % self.num_KV_heads:
            raise ValueError(
                f"Number of num_heads ({self.num_heads}) must be divisible by "
                f"number of KV num_heads ({self.num_KV_heads})"
            )
        if self.seq_len <= 0:
            raise ValueError("seq_len must be greater than 0")
        self.check_derived("seq_pad")

    def resolve(self, dev):
        if dev is not None and (dev.arch is not AIEArch.AIE2p or dev.cols < 8):
            raise Unresolvable(
                f"MHA is pinned to the 8-column NPU2 array (memtiles at columns "
                f"3-7); got {dev.name} ({dev.arch}) with {dev.cols} columns"
            )
        q_shims = 2 if self.num_pipelines > 6 else 1
        return dataclasses.replace(
            self,
            q_shims=q_shims,
            join_rows=self.B_q * (self.num_pipelines // q_shims),
        )

    # -- derived geometry ------------------------------------------------------

    def seq_padding(self, seq_len: int) -> int:
        """``seq_len`` rounded up to a multiple of ``B_q * num_pipelines``."""
        unit = self.B_q * self.num_pipelines
        return ceildiv(seq_len, unit) * unit

    # -- the array -------------------------------------------------------------

    def array(self, target) -> list:
        of_depth = 2
        dtype = bfloat16
        B_q, B_kv, d = self.B_q, self.B_kv, self.d
        num_pipelines = self.num_pipelines
        n_join = num_pipelines // self.q_shims  # the pipelines on one shim

        inv_scale = (
            1 / np.sqrt(d)
        ) * 1.4453125  # 1.4453125 ≈ log2(e), converts softmax base

        # Tensors living on the AIE-array
        q_ty = np.ndarray[(B_q, d), np.dtype[dtype]]
        k_ty = np.ndarray[(d, B_kv), np.dtype[dtype]]
        qk_ty = np.ndarray[(B_q, B_kv), np.dtype[dtype]]
        s_ty = np.ndarray[(4 * B_q,), np.dtype[dtype]]
        joined_ty = self.Q.tile  # (n_join * B_q, d)

        # Every one of these comes out of mha.cc, which #includes mm.cc and
        # softmax.cc, so they all name one object: matmul_QK is its QK^T
        # product, and the rest of its symbols are bound from that object
        # rather than declared separately, which would recompile the
        # translation unit and redefine every symbol in it.
        matmul_QK = kernels.linalg.mha(
            B_q, d, B_kv, b_col_maj=True, emulate_bf16_mmul_with_bfp16=True
        )
        mha_object = matmul_QK.object_file

        # Upstream's standalone zero over the (DIM_M, DIM_N) tile is the fill.
        zero_kernel = kernels.zero(tile_size=(B_q, B_kv), dtype=dtype)
        # The 16-bit passThroughLine, bound to the bf16 scale buffers.
        memcopy_kernel_scale = kernels.eltwise.passthrough(
            4 * B_q, np.int16
        ).object_file.bind("passThroughLine", [s_ty, s_ty, np.int32])
        scale_buffer_init_kernel = mha_object.bind(
            "init_scale_buffer", [s_ty, np.int32]
        )
        partial_softmax_kernel = mha_object.bind(
            "partial_softmax",
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
        matmul_PV = mha_object.bind(
            "matmul_PV",
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
        rescale_O = mha_object.bind(
            "rescale_O",
            [qk_ty, s_ty, np.int32, np.ndarray[(2,), np.dtype[np.int32]]],
        )

        # AIE-array data movement with object fifos. Q arrives joined for
        # n_join pipelines and is split between them on a memtile; K and V
        # are forwarded through a memtile to every pipeline.
        # Each stream is blocked as the product that reads or writes it takes
        # it: Q, K (as stored) and the scores as QK^T's, V and O as P*V's
        # (matmul_PV, on the micro-tile mha.cc's P*V product expands).
        qk = matmul_QK.stream_dims
        pv = mm_stream_dims(B_q, B_kv, d, kernels.linalg.mha.mac_dims(pv=True))
        q_dims = qk.A
        k_dims = qk.B
        a_dims = qk.C
        v_dims = pv.B
        o_dims = pv.C

        # The Q splits and O joins, one per shim, on memtiles (6, 1) and (7, 1).
        inQ, memQ, memO, outO = [], [], [], []
        for shim in range(self.q_shims):
            suffix = "" if shim == 0 else "2"
            in_q = ObjectFifo(joined_ty, name=f"inQ{suffix}")
            inQ.append(in_q)
            memQ += in_q.cons().split(
                offsets=[B_q * d * i for i in range(n_join)],
                obj_types=[q_ty] * n_join,
                names=[f"memQ{suffix}{i}" for i in range(n_join)],
                dims_to_stream=None if q_dims is None else [q_dims] * n_join,
                depths=[of_depth] * n_join,
                tile=Tile(col=6 + shim, row=1),
            )
            mem_o = ObjectFifo(joined_ty, name=f"memO{suffix}", dims_to_stream=o_dims)
            memO.append(mem_o)
            outO += mem_o.prod().join(
                offsets=[B_q * d * i for i in range(n_join)],
                obj_types=[q_ty] * n_join,
                names=[f"outO{suffix}{i}" for i in range(n_join)],
                depths=[of_depth] * n_join,
                tile=Tile(col=6 + shim, row=1),
            )

        # K is stored in column-major order
        inK = ObjectFifo(k_ty, name="inK", depth=of_depth)
        memK = inK.cons().forward(
            name="memK", dims_to_stream=k_dims, tile=Tile(col=3, row=1), depth=of_depth
        )
        inV = ObjectFifo(k_ty, name="inV", depth=of_depth)
        memV = inV.cons().forward(
            name="memV", dims_to_stream=v_dims, tile=Tile(col=4, row=1), depth=of_depth
        )

        # Per-pipeline fifos between the three stages.
        memA, outA, memP, outP, scaleOF = [], [], [], [], []
        for i in range(num_pipelines):
            memA.append(ObjectFifo(qk_ty, depth=of_depth, name=f"memA{i}"))
            outA.append(
                memA[i]
                .cons()
                .forward(name=f"outA{i}", dims_to_stream=a_dims, depth=of_depth)
            )
            memP.append(ObjectFifo(qk_ty, depth=of_depth, name=f"memP{i}"))
            outP.append(
                memP[i]
                .cons()
                .forward(name=f"outP{i}", dims_to_stream=q_dims, depth=of_depth)
            )
            scaleOF.append(ObjectFifo(s_ty, depth=of_depth, name=f"scaleOF{i}"))

        # Under a bound each core computes the Q blocks and, per Q block,
        # the KV blocks the bound covers, then passes the rest of what the
        # DMAs stream through untouched: the same acquires and releases,
        # no kernel call. The unbounded bodies are as they were.
        bounded = "valid" in self.bound_extents and target.image == "elf"
        words = (
            [
                self.q_blocks_valid.param,
                self.kv_blocks_valid.param,
                self.s_q.param,
                self.s_kv.param,
            ]
            if bounded
            else []
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
            *valid,
        ):
            barrier.wait_for_value(1)
            loop_idx_q = mha_rtps[0]
            loop_idx_kv = mha_rtps[1]
            q_valid = valid[0].read() if bounded else loop_idx_q
            kv_valid = valid[1].read() if bounded else loop_idx_kv

            def kv_block(elem_in_q, compute: bool):
                elem_in_k = of_k.acquire(1)
                elem_a_out = of_a_out.acquire(1)
                if compute:
                    zero(elem_a_out)
                    matmul_QK(elem_in_q, elem_in_k, elem_a_out, idx_buffer)
                of_k.release(1)
                of_a_out.release(1)
                if compute:
                    idx_buffer[0] += 1

            def q_block(compute: bool):
                elem_in_q = of_q.acquire(1)
                for _ in range_(kv_valid if compute else loop_idx_kv):
                    kv_block(elem_in_q, compute)
                if bounded and compute:
                    for _ in range_(loop_idx_kv - kv_valid):
                        kv_block(elem_in_q, False)
                if compute:
                    idx_buffer[0] = 0
                    idx_buffer[1] += num_pipelines
                of_q.release(1)

            for _ in range_(sys.maxsize):
                idx_buffer[0] = 0
                idx_buffer[1] = q_block_bias
                for _ in range_(q_valid):
                    q_block(True)
                if bounded:
                    for _ in range_(loop_idx_q - q_valid):
                        q_block(False)

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
            *valid,
        ):
            # The index buffer counts how many Q and KV blocks this worker has
            # processed; from it the kernel infers its position in A and P.
            barrier.wait_for_value(1)
            loop_idx_q = mha_rtps[0]
            loop_idx_kv = mha_rtps[1]
            S_q_effective = valid[2].read() if bounded else mha_rtps[2]
            S_kv_effective = valid[3].read() if bounded else mha_rtps[3]
            q_valid = valid[0].read() if bounded else loop_idx_q
            kv_valid = valid[1].read() if bounded else loop_idx_kv

            def kv_block(compute: bool):
                elt_of_out_p = of_out_p.acquire(1)
                elt_of_in_a = of_in_a.acquire(1)
                elt_of_out_scale = of_out_scale.acquire(1)
                if compute:
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
                if compute:
                    idx_buffer[0] += 1

            def q_block(compute: bool):
                if compute:
                    init_scale_buffer(scale_buffer, B_q)
                for _ in range_(kv_valid if compute else loop_idx_kv):
                    kv_block(compute)
                if bounded and compute:
                    for _ in range_(loop_idx_kv - kv_valid):
                        kv_block(False)
                if compute:
                    idx_buffer[0] = 0
                    idx_buffer[1] += num_pipelines

            for _ in range_(sys.maxsize):
                # Required, otherwise the buffer is kept across warmup.
                idx_buffer[0] = 0
                idx_buffer[1] = q_block_bias
                for _ in range_(q_valid):
                    q_block(True)
                if bounded:
                    for _ in range_(loop_idx_q - q_valid):
                        q_block(False)

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
            *valid,
        ):
            barrier.wait_for_value(1)
            loop_idx_q = mha_rtps[0]
            loop_idx_kv_total = mha_rtps[1]
            q_valid = valid[0].read() if bounded else loop_idx_q
            loop_idx_kv = valid[1].read() if bounded else loop_idx_kv_total

            def pass_through(n):
                # KV blocks past the bound: consumed, not attended over.
                for _ in range_(n):
                    of_p.acquire(1)
                    of_v.acquire(1)
                    of_scale.acquire(1)
                    of_p.release(1)
                    of_v.release(1)
                    of_scale.release(1)

            for _ in range_(sys.maxsize):
                idx_buffer[0] = 0
                idx_buffer[1] = q_block_bias

                for _ in range_(q_valid):
                    elem_o_out = of_o_out.acquire(1)
                    zero(elem_o_out)

                    # First iteration, don't rescale O_{i-1}
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

                    # Last iteration, final rescaling
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
                    with else_(if_op):
                        rescale_O(elem_o_out, elt_of_out_scale, B_q, idx_buffer)
                        idx_buffer[0] += 1

                    if bounded:
                        pass_through(loop_idx_kv_total - loop_idx_kv)
                    idx_buffer[0] = 0
                    idx_buffer[1] += num_pipelines

                    of_o_out.release(1)

                if bounded:
                    for _ in range_(loop_idx_q - q_valid):
                        of_o_out.acquire(1)  # a padding block of O: left as is
                        pass_through(loop_idx_kv_total)
                        of_o_out.release(1)

        # One runtime-parameter buffer and one barrier per worker, since each
        # is placed with its core. The preamble writes the four residents into
        # every buffer and sets every barrier.
        mha_rtps_list = [
            [
                Buffer(
                    np.ndarray[(4,), np.dtype[np.int32]],
                    name=f"mha_rtpss_{i}_stage{j}",
                    use_write_rtp=True,
                )
                for i in range(num_pipelines)
            ]
            for j in range(3)
        ]
        worker_barrier_list = [
            [target.barrier() for _ in range(num_pipelines)] for _ in range(3)
        ]

        matmul_workers, softmax_workers, matmul_pv_workers = [], [], []
        for i in range(num_pipelines):
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
                    ]
                    + words,
                    stack_size=0xD00,
                    tile=Tile(col=i, row=2),
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
                    ]
                    + words,
                    stack_size=0xD00,
                    tile=Tile(col=i, row=3),
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
                    ]
                    + words,
                    stack_size=0xD00,
                    tile=Tile(col=i, row=4),
                    while_true=False,
                )
            )

        # The shim ends, on the columns the operands' via= pins declare.
        # Every coordinate in this design is load-bearing: relaxed to
        # AnyShimTile/AnyMemTile/AnyComputeTile the router reports "Unable
        # to find a legal routing", so the map here is not a performance
        # preference. Q's slots share column 4's two channels, O's column 7's.
        def shim_of(operand) -> Tile:
            lanes = operand.lanes
            assert lanes is not None and isinstance(lanes.via, Shim)
            return Tile(col=lanes.via.col, row=0)

        for s in range(self.q_shims):
            self.Q.lane(s).bind(inQ[s].prod(tile=shim_of(self.Q)))
            self.O.lane(s).bind(memO[s].cons(tile=shim_of(self.O)))
        self.K.bind(inK.prod(tile=shim_of(self.K)))
        self.V.bind(inV.prod(tile=shim_of(self.V)))

        flat_rtps = [b for stage in mha_rtps_list for b in stage]
        self.q_blocks_per_pipeline.bind(flat_rtps, 0)
        self.kv_blocks.bind(flat_rtps, 1)
        if not bounded:  # else the cores read the lengths per call
            self.s_q.bind(flat_rtps, 2)
            self.s_kv.bind(flat_rtps, 3)

        return matmul_workers + softmax_workers + matmul_pv_workers

    def ops(self) -> int:
        """Q K^T and its product with V, causal: half of each, per head."""
        return 2 * self.num_heads * self.seq_len**2 * self.d

    def reference(self, Q, K, V, s_q=None, s_kv=None):
        """CPU reference: causal attention per head, K and V repeated over each
        query group. Rows past ``seq_len`` (the padding) come out as zeros;
        the real rows never attend to them, causality masks them. In the
        interleaved layout the operands are ``(seq, heads, d)`` and so is O.
        ``s_q``/``s_kv`` are the per-call lengths when a graph binds them.
        """
        # Not the linalg.mha contracts: each is one tile of an online softmax,
        # and the operator is whole attention.
        kv_heads = self.num_KV_heads
        seq_len = self.seq_len if s_q is None else int(s_q)
        keys = int(s_kv) if s_kv is not None else None
        if self.heads_interleaved:
            Q, K, V = (np.swapaxes(t, 0, 1) for t in (Q, K, V))
        groups = self.num_heads // kv_heads
        K = np.repeat(K, groups, axis=0)
        V = np.repeat(V, groups, axis=0)
        # Causal scaled-dot-product attention, in float32 and rounded once.
        # Against torch's FLASH backend this differs by under 1e-6, which is
        # less than torch's own FLASH and MATH backends differ from each other.
        q, k, v = (t.astype(np.float32) for t in (Q, K, V))
        seq = k.shape[1]
        mask = np.triu(np.full((seq, seq), -np.inf, dtype=np.float32), 1)
        if keys is not None and keys < seq:
            mask[:, keys:] = -np.inf  # keys past the call's length
        scale = np.sqrt(np.float32(self.d))
        out = np.empty(Q.shape, dtype=Q.dtype)
        # A head at a time: at 16K rows one head's scores are 1 GiB of
        # float32, and all of them at once more than a test host has.
        for h in range(q.shape[0]):
            scores = q[h] @ k[h].T / scale + mask
            e = np.exp(scores - scores.max(axis=-1, keepdims=True))
            out[h] = (e / e.sum(axis=-1, keepdims=True)) @ v[h]
        out[:, seq_len:] = 0
        if self.heads_interleaved:
            return np.ascontiguousarray(np.swapaxes(out, 0, 1))
        return out

    # -- the runtime sequence --------------------------------------------------

    def sequence(self, rt):
        """One descriptor set per KV group.

        The array consumes, per head and per Q block, the block's Q rows on
        each shim and then all of that head's K and V; O comes back per
        block. Issued as such, that is six descriptors per block, 768 a
        call for 32 heads over 2048 rows on 8 pipelines, and the fused
        sequence's size follows. Instead
        each shim's Q (and O) is one pattern over the group's heads and
        every block, and K and V are one pattern each, the head's rows
        re-read once per (head, block) from the descriptor's iteration
        slot: the same bytes in the same order, six descriptors a group.
        """
        kv_heads, S = self.num_KV_heads, self.seq_pad
        group = self.num_heads // kv_heads
        rows = self.join_rows  # Q rows each shim carries per block
        blocks = S // (rows * self.q_shims)  # per pipeline
        d = self.d

        def strides_of(buffer):
            # (head, row) element strides of a (heads, seq, d) or, interleaved
            # per token, (seq, heads, d) buffer.
            n_heads = buffer.shape[1] if self.heads_interleaved else buffer.shape[0]
            return (d, n_heads * d) if self.heads_interleaved else (S * d, d)

        def q_rows(buffer, head0, shim):
            # The group's heads, each block's `rows` rows for this shim.
            head_s, row_s = strides_of(buffer)
            return TensorAccessPattern(
                buffer.shape,
                head0 * head_s + shim * rows * row_s,
                [group, blocks, rows, d],
                [head_s, self.q_shims * rows * row_s, row_s, 1],
            )

        def kv_rows(buffer, kv_head):
            # The head's rows, re-read once per (head, block) of the group.
            head_s, row_s = strides_of(buffer)
            return TensorAccessPattern(
                buffer.shape, kv_head * head_s, [group * blocks, S, d], [0, row_s, 1]
            )

        for kv_head in range(kv_heads):
            head0 = kv_head * group
            with rt.group():
                for shim in range(self.q_shims):
                    rt.fill(self.Q.lane(shim), q_rows(self.Q, head0, shim))
                rt.fill(self.K, kv_rows(self.K, kv_head))
                rt.fill(self.V, kv_rows(self.V, kv_head))
                for shim in range(self.q_shims):
                    rt.drain(self.O.lane(shim), q_rows(self.O, head0, shim))
