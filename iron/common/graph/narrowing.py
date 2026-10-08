# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Joint narrowing: each design's width and which designs share a device,
chosen together from measured costs.

A design at its default width takes as much of the device as its resolution
gives it -- an elementwise array every shim column -- and two such designs
cannot share one configuration (``image.coresidence``). Narrowing one
leaves room for another; widening one past a default its resolution keeps
narrow can shorten its step. Either changes what configuring it costs. ``JointNarrowing`` picks, for a traced graph,
each design's width among those its operator declares
(``Operator.widths``) and a partition of the designs into devices, to
minimise the modelled time of the runlist:

    D0 + sum over steps of t_step
       + sum over device entries of (base + sum over its members of load)
       + R if the entries are odd

A device is *entered* at a step whose design is in it when the step before
is not; entering configures it. ``R`` is the empty configure the parity
rule adds (``Fusion.needs_reset``). ``t_step`` and
``load`` are measured per design and width, ``D0``, ``base`` and ``R`` per
device (``probe``, into a ``CostTable``).

The model decomposes over devices, bar the parity: a device's cost is its
entries times its configure plus its members' steps. Only a pack that is
connected in the runlist's adjacency can save an entry, so the candidates
are the connected sets of designs; an exact search over partitions into
them, carrying the parity, finds the cheapest. Whether a pack's widths fit
is for the placer (``fits``), asked only for the packs a solution uses:
a pack that does not fit tries its next-cheapest widths, then is dropped,
and the search reruns. What the search chose is recorded, keyed on the
runlist, the table and the device, and a later tuning of the same runlist
takes it while its packs still fit.

Nothing here names an operator. Candidates come from the width tunables,
legality from the operator's own resolution, the shim prefilter from the
declared streams, the fit from the placer, and the costs from measurement.
A width is a candidate only if its output was measured bit-identical to the
default width's, so tuning never trades accuracy. A design the table does
not hold stays at its default width, alone in its device.
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
from collections.abc import Iterable, Iterator, Mapping, Sequence
from pathlib import Path

from aie.dialects.aie import WireBundle, get_target_model
from aie.utils.compile import NPU_CACHE_HOME

from ..declare import Operator
from ..design import OperatorDesign
from ..image.coresidence import fits
from ..image.fusion import generate, parameters_preamble
from .trace import TracedGraph


def cost_key(op: Operator, dev=None) -> str:
    """What the cost table keys a design by: its class and its identity
    (every compared field, resolved for ``dev``, the bound device unless
    given), as the fused image names it. Sources aside: a table outlives
    an edit to how a design is generated, so remeasure after one.
    """
    design = OperatorDesign(op.resolved(dev))
    return f"{type(op).__name__}_{design.identity}"


# -- candidates ------------------------------------------------------------


@dataclasses.dataclass(frozen=True, eq=False)
class Variant:
    """One width of a design: the operator as a graph holds it (unresolved)
    and resolved, its width tunables, its cost key, and the shim channels
    its streams take.
    """

    op: Operator
    resolved: Operator
    widths: tuple[tuple[str, int], ...]
    key: str
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
    the device's columns, widest first; widths that resolve to one design
    give it once.
    """
    default = Variant.of(op, dev)
    defaults = dict(default.widths)
    out = [default]
    for combo in itertools.product(*(_widths(w, dev.cols) for w in defaults.values())):
        widths = dict(zip(defaults, combo))
        if widths == defaults:
            continue
        try:
            variant = Variant.of(op.with_tunables(**widths), dev)
        except ValueError:  # unresolvable or incompatible at this width
            continue
        if all(v.key != variant.key for v in out):
            out.append(variant)
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


# -- the measured costs ----------------------------------------------------


@dataclasses.dataclass(frozen=True)
class StepCost:
    """One design at one width, measured alone: its time per step while its
    device is configured; one run of one step less that (``D0 + base + load
    + R``); and whether its output is bit-identical to the default width's
    on the same inputs.
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
    """A configure's cost split, measured on one pair of designs: the
    dispatch ``D0``, the empty reset configure ``R``, the part of a
    configure no design accounts for (``base``), and the pair's mean
    configure (``switch``).
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

    ``steps`` is keyed by ``cost_key``, ``calibrations`` by the pair of
    keys they were measured on; the model uses the median of each
    calibrated figure. The key covers a design's fields, not the code that
    generates it or the kernels it links, so a table outlives a change to
    either: remeasure after one.
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

    def digest(self) -> str:
        """The table's entries, hashed: what a tuning from it is keyed on."""
        entries = {
            name: {k: dataclasses.asdict(v) for k, v in table.items()}
            for name, table in (
                ("steps", self.steps),
                ("calibrations", self.calibrations),
            )
        }
        return hashlib.sha256(json.dumps(entries, sort_keys=True).encode()).hexdigest()

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
        """A measured design's step time; zero for one not measured."""
        cost = self.steps.get(key)
        return 0.0 if cost is None else cost.t_step_us

    def load(self, key: str) -> float:
        """What configuring a measured design adds to a configure; zero for
        one not measured.
        """
        cost = self.steps.get(key)
        if cost is None:
            return 0.0
        return cost.alone_us - self.dispatch_us - self.reset_us - self.base_us

    @staticmethod
    def today() -> str:
        return datetime.date.today().isoformat()


