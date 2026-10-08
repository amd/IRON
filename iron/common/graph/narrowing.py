# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Joint narrowing: each design's tunables (``Operator.domains``: its width,
narrower or wider than its default, and any other its operator searches)
and which designs share a device, chosen together to minimise the modelled
time of a full-ELF runlist:

    D0 + sum over steps of t_step
       + sum over device entries of (base + sum over its members of load)
       + R if the entries are odd

A device is entered at a step whose design is in it when the step before is
not; entering configures it. The designs of one array share a device
(``Packing.sharing``) that loads the array once, so the search takes them
as one, at one setting. ``R`` is the empty configure the parity rule
adds (``Fusion.needs_reset``). ``t_step`` and ``load`` are measured per
design and setting, ``D0``, ``base`` and ``R`` per device (``probe``, into a
``CostTable``). A pack the table holds measured as one (``CostTable.packs``)
is priced as measured instead: its entry, and each member's step on it.

Only a pack connected in the runlist's adjacency can save an entry, so the
candidates are the connected sets of designs, and an exact search over
partitions into them, carrying the parity, finds the cheapest. The placer
(``fits``) is asked only about the packs a solution uses; a refused pack
tries its next-cheapest settings, then is dropped, and the search reruns.

A setting is a candidate only if it was measured accurate: its output
bit-identical to the default's, or within the gate of the default and its
own. A design the table does not hold stays at its default, alone in its
device.

A design whose work follows a per-call value (a bound extent: attention
over the context so far) is priced at the calls' operating points where
the table holds them (``StepCost.points``): ``t_step`` is their weighted
mean, a pack's step moves with it, and a setting is a candidate only if
accurate at each.

An xclbin chain (a ``"separate"`` table) is a dispatch per step and a
kernel per design, so nothing packs and the designs of one array are not
tied:

    F + sum over steps of c + sum over switches of L(incoming design)

counting the switches cyclically, as a decode loop calls the version back
to back. ``c`` is a step dispatched alone, ``L`` a design's load, ``F`` the
rest of a call. The switches follow from the runlist alone, so each design
takes the setting minimising its occurrences times ``c`` plus its arrivals
times ``L``, independently of the others.

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
import math
import os
import statistics
from collections import Counter
from collections.abc import Hashable, Iterable, Iterator, Mapping, Sequence
from pathlib import Path
from typing import Any

import numpy as np
from aie.dialects.aie import WireBundle, get_target_model
from aie.utils.compile import NPU_CACHE_HOME

from ..declare import Operator
from ..design import OperatorDesign, runtime
from ..image.coresidence import Packing, fits
from ..image.fusion import generate, parameters_preamble
from .fold import FOLD_RUNS, Folding, Made, folded, foldings
from .trace import TracedGraph


def cost_key(op: Operator, dev=None) -> str:
    """A design's class and identity, resolved for ``dev``, as the fused
    image names it, at its probe (``Operator.probed``): the designs that
    differ only in fields their cost cannot follow share one key. The key
    leaves out the sources, so remeasure after editing how a design is
    generated.
    """
    design = OperatorDesign(op.probed().resolved(dev))
    return f"{type(op).__name__}_{design.identity}"


def cost_keys(traced: TracedGraph, dev, keyed: dict[int, str]) -> list[str]:
    """Each step's ``cost_key``, kept in ``keyed`` by its operator's ``id``:
    the caller holds every operator ``keyed`` names, so an id stays its own.
    """
    for s in traced.steps:
        if id(s.op) not in keyed:
            keyed[id(s.op)] = cost_key(s.op, dev)
    return [keyed[id(s.op)] for s in traced.steps]


@dataclasses.dataclass(frozen=True, eq=False)
class Variant:
    """One setting of a design's searched tunables, its array and the shim
    channels its streams take.
    """

    op: Operator
    resolved: Operator
    tunables: tuple[tuple[str, Any], ...]
    key: str
    array: Hashable
    mm2s: int
    s2mm: int

    @classmethod
    def of(cls, op: Operator, dev) -> Variant:
        resolved = op.resolved(dev)
        streams = [b for b in resolved.buffers if b.streamed]
        return cls(
            op=op,
            resolved=resolved,
            tunables=tuple(
                (name, getattr(resolved, name)) for name in resolved.domains(dev)
            ),
            key=cost_key(resolved, dev),
            array=resolved.array_key(),
            mm2s=sum(s.count for s in streams if not s.direction.drains),
            s2mm=sum(s.count for s in streams if s.direction.drains),
        )


