# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Folds of a traced graph: every DMA-only movement step, and the ways its
neighbours could do it instead.

A step whose overlay is :class:`~iron.common.declare.Movement` without
cores computes nothing, so it can go (:mod:`iron.common.declare.refold`):

- **into its readers** (:attr:`Side.READ`): every step that reads its output
  reads its input through the composed order. A read may repeat, so this is
  how a repeat goes. The output must be an intermediate: a state or a
  graph output has to be written.
- **into its writer** (:attr:`Side.WRITE`): the step that wrote its input
  writes its output instead, at the movement's per-call offset if it had
  one. A write must be injective, so a repeat cannot go this way; a copy
  into a cache can. The input must be an intermediate the movement alone
  reads.

Both keep every transfer where it happened relative to the others it could
race with: a read moved later must not pass a write of what it reads, a
write moved earlier must not pass a read or write of what it writes.

:func:`candidates` lists every fold, legal or not (with the reason), without
choosing: which to take is a cost question. :func:`apply` takes a set of
them; :class:`FoldAll` is the policy that takes every one it can.
"""

from __future__ import annotations

import dataclasses
from collections.abc import Iterator, Sequence
from typing import Protocol

import numpy as np

from ..declare import Movement, Operator
from ..declare.field import Incompatible
from ..declare.refold import Adopted, Refold, Relation, Reorder, Side, Unfoldable
from .handle import Affine, Handle
from .trace import Binding, TracedGraph, TracedStep


@dataclasses.dataclass(frozen=True)
class Fold:
    """A legal fold: movement step ``movement`` done by the steps in
    ``neighbours``, each taking its ``refolds`` entry and walking its batches
    as its ``reorders`` entry says."""

    movement: int
    side: Side
    neighbours: tuple[int, ...]
    refolds: tuple[Refold, ...]
    reorders: tuple[Reorder | None, ...]
    # What the movement's per-call offset on the side kept was bound to; the
    # neighbours' transfers move by it now.
    offset: Affine | None = None

    def describe(self, traced: TracedGraph) -> str:
        what = type(traced.steps[self.movement].op).__name__
        into = ", ".join(
            f"{type(traced.steps[i].op).__name__}@{i}"
            + (f" {r.outer}x{r.inner}" if r is not None else "")
            for i, r in zip(self.neighbours, self.reorders)
        )
        return f"{what}@{self.movement} {self.side.value} into {into}"


@dataclasses.dataclass(frozen=True)
class Refused:
    """A fold that is not legal, and why."""

    movement: int
    side: Side
    reason: str

    def describe(self, traced: TracedGraph) -> str:
        what = type(traced.steps[self.movement].op).__name__
        return f"{what}@{self.movement} {self.side.value}: {self.reason}"


def _named(h: Handle) -> str:
    """The buffer a handle is, or is a slice of."""
    return h.parent.name if h.parent is not None else h.name


def _touches(step: TracedStep, name: str, *, reads: bool, writes: bool) -> bool:
    handles = (step.inputs if reads else []) + (step.outputs if writes else [])
    return any(_named(h) == name for h in handles)


def _graph_results(traced: TracedGraph) -> set[str]:
    names = {h.name for h in traced.outputs}
    names |= {h.name for h in traced.carry.values() if isinstance(h, Handle)}
    return names


def movements(traced: TracedGraph, dev) -> Iterator[int]:
    """The steps a fold could remove: DMA-only movements, one buffer each way."""
    for i, step in enumerate(traced.steps):
        tuned = step.op.tuned(dev)
        if tuned.ov.semantics() != Movement(has_cores=False):
            continue
        if sorted(b.direction for b in tuned.buffers) == ["in", "out"]:
            yield i


def candidates(
    traced: TracedGraph, dev, memo: dict | None = None
) -> list[Fold | Refused]:
    """Every fold of every movement step, each side, legal or refused.

    ``memo`` caches whether an operator takes a fold, across calls: every
    layer of a model asks the same question of the same design.
    """
    memo = {} if memo is None else memo
    out: list[Fold | Refused] = []
    for i in movements(traced, dev):
        for side in (Side.READ, Side.WRITE):
            try:
                out.append(_fold(traced, dev, i, side, memo))
            except Unfoldable as e:
                out.append(Refused(i, side, str(e)))
    return out


def _binding_for(traced: TracedGraph, op: Operator, name: str) -> Binding:
    for b in traced.bindings:
        if b.op is op and b.member.name == name:
            return b
    raise Unfoldable(f"no graph binding for {type(op).__name__}.{name}")


def _ends(traced: TracedGraph, i: int) -> tuple[Handle, Handle]:
    """The movement step's input and output handles."""
    step = traced.steps[i]
    names = [b.name for b in step.op.buffers]
    x = next(b for b in step.op.buffers if b.direction == "in")
    y = next(b for b in step.op.buffers if b.direction == "out")
    return step.slots[names.index(x.name)], step.slots[names.index(y.name)]


