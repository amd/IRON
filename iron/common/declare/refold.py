# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Folding a DMA-only movement into a neighbour's transfers.

A :class:`~.semantics.Movement` overlay without cores computes nothing: slot
by slot, element ``k`` its input stream carries is element ``k`` its output
stream carries, so its two declared orders are a :class:`Relation` between
two buffers. A neighbour whose transfers compose with that relation can do
the movement itself, and the step goes away:

- a reader of the movement's output reads its input instead (a read may
  repeat an element: grouped-query attention's keys, read once per head);
- the writer of the movement's input writes its output instead (a write
  may not repeat one: a KV-cache row, written straight into the cache).

What goes through the neighbour's array is unchanged -- the same elements
in the same sequence -- so a fold is exact by construction; only where each
comes from or goes to in DDR moves. :class:`Refold` is one such change,
carried on the operator (:meth:`Operator.refolded`); :meth:`Operator.issued_order`
is the neighbour's own order with every fold applied.

The composition keeps the neighbour's own descriptors, slot for slot: each
dimension keeps its size and gets the stride it has through the relation,
and a dimension the relation is not affine along is split in two where
that makes it so (the heads of grouped-query attention become ``(groups,
repeat)`` with strides ``(matrix, 0)``). A re-read can sit only in the
iteration slot, so a split whose zero-stride half lands anywhere else needs
the neighbour to walk its batches in another order: :class:`Reorder`, legal
when the operator declares its batches independent
(:meth:`Operator.independent_batches`) and applied to every buffer alike.
"""

from __future__ import annotations

import enum
import functools
from dataclasses import dataclass
from typing import TYPE_CHECKING

import numpy as np

from ..tiling import Access, legalize
from .legality import Direction, access_legal

if TYPE_CHECKING:
    from .bound import BoundBuffer, BoundValue
    from .order import Order


class Unfoldable(ValueError):
    """This fold cannot be expressed in the neighbour's transfers."""


class Side(enum.Enum):
    """Which of the movement's buffers the neighbour held."""

    # The neighbour read the movement's output; it reads its input instead.
    READ = "read"
    # The neighbour wrote the movement's input; it writes its output instead.
    WRITE = "write"


@dataclass(frozen=True)
class Relation:
    """What a DMA-only movement moves: per slot, its input descriptors and
    its output descriptors, element ``k`` of one being element ``k`` of the
    other."""

    src_elements: int
    dst_elements: int
    src: tuple[tuple[Access, ...], ...]
    dst: tuple[tuple[Access, ...], ...]

    @classmethod
    def of(cls, src: "Order", dst: "Order", src_elements: int, dst_elements: int):
        if len(src.slots) != len(dst.slots):
            raise Unfoldable(
                f"the movement reads through {len(src.slots)} slots and writes "
                f"through {len(dst.slots)}"
            )
        for i, (a, b) in enumerate(zip(src.slots, dst.slots)):
            n_in, n_out = sum(x.count for x in a), sum(x.count for x in b)
            if n_in != n_out:
                raise Unfoldable(
                    f"slot {i} of the movement reads {n_in} elements and writes {n_out}"
                )
        return cls(src_elements, dst_elements, src.slots, dst.slots)

    def gather(self) -> np.ndarray:
        """For every output element, the input element it holds (-1: never written)."""
        return _gather(self)

    def scatter(self) -> np.ndarray:
        """For every input element, the output element it lands in (-1: never read)."""
        return _scatter(self)


def _pairs(rel: Relation) -> tuple[np.ndarray, np.ndarray]:
    src = [acc.indices() for slot in rel.src for acc in slot]
    dst = [acc.indices() for slot in rel.dst for acc in slot]
    return np.concatenate(src), np.concatenate(dst)


@functools.lru_cache(maxsize=16)
def _gather(rel: Relation) -> np.ndarray:
    src, dst = _pairs(rel)
    out = np.full(rel.dst_elements, -1, dtype=np.int64)
    if np.unique(dst).size != dst.size:
        raise Unfoldable("the movement writes an output element more than once")
    out[dst] = src
    return out


@functools.lru_cache(maxsize=16)
def _scatter(rel: Relation) -> np.ndarray:
    src, dst = _pairs(rel)
    out = np.full(rel.src_elements, -1, dtype=np.int64)
    if np.unique(src).size != src.size:
        raise Unfoldable(
            "the movement reads an input element more than once: a write "
            "cannot repeat it"
        )
    out[src] = dst
    return out


@dataclass(frozen=True)
class Adopted:
    """A per-call value a fold brings over from the movement: the base
    address it shifted its kept side by (a KV-cache position)."""

    dtype: str  # numpy dtype name


