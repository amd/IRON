# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Choosing which arrays share one device configuration (a profile's
packings).

A full ELF configures a device each time a version switches to it, about
``SWITCH_US`` plus ``SWITCH_CORE_US`` per core it holds. ``Packer`` groups a
version's arrays to minimize one estimate of the version's time
(``Packer.objective``): every step's measured time at its array's setting,
plus every switch into a group. Groups grow by the merge that most improves
the estimate, then single arrays move between groups while that improves
it. A group that does not co-reside is fitted (``Packer.fit``): the member
whose change costs least per core it frees is narrowed (its ``widths``
tunables) or aligned to another member's setting so the two share one
array, and members are then widened back while the group still fits; a
member left narrowed has its other tunables searched at its width
(``Packer.retile``). A version's grouping is kept only where the version,
built with it, is bit-identical and faster end to end (``compare_graphs``),
and no other version a packing matches gets slower.
"""

from __future__ import annotations

import collections
import dataclasses
import itertools
import re
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import Any

from aie.utils.compile.jit.params import widths

from iron.common.declare import Operator, Profile
from iron.common.design import OperatorDesign
from iron.common.graph.compiled import CompiledGraph, _step_words, apply_profile
from iron.common.image.packaging import plan
from .autotune import CONFIDENCE, FIT_CACHE, Shape, Timed, settings
from .fusions import _json_safe, compare_graphs, group_fit_verdict
from .measure import Cache, Timing, measure

# npu2 (Strix Halo, turbo): a 1-core design alternated with designs of 1 to
# 8 cores cost 40 to 68 us a switch more than each run alone.
SWITCH_US = 37.0
SWITCH_CORE_US = 7.0
# Merges tried each round, the most adjacent pairs of groups first.
MERGE_CANDIDATES = 8

Setting = dict[str, Any]
Group = dict[Any, Setting]


def width_tunables(op: Operator) -> list[str]:
    """``op``'s tunables that count its columns, channels or cores."""
    declaration = type(op).declaration
    return [n for n in declaration.tunables if declaration.params[n].domain is widths]


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
        switch: tuple[float, float] = (SWITCH_US, SWITCH_CORE_US),
    ):
        self.call, self.dev = call, dev
        self.timing, self.repeats, self.cache = timing, repeats, cache
        self.fit_cache, self.log, self.lock = fit_cache, log, lock
        self.switch = switch
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
                text = str(OperatorDesign(op).module())
                self._cores[array] = len(re.findall(r"aie\.core\(", text))
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
            group_fit_verdict(list(self._distinct(group).values()), self.fit_cache)
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

    def tiles(self, key, setting: Setting) -> list[Setting]:
        """``setting`` with each combination of unit ``key``'s other
        tunables' domains at its widths that every shape of it resolves at,
        ``setting`` itself first.
        """
        names = width_tunables(self.recorded(key))
        at = self.op(key, setting)
        found = [setting]
        for s in settings(at, self.dev, frozenset(names)):
            candidate = {**setting, **{n: v for n, v in s.items() if n not in names}}
            if candidate == setting:
                continue
            try:
                self.arrays(key, candidate)
            except ValueError:
                continue
            found.append(candidate)
        return found

    def cost(self, key, setting: Mapping[str, Any]) -> float:
        """Array ``key``'s steps' time at ``setting``, summed, each shape
        weighted over its points (``Timed.op_points``); infinite where it
        does not build there.
        """
        frozen = (key, tuple(sorted(setting.items())))
        if frozen not in self._costs:
            total = 0.0
            for op, count in self.shapes[key].values():
                try:
                    variants = [op, op._with_tunables(**setting)] if setting else [op]
                except ValueError:
                    total = float("inf")
                    break
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
                    index = len(variants) - 1
                    if index not in m:
                        total = float("inf")
                        break
                    total += weight * count * m[index].t_step_us
            self._costs[frozen] = total
        return self._costs[frozen]

    def objective(self, groups: Sequence[Group]) -> float:
        """The version's estimated time under ``groups``: every array's steps
        at its setting, and every switch into a group, fixed plus per core
        of the group switched into.
        """
        group_of = {k: i for i, g in enumerate(groups) for k in g}
        cores = [self.cores(g) for g in groups]
        fixed, per_core = self.switch
        total = sum(self.cost(k, s) for g in groups for k, s in g.items())
        for a, b in zip(self.order, self.order[1:]):
            if b is not None and (a is None or group_of[a] != group_of[b]):
                total += fixed + per_core * cores[group_of[b]]
        return total

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
        its other tunables there that still fits.
        """
        current = dict(group)
        for key, setting in group.items():
            if not setting:
                continue
            for candidate in self.tiles(key, setting):
                if self.cost(key, candidate) >= self.cost(key, current[key]):
                    continue
                trial = {**current, key: candidate}
                if self.fits(trial):
                    current = trial
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
        each shape once, at its unit's setting.
        """
        out: dict[Any, tuple] = {}
        for k, s in group.items():
            for (_, shape), (op, _) in self.shapes[k].items():
                out.setdefault(
                    shape,
                    (
                        type(op),
                        _json_safe(Shape(op.resolved(self.dev)).named(())),
                        s or None,
                    ),
                )
        return list(out.values())