def _fold(traced: TracedGraph, dev, i: int, side: Side, memo: dict) -> Fold:
    step = traced.steps[i]
    tuned = step.op.tuned(dev)
    x_buf = next(b for b in tuned.buffers if b.direction == "in")
    y_buf = next(b for b in tuned.buffers if b.direction == "out")
    x_h, y_h = _ends(traced, i)
    ox, oy = tuned.issued_order(x_buf), tuned.issued_order(y_buf)
    relation = Relation.of(ox, oy, x_buf.elements, y_buf.elements)
    if side is Side.READ:
        kept, gone, kept_order, gone_order = x_h, y_h, ox, oy
    else:
        kept, gone, kept_order, gone_order = y_h, x_h, oy, ox
    if gone.role != "intermediate" or gone.parent is not None:
        raise Unfoldable(f"{gone.name} is a {gone.role}, which must stay written")
    if gone.name in _graph_results(traced):
        raise Unfoldable(f"{gone.name} is a result of the graph")
    if gone_order.offset_by is not None:
        raise Unfoldable(
            f"the movement moves {gone.name} at a per-call offset, so where an "
            f"element lies there changes per call"
        )
    offset, expression = None, None
    if kept_order.offset_by is not None:
        offset = Adopted(np.dtype(kept_order.offset_by.dtype).name)
        expression = _binding_for(traced, step.op, kept_order.offset_by.name).expression
    if side is Side.READ:
        steps = _readers(traced, i, gone.name)
        for j in steps:
            _no_hazard(traced, i, j, kept, reads=False, writes=True)
    else:
        steps = [_writer(traced, i, gone.name)]
        _no_hazard(traced, steps[0], i, kept, reads=True, writes=True)
    refolds, reorders = [], []
    for j in steps:
        refold, reorder = _refold(
            traced, dev, j, gone, kept, side, relation, offset, memo
        )
        refolds.append(refold)
        reorders.append(reorder)
    return Fold(i, side, tuple(steps), tuple(refolds), tuple(reorders), expression)


def _readers(traced: TracedGraph, i: int, name: str) -> list[int]:
    found = []
    for j, s in enumerate(traced.steps):
        if j == i:
            continue
        if _touches(s, name, reads=False, writes=True):
            raise Unfoldable(f"step {j} also writes {name}")
        if _touches(s, name, reads=True, writes=False):
            if j < i:
                raise Unfoldable(f"step {j} reads {name} before the movement writes it")
            if any(h.parent is not None for h in s.inputs if _named(h) == name):
                raise Unfoldable(f"step {j} reads a slice of {name}")
            found.append(j)
    if not found:
        raise Unfoldable(f"nothing reads {name}")
    return found


def _writer(traced: TracedGraph, i: int, name: str) -> int:
    writers = [
        j
        for j, s in enumerate(traced.steps)
        if j != i and _touches(s, name, reads=False, writes=True)
    ]
    readers = [
        j
        for j, s in enumerate(traced.steps)
        if j != i and _touches(s, name, reads=True, writes=False)
    ]
    if readers:
        raise Unfoldable(f"{name} is read by step {readers[0]} as well")
    if len(writers) != 1 or writers[0] > i:
        raise Unfoldable(
            f"{name} is not written by exactly one step before the movement"
        )
    j = writers[0]
    if any(h.parent is not None for h in traced.steps[j].outputs if _named(h) == name):
        raise Unfoldable(f"step {j} writes a slice of {name}")
    return j


