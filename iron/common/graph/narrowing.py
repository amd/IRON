# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Joint narrowing: each design's width and which designs share a device,
chosen together from measured costs.

A design at its default width takes as much of the device as its overlay's
tuning gives it -- an elementwise array every shim column -- and two such
designs cannot share one configuration (:mod:`..image.coresidence`).
Narrowing one leaves room for another; it also changes its own step time
and what configuring it costs. :class:`JointNarrowing` picks, for a traced
graph, each design's width among those its overlay declares
(:attr:`Overlay.widths`) and a partition of the designs into devices, to
minimise the modelled time of the runlist:

    D0 + sum over steps of t_step
       + sum over device entries of (base + sum over its members of load)
       + R if the entries are odd

A device is *entered* at a step whose design is in it when the step before
is not; entering configures it. ``R`` is the empty configure the parity
rule adds (:func:`..image.fusion.needs_additional_reset`). ``t_step`` and
``load`` are measured per design and width, ``D0``, ``base`` and ``R`` per
device (:mod:`.probe`, into a :class:`CostTable`).

The model decomposes over devices, bar the parity: a device's cost is its
entries times its configure plus its members' steps. Only a pack that is
connected in the runlist's adjacency can save an entry, so the candidates
are the connected sets of designs; an exact search over partitions into
them, carrying the parity, finds the cheapest. Whether a pack's widths fit
is for the placer (:func:`fits`), asked only for the packs a solution uses:
a pack that does not fit tries its next-cheapest widths, then is dropped,
and the search reruns.

