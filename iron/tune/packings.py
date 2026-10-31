# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Choosing which arrays share one device configuration (a profile's
packings).

A full ELF configures a device each time a version switches to it.
``Packer`` groups a version's units (the arrays a shape runs on) to minimize
one estimate of the version's time (``Packer.objective``): every step's
measured time at its unit's setting, plus what the device's cost model
(``costmodel.CostModel``) adds for the grouping's switches and packed steps.
Groups grow by the merge that most improves the estimate, then single units
move between groups while that improves it. A group that does not co-reside
is fitted (``Packer.fit``): the unit whose change costs least per core it
frees is narrowed (its ``widths`` tunables) or aligned to another array's
setting so the two share one, and units are then widened back while the
group still fits; a unit left narrowed has its other tunables searched at
its width (``Packer.retile``). A version's grouping is kept only where the
version, built with it, is bit-identical and faster end to end
(``compare_graphs``), each such check teaching the cost model, and applies
in that version alone; it applies in another version it matches only where
that version, built with it, is faster too (``widen_packings``).
"""

from __future__ import annotations

import collections
import dataclasses
import itertools
import re
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import Any

from aie import ir
from aie.utils.compile.jit.params import widths

from iron.common.declare import Operator, Profile
from iron.common.declare.profile import PackingEntry, Version
from iron.common.design import OperatorDesign
from iron.common.graph.compiled import apply_profile
from iron.common.image.step import FusionKind
from .autotune import CONFIDENCE, FIT_CACHE, Shape, Timed, _json_safe, time_shape
from .costmodel import FEATURES, CostModel
from .failures import Kind, Ledger, first_error
from .fold import fold_profile
from .fusions import (
    NotBitIdentical,
    _device_timeout,
    compare_graphs,
    group_fit_verdict,
    refuse_group,
)
from .measure import Cache, Timing, measure
from .verify import built

# Merges tried each round, the most adjacent pairs of groups first.
MERGE_CANDIDATES = 8
# Searches of one version, each after refusing what failed the last.
ATTEMPTS = 3
# A version is searched only where its switches cost at least this share of
# its steps' own time: packing removes switches, and narrowing slows steps.
MIN_SWITCH_SHARE = 0.05

Setting = dict[str, Any]
Group = dict[Any, Setting]


def width_tunables(op: Operator) -> list[str]:
    """``op``'s tunables that count its columns, channels or cores."""
    declaration = type(op).declaration
    return [n for n in declaration.tunables if declaration.params[n].domain is widths]


def design_cores(op: Operator) -> int:
    """The cores ``op``'s design places."""
    return len(re.findall(r"aie\.core\(", str(OperatorDesign(op).module())))


def adjacent(order: Sequence[Any], group_of: Mapping[Any, int]) -> collections.Counter:
    """How often a step of one group follows a step of another, by the pair
    of groups (lower first): the switches merging the pair removes. A None
    in ``order`` is a step no group holds.
    """
    pairs: collections.Counter = collections.Counter()
    for a, b in zip(order, order[1:]):
        if a is None or b is None or group_of[a] == group_of[b]:
            continue
        ga, gb = sorted((group_of[a], group_of[b]))
        pairs[ga, gb] += 1
    return pairs


