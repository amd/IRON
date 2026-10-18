# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import dataclasses

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import ObjectFifo, TaskGroup, Worker
from aie.iron.controlflow import range_
from aie.iron.device import Device
from aie.iron.kernels import datamovement
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import (
    Auto,
    Built,
    Divisors,
    In,
    Operand,
    Operator,
    Out,
    Param,
    Rtp,
    Value,
)
from iron.common.testing import Case, Testing


def _cases(cls, dev: Device):
    m = n = 64
    tiles = dict(m=m, n=n, s=8)
    out = [
        Case(dict(M=2048, N=64, num_aie_columns=1, num_channels=c, **tiles))
        for c in (1, 2)
    ]
    # num_batches > 1: independent same-shape transposes in one dispatch.
    out.append(
        Case(
            dict(
                M=2048, N=64, num_aie_columns=1, num_channels=1, **tiles, num_batches=2
            )
        )
    )
    # One tile, and the widest grid.
    out += [
        Case(
            dict(M=64, N=64, num_aie_columns=1, num_channels=1, **tiles),
            extensive=True,
        ),
        Case(
            dict(M=2048, N=512, num_aie_columns=dev.cols, num_channels=2, **tiles),
            extensive=True,
        ),
    ]
    out.append(
        Case(
            dict(M=8192, N=512, num_aie_columns=dev.cols, num_channels=2, **tiles),
            bench=True,
        )
    )
    return out


