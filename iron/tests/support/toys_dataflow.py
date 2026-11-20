# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Toy compositions over the composition contract: a ``Region`` paired with a matching ``Recording``."""

from __future__ import annotations

import numpy as np
from aie.iron.device import Device

import iron
from iron import Precision, Scratchpad
from iron.common.declare.composition import Region
from iron.common.graph.record import Recording
from iron.common.image.step import Edge, EdgeKind
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm import GEMM
from iron.operators.rms_norm import RMSNorm
from iron.operators.silu import SiLU
from iron.tests.support import sequences
from iron.tests.support.toys_edges import member


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
        member(add),
        member(silu),
        member(mul),
    )
    edges = (
        Edge(0, "y", 1, "x", **edge_kwargs),
        Edge(1, "y", 2, "a", **edge_kwargs),
    )
    return Region(parts=members, edges=edges)


def broadcast_skip(add_cols: int = 2, norm_cols: int = 2, depth: int | None = None):
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
        member(first),
        member(norm),
        member(second),
    )
    skip = Edge(0, "y", 2, "b", depth=depth)
    # Every step at the same columns: each edge's lanes meet as they are. The
    # skip stays edges[1].
    edges = (Edge(0, "y", 1, "x"), skip, Edge(1, "y", 2, "a"))
    region = Region(parts=members, edges=edges)
    return region, first, norm, second


def broadcast_skip_recording(name: str, first, norm, second) -> Recording:
    """Return ``first``, ``norm`` and ``second`` wired as ``broadcast_skip`` names them."""
    steps = sequences.steps(
        (first, "a", "r", "h"),
        (norm, "h", "normed"),
        (second, "normed", "h", "out"),
    )
    return Recording.of_steps(name, steps, ["a", "r"], ["out"])


def rate_skip(
    tile: int = 64, row: int = 256, size: int = 2048, depth: int | None = None
) -> tuple[Region, Recording]:
    """Return an add whose ``tile``-element output a norm reads as ``row``-element rows, the add's output also skipped to a second add.

    The add's tiles restage into the norm's rows through a memtile, so the
    norm takes ``row // tile`` of them before it writes a row, and the second
    add, which reads the skip and the norm's rows tile by tile, waits on the
    norm meanwhile: the skip must hold those tiles, its minimum ``row //
    tile``, and below it the window deadlocks. ``depth`` is the skip's.
    """
    first = ElementwiseAdd(size=size, num_aie_columns=1, tile_size=tile)
    norm = RMSNorm(rows=size // row, tile_size=row, num_aie_columns=1)
    second = ElementwiseAdd(size=size, num_aie_columns=1, tile_size=tile)
    steps = sequences.steps(
        (first, "a", "r", "h"), (norm, "h", "n"), (second, "n", "h", "out")
    )
    recording = Recording.of_steps("rate_skip", steps, ["a", "r"], ["out"])
    edges = (
        Edge(0, "y", 1, "x", kind=EdgeKind.STAGED),
        Edge(0, "y", 2, "b", depth=depth),
        Edge(1, "y", 2, "a", kind=EdgeKind.STAGED),
    )
    return Region(tuple(member(s.op) for s in recording.steps), edges), recording


def gemm_rowwise(
    dev: Device,
    M: int = 64,
    K: int = 64,
    N: int = 64,
    row_tile: int = 16,
    cols: int = 1,
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
        member(gemm),
        member(norm),
    )
    edges = (Edge(0, "C", 1, "x", depth=depth),)
    return Region(parts=members, edges=edges)


def gemm_rowwise_recording(name: str, gemm, norm) -> Recording:
    """Return ``gemm`` then ``norm`` as a recording, over host inputs ``A``, ``B``."""
    steps = sequences.steps((gemm, "A", "B", "mid"), (norm, "mid", "out"))
    return Recording.of_steps(name, steps, ["A", "B"], ["out"])


class BoundedRows(iron.Graph):
    """A GEMM over the first ``n`` rows of ``a``, each row then normalized: a valid length short of ``a``'s rows.

    Args:
        tile_m: The GEMM's rows a tile.
    """

    def __init__(self, tile_m: int) -> None:
        self.tile_m = tile_m

    def body(self, a, b, *, n: Scratchpad[np.int32]):
        rows = GEMM.step(
            a[:n],
            b,
            precision=Precision.MEDIUM,
            num_aie_columns=1,
            tile_m=self.tile_m,
        )
        return RMSNorm.step(rows, num_aie_columns=1)


def gemm_into_gemm(
    dev: Device,
    M: int,
    width: int,
    producer_tile: int,
    consumer_tile: int,
    cols: int = 1,
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
        member(producer),
        member(consumer),
    )
    edges = (Edge(0, "C", 1, "A", depth=depth),)
    return Region(parts=members, edges=edges)


def gemm_into_gemm_recording(name: str, producer: GEMM, consumer: GEMM) -> Recording:
    """Return ``producer`` then ``consumer`` as a recording, over host inputs ``A``, ``B``, ``B2``."""
    steps = sequences.steps((producer, "A", "B", "mid"), (consumer, "mid", "B2", "out"))
    return Recording.of_steps(name, steps, ["A", "B", "B2"], ["out"])


def running_sum(size: int = 256, tile: int = 128, cols: int = 1):
    """Return a one-step accumulate-in-place loop, the feedback family's running sum: ``acc = acc + x``."""
    add = ElementwiseAdd(size=size, tile_size=tile, num_aie_columns=cols)
    members = (member(add),)
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
    return Recording.of_steps(
        name, steps, ["x"], [] if feedback else ["acc"], feedback=feedback
    )
