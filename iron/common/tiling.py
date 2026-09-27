# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Access patterns for the derived sequence, in pure Python.

A host buffer is moved through a stream as a set of DMA transfers, each an
``Access``: an offset into the flat buffer plus up to four (size, stride)
dimensions, which is what a shim buffer descriptor encodes. This module
decides the transfers and encodes them; :mod:`iron.common.design` turns each
``Access`` into a ``TensorAccessPattern`` and issues it.

The descriptor rules are applied here and nowhere else. They are
``AIEX::verifyStridesWraps``'s, over the field widths the current device's
target model gives a shim tile (:func:`limits`), and are stated in tap
order (outermost first), ``sizes = [iter, d2, d1, d0]``; the figures are
NPU1's and NPU2's:

* ``d0``, the innermost, is at most 1023 *granules* (2046 bf16 elements),
  unless the whole transfer is linear or contiguous, when the 32-bit length
  field applies and any run fits;
* ``d1`` is at most 1023 elements; ``d2`` has no wrap field;
* ``iter`` is at most 64 and is the only dimension whose stride may be 0
  (a re-read); every other dimension with size above 1 needs a positive
  stride;
* addressing is 4-byte granular: the offset, the innermost size and every
  non-unit stride are whole granules, and the 20-bit stride field counts
  them.

GEMV, repeat and mha each carried a private copy of the first rule. GEMV's
copy stays in its ``sequence(rt)`` override until its object is proven
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

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib.tap import TensorAccessPattern


@dataclass(frozen=True)
class Limits:
    """What a shim buffer descriptor's fields hold."""

    wrap: int  # d0 in granules, d1 in elements
    step: int  # a stride, in granules
    iterations: int
    granule_bytes: int


def limits() -> Limits:
    """The current device's shim descriptor fields, from its target model.

    A mem tile's descriptor has the same wrap and a narrower stride, a core
    tile's a narrower wrap; every transfer here is a shim's.
    """
    device = aie_utils.get_current_device()
    if device is None:
        raise RuntimeError(
            "no device is current; bind one with aie.utils.set_current_device"
        )
    return Limits(
        wrap=(1 << device.get_dma_bd_wrap_bits(0, 0)) - 1,
        step=(1 << device.get_dma_bd_step_bits(0, 0)) - 1,
        # The iteration field is biased by one: n bits count to 2**n.
        iterations=1 << device.get_dma_bd_iter_bits(0, 0),
        granule_bytes=device.address_gen_granularity // 8,
    )


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
        return TensorAccessPattern(
            (self.elements,), self.offset, list(self.sizes), list(self.strides)
        )


def granule_elements(dtype) -> int:
    """Elements per address granule for ``dtype`` (2 for bf16, 1 for i32)."""
    itemsize, granule = np.dtype(dtype).itemsize, limits().granule_bytes
    if granule % itemsize:
        raise ValueError(
            f"{np.dtype(dtype)} does not divide the {granule}-byte shim granule"
        )
    return granule // itemsize


def contiguous(elements: int, offset: int, run: int) -> Access:
    """A single linear transfer: ``run`` elements from ``offset``."""
    if offset + run > elements:
        raise ValueError(
            f"transfer of {run} at {offset} runs past a buffer of {elements}"
        )
    return Access(elements, offset, (1, 1, 1, run), (0, 0, 0, 1))


# One bank of a core's local memory. AIE2 and AIE2P both have eight 8 KB
# banks, and a fifo object spanning more than one bank cannot be
# double-buffered in what is left; the target model exposes the total
# (get_local_memory_size) but not the banking, so the figure is named here
# rather than spelled at each use.
L1_BANK_BYTES = 8192


def bank_elements(dtype) -> int:
    """Elements of ``dtype`` in one local-memory bank: the largest line a core
    holds at a fifo depth of two.
    """
    return L1_BANK_BYTES // np.dtype(dtype).itemsize


