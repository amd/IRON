# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""TopKRouter: each row's ``top_k`` experts and their weights, on the device.

Bit for bit as ``aie.iron.kernels.moe.router_top_k_ref``: the exact top
``top_k`` of a row of bf16 router logits, the lowest indices winning a tie,
and a softmax over the chosen logits. A select core reduces each row to a
``sample_select`` summary and a router core turns it into the ids and the
weights, a pair of cores for each lane of rows.
"""

import dataclasses

import numpy as np
from aie.iron import Buffer, ObjectFifo, Worker, ceildiv
from aie.iron.controlflow import range_
from aie.iron.kernels import moe, sample
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import (
    Auto,
    Built,
    Extent,
    In,
    Operator,
    Out,
    Param,
    Rtp,
    Unresolvable,
    Value,
)
from iron.common.testing import Case, Testing


def _logits(op: "TopKRouter") -> dict:
    """Rows of logits, each with ties straddling its ``top_k``-th."""
    rng = np.random.default_rng(13)
    logits = rng.normal(0, 3, (op.rows, op.experts)).astype(bfloat16)
    for row in logits:
        boundary = np.sort(row.astype(np.float32))[::-1][op.top_k - 1]
        row[rng.choice(op.experts, min(4, op.experts), replace=False)] = boundary
    return dict(given={op.logits: logits})


class TopKRouter(Operator):
    """Each of ``rows`` rows of ``experts`` router logits to its ``top_k``
    expert ids and weights: ``weights`` holds a row's ``i``-th weight at
    ``2 * i``, a zero after each.
    """

    test = Testing(
        [
            Case(dict(experts=32, top_k=8), id="one_row"),
            Case(dict(experts=64, top_k=6, rows=16, pairs=4), id="rows", lower=True),
            Case(dict(experts=32, top_k=8, rows=256, pairs=8), id="chunk", bench=True),
        ],
        draw=_logits,
    )

    experts: int = Param()
    top_k: int = Param()
    rows: int = Param(default=1)
    weights_width: int = Param(derive=lambda op: 2 * op.top_k, repr=False)
    pairs: int = Auto()

    logits = In(rows, experts, obj_shape=(experts,), per=(pairs,))
    ids = Out(rows, top_k, dtype=np.int32, obj_shape=(top_k,), per=(pairs,))
    weights = Out(rows, weights_width, obj_shape=(weights_width,), per=(pairs,))
    valid = Extent(rows)
    count = Value(derive=lambda op: ceildiv(op.valid, op.pairs))

    def validate(self) -> None:
        if not 1 <= self.top_k <= self.experts:
            raise ValueError(
                f"TopKRouter: top_k ({self.top_k}) must be from 1 to experts "
                f"({self.experts})"
            )

    def resolve(self, dev):
        pairs = self.pairs or max(
            p for p in range(1, dev.cols + 1) if self.rows % p == 0
        )
        if self.rows % pairs or pairs > dev.cols:
            raise Unresolvable(
                f"TopKRouter: {self.rows} rows over {pairs} pairs of cores, on a "
                f"device of {dev.cols} columns"
            )
        return dataclasses.replace(self, pairs=pairs)

    def compatible(self) -> None:
        config = self.array_config()
        config.select()
        config.route()

    class Array(Operator.Array):
        def select(self):
            return sample.sample_select(
                slice_size=self.experts, chunk=self.experts, k_max=self.top_k
            )

        def route(self):
            return moe.router_top_k(slice_size=self.experts, top_k=self.top_k)

        def build(self) -> Built:
            select, route = self.select(), self.route()
            words = sample.summary_words(self.experts, self.top_k)
            summary_ty = np.ndarray[(words,), np.dtype[np.int32]]

            def select_body(of_x, of_sum, kernel, row, state, rtp):
                n = rtp.read()[self.count]
                for _ in range_(n):
                    x, summary = of_x.acquire(1), of_sum.acquire(1)
                    kernel(x, row, state, summary)
                    of_x.release(1)
                    of_sum.release(1)

            def route_body(of_sum, of_ids, of_weights, kernel, rtp):
                n = rtp.read()[self.count]
                for _ in range_(n):
                    summary = of_sum.acquire(1)
                    ids, weights = of_ids.acquire(1), of_weights.acquire(1)
                    kernel(summary, ids, weights)
                    of_sum.release(1)
                    of_ids.release(1)
                    of_weights.release(1)

            workers, rtps, lanes = [], [], ([], [], [])
            for _ in range(self.pairs):
                of_x = ObjectFifo(self.logits.obj_type, depth=self.logits.depth)
                of_ids = ObjectFifo(self.ids.obj_type, depth=self.ids.depth)
                of_weights = ObjectFifo(self.weights.obj_type, depth=self.weights.depth)
                of_sum = ObjectFifo(summary_ty, depth=2)
                for lane, end in zip(
                    lanes, (of_x.prod(), of_ids.cons(), of_weights.cons())
                ):
                    lane.append(end)
                # The select kernel reads only the row's top-k: always this one's.
                row = Buffer(
                    np.ndarray[(sample.ROW_WORDS,), np.dtype[np.int32]],
                    initial_value=sample.draw_row(1.0, self.top_k, 0),
                )
                state = Buffer(
                    np.ndarray[(sample.SELECT_STATE_WORDS,), np.dtype[np.int32]],
                    initial_value=np.zeros(sample.SELECT_STATE_WORDS, np.int32),
                )
                pair = [Rtp([self.count]), Rtp([self.count])]
                rtps += pair
                workers += [
                    Worker(
                        select_body,
                        [of_x.cons(), of_sum.prod(), select, row, state, pair[0]],
                    ),
                    Worker(
                        route_body,
                        [
                            of_sum.cons(),
                            of_ids.prod(),
                            of_weights.prod(),
                            route,
                            pair[1],
                        ],
                    ),
                ]
            for operand, ends in zip((self.logits, self.ids, self.weights), lanes):
                operand.bind(ends)
            return Built(workers, rtps)

    def ops(self) -> int:
        return 0  # a selection and a small softmax: its figure is latency

    def reference(self, logits):
        """``(ids, weights)``, ``router_top_k_ref`` row by row."""
        logits = np.asarray(logits).reshape(self.rows, self.experts)
        ids, weights = zip(*(moe.router_top_k_ref(row, self.top_k) for row in logits))
        return np.stack(ids), np.stack(weights)

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()
