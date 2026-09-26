# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Folds of a traced graph: steps whose work a neighbour can do instead.

A step whose overlay is :class:`~iron.common.declare.Movement` without
cores computes nothing, so it can go (:mod:`iron.common.declare.refold`):

- **into its readers** (:attr:`Kind.READ`): every step that reads its output
  reads its input through the composed order. A read may repeat, so this is
  how a repeat goes. The output must be an intermediate: a state or a
  graph output has to be written.
- **into its writer** (:attr:`Kind.WRITE`): the step that wrote its input
  writes its output instead, at the movement's per-call offset if it had
  one. A write must be injective, so a repeat cannot go this way; a copy
  into a cache can. The input must be an intermediate the movement alone
  reads.

A step whose array is elementwise, one input to one output
(:meth:`~iron.common.declare.Overlay.pointwise`), can go **into its
producer's cores** (:attr:`Kind.EPILOGUE`), when the producer's array hosts
an epilogue (:meth:`~iron.common.declare.Overlay.with_epilogue`): each
output object is final when released, and the kernel runs on it there.

Every kind keeps each transfer where it happened relative to the others it
could race with: a read moved later must not pass a write of what it
reads, a write moved earlier must not pass a read or write of what it
writes.

:func:`candidates` lists every fold, legal or not (with the reason), without
choosing: which to take is a cost question. :func:`apply` takes a set of
them; :class:`FoldAll` is the policy that takes every one it can.
"""

from __future__ import annotations

import dataclasses
import enum
from collections.abc import Iterator, Sequence
from typing import Protocol

import numpy as np

from ..declare import Local, Movement, Operator, Overlay
from ..declare.field import Incompatible
from ..declare.refold import Adopted, Refold, Relation, Reorder, Side, Unfoldable
from ..design.target import Target
from ..image.coresidence import fits
from ..image.fusion import format_params, generate_design
from ..kernels import kernels_dir
from .handle import Affine, Handle
from .trace import Binding, TracedGraph, TracedStep


class Kind(enum.Enum):
    """How a step's work goes to a neighbour."""

    READ = "read"  # a movement done by its readers' reads
    WRITE = "write"  # a movement done by its writer's write
    EPILOGUE = "epilogue"  # an elementwise step run by its producer's cores

    @property
    def side(self) -> Side:
        """The DMA side a movement fold of this kind composes."""
        return {Kind.READ: Side.READ, Kind.WRITE: Side.WRITE}[self]


@dataclasses.dataclass(frozen=True)
class Edit:
    """What a fold changes on one neighbouring step: a buffer retargeted
    through a movement, the batch walk that needs, an epilogue its cores
    now run."""

    step: int
    refold: Refold | None = None
    reorder: Reorder | None = None
    epilogue: Overlay | None = None


@dataclasses.dataclass(frozen=True)
class Fold:
    """A legal fold: step ``removed`` done by its neighbours, as ``edits``
    say. ``offset`` is what the removed step's per-call offset on the side
    kept was bound to; the neighbours' transfers move by it now."""

    removed: int
    kind: Kind
    edits: tuple[Edit, ...]
    offset: Affine | None = None

    @property
    def neighbours(self) -> tuple[int, ...]:
        return tuple(e.step for e in self.edits)

    def describe(self, traced: TracedGraph) -> str:
        what = type(traced.steps[self.removed].op).__name__
        into = ", ".join(
            f"{type(traced.steps[e.step].op).__name__}@{e.step}"
            + (f" {e.reorder.outer}x{e.reorder.inner}" if e.reorder else "")
            for e in self.edits
        )
        return f"{what}@{self.removed} {self.kind.value} into {into}"


@dataclasses.dataclass(frozen=True)
class Refused:
    """A fold that is not legal, and why."""

    removed: int
    kind: Kind
    reason: str

    def describe(self, traced: TracedGraph) -> str:
        what = type(traced.steps[self.removed].op).__name__
        return f"{what}@{self.removed} {self.kind.value}: {self.reason}"


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


def pointwise_steps(traced: TracedGraph, dev) -> Iterator[int]:
    """The steps an epilogue fold could remove: elementwise, one in, one out."""
    for i, step in enumerate(traced.steps):
        tuned = step.op.tuned(dev)
        if tuned.ov.semantics() != Local(1):
            continue
        if sorted(b.direction for b in tuned.buffers) == ["in", "out"]:
            yield i


def candidates(
    traced: TracedGraph, dev, memo: dict | None = None
) -> list[Fold | Refused]:
    """Every fold of every step that could go, each kind, legal or refused.

    ``memo`` caches whether an operator takes a fold, across calls: every
    layer of a model asks the same question of the same design.
    """
    memo = {} if memo is None else memo
    out: list[Fold | Refused] = []
    for i in movements(traced, dev):
        for kind in (Kind.READ, Kind.WRITE):
            try:
                out.append(_fold(traced, dev, i, kind, memo))
            except Unfoldable as e:
                out.append(Refused(i, kind, str(e)))
    for i in pointwise_steps(traced, dev):
        try:
            out.append(_epilogue(traced, dev, i, memo))
        except Unfoldable as e:
            out.append(Refused(i, Kind.EPILOGUE, str(e)))
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