Nothing here names an operator. Candidates come from the width tunables,
legality from the overlay's own tuning, the shim prefilter from the
declared streams, the fit from the placer, and the costs from measurement.
A width is a candidate only if its output was measured bit-identical to the
default width's, so tuning never trades accuracy. A design the table does
not hold stays at its default width, alone in its device.
"""

from __future__ import annotations

import dataclasses
import datetime
import functools
import heapq
import itertools
import json
import statistics
from collections import Counter
from collections.abc import Iterator, Mapping, Sequence
from pathlib import Path

from aie.dialects.aie import WireBundle, get_target_model

from ..declare import Operator
from ..image.coresidence import fits
from ..image.fusion import format_params, generate_design
from ..image.jit_compile import design_identity
from .trace import TracedGraph


def cost_key(op: Operator) -> str:
    """What the cost table keys a design by: its class and its full identity
    (design code, parameters, device), as the fused image names it."""
    return f"{type(op).__name__}_{design_identity(op.generator())}"


# -- candidates ------------------------------------------------------------


@dataclasses.dataclass(frozen=True, eq=False)
class Variant:
    """One width of a design: the operator as a graph holds it (untuned),
    its width tunables, and the shim channels its streams take."""

    op: Operator
    widths: tuple[tuple[str, int], ...]
    key: str
    mm2s: int
    s2mm: int


def _narrower(width: int) -> list[int]:
    """``width`` and every power of two below it, widest first."""
    out = {width}
    w = 1
    while w < width:
        out.add(w)
        w *= 2
    return sorted(out, reverse=True)


def _width_values(ov) -> dict[str, int]:
    fields = dataclasses.asdict(ov)
    return {name: fields[name] for name in ov.widths}


def _variant(op: Operator, tuned: Operator) -> Variant:
    streams = tuned.ov.streams.values()
    return Variant(
        op=op,
        widths=tuple(_width_values(tuned.ov).items()),
        key=cost_key(op),
        mm2s=sum(s.count for s in streams if s.direction == "in"),
        s2mm=sum(s.count for s in streams if s.direction == "out"),
    )


def with_widths(op: Operator, widths: Mapping[str, int]) -> Operator:
    """``op`` on a copy of its overlay with ``widths`` set, still untuned,
    carrying the per-call values a graph bound on it."""
    new = dataclasses.replace(op, ov=dataclasses.replace(op.ov, **widths))
    for name in op.used_values:
        new.use_value(name)
    return new


def variants(op: Operator, dev) -> list[Variant]:
    """``op`` at its default width, then at every narrower one its overlay
    tunes to. Each width tunable ranges over powers of two up to its default."""
    default = op.tuned(dev)
    defaults = _width_values(default.ov)
    out = [_variant(op, default)]
    for combo in itertools.product(*(_narrower(w) for w in defaults.values())):
        widths = dict(zip(defaults, combo))
        if widths == defaults:
            continue
        candidate = with_widths(op, widths)
        try:
            tuned = candidate.tuned(dev)
        except ValueError:  # Untunable or Incompatible at this width
            continue
        out.append(_variant(candidate, tuned))
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
    on the same inputs."""

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
    configure (``switch``)."""

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

    ``steps`` is keyed by :func:`cost_key`, ``calibrations`` by the pair of
    keys they were measured on; the model uses the median of each
    calibrated figure. The identity in a key covers a design's code and
    parameters, not the kernels it links, so a table outlives a kernel
    change: remeasure after one.
    """

    def __init__(self, path: Path | str):
        self.path = Path(path)
        self.steps: dict[str, StepCost] = {}
        self.calibrations: dict[str, Calibration] = {}
        if self.path.exists():
            data = json.loads(self.path.read_text())
            self.steps = {k: StepCost(**v) for k, v in data["steps"].items()}
            self.calibrations = {
                k: Calibration(**v) for k, v in data["calibrations"].items()
            }

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "steps": {k: dataclasses.asdict(v) for k, v in sorted(self.steps.items())},
            "calibrations": {
                k: dataclasses.asdict(v) for k, v in sorted(self.calibrations.items())
            },
        }
        self.path.write_text(json.dumps(data, indent=1) + "\n")

    def record_step(self, key: str, cost: StepCost) -> None:
        self.steps[key] = cost

    def record_calibration(self, pair: tuple[str, str], cal: Calibration) -> None:
        self.calibrations["|".join(pair)] = cal

    def _calibrated(self, figure: str) -> float:
        if not self.calibrations:
            raise ValueError(f"{self.path}: no configure calibration measured")
        return statistics.median(
            dataclasses.asdict(c)[figure] for c in self.calibrations.values()
        )

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
        one not measured."""
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
    it runs at, ``groups`` lists the designs sharing a device."""
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
    """What :class:`JointNarrowing` chose for a graph, and what the model
    predicts for it and for the graph as traced (``baseline``: default
    widths, a device per design). ``unmeasured`` are the designs the table
    did not hold: they stay as traced, and the predictions leave out their
    steps and loads."""

    chosen: dict[str, Variant]  # default key -> the width it runs at
    groups: tuple[tuple[str, ...], ...]  # default keys sharing one device
    configures: int
    predicted_us: float
    baseline_configures: int
    baseline_us: float
    unmeasured: tuple[str, ...]

    def apply(self, traced: TracedGraph) -> tuple[TracedGraph, list[list[Operator]]]:
        """``traced`` with every narrowed design's operators rebuilt at their
        width, and the packs as operator groups for ``coresident=``."""
        replace: dict[int, Operator] = {}
        keys = {}
        for step in traced.steps:
            op = step.op
            if id(op) in keys:
                continue
            keys[id(op)] = key = cost_key(op)
            variant = self.chosen.get(key)
            if variant is not None and variant.key != key:
                replace[id(op)] = with_widths(op, dict(variant.widths))
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
        predictions. ``names`` labels a key (its class, say)."""
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
    runlist's order), how often it is entered, and its widths, cheapest
    first, as the placer has not yet refused them."""

    members: tuple[int, ...]
    entries: int
    combos: Iterator[tuple[float, tuple[Variant, ...]]]
    cost: float = 0.0
    combo: tuple[Variant, ...] = ()
    tried: int = 0

    @property
    def mask(self) -> int:
        return functools.reduce(lambda m, i: m | (1 << i), self.members, 0)

    def advance(self) -> bool:
        """Move to the next-cheapest widths; ``False`` when none are left."""
        found = next(self.combos, None)
        if found is None:
            return False
        self.cost, self.combo = found
        self.tried += 1
        return True


