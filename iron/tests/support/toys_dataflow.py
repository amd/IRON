# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Toy compositions over the composition contract: a ``Region`` paired with a matching ``Recording``."""

from __future__ import annotations

from aie.iron.device import from_name

from iron import Precision
from iron.common.declare.composition import Member, Region
from iron.common.graph.record import Recording
from iron.common.image.step import Edge
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm import GEMM
from iron.operators.rms_norm import RMSNorm
from iron.operators.silu import SiLU
from iron.tests.support import sequences

NPU2 = from_name("npu2", n_cols=8)
NPU2_SMALL = from_name("npu2", n_cols=2)


def _member(op, *dims: str, **tunables) -> Member:
    """Return ``op`` as a ``Member``: ``dims`` named off its own values, the rest its tunables."""
    values = vars(op)
    return Member(
        cls=type(op),
        dims={d: values[d] for d in dims},
        tunables={t: values[t] for t in tunables} or None,
    )


def add_silu_mul(size: int = 512, tile: int = 128, cols: int = 1):
    """``add -> SiLU -> mul``: a balanced stream chain, each hop a whole buffer."""
    add = ElementwiseAdd(size=size, tile_size=tile, num_aie_columns=cols)
    silu = SiLU(size=size, tile_size=tile, num_aie_columns=cols)
    mul = ElementwiseMul(size=size, tile_size=tile, num_aie_columns=cols)
    return add, silu, mul


def add_silu_mul_recording(name: str, add, silu, mul) -> Recording:
    """Return ``add``, ``silu``, ``mul`` as a recording, over host inputs ``a``, ``b``, ``w``."""
    steps = sequences.steps(
        (add, "a", "b", "mid1"), (silu, "mid1", "mid2"), (mul, "mid2", "w", "out")
    )
    return Recording.of_steps(name, steps, ["a", "b", "w"], ["out"])


def add_silu_mul_region(add, silu, mul, **edge_kwargs: object) -> Region:
    """Return the stream region over ``add``, ``silu``, ``mul``, ``edge_kwargs`` applied to every edge."""
    members = (
        _member(
            add, "size", tile_size=add.tile_size, num_aie_columns=add.num_aie_columns
        ),
        _member(
            silu, "size", tile_size=silu.tile_size, num_aie_columns=silu.num_aie_columns
        ),
        _member(
            mul, "size", tile_size=mul.tile_size, num_aie_columns=mul.num_aie_columns
        ),
    )
    edges = (
        Edge(0, "y", 1, "x", **edge_kwargs),
        Edge(1, "y", 2, "a", **edge_kwargs),
    )
    return Region(parts=members, edges=edges)


def broadcast_skip(add_cols: int = 2, norm_cols: int = 1, depth: int | None = None):
    """Return a residual ``add`` broadcast to a norm and a skip-held second ``add``.

    ``first``'s output feeds both ``norm`` and ``second`` directly, so the
    analysis derives the broadcast hand-off itself. At ``depth=2`` the
    second add holds its first object until the norm's branch comes back,
    deadlocking the array; at ``depth=4`` it runs. ``None`` leaves the
    depth to the dataflow analysis's minimum.
    """
    first = ElementwiseAdd(size=8 * 256, tile_size=256, num_aie_columns=add_cols)
    norm = RMSNorm(rows=8, tile_size=256, num_aie_columns=norm_cols)
    second = ElementwiseAdd(size=8 * 256, tile_size=256, num_aie_columns=add_cols)
    members = (
        _member(
            first,
            "size",
            tile_size=first.tile_size,
            num_aie_columns=first.num_aie_columns,
        ),
        _member(
            norm, "rows", tile_size=norm.tile_size, num_aie_columns=norm.num_aie_columns
        ),
        _member(
            second,
            "size",
            tile_size=second.tile_size,
            num_aie_columns=second.num_aie_columns,
        ),
    )
    skip = Edge(0, "y", 2, "b", depth=depth)
    edges = (Edge(0, "y", 1, "x"), skip)
    region = Region(parts=members, edges=edges)
    return region, first, norm, second


def broadcast_skip_recording(name: str, first, norm, second) -> Recording:
    """Return ``first``, ``norm`` and ``second`` wired as ``broadcast_skip`` names them."""
    steps = sequences.steps(
        (first, "a", "r", "h"),
        (norm, "h", "normed"),
        (second, "normed", "h", "out"),
    )
    return Recording.of_steps(name, steps, ["a", "r"], ["out"], feedback=["h"])


def gemm_rowwise(
    M: int = 64,
    K: int = 64,
    N: int = 64,
    row_tile: int = 16,
    cols: int = 1,
    dev=NPU2,
):
    """Return a GEMM whose ``tile_m``-row output tiles feed one row a firing into a row-wise norm.

    ``row_tile`` is GEMM's own ``tile_m`` tunable, so the edge's ``row_tile :
    1`` token rate is what the analysis derives from the operators
    themselves, never an annotation. ``gemm`` is resolved for ``dev``, so a
    row split ``dev``'s array would really make (``gemm.n_aie_rows``) is
    caught here rather than only once the composer builds it.
    """
    gemm = GEMM(
        M=M, K=K, N=N, precision=Precision.MEDIUM, num_aie_columns=cols, tile_m=row_tile
    ).resolved(dev)
    norm = RMSNorm(rows=M, tile_size=N, num_aie_columns=cols)
    return gemm, norm