class Packer:
    """One version's units, and what grouping them costs: each unit's
    operator for each shape in it and that shape's step count, the
    version's step order by unit, and a unit's time at a setting (``cost``,
    timed by ``measure``).

    A unit is the arrays, as recorded, that share a shape (``Shape.key``),
    with the shapes they run: a profile's packing names shapes, so every
    array a member's shape runs on lands in its group at its setting, and
    a unit is grouped and set as one.
    """

    def __init__(
        self,
        call: Timed,
        dev,
        *,
        timing: Timing,
        repeats: int,
        cache: Cache | None,
        fit_cache: Path,
        log: Callable[[str], None],
        lock: bool,
        model: CostModel,
        ledger: Ledger | None = None,
        cycles: Mapping[str, int] | None = None,
        core_mhz: float | None = None,
    ):
        self.call, self.dev = call, dev
        self.timing, self.repeats, self.cache = timing, repeats, cache
        self.fit_cache, self.log, self.lock = fit_cache, log, lock
        self.model, self.ledger = model, ledger
        self.cycles, self.core_mhz = cycles, core_mhz
        # Each step's array and shape, None for a step no unit holds.
        placed: list[tuple[Any, Any, Operator] | None] = []
        unit_of: dict[Any, int] = {}
        for step in call.recording.steps:
            op = step.op.resolved(dev)
            if (
                op.reference_only
                or op.exported_design() is not None
                or not width_tunables(op)
            ):
                placed.append(None)
                continue
            array, shape = ("array", op.array_key()), ("shape", Shape(op).key)
            placed.append((array, shape, step.op))
            known = {unit_of[n] for n in (array, shape) if n in unit_of}
            unit = min(known) if known else len(placed)
            for name, u in list(unit_of.items()):
                if u in known:
                    unit_of[name] = unit
            unit_of[array] = unit_of[shape] = unit
        # Each unit's shapes, by (array_key, Shape.key) as recorded: the
        # recording's own operator (Timed looks per-call values up by
        # identity) and its step count.
        self.shapes: dict[int, dict[Any, list]] = {}
        self.order: list[int | None] = []
        for entry in placed:
            if entry is None:
                self.order.append(None)
                continue
            array, shape, op = entry
            unit = unit_of[array]
            counted = self.shapes.setdefault(unit, {}).setdefault(
                (array[1], shape[1]), [op, 0]
            )
            counted[1] += 1
            self.order.append(unit)
        self._costs: dict[tuple, float] = {}
        self._cores: dict[Any, int] = {}
        self._options: dict[Any, list[Setting]] = {}

    def recorded(self, key) -> Operator:
        """Unit ``key``'s first shape's operator, as recorded."""
        first, _ = next(iter(self.shapes[key].values()))
        return first

    def op(self, key, setting: Mapping[str, Any]) -> Operator:
        """Unit ``key``'s first shape's operator at ``setting``, resolved."""
        return self.recorded(key)._with_tunables(**setting).resolved(self.dev)

    def array(self, key, setting: Mapping[str, Any]):
        """The array unit ``key``'s first shape runs on at ``setting``."""
        return self.op(key, setting).array_key()

    def arrays(self, key, setting: Mapping[str, Any]) -> dict[Any, Operator]:
        """The arrays unit ``key``'s shapes run on at ``setting``, each with
        an operator running on it.
        """
        out: dict[Any, Operator] = {}
        for op, _ in self.shapes[key].values():
            at = op._with_tunables(**setting).resolved(self.dev)
            out.setdefault(at.array_key(), at)
        return out

    def cores(self, group: Group) -> int:
        """The cores ``group``'s distinct arrays take."""
        total = 0
        for array, op in self._distinct(group).items():
            if array not in self._cores:
                self._cores[array] = design_cores(op)
            total += self._cores[array]
        return total

    def _distinct(self, group: Group) -> dict[Any, Operator]:
        """``group``'s distinct arrays, each with an operator running on it."""
        out: dict[Any, Operator] = {}
        for key, setting in group.items():
            for array, op in self.arrays(key, setting).items():
                out.setdefault(array, op)
        return out

    def fits(self, group: Group) -> bool:
        """Whether ``group``'s distinct arrays place in one device."""
        return (
            group_fit_verdict(
                list(self._distinct(group).values()), self.fit_cache, ledger=self.ledger
            )
            is None
        )

    def options(self, key) -> list[Setting]:
        """Array ``key``'s width settings, its own first (empty): each width
        combination its domains give, its other tunables held where they
        still resolve there, else left to resolve afresh.
        """
        if key in self._options:
            return self._options[key]
        first = self.recorded(key)
        names = width_tunables(first)
        free = first.replace(pinned=first.pinned - set(names))
        domains = {
            n: v
            for n, v in free.resolved(self.dev)._domains(self.dev).items()
            if n in names
        }
        own = self.op(key, {})
        others = {
            n: None
            for n in first.declaration.tunables
            if n not in names and first.declaration.params[n].init
        }
        found = [{}]
        for combo in itertools.product(*domains.values()):
            setting = dict(zip(domains, combo))
            if all(vars(own)[n] == v for n, v in setting.items()):
                continue
            for candidate in (setting, {**setting, **others}):
                try:
                    self.arrays(key, candidate)
                except ValueError:
                    continue
                found.append(candidate)
                break
        self._options[key] = found
        return found

    def cost(self, key, setting: Mapping[str, Any]) -> float:
        """Unit ``key``'s steps' time at ``setting``, summed, each shape
        weighted over its points (``Timed.op_points``); infinite where it
        does not build there. Timing one setting times every width option of
        the unit not yet timed beside it, in one ``measure`` batch.
        """
        frozen = (key, tuple(sorted(setting.items())))
        if frozen not in self._costs:
            pending = [dict(setting)] + [
                o
                for o in self.options(key)
                if o != setting and (key, tuple(sorted(o.items()))) not in self._costs
            ]
            self._price(key, pending)
        return self._costs[frozen]

    def _price(self, key, pending: Sequence[Setting]) -> None:
        """Time unit ``key`` at each of ``pending``, one ``measure`` batch per
        shape and point, into ``_costs``.
        """
        if not pending:
            return
        totals = [0.0] * len(pending)
        for op, count in self.shapes[key].values():
            variants: list[Operator] = [op]
            index: list[int | None] = []
            for setting in pending:
                if not setting:
                    index.append(0)
                    continue
                try:
                    variants.append(op._with_tunables(**setting))
                except ValueError:
                    index.append(None)
                    continue
                index.append(len(variants) - 1)
            for weight, values in self.call.op_points(op):
                m = measure(
                    variants,
                    full_elf=True,
                    timing=self.timing,
                    repeats=self.repeats,
                    values=values,
                    inputs=self.call.op_inputs(op),
                    cache=self.cache,
                    log=self.log,
                    lock=self.lock,
                )
                for n, i in enumerate(index):
                    if i is None or i not in m:
                        totals[n] = float("inf")
                    else:
                        totals[n] += weight * count * m[i].t_step_us
        for setting, total in zip(pending, totals):
            self._costs[(key, tuple(sorted(setting.items())))] = total

    def steps(self, groups: Sequence[Group]) -> float:
        """Every unit's steps' time at its setting under ``groups``, summed."""
        return sum(self.cost(k, s) for g in groups for k, s in g.items())

    def features(self, groups: Sequence[Group]) -> dict[str, float]:
        """What ``groups`` cost beyond their steps' own times depends on
        (``costmodel.FEATURES``): the switches into a group, the cores of the
        groups switched into, and the steps run in a group of several units.
        """
        group_of = {k: i for i, g in enumerate(groups) for k in g}
        cores = [self.cores(g) for g in groups]
        switches = switch_cores = 0
        for a, b in zip(self.order, self.order[1:]):
            if b is not None and (a is None or group_of[a] != group_of[b]):
                switches += 1
                switch_cores += cores[group_of[b]]
        packed = sum(
            1 for k in self.order if k is not None and len(groups[group_of[k]]) > 1
        )
        return {
            "switches": switches,
            "switch_cores": switch_cores,
            "packed_steps": packed,
        }

    def objective(self, groups: Sequence[Group]) -> float:
        """The version's estimated time under ``groups``: its steps' own
        times and what the cost model adds for their features.
        """
        return self.steps(groups) + self.model.predict(self.features(groups))

    def changes(self, group: Group) -> list[tuple[Any, Setting]]:
        """Every one-unit change of ``group``: a unit at another width option,
        or at the whole setting of an array in the group (its own or
        another unit's) where that puts two of the group's arrays on one.
        """
        changes = [(k, o) for k in group for o in self.options(k) if o != group[k]]
        arrays = {
            array: op
            for k, s in group.items()
            for array, op in self.arrays(k, s).items()
        }
        for key, setting in group.items():
            own = self.arrays(key, setting)
            for array, op in arrays.items():
                if type(op) is not type(self.recorded(key)):
                    continue
                aligned = {
                    n: vars(op)[n]
                    for n in op.declaration.tunables
                    if op.declaration.params[n].init
                }
                if aligned == setting:
                    continue
                try:
                    moved = self.arrays(key, aligned)
                except ValueError:
                    continue
                if len(set(moved) | set(arrays) - set(own)) < len(arrays):
                    changes.append((key, aligned))
        return changes

    def fit(self, group: Group) -> Group | None:
        """``group`` changed until it co-resides, the change costing least per
        core it frees first, then widened back while it still fits; None
        where no change of it fits.
        """
        current = dict(group)
        while not self.fits(current):
            here, best = self.cores(current), None
            for key, setting in self.changes(current):
                trial = {**current, key: setting}
                freed = here - self.cores(trial)
                if freed <= 0:
                    continue
                price = (self.cost(key, setting) - self.cost(key, current[key])) / freed
                if best is None or price < best[0]:
                    best = (price, trial)
            if best is None:
                return None
            current = best[1]
        while True:
            best = None
            for key, setting in self.changes(current):
                gain = self.cost(key, current[key]) - self.cost(key, setting)
                if gain <= 0 or (best is not None and gain <= best[0]):
                    continue
                trial = {**current, key: setting}
                if self.fits(trial):
                    best = (gain, trial)
            if best is None:
                return current
            current = best[1]

    def retile(self, group: Group) -> Group:
        """``group`` with each member off its own setting at the fastest of
        its other tunables there that still fits, searched as an operator's
        own tuning searches them (``time_shape``), its widths held.
        """
        current = dict(group)
        for key, setting in group.items():
            if not setting:
                continue
            shape = Shape(self.recorded(key))
            shape.pinned = frozenset(width_tunables(self.recorded(key)))
            shape.members = [
                (
                    op._with_tunables(**setting),
                    self.call.op_points(op),
                    self.call.op_inputs(op),
                )
                for op, _ in self.shapes[key].values()
            ]
            tried = time_shape(
                shape,
                self.dev,
                full_elf=True,
                timing=self.timing,
                repeats=self.repeats,
                cache=self.cache,
                cycles=self.cycles,
                core_mhz=self.core_mhz,
                log=self.log,
            )
            for t in sorted((t for t in tried if t.gains), key=lambda t: t.delta_us):
                trial = {**current, key: {**setting, **t.tunables}}
                if self.fits(trial):
                    current = trial
                    break
        return current

    def group(self) -> list[Group]:
        """The arrays grouped to minimize ``objective``: the merge that most
        improves it each round (of the ``MERGE_CANDIDATES`` most adjacent
        pairs of groups), then single arrays moved between groups while
        that improves it, then each group retiled.
        """
        groups: list[Group] = [{k: {}} for k in self.shapes]
        score = self.objective(groups)
        while True:
            group_of = {k: i for i, g in enumerate(groups) for k in g}
            pairs = adjacent(self.order, group_of).most_common(MERGE_CANDIDATES)
            best = None
            for (ga, gb), _ in pairs:
                fitted = self.fit({**groups[ga], **groups[gb]})
                if fitted is None:
                    continue
                trial = [g for i, g in enumerate(groups) if i not in (ga, gb)]
                trial.append(fitted)
                value = self.objective(trial)
                if value < score and (best is None or value < best[0]):
                    best = (value, trial)
            if best is None:
                break
            score, groups = best
            self.log(f"  merged: {len(groups)} groups, ~{score:.0f} us estimated")
        groups, score = self._improve(groups, score)
        groups = [self.retile(g) for g in groups]
        self.log(f"  grouped: {len(groups)} groups, ~{self.objective(groups):.0f} us")
        return groups

    def _improve(self, groups: list[Group], score: float) -> tuple[list[Group], float]:
        """``groups`` after moving single arrays between groups (or into one
        of their own) while that improves ``objective``.
        """
        while True:
            best = None
            for gi, g in enumerate(groups):
                if len(g) < 2:
                    continue
                for key in g:
                    rest = self.fit({k: s for k, s in g.items() if k != key})
                    if rest is None:
                        continue
                    targets = [i for i in range(len(groups)) if i != gi] + [None]
                    for hi in targets:
                        moved = (
                            {key: {}}
                            if hi is None
                            else self.fit({**groups[hi], key: g[key]})
                        )
                        if moved is None:
                            continue
                        trial = [
                            rest if i == gi else moved if i == hi else h
                            for i, h in enumerate(groups)
                        ]
                        if hi is None:
                            trial.append(moved)
                        value = self.objective(trial)
                        if value < score and (best is None or value < best[0]):
                            best = (value, trial)
            if best is None:
                return groups, score
            score, groups = best
            self.log(f"  moved an array: ~{score:.0f} us estimated")

    def members(self, group: Group) -> list:
        """``group`` as a packing entry's members (``Profile.add_packing``):
        each shape once, at its unit's setting, named without the dimensions
        a host sizes (``Timed.varying``) wherever the shape is still the only
        one of the recording's it names.
        """
        resolved = [s.op.resolved(self.dev) for s in self.call.recording.steps]
        out: dict[Any, tuple] = {}
        for k, s in group.items():
            for (_, shape), (op, _) in self.shapes[k].items():
                named = Shape(op.resolved(self.dev)).named((), derived=True)
                drop = self.call.varying.get(shape, frozenset())
                kept = {n: v for n, v in named.items() if n not in drop}
                if any(
                    isinstance(r, type(op))
                    and Shape(r).key != shape
                    and Profile.matches(kept, Profile.dims(type(r), vars(r)))
                    for r in resolved
                ):
                    kept = named
                out.setdefault(shape, (type(op), _json_safe(kept), s or None))
        return list(out.values())