def variants(op: Operator, dev, pinned: frozenset[str] = frozenset()) -> list[Variant]:
    """``op`` at its default tunables, then at every other combination of
    their ``Operator.domains`` it resolves at and whose derived transfers
    fit their descriptors.

    Args:
        op: The operator.
        dev: The device it is resolved against.
        pinned: Tunables another operator of its design pins, held at the
            value ``op`` resolves them to.
    """
    if pinned - op.pinned:
        resolved = op.resolved(dev)
        op = dataclasses.replace(
            op,
            pinned=op.pinned | pinned,
            **{name: getattr(resolved, name) for name in pinned - op.pinned},
        )
    default = Variant.of(op, dev)
    defaults = dict(default.tunables)
    out = [default]
    domains = default.resolved.domains(dev)
    for combo in itertools.product(*domains.values()):
        tunables = dict(zip(domains, combo))
        if tunables == defaults:
            continue
        try:
            variant = Variant.of(op.with_tunables(**tunables), dev)
            resolved = variant.resolved
            if not resolved.has_sequence_override():
                for buf in resolved.buffers:
                    runtime.Sequence(resolved, {}).plan(buf)
        except ValueError:  # unresolvable, incompatible or untransferable here
            continue
        out.append(variant)
    return out


FIT_CACHE = Path(NPU_CACHE_HOME) / "iron" / "fits"

# Standard errors a setting's step must beat its default's by to be taken.
CONFIDENCE = 2.0

# The packagings a table is measured under (``packaging.plan``'s dispatch).
DISPATCHES = ("fused", "separate")


def fit_verdict(
    designs: Mapping[str, OperatorDesign], fit_cache: Path = FIT_CACHE
) -> str | None:
    """Why the placer refuses ``designs`` on one device, or None if they fit.

    A design that cannot be generated is refused with the generator's error.
    The verdict is kept under ``fit_cache``, keyed on the designs' recipes,
    so it is reused exactly when the build would be.

    Args:
        designs: The designs, by the name each takes in the device.
        fit_cache: Where the verdicts persist across processes.
    """
    record = _fit_record(designs, fit_cache)
    if record.exists():
        verdict = record.read_text()
    else:
        texts, params = {}, {}
        try:
            for name, design in designs.items():
                generated = generate(design)
                texts[name] = str(generated.device)
                params.update(generated.parameters)
            diagnostic = fits(texts, parameters_preamble(params))
        except ValueError as e:
            diagnostic = str(e)
        verdict = "fits" if diagnostic is None else f"refused: {diagnostic}"
        _write(record, verdict)
    return None if verdict == "fits" else verdict.removeprefix("refused: ")


def refuse(
    designs: Mapping[str, OperatorDesign], why: str, fit_cache: Path = FIT_CACHE
) -> None:
    """Record that ``designs`` do not build on one device, which the placer
    passed, so ``fit_verdict`` refuses them from now on.
    """
    _write(_fit_record(designs, fit_cache), f"refused: {why}")


def _fit_record(designs: Mapping[str, OperatorDesign], fit_cache: Path) -> Path:
    """The file holding the verdict on ``designs``, keyed on their recipes."""
    h = hashlib.sha256(
        repr(sorted(d.compilable().recipe_hash for d in designs.values())).encode()
    )
    return fit_cache / h.hexdigest()[:24]


def _write(record: Path, verdict: str) -> None:
    """Write ``verdict`` to ``record`` whole, as another process may read it."""
    record.parent.mkdir(parents=True, exist_ok=True)
    partial = record.with_suffix(f".{os.getpid()}")
    partial.write_text(verdict)
    partial.replace(record)


def fitting(
    found: Sequence[Variant], fit_cache: Path = FIT_CACHE
) -> tuple[list[Variant], dict[str, str]]:
    """The settings of ``found`` the placer takes alone on a device, the
    default always among them, and why it refuses each other, by key.
    """
    kept, refused = [found[0]], {}
    for v in found[1:]:
        diagnostic = fit_verdict({v.key: OperatorDesign(v.resolved)}, fit_cache)
        if diagnostic is None:
            kept.append(v)
        else:
            refused[v.key] = diagnostic
    return kept, refused


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
class PointCost:
    """One design at one setting, stepped at one of its operating points:
    per-call values that change its work, as a long context does attention's.

    Attributes:
        weight: The share of the calls priced that run at this point.
        t_step_us: Its time per step there: its ``StepCost.t_step_us`` plus
            how much longer a step there took than one at the call's own
            values, the two run interleaved.
        noise_us: The standard error of that shift, paired round by round;
            None from a single round.
        exact: Its output there is bit-identical to the default setting's.
        accurate: Exact, or judged within the default's gate and its own.
        calls: The runs a round timed, fewer where a run is long.
    """

    weight: float
    t_step_us: float
    noise_us: float | None
    exact: bool
    accurate: bool
    calls: int


