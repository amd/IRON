# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import dataclasses

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, ObjectFifo, TaskGroup, Worker, WorkerRuntimeBarrier
from aie.iron.controlflow import range_
from aie.iron.device import Device
from aie.iron.kernels import datamovement
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import (
    In,
    Incompatible,
    Operator,
    Out,
    Value,
    auto,
    optional,
    param,
)
from iron.common.testing import Case, Testing


def _cases(cls, dev: Device):
    m = n = 64
    out = []
    for M in (64, 2048):
        for N in (64, 128, 256, 512):
            for cols in range(1, dev.cols + 1):
                for channels in (1, 2):
                    if (M // channels) % m or (N // cols) % n:
                        continue
                    if (M // channels) * (N // cols) * channels * cols != M * N:
                        continue
                    out.append(
                        Case(
                            dict(
                                M=M,
                                N=N,
                                num_aie_columns=cols,
                                num_channels=channels,
                                m=m,
                                n=n,
                                s=8,
                                num_batches=1,
                            ),
                            extensive=(M, N) != (2048, 64),
                        )
                    )
    # num_batches > 1: independent same-shape transposes in one dispatch, on
    # the regular shape; two batches in the default suite, four extensive.
    for batches in (2, 4):
        out.append(
            Case(
                dict(
                    M=2048,
                    N=64,
                    num_aie_columns=1,
                    num_channels=1,
                    m=m,
                    n=n,
                    s=8,
                    num_batches=batches,
                ),
                extensive=batches != 2,
            )
        )
    # Benched: 4 Mi elements, well past the dispatch cost. Each column takes a
    # 64-wide slice of N and each channel a 64-row-aligned slice of M.
    out.append(
        Case(
            dict(
                M=8192,
                N=512,
                num_aie_columns=dev.cols,
                num_channels=2,
                m=m,
                n=n,
                s=8,
                num_batches=1,
            ),
            bench=True,
        )
    )
    return out


class Transpose(Operator):
    """AIE-accelerated shuffle transpose: one core per (column, channel).

    The memtile partially transposes each m x n tile on the way in so a core
    only transposes s x s sub-tiles. The three trip counts (batches, tiles
    per column, tiles per channel) are values the sequence writes.

    ``num_batches`` > 1 performs that many independent (M,N)->(N,M) transposes on
    contiguous matrices laid back-to-back in memory (results concatenated),
    mirroring GEMV's batching: the per-batch tile work rides the same
    ObjectFifos, so B batched transposes cost ONE dispatch instead of B.
    """

    # A transpose is a permutation. Any tolerance here also accepts some class
    # of wrong permutation, so gate it exactly.
    test = Testing(_cases, tolerance=Tolerance.exact())

    M: int = param()
    N: int = param()
    num_batches: int = param(default=1)
    # Defaults: 64 x 64 tiles of 8 x 8 sub-tiles, every column, one channel.
    m: int = auto(64)
    n: int = auto(64)
    s: int = auto(8, array=True)
    num_aie_columns: int = auto()
    num_channels: int = auto(1)

    x = In(
        optional(num_batches), M, N, tile=(m, n), per=(num_aie_columns, num_channels)
    )
    y = Out(
        optional(num_batches), N, M, tile=(m, n), per=(num_aie_columns, num_channels)
    )
    batches = Value(np.int32, derive=lambda op: op.num_batches)
    col_tiles = Value(np.int32, derive=lambda op: op.N // op.n // op.num_aie_columns)
    chan_tiles = Value(np.int32, derive=lambda op: op.M // op.m // op.num_channels)

    def validate(self) -> None:
        if self.m % self.s != 0:
            raise ValueError(f"AIE tile rows ({self.m}) must be a multiple of {self.s}")
        if self.n % self.s != 0:
            raise ValueError(
                f"AIE tile columns ({self.n}) must be a multiple of {self.s}"
            )
        if self.m * self.n > 8192:
            raise ValueError(
                f"Kernel tile size {self.m * self.n} needs to be below 8192 to fit within data memory."
            )
        if self.s == 4 and (self.m <= 4 or self.n <= 4):
            raise ValueError(
                f"Kernel tile {self.s} needs AIE tile rows > 4 and columns > 4."
            )
        if self.s == 8 and (self.m <= 16 or self.n <= 16):
            raise ValueError(
                f"Kernel tile {self.s} needs AIE tile rows > 16 and columns > 16."
            )

    def resolve(self, dev):
        """Columns default to the most the device's shim budget allows that
        split N into whole n-wide tiles.
        """
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
            raise Incompatible(f"Matrix rows ({self.M}) must be a multiple of {self.m}")
        if self.N % self.n != 0:
            raise Incompatible(
                f"Matrix columns ({self.N}) must be a multiple of {self.n}"
            )
        # The design tiles each dimension separately, as
        # [M // num_channels // m, N // num_columns // n, m, n]. A quotient
        # that is not a whole number of tiles silently drops the remainder,
        # and one that floors to zero reaches the transfer as a zero-length
        # size, so each split is checked on its own, then the product.
        if (self.N // cols) % self.n:
            raise Incompatible(
                f"num_aie_columns ({cols}) does not split N={self.N} "
                f"into whole n-wide tiles: each column gets "
                f"{self.N // cols} columns, which is not a multiple "
                f"of n={self.n}"
            )
        if (self.M // chans) % self.m:
            raise Incompatible(
                f"num_channels ({chans}) does not split M={self.M} "
                f"into whole m-tall tiles: each channel gets "
                f"{self.M // chans} rows, which is not a multiple "
                f"of m={self.m}"
            )
        if self.M * self.N % (self.m * self.n * cols * chans) != 0:
            raise Incompatible(
                f"M x N ({self.M} x {self.N}) is not whole {self.m} x {self.n} tiles "
                f"over {cols} columns x {chans} channels"
            )

    def array(self, target) -> list:

        m, n, s = self.m, self.n, self.s
        cols, chans = self.num_aie_columns, self.num_channels
        n_cores = cols * chans
        tile_ty = np.ndarray[(m * n,), np.dtype[bfloat16]]
        depth = target.fifo_depth(m * n, self.x.dtype)
        l2l1 = TensorAccessPattern.full((n // s, s, m // s, s)).permute((2, 1, 0, 3))

        kernel = datamovement.transpose(m, n, s)
        of_l3l2 = [
            ObjectFifo(tile_ty, name=f"of_in1s_L3L2_{i}_{j}", depth=depth)
            for i in range(cols)
            for j in range(chans)
        ]
        of_l2l1 = [
            of_l3l2[k]
            .cons(from_stream=l2l1)
            .forward(
                obj_type=tile_ty,
                name=f"of_in1s_L2L1_{k // chans}_{k % chans}",
                depth=depth,
            )
            for k in range(n_cores)
        ]
        of_outs = [
            ObjectFifo(tile_ty, name=f"out_{i}_{j}", depth=depth)
            for i in range(cols)
            for j in range(chans)
        ]
        i32x3 = np.ndarray[(3,), np.dtype[np.int32]]
        counts = [
            Buffer(i32x3, name=f"counts_{k}", use_write_rtp=True)
            for k in range(n_cores)
        ]
        barriers = [WorkerRuntimeBarrier() for _ in range(n_cores)]

        def core_body(of_in, of_out, transpose, counts, barrier):
            barrier.wait_for_value(1)
            batches = counts[0]
            col_tiles = counts[1]
            chan_tiles = counts[2]
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
                [of_l2l1[k].cons(), of_outs[k].prod(), kernel, counts[k], barriers[k]],
            )
            for k in range(n_cores)
        ]
        for k in range(n_cores):
            self.x.lane(k).bind(of_l3l2[k].prod())
            self.y.lane(k).bind(of_outs[k].cons())
        self.batches.bind(counts, 0)
        self.col_tiles.bind(counts, 1)
        self.chan_tiles.bind(counts, 2)
        return workers + barriers

    def sequence(self, rt):
        """One task group per batch (a parallel fill+drain over all cores), so the
        contiguous matrices stream through the same fifos in sequence.
        """
        M, N, nb = self.M, self.N, self.num_batches
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
                    # Partially transposes the input on the way in so the
                    # kernel only transposes s x s sub-tiles.
                    tap_in = x[batch, j, :, :, i].permute((0, 2, 1, 3))
                    rt.fill(self.x.lane(k), tap_in, group=tg)
            for i in range(cols):
                for j in range(chans):
                    k = i * chans + j
                    tap_out = y[batch, i, :, :, j].permute((2, 0, 1, 3))
                    rt.drain(self.y.lane(k), tap_out, group=tg, wait=True)
            tg.finish()

    def ops(self) -> int:
        return 0  # a data mover: its figure is bandwidth

    def reference(self, x):
        """Each (M, N) matrix transposed."""
        # Not datamovement.transpose's contract: the kernel transposes each
        # subtile in place, and the DMA places the subtiles.
        return np.swapaxes(x, -2, -1)