def _profile(base: Profile, packings: Sequence[PackingEntry]) -> Profile:
    """``base``'s entries and fusions with ``packings`` as its only packings."""
    out = Profile()
    for cls, dims, tunables in base:
        out.add(cls, **dims, **tunables)
    for kind, steps, edges, versions in base.fusions():
        out.add_fusion(kind, steps, edges, versions)
    for p in packings:
        out.add_packing(p.members, p.versions)
    return out


def price_packings(
    calls: Sequence[Timed],
    dev,
    profile: Profile,
    *,
    full_elf: bool,
    timing: Timing = Timing(),
    confirm_timing: Timing = Timing(rounds=3, calls=10),
    repeats: int = 9,
    cache: Cache | None = None,
    fit_cache: Path = FIT_CACHE,
    model: CostModel | None = None,
    ledger: Ledger | None = None,
    cycles: Mapping[str, int] | None = None,
    core_mhz: float | None = None,
    progress: Callable[[Profile, CostModel], None] | None = None,
    log: Callable[[str], None] = print,
    lock: bool = False,
) -> Profile:
    """``profile`` with a packing entry for each group of arrays a version
    gains from sharing one device configuration (``Packer``), its members'
    settings in it, applying in that version; a version whose grouping does
    not gain end to end, beyond the noise, adds none. Each entry then applies
    in another version it matches only where that version gains from it too
    (``widen_packings``). ``profile``'s own packings are replaced, but for
    another graph's (``_foreign``), which a search of these calls leaves as
    they are, so one profile can hold several models' packings. A version
    whose every switch, priced by ``model``, costs under
    ``MIN_SWITCH_SHARE`` of its steps' own time is not searched.

    A grouping whose version does not build, hangs or is not bit-identical
    is refused (``refuse_group``) and the version searched again, up to
    ``ATTEMPTS`` times, recorded in ``ledger`` where one is given.

    Args:
        model: What a version pays beyond its steps' times; each end-to-end
            check adds it a sample. The prior where None.
        cycles: Kernel cycles per call by recipe key, which spare a narrowed
            array's tile search the settings its kernel alone makes slower
            (``time_shape``).
        core_mhz: The cores' clock ``cycles`` are timed at.
        progress: Called after each version's search with the profile found
            so far and ``model``, so a caller keeps what earlier versions
            found should a later one fail.
    """
    model = CostModel() if model is None else model
    base = _profile(profile, [e for e in profile.packings() if _foreign(e, calls, dev)])
    if not full_elf:
        log("packings: an xclbin per step configures every step; nothing to pack")
        return base
    found: list[PackingEntry] = []
    for call in calls:
        version = call.recording.version
        current = _profile(base, found)
        recording, _, _ = apply_profile(call.recording, current, dev)
        packer = Packer(
            dataclasses.replace(call, recording=recording),
            dev,
            timing=timing,
            repeats=repeats,
            cache=cache,
            fit_cache=fit_cache,
            log=log,
            lock=lock,
            model=model,
            ledger=ledger,
            cycles=cycles,
            core_mhz=core_mhz,
        )
        alone = [{k: {}} for k in packer.shapes]
        for k in packer.shapes:
            packer._price(k, [{}])
        switching, own = model.predict(packer.features(alone)), packer.steps(alone)
        if switching < MIN_SWITCH_SHARE * own:
            log(
                f"{recording.name}: its switches cost ~{switching:.0f} us of "
                f"{own:.0f} us of steps; not searched"
            )
            continue
        for attempt in range(ATTEMPTS):
            groups = packer.group()
            packed = [g for g in groups if sum(len(packer.shapes[k]) for k in g) > 1]
            if not packed:
                log(f"{recording.name}: no packing gains")
                break
            entries = [
                PackingEntry(tuple(packer.members(g)), frozenset({version}))
                for g in packed
            ]
            trial = _profile(base, [*found, *entries])
            try:
                delta, noise = _end_to_end(
                    call, dev, current, trial, confirm_timing, log, lock
                )
            except (ValueError, RuntimeError, ir.MLIRError) as e:
                kind = (
                    Kind.HANG
                    if _device_timeout(e)
                    else Kind.MISMATCH if isinstance(e, NotBitIdentical) else Kind.BUILD
                )
                log(f"{recording.name}: refused, {kind.value}: {first_error(str(e))}")
                if ledger is not None:
                    trial_path = ledger.directory / "profiles"
                    trial_path.mkdir(parents=True, exist_ok=True)
                    trial.save(trial_path / f"{recording.name}-{attempt}.json")
                    ledger.record(
                        kind,
                        dev.name,
                        str(e),
                        f"{recording.name} packed, profile "
                        f"profiles/{recording.name}-{attempt}.json",
                    )
                for g in packed:
                    refuse_group(
                        list(packer._distinct(g).values()),
                        f"{kind.value}: {first_error(str(e))}",
                        fit_cache,
                    )
                continue
            estimate = packer.objective(groups) - packer.objective(alone)
            steps = packer.steps(groups) - packer.steps(alone)
            before, after = packer.features(alone), packer.features(groups)
            model.add({f: after[f] - before[f] for f in FEATURES}, delta - steps)
            noise_s = "?" if noise is None else f"{noise:.1f}"
            log(
                f"{recording.name}: packed {delta:+.1f} ± {noise_s} us end to end, "
                f"{estimate:+.1f} us estimated; cost model now "
                + ", ".join(f"{f} {v:.1f}" for f, v in model.terms.items())
            )
            if noise is not None and delta < -CONFIDENCE * noise:
                found.extend(entries)
            break
        if progress is not None:
            progress(_profile(base, found), model)
    return widen_packings(
        calls, dev, _profile(base, found), timing=confirm_timing, log=log, lock=lock
    )