def _fold(traced: TracedGraph, dev, i: int, kind: Kind, memo: dict) -> Fold:
    side = kind.side
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
        raise Unfoldable(f"{gone.name} ({gone.role}) must stay written")
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
        _not_read_by(traced, steps[0], kept)
    edits = []
    for j in steps:
        refold, reorder = _refold(
            traced, dev, j, gone, kept, side, relation, offset, memo
        )
        edits.append(Edit(j, refold=refold, reorder=reorder))
    return Fold(i, kind, tuple(edits), expression)


def _epilogue(traced: TracedGraph, dev, i: int, memo: dict) -> Fold:
    """Elementwise step ``i`` run by the cores of the step that wrote its input."""
    step = traced.steps[i]
    tuned = step.op.tuned(dev)
    x_buf = next(b for b in tuned.buffers if b.direction == "in")
    y_buf = next(b for b in tuned.buffers if b.direction == "out")
    x_h, y_h = _ends(traced, i)
    if any(b.op is step.op for b in traced.bindings):
        raise Unfoldable(f"{type(step.op).__name__} is written a per-call value")
    ox, oy = tuned.issued_order(x_buf), tuned.issued_order(y_buf)
    if ox.offset_by is not None or oy.offset_by is not None:
        raise Unfoldable("its transfers move at a per-call offset")
    for slot in range(len(ox.slots)):
        if not np.array_equal(ox.indices(slot), oy.indices(slot)):
            raise Unfoldable(
                "it does not write each element where it read it, so its "
                "kernel cannot run in place of the store"
            )
    if x_h.role != "intermediate" or x_h.parent is not None:
        raise Unfoldable(f"{x_h.name} ({x_h.role}) must stay written")
    if x_h.name in _graph_results(traced):
        raise Unfoldable(f"{x_h.name} is a result of the graph")
    j = _writer(traced, i, x_h.name)
    _no_hazard(traced, j, i, y_h, reads=True, writes=True)
    _not_read_by(traced, j, y_h)
    producer = traced.steps[j].op
    at = [k for k, h in enumerate(traced.steps[j].slots) if h.name == x_h.name]
    if len(at) != 1 or producer.buffers[at[0]].direction != "out":
        raise Unfoldable(f"{type(producer).__name__}@{j} does not write it alone")
    epilogue = step.op.ov
    key = ("epilogue", producer.design_key(), epilogue.design_key())
    if key not in memo:
        memo[key] = _hosts(producer, epilogue, at[0], dev)
    if memo[key] is not None:
        raise Unfoldable(f"{type(producer).__name__}@{j}: {memo[key]}")
    return Fold(i, Kind.EPILOGUE, (Edit(j, epilogue=epilogue),))


def _hosts(producer: Operator, epilogue: Overlay, slot: int, dev) -> str | None:
    """Why ``producer``'s array cannot run ``epilogue`` on the objects of its
    buffer ``slot``; ``None`` if it can."""
    ov = producer.ov.with_epilogue(epilogue)
    if ov is None:
        return f"{type(producer.ov).__name__} hosts no epilogue"
    try:
        tuned = producer.replace(ov=ov).tuned(dev)
    except (Unfoldable, Incompatible) as e:
        return str(e)
    stream = tuned.buffers[slot].stream(tuned.ov)
    if stream is None:
        return "its output names no stream"
    try:
        pointwise = epilogue.pointwise(Target(dev, kernels_dir()), stream.elements)
    except ValueError as e:  # the kernel's own size rules
        return str(e)
    if pointwise is None:
        return f"{type(epilogue).__name__} has no pointwise kernel"
    # The epilogue's staging tile and kernel take local memory the array may
    # not have: the placer and the buffer allocation say.
    generated = generate_design(tuned.generator())
    params = format_params({n: str(t) for n, t in generated.params.items()})
    return fits({"host": str(generated.device)}, params)


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


