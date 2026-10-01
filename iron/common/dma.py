# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What one DMA buffer descriptor can express, per tile kind and device.

A descriptor walks up to a few nested (size, stride) dimensions, plus an
iteration dimension stepped once per re-run of the descriptor, and a channel
can re-run a descriptor chain ``repeat_count`` more times. These are the
limits the mlir-aie verifiers apply (``AIEX::verifyStridesWraps`` for a shim
runtime descriptor, ``DMABDOp::verify`` for a memtile or core one), and the
limits a fold spends against.

Two hardware facts shape everything here, both measured on npu2
(``iron/tests/common/dma.py``):

* **A stride is never 0.** Every step field stores ``stride - 1``, so a
  stored 0 already means one granule; no descriptor dimension on any tile
  kind can re-read. The shim's "stride 0 in the iteration dimension" is not a
  stride either: the lowering turns it into the channel's ``repeat_count``.
  A re-read is therefore expressible only as the *outermost* factor of a
  pattern, by ``repeat_count`` (optionally stepping the iteration
  dimension between runs), or across slots, by multicast.
* **A write is never checked for injectivity.** A shim S2MM whose pattern
  visits an address twice builds and runs; the last write wins. The rule
  that a write must be injective is ours to enforce.

Where the target model exposes a limit it is read from it
(:meth:`DmaFacts.of`); the rest are written down with the ``AIETargetModel``
method they stand for, and the tests check both against a real device.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum
from math import prod

import numpy as np
from aie.dialects.aie import WireBundle, get_target_model

from .tiling import Access, factor, granule_elements, legalize


class TileKind(Enum):
    SHIM = "shim"
    MEM = "mem"
    CORE = "core"


class Direction(Enum):
    """Which way a descriptor moves data: a READ streams memory out (MM2S),
    a WRITE lands a stream in memory (S2MM)."""

    READ = "mm2s"
    WRITE = "s2mm"


@dataclass(frozen=True)
class Endpoint:
    """One end of a transfer: which tile kind's DMA, moving which way."""

    kind: TileKind
    direction: Direction


@dataclass(frozen=True)
class BdLimits:
    """One tile kind's descriptor and channel limits.

    ``dims`` counts the wrapped (size, stride) dimensions, not the iteration
    one. ``wrap`` is the largest size a dimension may take: in elements on a
    memtile or core descriptor (the verifier counts elements), in granules
    for the shim's innermost dimension and elements for its others; the
    shim's outermost wrapped dimension has no wrap field (its size is carried
    by the length). ``step`` is the largest stride in granules. ``length`` is
    the longest transfer in granules. ``iteration`` is the iteration
    dimension's largest size and ``repeat`` the channel's largest
    ``repeat_count``. ``bds`` counts the tile's descriptors and
    ``bds_per_channel`` those one channel can reach (a memtile's even
    channels use 0-23, its odd ones 24-47). ``queue`` is how many tasks one
    channel's queue holds.
    """

    kind: TileKind
    dims: int
    wrap: int
    step: int
    length: int
    iteration: int
    repeat: int
    bds: int
    bds_per_channel: int
    mm2s: int
    s2mm: int
    queue: int

    def channels(self, direction: Direction) -> int:
        return self.mm2s if direction is Direction.READ else self.s2mm


# Not exposed to Python by the target model; values of AIE2TargetModel, the
# base both npu1 and npu2 derive from.
_BD_DIMS = {TileKind.SHIM: 3, TileKind.MEM: 4, TileKind.CORE: 3}  # getBDMaxDims
_BD_LENGTH = {  # getDmaBdMaxLen, 32-bit words
    TileKind.SHIM: (1 << 32) - 1,
    TileKind.MEM: (1 << 17) - 1,
    TileKind.CORE: (1 << 14) - 1,
}
_MAX_REPEAT = 255  # getMaxRepeatCount
_TASK_QUEUE = 4  # getDmaTaskQueueDepth
_MEM_BDS_PER_CHANNEL = 24  # isBdChannelAccessible

# The tile each kind is probed at: column 0, rows as on every NPU.
_PROBE = {TileKind.SHIM: (0, 0), TileKind.MEM: (0, 1), TileKind.CORE: (0, 2)}


