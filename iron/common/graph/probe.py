# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measuring what ``narrowing`` trades, on the NPU.

A full-ELF run costs ``D0`` (dispatch), a configure per device entered
(``base`` plus each member's load), the reset configure ``R`` when the
entries are odd, and each step's ``t_step``.

- ``measure_steps``: one run against ``repeats`` runs of a design gives
  ``t_step`` and ``alone = D0 + base + load + R``. Any other width is a
  candidate only if its output is bit-identical to the default's. Where
  each step is its own dispatch (NPU1), ``t_step`` holds the step's
  dispatch, there is no pack, ``base`` or ``R``, and the load is the
  entry measured by alternation against two reference designs.
- ``calibrate``, on measured designs A, B: ``A B A B ...`` against
  ``A A ... B B ...`` gives ``(E(A) + E(B)) / 2``; the grouped run gives
  ``D0``, the ``alone`` figures ``R``, and ``[A, B]`` packed gives ``base`` as
  ``E(A) + E(B) - E(pack)``.
- ``measure_graph``: every design of the versions it is given, each in a
  ``Call`` of its version.

Figures are medians of per-round medians, interleaved, of the run alone (the
callable's ``last_elapsed``); nothing else may dispatch meanwhile.
"""

from __future__ import annotations

import dataclasses
import statistics
import subprocess
import time
from collections.abc import Callable, Mapping, Sequence

import aie.utils as aie_utils
import numpy as np

from ..declare import Direction, Operator
from ..declare.bound import BoundBuffer, BoundValue
from ..design import device_symbol
from ..image.callable import FullELFCallable, StepCallable
from ..image.packaging import full_elf
from ..image.sequence import OperatorSequence
from .narrowing import (
    Calibration,
    CostTable,
    Runlist,
    StepCost,
    Variant,
    cost_key,
    variants,
)
from .trace import TracedGraph


@dataclasses.dataclass(frozen=True)
class Timing:
    """How long to measure: ``rounds`` interleaved rounds of ``calls`` runs."""

    rounds: int = 8
    calls: int = 50


def pmode() -> str:
    """The NPU's power mode, as ``xrt-smi`` reports it."""
    out = subprocess.run(
        ["xrt-smi", "examine", "-r", "platform"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    for line in out.splitlines():
        if "Power Mode" in line:
            return line.split(":", 1)[1].strip()
    raise RuntimeError(f"xrt-smi reports no power mode:\n{out}")


def _sample(dtype, nbytes: int, rng: np.random.Generator) -> np.ndarray:
    """``nbytes`` of normal floats or small integers, as bytes."""
    dtype = np.dtype(dtype)
    if dtype.kind == "f" or dtype.name == "bfloat16":
        n = nbytes // dtype.itemsize
        return rng.standard_normal(n, dtype=np.float32).astype(dtype).view(np.uint8)
    return rng.integers(0, 4, nbytes, dtype=np.uint8)


class Standalone:
    """A runlist of operators built alone into a loaded image, its inputs
    seeded random data: a full ELF where the device dispatches one, else a
    dispatch per step (``XclbinChain``).

    Args:
        distinct: Every step runs on buffers of its own, as a graph's do, so
            no step finds its inputs in a SoC cache.
        values: Each per-call value by name: the tuner cannot know what a
            value means. A value derived from bound extents follows from them.
        inputs: Input buffers by name, where random bytes would not be
            representative (a draw row's temperature and top-k).
    """

    def __init__(
        self,
        name: str,
        runlist: Sequence[Operator],
        coresident: Sequence[Sequence[Operator]] = (),
        values: Mapping[str, int] | None = None,
        seed: int = 0,
        distinct: bool = True,
        inputs: Mapping[str, np.ndarray] | None = None,
    ):
        self.steps = list(runlist)
        firsts = {}
        for k, op in enumerate(self.steps):
            firsts.setdefault(id(op), k)
        self._slot = [
            k if distinct else firsts[id(op)] for k, op in enumerate(self.steps)
        ]
        self._filled = sorted(set(self._slot))
        in_names, out_names = [], []
        for k in self._filled:
            op = self.steps[k]
            for buf, name_ in zip(op.buffers, self._names(k, op)):
                (out_names if buf.direction is Direction.OUT else in_names).append(
                    name_
                )
        self.sequence = OperatorSequence(
            name,
            [(op, *self._names(self._slot[k], op)) for k, op in enumerate(self.steps)],
            in_names,
            out_names,
            dispatch="auto",
            share_designs=True,
            coresident=coresident,
        ).compile()
        self.callable = self.sequence.get_callable()
        rng = np.random.default_rng(seed)
        for k in self._filled:
            op = self.steps[k]
            names = self._names(k, op)
            addressed = op.addressed_inputs(
                {buf.name: self.address(n) for buf, n in zip(op.buffers, names)}, rng
            )
            for buf, name_ in zip(op.buffers, names):
                if buf.name in addressed:
                    content = np.ascontiguousarray(addressed[buf.name], buf.dtype)
                    self._bytes(name_)[: buf.nbytes] = content.view(np.uint8)
                elif buf.direction.fills:
                    self._bytes(name_)[: buf.nbytes] = self._content(buf, inputs, rng)
        # Resolved: a value derived through a tunable is only seen once it is set.
        ops = {id(op): op.resolved() for op in self.steps}.values()
        # An extent read only through its derivations has no word.
        read = self.sequence.artifacts.parameters
        symbols = {
            device_symbol(op, v): np.int32(self._value(op, values or {}, v))
            for op in ops
            for v in op.values
            if device_symbol(op, v) in read
        }
        if symbols:
            self.callable.write_values(symbols)

    @staticmethod
    def _value(op: Operator, values: Mapping[str, int], v: BoundValue) -> int:
        """``v`` as given, or derived as a call derives it from the bounded
        extents given, of the resolved ``op``.
        """
        if v.name in values:
            return values[v.name]
        extents = {e: values[e] for e in op.bound_extents if e in values}
        if extents and v.name in op._per_call_derived():
            return op.derived_at(v.name, **extents)
        raise ValueError(
            f"per-call value {v.name!r} needs a representative value to be measured"
        )

    @staticmethod
    def _content(
        buf: BoundBuffer,
        inputs: Mapping[str, np.ndarray] | None,
        rng: np.random.Generator,
    ) -> np.ndarray:
        if inputs is None or buf.name not in inputs:
            return _sample(buf.dtype, buf.nbytes, rng)
        content = np.ascontiguousarray(inputs[buf.name], dtype=buf.dtype)
        if content.nbytes != buf.nbytes:
            raise ValueError(
                f"input {buf.name!r} is {content.nbytes} bytes, its buffer {buf.nbytes}"
            )
        return content.reshape(-1).view(np.uint8)

    @staticmethod
    def _names(k: int, op: Operator) -> list[str]:
        return [f"s{k}_{b.name}" for b in op.buffers]

    def _bytes(self, name: str) -> np.ndarray:
        return self.callable.get_storage(name).numpy_view().view(np.uint8)

    def address(self, name: str) -> int:
        """The device address of buffer ``name``."""
        view = self.callable.get_storage(name)
        root = view.storage.binding_handle(0, view.storage.nbytes)
        return root.address() + view.storage_offset

    def output_bytes(self) -> bytes:
        """What the steps wrote, after one run: every out and in-out buffer."""
        self.callable()
        return b"".join(
            self.callable.get_storage(name)
            .numpy()
            .view(np.uint8)[: buf.nbytes]
            .tobytes()
            for k in self._filled
            for buf, name in zip(self.steps[k].buffers, self._names(k, self.steps[k]))
            if buf.direction.drains
        )


def time_interleaved(
    runs: Sequence[FullELFCallable | StepCallable], timing: Timing
) -> list[float]:
    """Each loaded image's median of per-round medians, microseconds."""
    for run in runs:
        run()  # warm: first-run setup lands on nobody's figure
    medians: list[list[float]] = [[] for _ in runs]
    for _ in range(timing.rounds):
        for i, run in enumerate(runs):
            times = []
            for _ in range(timing.calls):
                run()
                times.append(run.last_elapsed)
            medians[i].append(statistics.median(times) * 1e6)
    return [statistics.median(m) for m in medians]


# The device contexts the driver holds at once; each run timed keeps one.
CONTEXTS = 16

# Past this nothing stays in a cache, and the repeats' copies would not fit.
DISTINCT_BYTES = 256 * 2**20


def measure_steps(
    table: CostTable,
    found: Sequence[Variant],
    timing: Timing = Timing(),
    repeats: int = 9,
    values: Mapping[str, int] | None = None,
    inputs: Mapping[str, np.ndarray] | None = None,
    references: tuple[Operator, Operator] | None = None,
    pairs: int = 4,
) -> dict[str, StepCost]:
    """Measure every width in ``found`` (the default first) into ``table``,
    as many at once as the device's contexts hold.

    Where each step is its own dispatch, ``[v]`` run again never
    reconfigures, so the entry ``E(v)`` comes from alternation against
    ``references`` ``r`` and ``q``: ``[v, r] * pairs`` against
    ``[v] * pairs + [r] * pairs`` gives ``E(v) + E(r)``, and with the same of
    ``(v, q)`` and ``(r, q)``, ``E(v)``.

    Args:
        values: Per-call values by name, for ``found``'s and the references'.
        references: Two designs other than ``found``'s, for a device without
            a full ELF.
    """
    mode = pmode()
    separate = not full_elf(aie_utils.ensure_current_device())
    if separate and references is None:
        raise ValueError(
            "each step is its own dispatch here: the entry cost needs references"
        )
    distinct = sum(b.nbytes for b in found[0].op.buffers) <= DISTINCT_BYTES
    reference = None
    out = {}
    per_batch = CONTEXTS // 6 if separate else CONTEXTS // 2
    for begin in range(0, len(found), per_batch):
        batch = found[begin : begin + per_batch]
        short = [
            Standalone(f"probe1_{v.key}", [v.op], values=values, inputs=inputs)
            for v in batch
        ]
        long = [
            Standalone(
                f"probe{repeats}_{v.key}",
                [v.op] * repeats,
                values=values,
                distinct=distinct,
                inputs=inputs,
            )
            for v in batch
        ]
        switches = []
        if separate:
            r, q = references
            for tag, a, b in [
                (f"{v.key}_{s}", v.op, ref)
                for v in batch
                for s, ref in (("r", r), ("q", q))
            ] + [("rq", r, q)]:
                switches += [
                    Standalone(f"alt{pairs}_{tag}", [a, b] * pairs, values=values),
                    Standalone(
                        f"grp{pairs}_{tag}", [a] * pairs + [b] * pairs, values=values
                    ),
                ]
        if reference is None:
            reference = short[0].output_bytes()
        exact = [run.output_bytes() == reference for run in short]
        times = time_interleaved([r.callable for r in short + long + switches], timing)
        n = len(batch)
        # Each `(alt, grp)` pair of `switches`, as `E(a) + E(b)`.
        sums = [
            (alt - grp) / (pairs - 1)
            for alt, grp in zip(times[2 * n :: 2], times[2 * n + 1 :: 2])
        ]
        for i, v in enumerate(batch):
            t_step = (times[n + i] - times[i]) / (repeats - 1)
            alone = times[i] - t_step
            if separate:
                alone += (sums[2 * i] + sums[2 * i + 1] - sums[-1]) / 2
            cost = StepCost(
                t_step_us=t_step,
                alone_us=alone,
                exact=exact[i],
                pmode=mode,
                rounds=timing.rounds,
                calls=timing.calls,
                measured=CostTable.today(),
            )
            table.record_step(v.key, cost)
            out[v.key] = cost
        # A probe holds its context while it lives; the next batch needs them.
        del short, long, switches
    return out


def calibrate(
    table: CostTable,
    a: Operator,
    b: Operator,
    timing: Timing = Timing(),
    pairs: int = 4,
    values: Mapping[str, int] | None = None,
) -> Calibration:
    """Split a configure's cost over measured designs ``a`` and ``b`` into
    ``table``. Where each step is its own dispatch there is no pack, and so
    no ``base``, and no reset configure.
    """
    ka, kb = cost_key(a), cost_key(b)
    ta, tb = table.steps[ka].t_step_us, table.steps[kb].t_step_us
    tag = f"{ka}_{kb}"
    runs = [
        Standalone(f"cal_alt{pairs}_{tag}", [a, b] * pairs, values=values),
        Standalone(f"cal_grp{pairs}_{tag}", [a] * pairs + [b] * pairs, values=values),
    ]
    fused = full_elf(aie_utils.ensure_current_device())
    if fused:
        runs += [
            Standalone(f"cal_pack_{tag}", [a, b], coresident=[[a, b]], values=values),
            Standalone(f"cal_a_{tag}", [a], values=values),
            Standalone(f"cal_b_{tag}", [b], values=values),
        ]
    alt, grp, *rest = time_interleaved([r.callable for r in runs], timing)
    switch = (alt - grp) / (2 * pairs - 2)  # (E(a) + E(b)) / 2
    dispatch = grp - pairs * (ta + tb) - 2 * switch
    reset = base = 0.0
    if fused:
        pack, alone_a, alone_b = rest
        reset = ((alone_a - ta) + (alone_b - tb) - 2 * switch) / 2 - dispatch
        base = 2 * switch - (pack - ta - tb - reset - dispatch)
    cal = Calibration(
        dispatch_us=dispatch,
        reset_us=reset,
        base_us=base,
        switch_us=switch,
        pmode=pmode(),
        rounds=timing.rounds,
        calls=timing.calls,
        measured=CostTable.today(),
    )
    table.record_calibration((ka, kb), cal)
    return cal


@dataclasses.dataclass(frozen=True)
class Call:
    """One call of a traced graph version, as its designs are measured at:
    the graph's per-call values, and what any buffer whose contents a step's
    time follows holds, by graph buffer name.
    """

    traced: TracedGraph
    values: Mapping[str, int] = dataclasses.field(default_factory=dict)
    contents: Mapping[str, np.ndarray] = dataclasses.field(default_factory=dict)

    def op_values(self, op: Operator) -> dict[str, int]:
        """The per-call values ``op`` is written in this call, by member name."""
        # A table's address the graph fills in; a word step alone reads none.
        values = {**dict.fromkeys(self.traced.addresses, 0), **self.values}
        return {
            b.member.name: b.expression.evaluate(values)
            for b in self.traced.bindings
            if b.op is op
        }

    def op_inputs(self, op: Operator) -> dict[str, np.ndarray]:
        """What ``op``'s buffers hold in this call, by ``op``'s buffer name."""
        return {
            buf.name: self.contents[name]
            for step in self.traced.steps
            if step.op is op
            for buf, name in zip(op.buffers, step.names)
            if name in self.contents
        }


def measure_graph(
    table: CostTable,
    calls: Sequence[Call],
    pairs: Sequence[tuple[str, str]],
    timing: Timing = Timing(),
    repeats: int = 9,
    remeasure: bool = False,
    log: Callable[[str], None] = print,
) -> None:
    """Measure every design of ``calls``' graphs into ``table``, saved as it
    goes: each at every width ``variants`` gives, in the first call that
    runs it, then the configure cost between each of ``pairs``, the first
    designs of those operator classes at their narrowest. Designs and
    calibrations already in the table are kept unless ``remeasure``; those
    the graphs no longer have are dropped.
    """
    dev = aie_utils.ensure_current_device()
    first: dict[str, tuple[Operator, Call]] = {}
    for call in calls:
        keys = [cost_key(s.op) for s in call.traced.steps]
        for key in Runlist(keys).order:
            step = call.traced.steps[keys.index(key)]
            first.setdefault(key, (step.op, call))
    found = {key: variants(op, dev) for key, (op, _) in first.items()}

    current = {v.key for vs in found.values() for v in vs}
    stale = [k for k in table.steps if k not in current]
    for k in stale:
        del table.steps[k]
    if stale:
        log(f"dropped {len(stale)} designs the graphs no longer have")

    by_class: dict[str, tuple[Variant, Call]] = {}
    for key, (op, call) in first.items():
        by_class.setdefault(type(op).__name__, (found[key][-1], call))
    named = [by_class[name] for name in dict.fromkeys(n for p in pairs for n in p)]
    if not full_elf(dev) and len(named) < 3:
        raise ValueError(
            f"each step is its own dispatch here: the pairs must name three "
            f"designs, the references each design's entry is measured against; "
            f"got {[type(v.op).__name__ for v, _ in named]}"
        )

    for i, (key, (op, call)) in enumerate(first.items()):
        name = type(op).__name__
        if not remeasure and all(v.key in table.steps for v in found[key]):
            log(f"[{i}] {name}: in the table")
            continue
        values = call.op_values(op)
        references = None
        if not full_elf(dev):
            mine = {v.key for v in found[key]}
            (r, r_call), (q, q_call) = [(v, c) for v, c in named if v.key not in mine][
                :2
            ]
            references = (r.op, q.op)
            values = {**r_call.op_values(r.op), **q_call.op_values(q.op), **values}
        start = time.time()
        costs = measure_steps(
            table,
            found[key],
            timing,
            repeats,
            values,
            call.op_inputs(op),
            references,
        )
        table.save()
        log(f"[{i}] {name} ({time.time() - start:.0f}s) at {values}")
        for v in found[key]:
            c = costs[v.key]
            log(
                f"    {dict(v.widths)}: t_step {c.t_step_us:8.2f} us  "
                f"alone {c.alone_us:8.2f} us  exact {c.exact}"
            )

    chosen = [(by_class[a][0], by_class[b][0]) for a, b in pairs]
    wanted = {f"{a.key}|{b.key}" for a, b in chosen}
    for k in [k for k in table.calibrations if k not in wanted]:
        del table.calibrations[k]
    for (a, b), (name_a, name_b) in zip(chosen, pairs):
        if not remeasure and f"{a.key}|{b.key}" in table.calibrations:
            log(f"calibration {name_a}/{name_b}: in the table")
            continue
        cal = calibrate(table, a.op, b.op, timing)
        table.save()
        log(
            f"calibration {name_a}/{name_b}: D0 {cal.dispatch_us:.1f}  "
            f"R {cal.reset_us:.1f}  base {cal.base_us:.1f}  "
            f"switch {cal.switch_us:.1f} us"
        )
    table.save()
