# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import In, Out, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import datamovement
from aie.utils.compile.jit.params import divisors, param, per_call, tunable, widths
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Rtp
from iron.common.testing import Case, Testing


class Decode(Operator):
    """Coded rows (``aie.utils.coded``) in, the bf16 weights they code out:
    ``rows`` rows a kernel call, each column's core a block of them. Its A is
    coded by declaration, so in a graph it reads a weight's coded rows, as a
    coded GEMV does, and its output is the weight bit for bit.
    """

    test = Testing(
        [
            Case(dict(M=2048, K=2048, num_aie_columns=8, rows=1), bench=True),
            Case(dict(M=256, K=192, num_aie_columns=2, rows=2)),
            Case(dict(M=64, K=8192, num_aie_columns=4, rows=1), lower=True),
        ],
        draw=lambda op: dict(normal=(op.A,)),
    )

    M: int = param()
    K: int = param()
    capacity: int = param(default=15, array=True)
    num_aie_columns: int = tunable(domain=widths)
    # Rows a call: more amortize a row's loop entry, two of each tile per
    # core must fit beside the stack.
    rows: int = tunable(domain=lambda op, dev, t: divisors(t, of=op.M, span=3))

    A = In(
        M,
        K,
        obj_shape=(rows, K),
        per=(num_aie_columns,),
        coded=True,
        capacity=capacity,
    )
    out = Out(M, K, obj_shape=(rows, K), per=(num_aie_columns,))
    tiles = per_call(derive=lambda op: op.M // (op.num_aie_columns * op.rows))

    def validate(self) -> None:
        if self.K % 64:
            raise ValueError(
                f"Decode: K ({self.K}) must be a multiple of 64, the coded unit"
            )

    def resolve(self, dev):
        rows = self.rows or 1
        cols = self.resolve_columns(
            dev, self.num_aie_columns, fits=lambda c: self.M % (c * rows) == 0
        )
        return self.replace(num_aie_columns=cols, rows=rows)

    def compatible(self) -> None:
        share = self.num_aie_columns * self.rows
        if self.M % share:
            raise ValueError(
                f"Decode: M ({self.M}) must divide into {self.num_aie_columns} "
                f"columns of {self.rows}-row tiles"
            )

    def build(self) -> Built:
        rows = self.rows
        decode = datamovement.decode_coded(rows, self.K)
        a_ends = self.A.fifos(self.A.depth)
        out_ends = self.out.fifos(self.out.depth)
        rtps = [Rtp([self.tiles]) for _ in range(self.num_aie_columns)]

        def core(of_a, of_out, decode, rtp):
            n = rtp.read()[self.tiles]
            for _ in range_(n):
                a = of_a.acquire(1)
                y = of_out.acquire(1)
                decode(rows, a, y)
                of_a.release(1)
                of_out.release(1)

        workers = [
            Worker(core, [a_ends[i], out_ends[i], decode, rtps[i]])
            for i in range(self.num_aie_columns)
        ]
        return Built(workers, rtps)

    def ops(self) -> int:
        return 0

    def tolerance(self) -> Tolerance:
        return Tolerance.exact(note="a lossless decode")

    def reference(self, A):
        return np.asarray(A, bfloat16)