def gemm_rowwise_region(gemm: GEMM, norm: RMSNorm, depth: int | None = None) -> Region:
    """Return the region over ``gemm`` -> ``norm``; the edge's rate is ``gemm.tile_m : 1`` rows a firing."""
    members = (
        _member(
            gemm,
            "M",
            "K",
            "N",
            num_aie_columns=gemm.num_aie_columns,
            tile_m=gemm.tile_m,
        ),
        _member(
            norm, "rows", tile_size=norm.tile_size, num_aie_columns=norm.num_aie_columns
        ),
    )
    edges = (Edge(0, "C", 1, "x", depth=depth),)
    return Region(parts=members, edges=edges)


def gemm_rowwise_recording(name: str, gemm, norm) -> Recording:
    """Return ``gemm`` then ``norm`` as a recording, over host inputs ``A``, ``B``."""
    steps = sequences.steps((gemm, "A", "B", "mid"), (norm, "mid", "out"))
    return Recording.of_steps(name, steps, ["A", "B"], ["out"])


def gemm_into_gemm(
    M: int,
    width: int,
    producer_tile: int,
    consumer_tile: int,
    cols: int = 1,
    dev=NPU2,
):
    """Return two GEMMs chained, the first's ``C`` feeding the second's ``A`` directly.

    ``producer_tile``/``consumer_tile`` are each GEMM's own ``tile_m``
    tunable, so the edge's rate is theirs, derived by the analysis, never
    an annotation; both GEMMs share ``width`` as their ``K`` and ``N`` so
    the first's output rows line up with the second's input rows. Both are
    resolved for ``dev``, since each GEMM's real per-firing row count is
    ``tile_m`` times the row split ``dev``'s array gives it
    (``n_aie_rows``), not ``tile_m`` alone.
    """
    producer = GEMM(
        M=M,
        K=width,
        N=width,
        precision=Precision.MEDIUM,
        num_aie_columns=cols,
        tile_m=producer_tile,
    ).resolved(dev)
    consumer = GEMM(
        M=M,
        K=width,
        N=width,
        precision=Precision.MEDIUM,
        num_aie_columns=cols,
        tile_m=consumer_tile,
    ).resolved(dev)
    return producer, consumer


def gemm_into_gemm_region(
    producer: GEMM, consumer: GEMM, depth: int | None = None
) -> Region:
    """Return the region over ``producer`` -> ``consumer``; the edge's rate is ``producer.tile_m : consumer.tile_m`` rows a firing."""
    members = (
        _member(
            producer,
            "M",
            "K",
            "N",
            num_aie_columns=producer.num_aie_columns,
            tile_m=producer.tile_m,
        ),
        _member(
            consumer,
            "M",
            "K",
            "N",
            num_aie_columns=consumer.num_aie_columns,
            tile_m=consumer.tile_m,
        ),
    )
    edges = (Edge(0, "C", 1, "A", depth=depth),)
    return Region(parts=members, edges=edges)


def gemm_into_gemm_recording(name: str, producer: GEMM, consumer: GEMM) -> Recording:
    """Return ``producer`` then ``consumer`` as a recording, over host inputs ``A``, ``B``, ``B2``."""
    steps = sequences.steps((producer, "A", "B", "mid"), (consumer, "mid", "B2", "out"))
    return Recording.of_steps(name, steps, ["A", "B", "B2"], ["out"])


def mismatched_rate_cycle(add_tile: int = 64, mul_tile: int = 32, size: int = 128):
    """Return a two-member cycle, ``add``'s output into ``mul`` and ``mul``'s back into ``add``.

    Both operators move a whole buffer a firing at their own ``tile_size``,
    so an edge's rate is theirs alone; at ``add_tile != mul_tile`` the two
    edges of the cycle demand repetitions no positive integer vector
    satisfies, so no annotation is needed to make the cycle inconsistent.
    """
    add = ElementwiseAdd(size=size, tile_size=add_tile, num_aie_columns=1)
    mul = ElementwiseMul(size=size, tile_size=mul_tile, num_aie_columns=1)
    members = (
        _member(add, "size", tile_size=add.tile_size),
        _member(mul, "size", tile_size=mul.tile_size),
    )
    edges = (Edge(0, "y", 1, "a"), Edge(1, "y", 0, "a"))
    region = Region(parts=members, edges=edges)
    return region, add, mul


def mismatched_rate_cycle_recording(name: str, add, mul) -> Recording:
    """Return ``add`` and ``mul`` wired as ``mismatched_rate_cycle`` names them, ``x`` carried across calls."""
    steps = sequences.steps((add, "x", "w", "mid"), (mul, "mid", "x", "x"))
    return Recording.of_steps(name, steps, ["w"], ["x"], feedback=["x"])


def running_sum(size: int = 256, tile: int = 128, cols: int = 1):
    """Return a one-step accumulate-in-place loop, the feedback family's running sum: ``acc = acc + x``."""
    add = ElementwiseAdd(size=size, tile_size=tile, num_aie_columns=cols)
    members = (
        _member(
            add, "size", tile_size=add.tile_size, num_aie_columns=add.num_aie_columns
        ),
    )
    edges = (Edge(0, "y", 0, "a"),)
    region = Region(parts=members, edges=edges)
    return region, add


def running_sum_recording(name: str, add, carried: bool = True) -> Recording:
    """Return ``add`` run once over an accumulator ``acc`` and a fresh input ``x`` each call.

    ``carried`` marks ``acc`` fed back across calls (``feedback=["acc"]``),
    which is where the analysis's one initial token on the self-loop edge
    comes from; without it the edge starts with none.
    """
    steps = sequences.steps((add, "acc", "x", "acc"))
    feedback = ["acc"] if carried else []
    return Recording.of_steps(name, steps, ["x"], ["acc"], feedback=feedback)
