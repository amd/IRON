# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Fused multi-head attention: ``num_pipelines`` three-stage pipelines (QK^T, partial softmax, P*V).

One per column, Q split across them on a memtile, K and V forwarded to
every one; P*V may split over two cores when d=512. The queries are the
keys' last rows, padded to 64, except one (a decode step), which packs a
KV group's heads into a block instead.
"""

import dataclasses
from typing import ClassVar

import numpy as np
from aie.dialects.aie import AIEArch
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, In, ObjectFifo, Out, Worker, ceildiv, kernels
from aie.iron.controlflow import range_
from aie.iron.device import AnyComputeTile, AnyMemTile, AnyShimTile, Device, Tile
from aie.iron.kernels.linalg import mm_stream_dims
from aie.utils import set_current_device
from aie.utils.compile.jit.context import compile_context
from aie.utils.compile.jit.params import (
    Select,
    divisors,
    param,
    per_call,
    tunable,
    widths,
)
from aie.utils.compile.utils import resolve_target_arch
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Rtp, Unresolvable
from iron.common.declare import Operand, Value
from iron.common.declare.operand import concrete
from iron.common.declare.operator import LaneTransfers
from iron.common.testing import Case, Testing


@dataclasses.dataclass(frozen=True)
class SplitColumns:
    """Where MHA's streams meet the array with P*V split over two cores.

    Each column carries every stream its links hold, so these are what the
    router finds.

    Attributes:
        q: Each Q shim's split.
        o: Each Q shim's O joins, one per half of the head.
        k, k_shim: K's memtile and shim.
        v: V's, one per half of the head.
    """

    q: tuple[int, ...]
    o: tuple[tuple[int, ...], ...]
    k: int
    k_shim: int
    v: tuple[int, ...]


# Whole in seq_pad's 64-row unit, up to the largest whose cores fit L1.
def block_sizes(op, dev, start: int) -> tuple[int, ...]:
    """Return the query blocks to try, whole in seq_pad's 64-row unit, up to the largest whose cores fit L1."""
    cap = max(
        (
            b
            for b in (16, 32, 64)
            if op.core_bytes(dev, b, op.key_block(b, dev), op.pv_cores)
            <= dev.core_memory_bytes
        ),
        default=16,
    )
    return divisors(start, of=op.kv_len, step=8 if op.packed else 16, cap=cap)


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
    # Gemma 3 1B's sliding decode and prompt chunk: a window not whole blocks.
    *(
        Case(
            dict(
                num_heads=4,
                num_KV_heads=1,
                d=256,
                seq_len=seq_len,
                kv_len=2048,
                window=511,
                num_pipelines=pipelines,
                heads_interleaved=True,
            ),
            lower=True,
        )
        for seq_len, pipelines in ((1, 1), (512, 8))
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
    # Llama 3.2 1B's and 3B's prompt chunk, and a full-attention layer at
    # d=256: 2048 queries, the last rows of 2K, 8K and 32K keys of a
    # KVCache.
    *(
        Case(
            dict(
                num_heads=heads,
                num_KV_heads=kv_heads,
                d=d,
                seq_len=2048,
                kv_len=kv_len,
                num_pipelines=8,
                heads_interleaved=True,
                kv_paired=True,
            ),
            id=f"chunk-d{d}-{kv_len // 1024}k",
            extensive=kv_len > 8192,
            bench=True,
        )
        for heads, kv_heads, d in ((32, 8, 64), (24, 8, 128), (8, 2, 256))
        for kv_len in (2048, 8192, 32768)
    ),
    # The same over its K and V apart, and paired with P*V split.
    Case(
        dict(
            num_heads=32,
            num_KV_heads=8,
            seq_len=2048,
            kv_len=2048,
            num_pipelines=8,
            heads_interleaved=True,
            kv_interleaved=True,
        ),
        lower=True,
    ),
    Case(
        dict(
            num_heads=32,
            num_KV_heads=8,
            seq_len=2048,
            kv_len=4096,
            num_pipelines=8,
            heads_interleaved=True,
            kv_paired=True,
            pv_cores=2,
        ),
        lower=True,
    ),
    # Llama 3.2 1B's and 3B's prompt chunk on one core a query block, and
    # Gemma 4 E2B's sliding layer, its 8 heads over one KV head (AIE2).
    *(
        Case(
            dict(
                num_heads=heads,
                num_KV_heads=kv_heads,
                d=d,
                seq_len=seq_len,
                kv_len=4096,
                window=window,
                num_pipelines=8,
                heads_interleaved=True,
                kv_paired=True,
                cores_per_block=1,
            ),
            lower=True,
        )
        for heads, kv_heads, d, seq_len, window in (
            (32, 8, 64, 2048, None),
            (24, 8, 128, 2048, None),
            (8, 1, 256, 512, 511),
        )
    ),
    # Llama 3.2 1B's decode step over 32K keys of a KVCache.
    Case(
        dict(
            num_heads=32,
            num_KV_heads=8,
            seq_len=1,
            kv_len=32768,
            num_pipelines=4,
            heads_interleaved=True,
            kv_paired=True,
        ),
        id="decode-d64-32k",
        bench=True,
    ),
]