@dataclasses.dataclass(frozen=True)
class StepCost:
    """One design at one setting of its tunables, measured alone.

    Attributes:
        t_step_us: Its time per step while its device is configured, at the
            per-call values of the call it is measured in; on an xclbin
            chain, `c`, a step dispatched alone.
        noise_us: The standard error it is compared to its design's default
            by: on the default's own row, of `t_step_us`; on any other, of
            its difference from the default, paired round by round in the
            run that timed both (through its twin's where it has one).
            None from a single round.
        alone_us: One run of one step, less `t_step_us`: `D0 + base + load + R`;
            on an xclbin chain, `F`.
        exact: Its output is bit-identical to the default setting's.
        accurate: It may replace the default: exact, or judged within the
            default's gate and its own (``probe.judge``).
        beside: The key of the design it was run beside, alternating each
            step; None on that design's own row.
        pair_us: The entries of the two, `E(beside) + E`, where a design's
            entry `E` is `base + load` (on an xclbin chain, `L`).
        points: Where the calls priced run it at more than one point, each
            by the bound extents it writes there (``"kv_valid=1024"``).
    """

    t_step_us: float
    noise_us: float | None
    alone_us: float
    exact: bool
    accurate: bool
    pmode: str
    rounds: int
    calls: int
    measured: str  # ISO date
    beside: str | None = None
    pair_us: float | None = None
    points: dict[str, PointCost] | None = None

    @classmethod
    def of(cls, row: Mapping[str, Any]) -> StepCost:
        """The cost a table's JSON row holds."""
        points = row.get("points")
        if points is None:
            return cls(**row)
        return cls(**{**row, "points": {k: PointCost(**p) for k, p in points.items()}})

    @property
    def expected_us(self) -> float:
        """Its step at the calls priced: its points' times by their weights,
        else `t_step_us`.
        """
        if not self.points:
            return self.t_step_us
        points = self.points.values()
        return sum(p.weight * p.t_step_us for p in points) / sum(
            p.weight for p in points
        )

    @property
    def admitted(self) -> bool:
        """It may replace the default at every point it is priced at."""
        return self.accurate and all(p.accurate for p in (self.points or {}).values())


@dataclasses.dataclass(frozen=True)
class Calibration:
    """A configure's cost split, measured on one pair of designs.

    Attributes:
        dispatch_us: `D0`; on an xclbin chain, `F`.
        reset_us: `R`, the empty configure; 0 on an xclbin chain.
        base_us: The part of a configure no design accounts for; 0 on an
            xclbin chain.
        switch_us: The pair's mean entry, `(E(a) + E(b)) / 2`; on an xclbin
            chain, its mean load.
    """

    dispatch_us: float
    reset_us: float
    base_us: float
    switch_us: float
    pmode: str
    rounds: int
    calls: int
    measured: str


@dataclasses.dataclass(frozen=True)
class PackCost:
    """Designs sharing one device on a full ELF, measured as that device.

    Attributes:
        beside: The key of the design it was run beside, alternating.
        pair_us: The entries of the two, `E(beside) + E`, where the pack's
            entry `E` is its base and every member's load.
        t_step_us: Each member's time per step on the device, by its key.
    """

    beside: str
    pair_us: float
    t_step_us: dict[str, float]
    pmode: str
    rounds: int
    calls: int
    measured: str