def fifo_depth(elements: int, dtype) -> int:
    """The depth a core-side fifo of ``elements``-long objects can have: two,
    or one when an object spans more than a local-memory bank.
    """
    return 1 if elements > bank_elements(dtype) else 2


def split_run(run: int, gran: int) -> tuple[int, int] | None:
    """Factor a contiguous run into ``(hi, lo)`` for the ``d1``/``d0`` slots.

    ``lo`` is at most a wrap of granules and a whole number of them; ``hi``
    is at most a wrap. ``None`` if no split fits. A ``gran`` of 1 bounds
    ``lo`` in elements, as a mem tile's stream dimensions are.
    """
    lim = limits().wrap
    lo_max = lim * gran
    if run <= lo_max and run % gran == 0:
        return (1, run)
    lo_start = (lo_max // gran) * gran
    for lo in range(lo_start, 0, -gran):
        if run % lo == 0 and run // lo <= lim:
            return (run // lo, lo)
    return None


def _is_contiguous(dims: Sequence[tuple[int, int]]) -> bool:
    """Row-major nested with no gaps: each stride is the product of the inner extent."""
    inner = 1
    for n, s in reversed(dims):
        if s != inner:
            return False
        inner *= n
    return True


def _slots(dims: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """``dims`` in the four slots, outermost first, unit slots padded in.

    A leading zero-stride dimension (a re-read) is only legal in the
    iteration slot, so it stays outermost and the padding goes after it;
    every other pattern pads in front.
    """
    pad = [(1, 0)] * (4 - len(dims))
    if dims and dims[0][1] == 0:
        return [dims[0]] + pad + list(dims[1:])
    return pad + list(dims)


def place(
    elements: int, offset: int, dims: Sequence[tuple[int, int]], gran: int
) -> Access | None:
    """``dims`` (outermost first, at most four) as one descriptor, each in
    the slot it is given, or ``None`` where a field cannot hold them.
    """
    if len(dims) > 4:
        return None
    lim = limits()
    padded = _slots(list(dims))
    (it, it_s), (d2, d2_s), (d1, d1_s), (d0, d0_s) = padded
    if d0_s != 1 or d0 % gran:
        return None
    if d0 // gran > lim.wrap or d1 > lim.wrap or it > lim.iterations:
        return None
    for n, st in ((d2, d2_s), (d1, d1_s)):
        if n > 1 and st < 1:
            return None
    if it > 1 and it_s < 0:
        return None
    for n, st in ((it, it_s), (d2, d2_s), (d1, d1_s)):
        if n > 1 and (st % gran or st > lim.step * gran):
            return None
    span = offset + sum((n - 1) * st for n, st in padded) + 1
    if span > elements:
        raise ValueError(f"access spans {span} elements of a buffer of {elements}")
    return Access(elements, offset, (it, d2, d1, d0), (it_s, d2_s, d1_s, d0_s))


def _pack(
    elements: int, offset: int, dims: list[tuple[int, int]], gran: int
) -> Access | None:
    """Like :func:`place`, but a contiguous pattern (unit dims removed) is
    one linear transfer.
    """
    if not dims:
        dims = [(1, 1)]
    if _is_contiguous(dims):
        total = prod(n for n, _ in dims)
        if total % gran:
            return None
        return contiguous(elements, offset, total)
    return place(elements, offset, dims, gran)


def repeated(
    elements: int,
    offset: int,
    run: int,
    repeats: Sequence[tuple[int, int]],
    dtype,
) -> Access | None:
    """``run`` contiguous elements, repeated over up to two outer (count, stride) dims.

    ``repeats`` is outermost first. The run takes the ``d0``/``d1`` slots
    (split if it exceeds ``d0``), one repeat takes ``d2`` (no wrap limit) and
    a second takes the iteration slot. Returns ``None`` when that does not
    fit; the caller then unrolls.
    """
    gran = granule_elements(dtype)
    if offset % gran:
        return None
    outer = [(int(n), int(s)) for n, s in repeats if int(n) != 1]
    if not outer:
        return contiguous(elements, offset, run) if run % gran == 0 else None
    if len(outer) > 2:
        return None
    split = split_run(run, gran)
    if split is None:
        return None
    hi, lo = split
    run_dims = ([(hi, lo)] if hi != 1 else [(1, 0)]) + [(lo, 1)]
    if len(outer) == 1:
        n, st = outer[0]
        # A re-read (stride 0) is only legal in the iteration slot; a strided
        # repeat goes in d2, which has no wrap limit.
        dims = [(n, st), (1, 0)] if st == 0 else [(1, 0), (n, st)]
        return place(elements, offset, dims + run_dims, gran)
    return place(elements, offset, outer + run_dims, gran)


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

    Unit dimensions are dropped; a contiguous pattern becomes one linear
    transfer; a size past its slot's limit is factored into a free slot when
    one exists; otherwise the outermost dimension is unrolled into several
    descriptors. Order is preserved throughout. Granularity violations
    cannot be fixed and are errors.

    This is the general form of the ``legalize_tap`` mha carries, which only
    knew how to collapse a contiguous tile to a linear run.
    """
    gran = granule_elements(dtype)
    if offset % gran:
        raise ValueError(
            f"offset {offset} is not a multiple of the {gran}-element shim granule"
        )
    dims = [(int(n), int(s)) for n, s in zip(sizes, strides) if int(n) != 1]
    for n, s in dims[:-1]:
        if s % gran:
            raise ValueError(
                f"stride {s} is not a multiple of the {gran}-element granule"
            )
    if dims and dims[-1][1] == 1 and dims[-1][0] % gran:
        raise ValueError(
            f"innermost size {dims[-1][0]} is not a multiple of the {gran}-element granule"
        )
    out = _legalize_dims(elements, offset, dims, gran)
    if len(out) > 1:
        # A pattern past the slots may fit once adjacent dimensions that nest
        # contiguously are one (as a buffer slice already spells them). Only
        # as a fallback: merging can also cost a slot's factoring room, and
        # a pattern that fits as given keeps its shape.
        merged = _merged(dims)
        if merged != dims:
            alt = _legalize_dims(elements, offset, merged, gran)
            if len(alt) < len(out):
                out = alt
    return out


def _merged(dims: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Adjacent dimensions that nest contiguously, as one: fewer slots used."""
    out: list[tuple[int, int]] = []
    for n, s in dims:
        if out and out[-1][1] == n * s:
            out[-1] = (out[-1][0] * n, s)
        else:
            out.append((n, s))
    return out


def _legalize_dims(
    elements: int, offset: int, dims: list[tuple[int, int]], gran: int
) -> list[Access]:
    packed = _pack(elements, offset, dims, gran)
    if packed is not None:
        return [packed]
    fields = limits()
    iterations = fields.iterations
    # Which slot overflowed? Try factoring it into a free slot, innermost first.
    if len(dims) < 4:
        padded = _slots(dims)
        caps = (iterations, None, fields.wrap, fields.wrap * gran)
        for pos in (3, 2, 0):
            n, st = padded[pos]
            cap = caps[pos]
            if cap is None or n <= cap:
                continue
            b = next(
                (
                    b
                    for b in range(cap, 0, -1)
                    if n % b == 0 and (pos != 3 or b % gran == 0)
                ),
                None,
            )
            if b is None or n // b > fields.wrap:
                continue
            i = dims.index((n, st))
            return _legalize_dims(
                elements,
                offset,
                dims[:i] + [(n // b, b * st), (b, st)] + dims[i + 1 :],
                gran,
            )
    if not dims:
        raise ValueError("cannot legalize an empty pattern")
    n0, s0 = dims[0]
    out: list[Access] = []
    if n0 > iterations:
        # Past the iteration count: as many descriptors as it takes, each
        # iterating at most that often, not one per iteration. A stream's
        # queue holds a handful, and one that stalls on its queue stalls
        # every stream issued after it.
        for i in range(0, n0, iterations):
            chunk = [(min(iterations, n0 - i), s0)] + dims[1:]
            out.extend(_legalize_dims(elements, offset + i * s0, chunk, gran))
        return out
    # No room: unroll the outermost dimension.
    for i in range(n0):
        out.extend(_legalize_dims(elements, offset + i * s0, dims[1:], gran))
    return out


# --------------------------------------------------------------------------
# Slicing a buffer: what ``buffer[:, r0:r1, :]`` means as a transfer
# --------------------------------------------------------------------------


def view(shape: Sequence[int], index) -> tuple[int, list[int], list[int]]:
    """``(offset, sizes, strides)`` of a basic slice over a row-major buffer.

    ``index`` is what ``__getitem__`` received: an int, a slice, or a tuple
    of them; missing trailing axes are taken whole. Steps other than 1 are
    rejected. Adjacent contiguous dimensions are merged, so a slice that
    selects whole rows collapses to one linear run.
    """
    offset, dims = _walk(shape, index)
    merged = _merged(dims) or [(1, 1)]
    return offset, [n for n, _ in merged], [s for _, s in merged]


def _walk(shape: Sequence[int], index) -> tuple[int, list[tuple[int, int]]]:
    """``(offset, [(size, stride), ...])`` of a basic slice, one entry per
    sliced axis (an integer index drops its axis), nothing merged: upstream's
    ``from_slice``, less the steps a view does not take.
    """
    key = index if isinstance(index, tuple) else (index,)
    if any(isinstance(k, slice) and k.step not in (None, 1) for k in key):
        raise ValueError(f"{index}: only unit steps are supported")
    tap = TensorAccessPattern.from_slice([int(n) for n in shape], key)
    return tap.offset, [(int(n), int(s)) for n, s in tap.transformation_dims]


@dataclass(frozen=True)
class Walk:
    """A strided walk over a flat buffer: where a view's elements are.

    ``offset`` in elements; ``sizes`` and ``strides`` from the outermost axis
    in, adjacent contiguous axes merged, so a whole buffer is one run. What
    a DMA is given, once legalized for the shim.
    """

    offset: int
    sizes: tuple[int, ...]
    strides: tuple[int, ...]
    # The axis a graph bounds per call (``x[:n]`` on a view a copy takes):
    # its size is the full extent here and patched to the call's at dispatch.
    bounded: int | None = None

    @classmethod
    def of(cls, shape) -> "Walk":
        """The whole of a row-major buffer of ``shape``, axis by axis."""
        shape = tuple(int(n) for n in shape) or (1,)
        return cls(0, shape, tuple(prod(shape[i + 1 :]) for i in range(len(shape))))

    @classmethod
    def slice(cls, shape, key) -> "Walk":
        """``buffer[key]`` over a row-major buffer of ``shape``."""
        offset, dims = _walk(shape, key)
        dims = dims or [(1, 1)]
        return cls(offset, tuple(n for n, _ in dims), tuple(s for _, s in dims))

    @classmethod
    def permuted(cls, shape, axes) -> "Walk":
        """``buffer.transpose(axes)`` over a row-major buffer of ``shape``."""
        shape = tuple(int(n) for n in shape)
        if sorted(axes) != list(range(len(shape))):
            raise ValueError(f"axes {axes} do not permute a shape of rank {len(shape)}")
        row = [prod(shape[i + 1 :]) for i in range(len(shape))]
        return cls(0, tuple(shape[a] for a in axes), tuple(row[a] for a in axes))

    @property
    def elements(self) -> int:
        return prod(self.sizes)

    @property
    def contiguous(self) -> bool:
        """One dense run: what a sub-buffer is."""
        merged = _merged(list(zip(self.sizes, self.strides))) or [(1, 1)]
        return len(merged) == 1 and merged[0][1] == 1

    def __str__(self) -> str:
        return (
            f"o{self.offset}s{'x'.join(map(str, self.sizes))}"
            f"t{'x'.join(map(str, self.strides))}"
            + (f"b{self.bounded}" if self.bounded is not None else "")
        )
