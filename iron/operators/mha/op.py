# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Fused multi-head attention, in the declared form.

:class:`MHAOverlay` is the array: ``num_of_pipelines`` three-stage pipelines
(QK matmul, partial softmax, PV matmul), one per column, fed by a Q stream
split across the pipelines on a memtile and by K and V streams every
pipeline consumes. The block sizes, the head dimension and the pipeline
count configure it; the sequence length and the head counts do not. The
cores loop forever and read their trip counts from four residents the
sequence writes.

:class:`MHA` is the host ABI: Q and O as ``(num_heads, seq_pad, d)``, K and
V as ``(num_KV_heads, seq_pad, d)`` with the sequence padded to a multiple
of ``B_q * num_of_pipelines``. Its sequence is an override: one task group
per (head, Q block) that fills Q for every shim, fills that head's whole K
and V, and drains O.
"""

import dataclasses
from dataclasses import field

import numpy as np
from ml_dtypes import bfloat16

from iron.common.declare import (
    select,
    Incompatible,
    In,
    Operator,
    Out,
    Overlay,
    Resident,
    Shim,
    StreamIn,
    StreamOut,
    Untunable,
    dim,
    operator,
    tunable,
)

_I32x4 = np.ndarray[(4,), np.dtype[np.int32]]  # type: ignore[misc]

# r, s, t: the dimensions of the microkernel MAC instruction. Only the
# bfp16-emulated bf16 path is supported.
MAC_DIMS = (8, 8, 8)


# --------------------------------------------------------------------------
# The overlay: the pipelined attention array.
# --------------------------------------------------------------------------


@operator
class MHAOverlay(Overlay):
    """The array for fused attention over ``(B_q, d)`` Q blocks and ``(d, B_kv)`` K/V blocks.

    More than six pipelines split the Q and O traffic over two shims (each
    memtile split serves at most six pipelines), so the Q and O streams have
    ``q_shims`` slots, each carrying ``join_rows = B_q * pipelines_per_shim``
    rows per block.
    """

    d: int = dim(64)  # head dimension: the width of every tile and the kernel's DIM_K
    B_q: int = tunable(64)
    B_kv: int = tunable(64)
    num_of_pipelines: int = tunable(1)
    emulate_bf16_mmul_with_bfp16: bool = field(default=True, repr=False)
    # Filled by tuning: how the pipelines are split across shims.
    q_shims: int | None = tunable(None, repr=False)
    join_rows: int | None = tunable(None, repr=False)

    q = StreamIn(join_rows, d, per=q_shims, via=Shim(4))
    k = StreamIn(d, B_kv, via=Shim(5))
    v = StreamIn(d, B_kv, via=Shim(6))
    o = StreamOut(join_rows, d, per=q_shims, via=Shim(7))
    q_blocks_per_pipeline = Resident(np.int32)
    kv_blocks = Resident(np.int32)
    s_q = Resident(np.int32)  # the unpadded sequence length, for masking
    s_kv = Resident(np.int32)

    # -- checks ----------------------------------------------------------------

    def validate(self) -> None:
        if self.d != 64:
            raise ValueError(f"Only d=64 is supported in this version, got d={self.d}")
        if not self.emulate_bf16_mmul_with_bfp16:
            raise ValueError("Only emulate_bf16_mmul_with_bfp16=True is supported")
        if self.num_of_pipelines < 1:
            raise ValueError("num_of_pipelines must be at least 1")
        if self.num_of_pipelines > 6 and self.num_of_pipelines % 2:
            raise ValueError(
                f"num_of_pipelines ({self.num_of_pipelines}) above 6 must be even: "
                f"the pipelines are split over two shims"
            )
        r, s, t = MAC_DIMS
        if self.B_q % r:
            raise ValueError(f"B_q must be divisible by r ({self.B_q} % {r} != 0)")
        if self.B_kv % t:
            raise ValueError(f"B_kv must be divisible by t ({self.B_kv} % {t} != 0)")
        if self.d % s:
            raise ValueError(f"d must be divisible by s ({self.d} % {s} != 0)")

    def tuning(self, dev) -> "MHAOverlay":
        if dev is not None and dev.resolve().name != "npu2":
            raise Untunable(
                f"MHA is pinned to the NPU2 array (memtiles at columns 3-7); "
                f"got {dev.resolve().name}"
            )
        q_shims = 2 if self.num_of_pipelines > 6 else 1
        return dataclasses.replace(
            self,
            q_shims=q_shims,
            join_rows=self.B_q * (self.num_of_pipelines // q_shims),
        )

    # -- derived geometry ------------------------------------------------------

    @property
    def pipelines_per_shim(self) -> int:
        return self.num_of_pipelines // (2 if self.num_of_pipelines > 6 else 1)

    def seq_padding(self, seq_len: int) -> int:
        """``seq_len`` rounded up to a multiple of ``B_q * num_of_pipelines``."""
        unit = self.B_q * self.num_of_pipelines
        return ((seq_len + unit - 1) // unit) * unit

    def kernel_flags(self) -> list[str]:
        """The -D set mha.cc and everything it includes compile under."""
        return [
            "-Dbf16_bf16_ONLY",
            f"-DDIM_M={self.B_q}",
            f"-DDIM_K={self.d}",
            f"-DDIM_N={self.B_kv}",
            "-DROUND_CONV_EVEN",
            "-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16",
            "-DB_COL_MAJ",
        ]

    # -- the array -------------------------------------------------------------

    def design(self, target) -> list:
        import sys

        from aie.helpers.dialects.scf import else_, if_
        from aie.iron import Buffer, ObjectFifo, Worker, kernels
        from aie.iron.controlflow import range_
        from aie.iron.device import Tile

        of_depth = 2
        dtype = bfloat16
        B_q, B_kv, d = self.B_q, self.B_kv, self.d
        num_of_pipelines = self.num_of_pipelines
        n_join = self.pipelines_per_shim
        r, s, t = MAC_DIMS

        inv_scale = (
            1 / np.sqrt(d)
        ) * 1.4453125  # 1.4453125 ≈ log2(e), converts softmax base

        # Tensors living on the AIE-array
        q_ty = np.ndarray[(B_q, d), np.dtype[dtype]]
        k_ty = np.ndarray[(d, B_kv), np.dtype[dtype]]
        qk_ty = np.ndarray[(B_q, B_kv), np.dtype[dtype]]
        s_ty = np.ndarray[(4 * B_q,), np.dtype[dtype]]
        joined_ty = self.q.tile  # (n_join * B_q, d)

        # Every one of these comes out of mha.cc, which #includes mm.cc and
        # softmax.cc, so they all name one object: declared separately each would
        # recompile that translation unit and redefine every symbol in it.
        mha_source = target.kernels_dir / "aie2p" / "mha.cc"
        kernel_flags = self.kernel_flags()

        def mha_kernel(name, arg_types):
            return target.kernel(
                name,
                arg_types,
                source=mha_source,
                compile_flags=kernel_flags,
                object_file_name="mha.o",
            )

        # mha.cc used to re-export a zero of its own over the (DIM_M, DIM_N)
        # tile; upstream's standalone zero over the same tile is the same fill.
        zero_kernel = kernels.zero(tile_size=(B_q, B_kv), dtype=dtype)
        memcopy_kernel_scale = target.kernel(
            "passThroughLine",
            [s_ty, s_ty, np.int32],
            source=target.kernels_dir / "generic" / "passThrough.cc",
            compile_flags=["-DBIT_WIDTH=16"],
            object_file_name="mha_passThrough.o",
        )
        scale_buffer_init_kernel = mha_kernel("init_scale_buffer", [s_ty, np.int32])
        partial_softmax_kernel = mha_kernel(
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
        matmul_QK = mha_kernel(
            "matmul_bf16_bf16_wrapper",
            [q_ty, k_ty, qk_ty, np.ndarray[(2,), np.dtype[np.int32]]],
        )
        matmul_PV = mha_kernel(
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
        rescale_O = mha_kernel(
            "rescale_O",
            [qk_ty, s_ty, np.int32, np.ndarray[(2,), np.dtype[np.int32]]],
        )

        # AIE-array data movement with object fifos. Q arrives joined for
        # n_join pipelines and is split between them on a memtile; K and V
        # are forwarded through a memtile to every pipeline.
        q_dims = [(B_q // r, r * d), (d // s, s), (r, d), (s, 1)]
        k_dims = [(B_kv // t, t * d), (d // s, s), (t, d), (s, 1)]
        v_dims = [(B_kv // s, s * B_kv), (B_kv // t, t), (s, B_kv), (t, 1)]
        a_dims = [(B_q // r, r * B_kv), (r, t), (B_kv // t, r * t), (t, 1)]
        o_dims = a_dims

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
                dims_to_stream=[q_dims] * n_join,
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
        for i in range(num_of_pipelines):
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
                    idx_buffer[1] += num_of_pipelines

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
            # The index buffer counts how many Q and KV blocks this worker has
            # processed; from it the kernel infers its position in A and P.
            barrier.wait_for_value(1)
            loop_idx_q = mha_rtps[0]
            loop_idx_kv = mha_rtps[1]
            S_q_effective = mha_rtps[2]
            S_kv_effective = mha_rtps[3]

            for _ in range_(sys.maxsize):
                # Required, otherwise the buffer is kept across warmup.
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
                    idx_buffer[1] += num_of_pipelines

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
                idx_buffer[0] = 0
                idx_buffer[1] = q_block_bias

                for _ in range_(loop_idx_q):
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

                    idx_buffer[0] = 0
                    idx_buffer[1] += num_of_pipelines

                    of_o_out.release(1)

        # One runtime-parameter buffer and one barrier per worker, since each
        # is placed with its core. The preamble writes the four residents into
        # every buffer and sets every barrier.
        mha_rtps_list = [
            [
                target.rtp(_I32x4, name=f"mha_rtpss_{i}_stage{j}")
                for i in range(num_of_pipelines)
            ]
            for j in range(3)
        ]
        worker_barrier_list = [
            [target.barrier() for _ in range(num_of_pipelines)] for _ in range(3)
        ]

        matmul_workers, softmax_workers, matmul_pv_workers = [], [], []
        for i in range(num_of_pipelines):
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
                    ],
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
                    ],
                    stack_size=0xD00,
                    tile=Tile(col=i, row=4),
                    while_true=False,
                )
            )

        # The shim ends. Every coordinate in this design is load-bearing:
        # relaxed to AnyShimTile/AnyMemTile/AnyComputeTile the router reports
        # "Unable to find a legal routing", so the map here is not a
        # performance preference. Q enters on column 4 and O leaves on 7,
        # both slots sharing the tile's two channels; K and V take 5 and 6.
        for shim in range(self.q_shims):
            self.q[shim].bind(inQ[shim].prod(tile=Tile(col=4, row=0)))
            self.o[shim].bind(memO[shim].cons(tile=Tile(col=7, row=0)))
        self.k.bind(inK.prod(tile=Tile(col=5, row=0)))
        self.v.bind(inV.prod(tile=Tile(col=6, row=0)))

        flat_rtps = [b for stage in mha_rtps_list for b in stage]
        self.q_blocks_per_pipeline.bind(flat_rtps, 0)
        self.kv_blocks.bind(flat_rtps, 1)
        self.s_q.bind(flat_rtps, 2)
        self.s_kv.bind(flat_rtps, 3)

        return matmul_workers + softmax_workers + matmul_pv_workers


# --------------------------------------------------------------------------
# The operator: the host ABI, declared against the overlay.
# --------------------------------------------------------------------------


@operator
class MHA(Operator[MHAOverlay]):
    """AIE-accelerated Multi-Head Attention operator"""

    num_heads: int = dim()
    # None takes the padded length inference binds from a shape (seq_pad).
    seq_len: int | None = dim(None)
    # The K/V head count: fewer than num_heads is grouped-query attention.
    # 0 or None means plain MHA (as many as num_heads); validate() fills it.
    num_KV_heads: int | None = dim(None)
    # seq_len rounded up to a multiple of B_q * num_of_pipelines; filled by
    # validate(), and checked against the value inference binds from a shape.
    seq_pad: int | None = dim(None, repr=False)
    # The layout a projection GEMM produces, ``(seq, heads, d)`` with the
    # heads interleaved per token, read and written as it is: a head's block
    # is then a strided slice, and no copy reorders the heads to the front.
    heads_interleaved: bool = field(default=False)

    Q = In(
        select(
            heads_interleaved,
            (seq_pad, num_heads, MHAOverlay.d),
            (num_heads, seq_pad, MHAOverlay.d),
        ),
        to=MHAOverlay.q,
    )
    K = In(
        select(
            heads_interleaved,
            (seq_pad, num_KV_heads, MHAOverlay.d),
            (num_KV_heads, seq_pad, MHAOverlay.d),
        ),
        to=MHAOverlay.k,
    )
    V = In(
        select(
            heads_interleaved,
            (seq_pad, num_KV_heads, MHAOverlay.d),
            (num_KV_heads, seq_pad, MHAOverlay.d),
        ),
        to=MHAOverlay.v,
    )
    O = Out(
        select(
            heads_interleaved,
            (seq_pad, num_heads, MHAOverlay.d),
            (num_heads, seq_pad, MHAOverlay.d),
        ),
        from_=MHAOverlay.o,
    )

    # -- checks ----------------------------------------------------------------

    def validate(self) -> None:
        if self.num_heads <= 0:
            raise ValueError("Number of num_heads must be greater than 0")
        if not self.num_KV_heads:
            self.num_KV_heads = self.num_heads
        if self.num_KV_heads > self.num_heads:
            raise ValueError(
                "Number of KV num_heads must be less than or equal to number of num_heads"
            )
        if self.num_heads % self.num_KV_heads:
            raise ValueError(
                f"Number of num_heads ({self.num_heads}) must be divisible by "
                f"number of KV num_heads ({self.num_KV_heads})"
            )
        if self.seq_len is None:
            if self.seq_pad is None:
                raise ValueError("MHA needs seq_len (or seq_pad, from a shape)")
            self.seq_len = self.seq_pad
        if self.seq_len <= 0:
            raise ValueError("seq_len must be greater than 0")
        expected = self.ov.seq_padding(self.seq_len)
        if self.seq_pad is None:
            self.seq_pad = expected
        elif self.seq_pad != expected:
            raise ValueError(
                f"seq_pad={self.seq_pad} does not match seq_len={self.seq_len} "
                f"padded to a multiple of B_q * num_of_pipelines ({expected})"
            )

    def compatible(self) -> None:
        ov = self.ov
        expected = ov.seq_padding(self.seq_len)
        if self.seq_pad != expected:
            raise Incompatible(
                f"seq_pad ({self.seq_pad}) is not seq_len ({self.seq_len}) padded "
                f"to a multiple of B_q * num_of_pipelines ({expected})"
            )

    def residents(self) -> dict[str, int]:
        ov = self.ov
        return {
            "q_blocks_per_pipeline": self.seq_pad // (ov.B_q * ov.num_of_pipelines),
            "kv_blocks": self.seq_pad // ov.B_kv,
            "s_q": self.seq_len,
            "s_kv": self.seq_len,
        }

    def reference(self, Q, K, V):
        """CPU reference: causal attention per head, K and V repeated over each
        query group. Rows past ``seq_len`` (the padding) come out as zeros;
        the real rows never attend to them, causality masks them. In the
        interleaved layout the operands are ``(seq, heads, d)`` and so is O."""
        if self.heads_interleaved:
            Q, K, V = (np.swapaxes(t, 0, 1) for t in (Q, K, V))
        groups = self.num_heads // self.num_KV_heads
        K = np.repeat(K, groups, axis=0)
        V = np.repeat(V, groups, axis=0)
        # Causal scaled-dot-product attention, in float32 and rounded once.
        # Against torch's FLASH backend this differs by under 1e-6, which is
        # less than torch's own FLASH and MATH backends differ from each other.
        q, k, v = (t.astype(np.float32) for t in (Q, K, V))
        scores = np.matmul(q, np.swapaxes(k, -2, -1)) / np.sqrt(
            np.float32(self.ov.d)
        )
        seq = scores.shape[-1]
        scores += np.triu(np.full((seq, seq), -np.inf, dtype=np.float32), 1)
        e = np.exp(scores - scores.max(axis=-1, keepdims=True))
        O = np.matmul(e / e.sum(axis=-1, keepdims=True), v).astype(Q.dtype)
        if self.seq_len < self.seq_pad:
            O = O.copy()
            O[:, self.seq_len :] = 0
        return np.ascontiguousarray(np.swapaxes(O, 0, 1)) if self.heads_interleaved else O

    # -- the runtime sequence --------------------------------------------------

    def design(self, rt):
        """One descriptor set per KV group.

        The array consumes, per head and per Q block, the block's Q rows on
        each shim and then all of that head's K and V; O comes back per
        block. Issued as such, that is six descriptors per block, 768 a
        call at Llama size, and the fused sequence's size follows. Instead
        each shim's Q (and O) is one pattern over the group's heads and
        every block, and K and V are one pattern each, the head's rows
        re-read once per (head, block) from the descriptor's iteration
        slot: the same bytes in the same order, six descriptors a group.
        """
        from iron.common.tiling import legalize

        ov = self.ov
        heads, kv_heads = self.num_heads, self.num_KV_heads
        group = heads // kv_heads
        rows = ov.join_rows  # Q rows each shim carries per block
        blocks = self.seq_pad // (rows * ov.q_shims)  # per pipeline
        S, d = self.seq_pad, ov.d

        def strides_of(buffer):
            # (head, row) element strides of a (heads, seq, d) or, interleaved
            # per token, (seq, heads, d) buffer.
            n_heads = buffer.shape[1] if self.heads_interleaved else buffer.shape[0]
            return (d, n_heads * d) if self.heads_interleaved else (S * d, d)

        def q_rows(buffer, head0, shim):
            # The group's heads, each block's `rows` rows for this shim.
            head_s, row_s = strides_of(buffer)
            return legalize(
                buffer.elements,
                head0 * head_s + shim * rows * row_s,
                (group, blocks, rows, d),
                (head_s, ov.q_shims * rows * row_s, row_s, 1),
                buffer.dtype,
            )

        def kv_rows(buffer, kv_head):
            # The head's rows, re-read once per (head, block) of the group.
            head_s, row_s = strides_of(buffer)
            return legalize(
                buffer.elements,
                kv_head * head_s,
                (group * blocks, S, d),
                (0, row_s, 1),
                buffer.dtype,
            )

        for kv_head in range(kv_heads):
            head0 = kv_head * group
            with rt.group():
                for shim in range(ov.q_shims):
                    for acc in q_rows(self.Q, head0, shim):
                        rt.fill(ov.q[shim], (self.Q, acc))
                for acc in kv_rows(self.K, kv_head):
                    rt.fill(ov.k, (self.K, acc))
                for acc in kv_rows(self.V, kv_head):
                    rt.fill(ov.v, (self.V, acc))
                for shim in range(ov.q_shims):
                    accs = q_rows(self.O, head0, shim)
                    for acc in accs:
                        rt.drain(ov.o[shim], (self.O, acc), wait=acc is accs[-1])