@dataclass(frozen=True)
class DmaFacts:
    """A device's descriptor limits per tile kind, and its shim tiles."""

    limits: dict[TileKind, BdLimits]
    shim_tiles: int

    def __getitem__(self, kind: TileKind) -> BdLimits:
        return self.limits[kind]

    def shim_channels(self, direction: Direction) -> int:
        """The device's shim DMA channels in one direction."""
        return self.shim_tiles * self[TileKind.SHIM].channels(direction)

    @classmethod
    def of(cls, dev) -> "DmaFacts":
        tm = get_target_model(dev.resolve())
        limits = {}
        for kind, (col, row) in _PROBE.items():
            if kind is TileKind.SHIM:
                mm2s = tm.get_num_source_shim_mux_connections(col, row, WireBundle.DMA)
                s2mm = tm.get_num_dest_shim_mux_connections(col, row, WireBundle.DMA)
            else:
                mm2s = tm.get_num_source_switchbox_connections(col, row, WireBundle.DMA)
                s2mm = tm.get_num_dest_switchbox_connections(col, row, WireBundle.DMA)
            bds = tm.get_num_bds(col, row)
            limits[kind] = BdLimits(
                kind=kind,
                dims=_BD_DIMS[kind],
                wrap=(1 << tm.get_dma_bd_wrap_bits(col, row)) - 1,
                step=1 << tm.get_dma_bd_step_bits(col, row),
                length=_BD_LENGTH[kind],
                iteration=1 << tm.get_dma_bd_iter_bits(col, row),
                repeat=_MAX_REPEAT,
                bds=bds,
                bds_per_channel=_MEM_BDS_PER_CHANNEL if kind is TileKind.MEM else bds,
                mm2s=mm2s,
                s2mm=s2mm,
                queue=_TASK_QUEUE,
            )
        shims = sum(
            1
            for col in range(tm.columns())
            for row in range(tm.rows())
            if tm.is_shim_noc_tile(col, row)
        )
        return cls(limits, shims)


class Reason(Enum):
    """Why a sequence of elements does not fit a tile kind's descriptors."""

    NOT_A_NEST = "no nest of (size, stride) loops visits the sequence"
    NOT_INJECTIVE = "a write visits an address more than once"
    NEGATIVE_STRIDE = "a descriptor never steps backwards"
    INNER_REPEAT = "a re-read that is not the outermost factor"
    GRANULE = "the 4-byte address granule does not divide it"
    DIMS = "more dimensions than one descriptor holds"
    WRAP = "a dimension larger than its wrap field"
    STEP = "a stride larger than its step field"
    LENGTH = "longer than one descriptor's length field"
    REPEAT = "more re-reads than the channel's repeat_count holds"
    BDS = "more descriptors than the tile has"
    BOUNDS = "it reaches outside the buffer"


@dataclass(frozen=True)
class Unfit:
    reason: Reason
    detail: str


@dataclass(frozen=True)
class Fit:
    """How one engine moves a sequence: its descriptors, issued in order, and
    the channel's ``repeat`` (re-runs of the whole chain; the shim carries a
    re-read in each descriptor's iteration slot instead, so it is 0 there).
    On the shim an ``Access`` is ``[iter, d2, d1, d0]``; on a memtile or core
    it is the descriptor's own dimensions, outermost first."""

    kind: TileKind
    direction: Direction
    bds: tuple[Access, ...]
    repeat: int = 0


def fit(
    indices: np.ndarray,
    elements: int,
    dtype,
    kind: TileKind,
    direction: Direction,
    limits: BdLimits,
) -> Fit | Unfit:
    """The descriptors that make a ``kind`` tile's DMA visit ``indices`` of a
    flat buffer of ``elements``, in order, moving them in ``direction``.

    A write must be injective. A re-read must be the outermost factor: the
    shim re-reads in its iteration slot and otherwise unrolls into more
    descriptors, while a memtile or core has one descriptor per object and
    re-reads only by the channel's ``repeat_count``.
    """
    indices = np.asarray(indices, dtype=np.int64).reshape(-1)
    if direction is Direction.WRITE and np.unique(indices).size != indices.size:
        return Unfit(
            Reason.NOT_INJECTIVE,
            f"{indices.size} writes to {np.unique(indices).size} addresses",
        )
    nest = factor(indices)
    if nest is None:
        return Unfit(Reason.NOT_A_NEST, f"{indices.size} elements")
    offset, dims = nest
    if any(s < 0 for _, s in dims):
        return Unfit(Reason.NEGATIVE_STRIDE, f"dims {dims}")
    if kind is TileKind.SHIM:
        return _fit_shim(offset, dims, elements, dtype, direction, limits)
    return _fit_tile(offset, dims, elements, dtype, kind, direction, limits)


