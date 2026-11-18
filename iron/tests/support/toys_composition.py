# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Toys the composition-contract tuning tests (``iron/tests/tuning/``) share.

Small, real IRON operators recorded as runs of steps (``iron/tests/support/sequences.py``,
as ``iron/tests/support/fusable.py`` does), the profile-layer trees
(``iron.common.declare.composition``) a composition transformation is named in, and
``has_worker_group``, the assertion a worker-placement test makes of them.
"""

from __future__ import annotations

import numpy as np

from iron import Precision
from iron.common.declare.composition import Configuration, Entry, Member, Region
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
    """Return decode MHA's graph, small: ``K . q -> Softmax -> V^T . p``.

    ``rows`` packs several query rows (as decode packs a KV group's heads) so ``Softmax``
    meets its row count's multiple-of-16 rule at a size small enough to toy with.
    """
    qk = GEMV(M=kv_len, K=head_dim, tile_size_input=4, tile_size_output=32)
    softmax = Softmax(rows=rows, cols=kv_len)
    pv = GEMV(M=head_dim, K=kv_len, tile_size_input=4, tile_size_output=32)
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
    seq: int = 32, kv_len: int = 128, head_dim: int = 64
) -> tuple[GEMM, ElementwiseAdd, Softmax, GEMM]:
    """Return prefill MHA's graph, small: ``Q K^T -> + causal mask -> Softmax -> P . V``."""
    qk = GEMM(M=seq, K=head_dim, N=kv_len, b_col_maj=True, precision=Precision.MEDIUM)
    add_mask = ElementwiseAdd(size=seq * kv_len, tile_size=kv_len)
    softmax = Softmax(rows=seq, cols=kv_len)
    pv = GEMM(M=seq, K=kv_len, N=head_dim, b_col_maj=True, precision=Precision.MEDIUM)
    return qk, add_mask, softmax, pv


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
    """Return the recording of ``axpy`` alone: ``out = scalar_factor * a + b``."""
    steps = sequences.steps((axpy, "a", "b", "out"))
    return Recording.of_steps(name, steps, ["a", "b"], ["out"])


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
    mul = ElementwiseMul(size=size, tile_size=32)
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
        GEMV(M=M, K=share, tile_size_input=4, tile_size_output=32)
        for _ in range(splits)
    ]


def gemv_fan_in_recording(
    name: str, M: int, K: int, splits: int, order: list[int] | None = None
) -> Recording:
    """Return ``splits`` ``GEMV`` partials over ``K``, reduced into one sum by a fixed-order chain of ``ElementwiseAdd``s.

    ``order`` places the partials' steps in a sequence of this order (a device's actual
    completion order); the reducer still sums by the partials' own index, first to last,
    so a call with another ``order`` records a distinct recording whose bits must still
    agree.
    """
    gemvs = gemv_k_split_partials(M, K, splits)
    order = list(range(splits)) if order is None else list(order)
    steps = []
    for i in order:
        steps += sequences.steps((gemvs[i], f"A{i}", f"B{i}", f"p{i}"))
    inputs = [f"A{i}" for i in range(splits)] + [f"B{i}" for i in range(splits)]
    running = "p0"
    for i in range(1, splits):
        adder = ElementwiseAdd(size=M, tile_size=min(M, 256))
        nxt = f"s{i}"
        steps += sequences.steps((adder, running, f"p{i}", nxt))
        running = nxt
    return Recording.of_steps(name, steps, inputs, [running])


def gemm_k_split_partials(M: int, K: int, N: int, splits: int) -> list[GEMM]:
    """Return ``splits`` ``GEMM``s, each over its own share of ``K``, their partials to be reduced."""
    share = K // splits
    return [
        GEMM(M=M, K=share, N=N, b_col_maj=True, precision=Precision.MEDIUM)
        for _ in range(splits)
    ]


def cascade_region(member_dims: list[Member], output: str, input: str) -> Region:
    """Return a cascade chain: each member's ``output`` carried to the next's ``input`` by ``EdgeKind.CASCADE``.

    GEMV and GEMM declare no cascade variant (a reported gap: cascade kernels for them are
    not built): this shapes the composition, not a kernel that runs a cascade put/get today.
    """
    edges = tuple(
        CompositionEdge(i, output, i + 1, input, kind=EdgeKind.CASCADE)
        for i in range(len(member_dims) - 1)
    )
    return Region(parts=tuple(member_dims), edges=edges)


def fan_in_reducer_region(
    members: list[Member], reducer: Member, output: str, a: str, b: str
) -> Region:
    """Return ``members``' partials fed to one reducing ``Member`` by a fixed-order chain."""
    parts = list(members)
    edges = []
    running = 0
    for i in range(1, len(members)):
        parts.append(reducer)
        edges.append(CompositionEdge(running, output, len(parts) - 1, a))
        edges.append(CompositionEdge(i, output, len(parts) - 1, b))
        running = len(parts) - 1
    return Region(parts=tuple(parts), edges=tuple(edges))


# ----------------------------------------------------------------- region shape and schedule


def qkv_among_rope_recording(name: str, M: int = 64, angle_rows: int = 32) -> Recording:
    """Return Q, K, V projections with RoPE interposed between K's and V's: ``{Q, K, V}`` is convex but not consecutive.

    Step order is ``GEMV_q, RoPE_q, GEMV_k, RoPE_k, GEMV_v, consumer``; the three
    projections (0, 2, 4) are a convex non-contiguous set a reordering can make consecutive.
    """
    gemv_q = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=32)
    rope_q = RoPE(rows=angle_rows, cols=M, angle_rows=angle_rows)
    gemv_k = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=32)
    rope_k = RoPE(rows=angle_rows, cols=M, angle_rows=angle_rows)
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
