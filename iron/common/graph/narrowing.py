# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Joint narrowing: each design's width (``Operator.widths``, narrower or
wider than its default) and which designs share a device, chosen together
to minimise the modelled runlist time:

    D0 + sum over steps of t_step
       + sum over device entries of (base + sum over its members of load)
       + R if the entries are odd

A device is entered at a step whose design is in it when the step before is
not; entering configures it. The designs of one array share a device
(``Packing.sharing``) that loads the array once, so the search takes them
as one, at one width. ``R`` is the empty configure the parity rule
adds (``Fusion.needs_reset``). ``t_step`` and ``load`` are measured per
design and width, ``D0``, ``base`` and ``R`` per device (``probe``, into a
``CostTable``).

Only a pack connected in the runlist's adjacency can save an entry, so the
candidates are the connected sets of designs, and an exact search over
partitions into them, carrying the parity, finds the cheapest. The placer
(``fits``) is asked only about the packs a solution uses; a refused pack
tries its next-cheapest widths, then is dropped, and the search reruns.

A width is a candidate only if its output was measured bit-identical to the
default width's. A design the table does not hold stays at its default
width, alone in its device.

A fold (``iron.common.graph.fold``) is another runlist: fewer steps, the
producer's design in place of two. Each the graph admits is priced by the
same search over its folded graph, and taken where the model's time drops,
the cheapest first; a fold changing a design the table does not hold is
not taken.
"""

from __future__ import annotations

import dataclasses
import datetime
import functools
import hashlib
import heapq
import itertools
import json
import os
import statistics
from collections import Counter
from collections.abc import Hashable, Iterable, Iterator, Mapping, Sequence
from pathlib import Path

from aie.dialects.aie import WireBundle, get_target_model
from aie.utils.compile import NPU_CACHE_HOME

from ..declare import Operator
from ..design import OperatorDesign
from ..image.coresidence import Packing, fits
from ..image.fusion import generate, parameters_preamble
from .fold import Fold, folded
from .trace import TracedGraph


def cost_key(op: Operator, dev=None) -> str:
    """A design's class and identity, resolved for ``dev``, as the fused
    image names it. The key leaves out the sources, so remeasure after
    editing how a design is generated.
    """
    design = OperatorDesign(op.resolved(dev))
    return f"{type(op).__name__}_{design.identity}"


@dataclasses.dataclass(frozen=True, eq=False)
class Variant:
    """One width of a design, its array and the shim channels its streams take."""

    op: Operator
    resolved: Operator
    widths: tuple[tuple[str, int], ...]
    key: str
    array: Hashable
    mm2s: int
    s2mm: int

    @classmethod
    def of(cls, op: Operator, dev) -> Variant:
        resolved = op.resolved(dev)
        streams = [b for b in resolved.buffers if b.streamed]
        widths: list[tuple[str, int]] = []
        for name, width in resolved.widths.items():
            assert width is not None, "a resolved operator sets its widths"
            widths.append((name, width))
        return cls(
            op=op,
            resolved=resolved,
            widths=tuple(widths),
            key=cost_key(resolved),
            array=resolved.array_key(),
            mm2s=sum(s.count for s in streams if not s.direction.drains),
            s2mm=sum(s.count for s in streams if s.direction.drains),
        )


def _widths(width: int, cols: int) -> list[int]:
    """``width`` and every power of two up to ``cols``, widest first."""
    out = {width}
    w = 1
    while w <= cols:
        out.add(w)
        w *= 2
    return sorted(out, reverse=True)


def variants(op: Operator, dev) -> list[Variant]:
    """``op`` at its default width, then at every other one it resolves at.
    Each width tunable ranges over its default and the powers of two up to
    the device's columns, widest first.
    """
    default = Variant.of(op, dev)
    defaults = dict(default.widths)
    out = [default]
    for combo in itertools.product(*(_widths(w, dev.cols) for w in defaults.values())):
        widths = dict(zip(defaults, combo))
        if widths == defaults:
            continue
        try:
            out.append(Variant.of(op.with_tunables(**widths), dev))
        except ValueError:  # unresolvable or incompatible at this width
            continue
    return out


def shim_budget(dev) -> tuple[int, int]:
    """The device's shim DMA channels: (MM2S, S2MM)."""
    tm = get_target_model(dev.resolve())
    shims = [
        (col, row)
        for col in range(tm.columns())
        for row in range(tm.rows())
        if tm.is_shim_noc_or_pl_tile(col, row)
    ]
    return (
        sum(
            tm.get_num_source_shim_mux_connections(c, r, WireBundle.DMA)
            for c, r in shims
        ),
        sum(
            tm.get_num_dest_shim_mux_connections(c, r, WireBundle.DMA) for c, r in shims
        ),
    )