def access_legal(acc: Access, end: Endpoint, dtype, facts: DmaFacts) -> Unfit | None:
    """Why one descriptor, exactly as it would be issued at ``end``, is
    illegal, or ``None`` if it is legal. Nothing is re-encoded: a pattern
    that only fails for want of re-encoding is :func:`fit`'s to rewrite.

    On the shim ``acc`` is ``[iter, d2, d1, d0]`` and a re-read (stride 0)
    is legal only in the iteration slot; on a memtile or core ``acc`` is the
    descriptor's own dimensions, and an outermost stride 0 is the channel's
    ``repeat_count``. A write must visit no address twice.
    """
    limits = facts[end.kind]
    dims = [(n, s) for n, s in zip(acc.sizes, acc.strides) if n != 1]
    if any(s < 0 for _, s in dims):
        return Unfit(Reason.NEGATIVE_STRIDE, f"dims {dims}")
    last = acc.offset + sum((n - 1) * s for n, s in dims)
    if acc.offset < 0 or last >= acc.elements:
        return Unfit(Reason.BOUNDS, f"elements {acc.offset}..{last} of {acc.elements}")
    if end.direction is Direction.WRITE:
        bad = _injective(acc, dims)
        if bad is not None:
            return bad
    if end.kind is TileKind.SHIM:
        return _check_shim(acc, dtype, limits)
    peeled = _peel_repeat(dims, end.direction, limits)
    if isinstance(peeled, Unfit):
        return peeled
    return _check_tile(acc.offset, peeled[1], acc.elements, dtype, end.kind, limits)


def writes_disjoint(accs: Sequence[Access]) -> Unfit | None:
    """Whether writes by ``accs`` (one slot's descriptors, or every slot's
    of one buffer, where two channels would race) land on distinct
    addresses."""
    every = np.concatenate([a.indices() for a in accs])
    distinct = np.unique(every).size
    if distinct != every.size:
        return Unfit(
            Reason.NOT_INJECTIVE, f"{every.size} writes to {distinct} addresses"
        )
    return None


def _injective(acc: Access, dims: list[tuple[int, int]]) -> Unfit | None:
    if any(s == 0 for _, s in dims):
        return Unfit(Reason.NOT_INJECTIVE, f"dims {dims}")
    # Each dimension clearing the reach of every finer one proves it without
    # listing the addresses; only a pattern that interleaves is listed.
    reach = 1
    for n, s in sorted(dims, key=lambda d: d[1]):
        if s < reach:
            return writes_disjoint([acc])
        reach += (n - 1) * s
    return None


def _contiguous(dims: list[tuple[int, int]]) -> bool:
    run = 1
    for n, s in reversed(dims):
        if s != run:
            return False
        run *= n
    return True


def _check_shim(acc: Access, dtype, limits: BdLimits) -> Unfit | None:
    """The shim's rules (``AIEX::verifyStridesWraps``) for ``acc`` as issued."""
    (it, it_s), *nd = zip(acc.sizes, acc.strides)
    (d2, _), (d1, _), (d0, d0_s) = nd
    inner = [(n, s) for n, s in nd if n != 1]
    if any(s == 0 for _, s in inner):
        return Unfit(Reason.INNER_REPEAT, f"dims {inner} under the iteration slot")
    if it > limits.iteration:
        # The verifier caps the iteration size before it lowers a zero
        # stride to repeat_count, so a re-read is capped the same.
        return Unfit(Reason.WRAP, f"iteration size {it} over {limits.iteration}")
    itemsize = np.dtype(dtype).itemsize
    if acc.offset * itemsize % 4 or d0 * itemsize % 4:
        return Unfit(Reason.GRANULE, f"offset {acc.offset}, d0 size {d0}")
    if d0 > 1 and d0_s != 1 and itemsize != 4:
        return Unfit(
            Reason.GRANULE, f"innermost stride {d0_s} of a {itemsize}-byte type"
        )
    # A contiguous innermost dimension is sized, not stepped; a zero
    # iteration stride is a repeat by now.
    stepped = [(it, it_s), *nd[:2]] + ([] if d0_s == 1 else [(d0, d0_s)])
    for n, s in stepped:
        if n == 1 or s == 0:
            continue
        if s * itemsize % 4:
            return Unfit(Reason.GRANULE, f"stride {s} of a {itemsize}-byte type")
        if s * itemsize // 4 > limits.step:
            return Unfit(Reason.STEP, f"stride {s} over {limits.step} granules")
    if not _contiguous(inner):
        if d0 * itemsize // 4 > limits.wrap:
            return Unfit(Reason.WRAP, f"d0 size {d0} over {limits.wrap} granules")
        if d1 > limits.wrap:
            return Unfit(Reason.WRAP, f"d1 size {d1} over {limits.wrap}")
    words = d2 * d1 * d0 * itemsize // 4
    if words > limits.length:
        return Unfit(Reason.LENGTH, f"{words} words over {limits.length}")
    return None