@dataclasses.dataclass(frozen=True)
class JointNarrowing:
    """Choose widths and packs for a traced graph from a :class:`CostTable`.

    Pass as ``coresident=`` to :meth:`GraphFunction.compile`. ``max_members``
    caps a pack; ``fit_attempts`` is how many of a pack's cheapest widths
    within the shim budget are put to the placer before it is given up.
    """

    table: CostTable = dataclasses.field(compare=False)
    max_members: int = 8
    fit_attempts: int = 3

    def tune(self, traced: TracedGraph, dev) -> Tuning:
        table = self.table
        keys = [cost_key(s.op) for s in traced.steps]
        runlist = Runlist(keys)
        first: dict[str, Operator] = {}
        for key, step in zip(keys, traced.steps):
            first.setdefault(key, step.op)
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

        def combos(members: tuple[int, ...], entries: int):
            """Each member's widths, cheapest assignments first, within the
            shim budget."""
            ranked = [
                sorted(candidates[i], key=lambda v, i=i: member_cost(i, v, entries))
                for i in members
            ]
            fixed = entries * table.base_us

            def cost(idx):
                return fixed + sum(
                    member_cost(i, ranked[n][j], entries)
                    for n, (i, j) in enumerate(zip(members, idx))
                )

            start = (0,) * len(members)
            heap = [(cost(start), start)]
            seen = {start}
            while heap:
                c, idx = heapq.heappop(heap)
                combo = tuple(ranked[n][j] for n, j in enumerate(idx))
                if self._within(combo, budget):
                    yield c, combo
                for n in range(len(idx)):
                    if idx[n] + 1 < len(ranked[n]):
                        nxt = idx[:n] + (idx[n] + 1,) + idx[n + 1 :]
                        if nxt not in seen:
                            seen.add(nxt)
                            heapq.heappush(heap, (cost(nxt), nxt))

        packs: list[_Pack] = []
        for members in self._connected(runlist, measured, candidates, budget):
            entries = runlist.entries(frozenset(runlist.order[i] for i in members))
            pack = _Pack(members, entries, combos(members, entries))
            if not pack.advance():
                continue
            gain = sum(alone[i][0] for i in members) - pack.cost
            # The parity can move the total by one reset either way.
            if gain + table.reset_us > 0:
                packs.append(pack)

        fitted: dict[tuple[str, ...], bool] = {}
        while True:
            chosen_packs = self._partition(runlist, alone, packs)
            refused = [p for p in chosen_packs if not self._fit(p.combo, fitted)]
            if not refused:
                break
            for p in refused:
                while True:
                    if p.tried >= self.fit_attempts or not p.advance():
                        packs.remove(p)
                        break
                    gain = sum(alone[i][0] for i in p.members) - p.cost
                    if gain + table.reset_us <= 0:
                        packs.remove(p)
                        break
                    if self._fit(p.combo, fitted):
                        break

        chosen: dict[str, Variant] = {
            k: alone[i][1] for i, k in enumerate(runlist.order)
        }
        for p in chosen_packs:
            for i, v in zip(p.members, p.combo):
                chosen[runlist.order[i]] = v
        groups = tuple(
            tuple(runlist.order[i] for i in sorted(p.members)) for p in chosen_packs
        )
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
            unmeasured=tuple(k for k, m in zip(runlist.order, measured) if not m),
        )

    def _candidates(self, op: Operator, dev) -> list[Variant]:
        """The widths the table allows: the default, first, and every
        narrower one measured exact."""
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
        (a set that is not has no superset that is)."""
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
                    if u > members[0] and measured[u] and u not in banned
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
        with the reset charged when the entries are odd."""
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
            for k, p in enumerate(by_lowest.get(i, ())):
                if p.mask & mask:
                    continue
                rest, picks = best(mask | p.mask, parity ^ (p.entries & 1))
                if p.cost + rest < answer[0]:
                    answer = (p.cost + rest, (id(p),) + picks)
            return answer

        _, picks = best(0, 0)
        by_id = {id(p): p for p in packs}
        return [by_id[k] for k in picks]

    @staticmethod
    def _fit(combo: Sequence[Variant], fitted: dict[tuple[str, ...], bool]) -> bool:
        key = tuple(sorted(v.key for v in combo))
        if key not in fitted:
            texts, params = {}, {}
            for v in combo:
                generated = generate_design(v.op.generator())
                texts[v.key] = str(generated.device)
                params.update({n: str(t) for n, t in generated.params.items()})
            fitted[key] = fits(texts, format_params(params)) is None
        return fitted[key]
