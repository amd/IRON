# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Access patterns for the derived sequence, in pure Python.

A host buffer is moved through a stream as a set of DMA transfers, each an
``Access``: an offset into the flat buffer plus up to four (size, stride)
dimensions, which is what a shim buffer descriptor encodes. This module
decides the transfers and encodes them; :mod:`iron.common.build` turns each
``Access`` into a ``TensorAccessPattern`` and issues it.

Two hardware limits are applied here and nowhere else:

* the three outer size fields of a shim descriptor are 10-bit (``DMA_BD_MAX_WRAP``);
  the innermost is the transfer length and is not wrap-limited;
* shim addressing is 4-byte granular, so every offset and every non-unit
  stride must be a whole number of 4-byte granules, and the 20-bit stride
  field counts granules.

GEMV, repeat and mha each carried a private copy of the first rule. GEMV's
copy stays in its ``design(rt)`` override until its object is proven
byte-identical; the derived operators use this one.

Upstream's ``taplib`` is used for what it does: ``TensorAccessPattern`` is the
descriptor object this module emits, ``TensorTiler2D`` is how an override
describes a 2-D tiling, and ``TensorAccessSequence`` is how coverage is
checked. It has no notion of descriptor legality, so :func:`legalize` takes
any tap, from a tiler or by hand, and returns descriptors that fit.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import prod
from typing import Iterator, Sequence

import numpy as np

from .utils import DMA_BD_MAX_WRAP

_STRIDE_BITS = 20
_ADDR_GRANULE_BYTES = 4


@dataclass(frozen=True)
class Access:
    """One DMA transfer over a flat buffer of ``elements`` elements."""

    elements: int
    offset: int
    sizes: tuple[int, int, int, int]
    strides: tuple[int, int, int, int]

    @property
    def count(self) -> int:
        """Elements moved by this transfer."""
        return prod(self.sizes)

    def tap(self):
        """The upstream ``TensorAccessPattern`` for this access (needs mlir-aie)."""
        from aie.helpers.taplib.tap import TensorAccessPattern

        return TensorAccessPattern(
            (self.elements,), self.offset, list(self.sizes), list(self.strides)
        )


def granule_elements(dtype) -> int:
    """Elements per 4-byte address granule for ``dtype`` (2 for bf16, 1 for i32)."""
    itemsize = np.dtype(dtype).itemsize
    if _ADDR_GRANULE_BYTES % itemsize:
        raise ValueError(f"{np.dtype(dtype)} does not divide the 4-byte shim granule")
    return _ADDR_GRANULE_BYTES // itemsize


def max_stride_elements(dtype) -> int:
    return ((1 << _STRIDE_BITS) - 1) * granule_elements(dtype)


def contiguous(elements: int, offset: int, run: int) -> Access:
    """A single linear transfer: ``run`` elements from ``offset``."""
    if offset + run > elements:
        raise ValueError(
            f"transfer of {run} at {offset} runs past a buffer of {elements}"
        )
    return Access(elements, offset, (1, 1, 1, run), (0, 0, 0, 1))