@dataclass(frozen=True)
class Refold:
    """One buffer of an operator, retargeted through a movement.

    ``buffer`` now reads (``READ``) or writes (``WRITE``) the movement's
    other buffer, of ``shape``; ``offset`` is the per-call value that
    buffer's transfers are shifted by, if the movement had one there.
    """

    buffer: str
    side: Side
    shape: tuple[int, ...]
    relation: Relation
    offset: Adopted | None = None

    @property
    def elements(self) -> int:
        return (
            self.relation.src_elements
            if self.side is Side.READ
            else self.relation.dst_elements
        )

    @property
    def value_name(self) -> str:
        """The name the adopted per-call value takes on the operator."""
        return f"{self.buffer}_offset"

    def compose(
        self, own: "Order", dtype, keep_count: bool, offset_by: "BoundValue | None"
    ) -> "Order":
        """``own``, the operator's order over the buffer it held, through the
        relation: the same descriptors, over the other buffer."""
        from .order import Order  # order imports tiling; a cycle through .legality

        if own.offset_by is not None:
            raise Unfoldable(
                f"{self.buffer} already moves at a per-call offset; a fold cannot "
                f"compose another relation onto it"
            )
        if self.side is Side.READ:
            index, direction = self.relation.gather(), Direction.MM2S
        else:
            index, direction = self.relation.scatter(), Direction.S2MM
        slots = []
        for accesses in own.slots:
            out: list[Access] = []
            for acc in accesses:
                out.extend(_compose_access(acc, index, self.elements, dtype, direction))
            if keep_count and len(out) != len(accesses):
                raise Unfoldable(
                    f"{self.buffer}: the fold needs {len(out)} descriptors where "
                    f"the operator's sequence issues {len(accesses)}"
                )
            slots.append(tuple(out))
        if direction is Direction.S2MM:
            written = np.concatenate([a.indices() for s in slots for a in s])
            if np.unique(written).size != written.size:
                raise Unfoldable(f"{self.buffer}: the folded write is not injective")
        return Order(own.stream, tuple(slots), offset_by)


def _affine_step(grid: np.ndarray, axis: int) -> int | None:
    """The constant difference along ``axis``, or ``None`` if it varies."""
    d = np.diff(grid, axis=axis)
    step = int(d.flat[0])
    return step if bool((d == step).all()) else None


