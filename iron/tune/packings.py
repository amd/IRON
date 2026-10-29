# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Choosing which arrays share one device configuration (a profile's
packings).

A full ELF configures an array each time a version switches to it, about
``SWITCH_US`` plus ``SWITCH_CORE_US`` per core of the array switched into.
``price_packings`` groups a version's arrays so consecutive steps share a
configuration: agglomeratively (``Packer``), the pair of groups whose steps
follow each other most often first, narrowing members (their ``widths``
tunables) where the merged group does not co-reside, the narrowing that
costs least per core freed first, while the switches a merge removes
outweigh what its narrowing costs. A version's grouping is kept only where
the version, built with it, is bit-identical and faster end to end
(``compare_graphs``).
"""

from __future__ import annotations

import collections
import dataclasses
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
    """One version's arrays (by ``array_key``), grouped by ``group``: each
    array's operator for each shape running on it, its steps, and what its
    steps cost at a width setting (``cost``, timed by ``measure``).
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
    ):
        self.call, self.dev = call, dev
        self.timing, self.repeats, self.cache = timing, repeats, cache
        self.fit_cache, self.log, self.lock = fit_cache, log, lock
        # Each array's shapes, by Shape.key: the recording's own operator
        # (Timed looks per-call values up by identity) and how many steps.
        self.shapes: dict[Any, dict[Any, list]] = {}
        self.order: list[Any] = []
        for step in call.recording.steps:
            op = step.op.resolved(dev)
            if (
                op.reference_only
                or op.exported_design() is not None
                or not width_tunables(op)
            ):
                self.order.append(None)
                continue
            key = op.array_key()
            entry = self.shapes.setdefault(key, {}).setdefault(
                Shape(op).key, [step.op, 0]
            )
            entry[1] += 1
            self.order.append(key)
        self._costs: dict[tuple, float] = {}
        self._cores: dict[tuple, int] = {}

    def op(self, key, setting: Mapping[str, Any] | None = None) -> Operator:
        """Array ``key``'s first shape's operator at ``setting``, resolved."""
        first, _ = next(iter(self.shapes[key].values()))
        return first._with_tunables(**(setting or {})).resolved(self.dev)

    def cores(self, key, setting: Mapping[str, Any]) -> int:
        """The cores array ``key`` takes at ``setting``."""
        frozen = (key, tuple(sorted(setting.items())))
        if frozen not in self._cores:
            text = str(OperatorDesign(self.op(key, setting)).module())
            self._cores[frozen] = len(re.findall(r"aie\.core\(", text))
        return self._cores[frozen]

    def options(self, key) -> list[dict[str, Any]]:
        """The width settings array ``key`` resolves at, its other tunables
        held, its own first (empty); a width its call gave is searched too.
        """
        first, _ = next(iter(self.shapes[key].values()))
        names = width_tunables(first)
        held = frozenset(first.declaration.tunables) - set(names)
        own = self.op(key)
        return [{}] + [
            {n: s[n] for n in names}
            for s in settings(
                first.replace(pinned=first.pinned - set(names)), self.dev, held
            )
            if any(s[n] != vars(own)[n] for n in names)
        ]

    def cost(self, key, setting: Mapping[str, Any]) -> float:
        """Array ``key``'s steps' time at ``setting``, summed, each shape
        weighted over its points (``Timed.op_points``); infinite where it
        does not build there.
        """
        frozen = (key, tuple(sorted(setting.items())))
        if frozen not in self._costs:
            total = 0.0
            for op, count in self.shapes[key].values():
                variants = [op, op._with_tunables(**setting)] if setting else [op]
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

    def fit(self, members: Mapping[Any, dict[str, Any]]) -> dict | None:
        """``members`` (each array's width setting) narrowed until they
        co-reside, the narrowing that costs least per core it frees first;
        None where no narrowing of them does.
        """
        current = dict(members)
        while True:
            ops = [self.op(k, s) for k, s in current.items()]
            if group_fit_verdict(ops, self.fit_cache) is None:
                return current
            best = None
            for k, s in current.items():
                here = self.cores(k, s)
                for option in self.options(k):
                    fewer = here - self.cores(k, option)
                    if fewer <= 0:
                        continue
                    price = (self.cost(k, option) - self.cost(k, s)) / fewer
                    if best is None or price < best[0]:
                        best = (price, k, option)
            if best is None:
                return None
            _, k, option = best
            current[k] = option

    def group(self) -> list[dict[Any, dict[str, Any]]]:
        """The arrays grouped, each group's members with the width setting
        each runs at in it: the pair of groups whose steps follow each other
        most often merged first, while the merge co-resides (``fit``) and the
        switches it removes outweigh its narrowing.
        """
        groups: list[dict[Any, dict[str, Any]]] = [{k: {}} for k in self.shapes]
        group_of = {k: i for i, k in enumerate(self.shapes)}
        while True:
            for (ga, gb), count in adjacent(self.order, group_of).most_common():
                members = {**groups[ga], **groups[gb]}
                fitted = self.fit(members)
                if fitted is None:
                    continue
                narrowing = sum(
                    self.cost(k, s) - self.cost(k, members[k])
                    for k, s in fitted.items()
                )
                mean_cores = sum(self.cores(k, s) for k, s in fitted.items()) / len(
                    fitted
                )
                saved = count * (SWITCH_US + SWITCH_CORE_US * mean_cores)
                if saved <= narrowing:
                    continue
                self.log(
                    f"  merged {len(groups[ga])} and {len(groups[gb])} arrays: "
                    f"{count} switches, ~{saved:.0f} us saved, "
                    f"{narrowing:+.0f} us narrowing"
                )
                groups[ga], groups[gb] = fitted, {}
                group_of.update(dict.fromkeys(fitted, ga))
                break
            else:
                return [g for g in groups if g]

    def members(self, group: Mapping[Any, dict[str, Any]]) -> list:
        """``group`` as a packing entry's members (``Profile.add_packing``)."""
        return [
            (type(op), _json_safe(Shape(op.resolved(self.dev)).named(())), s or None)
            for k, s in group.items()
            for op, _ in self.shapes[k].values()
        ]


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
    log: Callable[[str], None] = print,
    lock: bool = False,
) -> Profile:
    """``profile`` with a packing entry for each group of arrays a version
    gains from sharing one device configuration (``Packer``), its members'
    narrowed widths in it; a version whose grouping does not gain end to
    end, beyond the noise, adds none. ``profile``'s own packings are
    replaced.
    """
    out = Profile()
    for cls, dims, tunables in profile:
        out.add(cls, **dims, **tunables)
    for kind, steps, edges in profile.fusions():
        out.add_fusion(kind, steps, edges)
    if not full_elf:
        log("packings: an xclbin per step configures every step; nothing to pack")
        return out
    for call in calls:
        recording, _, _ = apply_profile(call.recording, out, dev)
        packer = Packer(
            dataclasses.replace(call, recording=recording),
            dev,
            timing=timing,
            repeats=repeats,
            cache=cache,
            fit_cache=fit_cache,
            log=log,
            lock=lock,
        )
        entries = [
            packer.members(g)
            for g in packer.group()
            if sum(len(packer.shapes[k]) for k in g) > 1
        ]
        if not entries:
            log(f"{recording.name}: no packing gains")
            continue
        trial = Profile()
        for cls, dims, tunables in out:
            trial.add(cls, **dims, **tunables)
        for kind, steps, edges in out.fusions():
            trial.add_fusion(kind, steps, edges)
        for members in [*out.packings(), *entries]:
            trial.add_packing(members)
        delta, noise = _end_to_end(call, dev, out, trial, confirm_timing, log, lock)
        noise_s = "?" if noise is None else f"{noise:.1f}"
        log(f"{recording.name}: packed {delta:+.1f} ± {noise_s} us end to end")
        if noise is not None and delta < -CONFIDENCE * noise:
            for members in entries:
                out.add_packing(members)
    return out


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
