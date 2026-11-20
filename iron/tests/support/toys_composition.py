# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Toys the composition-contract tuning tests (``iron/tests/tuning/``) share.

Small, real IRON operators recorded as runs of steps (``iron/tests/support/sequences.py``,
as ``iron/tests/support/fusable.py`` does), the profile-layer trees
(``iron.common.declare.composition``) a composition transformation is named in, and
``has_worker_group``, the assertion a worker-placement test makes of them.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron import Precision
from iron.common.declare.composition import (
    Configuration,
    Entry,
    Hold,
    Member,
    Region,
)
from iron.common.declare.composition import Edge as CompositionEdge
from iron.common.graph.record import Recording
from iron.common.image.step import EdgeKind
from iron.operators import (
    AXPY,
    GEMM,
    GEMV,
    MHA,
    Decode,
    ElementwiseAdd,
    ElementwiseMul,
    RMSNorm,
    RoPE,
    SelectiveScan,
    SiLU,
    Softmax,
)
from iron.operators.copy import Copy
from iron.tests.support import fusable, sequences
from iron.tests.support.toys_edges import member


def has_worker_group(
    node: Entry | Configuration | Region | Member, size: int = 2
) -> bool:
    """Whether ``node`` places ``size`` or more parts on one worker, anywhere inside it."""
    if isinstance(node, Entry):
        return has_worker_group(node.root, size)
    if isinstance(node, Configuration):
        return any(has_worker_group(part, size) for part in node.parts)
    if isinstance(node, Region):
        return any(len(worker) >= size for worker in node.workers) or any(
            has_worker_group(part, size) for part in node.parts
        )
    return False


def decode_attention_ops(
    kv_len: int = 128, head_dim: int = 64, rows: int = 32
) -> tuple[GEMV, Softmax, GEMV]:
    """Return decode MHA's graph, small: ``K . q -> Softmax -> V^T . p``, its scores float32 into the softmax.

    ``rows`` packs several query rows (as decode packs a KV group's heads) so ``Softmax``
    meets its row count's multiple-of-16 rule at a size small enough to toy with: each
    GEMV a batch a row, its one matrix shared (``repeat``).
    """
    qk = GEMV(
        M=kv_len,
        K=head_dim,
        num_batches=rows,
        repeat=rows,
        tile_size_input=4,
        tile_size_output=32,
        output_dtype=np.float32,
    )
    softmax = Softmax(rows=rows, cols=kv_len, input_dtype=np.float32)
    pv = GEMV(
        M=head_dim,
        K=kv_len,
        num_batches=rows,
        repeat=rows,
        tile_size_input=4,
        tile_size_output=32,
    )
    return qk, softmax, pv


def decode_attention_recording(
    name: str, qk: GEMV, softmax: Softmax, pv: GEMV
) -> Recording:
    """Return the recording of decode's graph: ``qk``'s ``C`` into ``softmax``'s ``x``, its ``y`` into ``pv``'s ``B``."""
    steps = sequences.steps(
        (qk, "K", "q", "scores"), (softmax, "scores", "p"), (pv, "V", "p", "out")
    )
    return Recording.of_steps(name, steps, ["K", "q", "V"], ["out"])


def prefill_attention_ops(
    seq: int = 32, kv_len: int = 128, head_dim: int = 64, scores: Any = bfloat16
) -> tuple[GEMM, ElementwiseAdd, Softmax, GEMM]:
    """Return prefill MHA's graph, small: ``Q K^T -> + causal mask -> Softmax -> P . V``, its scores of type ``scores`` up to the softmax."""
    qk = GEMM(
        M=seq,
        K=head_dim,
        N=kv_len,
        b_col_maj=True,
        precision=Precision.MEDIUM,
        output_dtype=scores,
    )
    add_mask = ElementwiseAdd(size=seq * kv_len, tile_size=kv_len, dtype=scores)
    softmax = Softmax(rows=seq, cols=kv_len, input_dtype=scores)
    pv = GEMM(M=seq, K=kv_len, N=head_dim, b_col_maj=True, precision=Precision.MEDIUM)
    return qk, add_mask, softmax, pv


