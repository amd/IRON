# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""When a movement operator can be folded into a neighbour's DMA.

A :class:`~iron.common.declare.Movement` operator re-indexes: each output
element is one input element. Instead of running it, a neighbour's
descriptors can do the re-indexing, so the moved copy is never made:

* **into a read** (:func:`fold_read`): the consumer reads the mover's input
  directly, at the composed indices. A read may visit an element more than
  once, so a repeat folds this way.
* **into a write** (:func:`fold_write`): the producer writes straight into
  the mover's output, at the composed indices. A write must land every
  element exactly once, so only a mover that neither repeats nor drops what
  it is given folds this way.

What the mover does is its :class:`ElementMap`, derived from its own two
orders: a DMA-only mover's slot ``k`` carries input element
``x.indices(k)[t]`` to output element ``y.indices(k)[t]``; a mover with
cores permutes each object on the way, as its :class:`Movement` says. The
composed indices must then fit the neighbour's descriptors (:func:`fit`),
per slot, in the neighbour's direction.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np

from .declare import BoundBuffer, BoundValue, Movement, Operator, Order
from .dma import DmaFacts, Direction, Fit, Reason, TileKind, Unfit, fit

UNWRITTEN = -1


class Blocker(Enum):
    NOT_MOVEMENT = "the operator is not a movement"
    NOT_PRODUCED = "the consumer reads elements the mover does not write"
    DUPLICATES = "the mover repeats an element, which a write cannot"
    DROPS = "the mover drops elements the producer writes"
    OFFSETS = "both sides shift by a per-call value"
    MULTICAST = "every slot reads the same elements: the stream would multicast"
    OVERLAP = "two slots write one element"
    FIT = "a slot's indices fit no descriptors"


@dataclass(frozen=True)
class Blocked:
    blocker: Blocker
    detail: str
    unfit: Unfit | None = None


@dataclass(frozen=True, eq=False)
class ElementMap:
    """What a movement operator does: output element ``j`` is input element
    ``source[j]``, or :data:`UNWRITTEN`. ``in_by``/``out_by`` are per-call
    values that shift the input/output side."""

    op: Operator
    x: BoundBuffer
    y: BoundBuffer
    source: np.ndarray
    in_by: BoundValue | None
    out_by: BoundValue | None


def element_map(op: Operator) -> ElementMap | Blocked:
    """``op``'s element map, from its orders and its semantics."""
    sem = op.ov.semantics()
    if not isinstance(sem, Movement):
        return Blocked(Blocker.NOT_MOVEMENT, f"{type(op).__name__} is {sem}")
    ins = [b for b in op.buffers if b.direction == "in"]
    outs = [b for b in op.buffers if b.direction == "out"]
    if len(ins) != 1 or len(outs) != 1 or len(op.buffers) != 2:
        return Blocked(
            Blocker.NOT_MOVEMENT, f"{type(op).__name__} is not one input, one output"
        )
    (x,), (y,) = ins, outs
    if np.dtype(x.dtype) != np.dtype(y.dtype):
        # An element's bytes are what moves; a folded descriptor cannot
        # convert them.
        return Blocked(
            Blocker.NOT_MOVEMENT,
            f"{type(op).__name__} turns {np.dtype(x.dtype)} into {np.dtype(y.dtype)}",
        )
    src, dst = op.order(x), op.order(y)
    if len(src.slots) != len(dst.slots):
        raise ValueError(
            f"{type(op).__name__}: {len(src.slots)} input slots against "
            f"{len(dst.slots)} output slots"
        )
    source = np.full(y.elements, UNWRITTEN, dtype=np.int64)
    perm = sem.within.permutation() if sem.within is not None else None
    for k in range(len(src.slots)):
        read, written = src.indices(k), dst.indices(k)
        if read.size != written.size:
            raise ValueError(
                f"{type(op).__name__}: slot {k} reads {read.size} elements "
                f"and writes {written.size}"
            )
        if perm is not None:
            objects = read.size // perm.size
            read = read.reshape(objects, perm.size)[:, perm].reshape(-1)
        # A later write of an element wins, as it does on the device.
        source[written] = read
    return ElementMap(op, x, y, source, src.offset_by, dst.offset_by)


@dataclass(frozen=True)
class Fold:
    """A neighbour's order, rewritten to reach past the mover: over the
    mover's input (a folded read) or its output (a folded write), with the
    descriptors each slot then takes."""

    order: Order
    fits: tuple[Fit, ...]

    @property
    def bds(self) -> int:
        """Descriptors the busiest slot issues."""
        return max(len(f.bds) for f in self.fits)


def fold_read(
    consumer: Operator,
    buffer: BoundBuffer,
    mover: ElementMap,
    facts: DmaFacts,
    kind: TileKind = TileKind.SHIM,
) -> Fold | Blocked:
    """``consumer`` reading ``mover``'s input where it read ``buffer``, the
    mover's output."""
    order = consumer.order(buffer)
    if order.offset_by is not None and mover.in_by is not None:
        return Blocked(
            Blocker.OFFSETS, f"{order.offset_by.name} and {mover.in_by.name}"
        )
    if mover.out_by is not None:
        # Where the copy lands moves per call; a read of it does not.
        return Blocked(
            Blocker.OFFSETS, f"the mover's output moves by {mover.out_by.name}"
        )
    slots = [
        [mover.source[acc.indices()] for acc in order[k]]
        for k in range(len(order.slots))
    ]
    for k, pieces in enumerate(slots):
        missing = sum(int((p == UNWRITTEN).sum()) for p in pieces)
        if missing:
            return Blocked(
                Blocker.NOT_PRODUCED,
                f"slot {k} reads {missing} elements "
                f"{type(mover.op).__name__} does not write",
            )
    by = order.offset_by if order.offset_by is not None else mover.in_by
    return _fold(order, slots, mover.x, Direction.READ, facts, kind, by)