def _with_fusions(base: Profile, fusions: Sequence) -> Profile:
    """``base``'s entries and packings with ``fusions`` as its only
    fusions: the fold-narrowing counterpart of ``_profile``, which does the
    same for a profile's packings.
    """
    out = Profile()
    for cls, dims, tunables in base:
        out.add(cls, **dims, **tunables)
    for kind, steps, edges, versions in fusions:
        out.add_fusion(kind, steps, edges, versions)
    for entry in base.packings():
        out.add_packing(entry.members, entry.versions)
    return out


def _narrow_for_rejected(fusions: Sequence, version: Version) -> list:
    """``fusions`` with a ``FOLD`` entry's own ``versions`` narrowed past
    ``version``, dropped entirely where that would leave it naming none: a
    version ``price_folds_before_packing`` rejects keeps the profile as it
    stood for the shapes a fold scoped to it (and no other version) alone
    named. A fusion of another kind, or a fold unscoped or scoped to a
    version other than this one, is untouched. Its packings are the
    caller's to replace (``_rejoin``): they were searched on the folded
    steps.
    """
    out = []
    for kind, steps, edges, versions in fusions:
        if kind is FusionKind.FOLD and versions is not None and version in versions:
            remaining = versions - {version}
            if not remaining:
                continue
            versions = remaining
        out.append((kind, steps, edges, versions))
    return out