def prefill_scores_recording(
    name: str, qk: GEMM, add_mask: ElementwiseAdd, softmax: Softmax
) -> Recording:
    """Return the recording of prefill's graph up to the softmax: ``Q K^T -> + causal mask -> Softmax``."""
    steps = sequences.steps(
        (qk, "Q", "Kt", "scores"),
        (add_mask, "scores", "mask", "masked"),
        (softmax, "masked", "p"),
    )
    return Recording.of_steps(name, steps, ["Q", "Kt", "mask"], ["p"])


def prefill_scores_region(
    qk: GEMM, add_mask: ElementwiseAdd, softmax: Softmax
) -> Region:
    """Return ``prefill_scores_recording``'s steps as one region: QK^T's column halves staged into the mask add's rows, which stream into the softmax."""
    return Region(
        parts=(member(qk), member(add_mask), member(softmax)),
        edges=(
            CompositionEdge(0, "C", 1, "a", kind=EdgeKind.STAGED),
            CompositionEdge(1, "y", 2, "x"),
        ),
    )


def prefill_attention_recording(
    name: str, qk: GEMM, add_mask: ElementwiseAdd, softmax: Softmax, pv: GEMM
) -> Recording:
    """Return the recording of prefill's graph, the causal mask added before the softmax."""
    steps = sequences.steps(
        (qk, "Q", "Kt", "scores"),
        (add_mask, "scores", "mask", "masked"),
        (softmax, "masked", "p"),
        (pv, "p", "V", "out"),
    )
    return Recording.of_steps(name, steps, ["Q", "Kt", "mask", "V"], ["out"])


def axpy_ops(
    size: int = 2048, tile: int = 256
) -> tuple[ElementwiseMul, ElementwiseAdd]:
    """Return AXPY's graph, ``a * x`` then ``+ y``."""
    mul = ElementwiseMul(size=size, tile_size=tile)
    add = ElementwiseAdd(size=size, tile_size=tile)
    return mul, add


def axpy_recording(name: str, mul: ElementwiseMul, add: ElementwiseAdd) -> Recording:
    """Return the recording of ``mul`` into ``add``, ``mul``'s ``y`` and ``add``'s ``a`` both ``mid``."""
    steps = sequences.steps((mul, "a", "x", "mid"), (add, "mid", "y", "out"))
    return Recording.of_steps(name, steps, ["a", "x", "y"], ["out"])


# ------------------------------------------------- monolithic operators these graphs replace


def decode_attention_operator(
    kv_len: int = 128, head_dim: int = 64, rows: int = 32
) -> MHA:
    """Return the fused ``MHA`` decode's graph of ``GEMV``, ``Softmax`` and ``GEMV`` replaces, at the same sizes."""
    return MHA(
        num_heads=rows,
        num_KV_heads=1,
        d=head_dim,
        seq_len=1,
        kv_len=kv_len,
        heads_interleaved=True,
    )


def decode_attention_operator_recording(name: str, mha: MHA) -> Recording:
    """Return the recording of ``mha`` alone, decode's fused replacement for its graph."""
    steps = sequences.steps((mha, "Q", "K", "V", "out"))
    return Recording.of_steps(name, steps, ["Q", "K", "V"], ["out"])