@dataclasses.dataclass(frozen=True)
class StepCost:
    """One design at one width, measured alone.

    Attributes:
        t_step_us: Its time per step while its device is configured.
        alone_us: One run of one step, less `t_step_us`: `D0 + base + load + R`.
        exact: Its output is bit-identical to the default width's.
    """

    t_step_us: float
    alone_us: float
    exact: bool
    pmode: str
    rounds: int
    calls: int
    measured: str  # ISO date


@dataclasses.dataclass(frozen=True)
class Calibration:
    """A configure's cost split, measured on one pair of designs.

    Attributes:
        dispatch_us: `D0`.
        reset_us: `R`, the empty configure.
        base_us: The part of a configure no design accounts for.
        switch_us: The pair's mean configure.
    """

    dispatch_us: float
    reset_us: float
    base_us: float
    switch_us: float
    pmode: str
    rounds: int
    calls: int
    measured: str


class CostTable:
    """Measured step and configure costs for one device, as JSON on disk.

    ``steps`` is keyed by ``cost_key``, ``calibrations`` by the pair of keys
    measured; the model takes the median of each calibrated figure.
    """

    def __init__(self, path: Path | str):
        self.path = Path(path)
        self.steps: dict[str, StepCost] = {}
        self.calibrations: dict[str, Calibration] = {}
        self._medians: dict[str, float] | None = None
        if self.path.exists():
            data = json.loads(self.path.read_text())
            self.steps = {k: StepCost(**v) for k, v in data["steps"].items()}
            self.calibrations = {
                k: Calibration(**v) for k, v in data["calibrations"].items()
            }

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        sections = []
        for name, table in (("steps", self.steps), ("calibrations", self.calibrations)):
            rows = [
                f"{json.dumps(k)}: {json.dumps(dataclasses.asdict(v))}"
                for k, v in sorted(table.items())
            ]
            sections.append(f'"{name}": {{\n  ' + ",\n  ".join(rows) + "\n}")
        self.path.write_text("{" + ",\n".join(sections) + "}\n")

    def record_step(self, key: str, cost: StepCost) -> None:
        self.steps[key] = cost

    def record_calibration(self, pair: tuple[str, str], cal: Calibration) -> None:
        self.calibrations["|".join(pair)] = cal
        self._medians = None

    def _calibrated(self, figure: str) -> float:
        if self._medians is None:
            if not self.calibrations:
                raise ValueError(f"{self.path}: no configure calibration measured")
            rows = [dataclasses.asdict(c) for c in self.calibrations.values()]
            self._medians = {
                name: statistics.median(row[name] for row in rows)
                for name in ("dispatch_us", "reset_us", "base_us")
            }
        return self._medians[figure]

    @property
    def dispatch_us(self) -> float:
        return self._calibrated("dispatch_us")

    @property
    def reset_us(self) -> float:
        return self._calibrated("reset_us")

    @property
    def base_us(self) -> float:
        return self._calibrated("base_us")

    def t_step(self, key: str) -> float:
        cost = self.steps.get(key)
        return 0.0 if cost is None else cost.t_step_us

    def load(self, key: str) -> float:
        """What configuring a design adds to a configure; 0 if unmeasured."""
        cost = self.steps.get(key)
        if cost is None:
            return 0.0
        return cost.alone_us - self.dispatch_us - self.reset_us - self.base_us

    @staticmethod
    def today() -> str:
        return datetime.date.today().isoformat()


class Runlist:
    """The runlist as the cost model sees it: a design key per step."""

    def __init__(self, keys: Sequence[str]):
        self.keys = list(keys)
        self.order = list(dict.fromkeys(keys))
        self.index = {k: i for i, k in enumerate(self.order)}
        self.occurrences = Counter(keys)
        # Steps whose predecessor runs another design (the first step too).
        self._arrivals = [
            (i, k) for i, k in enumerate(keys) if i == 0 or keys[i - 1] != k
        ]
        self.pairs: Counter = Counter()
        for a, b in zip(keys, keys[1:]):
            if a != b:
                i, j = sorted((self.index[a], self.index[b]))
                self.pairs[i, j] += 1

    def entries(self, members: frozenset[str]) -> int:
        """How often a device holding ``members`` is entered."""
        return sum(
            1
            for i, k in self._arrivals
            if k in members and (i == 0 or self.keys[i - 1] not in members)
        )

    def neighbours(self) -> dict[int, set[int]]:
        out: dict[int, set[int]] = {i: set() for i in range(len(self.order))}
        for i, j in self.pairs:
            out[i].add(j)
            out[j].add(i)
        return out


