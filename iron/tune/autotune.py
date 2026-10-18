# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Choosing each operator's tunables by timing them, written as a profile.

``autotune`` takes the calls a model runs (``Call``), finds each operator
shape in them, times every setting of its tunables
(``Operator.domains``) the placer takes against the setting it was traced
at, and returns a ``Profile`` naming the fastest for each shape. A setting
is taken only where it beats the traced one by ``CONFIDENCE`` standard
errors at the calls' operating points, and only where its output is
bit-identical to the traced one's or within both their tolerances
(``measure.judge``). Steps sharing a shape share its entry, so they are
timed together and their times summed. A GEMM setting is not built when its
matmul kernel alone, at the cycles mlir-aie's nightly timed it at
(``kernel_cycles``), takes longer than the fastest setting timed so far.
"""

from __future__ import annotations

import dataclasses
import hashlib
import itertools
import json
import logging
import math
import urllib.request
from collections.abc import Callable, Hashable, Mapping, Sequence
from pathlib import Path
from typing import Any

import numpy as np
from aie.iron import ExternalFunction
from aie.utils.compile import NPU_CACHE_HOME

from iron.common.declare import Operator, Profile
from iron.common.design import OperatorDesign
from iron.common.graph.trace import TracedGraph
from iron.common.image.coresidence import fits
from iron.operators.gemm import GEMM
from .measure import Cache, Standalone, Timing, judge, measure, write

logger = logging.getLogger(__name__)

# Standard errors a setting's step must beat the traced one's by to be taken.
CONFIDENCE = 2.0

# Past this many settings, a shape's tunables are searched one at a time.
EXHAUSTIVE = 32

FIT_CACHE = Path(NPU_CACHE_HOME) / "iron" / "fits"

# A core's clock in cycles per us: what mlir-aie's programming guide measured
# on npu2 (section-4d, "Two clocks"). npu1's has not been measured.
CORE_MHZ = {"npu2": 1760.0}

KERNEL_CHECKS = "https://xilinx.github.io/mlir-aie/kernel-checks/{npu}/latest.json"


def kernel_cycles(dev, log: Callable[[str], None] = print) -> dict[str, int]:
    """Each kernel's cycles per call as mlir-aie's nightly last timed it on
    ``dev``'s NPU, by ``ExternalFunction.build_key``; empty where they
    cannot be read or this mlir-aie names no builds.
    """
    if not hasattr(ExternalFunction, "build_key"):
        return {}
    url = KERNEL_CHECKS.format(npu=dev.name)
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            latest = json.load(response)
    except (OSError, ValueError) as e:
        log(f"no kernel timings from {url}: {e}")
        return {}
    rows = latest.get("rows", {})
    return {
        key: rows[case]["cycles"]["value"]
        for case, key in latest.get("builds", {}).items()
        if "cycles" in rows.get(case, {})
    }


def least_us(op: GEMM, values: Mapping[str, int], cycles, dev) -> float | None:
    """A step time ``op`` cannot beat at per-call ``values``: its busiest
    core's matmul calls at ``cycles`` per call. None where ``cycles`` does
    not hold its matmul or ``dev``'s core clock is unknown.
    """
    mhz = CORE_MHZ.get(dev.name)
    if mhz is None:
        return None
    per_call = cycles.get(op.array_config().matmul().build_key)
    if per_call is None:
        return None
    return op.matmul_calls(values) * per_call / mhz


@dataclasses.dataclass(frozen=True)
class Point:
    """A share of a graph's calls, run at one set of its per-call values.

    Attributes:
        weight: The share; a call's points' weights sum to 1.
        values: The graph's per-call values there, by name.
    """

    weight: float
    values: Mapping[str, int]


@dataclasses.dataclass(frozen=True)
class Call:
    """One call of a traced graph, as its operators are timed in: the
    graph's per-call values, and what any buffer whose contents a step's
    time follows holds, by graph buffer name. ``points`` are the values its
    calls run at, where they differ from call to call: an operator whose
    work they change is timed at each (``op_points``).
    """

    traced: TracedGraph
    values: Mapping[str, int] = dataclasses.field(default_factory=dict)
    contents: Mapping[str, np.ndarray] = dataclasses.field(default_factory=dict)
    points: Sequence[Point] = ()

    def op_values(
        self, op: Operator, values: Mapping[str, int] | None = None
    ) -> dict[str, int]:
        """The per-call values ``op`` is written in this call, or at the
        graph's ``values``, by member name.
        """
        # A table's address the graph fills in; a word step alone reads none.
        values = {
            **dict.fromkeys(self.traced.addresses, 0),
            **(self.values if values is None else values),
        }
        return {
            b.member.name: b.expression.evaluate(values)
            for b in self.traced.bindings
            if b.op is op
        }

    def op_points(self, op: Operator) -> list[tuple[float, dict[str, int]]]:
        """Where ``op`` is timed: each set of bound extents this call's
        ``points`` write it, with their summed weight and the per-call
        values of the first; the call's own values alone where every point
        writes it alike, as where it has no bound extent.
        """
        out: dict[tuple, tuple[float, dict[str, int]]] = {}
        for point in self.points:
            values = self.op_values(op, point.values)
            label = tuple(values[e] for e in sorted(op.bound_extents))
            weight, first = out.get(label, (0.0, values))
            out[label] = (weight + point.weight, first)
        if len(out) > 1:
            return list(out.values())
        return [(1.0, self.op_values(op))]

    def op_inputs(self, op: Operator) -> dict[str, np.ndarray]:
        """What ``op``'s buffers hold in this call, by ``op``'s buffer name."""
        return {
            buf.name: self.contents[ref.root]
            for step in self.traced.steps
            if step.op is op
            for buf, ref in zip(op.buffers, step.refs())
            if ref.nbytes is None and ref.root in self.contents
        }


def settings(
    op: Operator, dev, pinned: frozenset[str] = frozenset()
) -> list[dict[str, Any]]:
    """``op``'s tunables as resolved for ``dev``, then every other
    combination of their ``Operator.domains`` it resolves at and whose
    derived transfers fit their descriptors, each design once.

    Args:
        pinned: Tunables another operator of its shape pins, held at the
            value ``op`` resolves them to.
    """
    if pinned - op.pinned:
        resolved = op.resolved(dev)
        op = dataclasses.replace(
            op,
            pinned=op.pinned | pinned,
            **{name: vars(resolved)[name] for name in pinned - op.pinned},
        )
    resolved = op.resolved(dev)
    domains = resolved._domains(dev)
    default = {name: vars(resolved)[name] for name in domains}
    out = {_identity(resolved, dev): default}
    dropped = 0
    for combo in itertools.product(*domains.values()):
        tunables = dict(zip(domains, combo))
        if tunables == default:
            continue
        try:
            moved = op._with_tunables(**tunables).resolved(dev)
            if not moved.has_sequence_override():
                for buf in moved.buffers:
                    buf.transfers()
        except ValueError as e:  # unresolvable, incompatible or untransferable here
            logger.debug("%s at %s dropped: %s", type(op).__name__, tunables, e)
            dropped += 1
            continue
        out.setdefault(_identity(moved, dev), tunables)
    if dropped:
        logger.info(
            "%s: %d of %d settings dropped",
            type(op).__name__,
            dropped,
            math.prod(len(d) for d in domains.values()),
        )
    return list(out.values())


def _identity(op: Operator, dev) -> str:
    return OperatorDesign(op.resolved(dev)).identity


def refusal(op: Operator, fit_cache: Path = FIT_CACHE) -> str | None:
    """Why the placer refuses ``op`` alone on a device, or None if it fits;
    kept under ``fit_cache``, keyed on its recipe.
    """
    design = OperatorDesign(op.resolved())
    record = (
        fit_cache
        / hashlib.sha256(design.compilable().recipe_hash.encode()).hexdigest()[:24]
    )
    if record.exists():
        verdict = record.read_text()
    else:
        diagnostic = fits({design.identity: design})
        verdict = "fits" if diagnostic is None else f"refused: {diagnostic}"
        write(record, verdict)
    return None if verdict == "fits" else verdict.removeprefix("refused: ")


def line(found: Sequence[dict[str, Any]], through: dict[str, Any], name: str):
    """The settings of ``found`` a coordinate descent tries for tunable
    ``name`` from ``through``: at each of its values, the setting that
    differs from ``through`` in the fewest other tunables, the first in
    ``found`` on a tie. Where tunables are coupled, a value is reached by
    moving the others with it.
    """
    at: dict[Hashable, list[dict[str, Any]]] = {}
    for s in found:
        at.setdefault(s[name], []).append(s)
    return [
        min(ss, key=lambda s: sum(s[n] != through[n] for n in s)) for ss in at.values()
    ]


@dataclasses.dataclass(frozen=True)
class Trial:
    """One setting of a shape, timed against the setting it was traced at.

    Attributes:
        tunables: The setting.
        delta_us: How much longer its steps take, summed over the shape's
            operators and weighted over their points; negative is faster.
        noise_us: The standard error of `delta_us`; None from one round.
        refused: Why it may not replace the traced setting, or None.
    """

    tunables: dict[str, Any]
    delta_us: float
    noise_us: float | None
    refused: str | None = None

    @property
    def gains(self) -> bool:
        """It may be taken: admitted, and faster beyond the noise."""
        return (
            self.refused is None
            and self.noise_us is not None
            and self.delta_us < -CONFIDENCE * self.noise_us
        )


class Shape:
    """The operators of the calls one profile entry covers: one class at one
    set of dimensions (``Profile.dims``), its probed ones aside.
    """

    def __init__(self, op: Operator):
        self.cls = type(op)
        probes = self.cls.declaration.probes
        given = {f.name: vars(op)[f.name] for f in dataclasses.fields(op)}
        self.dims = {
            k: v for k, v in Profile.dims(self.cls, given).items() if k not in probes
        }
        # Each operator, where it is timed (``Call.op_points``) and what its
        # inputs hold (``Call.op_inputs``).
        self.members: list[
            tuple[Operator, list[tuple[float, dict[str, int]]], dict[str, np.ndarray]]
        ] = []
        # Tunables any of its operators' calls give: none of them moves.
        self.pinned: frozenset[str] = frozenset()

    @property
    def key(self) -> Hashable:
        return (self.cls, tuple(self.dims.items()))

    def named(self, covering: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
        """The dimensions its entry names: those off their field's default,
        and every one an entry ``covering`` it names, so it outranks them.
        """
        defaults = Profile.dims(self.cls, {})
        names = {n for matched in covering for n in matched}
        return {
            k: v
            for k, v in self.dims.items()
            if k in names or k not in defaults or v != defaults[k]
        }

    def __str__(self) -> str:
        dims = " ".join(f"{k}={v}" for k, v in self.named(()).items())
        return f"{self.cls.__name__} {dims}".strip()


def shapes(calls: Sequence[Call], dev) -> list[Shape]:
    """The shapes of ``calls``' operators that have a tunable to search, in
    the order the calls first run them, each operator design once.
    """
    found: dict[Hashable, Shape] = {}
    seen: set[str] = set()
    for call in calls:
        for step in call.traced.steps:
            op = step.op
            shape = Shape(op)
            shape = found.setdefault(shape.key, shape)
            shape.pinned |= op.pinned
            identity = _identity(op._probed(), dev)
            if identity not in seen:
                seen.add(identity)
                shape.members.append((op, call.op_points(op), call.op_inputs(op)))
    return [s for s in found.values() if s.members[0][0].resolved(dev)._domains(dev)]


def time_shape(
    shape: Shape,
    dev,
    *,
    full_elf: bool,
    timing: Timing = Timing(),
    repeats: int = 9,
    cache: Cache | None = None,
    remeasure: bool = False,
    exhaustive: int = EXHAUSTIVE,
    fit_cache: Path = FIT_CACHE,
    cycles: Mapping[str, int] | None = None,
    log: Callable[[str], None] = print,
) -> list[Trial]:
    """Each setting of ``shape`` timed, the traced one first: every setting
    its operators share and the placer takes where there are at most
    ``exhaustive``, else those a coordinate descent tries, each tunable's
    ``line`` through the fastest setting taken so far, until a pass over the
    tunables moves it no further. A setting whose ``least_us`` at
    ``cycles`` is no faster than the fastest taken so far is not timed.
    """
    found = settings(shape.members[0][0]._probed(), dev, shape.pinned)
    for op, _, _ in shape.members[1:]:
        own = settings(op._probed(), dev, shape.pinned)
        found = [s for s in found if s in own]
    found = [found[0]] + [
        s
        for s in found[1:]
        if all(
            refusal(op._probed()._with_tunables(**s), fit_cache) is None
            for op, _, _ in shape.members
        )
    ]
    if len(found) == 1:
        return [Trial(found[0], 0.0, 0.0)]
    tried: dict[tuple, Trial] = {}
    least = (
        {_frozen(s): _least(shape, s, cycles, dev) for s in found[1:]}
        if cycles and issubclass(shape.cls, GEMM)
        else {}
    )
    traced_us: float | None = None

    def slower(s: dict[str, Any]) -> bool:
        bound = least.get(_frozen(s))
        if bound is None or traced_us is None:
            return False
        best = min((t.delta_us for t in tried.values() if t.gains), default=0.0)
        return bound >= traced_us + best

    def run(batch: list[dict[str, Any]]) -> None:
        nonlocal traced_us
        todo = [found[0]] + [
            s
            for s in batch
            if s is not found[0] and _frozen(s) not in tried and not slower(s)
        ]
        if skipped := sum(1 for s in batch if slower(s) and _frozen(s) not in tried):
            log(f"    {skipped} slower by their kernel alone, not timed")
        trials, traced_us = _time(
            shape, todo, full_elf, timing, repeats, cache, remeasure, log
        )
        for s, t in zip(todo, trials):
            tried[_frozen(s)] = t

    if len(found) <= exhaustive:
        if any(b is not None for b in least.values()):
            run([])  # the traced setting's own time, which a bound is held to
        run(found)
    else:
        best, moved = found[0], True
        while moved:
            moved = False
            for name in found[0]:
                run(line(found, best, name))
                taken = [t for t in tried.values() if t.gains or t.tunables == found[0]]
                fastest = min(taken, key=lambda t: t.delta_us)
                if fastest.tunables != best:
                    best, moved = fastest.tunables, True
    return [tried[_frozen(s)] for s in found if _frozen(s) in tried]


def _frozen(tunables: Mapping[str, Any]) -> tuple:
    return tuple(tunables.items())


def _least(shape: Shape, s: dict[str, Any], cycles, dev) -> float | None:
    """``least_us`` of ``shape`` at setting ``s``, weighted as ``_time``
    weighs its operators' steps; None where any is unknown.
    """
    total = 0.0
    for op, points, _ in shape.members:
        moved = op._probed()._with_tunables(**s).resolved(dev)
        for weight, values in points:
            bound = least_us(moved, values, cycles, dev)
            if bound is None:
                return None
            total += weight * bound
    return total


def _time(
    shape: Shape,
    found: list[dict[str, Any]],
    full_elf: bool,
    timing: Timing,
    repeats: int,
    cache: Cache | None,
    remeasure: bool,
    log: Callable[[str], None],
) -> tuple[list[Trial], float]:
    """``found``'s settings (the traced one first) timed and judged at each
    point of each of ``shape``'s operators, and the traced one's weighted
    step time; one that does not build is refused.
    """
    traced_us = 0.0
    deltas = [0.0] * len(found)
    variances: list[float | None] = [0.0] * len(found)
    refused: list[str | None] = [None] * len(found)
    for op, points, inputs in shape.members:
        ops = [op._probed()._with_tunables(**s).resolved() for s in found]
        for weight, values in points:
            ran = measure(
                ops,
                full_elf=full_elf,
                timing=timing,
                repeats=repeats,
                values=values,
                inputs=inputs,
                cache=cache,
                remeasure=remeasure,
                log=log,
            )
            default = ran[0]
            traced_us += weight * default.t_step_us
            for i in range(1, len(found)):
                if i not in ran:
                    refused[i] = refused[i] or "does not build"
                    continue
                delta, noise = ran[i].difference(default)
                deltas[i] += weight * delta
                variances[i] = (
                    None
                    if variances[i] is None or noise is None
                    else variances[i] + (weight * noise) ** 2
                )
                if refused[i] is None and ran[i].output != default.output:
                    refused[i] = _judged(ops[0], ops[i], values, inputs, full_elf)
    return [
        Trial(s, d, 0.0 if i == 0 else (None if v is None else math.sqrt(v)), r)
        for i, (s, d, v, r) in enumerate(zip(found, deltas, variances, refused))
    ], traced_us


def _judged(
    default: Operator,
    op: Operator,
    values: Mapping[str, int],
    inputs: Mapping[str, np.ndarray],
    full_elf: bool,
) -> str | None:
    """``judge`` on one run of ``op`` at ``values`` on ``inputs``."""
    run = Standalone(
        f"judge_{_identity(op, op.dev)}",
        [op],
        values={op: values},
        inputs={op: inputs},
        full_elf=full_elf,
    )
    run.digest()
    return judge(default, op, run.inputs(), run.written(), values)


def autotune(
    calls: Sequence[Call],
    dev,
    profile: Profile | None = None,
    *,
    full_elf: bool,
    timing: Timing = Timing(),
    repeats: int = 9,
    cache: Cache | None = None,
    remeasure: bool = False,
    cycles: Mapping[str, int] | None = None,
    log: Callable[[str], None] = print,
) -> Profile:
    """``profile`` with an entry for each shape of ``calls`` (``shapes``)
    naming the fastest setting taken (``time_shape``), the traced one where
    none gains. Its entries covering any of those shapes are replaced; the
    rest are kept.

    Args:
        calls: The calls whose graphs were traced under ``profile``.
        full_elf: How the calls' graphs are packaged.
        cache: Where each time is kept across runs (``Cache.here()``).
        remeasure: Time again what ``cache`` holds.
        cycles: Kernel cycles per call by build key (``kernel_cycles``).
    """
    found = shapes(calls, dev)
    covering: dict[Hashable, list[Mapping[str, Any]]] = {s.key: [] for s in found}
    out = Profile()
    for cls, matched, tunables in profile or ():
        covered = [
            s
            for s in found
            if issubclass(s.cls, cls) and Profile.matches(matched, s.dims)
        ]
        for s in covered:
            covering[s.key].append(matched)
        if not covered:
            out.add(cls, **matched, **tunables)
    for i, shape in enumerate(found):
        log(f"[{i + 1}/{len(found)}] {shape}")
        tried = time_shape(
            shape,
            dev,
            full_elf=full_elf,
            timing=timing,
            repeats=repeats,
            cache=cache,
            remeasure=remeasure,
            cycles=cycles,
            log=log,
        )
        gains = [t for t in tried if t.gains]
        best = min(gains, key=lambda t: t.delta_us, default=tried[0])
        if gains:
            log(f"    {best.tunables}: {best.delta_us:+.1f} ± {best.noise_us:.1f} us")
        out.add(shape.cls, **shape.named(covering[shape.key]), **best.tunables)
    return out
