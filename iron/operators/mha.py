# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Fused multi-head attention.

``num_pipelines`` three-stage pipelines (QK^T, partial softmax, P*V), one
per column: Q split across them on a memtile, K and V forwarded to every
one. Where a core holds no P*V block (d=512), P*V splits over two cores by
halves of the head. The queries are the keys' last rows, padded to 64; one
query (a decode step) is not padded but packs a KV group's heads into a
block, and each pipeline takes its own K and V lanes.
"""

import dataclasses
from typing import ClassVar

import numpy as np
from aie.dialects.aie import AIEArch
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    Buffer,
    ObjectFifo,
    TaskGroup,
    Worker,
    ceildiv,
    kernels,
)
from aie.iron.controlflow import range_
from aie.iron.device import AnyComputeTile, AnyMemTile, AnyShimTile, Device, Tile
from aie.iron.kernels.linalg import mm_stream_dims
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import (
    Divisors,
    Extent,
    In,
    Operator,
    Out,
    Unresolvable,
    Value,
    Width,
    Auto,
    Param,
    Select,
    Built,
    Operand,
    Rtp,
)
from iron.common.testing import Case, Testing

STACK_SIZE = 0xD00
# The softmax core's accurate exp2 polynomial needs 4 KiB, as aiecc measures it.
SOFTMAX_STACK_SIZE = 0x1000


@dataclasses.dataclass(frozen=True)
class Columns:
    """Where MHA's streams meet the array on one array width.

    Attributes:
        q: Q's shim column.
        k: K's shim column, when every pipeline reads one K stream.
        v: V's shim column, likewise.
        o: O's shim column.
        qo_mem: The memtile column of the Q split and the O join, the
            second shim's the next one.
        k_mem: K's memtile column, when every pipeline reads one K stream.
        v_mem: V's memtile column, likewise.
    """

    q: int
    k: int
    v: int
    o: int
    qo_mem: int
    k_mem: int
    v_mem: int


@dataclasses.dataclass(frozen=True)
class SplitColumns:
    """Where MHA's streams meet the array with P*V split over two cores.

    Each column then carries every stream its links hold, so these columns
    are the only ones the router finds.

    Attributes:
        q: Each Q shim's split.
        o: Each Q shim's O joins, one per half of the head.
        k: K's memtile.
        k_shim: K's shim.
        v: V's, one per half of the head.
    """

    q: tuple[int, ...]
    o: tuple[tuple[int, ...], ...]
    k: int
    k_shim: int
    v: tuple[int, ...]


# Whole in seq_pad's 64-row unit, up to the largest whose cores fit L1.
BLOCK_SIZES = Divisors(
    of=lambda op, dev: op.kv_len,
    step=16,
    cap=lambda op, dev: max(
        (
            b
            for b in (16, 32, 64)
            if op.core_bytes(b, op.key_block(b, dev.core_memory_bytes), op.pv_cores)
            <= dev.core_memory_bytes
        ),
        default=16,
    ),
)


# At NPU2's eight pipelines; _cases halves them on a narrower array.
_CASES = [
    Case(dict(num_heads=1, seq_len=16384, num_pipelines=8), bench=True),
    # Grouped-query: 8 query heads over 2 KV heads.
    Case(
        dict(num_heads=8, num_KV_heads=2, seq_len=16384, num_pipelines=8),
        extensive=True,
        bench=True,
    ),
    # A chunk over a cache: 2048 queries, the last rows of 8192 keys.
    Case(
        dict(
            num_heads=8,
            num_KV_heads=2,
            seq_len=2048,
            kv_len=8192,
            num_pipelines=8,
        ),
        lower=True,
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
        ),
        lower=True,
    ),
    # Groups that do not divide a block: Granite 4.2-3B's and Llama 3.2 3B's.
    *(
        Case(
            dict(
                num_heads=heads,
                num_KV_heads=8,
                d=d,
                seq_len=1,
                kv_len=2048,
                num_pipelines=4,
                heads_interleaved=True,
            ),
            lower=True,
        )
        for heads, d in ((40, 64), (24, 128))
    ),
    Case(
        dict(num_heads=8, num_KV_heads=2, seq_len=1, kv_len=512, num_pipelines=2),
        extensive=True,
    ),
    # EmbeddingGemma 2's sliding layer.
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
    # Its global layer: P*V split over two cores.
    Case(
        dict(
            num_heads=4,
            num_KV_heads=1,
            seq_len=2000,
            d=512,
            causal=False,
            num_pipelines=8,
        ),
        lower=True,
    ),
    Case(
        dict(num_heads=8, num_KV_heads=2, seq_len=2048, d=128, num_pipelines=8),
        extensive=True,
    ),
]


def _cases(cls, dev: Device):
    share = 1 if dev.cols >= max(cls.COLUMNS) else 2
    return [
        dataclasses.replace(
            c, kwargs={**c.kwargs, "num_pipelines": c.kwargs["num_pipelines"] // share}
        )
        for c in _CASES
    ]


class MHA(Operator):
    """AIE-accelerated Multi-Head Attention: fused attention over ``(B_q, d)``
    Q blocks, ``(d, B_kv)`` K blocks and ``(B_kv, d)`` V blocks.

    More than six pipelines split Q and O over two shims (a memtile split
    serves at most six).
    """

    test = Testing(_cases)

    num_heads: int = Param()
    num_KV_heads: int = Param(derive=lambda op: op.num_heads)
    seq_len: int = Param(derive=lambda op: op.seq_pad)
    seq_pad: int = Param(derive=lambda op: op.seq_padding(op.seq_len), repr=False)
    # A cache longer than the queries, whose last rows the queries are.
    kv_len: int = Param(derive=lambda op: op.seq_pad)
    # ``(seq, heads, d)`` as a projection writes it, so no copy reorders the heads.
    heads_interleaved: bool = Param(default=False)
    kv_interleaved: bool = Param(default=False)
    d: int = Param(default=64)
    causal: bool = Param(default=True)
    # Keys more than this many positions from a query are masked.
    window: int | None = Param(default=None)
    scale: float = Param(derive=lambda op: float(1 / np.sqrt(op.d)))
    B_q: int = Auto(domain=BLOCK_SIZES)
    B_kv: int = Auto(repr=False, derived=True)
    num_pipelines: int = Auto(default=1, domain=Width())
    # Filled by resolve.
    q_shims: int = Auto(repr=False, derived=True)
    join_rows: int = Auto(repr=False, derived=True)
    kv_lanes: int = Auto(repr=False, derived=True)
    width: int = Auto(repr=False, derived=True)
    # Two P*V cores, by halves of the head, where one's L1 holds no block.
    pv_cores: int = Auto(repr=False, domain=(1, 2))
    pv_width: int = Auto(repr=False, derived=True)

    # One query packed puts pipeline p's K and V on column p: pipelines stop short of q.
    COLUMNS: ClassVar[dict[int, Columns]] = {
        8: Columns(q=4, k=5, v=6, o=7, qo_mem=6, k_mem=3, v_mem=4),
        4: Columns(q=2, k=0, v=1, o=3, qo_mem=2, k_mem=0, v_mem=1),
    }
    SPLIT_COLUMNS: ClassVar[dict[int, SplitColumns]] = {
        8: SplitColumns(q=(1, 6), o=((0, 2), (5, 7)), k=3, k_shim=3, v=(3, 4)),
        4: SplitColumns(q=(0,), o=((1, 2),), k=3, k_shim=0, v=(3, 3)),
    }

    Q = In(
        Select(heads_interleaved, (seq_pad, num_heads, d), (num_heads, seq_pad, d)),
        obj_type=(join_rows, d),
        per=(q_shims,),
    )
    K = In(
        Select(kv_interleaved, (kv_len, num_KV_heads, d), (num_KV_heads, kv_len, d)),
        obj_type=(d, B_kv),
        per=(kv_lanes,),
    )
    V = In(
        Select(kv_interleaved, (kv_len, num_KV_heads, d), (num_KV_heads, kv_len, d)),
        obj_type=(B_kv, pv_width),
        per=(kv_lanes, pv_cores),
    )
    O = Out(
        Select(heads_interleaved, (seq_pad, num_heads, d), (num_heads, seq_pad, d)),
        obj_type=(join_rows, pv_width),
        per=(q_shims, pv_cores),
    )
    # A bound on the queries limits the compute; Q and O stream every row.
    valid = Extent(seq_pad)
    # A bound on the keys limits K's and V's blocks: the work follows the context.
    kv_valid = Extent(kv_len)
    # One query packed sits past every key block: no causal skip, no diagonal.
    heads = Value(
        derive=lambda op: (
            op.num_KV_heads // op.num_pipelines if op.packed else op.num_heads
        ),
    )
    q_blocks_per_pipeline = Value(
        derive=lambda op: ceildiv(op.seq_pad, op.B_q * op.num_pipelines)
    )
    q_blocks_valid = Value(
        derive=lambda op: ceildiv(op.q_tokens, op.B_q * op.num_pipelines)
    )
    kv_blocks = Value(derive=lambda op: ceildiv(op.kv_tokens, op.B_kv))
    s_q = Value(
        derive=lambda op: (
            (op.first_query_block + op.num_pipelines) * op.B_q
            if op.packed
            else op.first_query_block * op.B_q + op.q_tokens
        ),
    )
    s_kv = Value(derive=lambda op: op.kv_tokens)
    q_start = Value(derive=lambda op: op.first_query_block)

    @property
    def packed(self) -> bool:
        """One query, a KV group's heads packed as a block's rows."""
        return self.seq_len == 1

    @property
    def q_tokens(self) -> int:
        """The query rows attended from: the call's bound, else ``seq_len``."""
        valid = self.valid  # read first: it makes a derivation per call
        return valid if "valid" in self.bound_extents else self.seq_len

    @property
    def kv_tokens(self) -> int:
        """The keys attended over: the call's bound, else kv_len less Q's padding."""
        kv_valid, q_tokens = self.kv_valid, self.q_tokens  # extents first
        if "kv_valid" in self.bound_extents:
            return kv_valid
        return self.kv_len - self.seq_pad + q_tokens

    @property
    def first_query_block(self) -> int:
        """The position of Q's first row, in Q blocks, which mha.cc masks by."""
        if self.packed:
            return ceildiv(self.kv_tokens, self.B_q)
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

    def validate(self) -> None:
        if self.d <= 0 or self.d % 64:
            raise ValueError(f"d must be a positive multiple of 64, got d={self.d}")
        if self.window is not None and self.window <= 0:
            raise ValueError(f"window must be positive or None, got {self.window}")
        # partial_softmax scales a row's maximum in place of every element.
        if not 0 <= self.scale < np.inf:
            raise ValueError(f"scale must be finite and not negative, got {self.scale}")
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
        if 64 % self.B_q:
            raise ValueError(
                f"B_q ({self.B_q}) must divide 64, the block seq_pad is whole of"
            )
        if self.pv_cores not in (1, 2) or self.pv_width * self.pv_cores != self.d:
            raise ValueError(
                f"P*V takes one core or two, each a pv_width ({self.pv_width}) "
                f"share of d ({self.d}); got pv_cores={self.pv_cores}"
            )
        for pv, dims in (
            (False, ("B_q", "d", "B_kv")),
            (True, ("B_q", "B_kv", "pv_width")),
        ):
            mac = kernels.linalg.mha.mac_dims(
                pv=pv,
                device=self.dev,
            )
            for name, m in zip(dims, mac):
                if vars(self)[name] % m:
                    raise ValueError(
                        f"{name}={vars(self)[name]} must be a multiple of "
                        f"{'P*V' if pv else 'QK^T'}'s micro-tile {mac}"
                    )
        # A row whose window misses a key block another row of its query
        # block keeps would weigh its masked keys 1 (mha.cc).
        if self.window and self.window % self.B_q:
            raise ValueError(
                f"window ({self.window}) must be whole {self.B_q}-row blocks"
            )
        if not self.packed and self.seq_pad % (64 * self.num_pipelines):
            raise ValueError(
                f"seq_pad ({self.seq_pad}) must be whole rounds of 64 rows on "
                f"each of num_pipelines ({self.num_pipelines})"
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
        if self.num_pipelines > self.width:
            raise ValueError(
                f"num_pipelines ({self.num_pipelines}) is at most the "
                f"{self.width} columns it is placed on, one pipeline a column"
            )
        if self.pv_cores > 1 and self.num_pipelines // self.q_shims > 4:
            raise ValueError(
                f"with P*V split, an O join serves at most 4 pipelines, not "
                f"{self.num_pipelines // self.q_shims}: its memtile also forwards "
                f"a pipeline's scores and P"
            )
        if self.packed:
            if self.window:
                raise ValueError(
                    "one query packed sits past every key block, where a "
                    "window would mask them"
                )
            if self.pv_cores > 1:
                raise ValueError(
                    "one query packed reads K and V over its pipeline's own "
                    "shim, whose two channels leave V one lane: P*V takes one core"
                )
            group = self.num_heads // self.num_KV_heads
            if group > self.B_q:
                raise ValueError(
                    f"one query packs a KV group's {group} heads into a block's "
                    f"B_q ({self.B_q}) rows, which must hold them"
                )
            q = self.COLUMNS[self.width].q
            if self.num_pipelines > q or self.num_KV_heads % self.num_pipelines:
                raise ValueError(
                    f"one query takes num_pipelines ({self.num_pipelines}) at most "
                    f"{q} dividing num_KV_heads ({self.num_KV_heads}): each pipeline "
                    f"has its own K and V lanes, through its own column's memtile"
                )

    @classmethod
    def fits(cls, dev) -> bool:
        """Whether ``dev`` has the columns of a layout MHA is placed on."""
        return dev.cols >= min(cls.COLUMNS)

    def resolve(self, dev):
        if dev is not None and not self.fits(dev):
            raise Unresolvable(
                f"MHA is placed on {min(self.COLUMNS)} columns or more; got "
                f"{dev.name} ({dev.arch}) with {dev.cols}"
            )
        B_q, pv_cores = self.B_q, self.pv_cores
        mem = None if dev is None else dev.core_memory_bytes
        if B_q is None or pv_cores is None:
            if dev is None:
                raise Unresolvable(
                    "MHA's block size and P*V cores follow the cores' memory; "
                    "none is bound and not both were given"
                )
            group = self.num_heads // self.num_KV_heads
            # Every row of a packed block is computed: the narrowest holding the group.
            blocks = (16, 32, 64) if self.packed else (64, 32, 16)
            fit = next(
                (
                    (cores, b)
                    for cores in ((1, 2) if pv_cores is None else (pv_cores,))
                    for b in (blocks if B_q is None else (B_q,))
                    if self.core_bytes(b, self.key_block(b, mem), cores) <= mem
                    and not (self.packed and B_q is None and group > b)
                ),
                None,
            )
            if fit is None and B_q is None:
                raise Unresolvable(
                    f"MHA at d={self.d}: no block of 16 rows or more fits a "
                    f"core's {mem} bytes"
                )
            pv_cores, B_q = fit or (pv_cores or 1, B_q)
        B_kv = self.key_block(B_q, mem)
        if self.B_kv not in (None, B_kv):
            raise ValueError(
                f"B_kv ({self.B_kv}) is {B_kv}: "
                + (
                    "one query packed takes the widest key block that fits"
                    if self.packed
                    else f"B_q's, as mha.cc's causal skip compares a KV block's "
                    f"index with a Q block's"
                )
            )
        q_shims = 2 if self.num_pipelines > 6 else 1
        if dev is not None:
            width = max(w for w in self.COLUMNS if w <= dev.cols)
        else:
            width = max(self.COLUMNS) if self.width is None else self.width
        if pv_cores > 1 and width not in self.SPLIT_COLUMNS:
            raise Unresolvable(
                f"MHA at d={self.d} splits P*V over two cores, which is placed "
                f"on {', '.join(map(str, self.SPLIT_COLUMNS))} columns, not {width}"
            )
        return dataclasses.replace(
            self,
            B_q=B_q,
            B_kv=B_kv,
            q_shims=q_shims,
            join_rows=B_q * (self.num_pipelines // q_shims),
            kv_lanes=self.num_pipelines if self.packed else 1,
            width=width,
            pv_cores=pv_cores,
            pv_width=self.d // pv_cores,
        )

    def seq_padding(self, seq_len: int) -> int:
        """``seq_len`` rounded up to 64; one query, packed, is not padded."""
        if seq_len == 1:
            return 1
        return ceildiv(seq_len, 64) * 64

    def key_block(self, B_q: int, mem: int | None) -> int:
        """``B_kv`` for ``B_q``: ``B_q`` itself, which mha.cc's causal skip
        compares by; packed, past every key, the widest that fits ``mem`` (any
        where None), since mha.cc's vectorized softmax reads 64-key rows."""
        if not self.packed:
            return B_q
        return next(
            (
                b
                for b in (64, 32, 16)
                if B_q <= b
                and not self.kv_len % b
                and (mem is None or self.core_bytes(B_q, b, 1) <= mem)
            ),
            B_q,
        )

    def core_bytes(self, B_q: int, B_kv: int, pv_cores: int) -> int:
        """The L1 bytes the fuller of a pipeline's QK^T and P*V cores holds.

        Args:
            pv_cores: The P*V cores the head is split over.

        Returns:
            The larger core's bytes, its stack included.
        """
        d, pv_width = self.d, self.d // pv_cores
        pv = 4 * B_q * B_kv + 4 * pv_width * B_kv + 6 * pv_width * B_q + 32 * B_q
        qk = (4 if pv_cores == 1 else 2) * d * B_q + 4 * d * B_kv + 4 * B_q * B_kv
        return max(pv, qk) + STACK_SIZE

    class Array(Operator.Array):
        B_q: int
        B_kv: int
        d: int
        causal: bool
        window: int | None
        scale: float
        num_pipelines: int
        kv_lanes: int
        width: int
        pv_cores: int
        pv_width: int
        q_shims: int
        join_rows: int
        Q: Operand
        K: Operand
        V: Operand
        O: Operand
        heads: Value
        kv_blocks: Value
        q_blocks_per_pipeline: Value
        q_blocks_valid: Value
        q_start: Value
        s_q: Value
        s_kv: Value
        dev: Device

        def build(self) -> Built:
            of_depth = 2
            dtype = bfloat16
            B_q, B_kv, d = self.B_q, self.B_kv, self.d
            num_pipelines = self.num_pipelines
            n_join = num_pipelines // self.q_shims  # the pipelines on one shim
            # With P*V split, the two P*V cores share SPLIT_COLUMNS' own adjacent
            # tiles, the line between them shared L1, a physical invariant no
            # placer can infer; aiecc's placer takes every other tile (checked
            # against mlir-aie #3921's placer fixes, 533e0c121: the full catalog,
            # Llama and EG2's MHA shapes placed freely are numpy-correct on npu2,
            # and within noise of the old hand pins on every shape but one, a
            # 16384-token prefill chunk, where the gap (~0.1%, 338246 vs 338409 us
            # median over repeats) is small enough next to the pin's own run-to-
            # run spread not to keep it).
            pv_cores, pv_width = self.pv_cores, self.pv_width
            every = pv_cores > 1
            memtiles = every

            # partial_softmax takes exp2, so the scale is in the log2 domain.
            inv_scale = float(bfloat16(self.scale * np.log2(np.e)))
            # AIE2P's exp2 instruction is up to 6% high; AIE2 has none to replace.
            accurate_exp2 = self.dev.arch is AIEArch.AIE2p

            q_ty = np.ndarray[(B_q, d), np.dtype[dtype]]
            k_ty = np.ndarray[(d, B_kv), np.dtype[dtype]]
            v_ty = np.ndarray[(B_kv, pv_width), np.dtype[dtype]]
            o_ty = np.ndarray[(B_q, pv_width), np.dtype[dtype]]
            qk_ty = np.ndarray[(B_q, B_kv), np.dtype[dtype]]
            s_ty = np.ndarray[(4 * B_q,), np.dtype[np.float32]]
            acc_ty = np.ndarray[(B_q, pv_width), np.dtype[np.float32]]
            joined_ty = self.Q.obj_type  # (n_join * B_q, d)

            # The rest bind from mha.cc's object: declared apart, each would
            # redefine it. Never on bfp16 macs: bfp16 shares an exponent over 8
            # keys of P*V, and the softmax bounds the time.
            matmul_QK = kernels.linalg.mha(
                B_q,
                d,
                B_kv,
                b_col_maj=True,
                accurate_exp2=accurate_exp2,
                causal=self.causal,
                window=self.window or 0,
            )
            mha_object = matmul_QK.object_file

            zero_scores = kernels.zero(tile_size=(B_q, B_kv), dtype=dtype)
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
            # Split, a P*V core's product is mha.cc compiled at its share's width.
            pv_object = (
                mha_object
                if pv_cores == 1
                else kernels.linalg.mha(
                    B_q,
                    pv_width,
                    B_kv,
                    b_col_maj=True,
                    causal=self.causal,
                    window=self.window or 0,
                ).object_file
            )
            matmul_PV = pv_object.bind(
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
            rescale_O = pv_object.bind(
                "rescale_O",
                [acc_ty, o_ty, s_ty, np.int32, np.ndarray[(2,), np.dtype[np.int32]]],
            )

            # Each stream is blocked as the product that reads or writes it takes it.
            qk = matmul_QK.stream_dims
            pv = mm_stream_dims(
                B_q, B_kv, pv_width, kernels.linalg.mha.mac_dims(pv=True)
            )
            q_dims = qk.A
            k_dims = qk.B
            a_dims = qk.C
            p_dims = pv.A
            v_dims = pv.B
            o_dims = pv.C

            # Split, Q is one block deep: the QK core's L1 holds one d=512 block.
            split = pv_cores > 1
            q_depth = 1 if split else of_depth
            columns = MHA.COLUMNS[self.width]
            layout = MHA.SPLIT_COLUMNS[self.width] if split else None
            inQ, memQ, memO = [], [], []
            outO = [[] for _ in range(pv_cores)]
            for shim in range(self.q_shims):
                suffix = "" if shim == 0 else "2"
                in_q = ObjectFifo(joined_ty)
                inQ.append(in_q)
                memQ += in_q.cons().split(
                    offsets=[B_q * d * i for i in range(n_join)],
                    obj_types=[q_ty] * n_join,
                    to_stream=None if q_dims is None else [q_dims] * n_join,
                    depths=[q_depth] * n_join,
                    tile=(
                        Tile(layout.q[shim] if split else columns.qo_mem + shim, 1)
                        if memtiles
                        else AnyMemTile
                    ),
                )
                for h in range(pv_cores):
                    half = "" if h == 0 else f"_{h}"
                    mem_o = ObjectFifo(self.O.obj_type, to_stream=o_dims)
                    memO.append(mem_o)
                    outO[h] += mem_o.prod().join(
                        offsets=[B_q * pv_width * i for i in range(n_join)],
                        obj_types=[o_ty] * n_join,
                        # One O block: the PV core's L1 also holds its float32 O.
                        depths=[1] * n_join,
                        tile=(
                            Tile(
                                layout.o[shim][h] if split else columns.qo_mem + shim, 1
                            )
                            if memtiles
                            else AnyMemTile
                        ),
                    )

            kv_lanes = self.kv_lanes
            inK, inV, memK, memV = [], [], [], []
            for lane in range(kv_lanes):
                suffix = "" if lane == 0 else str(lane)
                shared = kv_lanes == 1
                inK.append(ObjectFifo(k_ty, depth=of_depth))
                memK.append(
                    inK[lane]
                    .cons()
                    .forward(
                        to_stream=k_dims,
                        tile=(
                            Tile(
                                (
                                    layout.k
                                    if split
                                    else columns.k_mem if shared else lane
                                ),
                                1,
                            )
                            if memtiles
                            else AnyMemTile
                        ),
                        depth=of_depth,
                    )
                )
                for h in range(pv_cores):
                    half = "" if h == 0 else f"_{h}"
                    inV.append(ObjectFifo(v_ty, depth=of_depth))
                    memV.append(
                        inV[-1]
                        .cons()
                        .forward(
                            to_stream=v_dims,
                            tile=(
                                Tile(
                                    (
                                        layout.v[h]
                                        if split
                                        else columns.v_mem if shared else lane
                                    ),
                                    1,
                                )
                                if memtiles
                                else AnyMemTile
                            ),
                            depth=of_depth,
                        )
                    )

            memA, outA, memP, outP, scaleOF = [], [], [], [], []
            for i in range(num_pipelines):
                memA.append(ObjectFifo(qk_ty, depth=of_depth))
                outA.append(
                    memA[i]
                    .cons()
                    .forward(
                        to_stream=a_dims,
                        depth=of_depth,
                        tile=Tile(i, 1) if split else AnyMemTile,
                    )
                )
                memP.append(ObjectFifo(qk_ty, depth=of_depth))
                outP.append(
                    memP[i]
                    .cons()
                    .forward(
                        to_stream=p_dims,
                        depth=of_depth,
                        tile=Tile(i, 1) if split else AnyMemTile,
                    )
                )
                # A copy of the row state for each P*V core, which rescales its own.
                scaleOF.append(
                    [ObjectFifo(s_ty, depth=of_depth) for h in range(pv_cores)]
                )

            # Q blocks past the bound pass through: Q and O stream every block.
            blocks = [
                self.heads,
                self.q_blocks_per_pipeline,
                self.q_blocks_valid,
                self.kv_blocks,
            ]

            def batched_matmul_qk(
                of_q,
                of_k,
                of_a_out,
                zero,
                matmul_QK,
                q_block_bias,
                rtp,
                idx_buffer,
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

                words = rtp.read()
                heads, q_blocks, q_valid, kv_blocks = (words[v] for v in blocks)
                q_start = words[self.q_start]
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
                rtp,
                idx_buffer,
                scale_buffer,
            ):
                # The index buffer is the kernel's position in A and P.
                def q_block(compute: bool, kv_blocks, s_q, s_kv):
                    if compute:
                        init_scale_buffer(scale_buffer, B_q)
                    for _ in range_(kv_blocks):
                        elt_of_out_p = of_out_p.acquire(1)
                        elt_of_in_a = of_in_a.acquire(1)
                        elts_of_out_scale = [of.acquire(1) for of in of_out_scale]
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
                            for elt in elts_of_out_scale:
                                memcopy_kernel_scale(scale_buffer, elt, 4 * B_q)
                        of_in_a.release(1)
                        of_out_p.release(1)
                        for of in of_out_scale:
                            of.release(1)
                        if compute:
                            idx_buffer[0] += 1
                    if compute:
                        idx_buffer[0] = 0
                        idx_buffer[1] += num_pipelines

                words = rtp.read()
                heads, q_blocks, q_valid, kv_blocks = (words[v] for v in blocks)
                s_q, s_kv, q_start = (
                    words[self.s_q],
                    words[self.s_kv],
                    words[self.q_start],
                )
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
                rtp,
                idx_buffer,
                acc,
            ):
                words = rtp.read()
                heads, q_blocks, q_valid, loop_idx_kv = (words[v] for v in blocks)
                s_kv, q_start = words[self.s_kv], words[self.q_start]
                for _ in range_(heads):
                    idx_buffer[0] = 0
                    idx_buffer[1] = q_start + q_block_bias

                    for _ in range_(q_valid):
                        # matmul_PV starts the accumulator on KV block 0.
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

            qk_rtps = [Rtp([*blocks, self.q_start]) for _ in range(num_pipelines)]
            softmax_rtps = [
                Rtp([*blocks, self.s_q, self.s_kv, self.q_start])
                for _ in range(num_pipelines)
            ]
            pv_rtps = [
                [Rtp([*blocks, self.s_kv, self.q_start]) for _ in range(num_pipelines)]
                for _ in range(pv_cores)
            ]

            matmul_workers, softmax_workers, matmul_pv_workers = [], [], []
            for i in range(num_pipelines):
                idx_buffer_qk = Buffer(
                    initial_value=np.zeros(shape=(2,), dtype=np.int32),
                )
                matmul_workers.append(
                    Worker(
                        batched_matmul_qk,
                        fn_args=[
                            memQ[i].cons(),
                            memK[i % kv_lanes].cons(),
                            memA[i].prod(),
                            zero_scores,
                            matmul_QK,
                            i,
                            qk_rtps[i],
                            idx_buffer_qk,
                        ],
                        stack_size=STACK_SIZE,
                        tile=Tile(i, 2) if every else AnyComputeTile,
                    )
                )
                idx_buffer_softmax = Buffer(
                    initial_value=np.zeros(shape=(2,), dtype=np.int32),
                )
                scale_buffer_softmax = Buffer(
                    initial_value=np.zeros(shape=(4 * B_q,), dtype=np.float32),
                )
                softmax_workers.append(
                    Worker(
                        softmax,
                        fn_args=[
                            outA[i].cons(),
                            memP[i].prod(),
                            [of.prod() for of in scaleOF[i]],
                            partial_softmax_kernel,
                            scale_buffer_init_kernel,
                            memcopy_kernel_scale,
                            i,
                            softmax_rtps[i],
                            idx_buffer_softmax,
                            scale_buffer_softmax,
                        ],
                        stack_size=SOFTMAX_STACK_SIZE,
                        tile=(
                            Tile(i, 3 if pv_cores == 1 else 4)
                            if every
                            else AnyComputeTile
                        ),
                    )
                )
                # Split, the halves sit either side of the softmax, whose row
                # state each reads from shared memory.
                for h, row in enumerate([4] if pv_cores == 1 else [3, 5]):
                    idx_buffer_pv = Buffer(
                        initial_value=np.zeros(shape=(2,), dtype=np.int32),
                    )
                    matmul_pv_workers.append(
                        Worker(
                            batched_matmul_pv,
                            fn_args=[
                                outP[i].cons(),
                                memV[(i % kv_lanes) * pv_cores + h].cons(),
                                scaleOF[i][h].cons(),
                                outO[h][i].prod(),
                                matmul_PV,
                                rescale_O,
                                i,
                                pv_rtps[h][i],
                                idx_buffer_pv,
                                Buffer(acc_ty),
                            ],
                            stack_size=STACK_SIZE,
                            tile=Tile(i, row) if every else AnyComputeTile,
                        )
                    )

            two_shims = self.q_shims > 1
            qs, outs, ks, vs = [], [], [], []
            for s in range(self.q_shims):
                q_col = layout.q[s] if split else 0 if two_shims else columns.q
                qs.append(inQ[s].prod(tile=Tile(q_col, 0) if every else AnyShimTile))
                for h in range(pv_cores):
                    o_col = layout.o[s][h] if split else 0 if two_shims else columns.o
                    outs.append(
                        memO[s * pv_cores + h].cons(
                            tile=Tile(o_col, 0) if every else AnyShimTile
                        )
                    )
            for lane in range(kv_lanes):
                shared = kv_lanes == 1
                k_col = layout.k_shim if split else columns.k if shared else lane
                ks.append(inK[lane].prod(tile=Tile(k_col, 0) if every else AnyShimTile))
                for h in range(pv_cores):
                    v_col = layout.v[h] if split else columns.v if shared else lane
                    vs.append(
                        inV[lane * pv_cores + h].prod(
                            tile=Tile(v_col, 0) if every else AnyShimTile
                        )
                    )
            self.Q.bind(qs)
            self.O.bind(outs)
            self.K.bind(ks)
            self.V.bind(vs)

            return Built(
                matmul_workers + softmax_workers + matmul_pv_workers,
                [*qk_rtps, *softmax_rtps, *(r for rtps in pv_rtps for r in rtps)],
            )

    def ops(self) -> int:
        """Q K^T and its product with V per head, over the keys each query keeps."""
        keys = self.kv_len - self.seq_pad + self.seq_len
        position = keys - self.seq_len + np.arange(self.seq_len)
        ahead = 0 if self.causal else (self.window or keys)
        lo = np.maximum(position - self.window, 0) if self.window else 0
        hi = np.minimum(position + ahead, keys - 1)
        return 4 * self.num_heads * self.d * int((hi - lo + 1).sum())

    def reference(self, Q, K, V, s_q=None, s_kv=None):
        """Attention per head, the queries the keys' last rows; query rows from
        ``s_q`` on are zeros and keys from ``s_kv`` on are masked.
        """
        if self.heads_interleaved:
            Q = np.swapaxes(Q, 0, 1)
        if self.kv_interleaved:
            K, V = (np.swapaxes(t, 0, 1) for t in (K, V))
        groups = self.num_heads // self.num_KV_heads
        offset = K.shape[1] - Q.shape[1]
        start = offset if self.causal or self.window else 0
        s_q = start + self.seq_len if s_q is None else int(s_q)
        s_kv = offset + self.seq_len if s_kv is None else int(s_kv)
        K, V = K[:, :s_kv], V[:, :s_kv]
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
        # A head at a time: at 16K rows one head's scores are 1 GiB of float32.
        for h in range(q.shape[0]):
            scores = q[h] @ k[h // groups].T * scale + mask
            e = np.exp(scores - scores.max(axis=-1, keepdims=True))
            out[h, :rows] = (e / e.sum(axis=-1, keepdims=True)) @ v[h // groups]
        if self.heads_interleaved:
            return np.ascontiguousarray(np.swapaxes(out, 0, 1))
        return out

    def tolerance(self) -> Tolerance:
        return Tolerance(rtol=0.04, atol=0.15, max_mismatch_frac=0.005)

    def sequence(self, rt):
        """One descriptor set per KV group: K and V re-read per (head, block)
        from the iteration slot, not six descriptors per block.
        """
        kv_heads = self.num_KV_heads
        group = self.num_heads // kv_heads
        rows = self.join_rows  # Q rows each shim carries per block
        blocks = ceildiv(self.seq_pad, rows * self.q_shims)  # per pipeline
        B_kv = self.B_kv
        kv_blocks = ceildiv(self.kv_tokens, B_kv)
        kv_valid = self.kv_blocks if self.kv_blocks.per_call else None

        def by_head(buffer, interleaved):
            tap = TensorAccessPattern.full(buffer.shape)
            return tap.permute((1, 0, 2)) if interleaved else tap

        def q_rows(buffer, head0, shim):
            heads = by_head(buffer, self.heads_interleaved)[head0 : head0 + group]
            by_shim = heads.split(1, self.q_shims * rows)
            return by_shim[:, :, shim * rows : (shim + 1) * rows]

        def kv_rows(buffer, kv_head, reads):
            head = by_head(buffer, self.kv_interleaved)[kv_head, : kv_blocks * B_kv]
            return head.split(0, B_kv).repeat(reads)

        if self.packed:
            steps = kv_heads // self.num_pipelines
            # A group that does not divide a block is two overlapping runs.
            width = 1 << (group.bit_length() - 1)

            def packed_rows(buffer, kv_head):
                heads = by_head(buffer, self.heads_interleaved)
                if width == group:
                    heads = heads[kv_head * group : (kv_head + 1) * group, 0]
                    return heads.coalesce().repeat(self.B_q // group)
                first = heads[kv_head * group : kv_head * group + width, 0]
                both = TensorAccessPattern(
                    first.tensor_dims,
                    first.offset,
                    (2, *first.sizes),
                    ((group - width) * first.strides[0], *first.strides),
                )
                return both.coalesce().repeat(self.B_q // (2 * width))

            for step in range(steps):
                owned = [p * steps + step for p in range(self.num_pipelines)]
                tg = TaskGroup()
                for kv_head in owned:
                    self.Q.fill(packed_rows(self.Q, kv_head), lane=0, group=tg)
                for p, kv_head in enumerate(owned):
                    for x in (self.K, self.V):
                        x.fill(
                            kv_rows(x, kv_head, 1),
                            lane=p,
                            group=tg,
                            length_parameter=kv_valid,
                            length_unit=B_kv * x.shape[-1],
                        )
                for kv_head in owned:
                    self.O.drain(
                        packed_rows(self.O, kv_head), lane=0, group=tg, wait=True
                    )
                tg.finish()
            return

        cores, pv_width = self.pv_cores, self.pv_width
        # A shim descriptor's iteration count.
        iterations = 1 << self.dev.get_dma_bd_iter_bits(0, 0)
        for kv_head in range(kv_heads):
            head0 = kv_head * group
            tg = TaskGroup()
            for shim in range(self.q_shims):
                self.Q.fill(q_rows(self.Q, head0, shim), lane=shim, group=tg)
            # A bounded pattern is one descriptor: re-reads at most the slot's count.
            reads = group * blocks
            for first in range(0, reads, iterations):
                count = min(iterations, reads - first)
                self.K.fill(
                    kv_rows(self.K, kv_head, count),
                    group=tg,
                    length_parameter=kv_valid,
                    length_unit=B_kv * self.K.shape[-1],
                )
                for h in range(cores):
                    self.V.fill(
                        kv_rows(self.V, kv_head, count)[
                            ..., h * pv_width : (h + 1) * pv_width
                        ],
                        lane=h,
                        group=tg,
                        length_parameter=kv_valid,
                        length_unit=B_kv * pv_width,
                    )
            for shim in range(self.q_shims):
                for h in range(cores):
                    self.O.drain(
                        q_rows(self.O, head0, shim)[
                            ..., h * pv_width : (h + 1) * pv_width
                        ],
                        lane=shim * cores + h,
                        group=tg,
                        wait=True,
                    )
            tg.finish()
