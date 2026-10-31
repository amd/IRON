# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What bounds each version of a graph, before a tune decides what to
search: each design's standalone time and the weight bytes it reads, the
switches between configurations as the cost model prices them, and an
estimate of what each transform could remove, with its basis.
"""

from __future__ import annotations

import collections
import dataclasses
from collections.abc import Callable, Hashable, Mapping, Sequence, Set

from aie.utils import coded
from aie.utils.compile.jit.params import OperatorParam

from iron.common.declare import Operator, Profile
from iron.common.design import OperatorDesign
from iron.common.graph.compiled import apply_profile
from iron.operators.gemm import GEMM
from .autotune import Shape, Timed, least_us
from .costmodel import CostModel
from .fold import array_scoped_fold_candidates
from .measure import Cache, Timing, measure
from .packings import design_cores

# A design reading weights at this share of the version's fastest read rate
# is bound by it; one whose kernel bound is this share of its time, by compute.
BOUND_SHARE = 0.7

# The designs a survey's report lists, the costliest first.
TOP_DESIGNS = 6


@dataclasses.dataclass(frozen=True)
class Design:
    """One design of a version, over every step that runs it.

    Attributes:
        name: Its class and the dimensions its shape names.
        shape: Its shape's ``Shape.key``, a tunable entry's unit.
        steps: How many steps run it.
        us: Its steps' standalone time per call, weighted over the points.
        weight_bytes: The weight bytes its steps read per call.
        kernel_us: Its steps' kernel-cycle bound per call, where one is known.
        bound: ``"weight-read"``, ``"compute"`` or ``"other"``.
    """

    name: str
    shape: Hashable
    steps: int
    us: float
    weight_bytes: int
    kernel_us: float | None
    bound: str


@dataclasses.dataclass(frozen=True)
class Estimate:
    """What a transform could remove from a version, and why that much."""

    us: float
    basis: str


@dataclasses.dataclass(frozen=True)
class Survey:
    """One version: its designs, its switches and the estimates."""

    name: str
    designs: tuple[Design, ...]
    switches: int
    switch_us: float
    estimates: Mapping[str, Estimate]

    @property
    def steps_us(self) -> float:
        return sum(d.us for d in self.designs)

    def shares(self) -> dict[Hashable, float]:
        """Each shape's share of the version's time, its designs together."""
        total = self.steps_us + self.switch_us
        out: dict[Hashable, float] = collections.defaultdict(float)
        for d in self.designs:
            out[d.shape] += d.us / total
        return dict(out)

    def lines(self) -> list[str]:
        total = self.steps_us + self.switch_us
        out = [
            f"{self.name}: {self.steps_us:.0f} us of steps + {self.switch_us:.0f} us "
            f"of {self.switches} switches"
        ]
        bound: dict[str, float] = collections.defaultdict(float)
        for d in self.designs:
            bound[d.bound] += d.us
        out += [
            f"  {kind}: {us:.0f} us ({100 * us / total:.0f}%)"
            for kind, us in bound.items()
        ]
        out += [
            f"    {d.name} x{d.steps}: {d.us:.0f} us ({d.bound})"
            for d in sorted(self.designs, key=lambda d: -d.us)[:TOP_DESIGNS]
        ]
        out += [
            f"  {name}: up to {e.us:.0f} us ({e.basis})"
            for name, e in sorted(self.estimates.items(), key=lambda kv: -kv[1].us)
        ]
        return out


def survey(
    call: Timed,
    profile: Profile,
    dev,
    times: Mapping[str, float],
    model: CostModel,
    codable: Set[Hashable] = frozenset(),
    cycles: Mapping[str, int] | None = None,
    core_mhz: float | None = None,
) -> Survey:
    """``call``'s version as ``profile`` builds it, surveyed from ``times``,
    each design's standalone step time by its name (``step_times``).

    Args:
        codable: The shapes (``Shape.key``) ``plan.coded_seed`` would code.
        cycles: Kernel cycles per call (``kernel_cycles``), for GEMM's bound.
        core_mhz: The clock ``cycles`` are timed at.
    """
    recording, fused, packing = apply_profile(call.recording, profile, dev)
    inside = {i: f for f in fused for i in f.steps}
    shapes: dict[str, Shape] = {}
    counts: collections.Counter[str] = collections.Counter()
    weights: collections.Counter[str] = collections.Counter()
    kernels: dict[str, float] = collections.defaultdict(float)
    ops: dict[str, Operator] = {}
    config: list[Hashable] = []
    members: dict[Hashable, dict[str, Operator]] = {}
    for i, step in enumerate(recording.steps):
        op = step.op.resolved(dev)
        name = OperatorDesign(op).name
        shapes.setdefault(name, Shape(step.op))
        ops.setdefault(name, op)
        counts[name] += 1
        read = sum(h.nbytes for h in step.slots if h.role == "weight")
        # A gather, or any data mover, reads no more of a weight than it writes.
        if step.gather is not None or op.ops() == 0:
            read = min(read, sum(b.nbytes for b in op.outputs))
        weights[name] += read
        if isinstance(op, GEMM) and cycles and core_mhz:
            bound = least_us(op, call.op_values(step.op), cycles, core_mhz)
            kernels[name] += bound or 0.0
        unit = inside[i] if i in inside else packing.group_of(name)
        config.append(unit)
        members.setdefault(unit, {})[name] = op
    ceiling = max(
        (weights[n] / times[n] for n in counts if weights[n] and times[n] > 0),
        default=0.0,
    )
    designs = []
    coded_us = 0.0
    for name, op in ops.items():
        us, weight, kernel = times[name], weights[name], kernels[name]
        if ceiling and weight and weight / us >= BOUND_SHARE * ceiling:
            bound = "weight-read"
        elif kernel and kernel >= BOUND_SHARE * us:
            bound = "compute"
        else:
            bound = "other"
        if bound == "weight-read" and shapes[name].key in codable:
            for b in op.inputs:
                flag = b.declared_coded
                if isinstance(flag, OperatorParam) and not vars(op)[flag.name]:
                    K = b.logical_shape[-1]
                    coded_us += us * (1 - coded.row_bytes(K, b.capacity) / (2 * K))
        designs.append(
            Design(
                str(shapes[name]),
                shapes[name].key,
                counts[name],
                us,
                weight,
                kernel or None,
                bound,
            )
        )
    # Designs sharing an array share its cores.
    cores = {
        unit: sum(
            design_cores(op)
            for op in {op.array_key(): op for op in held.values()}.values()
        )
        for unit, held in members.items()
    }
    entered = [b for a, b in zip(config, config[1:]) if a != b]
    switch_us = model.predict(
        {
            "switches": len(entered),
            "switch_cores": sum(cores[u] for u in entered),
            "packed_steps": sum(1 for u in config if len(members[u]) > 1),
        }
    )
    folded = [
        OperatorDesign(call.recording.steps[i].op.resolved(dev)).name
        for f in array_scoped_fold_candidates(call.recording)
        for i in f.steps[1:]
    ]
    fold_us = sum(times[n] / counts[n] for n in folded if n in counts)
    estimates = {
        "coded": Estimate(
            coded_us, "read-bound GEMVs' time times the bytes coding saves"
        ),
        "packing": Estimate(
            switch_us, f"the cost model's price of {len(entered)} switches"
        ),
        "folds": Estimate(fold_us, f"the {len(folded)} steps a fold removes"),
    }
    inputs = ", ".join(f"{n}{list(s)}" for n, s, _ in recording.version)
    return Survey(
        f"{recording.name} ({inputs or 'no inputs'})",
        tuple(designs),
        len(entered),
        switch_us,
        estimates,
    )


def step_times(
    call: Timed,
    profile: Profile,
    dev,
    *,
    full_elf: bool,
    timing: Timing,
    repeats: int,
    cache: Cache | None,
    log: Callable[[str], None] = print,
    lock: bool = False,
) -> dict[str, float]:
    """Each design of ``call``'s version under ``profile``, by name: its
    standalone step time summed over the steps running it, weighted over the
    call's points (``measure``, cached)."""
    recording, _, _ = apply_profile(call.recording, profile, dev)
    out: dict[str, float] = collections.defaultdict(float)
    for step in recording.steps:
        op = step.op.resolved(dev)
        name = OperatorDesign(op).name
        for weight, values in call.op_points(step.op):
            ran = measure(
                [op],
                full_elf=full_elf,
                timing=timing,
                repeats=repeats,
                values=values,
                inputs=call.op_inputs(step.op),
                cache=cache,
                log=log,
                lock=lock,
            )
            out[name] += weight * ran[0].t_step_us
    return dict(out)