def _decide_fold(
    fusions: Sequence,
    call: Timed,
    version: Version,
    delta: float,
    noise: float | None,
    log: Callable[[str], None],
) -> list:
    """``call``'s own version's share of ``price_folds_before_packing``'s
    decision: ``fusions`` kept as given where ``delta``/``noise`` (``call``'s
    ``_end_to_end`` against the profile as it stands) gain beyond the noise
    (``CONFIDENCE``, as every other packing decision here already asks), an
    unmeasurable noise counting as no gain; narrowed back out otherwise
    (``_narrow_for_rejected``), so this version keeps the profile as it
    stood rather than the whole packed-and-folded result discarded. Logs
    which, by name, with the gain found.

    Device-free on its own: the device time is in ``delta``/``noise``
    (``_end_to_end``, the one part of this decision that needs it), not here.
    """
    report = (
        f"{call.recording.name} {delta:+.1f} ± "
        f"{'?' if noise is None else f'{noise:.1f}'} us"
    )
    if noise is not None and delta < -CONFIDENCE * noise:
        log(
            f"price_folds_before_packing: {call.recording.name} keeps its folds, {report}"
        )
        return list(fusions)
    log(
        f"price_folds_before_packing: {call.recording.name} keeps the profile "
        f"as it stood, its folds do not gain beyond the noise, {report}"
    )
    return _narrow_for_rejected(fusions, version)