class CostTable:
    """Measured step and configure costs for one device and one packaging,
    as JSON on disk.

    ``steps`` is keyed by ``cost_key``, ``calibrations`` by the pair of keys
    measured, ``packs`` by ``pack_name``; the model takes the median of each
    calibrated figure.

    Args:
        path: The JSON file; read if it exists.
        device: The device's name (``dev.name``) it is measured on.
        dispatch: The packaging it is measured under: ``"fused"`` (one full
            ELF) or ``"separate"`` (an xclbin dispatch per step).

    Raises:
        ValueError: The file was measured for another device or packaging
            than the one given.
    """

    def __init__(
        self, path: Path | str, device: str | None = None, dispatch: str | None = None
    ):
        if dispatch not in (None, *DISPATCHES):
            raise ValueError(f"dispatch must be one of {DISPATCHES}, got {dispatch!r}")
        self.path = Path(path)
        self.device = device
        self.dispatch = dispatch
        self.steps: dict[str, StepCost] = {}
        self.calibrations: dict[str, Calibration] = {}
        self.packs: dict[str, PackCost] = {}
        self._medians: dict[str, float] | None = None
        self._entry_costs: dict[str, float | None] | None = None
        if self.path.exists():
            data = json.loads(self.path.read_text())
            for name in ("device", "dispatch"):
                given = vars(self)[name]
                if given is not None and given != data[name]:
                    raise ValueError(
                        f"{self.path} is measured for {name} {data[name]!r}, "
                        f"not {given!r}"
                    )
            self.device, self.dispatch = data["device"], data["dispatch"]
            # An entry recorded without a field its kind now requires is
            # left out, so it is measured again.
            for name, kind in (
                ("steps", StepCost),
                ("calibrations", Calibration),
                ("packs", PackCost),
            ):
                required = {
                    f.name
                    for f in dataclasses.fields(kind)
                    if f.default is dataclasses.MISSING
                }
                setattr(
                    self,
                    name,
                    {
                        k: StepCost.of(v) if kind is StepCost else kind(**v)
                        for k, v in data.get(name, {}).items()
                        if required <= v.keys()
                    },
                )

    def measures(self, dev) -> None:
        """Check that this table is measured on ``dev``.

        Raises:
            ValueError: It is for another device, or names none.
        """
        if self.device is None or self.dispatch is None:
            raise ValueError(f"{self.path}: give the table its device and dispatch")
        if self.device != dev.name:
            raise ValueError(
                f"{self.path} is measured on {self.device}, not {dev.name}"
            )

    def save(self) -> None:
        if self.device is None or self.dispatch is None:
            raise ValueError(f"{self.path}: give the table its device and dispatch")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        sections = [
            f'"device": {json.dumps(self.device)}',
            f'"dispatch": {json.dumps(self.dispatch)}',
        ]
        sectioned = [("steps", self.steps), ("calibrations", self.calibrations)]
        if self.packs:
            sectioned.append(("packs", self.packs))
        for name, table in sectioned:
            rows = []
            for k, v in sorted(table.items()):
                row = dataclasses.asdict(v)
                # A field left at its default None is left out; a required one is kept.
                kept = {
                    f.name: row[f.name]
                    for f in dataclasses.fields(v)
                    if row[f.name] is not None or f.default is dataclasses.MISSING
                }
                rows.append(f"{json.dumps(k)}: {json.dumps(kept)}")
            sections.append(f'"{name}": {{\n  ' + ",\n  ".join(rows) + "\n}")
        self.path.write_text("{" + ",\n".join(sections) + "}\n")

    @property
    def pmode(self) -> str | None:
        """The power mode its entries are measured at; None if it has none."""
        modes = {
            c.pmode
            for entries in (self.steps, self.calibrations, self.packs)
            for c in entries.values()
        }
        if len(modes) > 1:
            raise ValueError(
                f"{self.path} mixes power modes {sorted(modes)}: measure it "
                f"again (remeasure)"
            )
        return next(iter(modes), None)

    def measures_at(self, pmode: str) -> None:
        """Check that an entry measured at power mode ``pmode`` may join
        this table: its entries are at that mode, or it has none.

        Raises:
            ValueError: They are at another.
        """
        if self.pmode not in (None, pmode):
            raise ValueError(
                f"{self.path} is measured at power mode {self.pmode}, not "
                f"{pmode}: set the NPU's back, or measure the table again "
                f"(remeasure)"
            )

    def record_step(self, key: str, cost: StepCost) -> None:
        self.measures_at(cost.pmode)
        self.steps[key] = cost

    def record_calibration(self, pair: tuple[str, str], cal: Calibration) -> None:
        self.measures_at(cal.pmode)
        self.calibrations["|".join(pair)] = cal
        self._medians = None
        self._entry_costs = None

    def record_pack(self, keys: Iterable[str], cost: PackCost) -> None:
        self.measures_at(cost.pmode)
        self.packs[self.pack_name(keys)] = cost

    def pack_entry(self, name: str) -> float:
        """One entry into the device ``packs`` holds as ``name``: its pair's
        entries less that of the design it was run beside.
        """
        pack = self.packs[name]
        return pack.pair_us - self.load(pack.beside) - self.base_us

    @staticmethod
    def pack_name(keys: Iterable[str]) -> str:
        """The name ``packs`` holds the designs of ``keys`` under, in any order."""
        return "|".join(sorted(set(keys)))

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
        """A design's step at the calls priced (``StepCost.expected_us``);
        0 if unmeasured.
        """
        cost = self.steps.get(key)
        return 0.0 if cost is None else cost.expected_us

    def pack_step(self, name: str, key: str) -> float:
        """A member's step on the device ``packs`` holds as ``name``, at the
        calls priced: its step there, measured at its call's values, moved
        as its own step moves from those to its points.
        """
        cost = self.steps[key]
        return self.packs[name].t_step_us[key] + cost.expected_us - cost.t_step_us

    def step_against(self, key: str, default: str, confidence: float) -> float:
        """Setting ``key``'s step time at the calls priced (``t_step``) as a
        choice against its design's ``default``, which is priced at the same
        points: the default's where ``key`` is faster by less than
        ``confidence`` standard errors of their difference, or by any
        amount where that is unknown. A win within the noise is not one.
        """
        t, d = self.steps.get(key), self.steps.get(default)
        if key == default or t is None or d is None:
            return self.t_step(key)
        points = t.points or {}
        total = sum(p.weight for p in points.values())
        # The difference at each point is the one at the call's values plus
        # the two settings' shifts there, each measured on its own.
        noises = [(1.0, t.noise_us)] + [
            (p.weight / total, noise)
            for label, p in points.items()
            for noise in (p.noise_us, d.points[label].noise_us)
        ]
        noise = (
            None
            if any(n is None for _, n in noises)
            else math.sqrt(sum((w * n) ** 2 for w, n in noises))
        )
        if noise is None or t.expected_us >= d.expected_us - confidence * noise:
            return max(t.expected_us, d.expected_us)
        return t.expected_us

    def load(self, key: str) -> float:
        """What configuring a design adds to an entry's base; 0 if unmeasured.

        It is the design's entry `E = base + load` less the base (on an
        xclbin chain, `L`, its load on a switch into it): `E` solved from
        the calibrations where a pair names the design, else its pair's
        entries less that of the design it was run beside.

        Raises:
            ValueError: The measurements do not determine it.
        """
        solved = self.entry_costs()
        if key in solved:
            if solved[key] is None:
                raise ValueError(
                    f"{self.path}: the calibration pairs do not determine the load "
                    f"of {key}; pairs closing an odd cycle, a triangle, would"
                )
            return solved[key] - self.base_us
        cost = self.steps.get(key)
        if cost is None:
            return 0.0
        if cost.beside is None:
            raise ValueError(
                f"{self.path}: the load of {key} is measured neither beside "
                f"another design nor in a calibration pair"
            )
        if cost.beside not in solved and cost.beside not in self.steps:
            raise ValueError(
                f"{self.path}: the load of {key} is measured beside "
                f"{cost.beside}, whose own load is not"
            )
        return cost.pair_us - self.load(cost.beside) - 2 * self.base_us

    def entry_costs(self) -> dict[str, float | None]:
        """Each design a calibration pair names, by its entry `E` solved
        from the pairs' mean entries, `s(a, b) = (E(a) + E(b)) / 2`, by least
        squares; None where the pairs do not determine it (a pair alone, or
        pairs closing no odd cycle).
        """
        if self._entry_costs is None:
            pairs = [(k.split("|"), c.switch_us) for k, c in self.calibrations.items()]
            names = list(dict.fromkeys(n for pair, _ in pairs for n in pair))
            index = {n: i for i, n in enumerate(names)}
            halves = np.zeros((len(pairs), len(names)))
            for row, (pair, _) in enumerate(pairs):
                for n in pair:
                    halves[row, index[n]] += 0.5
            switches = np.array([s for _, s in pairs])
            solved = np.linalg.lstsq(halves, switches, rcond=None)[0]
            # A load is determined where its unit vector is in the row space.
            free = np.eye(len(names)) - np.linalg.pinv(halves) @ halves
            self._entry_costs = {
                n: None if np.abs(free[i]).max() > 1e-9 else float(solved[i])
                for n, i in index.items()
            }
        return self._entry_costs

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

    def switches(self) -> Counter:
        """How often each design follows another, the last step wrapping to
        the first: a runlist called back to back.
        """
        return Counter(
            k
            for previous, k in zip(self.keys[-1:] + self.keys[:-1], self.keys)
            if previous != k
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
    A device whose designs at their settings the table holds as a pack
    costs that pack's entry and its members' steps on it.

    Args:
        table: The measured costs.
        keys: The runlist's design keys.
        groups: The designs sharing a device; none on an xclbin chain.
        chosen: Each design's key at the setting it runs at.
        arrays: Each design's array at that setting: the designs of one array
            share a device too, which loads the array once. An xclbin chain
            loads each design of its own.

    Returns:
        `(time_us, configures)`, the reset included; on an xclbin chain,
        `configures` counts the switches.

    Raises:
        ValueError: `groups` are given for an xclbin chain.
    """
    chosen = chosen or {}
    arrays = arrays or {}
    if table.dispatch == "separate":
        if groups:
            raise ValueError("an xclbin chain loads each design alone; it packs none")
        runlist = Runlist(keys)
        switches = runlist.switches()
        total = table.dispatch_us + sum(
            n * table.t_step(chosen.get(k, k)) for k, n in runlist.occurrences.items()
        )
        total += sum(n * table.load(chosen.get(k, k)) for k, n in switches.items())
        return total, sum(switches.values())
    order = list(dict.fromkeys(keys))
    packing = Packing(tuple(map(tuple, groups))).sharing(
        {k: arrays.get(k, k) for k in order}
    )
    members = packing.devices(order)
    names = {
        here: table.pack_name(chosen.get(m, m) for m in designs)
        for here, designs in members.items()
    }
    total = table.dispatch_us
    entries = 0
    previous = None
    for k in keys:
        here = packing.device_of(k)
        pack = table.packs.get(names[here])
        key = chosen.get(k, k)
        total += (
            table.t_step(key) if pack is None else table.pack_step(names[here], key)
        )
        if here != previous:
            entries += 1
            if pack is None:
                loads: dict[Hashable, float] = {}
                for m in members[here]:
                    loads.setdefault(arrays.get(m, m), table.load(chosen.get(m, m)))
                total += table.base_us + sum(loads.values())
            else:
                total += table.pack_entry(names[here])
            previous = here
    if entries % 2:
        total += table.reset_us
        entries += 1
    return total, entries


@dataclasses.dataclass
class Tuning:
    """What ``JointNarrowing`` chose, and the model's prediction for it and
    for the graph as traced (``baseline``). The predictions leave out the
    ``unmeasured`` designs, which stay as traced, and the ``unpriced`` folds,
    which a design the table lacks keeps from being taken. ``chosen`` and
    ``groups`` name the designs of the graph with ``folds`` applied;
    ``inexact`` those whose setting was judged within their gates rather
    than found bit-identical to their default.
    """

    chosen: dict[str, Variant]  # default key -> the setting it runs at
    # Default keys sharing one device, an array's first design standing for
    # the array: the fusion adds its other designs.
    groups: tuple[tuple[str, ...], ...]
    # The setting keys of each device holding more than one design, array
    # mates included: what ``CostTable.packs`` would price.
    devices: tuple[tuple[str, ...], ...]
    configures: int
    predicted_us: float
    baseline_configures: int
    baseline_us: float
    unmeasured: tuple[str, ...]
    inexact: tuple[str, ...] = ()
    folds: tuple[Folding, ...] = ()
    unpriced: tuple[Folding, ...] = ()

    def apply(
        self, traced: TracedGraph, dev=None
    ) -> tuple[TracedGraph, list[list[Operator]]]:
        """``traced`` with the chosen folds applied, every narrowed design's
        operators rebuilt at their setting, and the packs as operator groups
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
                held = variant.op.pinned - op.pinned
                replace[id(op)] = op.with_tunables(
                    **dict(variant.tunables),
                    **{name: getattr(variant.resolved, name) for name in held},
                )
        narrowed = traced.with_operators(replace)
        members: dict[str, list[Operator]] = {}
        for old, new in zip(traced.steps, narrowed.steps):
            ops = members.setdefault(keys[id(old.op)], [])
            if all(o is not new.op for o in ops):
                ops.append(new.op)
        groups = [[op for key in group for op in members[key]] for group in self.groups]
        return narrowed, groups

    def report(self, names: Mapping[str, str] | None = None) -> str:
        """One line per fold and design that changed, the predictions, then
        one per design and fold the table could not price.
        """
        names = names or {}
        lines = [f"  fold: {fold}" for fold in self.folds]
        for key, v in self.chosen.items():
            if v.key != key:
                note = " (within its gates, not exact)" if key in self.inexact else ""
                lines.append(f"  {names.get(key, key)}: {dict(v.tunables)}{note}")
        for group in self.groups:
            lines.append("  pack: " + ", ".join(names.get(k, k) for k in group))
        lines.append(
            f"  model: {self.baseline_us:.1f} us ({self.baseline_configures} "
            f"configures) -> {self.predicted_us:.1f} us ({self.configures})"
        )
        lines += [
            f"  unmeasured, left as traced: {names.get(k, k)}" for k in self.unmeasured
        ]
        lines += [f"  unpriced, not taken: fold {fold}" for fold in self.unpriced]
        return "\n".join(lines)


@dataclasses.dataclass
class _Pack:
    """A candidate device: a connected set of designs, its entries, and its
    cheapest settings within the shim budget; the search prices ``options[0]``.
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
    """Choose tunables and packs for a traced graph; pass as ``coresident=``
    to ``Graph.compile``.

    Attributes:
        table: The measured costs.
        max_members: The most designs in one pack.
        fit_attempts: How many of a pack's cheapest settings the placer is
            asked about before the pack is dropped.
        fit_cache: Where the placer's verdicts persist across processes.
        fold_runs: The most ``folded`` runs ``foldings`` makes to find
            each way to fold a graph; past it the folds found are taken
            greedily.
        confidence: How many standard errors of the difference a setting's
            step must beat its default's by to be taken
            (``CostTable.step_against``).
    """

    table: CostTable = dataclasses.field(compare=False)
    max_members: int = 8
    fit_attempts: int = 3
    fit_cache: Path = dataclasses.field(default=FIT_CACHE, compare=False)
    fold_runs: int = FOLD_RUNS
    confidence: float = CONFIDENCE

    def tune(self, traced: TracedGraph, dev, dispatch: str) -> Tuning:
        """Choose the folds, tunables and packs of ``traced`` for ``dev``,
        packaged as ``dispatch`` (``packaging.plan``'s).

        Each way the graph folds (``foldings``) is priced and the cheapest
        taken. Where ``fold_runs`` do not find every way, each fold found is
        priced on its own, then those that gain are taken cheapest first,
        each kept only if the model's time drops with it beside those
        already taken.

        Raises:
            ValueError: The table is measured on another device or under
                another packaging.
        """
        self.table.measures(dev)
        if self.table.dispatch != dispatch:
            raise ValueError(
                f"{self.table.path} prices dispatch {self.table.dispatch!r}; "
                f"this version is packaged {dispatch!r}"
            )
        # Each operator's cost key by ``id``: every one is traced's or made's,
        # held throughout, so its id stays its own.
        keyed: dict[int, str] = {}
        plain = self._narrow(traced, dev, keyed)
        keys = set(cost_keys(traced, dev, keyed))
        made = Made(dev)
        ways, every = foldings(traced, dev, self.fold_runs, made)
        candidates = list(dict.fromkeys(f for applied in ways for f in applied))
        # Ways folding alike are priced once.
        priced: dict[frozenset[Folding], Tuning | None] = {}
        best = plain
        if every:
            for trial, applied in ways.values():
                self._priced(trial, applied, dev, keys, keyed, priced)
            unpriced = [
                f
                for f in candidates
                if not any(t is not None and f in t.folds for t in priced.values())
            ]
            for trial in priced.values():
                if trial is not None and trial.predicted_us < best.predicted_us:
                    best = trial
        else:
            singles = {
                f: self._priced(
                    *folded(traced, dev, (f,), made=made), dev, keys, keyed, priced
                )
                for f in candidates
            }
            unpriced = [f for f, t in singles.items() if t is None]
            gains = [
                t
                for t in singles.values()
                if t is not None and t.predicted_us < plain.predicted_us
            ]
            for single in sorted(gains, key=lambda t: t.predicted_us):
                trial = (
                    single
                    if not best.folds
                    else self._priced(
                        *folded(traced, dev, best.folds + single.folds, made=made),
                        dev,
                        keys,
                        keyed,
                        priced,
                    )
                )
                if trial is not None and trial.predicted_us < best.predicted_us:
                    best = trial
        return dataclasses.replace(
            best,
            baseline_us=plain.baseline_us,
            baseline_configures=plain.baseline_configures,
            unpriced=tuple(unpriced),
        )

    def _priced(
        self,
        trial: TracedGraph,
        applied: Counter[Folding],
        dev,
        keys: set[str],
        keyed: dict[int, str],
        priced: dict[frozenset[Folding], Tuning | None],
    ) -> Tuning | None:
        """``trial``, the graph with the folds of ``applied`` applied, tuned;
        or None where a design the folds add or remove (beside ``keys``, the
        graph's) is unmeasured. Kept in ``priced`` by the folds, and taken
        from it; each operator's cost key in ``keyed`` (``cost_keys``).
        """
        taken = frozenset(applied)
        if taken not in priced:
            changed = keys ^ set(cost_keys(trial, dev, keyed))
            priced[taken] = (
                None
                if any(k not in self.table.steps for k in changed)
                else dataclasses.replace(
                    self._narrow(trial, dev, keyed), folds=tuple(applied)
                )
            )
        return priced[taken]

    def _narrow(self, traced: TracedGraph, dev, keyed: dict[int, str]) -> Tuning:
        """The tunables and packs of ``traced`` as it is; each operator's
        cost key in ``keyed`` (``cost_keys``).
        """
        table = self.table
        keys = cost_keys(traced, dev, keyed)
        first: dict[str, Operator] = {}
        pinned: dict[str, frozenset[str]] = {}
        for key, step in zip(keys, traced.steps):
            first.setdefault(key, step.op)
            pinned[key] = pinned.get(key, frozenset()) | step.op.pinned
        # A setting applies to every operator of its design, so it moves no
        # tunable any of them pins.
        found = {k: self._candidates(op, dev, pinned[k]) for k, op in first.items()}
        # Each setting's step as the choice sees it, by design.
        steps = {
            k: {
                v.key: table.step_against(v.key, cands[0].key, self.confidence)
                for v in cands
            }
            for k, cands in found.items()
        }
        if table.dispatch == "separate":
            chosen, groups = self._separate(keys, found, steps), ()
        else:
            chosen, groups = self._packed(keys, found, steps, dev)
        devices = Packing(groups).sharing(
            {k: chosen[k].array for k in dict.fromkeys(keys)}
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
            devices=tuple(
                tuple(chosen[k].key for k in group) for group in devices.groups
            ),
            configures=configures,
            predicted_us=predicted,
            baseline_configures=baseline_configures,
            baseline_us=baseline,
            unmeasured=tuple(k for k in found if k not in table.steps),
            inexact=tuple(
                k
                for k, v in chosen.items()
                if v.key != k
                and not all(
                    c.exact
                    for c in [
                        table.steps[v.key],
                        *(table.steps[v.key].points or {}).values(),
                    ]
                )
            ),
        )

    def _separate(
        self,
        keys: Sequence[str],
        found: Mapping[str, Sequence[Variant]],
        steps: Mapping[str, Mapping[str, float]],
    ) -> dict[str, Variant]:
        """Each design's setting on an xclbin chain, by default key: its
        cheapest of ``found``, its occurrences in ``keys`` times its step
        (``steps``) and its switches in times its load.
        """
        table = self.table
        runlist = Runlist(keys)
        arrivals = runlist.switches()
        return {
            k: min(
                cands,
                key=lambda v: runlist.occurrences[k] * steps[k][v.key]
                + arrivals[k] * table.load(v.key),
            )
            for k, cands in found.items()
        }

    def _packed(
        self,
        keys: Sequence[str],
        found: Mapping[str, Sequence[Variant]],
        steps: Mapping[str, Mapping[str, float]],
        dev,
    ) -> tuple[dict[str, Variant], tuple[tuple[str, ...], ...]]:
        """Each design's setting on a full ELF, by default key, and the
        packs; a setting alone priced at its step in ``steps``.
        """
        table = self.table
        # The designs of one array are one device, so they keep one array:
        # the search runs over arrays, each named for its first design, and
        # every other design of it takes its cheapest setting at that array
        # (on the array, not the tunables: one call may pin what another searches).
        units: dict[Hashable, list[str]] = {}
        for k, cands in found.items():
            units.setdefault(cands[0].array, []).append(k)
        unit = {k: designs[0] for designs in units.values() for k in designs}
        runlist = Runlist([unit[k] for k in keys])
        designs_of = [units[found[k][0].array] for k in runlist.order]
        at: dict[str, dict[Hashable, Variant]] = {}
        for k, cands in found.items():
            cheapest = at.setdefault(k, {})
            for v in cands:
                held = cheapest.get(v.array)
                if held is None or steps[k][v.key] < steps[k][held.key]:
                    cheapest[v.array] = v
        candidates = [
            [v for v in found[k] if all(v.array in at[m] for m in designs)]
            for k, designs in zip(runlist.order, designs_of)
        ]
        measured = [all(m in table.steps for m in designs) for designs in designs_of]
        occurrences = Counter(keys)
        budget = shim_budget(dev)

        def member_cost(i: int, v: Variant, entries: int) -> float:
            return (
                entries * table.load(v.key)
                + occurrences[runlist.order[i]] * steps[runlist.order[i]][v.key]
                + sum(
                    occurrences[m] * steps[m][at[m][v.array].key]
                    for m in designs_of[i][1:]
                )
            )

        def device_cost(
            members: Sequence[int], pick: Sequence[Variant], entries: int
        ) -> float:
            settings = [
                (m, v if m == designs_of[i][0] else at[m][v.array])
                for i, v in zip(members, pick)
                for m in designs_of[i]
            ]
            name = table.pack_name(s.key for _, s in settings)
            if name not in table.packs:
                return entries * table.base_us + sum(
                    member_cost(i, v, entries) for i, v in zip(members, pick)
                )
            return entries * table.pack_entry(name) + sum(
                occurrences[m] * table.pack_step(name, s.key) for m, s in settings
            )

        # Alone, each design takes its cheapest setting.
        alone: list[tuple[float, Variant, int]] = []
        for i, key in enumerate(runlist.order):
            e = runlist.entries(frozenset([key]))
            best = min(candidates[i], key=lambda v: device_cost((i,), (v,), e))
            alone.append((device_cost((i,), (best,), e), best, e))

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
            # Ranked as each member alone, then priced as the pack where measured.
            options = sorted(
                (
                    (device_cost(members, pick, entries), pick)
                    for _, pick in _cheapest(ranked, budget, self.fit_attempts)
                ),
                key=lambda option: option[0],
            )
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
        chosen: dict[str, Variant] = {}
        for k in found:
            v = picked[runlist.index[unit[k]]]
            chosen[k] = v if k == unit[k] else at[k][v.array]
        groups = tuple(
            tuple(runlist.order[i] for i in sorted(p.members)) for p in chosen_packs
        )
        return chosen, groups

    @staticmethod
    def _gain(pack: _Pack, alone: Sequence[tuple[float, Variant, int]]) -> float:
        """What ``pack`` saves over its members each alone, bar the parity."""
        return sum(alone[i][0] for i in pack.members) - pack.cost

    def _candidates(
        self, op: Operator, dev, pinned: frozenset[str] = frozenset()
    ) -> list[Variant]:
        """The default setting, then every other one measured accurate at
        every point the default is priced at, and at those alone.
        """
        found = variants(op, dev, pinned)
        default = found[0]
        steps = self.table.steps
        if default.key not in steps:
            return [default]
        points = (steps[default.key].points or {}).keys()
        return [default] + [
            v
            for v in found[1:]
            if v.key in steps
            and steps[v.key].admitted
            and (steps[v.key].points or {}).keys() == points
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
            fitted[key] = (
                fit_verdict(
                    {v.key: OperatorDesign(v.resolved) for v in combo}, self.fit_cache
                )
                is None
            )
        return fitted[key]