class PrefillAttention(iron.Graph):
    """Prefill MHA's graph over the fused ``MHA``'s own ``Q``, ``K`` and ``V``: ``(Q * scale) K^T + causal mask -> Softmax -> P V``.

    One head with no padded rows. ``mha``'s scale is a power of two, so
    scaling ``Q`` on chip first is exact; the mask is its causal one, the
    queries the keys' last rows, held as a weight. Its scores are of type
    ``scores`` up to the softmax. Both matmuls sum in f32 at ``HIGHEST``, as
    the MHA does (it never takes bfp16 macs). The mask add and the softmax
    take two columns each, so the four steps fit npu1's 16 cores together.
    """

    def __init__(self, mha: MHA, scores: Any = bfloat16):
        seq, keys, d = mha.seq_len, mha.kv_len, mha.d
        self.sizes, self.scores = (seq, keys, d), scores
        self.scale = iron.param(np.full(seq * d, mha.scale, dtype=bfloat16))
        position = keys - seq + np.arange(seq)[:, None]
        causal = np.where(np.arange(keys) > position, -np.inf, 0)
        self.mask = iron.param(causal.astype(scores).reshape(-1))

    def body(self, Q, K, V):
        seq, keys, d = self.sizes
        q = ElementwiseMul.step(Q.reshape(seq * d), self.scale)
        scores = GEMM.step(
            q.reshape(seq, d),
            K.reshape(keys, d),
            b_col_maj=True,
            precision=Precision.HIGHEST,
            output_dtype=self.scores,
        )
        masked = ElementwiseAdd.step(
            scores.reshape(seq * keys),
            self.mask,
            tile_size=keys,
            dtype=self.scores,
            num_aie_columns=2,
        )
        p = Softmax.step(
            masked.reshape(seq, keys), input_dtype=self.scores, num_aie_columns=2
        )
        out = GEMM.step(p, V.reshape(keys, d), precision=Precision.HIGHEST)
        return out.reshape(1, seq, d)


def prefill_attention_graph(
    mha: MHA, scores: Any = bfloat16
) -> tuple[Recording, Region]:
    """Return ``PrefillAttention``'s recording at ``mha``'s inputs, and its four attention steps as one region.

    QK^T's scores staged into the mask add, its rows streamed into the
    softmax, whose rows are staged into P V's tiles; the scaling of Q runs
    on its own.
    """
    recording = PrefillAttention(mha, scores).record(
        **{b.name: tuple(b.shape) for b in mha.resolved().inputs}
    )
    region = Region(
        parts=tuple(member(step.op) for step in recording.steps[1:]),
        edges=(
            CompositionEdge(0, "C", 1, "a", kind=EdgeKind.STAGED),
            CompositionEdge(1, "y", 2, "x"),
            CompositionEdge(2, "y", 3, "A", kind=EdgeKind.STAGED),
        ),
    )
    return recording, region


def prefill_attention_operator(
    seq: int = 32, kv_len: int = 128, head_dim: int = 64
) -> MHA:
    """Return the fused ``MHA`` prefill's graph of ``GEMM``, add, ``Softmax`` and ``GEMM`` replaces, at the same sizes."""
    return MHA(num_heads=1, d=head_dim, seq_len=seq, kv_len=kv_len)


def prefill_attention_operator_recording(name: str, mha: MHA) -> Recording:
    """Return the recording of ``mha`` alone, prefill's fused replacement for its graph."""
    steps = sequences.steps((mha, "Q", "K", "V", "out"))
    return Recording.of_steps(name, steps, ["Q", "K", "V"], ["out"])


def axpy_operator(
    size: int = 2048, tile: int = 256, scalar_factor: float = 3.0
) -> AXPY:
    """Return the ``AXPY`` operator the mul-then-add graph replaces, ``scalar_factor`` the value held constant in the graph's ``a``."""
    return AXPY(size=size, tile_size=tile, scalar_factor=scalar_factor)


def axpy_operator_recording(name: str, axpy: AXPY) -> Recording:
    """Return the recording of ``axpy`` alone on the graph's ``x`` and ``y``: ``out = scalar_factor * x + y``."""
    steps = sequences.steps((axpy, "x", "y", "out"))
    return Recording.of_steps(name, steps, ["x", "y"], ["out"])


# ----------------------------------------------------------------- two actors, one core


def gemv_silu_pair(M: int = 64) -> tuple[GEMV, SiLU]:
    """Return a projection and the gate activation it feeds (the fold hook's ``GEMV -> SiLU``)."""
    gemv = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=32)
    silu = SiLU(size=M, tile_size=32)
    return gemv, silu