def model_us(
    table: CostTable,
    keys: Sequence[str],
    groups: Sequence[Sequence[str]] = (),
    chosen: Mapping[str, str] | None = None,
    arrays: Mapping[str, Hashable] | None = None,
) -> tuple[float, int]:
    """The model's time for a runlist of design keys, and its configures.

    Args:
        table: The measured costs.
        keys: The runlist's design keys.
        groups: The designs sharing a device.
        chosen: Each design's key at the width it runs at.
        arrays: Each design's array at that width: the designs of one array
            share a device too, which loads the array once.

    Returns:
        `(time_us, configures)`, the reset included.
    """
    chosen = chosen or {}
    arrays = arrays or {}
    order = list(dict.fromkeys(keys))
    packing = Packing(tuple(map(tuple, groups))).sharing(
        {k: arrays.get(k, k) for k in order}
    )
    members = packing.devices(order)
    total = table.dispatch_us
    entries = 0
    previous = None
    for k in keys:
        total += table.t_step(chosen.get(k, k))
        here = packing.device_of(k)
        if here != previous:
            entries += 1
            loads: dict[Hashable, float] = {}
            for m in members[here]:
                loads.setdefault(arrays.get(m, m), table.load(chosen.get(m, m)))
            total += table.base_us + sum(loads.values())
            previous = here
    if entries % 2:
        total += table.reset_us
        entries += 1
    return total, entries


@dataclasses.dataclass
class Tuning:
    """What ``JointNarrowing`` chose, and the model's prediction for it and
    for the graph as traced (``baseline``). The predictions leave out the
    ``unmeasured`` designs, which stay as traced. ``chosen`` and ``groups``
    name the designs of the graph with ``folds`` applied.
    """

    chosen: dict[str, Variant]  # default key -> the width it runs at
    # Default keys sharing one device, an array's first design standing for
    # the array: the fusion adds its other designs.
    groups: tuple[tuple[str, ...], ...]
    configures: int
    predicted_us: float
    baseline_configures: int
    baseline_us: float
    unmeasured: tuple[str, ...]
    folds: tuple[Fold, ...] = ()

    def apply(
        self, traced: TracedGraph, dev=None
    ) -> tuple[TracedGraph, list[list[Operator]]]:
        """``traced`` with the chosen folds applied, every narrowed design's
        operators rebuilt at their width, and the packs as operator groups
        for ``coresident=``.
        """
        if self.folds:
            traced, _ = folded(traced, dev, self.folds)
        replace: dict[int, Operator] = {}
        keys: dict[int, str] = {}
        for step in traced.steps:
            op = step.op
            if id(op) in keys:
                continue
            keys[id(op)] = key = cost_key(op, dev)
            variant = self.chosen.get(key)
            if variant is not None and variant.key != key:
                replace[id(op)] = op.with_tunables(**dict(variant.widths))
        narrowed = traced.with_operators(replace)
        members: dict[str, list[Operator]] = {}
        for old, new in zip(traced.steps, narrowed.steps):
            ops = members.setdefault(keys[id(old.op)], [])
            if all(o is not new.op for o in ops):
                ops.append(new.op)
        groups = [[op for key in group for op in members[key]] for group in self.groups]
        return narrowed, groups

    def report(self, names: Mapping[str, str] | None = None) -> str:
        """One line per design that changed, then the predictions."""
        names = names or {}
        lines = [f"  fold: {fold}" for fold in self.folds]
        for key, v in self.chosen.items():
            if v.key != key:
                lines.append(f"  {names.get(key, key)}: {dict(v.widths)}")
        for group in self.groups:
            lines.append("  pack: " + ", ".join(names.get(k, k) for k in group))
        lines.append(
            f"  model: {self.baseline_us:.1f} us ({self.baseline_configures} "
            f"configures) -> {self.predicted_us:.1f} us ({self.configures})"
        )
        if self.unmeasured:
            lines.append(f"  unmeasured (left out): {len(self.unmeasured)} designs")
        return "\n".join(lines)