class Transpose(Operator):
    """AIE-accelerated shuffle transpose: one core per (column, channel).

    The memtile partially transposes each m x n tile on the way in, so a core
    only transposes s x s sub-tiles; ``num_batches`` transposes ride one
    dispatch.
    """

    test = Testing(_cases)

    M: int = Param()
    N: int = Param()
    num_batches: int | None = Param(default=None)
    m: int = Auto(
        default=64,
        domain=Divisors(
            of=lambda op, dev: op.M,
            step=lambda op, dev: op.s,
            cap=lambda op, dev: 8192 // op.n,
        ),
    )
    n: int = Auto(
        default=64,
        domain=Divisors(
            of=lambda op, dev: op.N,
            step=lambda op, dev: op.s,
            cap=lambda op, dev: 8192 // op.m,
        ),
    )
    s: int = Auto(default=8, domain=(8, 4))
    num_aie_columns: int = Auto()
    num_channels: int = Auto(default=1)

    x = In(num_batches, M, N, obj_type=(m, n), per=(num_aie_columns, num_channels))
    y = Out(num_batches, N, M, obj_type=(m, n), per=(num_aie_columns, num_channels))
    batches = Value(derive=lambda op: op.num_batches or 1)
    col_tiles = Value(derive=lambda op: op.N // op.n // op.num_aie_columns)
    chan_tiles = Value(derive=lambda op: op.M // op.m // op.num_channels)

    def validate(self) -> None:
        if self.m % self.s != 0:
            raise ValueError(
                f"Transpose: m ({self.m}) must be a multiple of s ({self.s})"
            )
        if self.n % self.s != 0:
            raise ValueError(
                f"Transpose: n ({self.n}) must be a multiple of s ({self.s})"
            )
        if self.m * self.n > 8192:
            raise ValueError(
                f"Transpose: m x n ({self.m * self.n}) must be at most 8192 to fit "
                f"data memory"
            )
        if self.s == 4 and (self.m <= 4 or self.n <= 4):
            raise ValueError(
                f"Transpose: m and n ({self.m}, {self.n}) must be above 4 when s is 4"
            )
        if self.s == 8 and (self.m <= 16 or self.n <= 16):
            raise ValueError(
                f"Transpose: m and n ({self.m}, {self.n}) must be above 16 when s is 8"
            )

    def resolve(self, dev):
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            self.num_channels,
            fits=lambda c: self.N % c == 0 and (self.N // c) % self.n == 0,
        )
        return dataclasses.replace(self, num_aie_columns=cols)

    def compatible(self) -> None:
        cols, chans = self.num_aie_columns, self.num_channels
        if self.M % self.m != 0:
            raise ValueError(
                f"Transpose: M ({self.M}) must be a multiple of m ({self.m})"
            )
        if self.N % self.n != 0:
            raise ValueError(
                f"Transpose: N ({self.N}) must be a multiple of n ({self.n})"
            )
        # Each split on its own: a partial tile would be silently dropped.
        if (self.N // cols) % self.n:
            raise ValueError(
                f"Transpose: num_aie_columns ({cols}) does not split N ({self.N}) "
                f"into whole n-wide tiles: each column gets "
                f"{self.N // cols} columns, which is not a multiple "
                f"of n ({self.n})"
            )
        if (self.M // chans) % self.m:
            raise ValueError(
                f"Transpose: num_channels ({chans}) does not split M ({self.M}) "
                f"into whole m-tall tiles: each channel gets "
                f"{self.M // chans} rows, which is not a multiple "
                f"of m ({self.m})"
            )
        if self.M * self.N % (self.m * self.n * cols * chans) != 0:
            raise ValueError(
                f"Transpose: M x N ({self.M} x {self.N}) is not whole {self.m} x {self.n} tiles "
                f"over {cols} columns x {chans} channels"
            )

    class Array(Operator.Array):
        m: int
        n: int
        num_aie_columns: int
        num_channels: int
        s: int
        batches: Value
        chan_tiles: Value
        col_tiles: Value
        x: Operand
        y: Operand

        def build(self) -> Built:

            m, n, s = self.m, self.n, self.s
            cols, chans = self.num_aie_columns, self.num_channels
            n_cores = cols * chans
            tile_ty = np.ndarray[(m * n,), np.dtype[bfloat16]]
            depth = self.x.l1_depth
            l2l1 = TensorAccessPattern.full((n // s, s, m // s, s)).permute(
                (2, 1, 0, 3)
            )

            kernel = datamovement.transpose(m, n, s)
            of_l3l2 = [
                ObjectFifo(tile_ty, depth=depth)
                for i in range(cols)
                for j in range(chans)
            ]
            of_l2l1 = [
                of_l3l2[k]
                .cons(from_stream=l2l1)
                .forward(
                    obj_type=tile_ty,
                    depth=depth,
                )
                for k in range(n_cores)
            ]
            of_outs = [
                ObjectFifo(tile_ty, depth=depth)
                for i in range(cols)
                for j in range(chans)
            ]
            rtps = [
                Rtp([self.batches, self.col_tiles, self.chan_tiles])
                for _ in range(n_cores)
            ]

            def core_body(of_in, of_out, transpose, rtp):
                words = rtp.read()
                batches = words[self.batches]
                col_tiles = words[self.col_tiles]
                chan_tiles = words[self.chan_tiles]
                # The kernel only ever sees s*s sub-tiles, so it is batch-agnostic.
                for _ in range_(batches):
                    for _ in range_(col_tiles):
                        for _ in range_(chan_tiles):
                            elem_in = of_in.acquire(1)
                            elem_out = of_out.acquire(1)
                            transpose(elem_in, elem_out)
                            of_out.release(1)
                            of_in.release(1)

            workers = [
                Worker(
                    core_body,
                    [of_l2l1[k].cons(), of_outs[k].prod(), kernel, rtps[k]],
                )
                for k in range(n_cores)
            ]
            self.x.bind([f.prod() for f in of_l3l2])
            self.y.bind([f.cons() for f in of_outs])
            return Built(workers, rtps)

    def sequence(self, rt):
        """One task group per batch through the same fifos."""
        M, N, nb = self.M, self.N, self.num_batches or 1
        m, n, cols, chans = self.m, self.n, self.num_aie_columns, self.num_channels
        # Each core's block of a batch: chans row-bands, cols column-bands.
        x = TensorAccessPattern.full(
            (nb, chans, M // chans // m, m, cols, N // cols // n, n)
        )
        y = TensorAccessPattern.full(
            (nb, cols, N // cols // n, n, chans, M // chans // m, m)
        )
        for batch in range(nb):
            tg = TaskGroup()
            for i in range(cols):
                for j in range(chans):
                    k = i * chans + j
                    tap_in = x[batch, j, :, :, i].permute((0, 2, 1, 3))
                    self.x.fill(tap_in, lane=k, group=tg)
            for i in range(cols):
                for j in range(chans):
                    k = i * chans + j
                    tap_out = y[batch, i, :, :, j].permute((2, 0, 1, 3))
                    self.y.drain(tap_out, lane=k, group=tg, wait=True)
            tg.finish()

    def ops(self) -> int:
        return 0  # a data mover: its figure is bandwidth

    def reference(self, x):
        """Each (M, N) matrix transposed."""
        # Not the kernel's contract: the DMA places the subtiles.
        return np.swapaxes(x, -2, -1)

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()