def _no_hazard(
    traced: TracedGraph, lo: int, hi: int, h: Handle, *, reads: bool, writes: bool
) -> None:
    """Nothing strictly between steps ``lo`` and ``hi`` touches ``h`` that way."""
    name = _named(h)
    for k in range(lo + 1, hi):
        if _touches(traced.steps[k], name, reads=reads, writes=writes):
            raise Unfoldable(
                f"step {k} ({type(traced.steps[k].op).__name__}) touches {name} "
                f"between the steps the fold would join"
            )


def _walks(op: Operator) -> list[Reorder | None]:
    """The batch walks to try, the declared one first."""
    nb = op.independent_batches()
    return [None] + [
        Reorder(nb // inner, inner) for inner in range(2, nb) if nb % inner == 0
    ]


def _takes(
    op: Operator, dev, refolds: Sequence[Refold], walk, memo: dict
) -> str | None:
    """Why ``op`` cannot take ``refolds`` walking its batches as ``walk``; ``None`` if it can."""
    key = (op.design_key(), tuple(refolds), walk)
    if key not in memo:
        try:
            op.refolded(tuple(refolds), walk).tuned(dev)
            memo[key] = None
        except (Unfoldable, Incompatible) as e:
            memo[key] = str(e)
    return memo[key]


def _refold(
    traced: TracedGraph,
    dev,
    j: int,
    gone: Handle,
    kept: Handle,
    side: Side,
    relation: Relation,
    offset: Adopted | None,
    memo: dict,
) -> tuple[Refold, Reorder | None]:
    """How step ``j``'s buffer on ``gone`` is retargeted to ``kept``, and the
    batch walk that makes it fit."""
    step = traced.steps[j]
    op = step.op
    if not op.accepts_folds():
        raise Unfoldable(
            f"{type(op).__name__}@{j} computes its own descriptors, so a fold "
            f"cannot change them"
        )
    held = [k for k, h in enumerate(step.slots) if h.name == gone.name]
    if len(held) != 1:
        raise Unfoldable(
            f"{type(op).__name__}@{j} holds {gone.name} in {len(held)} buffers"
        )
    buf = op.buffers[held[0]]
    want = "in" if side is Side.READ else "out"
    if buf.direction != want:
        raise Unfoldable(
            f"{type(op).__name__}.{buf.name} is an {buf.direction} buffer; the "
            f"fold needs an {want} one"
        )
    refold = Refold(buf.name, side, kept.shape, relation, offset)
    reasons = []
    for walk in _walks(op):
        reason = _takes(op, dev, [refold], walk, memo)
        if reason is None:
            return refold, walk
        reasons.append(reason)
    raise Unfoldable(f"{type(op).__name__}@{j}: {reasons[0]}")


def apply(traced: TracedGraph, folds: Sequence[Fold], dev) -> TracedGraph:
    """``traced`` with every fold in ``folds`` taken: their movement steps
    gone, their neighbours on refolded operators, the movements' per-call
    values bound on those. Raises :class:`Unfoldable` if two folds cannot
    share a neighbour."""
    removed = {f.movement for f in folds}
    if len(removed) != len(folds):
        raise Unfoldable("two folds remove the same movement")
    edits: dict[int, list[tuple[Fold, int]]] = {}
    for f in folds:
        for n, j in enumerate(f.neighbours):
            if j in removed:
                raise Unfoldable(f"step {j} is folded into and folded away")
            edits.setdefault(j, []).append((f, n))
    renamed: dict[str, Handle] = {}
    for f in folds:
        x_h, y_h = _ends(traced, f.movement)
        kept, gone = (x_h, y_h) if f.side is Side.READ else (y_h, x_h)
        renamed[gone.name] = kept
    swapped: dict[int, Operator] = {}  # id(step) -> its new operator
    steps: list[TracedStep] = []
    for k, s in enumerate(traced.steps):
        if k in removed:
            continue
        if k not in edits:
            steps.append(s)
            continue
        refolds = tuple(f.refolds[n] for f, n in edits[k])
        walks = {f.reorders[n] for f, n in edits[k]} - {None}
        if len(walks) > 1:
            raise Unfoldable(f"step {k}: its folds need different batch walks {walks}")
        op = s.op.refolded(refolds, next(iter(walks), None))
        op.tuned(dev)  # every order composes, together
        swapped[id(s)] = op

        def move(hs):
            return [renamed.get(h.name, h) for h in hs]

        steps.append(TracedStep(op, move(s.slots), move(s.inputs), move(s.outputs)))
    by_old_op = {id(s.op): swapped[id(s)] for s in traced.steps if id(s) in swapped}
    gone_ops = {id(traced.steps[f.movement].op) for f in folds}
    bindings: list[Binding] = []
    for b in traced.bindings:
        if id(b.op) in gone_ops:
            continue
        new = by_old_op.get(id(b.op))
        if new is None:
            bindings.append(b)
            continue
        on_op = any(v is b.member for v in b.op.values)
        owner_values = new.values if on_op else new.ov.values
        member = next(v for v in owner_values if v.name == b.member.name)
        bindings.append(Binding(new, member, b.expression))
    # A movement's offset on the side it kept now shifts its neighbours'.
    for f in folds:
        if f.offset is None:
            continue
        for j, refold in zip(f.neighbours, f.refolds):
            op = swapped[id(traced.steps[j])]
            member = next(v for v in op.values if v.name == refold.value_name)
            bindings.append(Binding(op, member, f.offset))
    return dataclasses.replace(traced, steps=steps, bindings=bindings)


class Folding(Protocol):
    """What ``compile(fold=...)`` takes: a policy that folds a traced graph."""

    def fold(self, traced: TracedGraph, dev) -> TracedGraph: ...


@dataclasses.dataclass(frozen=True)
class FoldAll:
    """Take every fold that is legal, one per movement, preferring ``sides``
    in order where both are. What a device where every step costs a
    dispatch wants; elsewhere a cost model chooses."""

    sides: tuple[Side, ...] = (Side.READ, Side.WRITE)
    # When given, only movements of these classes, and only into these.
    only: tuple[type[Operator], ...] = ()
    into: tuple[type[Operator], ...] = ()

    def _wanted(self, traced: TracedGraph, f: Fold) -> bool:
        if f.side not in self.sides:
            return False
        if self.only and not isinstance(traced.steps[f.movement].op, self.only):
            return False
        return not self.into or all(
            isinstance(traced.steps[j].op, self.into) for j in f.neighbours
        )

    def choose(self, traced: TracedGraph, dev) -> list[Fold]:
        found = [
            c
            for c in candidates(traced, dev)
            if isinstance(c, Fold) and self._wanted(traced, c)
        ]
        rank = {side: n for n, side in enumerate(self.sides)}
        chosen: dict[int, Fold] = {}
        for f in sorted(found, key=lambda f: (f.movement, rank[f.side])):
            chosen.setdefault(f.movement, f)
        # A neighbour may take folds from several movements, but not two batch
        # walks; the earlier movement keeps its walk.
        taken: list[Fold] = []
        walks: dict[int, Reorder] = {}
        for f in chosen.values():
            clash = any(
                r is not None and walks.get(j, r) != r
                for j, r in zip(f.neighbours, f.reorders)
            )
            if clash or any(j in chosen for j in f.neighbours):
                continue
            for j, r in zip(f.neighbours, f.reorders):
                if r is not None:
                    walks[j] = r
            taken.append(f)
        return taken

    def fold(self, traced: TracedGraph, dev) -> TracedGraph:
        return apply(traced, self.choose(traced, dev), dev)
