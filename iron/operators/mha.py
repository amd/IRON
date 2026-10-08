# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Fused multi-head attention, in the declared form.

The array is ``num_pipelines`` three-stage pipelines (QK matmul, partial
softmax, PV matmul), one per column, fed by a Q stream split across the
pipelines on a memtile and by K and V streams every pipeline consumes. The
block sizes, the head dimension and the pipeline count configure it; the
sequence length and the head counts do not. The cores run one call at a
time, reading their trip counts from seven values the sequence writes.

The host ABI is Q and O as ``(num_heads, seq_pad, d)``, K and V as
``(num_KV_heads, kv_len, d)`` with the sequence padded to a multiple of
``64 * num_pipelines``. The queries are the last rows of the keys: a
prompt's chunk attends over the cache it extends. A query keeps the keys up
to its own position (``causal``), those within ``window`` positions of it,
or both; with neither, every key. The sequence is an
override: one task group per KV group that fills Q for every shim, fills
that group's K and V, and drains O.

One query (``seq_len`` 1, a decode step) is not padded: its heads are
packed. A block's rows are one KV group's query heads, repeated to fill
it, and each pipeline takes its own KV groups, so K and V have a lane per
pipeline rather than one every pipeline reads.
"""

import dataclasses

import numpy as np
from aie.dialects.aie import AIEArch
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    Buffer,
    ObjectFifo,
    TaskGroup,
    Worker,
    WorkerRuntimeBarrier,
    ceildiv,
    kernels,
)
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
    Select,
)
from iron.common.testing import Case, Testing

STACK_SIZE = 0xD00


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
            Case(dict(num_heads=1, seq_len=16384, num_pipelines=8), bench=True),
            # Grouped-query: 8 query heads over 2 KV heads.
            Case(
                dict(num_heads=8, num_KV_heads=2, seq_len=16384, num_pipelines=8),
                extensive=True,
                bench=True,
            ),
            Case(dict(num_heads=1, seq_len=16384, num_pipelines=4), extensive=True),
            # A chunk over a cache: 2048 queries, the last rows of 8192 keys.
            Case(
                dict(
                    num_heads=8,
                    num_KV_heads=2,
                    seq_len=2048,
                    kv_len=8192,
                    num_pipelines=8,
                )
            ),
            # One query over a cache, its heads packed: Llama 3.2 1B's decode.
            Case(
                dict(
                    num_heads=32,
                    num_KV_heads=8,
                    seq_len=1,
                    kv_len=2048,
                    num_pipelines=4,
                    heads_interleaved=True,
                )
            ),
            Case(
                dict(
                    num_heads=8, num_KV_heads=2, seq_len=1, kv_len=512, num_pipelines=2
                ),
                extensive=True,
            ),
            # EmbeddingGemma 2's sliding layer: bidirectional within 512
            # positions, d=256, over 2000 rows, the last block part padding.
            Case(
                dict(
                    num_heads=4,
                    num_KV_heads=2,
                    seq_len=2000,
                    d=256,
                    causal=False,
                    window=512,
                    num_pipelines=8,
                )
            ),
            # Bidirectional over every key.
            Case(
                dict(
                    num_heads=8,
                    num_KV_heads=2,
                    seq_len=1000,
                    causal=False,
                    num_pipelines=8,
                )
            ),
            Case(
                dict(num_heads=8, num_KV_heads=2, seq_len=2048, d=128, num_pipelines=8),
                extensive=True,
            ),
        ],
        tolerance=Tolerance(rtol=0.04, atol=0.15, max_mismatch_frac=0.005),
    )

    num_heads: int = param()
    # The K/V head count: fewer than num_heads is grouped-query attention;
    # left out, plain MHA.
    num_KV_heads: int = param(default=lambda op: op.num_heads)
    # seq_pad is seq_len rounded up to a multiple of 64 * num_pipelines;
    # a shape gives seq_pad, from which seq_len follows when it is not given.
    seq_len: int = param(default=lambda op: op.seq_pad)
    seq_pad: int = param(default=lambda op: op.seq_padding(op.seq_len), repr=False)
    # The rows of K and V: a cache longer than the queries, whose last
    # rows the queries are; left out, as many as Q's.
    kv_len: int = param(default=lambda op: op.seq_pad)
    # The layout a projection GEMM produces, ``(seq, heads, d)`` with the
    # heads interleaved per token, read and written as it is: a head's block
    # is then a strided slice, and no copy reorders the heads to the front.
    # One flag for Q and O, one for K and V, which may come from a cache.
    heads_interleaved: bool = param(default=False)
    kv_interleaved: bool = param(default=False)
    # The head dimension: the width of every tile and the kernel's DIM_K.
    d: int = param(default=64)
    causal: bool = param(default=True, array=True)
    # Keys more than this many positions from a query are masked; None is
    # no window.
    window: int | None = param(default=None, array=True)
    scale: float = param(default=lambda op: float(1 / np.sqrt(op.d)), array=True)
    # Left out, the largest block whose P*V core fits L1 at this d.
    B_q: int = auto(array=True)
    B_kv: int = auto()
    num_pipelines: int = auto(1, array=True)
    emulate_bf16_mmul_with_bfp16: bool = param(default=True, repr=False)
    # Filled by resolve: how the pipelines are split across shims, and K
    # and V's lanes, one every pipeline reads or, one query packed, one each.
    q_shims: int = auto(repr=False)
    join_rows: int = auto(repr=False)
    kv_lanes: int = auto(array=True, repr=False)

    Q = In(
        Select(heads_interleaved, (seq_pad, num_heads, d), (num_heads, seq_pad, d)),
        tile=(join_rows, d),
        per=(q_shims,),
        via=Shim(4),
    )
    K = In(
        Select(kv_interleaved, (kv_len, num_KV_heads, d), (num_KV_heads, kv_len, d)),
        tile=(d, B_kv),
        per=(kv_lanes,),
        via=Shim(5),
    )
    V = In(
        Select(kv_interleaved, (kv_len, num_KV_heads, d), (num_KV_heads, kv_len, d)),
        tile=(B_kv, d),
        per=(kv_lanes,),
        via=Shim(6),
    )
    O = Out(
        Select(heads_interleaved, (seq_pad, num_heads, d), (num_heads, seq_pad, d)),
        tile=(join_rows, d),
        per=(q_shims,),
        via=Shim(7),
    )
    # The query rows, or fewer per call (``Q[:n]`` in a graph): Q and O
    # stream every row; the cores compute the blocks the bound covers and
    # pass the rest through.
    valid = Extent(seq_pad)
    # The keys, or fewer per call (``K[:, :n]``): K and V stream only the
    # blocks the bound covers, so the work follows the context.
    kv_valid = Extent(kv_len)
    # The cores' trip counts, in the order of their runtime-parameter words:
    # the heads, the Q blocks per pipeline of each streamed and computed,
    # the KV blocks per Q block, the unpadded lengths for masking (positions,
    # so the queries' end is the keys'), and the block index of the first
    # query. One query packed, a pipeline's heads are its KV groups, its one
    # block past every key block (no causal skip, no diagonal) and every row
    # of it valid.
    heads = Value(
        np.int32,
        derive=lambda op: (
            op.num_KV_heads // op.num_pipelines if op.packed else op.num_heads
        ),
    )
    q_blocks_per_pipeline = Value(
        np.int32, derive=lambda op: ceildiv(op.seq_pad, op.B_q * op.num_pipelines)
    )
    q_blocks_valid = Value(
        np.int32, derive=lambda op: ceildiv(op.q_tokens, op.B_q * op.num_pipelines)
    )
    kv_blocks = Value(np.int32, derive=lambda op: ceildiv(op.kv_tokens, op.B_kv))
    s_q = Value(
        np.int32,
        derive=lambda op: (
            (op.first_query_block + op.num_pipelines) * op.B_q
            if op.packed
            else op.first_query_block * op.B_q + op.q_tokens
        ),
    )
    s_kv = Value(np.int32, derive=lambda op: op.kv_tokens)
    q_start = Value(np.int32, derive=lambda op: op.first_query_block)

    @property
    def packed(self) -> bool:
        """One query, its heads packed as a block's rows: a KV group's heads,
        repeated to fill the block, a block per group.
        """
        return self.seq_len == 1

    @property
    def q_tokens(self) -> int:
        """The query rows attended from: the call's bound, else ``seq_len``."""
        valid = self.valid  # read first: it makes a derivation per call
        return valid if "valid" in self.bound_extents else self.seq_len

    @property
    def kv_tokens(self) -> int:
        """The keys attended over: the call's bound, else ``kv_len`` less the
        padding Q has past its valid rows.
        """
        kv_valid, q_tokens = self.kv_valid, self.q_tokens  # extents first
        if "kv_valid" in self.bound_extents:
            return kv_valid
        return self.kv_len - self.seq_pad + q_tokens

    @property
    def first_query_block(self) -> int:
        """The position of Q's first row, in blocks: the queries are the
        keys' last rows, and a block's position is what mha.cc masks by.
        One query packed is past every key block: it attends over them all.
        With no band, nothing reads a position, and the queries start at 0.
        """
        if self.packed:
            return ceildiv(self.kv_tokens, self.B_kv)
        if not (self.causal or self.window):
            return 0
        start = self.kv_tokens - self.q_tokens
        if start < 0 or start % self.B_q:
            raise ValueError(
                f"MHA's queries start at key {start}, which is not a whole number "
                f"of {self.B_q}-row blocks into the keys"
            )
        return start // self.B_q

    def extent_unit(self, buffer: str) -> int:
        return 0  # no tiles-per-lane word: the sequence patches K and V itself

    # -- checks ----------------------------------------------------------------

    def validate(self) -> None:
        if self.d <= 0 or self.d % 64:
            raise ValueError(f"d must be a positive multiple of 64, got d={self.d}")
        if self.window is not None and self.window <= 0:
            raise ValueError(f"window must be positive or None, got {self.window}")
        # partial_softmax scales a row's maximum in place of every element.
        if not 0 <= self.scale < np.inf:
            raise ValueError(f"scale must be finite and not negative, got {self.scale}")
        if not self.emulate_bf16_mmul_with_bfp16:
            raise ValueError("Only emulate_bf16_mmul_with_bfp16=True is supported")
        if self.num_pipelines < 1:
            raise ValueError("num_pipelines must be at least 1")
        if self.num_pipelines > 6 and self.num_pipelines % 2:
            raise ValueError(
                f"num_pipelines ({self.num_pipelines}) above 6 must be even: "
                f"the pipelines are split over two shims"
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

    def compatible(self) -> None:
        # mha.cc's causal skip compares a KV block's index with a Q block's.
        if self.B_q != self.B_kv:
            raise ValueError(f"B_q ({self.B_q}) and B_kv ({self.B_kv}) must match")
        if 64 % self.B_q:
            raise ValueError(
                f"B_q ({self.B_q}) must divide 64, the block seq_pad is whole of"
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
        # A row whose window misses a key block another row of its query
        # block keeps would weigh its masked keys 1 (mha.cc).
        if self.window and self.window % self.B_q:
            raise ValueError(
                f"window ({self.window}) must be whole {self.B_q}-row blocks"
            )
        if self.kv_len % self.B_kv or self.kv_len < self.seq_pad:
            raise ValueError(
                f"kv_len ({self.kv_len}) must be whole {self.B_kv}-row blocks and "
                f"at least seq_pad ({self.seq_pad}): the queries are its last rows"
            )
        if self.kv_lanes != (self.num_pipelines if self.packed else 1):
            raise ValueError(
                f"kv_lanes ({self.kv_lanes}) is one per pipeline for one query, "
                f"else one; resolve() sets it"
            )
        if self.packed:
            if self.window:
                raise ValueError(
                    "one query packed sits past every key block, where a "
                    "window would mask them"
                )
            group = self.num_heads // self.num_KV_heads
            if self.B_q % group:
                raise ValueError(
                    f"one query packs a KV group's {group} heads into a block's "
                    f"B_q ({self.B_q}) rows, which they must divide"
                )
            # K and V take both input channels of shims 0 to P-1, and Q shim 4's.
            if self.num_pipelines > 4 or self.num_KV_heads % self.num_pipelines:
                raise ValueError(
                    f"one query takes num_pipelines ({self.num_pipelines}) at most "
                    f"4 dividing num_KV_heads ({self.num_KV_heads}): each pipeline "
                    f"has its own K and V lanes, on its own column's shim"
                )

    def resolve(self, dev):
        if dev is not None and (dev.arch is not AIEArch.AIE2p or dev.cols < 8):
            raise Unresolvable(
                f"MHA is pinned to the 8-column NPU2 array (memtiles at columns "
                f"3-7); got {dev.name} ({dev.arch}) with {dev.cols} columns"
            )
        B_q = self.B_q
        if B_q is None:
            if dev is None:
                raise Unresolvable(
                    "MHA's block size follows the cores' memory; none is bound "
                    "and none was given"
                )
            # The P*V core holds the most: P and V two deep, one bf16 O block,
            # the float32 O, two row-state buffers and its stack.
            B_q = next(
                (
                    b
                    for b in (64, 32, 16)
                    if 4 * b * b + 10 * self.d * b + 32 * b + STACK_SIZE
                    <= dev.core_memory_bytes
                ),
                None,
            )
            if B_q is None:
                raise Unresolvable(
                    f"MHA at d={self.d}: no block of 16 rows or more fits a P*V "
                    f"core's {dev.core_memory_bytes} bytes"
                )
        q_shims = 2 if self.num_pipelines > 6 else 1
        return dataclasses.replace(
            self,
            B_q=B_q,
            B_kv=B_q if self.B_kv is None else self.B_kv,
            q_shims=q_shims,
            join_rows=B_q * (self.num_pipelines // q_shims),
            kv_lanes=self.num_pipelines if self.packed else 1,
        )

    # -- derived geometry ------------------------------------------------------

    def seq_padding(self, seq_len: int) -> int:
        """``seq_len`` rounded up to a multiple of ``64 * num_pipelines``,
        whole blocks at every block size ``resolve`` picks; one query,
        packed, is not padded.
        """
        if seq_len == 1:
            return 1
        unit = 64 * self.num_pipelines
        return ceildiv(seq_len, unit) * unit

    # -- the array -------------------------------------------------------------

    def array(self, target) -> list:
        of_depth = 2
        dtype = bfloat16
        B_q, B_kv, d = self.B_q, self.B_kv, self.d
        num_pipelines = self.num_pipelines
        n_join = num_pipelines // self.q_shims  # the pipelines on one shim

        # partial_softmax takes exp2, so the scale is in the log2 domain.
        inv_scale = float(bfloat16(self.scale * np.log2(np.e)))

        # Tensors living on the AIE-array
        q_ty = np.ndarray[(B_q, d), np.dtype[dtype]]
        k_ty = np.ndarray[(d, B_kv), np.dtype[dtype]]
        v_ty = np.ndarray[(B_kv, d), np.dtype[dtype]]
        qk_ty = np.ndarray[(B_q, B_kv), np.dtype[dtype]]
        s_ty = np.ndarray[(4 * B_q,), np.dtype[np.float32]]
        acc_ty = np.ndarray[(B_q, d), np.dtype[np.float32]]
        joined_ty = self.Q.tile  # (n_join * B_q, d)

        # Every one of these comes out of mha.cc, which #includes mm.cc and
        # softmax.cc, so they all name one object: matmul_QK is its QK^T
        # product, and the rest of its symbols are bound from that object
        # rather than declared separately, which would recompile the
        # translation unit and redefine every symbol in it.
        matmul_QK = kernels.linalg.mha(
            B_q,
            d,
            B_kv,
            b_col_maj=True,
            emulate_bf16_mmul_with_bfp16=True,
            causal=self.causal,
            window=self.window or 0,
        )
        mha_object = matmul_QK.object_file

        # Upstream's standalone zero over the (DIM_M, DIM_N) tile is the fill.
        zero_kernel = kernels.zero(tile_size=(B_q, B_kv), dtype=dtype)
        # The 32-bit passThroughLine, bound to the float32 scale buffers.
        memcopy_kernel_scale = kernels.eltwise.passthrough(
            4 * B_q, np.int32
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
                v_ty,
                acc_ty,
                s_ty,
                np.int32,
                np.int32,
                np.ndarray[(2,), np.dtype[np.int32]],
                np.int32,
            ],
        )
        rescale_O = mha_object.bind(
            "rescale_O",
            [acc_ty, q_ty, s_ty, np.int32, np.ndarray[(2,), np.dtype[np.int32]]],
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
        p_dims = pv.A
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
                to_stream=None if q_dims is None else [q_dims] * n_join,
                depths=[of_depth] * n_join,
                tile=Tile(col=6 + shim, row=1),
            )
            mem_o = ObjectFifo(joined_ty, name=f"memO{suffix}", to_stream=o_dims)
            memO.append(mem_o)
            outO += mem_o.prod().join(
                offsets=[B_q * d * i for i in range(n_join)],
                obj_types=[q_ty] * n_join,
                names=[f"outO{suffix}{i}" for i in range(n_join)],
                # One O block: the PV core's L1 also holds its float32 O.
                depths=[1] * n_join,
                tile=Tile(col=6 + shim, row=1),
            )

        # K (stored column-major) and V are forwarded through a memtile: one
        # stream each that every pipeline reads, through memtiles (3, 1) and
        # (4, 1), or a lane per pipeline through its own column's.
        kv_lanes = self.kv_lanes
        inK, inV, memK, memV = [], [], [], []
        for lane in range(kv_lanes):
            suffix = "" if lane == 0 else str(lane)
            shared = kv_lanes == 1
            inK.append(ObjectFifo(k_ty, name=f"inK{suffix}", depth=of_depth))
            memK.append(
                inK[lane]
                .cons()
                .forward(
                    name=f"memK{suffix}",
                    to_stream=k_dims,
                    tile=Tile(col=3 if shared else lane, row=1),
                    depth=of_depth,
                )
            )
            inV.append(ObjectFifo(v_ty, name=f"inV{suffix}", depth=of_depth))
            memV.append(
                inV[lane]
                .cons()
                .forward(
                    name=f"memV{suffix}",
                    to_stream=v_dims,
                    tile=Tile(col=4 if shared else lane, row=1),
                    depth=of_depth,
                )
            )

        # Per-pipeline fifos between the three stages.
        memA, outA, memP, outP, scaleOF = [], [], [], [], []
        for i in range(num_pipelines):
            memA.append(ObjectFifo(qk_ty, depth=of_depth, name=f"memA{i}"))
            outA.append(
                memA[i]
                .cons()
                .forward(name=f"outA{i}", to_stream=a_dims, depth=of_depth)
            )
            memP.append(ObjectFifo(qk_ty, depth=of_depth, name=f"memP{i}"))
            outP.append(
                memP[i]
                .cons()
                .forward(name=f"outP{i}", to_stream=p_dims, depth=of_depth)
            )
            scaleOF.append(ObjectFifo(s_ty, depth=of_depth, name=f"scaleOF{i}"))

        # Each core computes, per head, the Q blocks the call's rows cover,
        # over the KV blocks its keys cover, and passes the Q blocks past
        # them through: the same acquires and releases, no kernel call, since
        # Q and O stream every block. Its counts are the seven values below;
        # a count the call sets is read from its scratchpad word on a full
        # ELF, and else written into the core's runtime-parameter buffer.
        # A worker's body is one call: it waits for the sequence to write
        # the counts, reads them, and re-arms the barrier, which a wait does
        # not consume; an xclbin's cores outlive the call, and would else
        # start the next on these counts. The sequence cannot set it again
        # before this call's O drains.
        counts = (
            "heads",
            "q_blocks_per_pipeline",
            "q_blocks_valid",
            "kv_blocks",
            "s_q",
            "s_kv",
            "q_start",
        )
        per_call = [n for n in counts if target.image == "elf" and self.uses_value(n)]
        params = [getattr(self, n).param for n in per_call]

        def read(rtps, words):
            return [
                words[per_call.index(n)].read() if n in per_call else rtps[i]
                for i, n in enumerate(counts)
            ]

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
            *words,
        ):
            def q_block(compute: bool, kv_blocks):
                elem_in_q = of_q.acquire(1)
                for _ in range_(kv_blocks):
                    elem_in_k = of_k.acquire(1)
                    elem_a_out = of_a_out.acquire(1)
                    if compute:
                        zero(elem_a_out)
                        matmul_QK(elem_in_q, elem_in_k, elem_a_out, idx_buffer)
                    of_k.release(1)
                    of_a_out.release(1)
                    if compute:
                        idx_buffer[0] += 1
                if compute:
                    idx_buffer[0] = 0
                    idx_buffer[1] += num_pipelines
                of_q.release(1)

            barrier.wait_for_value(1)
            heads, q_blocks, q_valid, kv_blocks, _, _, q_start = read(mha_rtps, words)
            barrier.release_with_value(1)
            for _ in range_(heads):
                idx_buffer[0] = 0
                idx_buffer[1] = q_start + q_block_bias
                for _ in range_(q_valid):
                    q_block(True, kv_blocks)
                for _ in range_(q_blocks - q_valid):
                    q_block(False, kv_blocks)

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
            *words,
        ):
            # The index buffer counts how many Q and KV blocks this worker has
            # processed; from it the kernel infers its position in A and P.
            def q_block(compute: bool, kv_blocks, s_q, s_kv):
                if compute:
                    init_scale_buffer(scale_buffer, B_q)
                for _ in range_(kv_blocks):
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
                            s_q,
                            s_kv,
                        )
                        memcopy_kernel_scale(scale_buffer, elt_of_out_scale, 4 * B_q)
                    of_in_a.release(1)
                    of_out_p.release(1)
                    of_out_scale.release(1)
                    if compute:
                        idx_buffer[0] += 1
                if compute:
                    idx_buffer[0] = 0
                    idx_buffer[1] += num_pipelines

            barrier.wait_for_value(1)
            heads, q_blocks, q_valid, kv_blocks, s_q, s_kv, q_start = read(
                mha_rtps, words
            )
            barrier.release_with_value(1)
            for _ in range_(heads):
                idx_buffer[0] = 0
                idx_buffer[1] = q_start + q_block_bias
                for _ in range_(q_valid):
                    q_block(True, kv_blocks, s_q, s_kv)
                for _ in range_(q_blocks - q_valid):
                    q_block(False, kv_blocks, s_q, s_kv)

        def batched_matmul_pv(
            of_p,
            of_v,
            of_scale,
            of_o_out,
            matmul_PV,
            rescale_O,
            q_block_bias,
            mha_rtps,
            barrier,
            idx_buffer,
            acc,
            *words,
        ):
            barrier.wait_for_value(1)
            heads, q_blocks, q_valid, loop_idx_kv, _, s_kv, q_start = read(
                mha_rtps, words
            )
            barrier.release_with_value(1)
            for _ in range_(heads):
                idx_buffer[0] = 0
                idx_buffer[1] = q_start + q_block_bias

                for _ in range_(q_valid):
                    # matmul_PV starts the accumulator on the KV block it is
                    # told is block 0.
                    for kv in range_(loop_idx_kv - 1):
                        elem_in_p = of_p.acquire(1)
                        elem_in_v = of_v.acquire(1)
                        elt_of_out_scale = of_scale.acquire(1)
                        matmul_PV(
                            elem_in_p,
                            elem_in_v,
                            acc,
                            elt_of_out_scale,
                            B_q,
                            kv,
                            idx_buffer,
                            s_kv,
                        )
                        of_p.release(1)
                        of_v.release(1)
                        of_scale.release(1)
                        idx_buffer[0] += 1

                    # The last block's scale holds the row sums rescale_O reads.
                    elem_in_p = of_p.acquire(1)
                    elem_in_v = of_v.acquire(1)
                    elt_of_out_scale = of_scale.acquire(1)
                    matmul_PV(
                        elem_in_p,
                        elem_in_v,
                        acc,
                        elt_of_out_scale,
                        B_q,
                        loop_idx_kv - 1,
                        idx_buffer,
                        s_kv,
                    )
                    of_p.release(1)
                    of_v.release(1)
                    elem_o_out = of_o_out.acquire(1)
                    rescale_O(acc, elem_o_out, elt_of_out_scale, B_q, idx_buffer)
                    of_scale.release(1)
                    of_o_out.release(1)

                    idx_buffer[0] = 0
                    idx_buffer[1] += num_pipelines

                for _ in range_(q_blocks - q_valid):
                    of_o_out.acquire(1)  # a padding block of O: left as is
                    for _ in range_(loop_idx_kv):
                        of_p.acquire(1)
                        of_v.acquire(1)
                        of_scale.acquire(1)
                        of_p.release(1)
                        of_v.release(1)
                        of_scale.release(1)
                    of_o_out.release(1)

        # One runtime-parameter buffer and one barrier per worker, since each
        # is placed with its core. The preamble writes the counts no call sets
        # into every buffer and sets every barrier.
        mha_rtps_list = [
            [
                Buffer(
                    np.ndarray[(len(counts),), np.dtype[np.int32]],
                    name=f"mha_rtpss_{i}_stage{j}",
                    use_write_rtp=True,
                )
                for i in range(num_pipelines)
            ]
            for j in range(3)
        ]
        worker_barrier_list = [
            [WorkerRuntimeBarrier() for _ in range(num_pipelines)] for _ in range(3)
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
                        memK[i % kv_lanes].cons(),
                        memA[i].prod(),
                        zero_kernel,
                        matmul_QK,
                        i,
                        mha_rtps_list[0][i],
                        worker_barrier_list[0][i],
                        idx_buffer_qk,
                    ]
                    + params,
                    stack_size=STACK_SIZE,
                    tile=Tile(col=i, row=2),
                )
            )
            idx_buffer_softmax = Buffer(
                initial_value=np.zeros(shape=(2,), dtype=np.int32),
                name=f"idx_buffer_softmax_{i}",
            )
            scale_buffer_softmax = Buffer(
                initial_value=np.zeros(shape=(4 * B_q,), dtype=np.float32),
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
                    + params,
                    stack_size=STACK_SIZE,
                    tile=Tile(col=i, row=3),
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
                        memV[i % kv_lanes].cons(),
                        scaleOF[i].cons(),
                        outO[i].prod(),
                        matmul_PV,
                        rescale_O,
                        i,
                        mha_rtps_list[2][i],
                        worker_barrier_list[2][i],
                        idx_buffer_pv,
                        Buffer(acc_ty, name=f"acc_pv_{i}"),
                    ]
                    + params,
                    stack_size=STACK_SIZE,
                    tile=Tile(col=i, row=4),
                )
            )

        # The shim ends, on the columns the operands' via= pins declare.
        # Every coordinate in this design is load-bearing: relaxed to
        # AnyShimTile/AnyMemTile/AnyComputeTile the router reports "Unable
        # to find a legal routing", so the map here is not a performance
        # preference. Q's slots share column 4's two channels, O's column 7's;
        # K and V's lanes, one per pipeline, its column's two.
        def shim_of(operand, lane=0) -> Tile:
            via = operand.member.via
            assert isinstance(via, Shim)
            return Tile(col=via.col if operand.count == 1 else lane, row=0)

        for s in range(self.q_shims):
            self.Q.lane(s).bind(inQ[s].prod(tile=shim_of(self.Q)))
            self.O.lane(s).bind(memO[s].cons(tile=shim_of(self.O)))
        for lane in range(kv_lanes):
            self.K.lane(lane).bind(inK[lane].prod(tile=shim_of(self.K, lane)))
            self.V.lane(lane).bind(inV[lane].prod(tile=shim_of(self.V, lane)))

        flat_rtps = [b for stage in mha_rtps_list for b in stage]
        for i, name in enumerate(counts):
            if name not in per_call:
                getattr(self, name).bind(flat_rtps, i)

        workers = matmul_workers + softmax_workers + matmul_pv_workers
        return workers + [b for stage in worker_barrier_list for b in stage]

    def ops(self) -> int:
        """Q K^T and its product with V per head, over the keys each query
        keeps: the queries are the last ``seq_len`` of ``kv_len - seq_pad +
        seq_len`` keys.
        """
        keys = self.kv_len - self.seq_pad + self.seq_len
        position = keys - self.seq_len + np.arange(self.seq_len)
        ahead = 0 if self.causal else (self.window or keys)
        lo = np.maximum(position - self.window, 0) if self.window else 0
        hi = np.minimum(position + ahead, keys - 1)
        return 4 * self.num_heads * self.d * int((hi - lo + 1).sum())

    def reference(self, Q, K, V, s_q=None, s_kv=None):
        """CPU reference: attention per head, K and V repeated over each query
        group, the queries the keys' last rows: query row ``r`` is at position
        ``len(K) - len(Q) + r`` and keeps the keys up to it if ``causal`` and
        within ``window`` of it if given. ``s_q`` and ``s_kv`` are positions,
        the per-call lengths when a graph binds them: query rows from ``s_q``
        on (by default Q's padding past ``seq_len``) come out as zeros, and
        keys from ``s_kv`` on (by default the keys past the last query) are
        masked. With no band, nothing reads a position and the queries start
        at 0, so ``s_q`` is a row count. In an interleaved layout the operands
        are ``(seq, heads, d)``.
        """
        # Not the linalg.mha contracts: each is one tile of an online softmax,
        # and the operator is whole attention.
        if self.heads_interleaved:
            Q = np.swapaxes(Q, 0, 1)
        if self.kv_interleaved:
            K, V = (np.swapaxes(t, 0, 1) for t in (K, V))
        groups = self.num_heads // self.num_KV_heads
        offset = K.shape[1] - Q.shape[1]
        start = offset if self.causal or self.window else 0
        s_q = start + self.seq_len if s_q is None else int(s_q)
        s_kv = offset + self.seq_len if s_kv is None else int(s_kv)
        # Keys from s_kv on are masked, so a cache is widened only as far as
        # it is read.
        K, V = K[:, :s_kv], V[:, :s_kv]
        # Scaled-dot-product attention, in float32 and rounded once.
        # Against torch's FLASH backend this differs by under 1e-6, which is
        # less than torch's own FLASH and MATH backends differ from each other.
        # The rows from s_q on are zeros; a window may keep none of their keys.
        rows = max(s_q - start, 0)
        q = Q[:, :rows].astype(np.float32)
        k, v = (t.astype(np.float32) for t in (K, V))
        position = offset + np.arange(q.shape[1])[:, None]
        key = np.arange(k.shape[1])
        masked = np.zeros((q.shape[1], k.shape[1]), dtype=bool)
        if self.causal or self.window:
            masked |= key > position + (0 if self.causal else self.window)
        if self.window:
            masked |= key < position - self.window
        mask = np.where(masked, -np.inf, 0).astype(np.float32)
        scale = np.float32(self.scale)
        out = np.zeros(Q.shape, dtype=Q.dtype)
        # A head at a time: at 16K rows one head's scores are 1 GiB of
        # float32, and all of them at once more than a test host has.
        # Each K and V head serves ``groups`` consecutive query heads.
        for h in range(q.shape[0]):
            scores = q[h] @ k[h // groups].T * scale + mask
            e = np.exp(scores - scores.max(axis=-1, keepdims=True))
            out[h, :rows] = (e / e.sum(axis=-1, keepdims=True)) @ v[h // groups]
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

        One query packed is a task group per step, each pipeline's block
        that step one of its KV groups: the group's heads repeated from the
        iteration slot at stride 0 into Q, and drained from O the same way,
        the same rows written over themselves.
        """
        kv_heads = self.num_KV_heads
        group = self.num_heads // kv_heads
        rows = self.join_rows  # Q rows each shim carries per block
        blocks = ceildiv(self.seq_pad, rows * self.q_shims)  # per pipeline
        B_kv = self.B_kv
        # K and V stream the blocks the keys cover, a call's by its bound.
        kv_blocks = ceildiv(self.kv_tokens, B_kv)
        kv_by = {1: self.value("kv_blocks")} if self.uses_value("kv_blocks") else None

        def by_head(buffer, interleaved):
            # A (heads, seq, d) or, interleaved per token, (seq, heads, d)
            # buffer, walked as (head, row, d).
            tap = TensorAccessPattern.full(buffer.shape)
            return tap.permute((1, 0, 2)) if interleaved else tap

        def q_rows(buffer, head0, shim):
            # The group's heads, each block's `rows` rows for this shim.
            heads = by_head(buffer, self.heads_interleaved)[head0 : head0 + group]
            by_shim = heads.split(1, self.q_shims * rows)
            return by_shim[:, :, shim * rows : (shim + 1) * rows]

        def kv_rows(buffer, kv_head, reads):
            # The head's blocks, read `reads` times; a call patches their count.
            head = by_head(buffer, self.kv_interleaved)[kv_head, : kv_blocks * B_kv]
            return head.split(0, B_kv).repeat(reads)

        if self.packed:
            steps = kv_heads // self.num_pipelines

            def packed_rows(buffer, kv_head):
                # The group's heads, contiguous in (1, heads, d) as in
                # (heads, 1, d), repeated to fill a block.
                heads = by_head(buffer, self.heads_interleaved)
                heads = heads[kv_head * group : (kv_head + 1) * group, 0]
                return heads.coalesce().repeat(self.B_q // group)

            for step in range(steps):
                owned = [p * steps + step for p in range(self.num_pipelines)]
                tg = TaskGroup()
                for kv_head in owned:
                    rt.fill(self.Q.lane(0), packed_rows(self.Q, kv_head), group=tg)
                for p, kv_head in enumerate(owned):
                    for x in (self.K, self.V):
                        rt.fill(
                            x.lane(p), kv_rows(x, kv_head, 1), group=tg, size_by=kv_by
                        )
                for kv_head in owned:
                    rt.drain(self.O.lane(0), packed_rows(self.O, kv_head), group=tg)
                tg.finish()
            return

        for kv_head in range(kv_heads):
            head0 = kv_head * group
            tg = TaskGroup()
            for shim in range(self.q_shims):
                rt.fill(self.Q.lane(shim), q_rows(self.Q, head0, shim), group=tg)
            for x in (self.K, self.V):
                rt.fill(x, kv_rows(x, kv_head, group * blocks), group=tg, size_by=kv_by)
            for shim in range(self.q_shims):
                rt.drain(self.O.lane(shim), q_rows(self.O, head0, shim), group=tg)
            tg.finish()
