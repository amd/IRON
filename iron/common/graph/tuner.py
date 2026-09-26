# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Choosing a graph's folds and its packaging together, from measured costs.

Three things change what a runlist costs, and each changes what the others
are worth:

- **folds** (:mod:`.fold`): a movement step done by a neighbour is a step
  fewer, and a boundary fewer;
- **packaging** (:mod:`iron.common.image.packaging`): one fused dispatch,
  where a boundary is a configure, or a dispatch per step, where every step
  is a round trip. A fold is worth more where boundaries cost more, so the
  fold choice is made per mode;
- **widths and packs** (:class:`.narrowing.JointNarrowing`), under the one
  mode that packs.

:class:`Tuner` evaluates, for every mode the device allows and the table
calibrates, a greedy choice of folds: movements that fold the same way into
the same designs (one per layer of a model) are one decision, taken if it
lowers the modelled time. The cheapest mode wins.

A folded design is a new design the table has not measured. What it runs is
its unfolded twin's array with other addresses in its descriptors, so it is
priced at the twin's measured costs, and the choice lists it as estimated;
measuring it replaces the estimate.
"""

from __future__ import annotations

import dataclasses
from collections.abc import Sequence

from ..declare import Operator
from ..image.packaging import FUSED, Mode
from .fold import Fold, apply, candidates
from .narrowing import (
    CostTable,
    JointNarrowing,
    StepCost,
    Tuning,
    cost_key,
    model_us,
    variants,
    with_widths,
)
from .trace import TracedGraph


@dataclasses.dataclass
class Choice:
    """What :class:`Tuner` chose for a graph: the mode, the folds (on the
    graph as traced), the widths and packs under a mode that packs, and
    what the model predicts. ``estimated`` are the folded designs priced at
    their unfolded twins; ``considered`` is every evaluation, for the
    report."""

    mode: Mode
    folds: tuple[Fold, ...]
    tuning: Tuning | None
    predicted_us: float
    boundaries: int
    estimated: tuple[str, ...]
    considered: list[tuple[str, str, float, int]]

    def report(self, traced: TracedGraph) -> str:
        lines = [
            f"  mode {self.mode.name}: {self.predicted_us:.1f} us, "
            f"{self.boundaries} boundaries, {len(self.folds)} folds"
        ]
        kinds: dict[str, int] = {}
        for f in self.folds:
            label = _kind_label(traced, f)
            kinds[label] = kinds.get(label, 0) + 1
        lines += [f"  fold x{n}: {label}" for label, n in kinds.items()]
        if self.estimated:
            lines.append(
                f"  estimated (priced at the unfolded twin): {len(self.estimated)} designs"
            )
        for mode, folds, us, n in self.considered:
            lines.append(f"    considered {mode} [{folds}]: {us:.1f} us ({n})")
        if self.tuning is not None:
            lines.append(self.tuning.report())
        return "\n".join(lines)


def _kind(traced: TracedGraph, f: Fold) -> tuple:
    """What makes two folds one decision: the movement's design, the side,
    and the designs it folds into."""
    return (
        cost_key(traced.steps[f.movement].op),
        f.side,
        tuple(cost_key(traced.steps[j].op) for j in f.neighbours),
    )


def _kind_label(traced: TracedGraph, f: Fold) -> str:
    what = type(traced.steps[f.movement].op).__name__
    into = ",".join(type(traced.steps[j].op).__name__ for j in f.neighbours)
    return f"{what} {f.side.value} into {into}"


@dataclasses.dataclass(frozen=True)
class Tuner:
    """Choose folds and packaging, and under a fused mode widths and packs,
    for a traced graph from a :class:`~.narrowing.CostTable`.

    Pass as ``tuner=`` to :meth:`GraphFunction.compile`. ``modes`` limits
    the packagings considered (an application whose versions share states
    needs the fused one); ``fold=False`` takes none.
    """

    table: CostTable = dataclasses.field(compare=False)
    fold: bool = True
    modes: tuple[Mode, ...] | None = None
    max_members: int = 8
    fit_attempts: int = 3

    def tune(self, traced: TracedGraph, dev, allowed: Sequence[Mode]) -> Choice:
        modes = [
            m
            for m in allowed
            if (self.modes is None or m in self.modes) and self.table.calibrated(m)
        ]
        if not modes:
            names = ", ".join(m.name for m in allowed)
            raise ValueError(
                f"{traced.name}: none of the packagings this device allows ({names}) "
                f"is calibrated in {self.table.path}"
            )
        legal = (
            [c for c in candidates(traced, dev) if isinstance(c, Fold)]
            if self.fold
            else []
        )
        kinds: dict[tuple, list[Fold]] = {}
        for f in legal:
            kinds.setdefault(_kind(traced, f), []).append(f)
        # Per movement kind, its sides: one decision covers every layer.
        decisions: dict[tuple, dict] = {}
        for (movement, side, into), folds in kinds.items():
            decisions.setdefault((movement, into), {})[side] = folds
        narrowing = JointNarrowing(self.table, self.max_members, self.fit_attempts)
        considered: list[tuple[str, str, float, int]] = []
        best: Choice | None = None
        for mode in modes:
            taken: dict[tuple, list[Fold]] = {}
            current = self._evaluate(traced, dev, mode, [], narrowing)
            considered.append((mode.name, "", current.predicted_us, current.boundaries))
            for key, sides in decisions.items():
                for side, folds in sides.items():
                    trial = {**taken, key: folds}
                    chosen = [f for fs in trial.values() for f in fs]
                    try:
                        result = self._evaluate(traced, dev, mode, chosen, narrowing)
                    except ValueError as e:  # two folds that cannot share a step
                        considered.append((mode.name, f"refused: {e}", 0.0, 0))
                        continue
                    label = ", ".join(
                        _kind_label(traced, fs[0]) for fs in trial.values()
                    )
                    considered.append(
                        (mode.name, label, result.predicted_us, result.boundaries)
                    )
                    if result.predicted_us < current.predicted_us:
                        current, taken = result, trial
            if best is None or current.predicted_us < best.predicted_us:
                best = current
        best.considered = considered
        return best

    def _evaluate(
        self,
        traced: TracedGraph,
        dev,
        mode: Mode,
        folds: list[Fold],
        narrowing: JointNarrowing,
    ) -> Choice:
        folded = apply(traced, folds, dev) if folds else traced
        table, estimated = self._priced(folded, dev)
        if mode.packs:
            tuning = dataclasses.replace(narrowing, table=table).tune(folded, dev)
            return Choice(
                mode,
                tuple(folds),
                tuning,
                tuning.predicted_us,
                tuning.configures,
                estimated,
                [],
            )
        keys = [cost_key(s.op) for s in folded.steps]
        predicted, dispatches = model_us(table, keys, mode=mode)
        return Choice(mode, tuple(folds), None, predicted, dispatches, estimated, [])

    def _priced(self, traced: TracedGraph, dev) -> tuple[CostTable, tuple[str, ...]]:
        """The table with every folded design's widths priced at its twin's."""
        extra: dict[str, StepCost] = {}
        seen: set[str] = set()
        for step in traced.steps:
            op = step.op
            if not (op.refolds or op.reorder is not None):
                continue
            key = cost_key(op)
            if key in seen or key in self.table.steps:
                continue
            seen.add(key)
            twin = _twin(op)
            for v in variants(op, dev):
                twin_key = cost_key(with_widths(twin, dict(v.widths)))
                if twin_key in self.table.steps:
                    extra[v.key] = self.table.steps[twin_key]
        return self.table.with_steps(extra), tuple(sorted(extra))


def _twin(op: Operator) -> Operator:
    """``op`` without its folds: the array it runs, with its own addresses."""
    twin = dataclasses.replace(op)
    for name in op.used_values:
        twin.use_value(name)
    return twin