@dataclasses.dataclass
class _Pack:
    """A candidate device: a connected set of designs, its entries, and its
    cheapest widths within the shim budget; the search prices ``options[0]``.
    """

    members: tuple[int, ...]
    entries: int
    options: list[tuple[float, tuple[Variant, ...]]]

    @property
    def cost(self) -> float:
        return self.options[0][0]

    @property
    def combo(self) -> tuple[Variant, ...]:
        return self.options[0][1]

    @property
    def mask(self) -> int:
        return functools.reduce(lambda m, i: m | (1 << i), self.members, 0)


def _cheapest(
    ranked: Sequence[Sequence[tuple[float, Variant]]],
    budget: tuple[int, int],
    k: int,
) -> list[tuple[float, tuple[Variant, ...]]]:
    """The ``k`` cheapest picks of one variant per member within the shim
    ``budget``, cheapest first, by branch and bound.
    """
    n = len(ranked)
    rest_cost = [0.0] * (n + 1)
    rest_mm2s = [0] * (n + 1)
    rest_s2mm = [0] * (n + 1)
    for m in reversed(range(n)):
        rest_cost[m] = rest_cost[m + 1] + ranked[m][0][0]
        rest_mm2s[m] = rest_mm2s[m + 1] + min(v.mm2s for _, v in ranked[m])
        rest_s2mm[m] = rest_s2mm[m + 1] + min(v.s2mm for _, v in ranked[m])
    found: list[tuple[float, int, tuple[Variant, ...]]] = []  # max-heap by -cost
    counter = itertools.count()

    def dfs(m: int, cost: float, mm2s: int, s2mm: int, pick: tuple) -> None:
        if m == n:
            entry = (-cost, next(counter), pick)
            if len(found) < k:
                heapq.heappush(found, entry)
            else:
                heapq.heappushpop(found, entry)
            return
        for c, v in ranked[m]:
            total = cost + c
            if len(found) == k and total + rest_cost[m + 1] >= -found[0][0]:
                break
            a, b = mm2s + v.mm2s, s2mm + v.s2mm
            if a + rest_mm2s[m + 1] > budget[0] or b + rest_s2mm[m + 1] > budget[1]:
                continue
            dfs(m + 1, total, a, b, pick + (v,))

    dfs(0, 0.0, 0, 0, ())
    return [(-c, pick) for c, _, pick in sorted(found, reverse=True)]