def _split_axis(grid: np.ndarray, axis: int) -> list[tuple[int, int]] | None:
    """``axis`` as ``(outer, inner)`` dimensions each affine, the fewest outer first."""
    n = grid.shape[axis]
    for a in range(2, n):
        if n % a:
            continue
        shape = grid.shape[:axis] + (a, n // a) + grid.shape[axis + 1 :]
        g = grid.reshape(shape)
        outer, inner = _affine_step(g, axis), _affine_step(g, axis + 1)
        if outer is not None and inner is not None:
            return [(a, outer), (n // a, inner)]
    return None


def _place(entries: list[tuple[int, int]]) -> list[tuple[int, int]] | None:
    """``entries`` (outermost first) in the four slots: unit entries give way
    from the outside in; ``None`` if there are more real ones than slots."""
    entries = list(entries)
    while len(entries) > 4:
        unit = next((i for i, (n, _) in enumerate(entries) if n == 1), None)
        if unit is None:
            return None
        del entries[unit]
    return [(1, 0)] * (4 - len(entries)) + entries


def _compose_access(
    acc: Access, index: np.ndarray, elements: int, dtype, direction: "Direction"
) -> list[Access]:
    """One descriptor through ``index``: its own slots where they fit, else
    the legalized pattern (which may be several descriptors)."""
    grid = index[acc.indices()]
    if bool((grid < 0).any()):
        what = "never wrote" if direction is Direction.MM2S else "never reads"
        raise Unfoldable(f"the descriptor covers elements the movement {what}")
    grid = grid.reshape(acc.sizes)
    entries: list[tuple[int, int]] = []
    for axis, (n, stride) in enumerate(zip(acc.sizes, acc.strides)):
        if n == 1:
            # Unit dimensions keep their stride: it moves nothing, but it is
            # spelled in the descriptor, and an unchanged one stays unchanged.
            entries.append((1, stride))
            continue
        step = _affine_step(grid, axis)
        if step is not None:
            entries.append((n, step))
            continue
        split = _split_axis(grid, axis)
        if split is None:
            raise Unfoldable(
                f"dimension {axis} ({n} at stride {stride}) is not affine through "
                f"the movement, whole or split in two"
            )
        entries.extend(split)
    offset = int(grid.flat[0])
    placed = _place(entries)
    if placed is not None:
        sizes = tuple(n for n, _ in placed)
        strides = tuple(s for _, s in placed)
        folded = Access(elements, offset, sizes, strides)  # type: ignore[arg-type]
        if access_legal(folded, direction, dtype) is None:
            return [folded]
    return _legalized(entries, offset, elements, dtype, direction)


def _legalized(entries, offset, elements, dtype, direction) -> list[Access]:
    real = [(n, s) for n, s in entries if n != 1]
    try:
        out = legalize(
            elements, offset, [n for n, _ in real], [s for _, s in real], dtype
        )
    except ValueError as e:
        raise Unfoldable(str(e)) from None
    for acc in out:
        reason = access_legal(acc, direction, dtype)
        if reason is not None:
            raise Unfoldable(reason)
    return out


@dataclass(frozen=True)
class Reorder:
    """An operator's batches walked in another order: split into ``(outer,
    inner)``, inner-major. Batch ``o * inner + i`` goes at ``i * outer + o``.

    Legal only on an operator that declares its batches independent, and
    applied to every buffer that has the batch axis, so each batch's
    operands still meet.
    """

    outer: int
    inner: int

    @property
    def batches(self) -> int:
        return self.outer * self.inner

    @property
    def permutation(self) -> list[int]:
        """The batch at each position of the new walk."""
        return [
            o * self.inner + i for i in range(self.inner) for o in range(self.outer)
        ]

    def apply(self, order: "Order", buffer: "BoundBuffer", keep_count: bool) -> "Order":
        """``order`` over ``buffer`` with its batches in this walk."""
        from .order import Order

        if buffer.batch_axes < 1 or buffer.shape[0] != self.batches:
            return order
        per = buffer.elements // self.batches
        direction = Direction.MM2S if order.stream.direction == "in" else Direction.S2MM
        slots = tuple(
            self._slot(accs, per, buffer.elements, buffer.dtype, direction)
            for accs in order.slots
        )
        if keep_count and any(len(a) != len(b) for a, b in zip(slots, order.slots)):
            raise Unfoldable(
                f"{buffer.name}: walking the batches as {self} changes how many "
                f"descriptors the operator's sequence issues"
            )
        return Order(order.stream, slots, order.offset_by)

    def _slot(self, accs, per, elements, dtype, direction) -> tuple[Access, ...]:
        nb = self.batches
        parts = [acc.indices() for acc in accs]
        flat = np.concatenate(parts)
        if flat.size % nb:
            raise Unfoldable(
                f"a slot's {flat.size} elements do not split into {nb} batches"
            )
        chunks = flat.reshape(nb, -1)
        if not bool((chunks // per == np.arange(nb)[:, None]).all()):
            raise Unfoldable("a slot does not walk the batches outermost, in order")
        want = chunks[self.permutation].reshape(-1)
        if len(accs) == nb and all(p.size == chunks.shape[1] for p in parts):
            out = tuple(accs[b] for b in self.permutation)
        elif len(accs) == 1:
            out = self._single(accs[0], per, elements, dtype, direction)
        else:
            raise Unfoldable(
                f"a slot of {len(accs)} descriptors over {nb} batches has no batch walk to reorder"
            )
        got = np.concatenate([a.indices() for a in out])
        if not np.array_equal(got, want):
            raise Unfoldable(
                "the reordered descriptors do not walk the batches as asked"
            )
        return out

    def _single(
        self, acc: Access, per, elements, dtype, direction
    ) -> tuple[Access, ...]:
        """One descriptor, its batch dimension split and walked inner-major.

        The batch dimension is the one of ``batches`` at the batch stride;
        a descriptor that walks the batches inside one contiguous run (a
        whole vector per column) has the run split first.
        """
        nb, inner, outer = self.batches, self.inner, self.outer
        walk = [(inner, per), (outer, inner * per)]
        axis = next(
            (
                j
                for j, (n, s) in enumerate(zip(acc.sizes, acc.strides))
                if n == nb and s == per and all(m == 1 for m in acc.sizes[:j])
            ),
            None,
        )
        if axis is not None:
            entries = list(zip(acc.sizes, acc.strides))
            placed = _place(entries[:axis] + walk + entries[axis + 1 :])
            if placed is not None:
                folded = Access(
                    elements,
                    acc.offset,
                    tuple(n for n, _ in placed),  # type: ignore[arg-type]
                    tuple(s for _, s in placed),  # type: ignore[arg-type]
                )
                if access_legal(folded, direction, dtype) is None:
                    return (folded,)
            entries = entries[:axis] + walk + entries[axis + 1 :]
            real = [(n, s) for n, s in entries if n != 1]
        elif acc.count == nb * per and _contiguous(acc):
            real = walk + [(per, 1)]
        else:
            raise Unfoldable(f"{acc} has no batch dimension to reorder")
        try:
            return tuple(
                legalize(
                    elements,
                    acc.offset,
                    [n for n, _ in real],
                    [s for _, s in real],
                    dtype,
                )
            )
        except ValueError as e:
            raise Unfoldable(str(e)) from None


def _contiguous(acc: Access) -> bool:
    idx = acc.indices()
    return bool(np.array_equal(idx, np.arange(idx[0], idx[0] + idx.size)))