def gemv_silu_recording(name: str, gemv: GEMV, silu: SiLU) -> Recording:
    """Return the recording of ``gemv``'s ``C`` feeding ``silu``'s ``x``."""
    steps = sequences.steps((gemv, "A", "B", "mid"), (silu, "mid", "out"))
    return Recording.of_steps(name, steps, ["A", "B"], ["out"])


def decode_gemv_pair(M: int = 256, K: int = 192) -> tuple[Decode, GEMV]:
    """Return a coded-weight decode step feeding the projection it codes for (the decode hook)."""
    decode = Decode(M=M, K=K, rows=2)
    gemv = GEMV(M=M, K=K, tile_size_input=4, tile_size_output=32)
    return decode, gemv


def decode_gemv_recording(name: str, decode: Decode, gemv: GEMV) -> Recording:
    """Return the recording of ``decode``'s ``out`` feeding ``gemv``'s ``A``."""
    steps = sequences.steps((decode, "A", "mid"), (gemv, "mid", "B", "out"))
    return Recording.of_steps(name, steps, ["A", "B"], ["out"])


def add_softmax_pair(rows: int = 32, cols: int = 64) -> tuple[ElementwiseAdd, Softmax]:
    """Return a causal-mask add feeding the softmax it was pre-added for (the mask-addend hook)."""
    add = ElementwiseAdd(size=rows * cols, tile_size=cols)
    softmax = Softmax(rows=rows, cols=cols)
    return add, softmax


def add_softmax_recording(
    name: str, add: ElementwiseAdd, softmax: Softmax
) -> Recording:
    """Return the recording of ``add``'s ``y`` feeding ``softmax``'s ``x``."""
    steps = sequences.steps((add, "a", "b", "mid"), (softmax, "mid", "out"))
    return Recording.of_steps(name, steps, ["a", "b"], ["out"])


def rmsnorm_mul_pair(rows: int = 1, size: int = 64) -> tuple[RMSNorm, ElementwiseMul]:
    """Return a norm feeding the weight-row multiply it was pre-multiplied for."""
    rms = RMSNorm(rows=rows, tile_size=size, num_aie_columns=1)
    mul = ElementwiseMul(size=size, tile_size=size)
    return rms, mul


def rmsnorm_mul_recording(name: str, rms: RMSNorm, mul: ElementwiseMul) -> Recording:
    """Return the recording of ``rms``'s ``y`` feeding ``mul``'s ``a``."""
    steps = sequences.steps((rms, "x", "mid"), (mul, "mid", "w", "out"))
    return Recording.of_steps(name, steps, ["x", "w"], ["out"])


PAIR_TOYS = {
    "gemv_silu": (gemv_silu_pair, gemv_silu_recording, "C", "x"),
    "decode_gemv": (decode_gemv_pair, decode_gemv_recording, "out", "A"),
    "add_softmax": (add_softmax_pair, add_softmax_recording, "y", "x"),
    "rmsnorm_mul": (rmsnorm_mul_pair, rmsnorm_mul_recording, "y", "a"),
}


def fan_in_recording(name: str, M: int = 64) -> Recording:
    """Return two producers (``gate``, ``up``) read by one consumer (``Mul``), both on its core."""
    gate = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=32)
    up = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=32)
    mul = ElementwiseMul(size=M, tile_size=32)
    steps = sequences.steps(
        (gate, "Wg", "x", "g"), (up, "Wu", "x", "u"), (mul, "g", "u", "out")
    )
    return Recording.of_steps(name, steps, ["Wg", "Wu", "x"], ["out"])