@dataclasses.dataclass(frozen=True)
class JointNarrowing:
    """Choose widths and packs for a traced graph; pass as ``coresident=``
    to ``Graph.compile``.

    Attributes:
        table: The measured costs.
        max_members: The most designs in one pack.
        fit_attempts: How many of a pack's cheapest widths the placer is
            asked about before the pack is dropped.
        fit_cache: Where the placer's verdicts persist across processes.
    """

    table: CostTable = dataclasses.field(compare=False)
    max_members: int = 8
    fit_attempts: int = 3
    fit_cache: Path = dataclasses.field(
        default=Path(NPU_CACHE_HOME) / "iron" / "fits", compare=False
    )

    def tune(self, traced: TracedGraph, dev) -> Tuning:
        """Choose the folds, widths and packs of ``traced`` for ``dev``.

        Each fold the graph admits is priced on its own, then those that
        gain are taken cheapest first, each kept only if the model's time
        drops with it beside those already taken.
        """
        plain = self._narrow(traced, dev)
        keys = {cost_key(s.op, dev) for s in traced.steps}
        _, admitted = folded(traced, dev)
        gains = []
        for fold in admitted:
            trial = self._folding(traced, dev, (fold,), keys)
            if trial is not None and trial.predicted_us < plain.predicted_us:
                gains.append(trial)
        best = plain
        for single in sorted(gains, key=lambda t: t.predicted_us):
            trial = (
                single
                if not best.folds
                else self._folding(traced, dev, best.folds + single.folds, keys)
            )
            if trial is not None and trial.predicted_us < best.predicted_us:
                best = trial
        return dataclasses.replace(
            best,
            baseline_us=plain.baseline_us,
            baseline_configures=plain.baseline_configures,
        )

    def _folding(
        self,
        traced: TracedGraph,
        dev,
        folds: tuple[Fold, ...],
        keys: set[str],
    ) -> Tuning | None:
        """``traced`` tuned with ``folds`` applied, or None where a design
        the folds add or remove (beside ``keys``, the graph's) is unmeasured.
        """
        trial, _ = folded(traced, dev, folds)
        changed = keys ^ {cost_key(s.op, dev) for s in trial.steps}
        if any(k not in self.table.steps for k in changed):
            return None
        return dataclasses.replace(self._narrow(trial, dev), folds=folds)

    def _narrow(self, traced: TracedGraph, dev) -> Tuning:
        """The widths and packs of ``traced`` as it is."""
        table = self.table
        keys = [cost_key(s.op, dev) for s in traced.steps]
        first: dict[str, Operator] = {}
        for key, step in zip(keys, traced.steps):
            first.setdefault(key, step.op)
        found = {k: self._candidates(op, dev) for k, op in first.items()}
        # The designs of one array are one device, so they take one width:
        # the search runs over arrays, each named for its first design.
        units: dict[Hashable, list[str]] = {}
        for k, cands in found.items():
            units.setdefault(cands[0].array, []).append(k)
        unit = {k: designs[0] for designs in units.values() for k in designs}
        runlist = Runlist([unit[k] for k in keys])
        designs_of = [units[found[k][0].array] for k in runlist.order]
        at = {k: {v.widths: v for v in cands} for k, cands in found.items()}
        candidates = [
            [v for v in found[k] if all(v.widths in at[m] for m in designs)]
            for k, designs in zip(runlist.order, designs_of)
        ]
        measured = [all(m in table.steps for m in designs) for designs in designs_of]
        occurrences = Counter(keys)
        budget = shim_budget(dev)

        def member_cost(i: int, v: Variant, entries: int) -> float:
            return entries * table.load(v.key) + sum(
                occurrences[m] * table.t_step(at[m][v.widths].key)
                for m in designs_of[i]
            )

        # Alone, each design takes its cheapest width.
        alone: list[tuple[float, Variant, int]] = []
        for i, key in enumerate(runlist.order):
            e = runlist.entries(frozenset([key]))
            best = min(candidates[i], key=lambda v: member_cost(i, v, e))
            alone.append((e * table.base_us + member_cost(i, best, e), best, e))

        packs: list[_Pack] = []
        for members in self._connected(runlist, measured, candidates, budget):
            entries = runlist.entries(frozenset(runlist.order[i] for i in members))
            ranked = [
                sorted(
                    ((member_cost(i, v, entries), v) for v in candidates[i]),
                    key=lambda cv: cv[0],
                )
                for i in members
            ]
            options = [
                (entries * table.base_us + c, pick)
                for c, pick in _cheapest(ranked, budget, self.fit_attempts)
            ]
            if not options:
                continue
            pack = _Pack(members, entries, options)
            # The parity can move the total by one reset either way.
            if self._gain(pack, alone) + table.reset_us > 0:
                packs.append(pack)

        fitted: dict[tuple[str, ...], bool] = {}
        while True:
            chosen_packs = self._partition(runlist, alone, packs)
            refused = [p for p in chosen_packs if not self._fit(p.combo, fitted)]
            if not refused:
                break
            for p in refused:
                while p.options and not self._fit(p.combo, fitted):
                    p.options.pop(0)
                if not p.options or self._gain(p, alone) + table.reset_us <= 0:
                    packs.remove(p)

        picked = [best for _, best, _ in alone]
        for p in chosen_packs:
            for i, v in zip(p.members, p.combo):
                picked[i] = v
        chosen: dict[str, Variant] = {
            k: at[k][picked[runlist.index[unit[k]]].widths] for k in found
        }
        groups = tuple(
            tuple(runlist.order[i] for i in sorted(p.members)) for p in chosen_packs
        )
        predicted, configures = model_us(
            table,
            keys,
            groups,
            {k: v.key for k, v in chosen.items()},
            {k: v.array for k, v in chosen.items()},
        )
        baseline, baseline_configures = model_us(
            table, keys, arrays={k: cands[0].array for k, cands in found.items()}
        )
        return Tuning(
            chosen=chosen,
            groups=groups,
            configures=configures,
            predicted_us=predicted,
            baseline_configures=baseline_configures,
            baseline_us=baseline,
            unmeasured=tuple(k for k in found if k not in table.steps),
        )

    @staticmethod
    def _gain(pack: _Pack, alone: Sequence[tuple[float, Variant, int]]) -> float:
        """What ``pack`` saves over its members each alone, bar the parity."""
        return sum(alone[i][0] for i in pack.members) - pack.cost

    def _candidates(self, op: Operator, dev) -> list[Variant]:
        """The default width, then every other one measured exact."""
        found = variants(op, dev)
        default = found[0]
        if default.key not in self.table.steps:
            return [default]
        return [default] + [
            v
            for v in found[1:]
            if v.key in self.table.steps and self.table.steps[v.key].exact
        ]

    @staticmethod
    def _within(combo: Sequence[Variant], budget: tuple[int, int]) -> bool:
        return (
            sum(v.mm2s for v in combo) <= budget[0]
            and sum(v.s2mm for v in combo) <= budget[1]
        )

    def _connected(
        self,
        runlist: Runlist,
        measured: list[bool],
        candidates: list[list[Variant]],
        budget: tuple[int, int],
    ) -> Iterator[tuple[int, ...]]:
        """Every connected set of two or more measured designs, up to
        ``max_members``, whose narrowest widths are within the shim budget.
        """
        neighbours = runlist.neighbours()
        narrowest = [min(c, key=lambda v: (v.mm2s + v.s2mm, v.key)) for c in candidates]

        def grow(members: tuple[int, ...], frontier: set[int], banned: set[int]):
            if len(members) > 1:
                yield tuple(sorted(members))
            if len(members) == self.max_members:
                return
            frontier = set(frontier)
            banned = set(banned)
            while frontier:
                w = frontier.pop()
                banned.add(w)
                grown = members + (w,)
                if not self._within([narrowest[i] for i in grown], budget):
                    continue
                reach = {
                    u
                    for u in neighbours[w]
                    if u > min(members) and measured[u] and u not in banned
                } - set(grown)
                yield from grow(grown, frontier | reach, banned)

        for v in range(len(runlist.order)):
            if not measured[v]:
                continue
            start = {u for u in neighbours[v] if u > v and measured[u]}
            yield from grow((v,), start, {v})

    def _partition(
        self,
        runlist: Runlist,
        alone: list[tuple[float, Variant, int]],
        packs: list[_Pack],
    ) -> list[_Pack]:
        """The cheapest partition into ``packs`` and single designs."""
        n = len(runlist.order)
        reset = self.table.reset_us
        by_lowest: dict[int, list[_Pack]] = {}
        for p in packs:
            by_lowest.setdefault(min(p.members), []).append(p)
        full = (1 << n) - 1

        @functools.cache
        def best(mask: int, parity: int) -> tuple[float, tuple[int, ...]]:
            if mask == full:
                return (reset if parity else 0.0), ()
            i = (~mask & (mask + 1)).bit_length() - 1  # lowest unassigned
            cost, _, e = alone[i]
            rest, picks = best(mask | (1 << i), parity ^ (e & 1))
            answer = (cost + rest, picks)
            for p in by_lowest.get(i, ()):
                if p.mask & mask:
                    continue
                rest, picks = best(mask | p.mask, parity ^ (p.entries & 1))
                if p.cost + rest < answer[0]:
                    answer = (p.cost + rest, (id(p),) + picks)
            return answer

        _, picks = best(0, 0)
        by_id = {id(p): p for p in packs}
        return [by_id[k] for k in picks]

    def _fit(
        self, combo: Sequence[Variant], fitted: dict[tuple[str, ...], bool]
    ) -> bool:
        key = tuple(sorted(v.key for v in combo))
        if key not in fitted:
            designs = {v.key: OperatorDesign(v.resolved) for v in combo}
            record = self._fit_record(designs.values())
            if record.exists():
                verdict = record.read_text()
            else:
                texts, params = {}, {}
                for name, design in designs.items():
                    generated = generate(design)
                    texts[name] = str(generated.device)
                    params.update(generated.parameters)
                diagnostic = fits(texts, parameters_preamble(params))
                verdict = "fits" if diagnostic is None else f"refused: {diagnostic}"
                record.parent.mkdir(parents=True, exist_ok=True)
                partial = record.with_suffix(f".{os.getpid()}")
                partial.write_text(verdict)
                partial.replace(record)
            fitted[key] = verdict == "fits"
        return fitted[key]

    def _fit_record(self, designs: Iterable[OperatorDesign]) -> Path:
        """The file holding the placer's verdict on ``designs``, keyed on
        their recipes so a verdict is reused exactly when the build would be.
        """
        h = hashlib.sha256(
            repr(sorted(d.compilable().recipe_hash for d in designs)).encode()
        )
        return self.fit_cache / h.hexdigest()[:24]