def price_folds_before_packing(
    calls: Sequence[Timed],
    dev,
    profile: Profile,
    *,
    full_elf: bool,
    timing: Timing = Timing(),
    confirm_timing: Timing = Timing(rounds=3, calls=10),
    repeats: int = 9,
    cache: Cache | None = None,
    fit_cache: Path = FIT_CACHE,
    model: CostModel | None = None,
    ledger: Ledger | None = None,
    cycles: Mapping[str, int] | None = None,
    core_mhz: float | None = None,
    progress: Callable[[Profile, CostModel], None] | None = None,
    log: Callable[[str], None] = print,
    lock: bool = False,
) -> Profile:
    """``profile`` with the folds its arrays admit (``iron.tune.fold.
    fold_profile``, scoped so a fold never splits a device array a call
    site that does not take it still shares, and scoped to the graph
    versions it was found in) packed (``price_packings``, so the search
    groups the same folded step list ``apply_profile`` builds from at build
    time). Kept per version, the way ``widen_packings`` decides a packing
    entry's own widening: a version keeps its folds only where it, folded
    and packed, beats ``profile`` as it stands (its own packings, or none)
    end to end (``compare_graphs``); one that does not gain keeps the
    profile as it stood instead, its own fold entries narrowed back out
    rather than the whole packed result discarded (``_narrow_for_rejected``),
    and its packings searched again without them (``_rejoin``): the ones
    found on its folded steps were never priced unfolded. The plain
    ``price_packings`` search on ``profile`` alone runs, and its result is
    returned, where folding admits nothing at all. The fold entries
    this adds are the tuner's own proposal, not Erika's (``chosen_folds``
    still takes any a hand-written profile names, unscoped).
    """
    with_folds = fold_profile(profile, calls)

    def plain() -> Profile:
        return price_packings(
            calls,
            dev,
            profile,
            full_elf=full_elf,
            timing=timing,
            confirm_timing=confirm_timing,
            repeats=repeats,
            cache=cache,
            fit_cache=fit_cache,
            model=model,
            ledger=ledger,
            cycles=cycles,
            core_mhz=core_mhz,
            progress=progress,
            log=log,
            lock=lock,
        )

    if with_folds.fusions() == profile.fusions():
        log(
            "price_folds_before_packing: no fold the tuner's own array "
            "scoping admits; packing the plain profile"
        )
        return plain()
    packed_and_folded = price_packings(
        calls,
        dev,
        with_folds,
        full_elf=full_elf,
        timing=timing,
        confirm_timing=confirm_timing,
        repeats=repeats,
        cache=cache,
        fit_cache=fit_cache,
        model=model,
        ledger=ledger,
        cycles=cycles,
        core_mhz=core_mhz,
        progress=progress,
        log=log,
        lock=lock,
    )
    fusions = packed_and_folded.fusions()
    rejected = []
    for call in calls:
        candidate = _with_fusions(packed_and_folded, fusions)
        delta, noise = _end_to_end(
            call, dev, profile, candidate, confirm_timing, log, lock
        )
        kept = _decide_fold(fusions, call, call.recording.version, delta, noise, log)
        if kept != fusions:
            rejected.append(call)
        fusions = kept
    folded = _with_fusions(packed_and_folded, fusions)
    if not rejected:
        return folded
    # A rejected version's packings were searched on its folded steps; it
    # takes the plain search's instead.
    log(
        "price_folds_before_packing: searching the packings of "
        f"{len(rejected)} version(s) without their folds"
    )
    unfolded = price_packings(
        rejected,
        dev,
        folded,
        full_elf=full_elf,
        timing=timing,
        confirm_timing=confirm_timing,
        repeats=repeats,
        cache=cache,
        fit_cache=fit_cache,
        model=model,
        ledger=ledger,
        cycles=cycles,
        core_mhz=core_mhz,
        progress=progress,
        log=log,
        lock=lock,
    )
    return _rejoin(folded, unfolded, {c.recording.version for c in rejected})


