# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tiled-strided memory layouts for IRON operators.

A tiled-strided layout describes how a logical multi-dimensional tensor is laid
out in memory as a hierarchy of tiles, each level carrying its own ``(step,
bound)`` stride. It is the layout model AIE kernels are written against: a GEMM
microkernel, for example, reads its ``MxK`` operand as ``mt x kt`` tiles of
``r x s`` elements, which is exactly a two-level tiled-strided layout.

The types here mirror ``snaxc.ir.tsl`` (``Stride`` -> ``TiledStride`` ->
``TiledStridedLayout``) so an IRON-authored layout can be handed to stream-dse's
code generation verbatim via :meth:`TiledStridedLayout.to_snaxc`. They carry no
stream-dse / snaxc / xdsl dependency themselves -- the snaxc import is lazy and
confined to ``to_snaxc`` -- so they are usable (and testable) in a plain IRON
install with no AIE codegen toolchain present.

This is a common primitive: it is meant to be shared across operators as the one
place a kernel's operand layouts are defined, rather than re-derived per operator
or hand-copied into stream-dse.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Stride:
    """One stride level: ``bound`` elements spaced ``step`` apart.

    ``step``/``bound`` may be ``None`` to denote a dynamic (run-time) value,
    matching snaxc's convention.
    """

    step: int | None
    bound: int | None


@dataclass
class TiledStride:
    """The strides of a single tensor dimension, outermost tile first.

    A simple (untiled) dimension has one stride; one level of tiling has two
    (the outer tile stride followed by the inner element stride), and so on.
    """

    strides: tuple[Stride, ...]

    def __post_init__(self) -> None:
        self.strides = tuple(self.strides)


@dataclass
class TiledStridedLayout:
    """A tiled-strided layout: one :class:`TiledStride` per tensor dimension."""

    tstrides: tuple[TiledStride, ...]
    offset: int = 0

    def __post_init__(self) -> None:
        self.tstrides = tuple(self.tstrides)

    def to_snaxc(self):
        """Return the equivalent ``snaxc.ir.tsl.TiledStridedLayout``.

        The snaxc import is deferred to here so this module stays usable without
        the AIE codegen toolchain installed. Used to feed IRON-authored layouts
        into stream-dse code generation.
        """
        from snaxc.ir.tsl import (
            Stride as SnaxStride,
            TiledStride as SnaxTiledStride,
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
    """Two-level tiled-strided layout for a ``rows x cols`` tensor.

    The tensor is tiled into ``(rows // row_unit) x (cols // col_unit)`` tiles of
    ``row_unit x col_unit`` elements, the tiles laid out row-major and each tile
    stored row-major internally. This reproduces stream-dse's GEMM/elementwise
    operand layouts (the intrinsic ``row_unit``/``col_unit`` are the kernel's MAC
    tile dimensions).
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
