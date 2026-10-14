# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tiled-strided memory layouts for IRON operators.

A layout is a hierarchy of tiles, each level a ``(step, bound)`` stride, as
a kernel reads its operands. The types mirror ``snaxc.ir.tsl`` and import
snaxc only in ``to_snaxc``, so they work without the AIE codegen toolchain.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Stride:
    """One stride level: ``bound`` elements ``step`` apart, ``None`` for dynamic."""

    step: int | None
    bound: int | None


@dataclass
class TiledStride:
    """The strides of one tensor dimension, outermost tile first."""

    strides: tuple[Stride, ...]

    def __post_init__(self) -> None:
        self.strides = tuple(self.strides)


@dataclass
class TiledStridedLayout:
    """A tiled-strided layout: one ``TiledStride`` per tensor dimension."""

    tstrides: tuple[TiledStride, ...]
    offset: int = 0

    def __post_init__(self) -> None:
        self.tstrides = tuple(self.tstrides)

    def to_snaxc(self):
        """The equivalent ``snaxc.ir.tsl.TiledStridedLayout``."""
        from snaxc.ir.tsl import (
            Stride as SnaxStride,
        )
        from snaxc.ir.tsl import (
            TiledStride as SnaxTiledStride,
        )
        from snaxc.ir.tsl import (
            TiledStridedLayout as SnaxTiledStridedLayout,
        )

        return SnaxTiledStridedLayout(
            [
                SnaxTiledStride([SnaxStride(s.step, s.bound) for s in ts.strides])
                for ts in self.tstrides
            ],
            offset=self.offset,
        )


def tiled_2d(rows: int, cols: int, row_unit: int, col_unit: int) -> TiledStridedLayout:
    """Two-level layout: ``row_unit x col_unit`` tiles, row-major, of a
    ``rows x cols`` tensor, as stream-dse's GEMM and elementwise operands are.
    """
    rows_t, cols_t = rows // row_unit, cols // col_unit
    return TiledStridedLayout(
        (
            TiledStride(
                (
                    Stride(row_unit * col_unit * cols_t, rows_t),
                    Stride(col_unit, row_unit),
                )
            ),
            TiledStride((Stride(row_unit * col_unit, cols_t), Stride(1, col_unit))),
        )
    )
