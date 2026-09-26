# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GQAContext: decode attention's context, read straight from the value cache.

``ctx[g, k, :] = sum_l weights[g, k, l] * cache[g, l, :]``: every head ``k``
of KV group ``g`` weighs that group's cached values by its attention
probabilities. It replaces repeating the cache per head, transposing it,
and a GEMV over the transpose, and computes the same bits as that GEMV:
see ``gqa_context_bf16.cc``.

One column per group, one core per head of it. The group's values stream
once through the column, ``chunk`` positions at a time, broadcast to all of
its cores; each core takes its own head's probabilities for those positions
from a memtile split, carries the partial sums in its own memory, and writes
its head's ``head_dim`` outputs, joined back per column in a memtile.

In a graph, over the ``(groups, seq_len * head_dim)`` cache and the
``(heads, seq_len)`` softmax output::

    ctx = GQAContext(values.reshape(G, L, D), weights.reshape(G, H // G, L))
"""

import numpy as np
from ml_dtypes import bfloat16

from aie.iron import Buffer, ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.utils.verify import Tolerance

from iron.common.declare import (
    BoundBuffer,
    Contraction,
    In,
    Operator,
    Order,
    Out,
    Overlay,
    Semantics,
    StreamIn,
    StreamOut,
    Untunable,
    dim,
    operator,
    tunable,
)
from iron.common.testing import Case, Testing
from iron.common.tiling import Access, contiguous

from .kernel import FIRST, LANES, LAST, gqa_context, gqa_context_ref

# Compute rows in a column, one head per row.
_ROWS = 4


@operator
class GQAContextOverlay(Overlay):
    """``groups`` columns of ``heads_per_group`` cores, one KV group each."""

    groups: int = dim()
    heads_per_group: int = dim()
    seq_len: int = dim()
    head_dim: int = dim(64)
    # Positions per kernel call: 128 unless given, or 64 when that does not
    # divide seq_len. A core holds two chunks of values (16 KB each at 128)
    # beside its 16 KB of partial sums.
    chunk: int | None = tunable(None)

    v = StreamIn(chunk, head_dim, per=groups, depth=2)
    p = StreamIn(heads_per_group, chunk, per=groups, depth=2)
    ctx = StreamOut(heads_per_group, head_dim, per=groups, depth=1)

    def validate(self) -> None:
        if self.chunk is None:
            self.chunk = 2 * LANES if self.seq_len % (2 * LANES) == 0 else LANES
        if not 1 <= self.heads_per_group <= _ROWS:
            raise ValueError(
                f"heads_per_group ({self.heads_per_group}) must be 1 to {_ROWS}: "
                "one core per head, in one column"
            )
        if self.seq_len % self.chunk:
            raise ValueError(
                f"seq_len ({self.seq_len}) must be a multiple of chunk ({self.chunk})"
            )
        gqa_context(self.chunk, self.head_dim)  # the kernel checks the rest

    def tuning(self, dev) -> "GQAContextOverlay":
        if dev is not None and self.groups > dev.cols:
            raise Untunable(
                f"{self.groups} groups need {self.groups} columns; "
                f"the device has {dev.cols}"
            )
        return self

    def semantics(self) -> Semantics:
        """The positions are reduced inside one core, so a released output is final."""
        return Contraction(final_at_release=True)

    def design(self, target) -> list:
        kernel = gqa_context(self.chunk, self.head_dim)
        calls = self.seq_len // self.chunk
        rows = self.heads_per_group
        acc_ty = np.ndarray[(LANES * self.head_dim,), np.dtype[np.float32]]
        p_ty = np.ndarray[(self.chunk,), np.dtype[bfloat16]]
        out_ty = np.ndarray[(self.head_dim,), np.dtype[bfloat16]]
        # Where each call's chunk sits in the context.
        if calls == 1:
            flags = [FIRST | LAST]
        else:
            flags = [FIRST] + [0] * (calls - 2) + [LAST]

        def core_body(of_v, of_p, of_out, acc, kernel):
            out = of_out.acquire(1)

            def call(flag):
                v = of_v.acquire(1)
                p = of_p.acquire(1)
                kernel(v, p, acc, out, flag)
                of_v.release(1)
                of_p.release(1)

            call(flags[0])
            if calls > 2:
                for _ in range_(calls - 2):
                    call(0)
            if calls > 1:
                call(flags[-1])
            of_out.release(1)

        workers = []
        for g in range(self.groups):
            of_v = ObjectFifo(self.v.tile, name=f"v_{g}", depth=self.v.depth)
            self.v[g].bind(of_v.prod())
            of_p = ObjectFifo(self.p.tile, name=f"p_{g}", depth=self.p.depth)
            self.p[g].bind(of_p.prod())
            p_heads = of_p.cons().split(
                [self.chunk * k for k in range(rows)],
                obj_types=[p_ty] * rows,
                names=[f"p_{g}_{k}" for k in range(rows)],
                depths=[self.p.depth] * rows,
            )
            of_ctx = ObjectFifo(self.ctx.tile, name=f"ctx_{g}", depth=self.ctx.depth)
            self.ctx[g].bind(of_ctx.cons())
            ctx_heads = of_ctx.prod().join(
                [self.head_dim * k for k in range(rows)],
                obj_types=[out_ty] * rows,
                names=[f"ctx_{g}_{k}" for k in range(rows)],
                depths=[1] * rows,
            )
            for k in range(rows):
                acc = Buffer(acc_ty, name=f"acc_{g}_{k}")
                workers.append(
                    Worker(
                        core_body,
                        [
                            of_v.cons(),
                            p_heads[k].cons(),
                            ctx_heads[k].prod(),
                            acc,
                            kernel,
                        ],
                    )
                )
        return workers


@operator
class GQAContext(Operator[GQAContextOverlay]):
    """Grouped-query attention context from the ``(G, L, D)`` value cache."""

    # The sum is the kernel's arithmetic model, so any difference is a bug.
    # The llama arm is the shape decode dispatches: 8 KV groups of 4 heads
    # over a max_seq_len=2048 context of head_dim=64.
    test = Testing(
        [
            Case(dict(groups=2, heads_per_group=4, seq_len=256), id="small"),
            Case(
                dict(groups=3, heads_per_group=2, seq_len=128, chunk=64),
                id="one_call_per_chunk",
            ),
            Case(dict(groups=1, heads_per_group=1, seq_len=128), id="single_call"),
            Case(dict(groups=4, heads_per_group=4, seq_len=64), id="shortest"),
            Case(dict(groups=8, heads_per_group=4, seq_len=2048), id="llama"),
        ],
        tolerance=Tolerance.exact(),
    )

    cache = In(
        GQAContextOverlay.groups,
        GQAContextOverlay.seq_len,
        GQAContextOverlay.head_dim,
        to=GQAContextOverlay.v,
    )
    weights = In(
        GQAContextOverlay.groups,
        GQAContextOverlay.heads_per_group,
        GQAContextOverlay.seq_len,
        to=GQAContextOverlay.p,
    )
    ctx = Out(
        GQAContextOverlay.groups,
        GQAContextOverlay.heads_per_group,
        GQAContextOverlay.head_dim,
        from_=GQAContextOverlay.ctx,
    )

    def reference(self, cache, weights):
        ov = self.ov
        ctx = gqa_context_ref(
            np.asarray(cache).reshape(ov.groups, ov.seq_len, ov.head_dim),
            np.asarray(weights).reshape(ov.groups * ov.heads_per_group, ov.seq_len),
            ov.heads_per_group,
        )
        return ctx.reshape(ov.groups, ov.heads_per_group, ov.head_dim)

    def order(self, buffer: BoundBuffer) -> Order:
        """Column ``g`` takes group ``g``: its values whole, in order; its
        heads' probabilities a chunk of positions at a time, every head's
        chunk together; its heads' contexts back, contiguous."""
        ov = self.ov
        rows, length, dim_ = ov.heads_per_group, ov.seq_len, ov.head_dim
        if buffer is self.cache:
            span = length * dim_
            return Order(
                ov.v,
                tuple(
                    (contiguous(buffer.elements, g * span, span),)
                    for g in range(ov.groups)
                ),
            )
        if buffer is self.weights:
            return Order(
                ov.p,
                tuple(
                    (
                        Access(
                            buffer.elements,
                            g * rows * length,
                            (1, length // ov.chunk, rows, ov.chunk),
                            (0, ov.chunk, length, 1),
                        ),
                    )
                    for g in range(ov.groups)
                ),
            )
        span = rows * dim_
        return Order(
            ov.ctx,
            tuple(
                (contiguous(buffer.elements, g * span, span),) for g in range(ov.groups)
            ),
        )