def fan_out_recording(name: str, M: int = 64) -> Recording:
    """Return one producer read by two consumers, each a candidate for the producer's core."""
    gemv = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=32)
    add = ElementwiseAdd(size=M, tile_size=32)
    silu = SiLU(size=M, tile_size=32)
    steps = sequences.steps(
        (gemv, "A", "B", "mid"), (add, "mid", "r", "out1"), (silu, "mid", "out2")
    )
    return Recording.of_steps(name, steps, ["A", "B", "r"], ["out1", "out2"])


def partner_and_outside_recording(name: str, M: int = 2048) -> Recording:
    """Return a consumer with one input from its core partner and another from outside (the residual add)."""
    gemv, add = fusable.gemv_add(M, M)
    return fusable.gemv_add_recording(name, gemv, add)


def gemv_add_recording(
    name: str, M: int = 2048, K: int = 2048, repeat: int = 1
) -> Recording:
    """Return a projection and its residual add, the projection's ``repeat`` given explicitly.

    ``repeat`` must divide ``num_batches``, so a ``repeat`` past 1 takes
    ``num_batches`` equal to it: one shared matrix of A over that many
    batches, the add over every batch's output.
    """
    gemv = GEMV(
        M=M,
        K=K,
        tile_size_input=4,
        tile_size_output=256,
        repeat=repeat,
        num_batches=None if repeat == 1 else repeat,
    )
    add = ElementwiseAdd(size=M * repeat, tile_size=256)
    steps = sequences.steps((gemv, "A", "B", "mid"), (add, "r", "mid", "out"))
    return Recording.of_steps(name, steps, ["A", "B", "r"], ["out"])


def output_also_read_outside_recording(name: str, M: int = 64) -> Recording:
    """Return a producer whose output feeds a partner on its core and is itself a graph output."""
    silu = SiLU(size=M, tile_size=32)
    mul = ElementwiseMul(size=M, tile_size=32)
    steps = sequences.steps((silu, "x", "mid"), (mul, "mid", "up", "out"))
    return Recording.of_steps(name, steps, ["x", "up"], ["mid", "out"])


def multi_output_recording(
    name: str, rows: int = 1, heads: int = 4, head_dim: int = 16, state_size: int = 16
) -> Recording:
    """Return ``SelectiveScan``, whose ``y`` feeds a partner on its core while its ``state`` is read elsewhere."""
    scan = SelectiveScan(
        rows=rows, heads=heads, head_dim=head_dim, state_size=state_size
    )
    size = rows * heads * head_dim
    add = ElementwiseAdd(size=size, tile_size=32)
    steps = sequences.steps(
        (scan, "xbc", "dt", "head", "state_in", "y", "state_out"),
        (add, "y", "r", "out"),
    )
    return Recording.of_steps(
        name, steps, ["xbc", "dt", "head", "state_in", "r"], ["out", "state_out"]
    )


def mismatched_tile_recording(name: str, M: int = 2048) -> Recording:
    """Return a pair whose tiles mismatch: AXPY's kernel needs a multiple of 64, a 2-wide GEMV tile does not give it."""
    gemv = GEMV(M=M, K=M, tile_size_input=2, tile_size_output=2)
    axpy = AXPY(size=M, tile_size=256)
    steps = sequences.steps((gemv, "A", "B", "mid"), (axpy, "mid", "r", "out"))
    return Recording.of_steps(name, steps, ["A", "B", "r"], ["out"])


# ----------------------------------------------------------------- reductions


def gemv_k_split_partials(M: int, K: int, splits: int) -> list[GEMV]:
    """Return ``splits`` ``GEMV``s, each over its own share of ``K``, their partials to be reduced."""
    share = K // splits
    return [
        GEMV(M=M, K=share, tile_size_input=4, tile_size_output=M) for _ in range(splits)
    ]