def _fit_shim(offset, dims, elements, dtype, direction, limits) -> Fit | Unfit:
    try:
        bds = legalize(
            elements,
            offset,
            [n for n, _ in dims] or [1],
            [s for _, s in dims] or [1],
            dtype,
        )
    except ValueError as e:
        return Unfit(Reason.GRANULE, str(e))
    if len(bds) > limits.bds:
        return Unfit(Reason.BDS, f"{len(bds)} descriptors, the shim has {limits.bds}")
    return Fit(TileKind.SHIM, direction, tuple(bds))


def _fit_tile(offset, dims, elements, dtype, kind, direction, limits) -> Fit | Unfit:
    peeled = _peel_repeat(dims, direction, limits)
    if isinstance(peeled, Unfit):
        return peeled
    repeat, dims = peeled
    if not dims:
        dims = [(1, 1)]
    if len(dims) > 1 or dims[0][1] != 1:
        # A single contiguous run needs no dimensions, only a length.
        dims = _split_wide(dims, limits, granule_elements(dtype))
    bad = _check_tile(offset, dims, elements, dtype, kind, limits)
    if bad is not None:
        return bad
    pad = [(1, 0)] * (4 - len(dims))
    full = pad + list(dims)
    access = Access(
        elements, offset, tuple(n for n, _ in full), tuple(s for _, s in full)
    )
    return Fit(kind, direction, (access,), repeat)


def _peel_repeat(
    dims: list[tuple[int, int]], direction: Direction, limits: BdLimits
) -> tuple[int, list[tuple[int, int]]] | Unfit:
    """A memtile or core pattern's outermost zero-stride dimension, as the
    channel's ``repeat_count``, and the dimensions its descriptor keeps."""
    if not dims or dims[0][1] != 0:
        return 0, dims
    if direction is Direction.WRITE:
        return Unfit(Reason.NOT_INJECTIVE, f"dims {dims}")
    repeat = dims[0][0] - 1
    if repeat > limits.repeat:
        return Unfit(
            Reason.REPEAT, f"{repeat + 1} reads, repeat_count holds {limits.repeat}"
        )
    return repeat, dims[1:]


def _check_tile(offset, dims, elements, dtype, kind, limits) -> Unfit | None:
    """Whether a memtile or core descriptor holds ``dims`` (unit dimensions
    dropped, outermost first) from ``offset``, as they stand."""
    if any(s == 0 for _, s in dims):
        return Unfit(Reason.INNER_REPEAT, f"dims {dims}")
    if not dims:
        dims = [(1, 1)]
    if len(dims) > limits.dims:
        return Unfit(
            Reason.DIMS,
            f"{len(dims)} dims, a {kind.value} descriptor holds {limits.dims}",
        )
    itemsize = np.dtype(dtype).itemsize
    gran = granule_elements(dtype)
    inner_n, inner_s = dims[-1]
    if itemsize != 4 and inner_s != 1:
        return Unfit(
            Reason.GRANULE, f"innermost stride {inner_s} of a {itemsize}-byte type"
        )
    if (
        offset % gran
        or (inner_n * itemsize) % 4
        or any(s * itemsize % 4 for _, s in dims[:-1])
    ):
        return Unfit(Reason.GRANULE, f"offset {offset}, dims {dims}")
    linear = len(dims) == 1 and dims[0][1] == 1
    for n, s in dims:
        if n > limits.wrap and not linear:
            return Unfit(Reason.WRAP, f"size {n} over {limits.wrap}")
        if s > limits.step or s > elements:
            return Unfit(Reason.STEP, f"stride {s} over {limits.step}")
    words = prod(n for n, _ in dims) * itemsize // 4
    if words > limits.length:
        return Unfit(Reason.LENGTH, f"{words} words over {limits.length}")
    return None


def _split_wide(
    dims: list[tuple[int, int]], limits: BdLimits, gran: int
) -> list[tuple[int, int]]:
    """Each dimension past the wrap field as two that nest to it, where one
    factoring fits (the innermost keeping whole granules); a dimension no
    factoring fits is left for the caller to reject."""
    out: list[tuple[int, int]] = []
    for i, (n, s) in enumerate(dims):
        if n <= limits.wrap:
            out.append((n, s))
            continue
        unit = gran if i == len(dims) - 1 else 1
        lo = next(
            (
                b
                for b in range(limits.wrap, 1, -1)
                if n % b == 0 and n // b <= limits.wrap and b % unit == 0
            ),
            None,
        )
        out.extend([(n, s)] if lo is None else [(n // lo, lo * s), (lo, s)])
    return out