def _cases(cls, dev: Device):
    share = 1 if dev.cols >= max(cls.PACKED_PIPELINES) else 2
    return [
        dataclasses.replace(
            c,
            kwargs={
                **c.kwargs,
                "num_pipelines": max(1, c.kwargs["num_pipelines"] // share),
            },
        )
        for c in _CASES
        # One core a query block is attend_block, AIE2's.
        if c.kwargs.get("cores_per_block") != 1 or dev.arch is AIEArch.AIE2
    ]


class MHA(Operator):
    """Fused attention over ``(B_q, d)`` Q, ``(d, B_kv)`` K and ``(B_kv, d)`` V blocks.

    More than six pipelines split Q and O over two shims.
    """

    test = Testing(_cases)

    num_heads: int = param()
    num_KV_heads: int = param(default=lambda op: op.num_heads)
    seq_len: int = param(default=lambda op: op.seq_pad)
    seq_pad: int = param(derive=lambda op: op.seq_padding(op.seq_len), repr=False)
    # A cache longer than the queries, whose last rows the queries are.
    kv_len: int = param(default=lambda op: op.seq_pad)
    # ``(seq, heads, d)`` as a projection writes it, so no copy reorders the heads.
    heads_interleaved: bool = param(default=False)
    # One operand KV, ``(kv_len, num_KV_heads, 2, d)``, a position's K and V
    # side by side as a KVCache holds them, in place of K and V.
    kv_paired: bool = param(default=False)
    kv_apart: bool = param(default=lambda op: not op.kv_paired, repr=False)
    kv_interleaved: bool = param(default=lambda op: op.kv_paired)
    d: int = param(default=64)
    causal: bool = param(default=True, array=True)
    # Keys more than this many positions from a query are masked.
    window: int | None = param(default=None, array=True)
    scale: float = param(default=lambda op: float(1 / np.sqrt(op.d)), array=True)
    # One query, a KV group's heads packed as a block's rows.
    packed: bool = param(
        derive=lambda op: op.seq_len == 1, repr=False, array=True, init=False
    )
    B_q: int = tunable(domain=block_sizes)
    B_kv: int = tunable(repr=False, init=False)
    num_pipelines: int = tunable(default=1, domain=widths)
    # Filled by resolve.
    q_shims: int = tunable(repr=False, init=False)
    join_rows: int = tunable(repr=False, init=False)
    kv_lanes: int = tunable(repr=False, init=False)
    # KV's lanes for each of kv_lanes: K's, then V's on each P*V core.
    kv_streams: int = tunable(repr=False, init=False)
    width: int = tunable(repr=False, init=False)
    # Two P*V cores, by halves of the head, where one's L1 holds no block.
    pv_cores: int = tunable(repr=False, domain=(1, 2))
    pv_width: int = tunable(repr=False, init=False)
    # The cores a query block's key blocks take: 3, today's pipeline of a
    # QK^T, a softmax and a P*V core; 1, mha.cc's attend_block on every core
    # of the columns placed (AIE2, over a paired KV).
    cores_per_block: int = tunable(default=3, domain=(1, 3))
    fused: bool = tunable(repr=False, init=False)
    # Fused, the cores a column holds, each a query block of a round.
    column_cores: int = tunable(repr=False, init=False)
    # The query heads a block packs a position, position-major: fused, a KV
    # group's; else 1.
    group: int = tunable(repr=False, init=False)

    aiecc_flags: ClassVar[tuple[str, ...]] = ("--reclaim-runtime-bds",)

    # The array widths MHA is placed on, each with the most pipelines one
    # query packed takes, a K and a V lane each.
    PACKED_PIPELINES: ClassVar[dict[int, int]] = {8: 4, 4: 2}
    SPLIT_COLUMNS: ClassVar[dict[int, SplitColumns]] = {
        8: SplitColumns(q=(1, 6), o=((0, 2), (5, 7)), k=3, k_shim=3, v=(3, 4)),
        4: SplitColumns(q=(0,), o=((1, 2),), k=3, k_shim=0, v=(3, 3)),
    }

    Q = In(
        Select(
            heads_interleaved,
            (seq_pad, num_heads, d),
            (num_heads, seq_pad, d),
        ),
        obj_shape=(join_rows, d),
        per=(q_shims,),
    )
    K = In(
        Select(
            kv_interleaved,
            (kv_len, num_KV_heads, d),
            (num_KV_heads, kv_len, d),
        ),
        obj_shape=(d, B_kv),
        per=(kv_lanes,),
        when=kv_apart,
    )
    V = In(
        Select(
            kv_interleaved,
            (kv_len, num_KV_heads, d),
            (num_KV_heads, kv_len, d),
        ),
        obj_shape=(B_kv, pv_width),
        per=(kv_lanes, pv_cores),
        when=kv_apart,
    )
    # A K lane's blocks, build() giving each V lane V's; fused, a block's keys
    # each its K row then its V row, one stream to every core.
    KV = In(
        kv_len,
        num_KV_heads,
        2,
        d,
        obj_shape=Select(fused, (B_kv, 2, d), (d, B_kv)),
        per=(kv_lanes, kv_streams),
        when=kv_paired,
    )
    O = Out(  # noqa: E741 -- an operand name: attention's Q, K, V, O
        Select(
            heads_interleaved,
            (seq_pad, num_heads, d),
            (num_heads, seq_pad, d),
        ),
        obj_shape=(join_rows, pv_width),
        per=(q_shims, pv_cores),
    )
    # A bound on the queries limits the compute; Q and O stream every row.
    valid = per_call(bounds=seq_pad)
    # A bound on the keys limits K's and V's blocks: the work follows the context.
    kv_valid = per_call(bounds=kv_len)
    # One query packed sits past every key block: no causal skip, no diagonal.
    heads = per_call(
        derive=lambda op: (
            op.num_KV_heads
            if op.fused
            else op.num_KV_heads // op.num_pipelines if op.packed else op.num_heads
        ),
    )
    # Fused, a core's rounds a KV head: one query block each.
    q_blocks_per_pipeline = per_call(
        derive=lambda op: ceildiv(op.seq_pad, op.positions * op.streams)
    )
    q_blocks_valid = per_call(
        derive=lambda op: ceildiv(op.q_tokens, op.positions * op.streams)
    )
    kv_blocks = per_call(derive=lambda op: ceildiv(op.kv_tokens, op.B_kv))
    # Fused, the key blocks each of ROUND_GROUPS groups of rounds streams: up
    # to its last valid query, so a round's stream ends near its own.
    kv_blocks_0 = per_call(derive=lambda op: op.group_blocks(0))
    kv_blocks_1 = per_call(derive=lambda op: op.group_blocks(1))
    kv_blocks_2 = per_call(derive=lambda op: op.group_blocks(2))
    kv_blocks_3 = per_call(derive=lambda op: op.group_blocks(3))
    # And each group's rounds.
    rounds_0 = per_call(derive=lambda op: op.group_rounds(0))
    rounds_1 = per_call(derive=lambda op: op.group_rounds(1))
    rounds_2 = per_call(derive=lambda op: op.group_rounds(2))
    rounds_3 = per_call(derive=lambda op: op.group_rounds(3))
    s_q = per_call(
        derive=lambda op: (
            (op.first_query_block + op.num_pipelines) * op.B_q
            if op.packed
            else op.first_query_block * op.B_q + op.q_tokens * op.group
        ),
    )
    s_kv = per_call(derive=lambda op: op.kv_tokens)
    q_start = per_call(derive=lambda op: op.first_query_block)
    q_offset = per_call(
        derive=lambda op: 0 if op.packed else op.first_query % op.positions
    )

    ROUND_GROUPS: ClassVar[int] = 4

    @property
    def round_groups(self) -> list[range]:
        """The rounds of each group, fused: ROUND_GROUPS runs, the last ones empty where the rounds are fewer."""
        rounds = self.seq_pad // (self.positions * self.streams)
        size = ceildiv(rounds, self.ROUND_GROUPS)
        return [
            range(min(g * size, rounds), min((g + 1) * size, rounds))
            for g in range(self.ROUND_GROUPS)
        ]

    def group_rounds(self, g: int) -> int:
        """Return group ``g``'s rounds, fused; else 0."""
        return len(self.round_groups[g]) if self.fused else 0

    def group_blocks(self, g: int) -> int:
        """Return the key blocks group ``g``'s rounds stream: through its last valid query's position, at least one."""
        if not self.fused:
            return 0
        rounds = self.round_groups[g]
        end = min(rounds.stop * self.positions * self.streams, self.q_tokens)
        blocks = ceildiv(self.first_query + end, self.B_kv)
        return max(1, min(blocks, ceildiv(self.kv_tokens, self.B_kv)))

    @property
    def positions(self) -> int:
        """The positions a query block covers, its rows over ``group``."""
        return self.B_q // self.group

    @property
    def streams(self) -> int:
        """The query blocks a round takes: a block a pipeline, or a core fused."""
        return self.num_pipelines * (self.column_cores if self.fused else 1)

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
    def first_query(self) -> int:
        """The position of Q's first row, which mha.cc masks by; 0 unmasked."""
        if not (self.causal or self.window):
            return 0
        start = self.kv_tokens - self.q_tokens
        if start < 0:
            raise ValueError(
                f"MHA: the {self.q_tokens} queries are more than the "
                f"{self.kv_tokens} keys whose last rows they are"
            )
        return start

    @property
    def first_query_block(self) -> int:
        """The Q block ``first_query`` is in, ``q_offset`` positions into it."""
        if self.packed:
            return ceildiv(self.kv_tokens, self.B_q)
        return self.first_query // self.positions

    def extent_unit(self, buffer: str) -> int:
        return 0  # no tiles-per-lane word: the sequence patches K and V itself

    def validate(self) -> None:
        if self.d <= 0 or self.d % 64:
            raise ValueError(f"MHA: d ({self.d}) must be a positive multiple of 64")
        if self.kv_apart == self.kv_paired:
            raise ValueError(
                f"MHA: K and V are apart or paired as KV, one of them; got "
                f"kv_apart={self.kv_apart}, kv_paired={self.kv_paired}"
            )
        if self.kv_paired and not self.kv_interleaved:
            raise ValueError("MHA: KV is position-major: kv_paired is kv_interleaved")
        if self.window is not None and self.window <= 0:
            raise ValueError(f"MHA: window ({self.window}) must be positive or None")
        # partial_softmax scales a row's maximum in place of every element.
        if not 0 <= self.scale < np.inf:
            raise ValueError(
                f"MHA: scale ({self.scale}) must be finite and not negative"
            )
        if self.num_pipelines < 1:
            raise ValueError(
                f"MHA: num_pipelines ({self.num_pipelines}) must be at least 1"
            )
        if self.num_pipelines > 6 and self.num_pipelines % 2:
            raise ValueError(
                f"MHA: num_pipelines ({self.num_pipelines}) above 6 must be even: "
                f"the pipelines are split over two shims"
            )
        if self.num_heads <= 0:
            raise ValueError(f"MHA: num_heads ({self.num_heads}) must be at least 1")
        if self.num_KV_heads <= 0:
            raise ValueError(
                f"MHA: num_KV_heads ({self.num_KV_heads}) must be at least 1"
            )
        if self.num_KV_heads > self.num_heads:
            raise ValueError(
                f"MHA: num_KV_heads ({self.num_KV_heads}) must be at most "
                f"num_heads ({self.num_heads})"
            )
        if self.num_heads % self.num_KV_heads:
            raise ValueError(
                f"MHA: num_heads ({self.num_heads}) must be a multiple of "
                f"num_KV_heads ({self.num_KV_heads})"
            )
        if self.seq_len <= 0:
            raise ValueError(f"MHA: seq_len ({self.seq_len}) must be at least 1")
        # Before resolve() sizes the cores, which builds each P*V share's kernel.
        if self.pv_cores is not None and (
            self.pv_cores not in (1, 2) or self.d % self.pv_cores
        ):
            raise ValueError(
                f"MHA: P*V takes one core or two, each an equal share of d "
                f"({self.d}); got pv_cores={self.pv_cores}"
            )

    def compatible(self) -> None:
        if self.pv_cores not in (1, 2) or self.pv_width * self.pv_cores != self.d:
            raise ValueError(
                f"MHA: P*V takes one core or two, each a pv_width ({self.pv_width}) "
                f"share of d ({self.d}); got pv_cores={self.pv_cores}"
            )
        for pv, dims in (
            (False, ("B_q", "d", "B_kv")),
            (True, ("B_q", "B_kv", "pv_width")),
        ):
            mac = kernels.linalg.mha.mac_dims(  # pyright: ignore[reportFunctionMemberAccess]
                pv=pv, device=self.dev
            )
            for name, m in zip(dims, mac):
                if vars(self)[name] % m:
                    raise ValueError(
                        f"MHA: {name} ({vars(self)[name]}) must be a multiple of "
                        f"{'P*V' if pv else 'QK^T'}'s micro-tile {mac}"
                    )
        if self.fused:
            group = self.num_heads // self.num_KV_heads
            if self.B_q % 8 or self.B_q % group or 64 % self.positions:
                raise ValueError(
                    f"MHA: B_q ({self.B_q}) must be whole groups of 8 rows and of "
                    f"{group} heads a position, its positions dividing 64"
                )
            if self.seq_pad % (self.positions * self.streams):
                raise ValueError(
                    f"MHA: seq_pad ({self.seq_pad}) must be whole rounds of "
                    f"{self.streams} blocks of {self.positions} positions"
                )
            if self.kv_len % self.B_kv or self.kv_len < self.seq_pad:
                raise ValueError(
                    f"MHA: kv_len ({self.kv_len}) must be whole {self.B_kv}-row blocks "
                    f"and at least seq_pad ({self.seq_pad})"
                )
            if self.num_pipelines > self.width:
                raise ValueError(
                    f"MHA: num_pipelines ({self.num_pipelines}) is at most the "
                    f"{self.width} columns it is placed on"
                )
            return
        if not self.packed and self.seq_pad % (64 * self.num_pipelines):
            raise ValueError(
                f"MHA: seq_pad ({self.seq_pad}) must be whole rounds of 64 rows on "
                f"each of num_pipelines ({self.num_pipelines})"
            )
        if self.kv_len % self.B_kv or self.kv_len < self.seq_pad:
            raise ValueError(
                f"MHA: kv_len ({self.kv_len}) must be whole {self.B_kv}-row blocks and "
                f"at least seq_pad ({self.seq_pad}): the queries are its last rows"
            )
        if self.kv_lanes != (self.num_pipelines if self.packed else 1):
            raise ValueError(
                f"MHA: kv_lanes ({self.kv_lanes}) is one per pipeline for one query, "
                f"else one; resolve() sets it"
            )
        if self.num_pipelines > self.width:
            raise ValueError(
                f"MHA: num_pipelines ({self.num_pipelines}) is at most the "
                f"{self.width} columns it is placed on, one pipeline a column"
            )
        if self.pv_cores > 1 and self.num_pipelines // self.q_shims > 4:
            raise ValueError(
                f"MHA: with P*V split, an O join serves at most 4 pipelines, not "
                f"{self.num_pipelines // self.q_shims}: its memtile also forwards "
                f"a pipeline's scores and P"
            )
        if self.packed:
            if self.pv_cores > 1:
                raise ValueError(
                    "MHA: one query packed reads K and V over its pipeline's own "
                    "shim, whose two channels leave V one lane: P*V takes one core"
                )
            group = self.num_heads // self.num_KV_heads
            if group > self.B_q:
                raise ValueError(
                    f"MHA: one query packs a KV group's {group} heads into a block's "
                    f"B_q ({self.B_q}) rows, which must hold them"
                )
            most = self.PACKED_PIPELINES[self.width]
            if self.num_pipelines > most or self.num_KV_heads % self.num_pipelines:
                raise ValueError(
                    f"MHA: one query takes num_pipelines ({self.num_pipelines}) at most "
                    f"{most} dividing num_KV_heads ({self.num_KV_heads}): each pipeline "
                    f"has its own K and V lanes"
                )

    @classmethod
    def fits(cls, dev) -> bool:
        """Whether ``dev`` has the columns of a layout MHA is placed on."""
        return dev.cols >= min(cls.PACKED_PIPELINES)

    def resolve(self, dev):
        if dev is not None and not self.fits(dev):
            raise Unresolvable(
                f"MHA is placed on {min(self.PACKED_PIPELINES)} columns or more; got "
                f"{dev.name} ({dev.arch}) with {dev.cols}"
            )
        if self.cores_per_block == 1:
            return self.resolve_fused(dev)
        B_q, pv_cores = self.B_q, self.pv_cores
        # Before any kernel is sized: mha.cc builds only 16-, 32- and 64-key blocks.
        if B_q is not None and 64 % B_q:
            raise ValueError(
                f"MHA: B_q ({B_q}) must divide 64, the block seq_pad is whole of"
            )
        if B_q is None or pv_cores is None:
            if dev is None:
                raise Unresolvable(
                    "MHA's block size and P*V cores follow the cores' memory; "
                    "none is bound and not both were given"
                )
            mem = dev.core_memory_bytes
            group = self.num_heads // self.num_KV_heads
            # Every row of a packed block is computed: the narrowest holding the group.
            blocks = (8, 16, 32, 64) if self.packed else (64, 32, 16)
            fit = next(
                (
                    (cores, b)
                    for cores in ((1, 2) if pv_cores is None else (pv_cores,))
                    for b in (blocks if B_q is None else (B_q,))
                    if self.core_bytes(dev, b, self.key_block(b, dev), cores) <= mem
                    and not (self.packed and B_q is None and group > b)
                ),
                None,
            )
            if fit is None and B_q is None:
                raise Unresolvable(
                    f"MHA at d={self.d}: no block of {min(blocks)} rows or more fits a "
                    f"core's {mem} bytes"
                )
            pv_cores, B_q = fit or (pv_cores or 1, B_q)
        B_kv = self.key_block(B_q, dev)
        q_shims = 2 if self.num_pipelines > 6 else 1
        if dev is not None:
            width = max(w for w in self.PACKED_PIPELINES if w <= dev.cols)
        else:
            width = max(self.PACKED_PIPELINES)
        if pv_cores > 1 and width not in self.SPLIT_COLUMNS:
            raise Unresolvable(
                f"MHA at d={self.d} splits P*V over two cores, which is placed "
                f"on {', '.join(map(str, self.SPLIT_COLUMNS))} columns, not {width}"
            )
        return self.replace(
            B_q=B_q,
            B_kv=B_kv,
            q_shims=q_shims,
            join_rows=B_q * (self.num_pipelines // q_shims),
            kv_lanes=self.num_pipelines if self.packed else 1,
            kv_streams=1 + pv_cores,
            width=width,
            pv_cores=pv_cores,
            pv_width=self.d // pv_cores,
            cores_per_block=3,
            fused=False,
            column_cores=3,
            group=1,
        )

    # Fused, the key block per head dimension, as today's pipeline takes it
    # on npu1, so the two mappings are one result (D5).
    FUSED_KEY_BLOCKS: ClassVar[dict[int, int]] = {64: 64, 128: 32, 256: 16}

    def resolve_fused(self, dev):
        """``resolve`` for one core a query block: every core of ``num_pipelines`` columns.

        A KV group's heads packed a position; ``B_q`` the widest block of whole
        positions dividing 64 whose core fits L1, unless given.

        Raises:
            Unresolvable: No device, not AIE2, K and V apart, one query, or no
                block fits.
        """
        if dev is None or dev.arch is not AIEArch.AIE2:
            raise Unresolvable(
                "MHA: one core a query block is mha.cc's attend_block, AIE2's"
            )
        if not self.kv_paired or self.packed or not self.heads_interleaved:
            raise Unresolvable(
                "MHA: one core a query block reads a paired KV, its heads interleaved, "
                "over more than one query"
            )
        if self.pv_cores not in (None, 1):
            raise Unresolvable("MHA: one core a query block takes P*V on that core")
        group = self.num_heads // self.num_KV_heads
        B_kv = self.FUSED_KEY_BLOCKS.get(self.d)
        if B_kv is None or self.kv_len % B_kv:
            raise Unresolvable(
                f"MHA: one core a query block takes d of "
                f"{', '.join(map(str, self.FUSED_KEY_BLOCKS))}, its key block dividing "
                f"kv_len ({self.kv_len}); got d={self.d}"
            )
        column_cores = len(dev.core_rows)
        cores = self.num_pipelines * column_cores
        blocks = (
            [self.B_q]
            if self.B_q is not None
            else [b for b in range(64, 7, -8) if not b % group]
        )
        fit = next(
            (
                b
                for b in blocks
                if not 64 % (b // group or 1)
                and not self.seq_pad % (b // group * cores)
                and self.fused_core_bytes(dev, b, B_kv) <= dev.core_memory_bytes
            ),
            None,
        )
        if fit is None:
            raise Unresolvable(
                f"MHA: no query block of whole positions of {group} heads fits a core's "
                f"{dev.core_memory_bytes} bytes and rounds of {cores} cores"
            )
        width = max(w for w in self.PACKED_PIPELINES if w <= dev.cols)
        return self.replace(
            B_q=fit,
            B_kv=B_kv,
            q_shims=self.num_pipelines,
            join_rows=fit * column_cores,
            kv_lanes=1,
            kv_streams=1,
            width=width,
            pv_cores=1,
            pv_width=self.d,
            cores_per_block=1,
            fused=True,
            column_cores=column_cores,
            group=group,
        )

    def fused_kernel(self, B_q: int, B_kv: int, group: int):
        """mha.cc's attend_block at a ``B_q`` x ``d`` x ``B_kv`` block, ``group`` heads a position."""
        return kernels.linalg.mha(
            B_q,
            self.d,
            B_kv,
            b_col_maj=True,
            fused=True,
            causal=self.causal,
            window=self.window or 0,
            group=group,
        )

    def fused_core_bytes(self, dev: Device, B_q: int, B_kv: int) -> int:
        """Return a fused core's L1 bytes: Q, two key blocks, O's two forms, S, P, state and stack."""
        d = self.d
        data = (
            2 * B_q * d  # Q, one block deep
            + 2 * 4 * B_kv * d  # K and V, two blocks deep
            + 2 * B_q * d  # O as it leaves
            + 4 * B_q * d  # O accumulating
            + 2 * 2 * B_q * B_kv  # S and P
            + 16 * B_q  # the online state
            + 12  # the block index
        )
        with set_current_device(dev), compile_context(_iron_kernel_registry=set()):
            frame = self.fused_kernel(
                B_q, B_kv, self.num_heads // self.num_KV_heads
            ).frame_bytes(resolve_target_arch(dev))
        return dev.default_core_stack_bytes + data + frame

    def seq_padding(self, seq_len: int) -> int:
        """``seq_len`` rounded up to 64; one query, packed, is not padded."""
        if seq_len == 1:
            return 1
        return ceildiv(seq_len, 64) * 64

    def key_block(self, B_q: int, dev: Device | None) -> int:
        """``B_kv`` for ``B_q``: itself, which mha.cc's causal skip compares by.

        Packed, the widest divisor of ``kv_len`` whose cores fit ``dev``
        (any, where None): the fewest key blocks a step.
        """
        if not self.packed:
            return B_q
        return next(
            (
                b
                for b in (64, 32, 16)
                if B_q <= b
                and not self.kv_len % b
                and (
                    dev is None
                    or self.core_bytes(dev, B_q, b, 1) <= dev.core_memory_bytes
                )
            ),
            B_q,
        )

    def core_bytes(self, dev: Device, B_q: int, B_kv: int, pv_cores: int) -> int:
        """Return the larger of a pipeline's QK^T and P*V cores' L1 bytes.

        Kernels' data and stack included, over the device's default stack.

        Args:
            dev: The device the cores' memory is measured against.
            B_q: The query block size.
            B_kv: The key/value block size.
            pv_cores: The P*V cores the head is split over.
        """
        d, pv_width = self.d, self.d // pv_cores
        arch = resolve_target_arch(dev)
        pv = 4 * B_q * B_kv + 4 * pv_width * B_kv + 6 * pv_width * B_q + 32 * B_q
        qk = (4 if pv_cores == 1 else 2) * d * B_q + 4 * d * B_kv + 4 * B_q * B_kv
        # Only measured, never built, so it stays out of the build's registry.
        # dev is bound because the factory reads its architecture from it.
        with set_current_device(dev), compile_context(_iron_kernel_registry=set()):
            qk_mha = self.mha_kernel(B_q, d, B_kv, dev.arch is AIEArch.AIE2p)
            pv_mha = qk_mha if pv_cores == 1 else self.mha_kernel(B_q, pv_width, B_kv)
            bind = pv_mha.object_file.bind
            pv += max(
                pv_mha.frame_bytes(arch, entry=bind(name).name)
                for name in ("matmul_PV", "rescale_O")
            )
            zero = kernels.zero(tile_size=(B_q, B_kv), dtype=bfloat16)
            # Summed, the two objects' stacks bound the deeper one from above.
            qk += qk_mha.frame_bytes(arch) + zero.frame_bytes(arch)
        return dev.default_core_stack_bytes + max(pv, qk)

    def mha_kernel(self, B_q: int, width: int, B_kv: int, accurate_exp2=False):
        """mha.cc at a ``B_q`` x ``width`` x ``B_kv`` block."""
        return kernels.linalg.mha(
            B_q,
            width,
            B_kv,
            b_col_maj=True,
            accurate_exp2=accurate_exp2,
            causal=self.causal,
            window=self.window or 0,
            # Unwindowed decode runs as it has, without mha.cc's packed path.
            packed=self.packed and self.window is not None,
        )

    def build(self) -> Built:
        if self.fused:
            return self.build_fused()
        of_depth = 2
        dtype = bfloat16
        B_q, B_kv, d = self.B_q, self.B_kv, self.d
        num_pipelines = self.num_pipelines
        n_join = num_pipelines // self.q_shims  # the pipelines on one shim
        # With P*V split, the two P*V cores share SPLIT_COLUMNS' own adjacent
        # tiles, the line between them shared L1, which no placer can infer;
        # otherwise aiecc's placer takes every tile.
        pv_cores, pv_width = self.pv_cores, self.pv_width
        split = pv_cores > 1

        # partial_softmax takes exp2, so the scale is in the log2 domain.
        inv_scale = float(bfloat16(self.scale * np.log2(np.e)))
        dev = self.dev
        if dev is None:
            raise Unresolvable("MHA: build() needs a bound device")
        # AIE2P's exp2 instruction is up to 6% high; AIE2 has none to replace.
        accurate_exp2 = dev.arch is AIEArch.AIE2p

        q_ty = np.ndarray[(B_q, d), np.dtype[dtype]]
        v_ty = np.ndarray[(B_kv, pv_width), np.dtype[dtype]]
        o_ty = np.ndarray[(B_q, pv_width), np.dtype[dtype]]
        qk_ty = np.ndarray[(B_q, B_kv), np.dtype[dtype]]
        s_ty = np.ndarray[(4 * B_q,), np.dtype[np.float32]]
        acc_ty = np.ndarray[(B_q, pv_width), np.dtype[np.float32]]

        # The rest bind from mha.cc's object: declared apart, each would
        # redefine it. Never on bfp16 macs: bfp16 shares an exponent over 8
        # keys of P*V, and the softmax bounds the time.
        matmul_QK = self.mha_kernel(B_q, d, B_kv, accurate_exp2)
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
                np.ndarray[(3,), np.dtype[np.int32]],
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
            else self.mha_kernel(B_q, pv_width, B_kv).object_file
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
                np.ndarray[(3,), np.dtype[np.int32]],
                np.int32,
            ],
        )
        rescale_O = pv_object.bind(
            "rescale_O",
            [acc_ty, o_ty, s_ty, np.int32, np.ndarray[(3,), np.dtype[np.int32]]],
        )

        # Each stream is blocked as the product that reads or writes it takes it.
        qk = matmul_QK.stream_dims
        pv = mm_stream_dims(
            B_q,
            B_kv,
            pv_width,
            kernels.linalg.mha.mac_dims(  # pyright: ignore[reportFunctionMemberAccess]
                pv=True
            ),
        )

        # Split, Q is one block deep: the QK core's L1 holds one d=512 block.
        q_depth = 1 if split else of_depth
        layout = MHA.SPLIT_COLUMNS[self.width] if split else None
        # Q and O are placed at the split layout's shim tiles; fifos()
        # returns the raw fifo, not an end, since each is split or joined
        # further below.
        inQ = self.Q.fifos(
            of_depth,
            tiles=[
                Tile(layout.q[s], 0) if layout is not None else AnyShimTile
                for s in range(self.q_shims)
            ],
        )
        memO = self.O.fifos(
            of_depth,
            tiles=[
                Tile(layout.o[s][h], 0) if layout is not None else AnyShimTile
                for s in range(self.q_shims)
                for h in range(pv_cores)
            ],
            to_stream=pv.C,
        )
        memQ = []
        outO = [[] for _ in range(pv_cores)]
        for shim in range(self.q_shims):
            memQ += (
                inQ[shim]
                .cons()
                .split(
                    offsets=[B_q * d * i for i in range(n_join)],
                    obj_types=[q_ty] * n_join,
                    to_stream=None if qk.A is None else [qk.A] * n_join,
                    depths=[q_depth] * n_join,
                    tile=Tile(layout.q[shim], 1) if layout is not None else AnyMemTile,
                )
            )
            for h in range(pv_cores):
                outO[h] += (
                    memO[shim * pv_cores + h]
                    .prod()
                    .join(
                        offsets=[B_q * pv_width * i for i in range(n_join)],
                        obj_types=[o_ty] * n_join,
                        # One O block: the PV core's L1 also holds its float32 O.
                        depths=[1] * n_join,
                        tile=(
                            Tile(layout.o[shim][h], 1)
                            if layout is not None
                            else AnyMemTile
                        ),
                    )
                )

        kv_lanes = self.kv_lanes
        k_tiles = [
            Tile(layout.k_shim, 0) if layout is not None else AnyShimTile
        ] * kv_lanes
        v_tiles = [
            Tile(layout.v[h], 0) if layout is not None else AnyShimTile
            for _ in range(kv_lanes)
            for h in range(pv_cores)
        ]
        if self.kv_paired:
            inK = [
                ObjectFifo(np.ndarray[(d, B_kv), np.dtype[dtype]], depth=of_depth)
                for _ in k_tiles
            ]
            inV = [ObjectFifo(v_ty, depth=of_depth) for _ in v_tiles]
            self.KV.bind(
                [
                    fifo.prod(tile=tile)
                    for lane in range(kv_lanes)
                    for fifo, tile in [
                        (inK[lane], k_tiles[lane]),
                        *zip(
                            inV[lane * pv_cores : (lane + 1) * pv_cores],
                            v_tiles[lane * pv_cores : (lane + 1) * pv_cores],
                        ),
                    ]
                ]
            )
        else:
            inK = self.K.fifos(of_depth, tiles=k_tiles)
            inV = self.V.fifos(of_depth, tiles=v_tiles)
        memK, memV = [], []
        for lane in range(kv_lanes):
            memK.append(
                inK[lane]
                .cons()
                .forward(
                    to_stream=qk.B,
                    tile=Tile(layout.k, 1) if layout is not None else AnyMemTile,
                    depth=of_depth,
                )
            )
            for h in range(pv_cores):
                memV.append(
                    inV[lane * pv_cores + h]
                    .cons()
                    .forward(
                        to_stream=pv.B,
                        tile=Tile(layout.v[h], 1) if layout is not None else AnyMemTile,
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
                    to_stream=qk.C,
                    depth=of_depth,
                    tile=Tile(i, 1) if split else AnyMemTile,
                )
            )
            memP.append(ObjectFifo(qk_ty, depth=of_depth))
            outP.append(
                memP[i]
                .cons()
                .forward(
                    to_stream=pv.A,
                    depth=of_depth,
                    tile=Tile(i, 1) if split else AnyMemTile,
                )
            )
            # A copy of the row state for each P*V core, which rescales its own.
            scaleOF.append([ObjectFifo(s_ty, depth=of_depth) for h in range(pv_cores)])

        # Q blocks past the bound pass through: Q and O stream every block.
        blocks = [
            self.heads,
            self.q_blocks_per_pipeline,
            self.q_blocks_valid,
            self.kv_blocks,
        ]

        def each_q_block(heads, q_blocks, q_valid, first, bias, idx, q_block):
            """``q_block(compute)`` over every head's Q blocks, those past the bound not computed.

            ``idx`` restarts at the head's first, ``first``'s block and row
            offset.
            """
            q_start, q_offset = first
            idx[2] = q_offset
            for _ in range_(heads):
                idx[0] = 0
                idx[1] = q_start + bias
                for _ in range_(q_valid):
                    q_block(True)
                for _ in range_(q_blocks - q_valid):
                    q_block(False)

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
            def q_block(compute: bool):
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
            first = words[self.q_start], words[self.q_offset]
            each_q_block(
                heads, q_blocks, q_valid, first, q_block_bias, idx_buffer, q_block
            )

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
            def q_block(compute: bool):
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
            s_q, s_kv = words[self.s_q], words[self.s_kv]
            first = words[self.q_start], words[self.q_offset]
            each_q_block(
                heads, q_blocks, q_valid, first, q_block_bias, idx_buffer, q_block
            )

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
            def q_block(compute: bool):
                if not compute:
                    of_o_out.acquire(1)  # a padding block of O: left as is
                    for _ in range_(loop_idx_kv):
                        of_p.acquire(1)
                        of_v.acquire(1)
                        of_scale.acquire(1)
                        of_p.release(1)
                        of_v.release(1)
                        of_scale.release(1)
                    of_o_out.release(1)
                    return
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

            words = rtp.read()
            heads, q_blocks, q_valid, loop_idx_kv = (words[v] for v in blocks)
            s_kv = words[self.s_kv]
            first = words[self.q_start], words[self.q_offset]
            each_q_block(
                heads, q_blocks, q_valid, first, q_block_bias, idx_buffer, q_block
            )

        first = [self.q_start, self.q_offset]
        qk_rtps = [Rtp([*blocks, *first]) for _ in range(num_pipelines)]
        softmax_rtps = [
            Rtp([*blocks, self.s_q, self.s_kv, *first]) for _ in range(num_pipelines)
        ]
        pv_rtps = [
            [Rtp([*blocks, self.s_kv, *first]) for _ in range(num_pipelines)]
            for _ in range(pv_cores)
        ]

        matmul_workers, softmax_workers, matmul_pv_workers = [], [], []
        for i in range(num_pipelines):
            idx_buffer_qk = Buffer(
                initial_value=np.zeros(shape=(3,), dtype=np.int32),
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
                    tile=Tile(i, 2) if split else AnyComputeTile,
                )
            )
            idx_buffer_softmax = Buffer(
                initial_value=np.zeros(shape=(3,), dtype=np.int32),
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
                    tile=Tile(i, 4) if split else AnyComputeTile,
                )
            )
            # Split, the halves sit either side of the softmax, whose row
            # state each reads from shared memory.
            for h in range(pv_cores):
                idx_buffer_pv = Buffer(
                    initial_value=np.zeros(shape=(3,), dtype=np.int32),
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
                        tile=Tile(i, 3 + 2 * h) if split else AnyComputeTile,
                    )
                )

        return Built(
            matmul_workers + softmax_workers + matmul_pv_workers,
            [*qk_rtps, *softmax_rtps, *(r for rtps in pv_rtps for r in rtps)],
        )

    def build_fused(self) -> Built:
        """One core a query block: ``column_cores`` cores a column, each attend_block over a KV head's every key block.

        Q split and O joined a column on its memtile; one K-and-V stream, tiled
        on a memtile, to every core. A round is a block a core, the cores in
        turn along the positions.
        """
        dtype = bfloat16
        B_q, B_kv, d = self.B_q, self.B_kv, self.d
        rows, cores = self.column_cores, self.streams
        inv_scale = float(bfloat16(self.scale * np.log2(np.e)))
        q_ty = np.ndarray[(B_q, d), np.dtype[dtype]]
        kv_ty = np.ndarray[(B_kv, 2 * d), np.dtype[dtype]]
        o_ty = np.ndarray[(B_q, d), np.dtype[dtype]]
        acc_ty = np.ndarray[(B_q, d), np.dtype[np.float32]]
        s_ty = np.ndarray[(B_q * B_kv,), np.dtype[dtype]]
        state_ty = np.ndarray[(4 * B_q,), np.dtype[np.float32]]
        idx_ty = np.ndarray[(3,), np.dtype[np.int32]]

        fused = self.fused_kernel(B_q, B_kv, self.group)
        obj = fused.object_file
        attend = obj.bind(
            "attend_block",
            [q_ty, kv_ty, acc_ty, s_ty, s_ty, state_ty, idx_ty, dtype] + [np.int32] * 2,
        )
        init = obj.bind("init_scale_buffer", [state_ty, np.int32])
        rescale = obj.bind("rescale_O", [acc_ty, o_ty, state_ty, np.int32, idx_ty])
        mac = (
            kernels.linalg.mha.mac_dims(  # pyright: ignore[reportFunctionMemberAccess]
                pv=False
            )
        )
        qk = mm_stream_dims(B_q, d, B_kv, mac, b_col_maj=True)
        pv = mm_stream_dims(B_q, B_kv, d, mac)

        inQ = self.Q.fifos(2, tiles=[AnyShimTile] * self.num_pipelines)
        memO = self.O.fifos(2, tiles=[AnyShimTile] * self.num_pipelines, to_stream=pv.C)
        memQ, outO = [], []
        for col in range(self.num_pipelines):
            memQ += (
                inQ[col]
                .cons()
                .split(
                    offsets=[B_q * d * k for k in range(rows)],
                    obj_types=[q_ty] * rows,
                    to_stream=[qk.A] * rows,
                    depths=[1] * rows,
                    tile=AnyMemTile,
                )
            )
            outO += (
                memO[col]
                .prod()
                .join(
                    offsets=[B_q * d * k for k in range(rows)],
                    obj_types=[o_ty] * rows,
                    depths=[1] * rows,
                    tile=AnyMemTile,
                )
            )
        inKV = ObjectFifo(kv_ty, depth=2)
        self.KV.bind([inKV.prod(tile=AnyShimTile)])
        tiled = fused.contract.layouts[1].stream
        memKV = inKV.cons().forward(to_stream=tiled, depth=2, tile=AnyMemTile)

        groups = [
            (self.rounds_0, self.kv_blocks_0),
            (self.rounds_1, self.kv_blocks_1),
            (self.rounds_2, self.kv_blocks_2),
            (self.rounds_3, self.kv_blocks_3),
        ]
        values = [
            self.heads,
            self.s_q,
            self.s_kv,
            self.q_start,
            self.q_offset,
            *(v for group in groups for v in group),
        ]

        def core(of_q, of_kv, of_o, attend, init, rescale, first, rtp, *bufs):
            idx, acc, s, p, state = bufs
            words = rtp.read()
            heads, s_q, s_kv, q_start, q_offset = (words[v] for v in values[:5])
            idx[2] = q_offset
            for _ in range_(heads):
                idx[1] = q_start + first
                for rounds, blocks in groups:
                    kv_blocks = words[blocks]
                    for _ in range_(words[rounds]):
                        q = of_q.acquire(1)
                        init(state, B_q)
                        idx[0] = 0
                        for _ in range_(kv_blocks):
                            attend(
                                q,
                                of_kv.acquire(1),
                                acc,
                                s,
                                p,
                                state,
                                idx,
                                inv_scale,
                                s_q,
                                s_kv,
                            )
                            of_kv.release(1)
                            idx[0] += 1
                        rescale(acc, of_o.acquire(1), state, B_q, idx)
                        of_o.release(1)
                        of_q.release(1)
                        idx[1] += cores

        rtps = [Rtp(values) for _ in range(cores)]
        workers = [
            Worker(
                core,
                fn_args=[
                    memQ[c].cons(),
                    memKV.cons(),
                    outO[c].prod(),
                    attend,
                    init,
                    rescale,
                    c,
                    rtps[c],
                    Buffer(initial_value=np.zeros(3, np.int32)),
                    Buffer(acc_ty),
                    Buffer(s_ty),
                    Buffer(s_ty),
                    Buffer(state_ty),
                ],
                tile=AnyComputeTile,
            )
            for c in range(cores)
        ]
        return Built(workers, rtps)

    def ops(self) -> int:
        """Q K^T and its product with V per head, over the keys each query keeps."""
        keys = self.kv_len - self.seq_pad + self.seq_len
        position = keys - self.seq_len + np.arange(self.seq_len)
        ahead = 0 if self.causal else (self.window or keys)
        lo = np.maximum(position - self.window, 0) if self.window else 0
        hi = np.minimum(position + ahead, keys - 1)
        return 4 * self.num_heads * self.d * int((hi - lo + 1).sum())

    def reference(self, Q, *kv, s_q=None, s_kv=None):
        """Attention per head of ``Q`` over K and V (``kv``, or ``KV``'s halves), the queries the keys' last rows.

        Query rows from ``s_q`` on are zeros and keys from ``s_kv`` on are
        masked.
        """
        if self.heads_interleaved:
            Q = np.swapaxes(Q, 0, 1)
        if self.kv_paired:
            (KV,) = kv
            K, V = (np.swapaxes(KV[:, :, x], 0, 1) for x in (0, 1))
        elif self.kv_interleaved:
            K, V = (np.swapaxes(t, 0, 1) for t in kv)
        else:
            K, V = kv
        groups = self.num_heads // self.num_KV_heads
        # The keys before the first query: those not in Q's padding, or a
        # bounded call's.
        offset = self.kv_tokens - self.q_tokens
        start = offset if self.causal or self.window else 0
        s_q = start + self.q_tokens if s_q is None else int(s_q)
        s_kv = self.kv_tokens if s_kv is None else int(s_kv)
        K, V = K[:, :s_kv], V[:, :s_kv]
        rows = max(s_q - start, 0)
        q = Q[:, :rows].astype(np.float32)
        k, v = (t.astype(np.float32) for t in (K, V))
        key = np.arange(k.shape[1])
        scale = np.float32(self.scale)
        out = np.zeros(Q.shape, dtype=Q.dtype)
        # A block of query rows at a time, its scores, mask and exponentials
        # 64 MiB each at any context, where all rows' are GiBs at 128K keys.
        step = max(1, 2**24 // max(k.shape[1], 1))
        for first in range(0, rows, step):
            block = slice(first, min(first + step, rows))
            position = offset + np.arange(block.start, block.stop)[:, None]
            masked = np.zeros((len(position), k.shape[1]), dtype=bool)
            if self.causal or self.window:
                # The enclosing "if" means self.window is set whenever not causal.
                masked |= key > position + (0 if self.causal else (self.window or 0))
            if self.window:
                masked |= key < position - self.window
            mask = np.where(masked, -np.inf, 0).astype(np.float32)
            for h in range(q.shape[0]):
                scores = q[h, block] @ k[h // groups].T * scale + mask
                e = np.exp(scores - scores.max(axis=-1, keepdims=True))
                out[h, block] = (e / e.sum(axis=-1, keepdims=True)) @ v[h // groups]
        if self.heads_interleaved:
            return np.ascontiguousarray(np.swapaxes(out, 0, 1))
        return out

    def tolerance(self) -> Tolerance:
        return Tolerance(
            rtol=0.04,
            atol=0.15,
            max_mismatch_frac=0.005,
            note="rtol about the softmax contract's aie::exp2 envelope (0.035 "
            "of |a| + |b|); atol and the 0.5% left to mismatch are set by hand, "
            "not derived",
        )

    def fused_rows(self, operand: Operand, kv_head: int, col: int, heads: int = 1):
        """Q's or O's rows column ``col``'s cores take of ``heads`` KV heads from ``kv_head``, every round.

        A KV group's heads a position, the cores' blocks in turn.
        """
        P, g, rows, cores = self.positions, self.group, self.column_cores, self.streams
        H, d = self.num_heads, self.d
        rounds = self.seq_pad // (P * cores)
        sizes = [rounds, rows * P, g * d]
        strides = [cores * P * H * d, H * d, 1]
        if heads > 1:
            sizes, strides = [heads, *sizes], [g * d, *strides]
        return TensorAccessPattern(
            operand.shape, (col * rows * P * H + kv_head * g) * d, sizes, strides
        )

    def fused_keys(self, kv_head: int, reads: int, blocks: int):
        """KV's first ``blocks`` key blocks of ``kv_head``, read ``reads`` times: a key's K row then its V row."""
        G, d, B = self.num_KV_heads, self.d, self.B_kv
        return TensorAccessPattern(
            self.KV.shape,
            kv_head * 2 * d,
            [reads, blocks, B, 2 * d],
            [0, B * G * 2 * d, G * 2 * d, 1],
        )

    def fused_key_fills(self) -> list[tuple[int, TensorAccessPattern, Value | None]]:
        """Return each KV fill, fused, in order: ``(kv_head, tap, length_parameter)``.

        One a group of rounds, split at a descriptor's iterations. Bounded per
        call, each pattern is sized for every key, its group's length patched
        down.
        """
        dev = self.dev
        if dev is None:
            raise Unresolvable("MHA: the key fills need a bound device")
        iterations = 1 << dev.get_dma_bd_iter_bits(0, 0)
        values = [
            self.kv_blocks_0,
            self.kv_blocks_1,
            self.kv_blocks_2,
            self.kv_blocks_3,
        ]
        fills = []
        for kv_head in range(self.num_KV_heads):
            for g, rounds in enumerate(self.round_groups):
                length = values[g] if values[g].per_call else None
                blocks = (
                    ceildiv(self.kv_tokens, self.B_kv)
                    if length is not None
                    else self.group_blocks(g)
                )
                for first in range(0, len(rounds), iterations):
                    reads = min(iterations, len(rounds) - first)
                    fills.append(
                        (kv_head, self.fused_keys(kv_head, reads, blocks), length)
                    )
        return fills

    def sequence(self, rt):
        """One descriptor set per KV group.

        K and V re-read per (head, block) from the iteration slot, not six
        descriptors per block.
        """
        if self.fused:
            fills = self.fused_key_fills()
            for kv_head in range(self.num_KV_heads):
                tg = rt.task_group()
                for col in range(self.num_pipelines):
                    self.Q.fill(
                        self.fused_rows(self.Q, kv_head, col), lane=col, group=tg
                    )
                # As below, O drains before the keys fill.
                for col in range(self.num_pipelines):
                    self.O.drain(
                        self.fused_rows(self.O, kv_head, col),
                        lane=col,
                        group=tg,
                        wait=True,
                    )
                for head, tap, length in fills:
                    if head == kv_head:
                        self.KV.fill(
                            tap,
                            group=tg,
                            length_parameter=length,
                            length_unit=2 * self.B_kv * self.d,
                        )
                rt.finish(tg)
            return
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

        def kv_rows(x, kv_head, reads):
            """K's (``x`` 0) or V's (1) blocks of ``kv_head``, read ``reads`` times."""
            if self.kv_paired:
                head = TensorAccessPattern.full(self.KV.shape)[:, kv_head, x]
            else:
                head = by_head((self.K, self.V)[x], self.kv_interleaved)[kv_head]
            return head[: kv_blocks * B_kv].split(0, B_kv).repeat(reads)

        def kv_fill(x, tap, p, h, group):
            """Fill pipeline lane ``p``'s K (``x`` 0) or its V share ``h`` (1)."""
            if self.kv_paired:
                operand = self.KV
                lane = p * self.kv_streams + (1 + h if x else 0)
            else:
                operand = (self.K, self.V)[x]
                lane = p * self.pv_cores + h if x else p
            operand.fill(
                tap,
                lane=lane,
                group=group,
                length_parameter=kv_valid,
                length_unit=B_kv * (self.pv_width if x else self.d),
            )

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
                (stride0,) = concrete(first.strides[:1], first)
                both = TensorAccessPattern(
                    first.tensor_dims,
                    first.offset,
                    (2, *first.sizes),
                    ((group - width) * stride0, *first.strides),
                )
                return both.coalesce().repeat(self.B_q // (2 * width))

            for step in range(steps):
                owned = [p * steps + step for p in range(self.num_pipelines)]
                tg = rt.task_group()
                for kv_head in owned:
                    self.Q.fill(packed_rows(self.Q, kv_head), lane=0, group=tg)
                for p, kv_head in enumerate(owned):
                    for x in (0, 1):
                        kv_fill(x, kv_rows(x, kv_head, 1), p, 0, tg)
                for kv_head in owned:
                    self.O.drain(
                        packed_rows(self.O, kv_head), lane=0, group=tg, wait=True
                    )
                rt.finish(tg)
            return

        cores, pv_width = self.pv_cores, self.pv_width
        dev = self.dev
        if dev is None:
            raise Unresolvable("MHA: sequence() needs a bound device")
        # A shim descriptor's iteration count.
        iterations = 1 << dev.get_dma_bd_iter_bits(0, 0)
        for kv_head in range(kv_heads):
            head0 = kv_head * group
            tg = rt.task_group()
            for shim in range(self.q_shims):
                self.Q.fill(q_rows(self.Q, head0, shim), lane=shim, group=tg)
            # O drains before K and V fill: past the queue's depth a fill
            # waits for a free slot, which the cores free only while O drains.
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
            # A bounded pattern is one descriptor: re-reads at most the slot's count.
            reads = group * blocks
            for first in range(0, reads, iterations):
                count = min(iterations, reads - first)
                kv_fill(0, kv_rows(0, kv_head, count), 0, 0, tg)
                for h in range(cores):
                    share = kv_rows(1, kv_head, count)
                    kv_fill(1, share[..., h * pv_width : (h + 1) * pv_width], 0, h, tg)
            rt.finish(tg)

    def lane_transfers(self, operand: Operand) -> LaneTransfers | None:
        """Q and O stream every row whatever ``kv_valid`` bounds (the rationale in AGENTS.md: a bound limits compute, not their DMA).

        So their order follows only the static shape; K and V move only the blocks a
        bound reaches, so their order carries ``kv_blocks`` as a ``length_parameter``.
        """
        if operand.name not in ("Q", "O", "K", "V", "KV"):
            return None
        if self.fused:
            if operand.name == "KV":
                # One lane, a pattern a fill in turn: its groups' lengths differ.
                unit = 2 * self.B_kv * self.d
                return [
                    (0, tap, length, unit) for _, tap, length in self.fused_key_fills()
                ]
            return [
                (col, self.fused_rows(operand, 0, col, self.num_KV_heads), None, None)
                for col in range(self.num_pipelines)
            ]

        def by_head(shape, interleaved):
            tap = TensorAccessPattern.full(shape)
            return tap.permute((1, 0, 2)) if interleaved else tap

        def insert_repeat(tap, axis, count):
            sizes = [*tap.sizes[:axis], count, *tap.sizes[axis:]]
            strides = [*tap.strides[:axis], 0, *tap.strides[axis:]]
            return TensorAccessPattern(tap.tensor_dims, tap.offset, sizes, strides)

        rows = self.join_rows
        if operand is self.Q or operand is self.O:
            if self.packed:
                group = self.num_heads // self.num_KV_heads
                steps = self.num_KV_heads // self.num_pipelines
                width = 1 << (group.bit_length() - 1)
                # The num_heads axis, one KV group (its packed block) at a
                # time, reindexed (step, pipeline) in the order the sequence
                # visits them.
                base = by_head(operand.shape, self.heads_interleaved)[:, 0]
                by_step_p = base.split(0, group).split(0, steps).permute((1, 0, 2, 3))
                if width == group:
                    tap = insert_repeat(by_step_p, 2, self.B_q // group)
                else:
                    (s,) = concrete((by_step_p.strides[2],), by_step_p)
                    both = TensorAccessPattern(
                        by_step_p.tensor_dims,
                        by_step_p.offset,
                        [*by_step_p.sizes[:2], 2, width, by_step_p.sizes[3]],
                        [
                            *by_step_p.strides[:2],
                            (group - width) * s,
                            s,
                            by_step_p.strides[3],
                        ],
                    )
                    tap = insert_repeat(both, 2, self.B_q // (2 * width))
                return [(0, tap, None, None)]
            full = by_head(operand.shape, self.heads_interleaved).split(
                1, self.q_shims * rows
            )
            if operand is self.O:
                pv_width = self.pv_width
                return [
                    (
                        shim * self.pv_cores + h,
                        full[:, :, shim * rows : (shim + 1) * rows][
                            ..., h * pv_width : (h + 1) * pv_width
                        ],
                        None,
                        None,
                    )
                    for shim in range(self.q_shims)
                    for h in range(self.pv_cores)
                ]
            return [
                (shim, full[:, :, shim * rows : (shim + 1) * rows], None, None)
                for shim in range(self.q_shims)
            ]

        # K, V or KV: K's (x 0) and V's (1) blocks for each pipeline lane,
        # laned as sequence() fills them.
        kv_blocks = ceildiv(self.kv_tokens, self.B_kv)
        length_parameter = self.kv_blocks if self.kv_blocks.per_call else None
        group = self.num_heads // self.num_KV_heads
        steps = self.num_KV_heads // self.num_pipelines
        blocks = ceildiv(self.seq_pad, rows * self.q_shims)
        pv_width = self.pv_width
        heads = {}
        for x in (0, 1) if self.kv_paired else (int(operand.name == "V"),):
            if self.kv_paired:
                full = TensorAccessPattern.full(operand.shape)[:, :, x]
                full = full.permute((1, 0, 2))
            else:
                full = by_head(operand.shape, self.kv_interleaved)
            heads[x] = full[:, : kv_blocks * self.B_kv].split(1, self.B_kv)
        out = []
        for p in range(self.kv_lanes):
            for x, full in heads.items():
                if self.packed:
                    shares = [full[p * steps : (p + 1) * steps]]
                else:
                    tap = insert_repeat(full, 1, group * blocks)
                    shares = [tap]
                    if x:
                        shares = [
                            tap[..., h * pv_width : (h + 1) * pv_width]
                            for h in range(self.pv_cores)
                        ]
                for h, tap in enumerate(shares):
                    if self.kv_paired:
                        lane = p * self.kv_streams + (1 + h if x else 0)
                    else:
                        lane = p * self.pv_cores + h if x else p
                    unit = self.B_kv * (pv_width if x else self.d)
                    out.append((lane, tap, length_parameter, unit))
        return out
