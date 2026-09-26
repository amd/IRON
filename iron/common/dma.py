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
    repeat = 0
    if dims and dims[0][1] == 0:
        if direction is Direction.WRITE:
            return Unfit(Reason.NOT_INJECTIVE, f"dims {dims}")
        repeat = dims[0][0] - 1
        dims = dims[1:]
        if repeat > limits.repeat:
            return Unfit(
                Reason.REPEAT, f"{repeat + 1} reads, repeat_count holds {limits.repeat}"
            )
    if any(s == 0 for _, s in dims):
        return Unfit(Reason.INNER_REPEAT, f"dims {dims}")
    if not dims:
        dims = [(1, 1)]
    if len(dims) > 1 or dims[0][1] != 1:
        # A single contiguous run needs no dimensions, only a length.
        dims = _split_wide(dims, limits, granule_elements(dtype))
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
    pad = [(1, 0)] * (4 - len(dims))
    full = pad + list(dims)
    access = Access(
        elements, offset, tuple(n for n, _ in full), tuple(s for _, s in full)
    )
    return Fit(kind, direction, (access,), repeat)


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