# -- the model -------------------------------------------------------------


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
) -> tuple[float, int]:
    """The model's time for a runlist of design keys, and its configures
    (the reset included): ``chosen`` maps a design to the key of the width
    it runs at, ``groups`` lists the designs sharing a device.
    """
    chosen = chosen or {}
    device = {k: i for i, group in enumerate(groups) for k in group}
    members: dict[object, list[str]] = {}
    for k in dict.fromkeys(keys):
        members.setdefault(device.get(k, k), []).append(k)
    total = table.dispatch_us
    entries = 0
    previous = None
    for k in keys:
        width = chosen.get(k, k)
        total += table.t_step(width)
        here = device.get(k, k)
        if here != previous:
            entries += 1
            total += table.base_us + sum(
                table.load(chosen.get(m, m)) for m in members[here]
            )
            previous = here
    if entries % 2:
        total += table.reset_us
        entries += 1
    return total, entries


# -- the tuner -------------------------------------------------------------


@dataclasses.dataclass
class Tuning:
    """What ``JointNarrowing`` chose for a graph, and what the model
    predicts for it and for the graph as traced (``baseline``: default
    widths, a device per design). ``unmeasured`` are the designs the table
    did not hold: they stay as traced, and the predictions leave out their
    steps and loads.
    """

    chosen: dict[str, Variant]  # default key -> the width it runs at
    groups: tuple[tuple[str, ...], ...]  # default keys sharing one device
    configures: int
    predicted_us: float
    baseline_configures: int
    baseline_us: float
    unmeasured: tuple[str, ...]

    def apply(
        self, traced: TracedGraph, dev=None
    ) -> tuple[TracedGraph, list[list[Operator]]]:
        """``traced`` with every narrowed design's operators rebuilt at their
        width, and the packs as operator groups for ``coresident=``.
        """
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
        """What was chosen, one line per design that changed, and the
        predictions. ``names`` labels a key (its class, say).
        """
        names = names or {}
        lines = []
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
    """A candidate device: a connected set of designs (indices into the
    runlist's order), how often it is entered, and its cheapest widths
    within the shim budget, cheapest first; ``options[0]`` is the one the
    search prices it at, and the placer's refusals drop options.
    """

    members: tuple[int, ...]
    entries: int
    options: list[tuple[float, tuple[Variant, ...]]]
    mask: int = dataclasses.field(init=False)

    def __post_init__(self):
        # Read once per search state: hundreds of millions of times.
        self.mask = sum(1 << i for i in self.members)

    @property
    def cost(self) -> float:
        return self.options[0][0]

    @property
    def combo(self) -> tuple[Variant, ...]:
        return self.options[0][1]


