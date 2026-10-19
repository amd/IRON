# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Experts: a mixture of experts' feed-forwards, each row through the
experts ``TopKRouter`` chose for it.
"""

import numpy as np
from aie.dialects.aie import T
from aie.extras.dialects import arith
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import CompileTime, In, ObjectFifo, Out, TaskGroup, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import moe
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Built, Extent, Operator, field
from iron.common.testing import Case, Testing

#: The rows and columns of a weight tile, so that at Qwen3's shapes a
#: shim BD repeats an expert's row blocks at most 64 times.
TILE = 32


def _routed(op: "Experts") -> dict:
    """Each row's ``top_k`` distinct experts, and weights at a layer's scale."""
    rng = np.random.default_rng(7)
    ids = [rng.choice(op.experts, op.top_k, replace=False) for _ in range(op.rows)]
    gate_up = rng.standard_normal(op.gate_up.shape) / np.sqrt(op.hidden)
    down = rng.standard_normal(op.down.shape) / np.sqrt(op.width)
    return dict(
        given={
            op.ids: np.array(ids, np.int32),
            op.gate_up: gate_up.astype(bfloat16),
            op.down: down.astype(bfloat16),
        },
        normal=(op.x, op.weights),
    )


class Experts(Operator):
    """Row ``r`` of ``x``: the sum over ``j < top_k`` of ``weights[r, 2 * j]``
    times expert ``e = ids[r, j]``'s gated feed-forward, ``down[e] @
    (silu(g) * u)`` where ``g`` and ``u`` are the halves of ``gate_up[e] @
    x``, in float32, rounded once. ``ids`` and ``weights`` are
    ``TopKRouter``'s; ``gate_up`` and ``down`` stack the experts as
    transformers holds them.

    One core, scalar, reading two streams: a row's ``x``, ``weights`` and
    ``ids``, which a memtile joins, and every expert's ``gate_up`` then
    ``down`` in ``TILE`` x ``TILE`` tiles, streamed for each row. The
    kernel skips the tiles of experts the row did not choose.
    """

    test = Testing(
        [
            Case(dict(rows=2, hidden=256, width=64, experts=4, top_k=2)),
            Case(dict(rows=8, hidden=512, width=256, experts=8, top_k=2), bench=True),
        ],
        draw=_routed,
    )

    rows: CompileTime[int] = field(array=True)
    hidden: CompileTime[int] = field()
    width: CompileTime[int] = field(array=True)
    experts: CompileTime[int] = field(array=True)
    top_k: CompileTime[int] = field()
    weights_width: CompileTime[int] = field(derive=lambda op: 2 * op.top_k, repr=False)
    gate_up_width: CompileTime[int] = field(derive=lambda op: 2 * op.width, repr=False)
    tile: CompileTime[int] = field(derive=lambda op: TILE * TILE, repr=False)

    x = In(rows, hidden, obj_shape=(hidden,))
    ids = In(rows, top_k, dtype=np.int32, obj_shape=(top_k,))
    weights = In(rows, weights_width, obj_shape=(weights_width,))
    gate_up = In(experts, gate_up_width, hidden, obj_shape=(tile,))
    down = In(experts, hidden, width, obj_shape=(tile,))
    y = Out(rows, hidden, obj_shape=(hidden,))
    # Every row is still computed under a bound.
    valid = Extent(rows)

    def validate(self) -> None:
        if self.hidden % TILE or self.width % TILE:
            raise ValueError(
                f"Experts: hidden ({self.hidden}) and width ({self.width}) "
                f"must be whole {TILE}-wide tiles"
            )

    class Array(Operator.Array):
        def kernel(self):
            return moe.experts(
                hidden=self.hidden,
                width=self.width,
                num_experts=self.experts,
                top_k=self.top_k,
                rows=TILE,
                cols=TILE,
            )

        def build(self) -> Built:
            H, K = self.hidden, self.top_k
            steps = 3 * self.width * H // self.tile
            row = ObjectFifo(np.ndarray[(H + 4 * K,), np.dtype[bfloat16]], depth=1)
            parts = row.prod().join(
                [0, H, H + 2 * K],
                obj_types=[o.obj_type for o in (self.x, self.weights, self.ids)],
            )
            for o, f in zip((self.x, self.weights, self.ids), parts):
                o.bind(f.prod())
            tiles = ObjectFifo(self.gate_up.obj_type)
            self.gate_up.bind(tiles.prod())
            self.down.bind(tiles.prod())
            of_y = ObjectFifo(self.y.obj_type)
            self.y.bind(of_y.cons())

            def core_fn(of_row, of_tile, of_y, experts):
                for _ in range_(self.rows):
                    row, y = of_row.acquire(1), of_y.acquire(1)
                    for step in range_(self.experts * steps):
                        tile = of_tile.acquire(1)
                        experts(row, tile, y, arith.index_cast(step, to=T.i32()))
                        of_tile.release(1)
                    of_row.release(1)
                    of_y.release(1)

            worker = Worker(
                core_fn, [row.cons(), tiles.cons(), of_y.prod(), self.kernel()]
            )
            return Built([worker])

    def sequence(self, rt):
        """A row at a time: its inputs, every expert's tiles, its output."""
        H, I = self.hidden, self.width

        def tiles(e, rows, cols):
            """Expert ``e``'s ``rows`` x ``cols`` matrix, tile by tile."""
            return TensorAccessPattern(
                (self.experts, rows, cols),
                e * rows * cols,
                [rows // TILE, cols // TILE, TILE, TILE],
                [TILE * cols, TILE, cols, 1],
            )

        for r in range(self.rows):
            tg = TaskGroup()
            for operand in (self.x, self.weights, self.ids):
                operand.fill(operand[r : r + 1], group=tg)
            for e in range(self.experts):
                expert = TaskGroup()
                self.gate_up.fill(tiles(e, 2 * I, H), group=expert)
                self.down.fill(tiles(e, H, I), group=expert, wait=True)
                expert.finish()
            self.y.drain(self.y[r : r + 1], group=tg, wait=True)
            tg.finish()

    def tolerance(self):
        return Tolerance.relative(
            8e-3, range_frac=1e-3, note="f32 throughout, rounded once: a bf16 ulp"
        )

    def ops(self) -> int:
        return 6 * self.rows * self.top_k * self.width * self.hidden

    def reference(self, x, ids, weights, gate_up, down):
        x, weights = (np.asarray(a, np.float32) for a in (x, weights))
        y = np.zeros(x.shape, np.float32)
        for r, chosen in enumerate(np.asarray(ids)):
            for j, e in enumerate(chosen):
                g, u = np.split(gate_up[e].astype(np.float32) @ x[r], 2)
                h = g / (1 + np.exp(-g)) * u
                y[r] += weights[r, 2 * j] * (down[e].astype(np.float32) @ h)
        return y.astype(bfloat16)