def _profile(base: Profile, packings: Sequence[list]) -> Profile:
    """``base``'s entries and fusions with ``packings`` as its only packings."""
    out = Profile()
    for cls, dims, tunables in base:
        out.add(cls, **dims, **tunables)
    for kind, steps, edges in base.fusions():
        out.add_fusion(kind, steps, edges)
    for members in packings:
        out.add_packing(members)
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
    switch: tuple[float, float] = (SWITCH_US, SWITCH_CORE_US),
    log: Callable[[str], None] = print,
    lock: bool = False,
) -> Profile:
    """``profile`` with a packing entry for each group of arrays a version
    gains from sharing one device configuration (``Packer``), its members'
    settings in it; a version whose grouping does not gain end to end,
    beyond the noise, adds none, and an entry that slows another version it
    matches is dropped. ``profile``'s own packings are replaced.

    Args:
        switch: A configuration switch's cost, fixed and per core, in us.
    """
    base = _profile(profile, [])
    if not full_elf:
        log("packings: an xclbin per step configures every step; nothing to pack")
        return base
    found: list[tuple[int, list]] = []
    for index, call in enumerate(calls):
        current = _profile(base, [m for _, m in found])
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
            switch=switch,
        )
        groups = packer.group()
        estimate = packer.objective(groups) - packer.objective(
            [{k: {}} for k in packer.shapes]
        )
        entries = [
            packer.members(g)
            for g in groups
            if sum(len(packer.shapes[k]) for k in g) > 1
        ]
        if not entries:
            log(f"{recording.name}: no packing gains")
            continue
        trial = _profile(base, [*(m for _, m in found), *entries])
        delta, noise = _end_to_end(call, dev, current, trial, confirm_timing, log, lock)
        noise_s = "?" if noise is None else f"{noise:.1f}"
        log(
            f"{recording.name}: packed {delta:+.1f} ± {noise_s} us end to end, "
            f"{estimate:+.1f} us estimated"
        )
        if noise is not None and delta < -CONFIDENCE * noise:
            found.extend((index, members) for members in entries)

    # Each version against the packings found on the others.
    for index, call in enumerate(calls):
        foreign = [m for i, m in found if i != index]
        matching = [m for m in foreign if _matches(m, call.recording, dev)]
        if not matching:
            continue
        own = _profile(base, [m for i, m in found if i == index])
        delta, noise = _end_to_end(
            call,
            dev,
            own,
            _profile(base, [m for _, m in found]),
            confirm_timing,
            log,
            lock,
        )
        noise_s = "?" if noise is None else f"{noise:.1f}"
        log(
            f"{call.recording.name}: the other versions' packings "
            f"{delta:+.1f} ± {noise_s} us end to end"
        )
        if noise is not None and delta > CONFIDENCE * noise:
            log(f"  dropping {len(matching)} packing(s) that slow it")
            found = [(i, m) for i, m in found if not any(m is n for n in matching)]
    return _profile(base, [m for _, m in found])


def _matches(members: list, recording, dev) -> bool:
    """Whether a packing entry of ``members`` names a step of ``recording``."""
    probe = _profile(Profile(), [members])
    return any(
        probe.packing_of(s.op.resolved(dev)) is not None for s in recording.steps
    )


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
    (``compare_graphs``).
    """
    graphs = []
    for p in (before, after):
        recording, fused, packing = apply_profile(call.recording, p, dev)
        chosen = plan(
            dev,
            recording,
            True,
            False,
            step_words=_step_words(recording),
            fusions=fused,
        )
        graphs.append(CompiledGraph(recording, chosen, fusions=fused, packing=packing))
    return compare_graphs(call, *graphs, timing=timing, log=log, lock=lock)
