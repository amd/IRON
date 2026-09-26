# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import dataclasses

from aie.iron.kernels import datamovement
import numpy as np
from ml_dtypes import bfloat16

from aie.utils.verify import Tolerance

from iron.common.declare import (
    Movement,
    Semantics,
    BoundBuffer,
    Incompatible,
    In,
    Operator,
    Order,
    Out,
    Overlay,
    Resident,
    StreamIn,
    StreamOut,
    Untunable,
    dim,
    operator,
    optional,
    tunable,
)
from iron.common.testing import Case, Testing, device_columns
from iron.common.tiling import Access


@operator
class TransposeOverlay(Overlay):
    """The array for a shuffle transpose: one core per (column, channel).

    The memtile partially transposes each m x n tile on the way in so a core
    only transposes s x s sub-tiles. The three trip counts (batches, tiles
    per column, tiles per channel) are residents the sequence writes.
    """

    # Defaults: 64 x 64 tiles of 8 x 8 sub-tiles, every column, one channel.
    m: int = tunable(64)
    n: int = tunable(64)
    s: int = tunable(8)
    num_aie_columns: int | None = tunable(None)
    num_channels: int = tunable(1)

    x = StreamIn(m, n, per=(num_aie_columns, num_channels))
    y = StreamOut(m, n, per=(num_aie_columns, num_channels))
    batches = Resident(np.int32)
    col_tiles = Resident(np.int32)
    chan_tiles = Resident(np.int32)

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

    def tuning(self, dev) -> "TransposeOverlay":
        cols = self.num_aie_columns
        if cols is None:
            if dev is None:
                raise Untunable("num_aie_columns defaults from the device; none given")
            cols = self.shim_columns(dev, self.num_channels)
        elif dev is not None:
            self.check_shim_columns(dev, cols, self.num_channels)
        return dataclasses.replace(self, num_aie_columns=cols)

    def semantics(self) -> Semantics:
        return Movement(has_cores=True)

    def design(self, target) -> list:
        from aie.iron import ObjectFifo, Worker
        from aie.iron.controlflow import range_

        m, n, s = self.m, self.n, self.s
        cols, chans = self.num_aie_columns, self.num_channels
        n_cores = cols * chans
        tile_ty = np.ndarray[(m * n,), np.dtype[bfloat16]]
        depth = 1 if m * n > 4096 else 2
        # The memtile reshuffle: sizes/strides only, so it is extent-free.
        l2l1 = [m // s, s, n // s, s], [s, m, s * m, 1]

        kernel = datamovement.transpose(m, n, s)
        of_l3l2 = [
            ObjectFifo(tile_ty, name=f"of_in1s_L3L2_{i}_{j}", depth=depth)
            for i in range(cols)
            for j in range(chans)
        ]
        of_l2l1 = [
            of_l3l2[k]
            .cons(dims_from_stream=_transformation_dims(*l2l1))
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
        counts = [target.rtp(i32x3, name=f"counts_{k}") for k in range(n_cores)]
        barriers = [target.barrier() for _ in range(n_cores)]

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
            self.x[k].bind(of_l3l2[k].prod())
            self.y[k].bind(of_outs[k].cons())
        self.batches.bind(counts, 0)
        self.col_tiles.bind(counts, 1)
        self.chan_tiles.bind(counts, 2)
        return workers


def _transformation_dims(sizes, strides):
    """What ``TensorAccessPattern.transformation_dims`` returns for these sizes/strides."""
    from aie.helpers.taplib.tap import TensorAccessPattern

    return TensorAccessPattern((1, 1), 0, sizes, strides).transformation_dims


def _cases():
    m = n = 64
    out = []
    for M in (64, 2048):
        for N in (64, 128, 256, 512):
            for cols in range(1, device_columns() + 1):
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
    return out


@operator
class Transpose(Operator[TransposeOverlay]):
    """AIE-accelerated transpose operator.

    ``num_batches`` > 1 performs that many independent (M,N)->(N,M) transposes on
    contiguous matrices laid back-to-back in memory (results concatenated),
    mirroring GEMV's batching: the per-batch tile work rides the same
    ObjectFifos, so B batched transposes cost ONE dispatch instead of B.
    """

    # A transpose is a permutation. Any tolerance here also accepts some class
    # of wrong permutation, so gate it exactly.
    test = Testing(_cases, tolerance=Tolerance.exact())

    M: int = dim()
    N: int = dim()
    num_batches: int = dim(1)

    x = In(optional(num_batches), M, N, to=TransposeOverlay.x)
    y = Out(optional(num_batches), N, M, from_=TransposeOverlay.y)

    def compatible(self) -> None:
        ov = self.ov
        if self.M % ov.m != 0:
            raise Incompatible(f"Matrix rows ({self.M}) must be a multiple of {ov.m}")
        if self.N % ov.n != 0:
            raise Incompatible(
                f"Matrix columns ({self.N}) must be a multiple of {ov.n}"
            )
        if self.M * self.N % (ov.m * ov.n * ov.num_aie_columns * ov.num_channels) != 0:
            raise Incompatible(
                "Transfer size must be divisible by m*n*num_columns*num_channels"
            )
        # The product check is necessary but not sufficient: the design tiles each
        # dimension separately, as [M // num_channels // m, N // num_columns // n, m, n].
        # A quotient that is not a whole number of tiles silently drops the remainder,
        # and one that floors to zero reaches the transfer as a zero-length size.
        if (self.N // ov.num_aie_columns) % ov.n:
            raise Incompatible(
                f"num_aie_columns ({ov.num_aie_columns}) does not split N={self.N} "
                f"into whole n-wide tiles: each column gets "
                f"{self.N // ov.num_aie_columns} columns, which is not a multiple "
                f"of n={ov.n}"
            )
        if (self.M // ov.num_channels) % ov.m:
            raise Incompatible(
                f"num_channels ({ov.num_channels}) does not split M={self.M} "
                f"into whole m-tall tiles: each channel gets "
                f"{self.M // ov.num_channels} rows, which is not a multiple "
                f"of m={ov.m}"
            )

    def residents(self) -> dict[str, int]:
        ov = self.ov
        return {
            "batches": self.num_batches,
            "col_tiles": self.N // ov.n // ov.num_aie_columns,
            "chan_tiles": self.M // ov.m // ov.num_channels,
        }

    def order(self, buffer: BoundBuffer) -> Order:
        """Per core, one descriptor per batch over its (M / chans) x (N / cols)
        block, in m x n tiles. The input is partially transposed on the way
        in, so the kernel only transposes s x s sub-tiles."""
        ov = self.ov
        M, N, nb = self.M, self.N, self.num_batches
        m, n, cols, chans = ov.m, ov.n, ov.num_aie_columns, ov.num_channels
        elems = M * N
        if buffer is self.x:
            return Order(
                ov.x,
                tuple(
                    tuple(
                        Access(
                            self.x.elements,
                            batch * elems + (M // chans) * j * N + (N // cols) * i,
                            (M // chans // m, N // cols // n, m, n),
                            (m * N, n, N, 1),
                        )
                        for batch in range(nb)
                    )
                    for i in range(cols)
                    for j in range(chans)
                ),
            )
        return Order(
            ov.y,
            tuple(
                tuple(
                    Access(
                        self.y.elements,
                        batch * elems + (N // cols) * i * M + (M // chans) * j,
                        (M // chans // m, N // cols // n, n, m),
                        (m, n * M, M, 1),
                    )
                    for batch in range(nb)
                )
                for i in range(cols)
                for j in range(chans)
            ),
        )

    def design(self, rt):
        """One task group per batch (a parallel fill+drain over all cores), so the
        contiguous matrices stream through the same fifos in sequence."""
        ov = self.ov
        src, dst = self.order(self.x), self.order(self.y)
        for batch in range(self.num_batches):
            with rt.group() as tg:
                for k in range(len(src.slots)):
                    rt.fill(ov.x[k], (self.x, src[k][batch]), group=tg)
                for k in range(len(dst.slots)):
                    rt.drain(ov.y[k], (self.y, dst[k][batch]), group=tg, wait=True)

    def reference(self, x):
        """CPU reference: 2D transpose of each (M, N) matrix stored row-major."""
        if self.num_batches > 1:
            return reference(x.reshape(self.num_batches, self.M, self.N))
        return reference(x.reshape(self.M, self.N))


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def reference(x):
    """CPU reference: 2D transpose of an ``(rows, cols)`` matrix (ground truth);
    of each matrix when a batch dimension leads."""
    return np.swapaxes(x, -2, -1)