def _cheapest(
    ranked: Sequence[Sequence[tuple[float, Variant]]],
    budget: tuple[int, int],
    k: int,
) -> list[tuple[float, tuple[Variant, ...]]]:
    """The ``k`` cheapest picks of one ``(cost, variant)`` per member, each
    member's ranked cheapest first, whose shim channels are within
    ``budget``; cheapest first. Branch and bound: a partial pick is dropped
    once its cost plus the cheapest rest cannot beat the k-th found, or its
    channels plus the fewest the rest can take overrun the budget.
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
    """Choose widths and packs for a traced graph from a ``CostTable``.

    Pass as ``coresident=`` to ``Graph.compile``. ``max_members`` caps a
    pack; ``fit_attempts`` is how many of a pack's cheapest widths within
    the shim budget are put to the placer before it is given up.
    ``cache`` is where the placer's verdicts (``fits/``) and the tunings
    (``tunings/``) are kept across processes.
    """

    table: CostTable = dataclasses.field(compare=False)
    max_members: int = 8
    fit_attempts: int = 3
    cache: Path = dataclasses.field(
        default=Path(NPU_CACHE_HOME) / "iron", compare=False
    )

    def tune(self, traced: TracedGraph, dev) -> Tuning:
        table = self.table
        keys = [cost_key(s.op, dev) for s in traced.steps]
        runlist = Runlist(keys)
        first: dict[str, Operator] = {}
        for key, step in zip(keys, traced.steps):
            first.setdefault(key, step.op)
        fitted: dict[tuple[str, ...], bool] = {}
        record = self._tuning_record(keys, dev)
        recorded = self._recorded(record, runlist, first, dev, fitted)
        if recorded is None:
            chosen, groups = self._search(runlist, first, dev, fitted)
            narrowed = {
                k: {"widths": dict(v.widths), "key": v.key}
                for k, v in chosen.items()
                if v.key != k
            }
            self._publish(
                record,
                json.dumps({"chosen": narrowed, "groups": groups}, sort_keys=True),
            )
        else:
            chosen, groups = recorded
        predicted, configures = model_us(
            table, keys, groups, {k: v.key for k, v in chosen.items()}
        )
        baseline, baseline_configures = model_us(table, keys)
        return Tuning(
            chosen=chosen,
            groups=groups,
            configures=configures,
            predicted_us=predicted,
            baseline_configures=baseline_configures,
            baseline_us=baseline,
            unmeasured=tuple(k for k in runlist.order if k not in table.steps),
        )

    def _recorded(
        self,
        record: Path,
        runlist: Runlist,
        first: Mapping[str, Operator],
        dev,
        fitted: dict[tuple[str, ...], bool],
    ) -> tuple[dict[str, Variant], tuple[tuple[str, ...], ...]] | None:
        """The tuning ``record`` holds, rebuilt, if every design still
        resolves to the key recorded for it and every pack still fits;
        ``None`` otherwise.
        """
        if not record.exists():
            return None
        data = json.loads(record.read_text())
        chosen: dict[str, Variant] = {}
        for k in runlist.order:
            narrowed = data["chosen"].get(k)
            if narrowed is None:
                chosen[k] = Variant.of(first[k], dev)
                continue
            try:
                chosen[k] = Variant.of(
                    first[k].with_tunables(**narrowed["widths"]), dev
                )
            except ValueError:
                return None
            if chosen[k].key != narrowed["key"]:
                return None
        groups = tuple(tuple(group) for group in data["groups"])
        for group in groups:
            if not self._fit([chosen[k] for k in group], fitted):
                return None
        return chosen, groups

    def _search(
        self,
        runlist: Runlist,
        first: Mapping[str, Operator],
        dev,
        fitted: dict[tuple[str, ...], bool],
    ) -> tuple[dict[str, Variant], tuple[tuple[str, ...], ...]]:
        """Each design's width and the packs, from the table and the placer."""
        table = self.table
        candidates = [self._candidates(first[k], dev) for k in runlist.order]
        measured = [k in table.steps for k in runlist.order]
        budget = shim_budget(dev)

        def member_cost(i: int, v: Variant, entries: int) -> float:
            return entries * table.load(v.key) + runlist.occurrences[
                runlist.order[i]
            ] * table.t_step(v.key)

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

        chosen: dict[str, Variant] = {
            k: alone[i][1] for i, k in enumerate(runlist.order)
        }
        for p in chosen_packs:
            for i, v in zip(p.members, p.combo):
                chosen[runlist.order[i]] = v
        groups = tuple(
            tuple(runlist.order[i] for i in sorted(p.members)) for p in chosen_packs
        )
        return chosen, groups

    @staticmethod
    def _gain(pack: _Pack, alone: Sequence[tuple[float, Variant, int]]) -> float:
        """What ``pack`` saves over its members each alone, bar the parity."""
        return sum(alone[i][0] for i in pack.members) - pack.cost

    def _candidates(self, op: Operator, dev) -> list[Variant]:
        """The widths the table allows: the default, first, and every
        other one measured exact.
        """
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
        ``max_members``, whose narrowest widths are within the shim budget
        (a set that is not has no superset that is).
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
        """The cheapest partition into ``packs`` and single designs, exact,
        with the reset charged when the entries are odd.
        """
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
                self._publish(record, verdict)
            fitted[key] = verdict == "fits"
        return fitted[key]

    @staticmethod
    def _publish(record: Path, text: str) -> None:
        """Write ``record`` whole or not at all: processes tune at once."""
        record.parent.mkdir(parents=True, exist_ok=True)
        partial = record.with_suffix(f".{os.getpid()}")
        partial.write_text(text)
        partial.replace(record)

    def _tuning_record(self, keys: Sequence[str], dev) -> Path:
        """The file holding what the search chose for the runlist ``keys``.

        Keyed on everything the search reads bar the placer, whose verdicts
        a recorded tuning is checked against when taken: the runlist, the
        table's entries, the device and the search's own fields. The search
        takes seconds to minutes on a graph of hundreds of designs.
        """
        h = hashlib.sha256(
            json.dumps(
                [
                    list(keys),
                    self.table.digest(),
                    repr(dev),
                    self.max_members,
                    self.fit_attempts,
                ]
            ).encode()
        )
        return self.cache / "tunings" / h.hexdigest()[:24]

    def _fit_record(self, designs: Iterable[OperatorDesign]) -> Path:
        """The file holding the placer's verdict on a pack of ``designs``:
        ``fits``, or ``refused:`` and the diagnostic.

        Keyed as a design's build is, on each design's recipe
        (``CompilableDesign.recipe_hash``), so a verdict is reused exactly
        when the build it predicts would be. Generating and placing a pack
        costs about 50 ms, and every process that tunes would otherwise ask
        again.
        """
        h = hashlib.sha256(
            repr(sorted(d.compilable().recipe_hash for d in designs)).encode()
        )
        return self.cache / "fits" / h.hexdigest()[:24]
