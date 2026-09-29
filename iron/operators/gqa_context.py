# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GQAContext: decode attention's context, read straight from the value cache.

``ctx[g, k, :] = sum_l weights[g, k, l] * cache[g, l, :]``: every head ``k``
of KV group ``g`` weighs that group's cached values by its attention
probabilities. It replaces repeating the cache per head, transposing it,
and a GEMV over the transpose, and computes the same bits as that GEMV:
``linalg.mv_col_maj`` is the GEMV's kernel reading its matrix transposed,
operation for operation.
"""

import dataclasses

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import MV_COL_MAJ_FIRST, MV_COL_MAJ_LAST, linalg
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import In, Incompatible, Operator, Out, auto, param
from iron.common.testing import Case, Testing

# Compute rows in a column, one head per row.
_ROWS = 4


def _lanes(seq_len: int) -> int:
    """The partial sums per output: the vector width GEMV's kernel takes at
    ``K = seq_len``, the widest of 64, 32, 16 with ``K % w == 0`` and ``K >=
    2 * w``, so the sums are that GEMV's.
    """
    return next((w for w in (64, 32, 16) if seq_len % w == 0 and seq_len >= 2 * w), 0)


def reference(values, weights, heads_per_group: int) -> np.ndarray:
    """``ctx[h, d] = sum_l weights[h, l] * values[h // heads_per_group, l, d]``.

    ``values`` is ``(groups, L, D)`` and ``weights`` ``(groups *
    heads_per_group, L)``, both bf16; the result is ``(heads, D)`` bf16. Summed
    as the kernel sums, at the GEMV's ``lanes`` (``_lanes``): lane ``j``
    of each output takes positions ``lanes * i + j`` in order of ``i``,
    starting from the first product; the lanes are halved, lane ``j +
    lanes / 2`` onto lane ``j``, down to 1; the float left is rounded to
    bf16, to nearest even. A product of two bf16 is exact in float32, so
    each step is one float32 addition, as on the core. The core's adder is
    not IEEE on every cancelling add of mixed signs, so on signed operands
    this can miss an output bit now and then; on non-negative ones it is
    exact.
    """
    values = np.asarray(values, dtype=bfloat16)
    weights = np.asarray(weights, dtype=bfloat16)
    groups, length, dim = values.shape
    lanes = _lanes(length)
    heads = weights.shape[0]
    if weights.shape != (groups * heads_per_group, length):
        raise ValueError(
            f"weights {weights.shape} are not ({groups} x {heads_per_group}, {length})"
        )
    v = np.repeat(values.astype(np.float32), heads_per_group, axis=0)
    # (heads, rounds, lanes, D): position lanes * i + j is round i, lane j.
    products = (v * weights.astype(np.float32)[:, :, None]).reshape(
        heads, length // lanes, lanes, dim
    )
    partial = products[:, 0].copy()
    for i in range(1, length // lanes):
        partial += products[:, i]
    half = lanes // 2
    while half >= 1:
        partial[:, :half] += partial[:, half : 2 * half]
        half //= 2
    return partial[:, 0].astype(bfloat16)


class GQAContext(Operator):
    """Grouped-query attention context from the ``(G, L, D)`` value cache.

    One column per group, one core per head of it. The group's values stream
    once through the column, ``chunk`` positions at a time, broadcast to all
    of its cores; each core takes its own head's probabilities for those
    positions from a memtile split, carries the partial sums in its own
    memory, and writes its head's ``head_dim`` outputs, joined back per
    column in a memtile.

    In a graph, over the ``(groups, seq_len, head_dim)`` cache and the
    ``(heads, seq_len)`` softmax output:

    ```python
    ctx = GQAContext(values, weights.reshape(G, H // G, L))
    ```
    """

    # The reference is the kernel's order in IEEE float32, which the core
    # matches on the non-negative operands drawn here (see reference), so
    # any difference is a bug. Equality with the GEMV decode used before, on
    # signed data, is iron/tests/operators/gqa_context_vs_gemv.py. The
    # llama arm is the shape decode dispatches: 8 KV groups of 4 heads over
    # a max_seq_len=2048 context of head_dim=64.
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

    groups: int = param()
    heads_per_group: int = param()
    # The array reads it: the kernel calls per context, and the lanes.
    seq_len: int = param(array=True)
    head_dim: int = param(default=64)
    # Positions per kernel call: 128 unless given, or 64 when that does not
    # divide seq_len. A core holds two chunks of values (16 KB each at 128)
    # beside its 16 KB of partial sums.
    chunk: int = auto()

    cache = In(
        groups, seq_len, head_dim, tile=(chunk, head_dim), per=(groups,), depth=2
    )
    weights = In(
        groups,
        heads_per_group,
        seq_len,
        tile=(heads_per_group, chunk),
        per=(groups,),
        depth=2,
    )
    ctx = Out(
        groups,
        heads_per_group,
        head_dim,
        tile=(heads_per_group, head_dim),
        per=(groups,),
        depth=1,
    )

    def validate(self) -> None:
        if not 1 <= self.heads_per_group <= _ROWS:
            raise ValueError(
                f"heads_per_group ({self.heads_per_group}) must be 1 to {_ROWS}: "
                "one core per head, in one column"
            )
        if self.seq_len % 64:
            raise ValueError(f"seq_len ({self.seq_len}) must be a multiple of 64")

    def resolve(self, dev):
        self.check_shim_columns(dev, self.groups)
        chunk = self.chunk or (128 if self.seq_len % 128 == 0 else 64)
        return dataclasses.replace(self, chunk=chunk)

    def compatible(self) -> None:
        if self.seq_len % self.chunk:
            raise Incompatible(
                f"seq_len ({self.seq_len}) must be a multiple of chunk ({self.chunk})"
            )
        # The kernel checks the rest: head_dim a whole number of vectors,
        # chunk whole rounds of the lanes.
        self._kernel()

    def _kernel(self):
        return linalg.mv_col_maj(
            self.head_dim, self.chunk, vec_size=_lanes(self.seq_len)
        )

    def array(self, target) -> list:
        kernel = self._kernel()
        calls = self.seq_len // self.chunk
        rows, lanes = self.heads_per_group, _lanes(self.seq_len)
        acc_ty = np.ndarray[(lanes * self.head_dim,), np.dtype[np.float32]]
        p_ty = np.ndarray[(self.chunk,), np.dtype[bfloat16]]
        out_ty = np.ndarray[(self.head_dim,), np.dtype[bfloat16]]
        # Where each call's chunk sits in the context.
        if calls == 1:
            flags = [MV_COL_MAJ_FIRST | MV_COL_MAJ_LAST]
        else:
            flags = [MV_COL_MAJ_FIRST] + [0] * (calls - 2) + [MV_COL_MAJ_LAST]

        def core_body(of_v, of_p, of_out, acc, kernel):
            out = of_out.acquire(1)

            def call(flag):
                v = of_v.acquire(1)
                p = of_p.acquire(1)
                kernel(flag, v, p, acc, out)
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
            of_v = ObjectFifo(self.cache.tile, name=f"v_{g}", depth=2)
            self.cache.lane(g).bind(of_v.prod())
            of_p = ObjectFifo(self.weights.tile, name=f"p_{g}", depth=2)
            self.weights.lane(g).bind(of_p.prod())
            p_heads = of_p.cons().split(
                [self.chunk * k for k in range(rows)],
                obj_types=[p_ty] * rows,
                names=[f"p_{g}_{k}" for k in range(rows)],
                depths=[2] * rows,
            )
            of_ctx = ObjectFifo(self.ctx.tile, name=f"ctx_{g}", depth=1)
            self.ctx.lane(g).bind(of_ctx.cons())
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

    def sequence(self, rt):
        """Column ``g`` takes group ``g``: its values whole, in order; its
        heads' probabilities a chunk of positions at a time, every head's
        chunk together; its heads' contexts back, contiguous.
        """
        rows, length, dim, chunk = (
            self.heads_per_group,
            self.seq_len,
            self.head_dim,
            self.chunk,
        )
        with rt.group() as tg:
            for g in range(self.groups):
                span = length * dim
                rt.fill(
                    self.cache.lane(g),
                    TensorAccessPattern(
                        self.cache.shape, g * span, [1, 1, 1, span], [0, 0, 0, 1]
                    ),
                    group=tg,
                )
                rt.fill(
                    self.weights.lane(g),
                    TensorAccessPattern(
                        self.weights.shape,
                        g * rows * length,
                        [1, length // chunk, rows, chunk],
                        [0, chunk, length, 1],
                    ),
                    group=tg,
                )
            for g in range(self.groups):
                span = rows * dim
                rt.drain(
                    self.ctx.lane(g),
                    TensorAccessPattern(
                        self.ctx.shape, g * span, [1, 1, 1, span], [0, 0, 0, 1]
                    ),
                    group=tg,
                    wait=True,
                )

    def ops(self) -> int:
        return 2 * self.groups * self.heads_per_group * self.seq_len * self.head_dim

    def reference(self, cache, weights):
        ctx = reference(
            np.asarray(cache).reshape(self.groups, self.seq_len, self.head_dim),
            np.asarray(weights).reshape(
                self.groups * self.heads_per_group, self.seq_len
            ),
            self.heads_per_group,
        )
        return ctx.reshape(self.groups, self.heads_per_group, self.head_dim)