def fold_write(
    producer: Operator,
    buffer: BoundBuffer,
    mover: ElementMap,
    facts: DmaFacts,
    kind: TileKind = TileKind.SHIM,
) -> Fold | Blocked:
    """``producer`` writing ``mover``'s output where it wrote ``buffer``, the
    mover's input."""
    order = producer.order(buffer)
    if order.offset_by is not None and mover.out_by is not None:
        return Blocked(
            Blocker.OFFSETS, f"{order.offset_by.name} and {mover.out_by.name}"
        )
    if mover.in_by is not None:
        return Blocked(
            Blocker.OFFSETS, f"the mover's input moves by {mover.in_by.name}"
        )
    written = np.flatnonzero(mover.source != UNWRITTEN)
    read = mover.source[written]
    counts = np.bincount(read, minlength=mover.x.elements)
    if (counts > 1).any():
        return Blocked(
            Blocker.DUPLICATES,
            f"{type(mover.op).__name__} writes {int((counts > 1).sum())} input "
            f"elements to more than one place",
        )
    target = np.full(mover.x.elements, UNWRITTEN, dtype=np.int64)
    target[read] = written
    slots = [
        [target[acc.indices()] for acc in order[k]] for k in range(len(order.slots))
    ]
    for k, pieces in enumerate(slots):
        dropped = sum(int((p == UNWRITTEN).sum()) for p in pieces)
        if dropped:
            return Blocked(
                Blocker.DROPS,
                f"slot {k} writes {dropped} elements "
                f"{type(mover.op).__name__} drops",
            )
    by = order.offset_by if order.offset_by is not None else mover.out_by
    return _fold(order, slots, mover.y, Direction.WRITE, facts, kind, by)


def _fold(
    order: Order,
    slots: list[list[np.ndarray]],
    buffer: BoundBuffer,
    direction: Direction,
    facts: DmaFacts,
    kind: TileKind,
    offset_by: BoundValue | None,
) -> Fold | Blocked:
    whole = [np.concatenate(pieces) for pieces in slots]
    if (
        direction is Direction.READ
        and len(whole) > 1
        and not order.stream.replicate
        and all(np.array_equal(whole[0], w) for w in whole[1:])
    ):
        return Blocked(Blocker.MULTICAST, f"stream {order.stream.name!r}")
    fits = fit_slots(slots, buffer, direction, facts, kind)
    if isinstance(fits, Blocked):
        return fits
    folded = Order(order.stream, tuple(f.bds for f in fits), offset_by=offset_by)
    return Fold(folded, fits)


def fit_slots(
    slots: list[list[np.ndarray]],
    buffer: BoundBuffer,
    direction: Direction,
    facts: DmaFacts,
    kind: TileKind = TileKind.SHIM,
) -> tuple[Fit, ...] | Blocked:
    """Each slot's elements of ``buffer``, given in pieces (one per descriptor
    it had), as descriptors moving them in ``direction``: as one sequence if
    that fits, else piece by piece (on the shim, which chains descriptors). A
    write must also land no element twice, in a slot or across slots."""
    if direction is Direction.WRITE:
        # Across slots, two channels race for the element; within one, the
        # later write wins, which fit() rejects as not injective.
        every = np.concatenate([np.unique(np.concatenate(pieces)) for pieces in slots])
        if np.unique(every).size != every.size:
            return Blocked(Blocker.OVERLAP, buffer.name)
    limits = facts[kind]
    fits = []
    for k, pieces in enumerate(slots):
        got = fit(
            np.concatenate(pieces),
            buffer.elements,
            buffer.dtype,
            kind,
            direction,
            limits,
        )
        if isinstance(got, Unfit) and kind is TileKind.SHIM and len(pieces) > 1:
            parts = [
                fit(p, buffer.elements, buffer.dtype, kind, direction, limits)
                for p in pieces
            ]
            bad = next((u for u in parts if isinstance(u, Unfit)), None)
            if bad is None:
                bds = tuple(acc for part in parts for acc in part.bds)
                got = (
                    Fit(kind, direction, bds)
                    if len(bds) <= limits.bds
                    else Unfit(
                        Reason.BDS, f"{len(bds)} descriptors, the shim has {limits.bds}"
                    )
                )
            else:
                got = bad
        if isinstance(got, Unfit):
            return Blocked(Blocker.FIT, f"slot {k}: {got.detail}", got)
        fits.append(got)
    return tuple(fits)


def check_order(
    op: Operator, buffer: BoundBuffer, facts: DmaFacts
) -> tuple[Fit, ...] | Blocked:
    """Whether ``op``'s declared order for ``buffer`` is one the shim can
    move in the buffer's direction: a read may re-read, a write must be
    injective across every slot."""
    order = op.order(buffer)
    direction = Direction.READ if buffer.direction == "in" else Direction.WRITE
    slots = [[acc.indices() for acc in order[k]] for k in range(len(order.slots))]
    return fit_slots(slots, buffer, direction, facts)