def reduction_recording(
    name: str, partials: list[GEMV] | list[GEMM], order: list[int] | None = None
) -> Recording:
    """Return ``partials``, each over its own share of a reduction, summed by a fixed-order chain of ``ElementwiseAdd``s.

    ``order`` places the partials' steps in a sequence of this order (a device's actual
    completion order); the reducer still sums by the partials' own index, first to last,
    so a call with another ``order`` records a distinct recording whose bits must still
    agree.
    """
    splits = len(partials)
    (size,) = [b.elements for b in partials[0].buffers if b.name == "C"]
    order = list(range(splits)) if order is None else list(order)
    steps = []
    for i in order:
        steps += sequences.steps((partials[i], f"A{i}", f"B{i}", f"p{i}"))
    inputs = [f"A{i}" for i in range(splits)] + [f"B{i}" for i in range(splits)]
    running = "p0"
    for i in range(1, splits):
        adder = ElementwiseAdd(size=size, tile_size=min(size, 256))
        nxt = f"s{i}"
        steps += sequences.steps((adder, running, f"p{i}", nxt))
        running = nxt
    return Recording.of_steps(name, steps, inputs, [running])


def gemv_fan_in_recording(
    name: str, M: int, K: int, splits: int, order: list[int] | None = None
) -> Recording:
    """Return ``reduction_recording`` of ``splits`` ``GEMV`` partials over ``K``."""
    return reduction_recording(name, gemv_k_split_partials(M, K, splits), order)


def gemm_k_split_partials(M: int, K: int, N: int, splits: int) -> list[GEMM]:
    """Return ``splits`` ``GEMM``s, each over its own share of ``K``, their partials to be reduced."""
    share = K // splits
    return [
        GEMM(M=M, K=share, N=N, b_col_maj=True, precision=Precision.MEDIUM)
        for _ in range(splits)
    ]


def fan_in_reducer_region(recording: Recording) -> Region:
    """Return ``reduction_recording``'s steps as recorded, each partial and running sum an edge into the add that reads it.

    Every edge a stream: the partials' objects are the adds' own. Edges by
    producer, then consumer, as ``candidates`` orders them.
    """
    _, writers = recording.users()
    edges = []
    for c, step in enumerate(recording.steps):
        if not isinstance(step.op, ElementwiseAdd):
            continue
        for sink, read in zip(step.op.buffers, step.refs()):
            if not sink.fills:
                continue
            (p,) = writers[read.root]
            made = recording.steps[p]
            (source,) = [
                b.name
                for b, wrote in zip(made.op.buffers, made.refs())
                if b.drains and wrote.root == read.root
            ]
            edges.append(CompositionEdge(p, source, c, sink.name))
    return Region(
        parts=tuple(member(step.op) for step in recording.steps),
        edges=tuple(sorted(edges, key=lambda e: (e.producer, e.consumer))),
    )


def cascade_reducer_region(recording: Recording) -> Region:
    """Return ``fan_in_reducer_region`` with its running sum on the cascade.

    Each add runs on the core of the partial it reads as ``b`` (held in
    L1), and its running sum ``a`` (the first partial, then the add
    before's) arrives on the cascade from the core before: one chain of
    cores, one a partial.
    """
    region = fan_in_reducer_region(recording)
    for index, edge in enumerate(region.edges):
        region = region.held(index, Hold.CASCADE if edge.input == "a" else Hold.L1)
    return region


def partial_read_twice(name: str, M: int, K: int) -> tuple[Recording, Region]:
    """Return two ``GEMV`` partials summed by an add, the first also read by a ``SiLU``, and its region.

    The region carries the first partial to the add on the cascade and to
    the ``SiLU`` by a stream; the add runs on the second partial's core
    (held in L1).
    """
    first, second = gemv_k_split_partials(M, K, 2)
    add = ElementwiseAdd(size=M, tile_size=M)
    silu = SiLU(size=M, tile_size=M)
    recording = Recording.of_steps(
        name,
        sequences.steps(
            (first, "A0", "B0", "p0"),
            (second, "A1", "B1", "p1"),
            (add, "p0", "p1", "s"),
            (silu, "p0", "t"),
        ),
        ["A0", "B0", "A1", "B1"],
        ["s", "t"],
    )
    region = Region(
        tuple(member(step.op) for step in recording.steps),
        (
            CompositionEdge(0, "C", 2, "a", kind=EdgeKind.CASCADE),
            CompositionEdge(0, "C", 3, "x"),
            CompositionEdge(1, "C", 2, "b"),
        ),
        workers=((1, 2),),
    )
    return recording, region