def split_run(
    run: int, gran: int, lim: int = DMA_BD_MAX_WRAP
) -> tuple[int, int] | None:
    """Factor a contiguous run into ``(hi, lo)`` for two descriptor dimensions.

    ``hi`` fills an outer (wrap-limited) size field, ``lo`` the innermost;
    ``lo`` must be a whole number of granules. ``None`` if no split fits.
    """
    if run <= lim and run % gran == 0:
        return (1, run)
    lo_start = (lim // gran) * gran
    for lo in range(lo_start, 0, -gran):
        if run % lo == 0 and run // lo <= lim:
            return (run // lo, lo)
    return None


def repeated(
    elements: int,
    offset: int,
    run: int,
    repeats: Sequence[tuple[int, int]],
    dtype,
) -> Access | None:
    """``run`` contiguous elements, repeated over up to two outer (count, stride) dims.

    ``repeats`` is outermost first. A stride of 0 re-reads the same run. Returns
    ``None`` when the shape does not fit a four-dimensional descriptor within
    the wrap, stride and granularity limits; the caller then unrolls.
    """
    gran = granule_elements(dtype)
    if len(repeats) > 2:
        return None
    if offset % gran:
        return None
    outer = [(int(n), int(s)) for n, s in repeats if int(n) != 1]
    max_stride = max_stride_elements(dtype)
    for n, s in outer:
        if n > DMA_BD_MAX_WRAP or s > max_stride or s % gran:
            return None
    if not outer:
        return contiguous(elements, offset, run)
    split = split_run(run, gran)
    if split is None:
        return None
    hi, lo = split
    dims = outer + ([(hi, lo)] if hi != 1 else []) + [(lo, 1)]
    if len(dims) > 4:
        return None
    while len(dims) < 4:
        dims.insert(0, (1, 0))
    sizes = tuple(n for n, _ in dims)
    strides = tuple(s for _, s in dims)
    total = prod(sizes)
    span = offset + sum((n - 1) * s for n, s in dims) + 1
    if span > elements:
        raise ValueError(f"access spans {span} elements of a buffer of {elements}")
    return Access(elements, offset, sizes, strides)  # type: ignore[arg-type]


# --------------------------------------------------------------------------
# Splitting a buffer across a stream's slots
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Block:
    """A slot's share of a buffer: a contiguous run, iterated over leading axes."""

    slot: int
    offset: int
    run: int
    repeats: tuple[tuple[int, int], ...]  # (count, stride) outermost first

    @property
    def unrolled(self) -> Iterator[tuple[int, int]]:
        """``(offset, run)`` for every repeat, outermost varying slowest."""
        counts = [n for n, _ in self.repeats]
        strides = [s for _, s in self.repeats]
        for idx in np.ndindex(*counts) if counts else [()]:
            yield self.offset + sum(i * s for i, s in zip(idx, strides)), self.run


def split(shape: Sequence[int], count: int, axis: int) -> list[Block]:
    """Divide ``shape`` along ``axis`` into ``count`` contiguous row-blocks.

    Axes before ``axis`` become repeats (each slot takes its block out of
    every leading index); axes from ``axis`` on are contiguous. Slot ``i``
    gets rows ``[i*rows/count, (i+1)*rows/count)``.
    """
    shape = tuple(int(s) for s in shape)
    if not 0 <= axis < len(shape):
        raise ValueError(f"axis {axis} out of range for shape {shape}")
    rows = shape[axis]
    if rows % count:
        raise ValueError(
            f"cannot split {rows} rows (axis {axis} of {shape}) across {count} slots"
        )
    inner = prod(shape[axis + 1 :]) if axis + 1 < len(shape) else 1
    run = (rows // count) * inner
    leading = shape[:axis]
    # stride of each leading axis in the flat buffer
    repeats = []
    for i, n in enumerate(leading):
        stride = prod(shape[i + 1 :])
        repeats.append((n, stride))
    return [Block(i, i * run, run, tuple(repeats)) for i in range(count)]


def whole(shape: Sequence[int]) -> Block:
    """The entire buffer as one block (broadcast streams, single-slot streams)."""
    return Block(0, 0, prod(int(s) for s in shape), ())


def encode(block: Block, elements: int, dtype) -> list[Access]:
    """Encode a block as one descriptor if it fits, else one per repeat.

    The single-descriptor form is what a coalesced batch loop needs (one
    iterated BD covering every batch); the unrolled form is the per-batch
    fallback, and the two move exactly the same elements in the same order.
    """
    one = repeated(elements, block.offset, block.run, block.repeats, dtype)
    if one is not None:
        return [one]
    return [contiguous(elements, off, run) for off, run in block.unrolled]


# --------------------------------------------------------------------------
# Legalising an arbitrary pattern (a taplib tap, or hand-written sizes/strides)
# --------------------------------------------------------------------------


def legalize(
    elements: int,
    offset: int,
    sizes: Sequence[int],
    strides: Sequence[int],
    dtype,
) -> list[Access]:
    """Rewrite one pattern as descriptors the shim can hold, moving the same elements.

    Unit dimensions are dropped. An outer size past the wrap limit is
    factored into two dimensions when a slot is free; otherwise the outermost
    dimension is unrolled into several descriptors. Order is preserved in
    both cases. Granularity violations cannot be fixed and are errors.

    This is the general form of the ``legalize_tap`` mha carries, which only
    knew how to collapse a contiguous tile to a linear run.
    """
    gran = granule_elements(dtype)
    if offset % gran:
        raise ValueError(
            f"offset {offset} is not a multiple of the {gran}-element shim granule"
        )
    dims = [(int(n), int(s)) for n, s in zip(sizes, strides) if int(n) != 1]
    if not dims:
        dims = [(1, 1)]
    max_stride = max_stride_elements(dtype)
    for n, s in dims[:-1]:
        if s % gran:
            raise ValueError(
                f"stride {s} is not a multiple of the {gran}-element granule"
            )
        if s > max_stride:
            raise ValueError(f"stride {s} exceeds the {_STRIDE_BITS}-bit stride field")
    return _legalize_dims(elements, offset, dims)


def _legalize_dims(
    elements: int, offset: int, dims: list[tuple[int, int]]
) -> list[Access]:
    outer = dims[:-1]
    over = next((i for i, (n, _) in enumerate(outer) if n > DMA_BD_MAX_WRAP), None)
    if over is None and len(dims) <= 4:
        padded = list(dims)
        while len(padded) < 4:
            padded.insert(0, (1, 0))
        sizes = tuple(n for n, _ in padded)
        strides = tuple(s for _, s in padded)
        return [Access(elements, offset, sizes, strides)]  # type: ignore[arg-type]
    if over is not None and len(dims) < 4:
        n, s = dims[over]
        b = next((b for b in range(DMA_BD_MAX_WRAP, 0, -1) if n % b == 0), 1)
        a = n // b
        if a <= DMA_BD_MAX_WRAP:
            return _legalize_dims(
                elements, offset, dims[:over] + [(a, b * s), (b, s)] + dims[over + 1 :]
            )
    # No room to factor: unroll the outermost dimension.
    n0, s0 = dims[0]
    out: list[Access] = []
    for i in range(n0):
        out.extend(_legalize_dims(elements, offset + i * s0, dims[1:]))
    return out