def _rejoin(folded: Profile, unfolded: Profile, versions: set[Version]) -> Profile:
    """``folded``'s packings outside ``versions`` and ``unfolded``'s inside
    them: the versions that rejected their folds take the packings searched
    without them, every other version keeps its folded ones. An unscoped
    entry is every version's and stays as ``folded`` has it.
    """
    entries = []
    for entry in folded.packings():
        if entry.versions is None:
            entries.append(entry)
        elif rest := entry.versions - versions:
            entries.append(PackingEntry(entry.members, frozenset(rest)))
    for entry in unfolded.packings():
        if entry.versions is not None and (own := entry.versions & versions):
            entries.append(PackingEntry(entry.members, frozenset(own)))
    return _profile(folded, entries)


def widen_packings(
    calls: Sequence[Timed],
    dev,
    profile: Profile,
    *,
    timing: Timing = Timing(rounds=3, calls=10),
    log: Callable[[str], None] = print,
    lock: bool = False,
) -> Profile:
    """``profile`` with each packing entry that names its versions applying
    also in each version of ``calls`` it matches but does not name, where
    that version, built with them, is faster end to end beyond the noise;
    elsewhere it keeps to the versions it names. A version's arrays are
    another's at other extents, so a grouping that pays where switches
    dominate can slow a version whose arrays' own time does. One end-to-end
    check per version the entries match.
    """
    entries = profile.packings()
    for call in calls:
        version = call.recording.version
        foreign = {
            i
            for i, e in enumerate(entries)
            if e.versions is not None
            and version not in e.versions
            and _matches(e.members, call.recording, dev)
        }
        if not foreign:
            continue
        widened = [
            (
                PackingEntry(e.members, e.versions | {version})
                if i in foreign and e.versions is not None
                else e
            )
            for i, e in enumerate(entries)
        ]
        delta, noise = _end_to_end(
            call,
            dev,
            _profile(profile, entries),
            _profile(profile, widened),
            timing,
            log,
            lock,
        )
        noise_s = "?" if noise is None else f"{noise:.1f}"
        log(
            f"{call.recording.name}: the other versions' packings "
            f"{delta:+.1f} ± {noise_s} us end to end"
        )
        if noise is not None and delta < -CONFIDENCE * noise:
            log(f"  applying {len(foreign)} packing(s) here too")
            entries = widened
        else:
            log(f"  keeping {len(foreign)} packing(s) to the versions they name")
    return _profile(profile, entries)