def gemm_silu_splice(
    name: str, M: int = 64, N: int = 128, tile: int = 32
) -> tuple[Recording, Region]:
    """Return a ``GEMM`` into a ``SiLU`` on its cores, and its region.

    One column, ``tile`` by ``tile`` tiles: each core writes several a
    call, which a memtile joins into the GEMM's output lanes. On one worker
    the SiLU is spliced into the GEMM's cores, running on each core's tile.
    """
    gemm = GEMM(
        M=M,
        K=64,
        N=N,
        tile_m=tile,
        tile_n=tile,
        num_aie_columns=1,
        b_col_maj=True,
        precision=Precision.MEDIUM,
    )
    silu = SiLU(size=M * N, tile_size=tile * tile)
    recording = Recording.of_steps(
        name,
        sequences.steps((gemm, "A", "B", "c"), (silu, "c", "out")),
        ["A", "B"],
        ["out"],
    )
    region = Region(
        (member(gemm), member(silu)),
        (CompositionEdge(0, "C", 1, "x"),),
        workers=((0, 1),),
    )
    return recording, region


# ----------------------------------------------------------------- region shape and schedule


def qkv_among_rope_recording(name: str, M: int = 64) -> Recording:
    """Return Q, K, V projections with RoPE interposed between K's and V's: ``{Q, K, V}`` is convex but not consecutive.

    Step order is ``GEMV_q, RoPE_q, GEMV_k, RoPE_k, GEMV_v, consumer``; the three
    projections (0, 2, 4) are a convex non-contiguous set a reordering can make consecutive.
    """
    gemv_q = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=32)
    rope_q = RoPE(rows=1, cols=M, angle_rows=1)
    gemv_k = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=32)
    rope_k = RoPE(rows=1, cols=M, angle_rows=1)
    gemv_v = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=32)
    consumer = ElementwiseAdd(size=M, tile_size=32)
    steps = sequences.steps(
        (gemv_q, "Wq", "x", "q"),
        (rope_q, "q", "angles", "q_rot"),
        (gemv_k, "Wk", "x", "k"),
        (rope_k, "k", "angles", "k_rot"),
        (gemv_v, "Wv", "x", "v"),
        (consumer, "q_rot", "v", "out"),
    )
    return Recording.of_steps(name, steps, ["Wq", "Wk", "Wv", "x", "angles"], ["out"])


def acyclic_contraction_recording(name: str) -> Recording:
    """Return ``a, b, c, d`` with ``a -> d`` and ``b -> c``: ``R1 = {a, c}``, ``R2 = {b, d}`` are each convex, their contraction a cycle."""
    a, b, c, d = (Copy(dtype=np.float32, input_buffer_size=64) for _ in range(4))
    steps = sequences.steps(
        (a, "x0", "o_a"), (b, "x1", "o_b"), (c, "o_b", "o_c"), (d, "o_a", "o_d")
    )
    return Recording.of_steps(name, steps, ["x0", "x1"], ["o_c", "o_d"])


def independent_regions_recording(name: str, M: int = 64) -> Recording:
    """Return two independent chains (no edge between them): a partial order lets them run at once."""
    gemv0 = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=32)
    silu0 = SiLU(size=M, tile_size=32)
    gemv1 = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=32)
    silu1 = SiLU(size=M, tile_size=32)
    steps = sequences.steps(
        (gemv0, "A0", "B0", "mid0"),
        (silu0, "mid0", "out0"),
        (gemv1, "A1", "B1", "mid1"),
        (silu1, "mid1", "out1"),
    )
    return Recording.of_steps(name, steps, ["A0", "B0", "A1", "B1"], ["out0", "out1"])