def _not_read_by(traced: TracedGraph, j: int, h: Handle) -> None:
    """Step ``j``, about to write ``h``, does not also read it: its reads and
    its new writes would race within the step."""
    if _touches(traced.steps[j], _named(h), reads=True, writes=False):
        raise Unfoldable(
            f"{type(traced.steps[j].op).__name__}@{j} reads {_named(h)}, which it "
            f"would now write"
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


def edited(op: Operator, edits: Sequence[Edit]) -> Operator:
    """``op`` with ``edits`` (every one on its step) made: its refolds and
    batch walk, then its epilogue."""
    refolds = tuple(e.refold for e in edits if e.refold is not None)
    walks = {e.reorder for e in edits} - {None}
    if len(walks) > 1:
        raise Unfoldable(f"its folds need different batch walks {walks}")
    if refolds or walks:
        op = op.refolded(refolds, next(iter(walks), None))
    epilogues = [e.epilogue for e in edits if e.epilogue is not None]
    if len(epilogues) > 1:
        raise Unfoldable("two epilogues on one array")
    if epilogues:
        ov = op.ov.with_epilogue(epilogues[0])
        if ov is None:
            raise Unfoldable(f"{type(op.ov).__name__} hosts no epilogue")
        op = op.replace(ov=ov)
    return op


def _renames(traced: TracedGraph, f: Fold) -> tuple[Handle, Handle]:
    """What the fold's neighbours hold instead: (gone, kept)."""
    x_h, y_h = _ends(traced, f.removed)
    return (y_h, x_h) if f.kind is Kind.READ else (x_h, y_h)


def apply(traced: TracedGraph, folds: Sequence[Fold], dev) -> TracedGraph:
    """``traced`` with every fold in ``folds`` taken: their steps gone, their
    neighbours on edited operators, a removed step's per-call values bound on
    those. Raises :class:`Unfoldable` if two folds cannot share a neighbour."""
    removed = {f.removed for f in folds}
    if len(removed) != len(folds):
        raise Unfoldable("two folds remove the same step")
    edits: dict[int, list[Edit]] = {}
    for f in folds:
        for e in f.edits:
            if e.step in removed:
                raise Unfoldable(f"step {e.step} is folded into and folded away")
            edits.setdefault(e.step, []).append(e)
    renamed: dict[str, Handle] = {}
    for f in folds:
        gone, kept = _renames(traced, f)
        renamed[gone.name] = kept
    swapped: dict[int, Operator] = {}  # id(step) -> its new operator
    steps: list[TracedStep] = []
    for k, s in enumerate(traced.steps):
        if k in removed:
            continue
        if k not in edits:
            steps.append(s)
            continue
        try:
            op = edited(s.op, edits[k])
        except Unfoldable as e:
            raise Unfoldable(f"step {k}: {e}") from None
        op.tuned(dev)  # every order composes, together
        swapped[id(s)] = op

        def move(hs):
            return [renamed.get(h.name, h) for h in hs]

        steps.append(TracedStep(op, move(s.slots), move(s.inputs), move(s.outputs)))
    by_old_op = {id(s.op): swapped[id(s)] for s in traced.steps if id(s) in swapped}
    gone_ops = {id(traced.steps[f.removed].op) for f in folds}
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
        for e in f.edits:
            op = swapped[id(traced.steps[e.step])]
            member = next(v for v in op.values if v.name == e.refold.value_name)
            bindings.append(Binding(op, member, f.offset))
    return dataclasses.replace(traced, steps=steps, bindings=bindings)


class Folding(Protocol):
    """What ``compile(fold=...)`` takes: a policy that folds a traced graph."""

    def fold(self, traced: TracedGraph, dev) -> TracedGraph: ...


@dataclasses.dataclass(frozen=True)
class FoldAll:
    """Take every fold that is legal, one per removed step, preferring
    ``kinds`` in order where several are. What a device where every step
    costs a dispatch wants; elsewhere a cost model chooses."""

    kinds: tuple[Kind, ...] = (Kind.READ, Kind.WRITE, Kind.EPILOGUE)
    # When given, only steps of these classes, and only into these.
    only: tuple[type[Operator], ...] = ()
    into: tuple[type[Operator], ...] = ()

    def _wanted(self, traced: TracedGraph, f: Fold) -> bool:
        if f.kind not in self.kinds:
            return False
        if self.only and not isinstance(traced.steps[f.removed].op, self.only):
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
        rank = {kind: n for n, kind in enumerate(self.kinds)}
        chosen: dict[int, Fold] = {}
        for f in sorted(found, key=lambda f: (f.removed, rank[f.kind])):
            chosen.setdefault(f.removed, f)
        # A neighbour may take folds from several steps, as long as they
        # compose; the earlier step's fold keeps its place.
        taken: list[Fold] = []
        on: dict[int, list[Edit]] = {}
        for f in chosen.values():
            if any(j in chosen for j in f.neighbours):
                continue
            trial = {j: on.get(j, []) + [e] for j, e in zip(f.neighbours, f.edits)}
            try:
                for j, es in trial.items():
                    edited(traced.steps[j].op, es).tuned(dev)
            except (Unfoldable, Incompatible):
                continue
            on.update(trial)
            taken.append(f)
        return taken

    def fold(self, traced: TracedGraph, dev) -> TracedGraph:
        return apply(traced, self.choose(traced, dev), dev)