def _foreign(entry: PackingEntry, calls: Sequence[Timed], dev) -> bool:
    """Whether a member of ``entry`` names no step of any of ``calls``: an
    entry another graph's search made (a shape these graphs never run), not
    one of theirs to replace.
    """
    probe = Profile()
    probe.add_packing(entry.members)
    named = {
        member
        for c in calls
        for step in c.recording.steps
        for _, member, _ in probe.packings_of(step.op.resolved(dev), None)
    }
    return len(named) < len(entry.members)


def _matches(members: Sequence, recording, dev) -> bool:
    """Whether a packing entry of ``members`` names a step of ``recording``."""
    probe = Profile()
    probe.add_packing(members)
    version = recording.version
    return any(probe.packings_of(s.op.resolved(dev), version) for s in recording.steps)


def _end_to_end(
    call: Timed,
    dev,
    before: Profile,
    after: Profile,
    timing: Timing,
    log: Callable[[str], None],
    lock: bool,
) -> tuple[float, float | None]:
    """``call``'s version built under ``after`` against it under ``before``
    (``compare_graphs``), each packaged as ``dev`` does: a full ELF where it
    dispatches one, else an xclbin per step.
    """
    return compare_graphs(
        call,
        built(call, before, dev),
        built(call, after, dev),
        timing=timing,
        log=log,
        lock=lock,
    )
