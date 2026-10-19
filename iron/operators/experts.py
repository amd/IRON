# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Experts: a mixture of experts' feed-forwards, each row through the
experts ``TopKRouter`` chose for it.
"""

import numpy as np
from aie.extras.dialects import arith
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, CompileTime, In, ObjectFifo, Out, TaskGroup, Worker
from aie.iron import kernels
from aie.iron.controlflow import if_, range_
from aie.iron.kernels import moe
from ml_dtypes import bfloat16

from iron.common import Built, Extent, Operator, field
from iron.common.testing import Case, Testing

#: The rows of ``width`` each kernel call takes.
TILE = 2


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

    One core, scalar: every row streams every expert's weights in tiles of
    ``TILE`` rows of ``width``, and the core computes the tiles of the
    experts the row chose, summing in float32.
    """

    test = Testing(
        [
            Case(dict(rows=2, hidden=256, width=64, experts=4, top_k=2)),
            Case(dict(rows=8, hidden=512, width=256, experts=8, top_k=2), bench=True),
        ],
        draw=_routed,
    )

    rows: CompileTime[int] = field()
    hidden: CompileTime[int] = field()
    width: CompileTime[int] = field()
    experts: CompileTime[int] = field()
    top_k: CompileTime[int] = field()
    weights_width: CompileTime[int] = field(derive=lambda op: 2 * op.top_k, repr=False)
    gate_up_width: CompileTime[int] = field(derive=lambda op: 2 * op.width, repr=False)
    gate_up_tile: CompileTime[int] = field(
        derive=lambda op: 2 * TILE * op.hidden, repr=False
    )
    down_tile: CompileTime[int] = field(derive=lambda op: TILE * op.hidden, repr=False)

    x = In(rows, hidden, obj_shape=(hidden,))
    ids = In(rows, top_k, dtype=np.int32, obj_shape=(top_k,))
    # A row's weights, one object per expert: the router's pair.
    weights = In(rows, weights_width, obj_shape=(2,), depth=top_k)
    gate_up = In(experts, gate_up_width, hidden, obj_shape=(gate_up_tile,), depth=1)
    down = In(experts, hidden, width, obj_shape=(down_tile,), depth=1)
    y = Out(rows, hidden, obj_shape=(hidden,))
    # Every row is still computed under a bound.
    valid = Extent(rows)

    def validate(self) -> None:
        if self.width % TILE:
            raise ValueError(
                f"Experts: width ({self.width}) is not a whole number of {TILE}-row tiles"
            )

    class Array(Operator.Array):
        def gate_up_kernel(self):
            return moe.expert_gate_up(rows=TILE, hidden=self.hidden)

        def down_kernel(self):
            # A tile of TILE of down's columns, every row of hidden.
            return moe.expert_down(rows=self.hidden, width=TILE)

        def build(self) -> Built:
            H, K = self.hidden, self.top_k
            ins = (self.x, self.ids, self.weights, self.gate_up, self.down)
            of_ins = [ObjectFifo(o.obj_type, depth=o.depth) for o in ins]
            of_y = ObjectFifo(self.y.obj_type, depth=self.y.depth)
            f32 = lambda n: np.ndarray[(n,), np.dtype[np.float32]]

            def core_fn(of_x, of_ids, of_w, of_gu, of_dn, of_y, *fns):
                gate_up, down, zero, convert, acc, h = fns
                for _ in range_(self.rows):
                    x, ids, w = of_x.acquire(1), of_ids.acquire(1), of_w.acquire(K)
                    pairs = [w] if K == 1 else [w[j] for j in range(K)]
                    zero(acc)
                    for e in range_(self.experts):
                        for _ in range_(self.width // TILE):
                            gu, dn = of_gu.acquire(1), of_dn.acquire(1)
                            for j in range(K):
                                with if_(arith.index_cast(e, to=ids[j].type) == ids[j]):
                                    gate_up(x, gu, h)
                                    down(h, dn, pairs[j], acc)
                            of_gu.release(1)
                            of_dn.release(1)
                    y = of_y.acquire(1)
                    convert(acc, y, H)
                    of_y.release(1)
                    of_x.release(1)
                    of_ids.release(1)
                    of_w.release(K)

            worker = Worker(
                core_fn,
                [
                    *(f.cons() for f in of_ins),
                    of_y.prod(),
                    self.gate_up_kernel(),
                    self.down_kernel(),
                    kernels.zero(H, np.float32),
                    kernels.datamovement.convert_copy(H),
                    Buffer(f32(H)),
                    Buffer(f32(TILE)),
                ],
            )
            for operand, f in zip(ins, of_ins):
                operand.bind(f.prod())
            self.y.bind(of_y.cons())
            return Built([worker])

    def sequence(self, rt):
        """A row at a time: its inputs, every expert's tiles, its output."""
        X, H, I = self.experts, self.hidden, self.width
        # Each tile of an expert's gate rows, then the up rows they pair with.
        gate_up = TensorAccessPattern(
            (X, 2 * I, H),
            0,
            [X, I // TILE, 2, TILE * H],
            [2 * I * H, TILE * H, I * H, 1],
        )
        # Each tile of TILE of an expert's down columns, row by row.
        down = TensorAccessPattern(
            (X, H, I), 0, [X, I // TILE, H, TILE], [H * I, TILE, I, 1]
        )
        for r in range(self.rows):
            tg = TaskGroup()
            for operand in (self.x, self.ids, self.weights):
                operand.fill(operand[r : r + 1], group=tg)
            self.gate_up.fill(gate_up, group=tg)
            self.down.fill(down, group=tg)
            self.y.drain(self.y[r : r + 1], group=tg, wait=True)
            tg.finish()

    def tolerance(self):
        return self.array_config().down_kernel().contract.tolerance

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
