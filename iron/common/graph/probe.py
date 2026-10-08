# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measuring what ``narrowing`` trades, on the NPU.

A full-ELF run costs ``D0`` (dispatch), a configure per device entered
(``base`` plus each member's load), the reset configure ``R`` when the
entries are odd, and each step's ``t_step``. An xclbin chain (a table's
dispatch ``"separate"``) costs ``F`` per call, each step's ``c``, its own
dispatch included, and the incoming design's load ``L`` at every switch,
counted around the call: a chain of one design never switches.

- ``measure_steps``: one run against ``repeats`` runs of a design gives
  ``t_step`` and ``alone = D0 + base + load + R`` (on an xclbin chain ``c``
  and ``F``). Any other setting of its
  tunables is a candidate only if its output is bit-identical to the
  default's, or ``judge`` finds it within the default's gate and its own.
  A design the ``CostCache`` holds is taken from it, not run.
- ``search``: which of a design's settings ``measure_steps`` runs: all of
  them, or coordinate descent where there are more than ``EXHAUSTIVE``.
- ``calibrate``, on measured designs A, B: ``A B A B ...`` against
  ``A A ... B B ...`` gives ``(E(A) + E(B)) / 2``; the grouped run gives
  ``D0``, the ``alone`` figures ``R``, and ``[A, B]`` packed gives ``base`` as
  ``E(A) + E(B) - E(pack)``. On an xclbin chain ``E`` is ``L``, the grouped
  run gives ``F``, and there is no reset or pack.
- ``measure_loads``: ``[R, k]`` alternating against them grouped, as
  ``calibrate`` does, gives ``E(R) + E(k)``, ``R`` a calibrated design.
- ``measure_packs``: on a full ELF, designs sharing one device alternating
  with ``R`` against them grouped gives the pack's entry, and each member
  repeated on it its step there.
- ``measure_graph``: every design of the versions it is given, each in a
  ``Call`` of its version, then the calibrations, then each design's entry.
- ``check_model``: a tuned version timed against the untuned one, each
  beside the model's prediction for it.

Figures are medians of per-round medians, interleaved, of the run alone (the
callable's ``last_elapsed``), a setting far behind the fastest over fewer
rounds (``Timing``); nothing else may dispatch meanwhile.
"""

from __future__ import annotations

import dataclasses
import hashlib
import math
import statistics
import subprocess
import time
from collections.abc import Callable, Hashable, Mapping, Sequence
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
from aie.iron.device import Device
from aie.utils import bfp

from .. import harness
from ..declare import Direction, Operator
from ..declare.bound import BoundBuffer, BoundValue
from ..design import OperatorDesign, device_symbol
from ..image.callable import FullELFCallable, StepCallable
from ..image.sequence import OperatorSequence
from .compiled import CompiledGraph
from .costcache import Accuracy, CostCache, Measurement, Pairing
from .fold import Made, folded, foldings, replaced
from .narrowing import (
    FIT_CACHE,
    Calibration,
    CostTable,
    JointNarrowing,
    PackCost,
    Runlist,
    StepCost,
    Variant,
    cost_key,
    cost_keys,
    fitting,
    refuse,
    variants,
)
from .trace import TracedGraph


@dataclasses.dataclass(frozen=True)
class Timing:
    """How long to measure: ``rounds`` interleaved rounds of ``calls`` runs.

    Where the runs are settings of one design, a setting whose runs take
    more than ``cutoff`` times the fastest setting's once ``settle`` rounds
    are in is timed no further, its figure those rounds'.
    """

    rounds: int = 8
    calls: int = 50
    settle: int = 2
    cutoff: float = 1.5


@dataclasses.dataclass(frozen=True)
class Timed:
    """A run's median of per-round medians, microseconds, over ``rounds``."""

    us: float
    rounds: int


def platform() -> dict[str, str]:
    """The NPU's platform report from ``xrt-smi``: its ``Name``, its
    ``Power Mode``, ...
    """
    out = subprocess.run(
        ["xrt-smi", "examine", "-r", "platform"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    report = {}
    for line in out.splitlines():
        name, sep, value = line.partition(":")
        if sep:
            report[name.strip()] = value.strip()
    if "Name" not in report or "Power Mode" not in report:
        raise RuntimeError(f"xrt-smi reports no platform name or power mode:\n{out}")
    return report


def pmode() -> str:
    """The NPU's power mode, as ``xrt-smi`` reports it."""
    return platform()["Power Mode"]


def cost_cache() -> CostCache:
    """The cost cache of this NPU at its present power mode."""
    report = platform()
    return CostCache(report["Name"], report["Power Mode"])


def _sample(dtype, nbytes: int, rng: np.random.Generator) -> np.ndarray:
    """``nbytes`` of normal floats or small integers, as bytes."""
    dtype = np.dtype(dtype)
    if dtype.kind == "f" or dtype.name == "bfloat16":
        n = nbytes // dtype.itemsize
        return rng.standard_normal(n, dtype=np.float32).astype(dtype).view(np.uint8)
    return rng.integers(0, 4, nbytes, dtype=np.uint8)


class Standalone:
    """A runlist of operators built alone into a loaded image, its inputs
    seeded random data.

    Args:
        dispatch: How the runlist is packaged (``narrowing.DISPATCHES``): one
            full ELF, or an xclbin per design dispatched step by step.
        distinct: Every step runs on buffers of its own, as a graph's do, so
            no step finds its inputs in a SoC cache.
        values: Per operator, each per-call value by name: the tuner cannot
            know what a value means. One derived from bound extents follows
            from theirs.
        inputs: Per operator, input buffers by name, where random bytes
            would not be representative (a draw row's temperature and top-k).
    """

    def __init__(
        self,
        name: str,
        runlist: Sequence[Operator],
        coresident: Sequence[Sequence[Operator]] = (),
        values: Mapping[Operator, Mapping[str, int]] | None = None,
        seed: int = 0,
        distinct: bool = True,
        inputs: Mapping[Operator, Mapping[str, np.ndarray]] | None = None,
        dispatch: str = "fused",
    ):
        self.steps = list(runlist)
        values, inputs = values or {}, inputs or {}
        self._values = {op: dict(values.get(op, {})) for op in self.steps}
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
            dispatch=dispatch,
            share_designs=True,
            coresident=coresident,
        ).compile()
        self.callable = self.sequence.get_callable()
        rng = np.random.default_rng(seed)
        self._before: dict[str, np.ndarray] = {}
        for k in self._filled:
            op = self.steps[k]
            for buf, name_ in zip(op.buffers, self._names(k, op)):
                if buf.direction.fills:
                    content = self._content(buf, inputs.get(op, {}), rng)
                    self._bytes(name_)[: buf.nbytes] = content
                    if buf.direction.drains:
                        self._before[name_] = content.copy()
        ops = {id(op): op for op in self.steps}.values()
        artifacts = self.sequence.artifacts
        # An extent read only through its derivations has no word in a full
        # ELF; an xclbin chain has no parameter table, its values dispatch-time.
        symbols = {
            device_symbol(op, v): np.int32(self._value(op, self._values[op], v))
            for op in ops
            for v in op.values
            if artifacts.kind == "xclbin"
            or device_symbol(op, v) in artifacts.parameters
        }
        if symbols:
            self.callable.write_values(symbols)

    @staticmethod
    def _value(op: Operator, values: Mapping[str, int], v: BoundValue) -> int:
        if v.name in values:
            return values[v.name]
        extents = op.bound_extents
        if v.name in op._per_call_derived() and extents.keys() <= values.keys():
            return op.resolved().derived_at(v.name, **{e: values[e] for e in extents})
        raise ValueError(
            f"per-call value {v.name!r} needs a representative value to be measured"
        )

    @staticmethod
    def _content(
        buf: BoundBuffer,
        inputs: Mapping[str, np.ndarray],
        rng: np.random.Generator,
    ) -> np.ndarray:
        if buf.name not in inputs:
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
        return self.callable.get_buffer(name).numpy_view().view(np.uint8)

    def digest(self) -> str:
        """Run once: the sha256 of what every step ``written``."""
        self.callable()
        return hashlib.sha256(
            b"".join(
                a.tobytes() for k in self._filled for a in self.written(k).values()
            )
        ).hexdigest()

    def inputs(self, k: int = 0) -> dict[str, np.ndarray]:
        """What step ``k`` was given, by buffer name: views of the device
        buffers, an in-out one as it was before any run.
        """
        op = self.steps[k]
        out = {}
        for buf, name in zip(op.buffers, self._names(self._slot[k], op)):
            if buf.direction.fills:
                data = self._before.get(name, self._bytes(name)[: buf.nbytes])
                out[buf.name] = data.view(buf.host_dtype).reshape(buf.host_shape)
        return out

    def written(self, k: int = 0) -> dict[str, np.ndarray]:
        """What step ``k`` wrote in the last run, by buffer name: along a
        bounded axis only the rows under the call's bound.
        """
        op = self.steps[k]
        out = {}
        for buf, name in zip(op.buffers, self._names(self._slot[k], op)):
            if not buf.direction.drains:
                continue
            under = [slice(None)] * len(buf.shape)
            for extent in op.bound_extents:
                axis = buf.extent_axis(op.value(extent).member)
                if axis is not None:
                    under[axis] = slice(0, self._values[op][extent])
            data = self._bytes(name)[: buf.nbytes].reshape(*buf.shape, -1)
            # A block-float buffer stays its blocks' bytes, as its host shape is.
            data = np.ascontiguousarray(data[tuple(under)]).view(buf.host_dtype)
            out[buf.name] = data if bfp.is_bfp(buf.dtype) else data[..., 0]
        return out


def judge(
    default: Operator,
    op: Operator,
    inputs: Mapping[str, np.ndarray],
    written: Mapping[str, np.ndarray],
    values: Mapping[str, int] | None = None,
) -> Accuracy | None:
    """Whether ``op``'s output ``written`` on ``inputs`` is within the gate
    of ``default``, the width it would replace, and within its own.

    Returns:
        None where a gate is missing or exact, or `values` bound an extent
        short of its length: there only a bit-identical width is admitted.
    """
    gates = {"the default's": default.gate(), "its own": op.gate()}
    if any(g is None or g.kind == "exact" for g in gates.values()):
        return None
    values = values or {}
    for extent in op.bound_extents:
        if values.get(extent) != getattr(op, op.value(extent).member.field.name):
            return None
    want = harness.expected(op, inputs, values)
    for which, gate in gates.items():
        bound = gate.bound(*inputs.values()) if gate.kind == "bound" else None
        for name, reference in want.items():
            verdict = harness.verify_buffer(
                written[name], name, reference, gate, bound=bound
            )
            if not verdict:
                detail = f"{name} under {which} gate: {verdict.detail}"
                return Accuracy(False, detail, CostTable.today())
    return Accuracy(True, "", CostTable.today())


def time_interleaved(
    runs: Sequence[FullELFCallable | StepCallable],
    timing: Timing,
    groups: Sequence[Hashable | None] = (),
    fastest: float = math.inf,
) -> list[Timed]:
    """Each loaded image's median of per-round medians, microseconds.

    Args:
        groups: Per run, the setting it measures, where the runs are
            settings of one design; a setting is timed no further once its
            slowest run is past ``timing.cutoff`` times the fastest
            setting's (``Timing``). None marks a run never stopped. Every
            run is timed every round if not given.
        fastest: The slowest run of the fastest setting timed before these.
    """
    for run in runs:
        run()  # warm: first-run setup lands on nobody's figure
    medians: list[list[float]] = [[] for _ in runs]
    live = set(range(len(runs)))
    for r in range(timing.rounds):
        for i, run in enumerate(runs):
            if i not in live:
                continue
            times = []
            for _ in range(timing.calls):
                run()
                times.append(run.last_elapsed)
            medians[i].append(statistics.median(times) * 1e6)
        if not groups or r + 1 < timing.settle:
            continue
        slowest: dict[Hashable, float] = {}
        for i in live:
            us = statistics.median(medians[i])
            slowest[groups[i]] = max(slowest.get(groups[i], 0.0), us)
        bar = timing.cutoff * min([fastest, *slowest.values()])
        live = {i for i in live if groups[i] is None or slowest[groups[i]] <= bar}
    return [Timed(statistics.median(m), len(m)) for m in medians]


@dataclasses.dataclass(frozen=True)
class ModelCheck:
    """The model's times for a tuned version and for the version as traced,
    beside what each took on the device, microseconds."""

    predicted_us: float
    measured_us: float
    baseline_us: float
    baseline_measured_us: float

    def report(self) -> str:
        """The two versions' modelled and measured times, the gain each
        side gives and the model's error."""
        lines = [
            f"  {name}: model {model:.1f} us, measured {measured:.1f} us "
            f"({(model - measured) / measured:+.1%})"
            for name, model, measured in (
                ("tuned", self.predicted_us, self.measured_us),
                ("as traced", self.baseline_us, self.baseline_measured_us),
            )
        ]
        lines.append(
            f"  gain: model {self.baseline_us - self.predicted_us:.1f} us, "
            f"measured {self.baseline_measured_us - self.measured_us:.1f} us"
        )
        return "\n".join(lines)


def check_model(
    tuned: CompiledGraph,
    untuned: CompiledGraph,
    tensors: Sequence[np.ndarray] = (),
    values: Mapping[str, int] | None = None,
    timing: Timing = Timing(),
) -> ModelCheck:
    """Time a tuned version against the same version compiled untuned,
    interleaved, and set each beside its prediction.

    Args:
        tuned: A version compiled with a `JointNarrowing`.
        untuned: The same graph and shapes compiled without one, by a graph
            instance of its own: a graph keeps one version per shape.
        tensors: The inputs both are called on.
        values: The per-call values both are called with.
        timing: How long to time them.

    Raises:
        ValueError: `tuned` was not tuned, `untuned` was, or the tuning left
            designs unmeasured, whose time the model leaves out.
    """
    tuning = tuned.tuning
    if tuning is None or untuned.tuning is not None:
        raise ValueError("check_model takes a tuned version and an untuned one")
    if tuning.unmeasured:
        raise ValueError(
            f"the model leaves out the designs its table lacks: {tuning.unmeasured}"
        )
    for version in (tuned, untuned):
        version(*tensors, **(values or {}))
    measured, baseline = time_interleaved([tuned.callable, untuned.callable], timing)
    return ModelCheck(tuning.predicted_us, measured.us, tuning.baseline_us, baseline.us)


# The device contexts the driver holds at once; each run timed keeps one.
CONTEXTS = 16

# Past this nothing stays in a cache, and the repeats' copies would not fit.
DISTINCT_BYTES = 256 * 2**20

# Measuring a pack reprices it, so a version's tuning may take another.
PACK_ROUNDS = 3


def measure_steps(
    table: CostTable,
    found: Sequence[Variant],
    timing: Timing = Timing(),
    repeats: int = 9,
    values: Mapping[str, int] | None = None,
    inputs: Mapping[str, np.ndarray] | None = None,
    cache: CostCache | None = None,
    remeasure: bool = False,
    twins: Sequence[Variant | None] = (),
    fit_cache: Path = FIT_CACHE,
    log: Callable[[str], None] = print,
) -> dict[str, StepCost]:
    """Measure every width in ``found`` (the default first) into ``table``,
    as many at once as the device's contexts hold. A width whose output is
    not the default's is run once more and judged: it is accurate if
    ``judge`` finds it, and the default, within their gates.

    Args:
        cache: Widths and verdicts it holds are taken from it rather than
            run, unless `remeasure`; those run are written to it.
        twins: For each width, the design in `table` it is priced against,
            or None. A width with a twin is run beside it, its step time
            recorded as the twin's plus their difference in that run, so a
            drift between this run and the twin's own does not reach it.
            Its one-run figure is its own: one run's noise exceeds the drift.
        fit_cache: Where a width that does not build is recorded as
            refused (``refuse``), so ``fitting`` leaves it out from then on.
        log: Where a width that does not build is reported.

    Returns:
        The widths run on the device, by key. One other than the default
        that does not build is left out of it and of ``table``.

    Raises:
        RuntimeError: The default or a twin does not build.
        ValueError: `cache` is for another power mode than the NPU's, or
            a twin is not in `table`.
    """
    mode = pmode()
    if cache is not None and cache.mode != mode:
        raise ValueError(f"the cost cache is for power mode {cache.mode}, not {mode}")
    twins = list(twins) or [None] * len(found)
    for t in twins:
        if t is not None and t.key not in table.steps:
            raise ValueError(f"twin {t.key} is not in the table")
    entries = [
        None if cache is None else cache.key(v.resolved, values, inputs, table.dispatch)
        for v in found
    ]
    besides = [
        (
            None
            if cache is None or t is None
            else cache.beside_key(
                cache.key(t.resolved, values, inputs, table.dispatch), e
            )
        )
        for t, e in zip(twins, entries)
    ]
    held: dict[str, Measurement] = {}
    near: dict[str, Measurement] = {}
    if cache is not None and not remeasure:
        for v, entry, beside in zip(found, entries, besides):
            m = cache.get(entry, Measurement)
            b = None if beside is None else cache.get(beside, Measurement)
            if m is not None and (beside is None or b is not None):
                held[v.key] = m
                if b is not None:
                    near[v.key] = b
    todo = [
        (v, e, t, b)
        for v, e, t, b in zip(found, entries, twins, besides)
        if v.key not in held
    ]
    default = found[0]
    distinct = sum(b.nbytes for b in default.op.buffers) <= DISTINCT_BYTES
    measured: dict[str, Measurement] = {}
    fastest = math.inf
    size = CONTEXTS // (4 if any(twins) else 2)
    failed: set[str] = set()
    batches = math.ceil(len(todo) / size)
    log(f"    {len(todo)} to run, {len(held)} from the cache, {batches} batches")
    for begin in range(0, len(todo), size):
        batch = todo[begin : begin + size]
        log(f"    batch {begin // size + 1}/{batches}: building {len(batch)}")
        runs, short, long = [], [], []
        for d, entry, of, own in [(v, e, v.key, True) for v, e, _, _ in batch] + [
            (t, b, v.key, False) for v, _, t, b in batch if t is not None
        ]:
            if of in failed:
                continue
            try:
                one = Standalone(
                    f"probe1_{d.key}",
                    [d.op],
                    values={d.op: values or {}},
                    inputs={d.op: inputs or {}},
                    dispatch=table.dispatch,
                )
                many = Standalone(
                    f"probe{repeats}_{d.key}",
                    [d.op] * repeats,
                    values={d.op: values or {}},
                    distinct=distinct,
                    inputs={d.op: inputs or {}},
                    dispatch=table.dispatch,
                )
            except RuntimeError as e:
                # The placer passed it, but the build did not. The default
                # is the graph's own and a twin was measured, so both build.
                if of == default.key or not own:
                    raise
                failed.add(of)
                refuse({of: OperatorDesign(d.resolved)}, str(e), fit_cache)
                log(f"{dict(d.tunables)} does not build, not measured: {e}")
                continue
            runs.append((entry, of, own))
            short.append(one)
            long.append(many)
        if not runs:
            continue
        log(f"    batch {begin // size + 1}/{batches}: timing {len(runs)} runs")
        # The default is the untuned graph's figure: always timed in full.
        groups = [None if of == default.key else of for _, of, _ in runs] * 2
        outputs = [run.digest() for run in short]
        times = time_interleaved(
            [r.callable for r in short + long], timing, groups, fastest
        )
        n = len(runs)
        slowest: dict[str, float] = {}
        for i, (entry, of, own) in enumerate(runs):
            t_step = (times[n + i].us - times[i].us) / (repeats - 1)
            m = Measurement(
                t_step_us=t_step,
                alone_us=times[i].us - t_step,
                output=outputs[i],
                pmode=mode,
                rounds=times[n + i].rounds,
                calls=timing.calls,
                measured=CostTable.today(),
            )
            slowest[of] = max(slowest.get(of, 0.0), times[n + i].us)
            if own:
                measured[of] = m
            else:
                near[of] = m
            if cache is not None:
                cache.put(entry, m)
        fastest = min(fastest, *slowest.values())
        # A probe holds its context while it lives; the next batch needs them.
        del short, long
    found, entries, twins = zip(
        *((v, e, t) for v, e, t in zip(found, entries, twins) if v.key not in failed)
    )
    known = held | measured
    reference = known[default.key].output
    inexact = {v.key for v in found[1:] if known[v.key].output != reference}
    judged = [
        (v, e) for v, e in zip(found, entries) if v is default or v.key in inexact
    ]
    accurate = set()
    for v, entry in judged if inexact else []:
        key = None if cache is None else cache.judged_key(entries[0], entry)
        verdict = None if key is None or remeasure else cache.get(key, Accuracy)
        if verdict is None:
            run = Standalone(
                f"judge_{v.key}",
                [v.op],
                values={v.op: values or {}},
                inputs={v.op: inputs or {}},
                dispatch=table.dispatch,
            )
            run.digest()
            verdict = judge(
                default.op, v.op, run.inputs(), run.written(), values
            ) or Accuracy(False, "not judged", CostTable.today())
            del run
            if key is not None:
                cache.put(key, verdict)
        if verdict.within:
            accurate.add(v.key)
        elif v is default:
            break  # a default its own gate refuses admits no inexact width
    for v, twin in zip(found, twins):
        m = known[v.key]
        if twin is not None:
            delta = m.t_step_us - near[v.key].t_step_us
            m = dataclasses.replace(
                m, t_step_us=table.steps[twin.key].t_step_us + delta
            )
        table.record_step(v.key, m.cost(reference, v.key in accurate))
    return {key: table.steps[key] for key in measured}


# Past this many settings, a design's tunables are searched one at a time.
EXHAUSTIVE = 32


def search(
    table: CostTable,
    found: Sequence[Variant],
    timing: Timing = Timing(),
    repeats: int = 9,
    values: Mapping[str, int] | None = None,
    inputs: Mapping[str, np.ndarray] | None = None,
    cache: CostCache | None = None,
    remeasure: bool = False,
    twins: Sequence[Variant | None] = (),
    exhaustive: int = EXHAUSTIVE,
    fit_cache: Path = FIT_CACHE,
    log: Callable[[str], None] = print,
) -> dict[str, StepCost]:
    """Measure the settings of ``found`` (the default first) into ``table``:
    every one when there are at most ``exhaustive``, else by coordinate
    descent, each tunable's line through the fastest accurate setting so far,
    from the default until a pass over the tunables moves it no further.
    A setting that does not build is left off every line after.
    The other arguments are ``measure_steps``'.

    Returns:
        The settings run on the device, by key.
    """
    if len(found) <= exhaustive:
        return measure_steps(
            table,
            found,
            timing,
            repeats,
            values,
            inputs,
            cache,
            remeasure,
            twins,
            fit_cache,
            log,
        )
    twin_of = dict(zip((v.key for v in found), twins or [None] * len(found)))
    default = found[0]
    best = default
    ran: dict[str, StepCost] = {}
    moved = True
    while moved:
        moved = False
        for i in range(len(default.tunables)):
            line = [
                v
                for v in found
                if all(
                    a == b
                    for j, (a, b) in enumerate(zip(v.tunables, best.tunables))
                    if j != i
                )
            ]
            batch = [default] + [v for v in line if v is not default]
            ran |= measure_steps(
                table,
                batch,
                timing,
                repeats,
                values,
                inputs,
                cache,
                remeasure and not ran,
                [twin_of[v.key] for v in batch] if twins else (),
                fit_cache,
                log,
            )
            built = [v for v in line if v.key in table.steps]
            found = [v for v in found if v not in line or v in built]
            fastest = min(
                (v for v in built if table.steps[v.key].accurate),
                key=lambda v: table.steps[v.key].t_step_us,
            )
            if table.steps[fastest.key].t_step_us < table.steps[best.key].t_step_us:
                best, moved = fastest, True
    return ran


def calibrate(
    table: CostTable,
    a: Operator,
    b: Operator,
    timing: Timing = Timing(),
    pairs: int = 4,
) -> Calibration:
    """Split a configure's cost over measured designs ``a`` and ``b`` into
    ``table``: on an xclbin chain, the mean of their loads and the dispatch,
    which the runs of one design alone give with the grouped run.
    """
    ka, kb = cost_key(a), cost_key(b)
    ta, tb = table.steps[ka].t_step_us, table.steps[kb].t_step_us
    tag = f"{ka}_{kb}"
    fused = table.dispatch == "fused"
    runlists = {
        f"alt{pairs}": [a, b] * pairs,
        f"grp{pairs}": [a] * pairs + [b] * pairs,
        "a": [a],
        "b": [b],
    }
    if fused:
        runlists["pack"] = [a, b]
    runs = [
        Standalone(
            f"cal_{name}_{tag}",
            runlist,
            coresident=[[a, b]] if name == "pack" else (),
            dispatch=table.dispatch,
        )
        for name, runlist in runlists.items()
    ]
    times = [t.us for t in time_interleaved([r.callable for r in runs], timing)]
    alt, grp, alone_a, alone_b = times[:4]
    switch = (alt - grp) / (2 * pairs - 2)  # (E(a) + E(b)) / 2
    reset = base = 0.0
    if fused:
        dispatch = grp - pairs * (ta + tb) - 2 * switch
        reset = ((alone_a - ta) + (alone_b - tb) - 2 * switch) / 2 - dispatch
        base = 2 * switch - (times[4] - ta - tb - reset - dispatch)
    else:
        # alone = F + c: the step times of this batch, not of the table's.
        dispatch = (pairs * (alone_a + alone_b) + 2 * switch - grp) / (2 * pairs - 1)
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


def measure_loads(
    table: CostTable,
    found: Sequence[Variant],
    reference: Variant,
    timing: Timing = Timing(),
    pairs: int = 4,
    values: Mapping[str, int] | None = None,
    inputs: Mapping[str, np.ndarray] | None = None,
    cache: CostCache | None = None,
    remeasure: bool = False,
) -> list[str]:
    """Measure into ``table`` the entry of each setting in ``found`` beside
    ``reference``: ``[reference, k]`` alternating ``pairs`` times, against
    each grouped, gives ``E(reference) + E(k)``, the step times and the
    dispatch cancelling.

    Args:
        reference: A design the table's calibrations solve the entry of,
            run with random inputs at no per-call value.
        values: The per-call values `found` is run at.
        inputs: What `found`'s input buffers hold, by buffer name.
        cache: Entries it holds are taken from it rather than run, unless
            `remeasure`; those run are written to it.

    Returns:
        The settings run on the device, each ``"reference>key"``.

    Raises:
        ValueError: A design is not in `table`, or `cache` is for another
            power mode than the NPU's.
    """
    for v in [reference, *found]:
        if v.key not in table.steps:
            raise ValueError(f"{v.key} is not in the table")
    mode = pmode()
    if cache is not None and cache.mode != mode:
        raise ValueError(f"the cost cache is for power mode {cache.mode}, not {mode}")
    entries = [None] * len(found)
    if cache is not None:
        after = cache.key(reference.resolved, dispatch=table.dispatch)
        entries = [
            cache.paired_key(
                after, cache.key(v.resolved, values, inputs, table.dispatch)
            )
            for v in found
        ]
    paired: dict[str, Pairing] = {}
    if cache is not None and not remeasure:
        for v, entry in zip(found, entries):
            held = cache.get(entry, Pairing)
            if held is not None:
                paired[v.key] = held
    todo = [(v, e) for v, e in zip(found, entries) if v.key not in paired]
    ran = []
    size = CONTEXTS // 2
    for begin in range(0, len(todo), size):
        batch = todo[begin : begin + size]
        runs = []
        for v, _ in batch:
            nbytes = sum(b.nbytes for op in (reference.op, v.op) for b in op.buffers)
            for name, runlist in (
                (f"alt{pairs}", [reference.op, v.op] * pairs),
                (f"grp{pairs}", [reference.op] * pairs + [v.op] * pairs),
            ):
                runs.append(
                    Standalone(
                        f"load_{name}_{reference.key}_{v.key}",
                        runlist,
                        values={v.op: values or {}},
                        distinct=nbytes <= DISTINCT_BYTES,
                        inputs={v.op: inputs or {}},
                        dispatch=table.dispatch,
                    )
                )
        times = time_interleaved([r.callable for r in runs], timing)
        for i, (v, entry) in enumerate(batch):
            alt, grp = times[2 * i], times[2 * i + 1]
            paired[v.key] = Pairing(
                pair_us=(alt.us - grp.us) / (pairs - 1),
                pmode=mode,
                rounds=min(alt.rounds, grp.rounds),
                calls=timing.calls,
                measured=CostTable.today(),
            )
            if cache is not None:
                cache.put(entry, paired[v.key])
            ran.append(f"{reference.key}>{v.key}")
        # A probe holds its context while it lives; the next batch needs them.
        del runs
    for v in found:
        table.record_step(
            v.key,
            dataclasses.replace(
                table.steps[v.key],
                beside=reference.key,
                pair_us=paired[v.key].pair_us,
            ),
        )
    return ran


@dataclasses.dataclass(frozen=True)
class Call:
    """One call of a traced graph version, as its designs are measured at:
    the graph's per-call values, and what any buffer whose contents a step's
    time follows holds, by graph buffer name. A graph ``folded`` from
    another names it in ``folded_from``: a design of its own is then priced
    beside the one whose step it took.
    """

    traced: TracedGraph
    values: Mapping[str, int] = dataclasses.field(default_factory=dict)
    contents: Mapping[str, np.ndarray] = dataclasses.field(default_factory=dict)
    folded_from: TracedGraph | None = None

    @classmethod
    def admitted(
        cls,
        traced: TracedGraph,
        dev,
        values: Mapping[str, int] | None = None,
        contents: Mapping[str, np.ndarray] | None = None,
    ) -> list[Call]:
        """The calls a version's tuning is priced by: ``traced`` with
        ``values`` and ``contents``, then ``traced`` folded each way it folds
        on ``dev`` (``foldings``) and with each of those folds alone.
        """
        values, contents = values or {}, contents or {}
        made = Made(dev)
        ways, _ = foldings(traced, dev, made=made)
        for fold in dict.fromkeys(f for applied in ways for f in applied):
            trial, applied = folded(traced, dev, (fold,), made=made)
            ways.setdefault(frozenset(applied), (trial, applied))
        return [cls(traced, values, contents)] + [
            cls(trial, values, contents, traced)
            for trial, applied in ways.values()
            if applied
        ]

    def op_values(self, op: Operator) -> dict[str, int]:
        """The per-call values ``op`` is written in this call, by member name."""
        return {
            b.member.name: b.expression.evaluate(self.values)
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


@dataclasses.dataclass(frozen=True)
class Designs:
    """The designs of a set of calls as ``measure_graph`` measures them,
    without a device: each design's first operator and the call it runs in,
    its settings (``variants`` of it at its probe that the placer takes,
    ``fitting``), and for a design a folded call has of its own, the design
    whose step it took. ``versions`` are the graphs the calls are of, as
    traced, and ``dev`` the device.
    """

    first: dict[str, tuple[Operator, Call]]
    settings: dict[str, list[Variant]]
    twin_of: dict[str, str]
    refused: dict[str, str]
    versions: tuple[TracedGraph, ...]
    dev: Device

    @classmethod
    def of(cls, calls: Sequence[Call], dev, fit_cache: Path = FIT_CACHE) -> Designs:
        """The designs of ``calls`` on ``dev``.

        Args:
            calls: The calls whose graphs are measured.
            dev: The device.
            fit_cache: Where the placer's verdicts persist.

        Raises:
            ValueError: A call is folded from a graph no call has.
        """
        first: dict[str, tuple[Operator, Call]] = {}
        pinned: dict[str, frozenset[str]] = {}
        twin_of: dict[str, str] = {}
        keyed: dict[int, str] = {}
        for call in calls:
            keys = cost_keys(call.traced, dev, keyed)
            for key, step in zip(keys, call.traced.steps):
                pinned[key] = pinned.get(key, frozenset()) | step.op.pinned
            for key in Runlist(keys).order:
                step = call.traced.steps[keys.index(key)]
                first.setdefault(key, (step.op, call))
            if call.folded_from is not None:
                for old, new in replaced(call.folded_from, call.traced):
                    twin_of.setdefault(cost_key(new, dev), cost_key(old, dev))
        # The tuner applies a setting to every operator of its design, so
        # one moves no tunable any of them pins (``JointNarrowing``).
        settings, refused = {}, {}
        for key, (op, _) in first.items():
            found = variants(op.probed(), dev, pinned[key])
            settings[key], why = fitting(found, fit_cache)
            refused.update(why)
        if not set(twin_of.values()) <= settings.keys():
            raise ValueError("a call is folded from a graph no call measures")
        versions = tuple(c.traced for c in calls if c.folded_from is None)
        return cls(first, settings, twin_of, refused, versions, dev)

    def stale(self, table: CostTable) -> list[str]:
        """The designs ``table`` holds that are no setting of these."""
        current = {v.key for vs in self.settings.values() for v in vs}
        return [k for k in table.steps if k not in current]

    def unmeasured(self, table: CostTable) -> list[str]:
        """The settings ``table`` lacks that ``search`` is sure to run: each
        of a design with at most ``EXHAUSTIVE``, else its default, where
        coordinate descent starts (its path follows the times).
        """
        return [
            v.key
            for vs in self.settings.values()
            for v in (vs if len(vs) <= EXHAUSTIVE else vs[:1])
            if v.key not in table.steps
        ]

    def calibrated(
        self, table: CostTable, pairs: Sequence[tuple[str, str]]
    ) -> list[tuple[Variant, Variant]]:
        """The designs each of ``pairs`` is calibrated between: the first
        design of each operator class, at its narrowest setting ``table``
        holds whose other tunables are the default's.
        """
        by_class: dict[str, Variant] = {}
        for key, (op, _) in self.first.items():
            default = self.settings[key][0]
            fixed = {
                n: x for n, x in default.tunables if n not in default.resolved.widths
            }
            narrowest = min(
                (
                    v
                    for v in self.settings[key]
                    if v.key in table.steps
                    and fixed.items() <= dict(v.tunables).items()
                ),
                key=lambda v: v.mm2s + v.s2mm,
            )
            by_class.setdefault(type(op).__name__, narrowest)
        return [(by_class[a], by_class[b]) for a, b in pairs]

    def unloaded(
        self, table: CostTable, chosen: Sequence[tuple[Variant, Variant]]
    ) -> list[Variant]:
        """The measured settings of ``table`` whose entry ``measure_loads``
        would run beside the first of the ``chosen`` calibrated designs,
        which are solved by their calibrations.
        """
        if not chosen:
            return []
        reference = chosen[0][0]
        solved = {v.key for pair in chosen for v in pair}
        return [
            v
            for vs in self.settings.values()
            for v in vs
            if v.key in table.steps
            and v.key not in solved
            and table.steps[v.key].beside != reference.key
        ]

    def unpacked(self, table: CostTable) -> list[tuple[str, ...]]:
        """The packs a full ELF's ``versions`` tuned by ``table`` take that
        it lacks, each the setting keys of one device.
        """
        if table.dispatch != "fused":
            return []
        tuner = JointNarrowing(table)
        taken = {
            table.pack_name(device): device
            for traced in self.versions
            for device in tuner.tune(traced, self.dev, table.dispatch).devices
        }
        return [device for name, device in taken.items() if name not in table.packs]

    def missing(self, table: CostTable, pairs: Sequence[tuple[str, str]]) -> list[str]:
        """What ``measure_graph`` would run for ``table`` next, in its
        return's terms: the ``unmeasured`` settings, else the calibrations
        of ``pairs`` the table lacks (``"a|b"``), which are between measured
        designs, else the ``unloaded`` settings (``"reference>key"``), else
        the ``unpacked`` packs (``CostTable.pack_name``).
        """
        designs = self.unmeasured(table)
        if designs:
            return designs
        chosen = self.calibrated(table, pairs)
        calibrations = [
            f"{a.key}|{b.key}"
            for a, b in chosen
            if f"{a.key}|{b.key}" not in table.calibrations
        ]
        if calibrations:
            return calibrations
        loads = [f"{chosen[0][0].key}>{v.key}" for v in self.unloaded(table, chosen)]
        if loads or not chosen:
            return loads
        return [table.pack_name(device) for device in self.unpacked(table)]


def measure_graph(
    table: CostTable,
    calls: Sequence[Call],
    pairs: Sequence[tuple[str, str]],
    timing: Timing = Timing(),
    repeats: int = 9,
    remeasure: bool = False,
    log: Callable[[str], None] = print,
    cache: CostCache | None = None,
) -> list[str]:
    """Measure every design of ``calls``' graphs into ``table``, saved as it
    goes: each at the settings ``variants`` gives that ``search`` runs, in
    the first call that runs it, then the configure cost between each of
    ``pairs``, the first designs of those operator classes at their
    narrowest measured width, each other setting's entry beside the
    first of those (``measure_loads``), and on a full ELF the packs the
    versions' tunings take, each as one device (``measure_packs``), until
    they take none the table lacks or ``PACK_ROUNDS`` have. Designs, entries,
    packs and calibrations already in the table or ``cache`` (this NPU's
    ``cost_cache()`` if not given) are kept unless ``remeasure``; those the
    graphs no longer have are dropped from the table. A design a folded
    call has of its own is measured beside the one whose step it took, at
    each setting both have that the other's ``search`` measured
    (``measure_steps``' `twins`); the call it is folded from comes first.

    Returns:
        The design keys, calibration pairs (``"a|b"``), entries
        (``"reference>key"``) and packs (``CostTable.pack_name``) run on the
        device.

    Raises:
        ValueError: ``pairs`` leave a calibrated design's entry undetermined:
            they close no odd cycle, as a triangle does.
    """
    dev = aie_utils.ensure_current_device()
    table.measures(dev)
    if cache is None:
        cache = cost_cache()
    designs = Designs.of(calls, dev)
    found, twin_of = designs.settings, designs.twin_of
    stale = designs.stale(table)
    for k in stale:
        del table.steps[k]
    for name in [
        n
        for n in table.packs
        if remeasure or not set(n.split("|")) <= table.steps.keys()
    ]:
        del table.packs[name]
    if stale:
        log(f"dropped {len(stale)} designs the graphs no longer have")
    for k, why in designs.refused.items():
        first_line, _, _ = why.partition("\n")
        log(f"not measured, the placer refuses {k}: {first_line}")

    ran = []
    for i, (key, (op, call)) in enumerate(designs.first.items()):
        name = type(op).__name__
        if not remeasure and all(v.key in table.steps for v in found[key]):
            log(f"[{i}/{len(designs.first)}] {name}: in the table")
            continue
        values = call.op_values(op)
        twins = []
        if twin_of.get(key, key) != key:
            # Descent measures only the settings on its path.
            settings = {
                v.tunables: v for v in found[twin_of[key]] if v.key in table.steps
            }
            twins = [settings.get(v.tunables) for v in found[key]]
        log(
            f"[{i}/{len(designs.first)}] {name}: {len(found[key])} settings at "
            f"{values}, started {time.strftime('%H:%M:%S')}"
        )
        start = time.time()
        costs = search(
            table,
            found[key],
            timing,
            repeats,
            values,
            call.op_inputs(op),
            cache,
            remeasure,
            twins,
            log=log,
        )
        ran += costs
        table.save()
        log(
            f"[{i}/{len(designs.first)}] {name} ({time.time() - start:.0f}s) at {values}"
            + (f" beside {twin_of[key]}" if twins else "")
        )
        for v in found[key]:
            if v.key not in table.steps:
                continue
            c = table.steps[v.key]
            log(
                f"    {dict(v.tunables)}: t_step {c.t_step_us:8.2f} us  "
                f"alone {c.alone_us:8.2f} us  exact {c.exact}  accurate {c.accurate}"
                + ("" if v.key in costs else "  (cached)")
            )

    chosen = designs.calibrated(table, pairs)
    wanted = {f"{a.key}|{b.key}" for a, b in chosen}
    for k in [k for k in table.calibrations if k not in wanted]:
        del table.calibrations[k]
    for (a, b), (name_a, name_b) in zip(chosen, pairs):
        pair = f"{a.key}|{b.key}"
        if not remeasure and pair in table.calibrations:
            log(f"calibration {name_a}/{name_b}: in the table")
            continue
        entry = cache.pair_key(
            cache.key(a.resolved, dispatch=table.dispatch),
            cache.key(b.resolved, dispatch=table.dispatch),
        )
        cal = None if remeasure else cache.get(entry, Calibration)
        if cal is None:
            cal = calibrate(table, a.op, b.op, timing)
            cache.put(entry, cal)
            ran.append(pair)
        else:
            table.record_calibration((a.key, b.key), cal)
        table.save()
        log(
            f"calibration {name_a}/{name_b}: D0 {cal.dispatch_us:.1f}  "
            f"R {cal.reset_us:.1f}  base {cal.base_us:.1f}  "
            f"switch {cal.switch_us:.1f} us" + ("" if pair in ran else "  (cached)")
        )

    if not chosen:
        log("no calibration pairs: no design's load is measured")
    undetermined = [k for k, e in table.entry_costs().items() if e is None]
    if undetermined:
        raise ValueError(
            f"calibration pairs {list(pairs)} do not determine the entries of "
            f"{undetermined}; pairs closing an odd cycle, a triangle, would"
        )
    # Every step measured again was recorded afresh, with no load.
    unloaded = {v.key for v in designs.unloaded(table, chosen)}
    for key, (op, call) in designs.first.items():
        settings = [v for v in found[key] if v.key in unloaded]
        if not settings:
            continue
        reference = chosen[0][0]
        loaded = measure_loads(
            table,
            settings,
            reference,
            timing,
            values=call.op_values(op),
            inputs=call.op_inputs(op),
            cache=cache,
            remeasure=remeasure,
        )
        ran += loaded
        table.save()
        log(f"loads of {type(op).__name__} beside {reference.key}:")
        for v in settings:
            c = table.steps[v.key]
            log(
                f"    {dict(v.tunables)}: E + E(reference) {c.pair_us:8.2f} us"
                + ("" if f"{reference.key}>{v.key}" in loaded else "  (cached)")
            )

    references = list({v.key: v for pair in chosen for v in pair}.values()) + [
        v
        for vs in found.values()
        for v in vs
        if v.key in table.steps and table.steps[v.key].beside is not None
    ]
    for _ in range(PACK_ROUNDS):
        unpacked = designs.unpacked(table) if chosen else []
        if not unpacked:
            break
        ran += measure_packs(
            table,
            unpacked,
            designs,
            references,
            timing,
            repeats,
            cache=cache,
            remeasure=remeasure,
            log=log,
        )
    table.save()
    return ran


def measure_packs(
    table: CostTable,
    devices: Sequence[Sequence[str]],
    designs: Designs,
    references: Sequence[Variant],
    timing: Timing = Timing(),
    repeats: int = 9,
    pairs: int = 4,
    cache: CostCache | None = None,
    remeasure: bool = False,
    log: Callable[[str], None] = print,
) -> list[str]:
    """Measure into a full ELF's ``table`` each of ``devices``, the setting
    keys of designs sharing one device, as that device: the pack
    alternating with a reference against each grouped gives
    ``E(reference) + E(pack)`` as ``measure_loads`` does, and each member
    repeated on the device, against the members once, its step there.

    Args:
        designs: The designs the settings are of; each is run at the
            values and on the inputs of the call it first runs in.
        references: Designs whose loads the table holds, in the order
            preferred; a pack is run beside the first that is none of its
            members, with random inputs at no per-call value.
        cache: Packs it holds are taken from it rather than run, unless
            `remeasure`; those run are written to it.

    Returns:
        The packs run on the device, by ``CostTable.pack_name``.

    Raises:
        ValueError: `table` prices an xclbin chain, a key is no setting of
            `designs`, a pack has more members than the device's contexts
            measure at once or holds every reference, or `cache` is for
            another power mode than the NPU's.
    """
    if table.dispatch != "fused":
        raise ValueError(f"{table.path} prices an xclbin chain: it packs no designs")
    mode = pmode()
    if cache is not None and cache.mode != mode:
        raise ValueError(f"the cost cache is for power mode {cache.mode}, not {mode}")
    of = {
        v.key: (v, *designs.first[design])
        for design, vs in designs.settings.items()
        for v in vs
    }
    ran = []
    for keys in devices:
        keys = list(dict.fromkeys(keys))
        strays = [k for k in keys if k not in of]
        if strays:
            raise ValueError(f"{strays} are no settings of these designs")
        if len(keys) + 3 > CONTEXTS:
            raise ValueError(
                f"a pack of {len(keys)} needs more than {CONTEXTS} contexts"
            )
        # Beside one of its own members the pack never leaves its device.
        reference = next((r for r in references if r.key not in keys), None)
        if reference is None:
            raise ValueError(
                f"the pack {keys} holds every reference; measure another "
                f"design's load to run it beside"
            )
        members = [of[k] for k in keys]
        ops = [v.op for v, _, _ in members]
        values = {v.op: call.op_values(op) for v, op, call in members}
        inputs = {v.op: call.op_inputs(op) for v, op, call in members}
        name = table.pack_name(keys)
        entry = None
        if cache is not None:
            entry = cache.pack_key(
                cache.key(reference.resolved, dispatch=table.dispatch),
                [
                    cache.key(v.resolved, values[v.op], inputs[v.op], table.dispatch)
                    for v, _, _ in members
                ],
            )
        pack = None if entry is None or remeasure else cache.get(entry, PackCost)
        if pack is None:
            nbytes = sum(b.nbytes for op in [reference.op, *ops] for b in op.buffers)
            runlists = [
                [reference.op, *ops] * pairs,
                [reference.op] * pairs + ops * pairs,
                ops,
            ] + [ops[:j] + [ops[j]] * repeats + ops[j + 1 :] for j in range(len(ops))]
            runs = [
                Standalone(
                    f"pack{n}_{reference.key}_{name}",
                    runlist,
                    coresident=[ops],
                    values=values,
                    distinct=nbytes <= DISTINCT_BYTES,
                    inputs=inputs,
                    dispatch=table.dispatch,
                )
                for n, runlist in enumerate(runlists)
            ]
            times = time_interleaved([r.callable for r in runs], timing)
            del runs
            alt, grp, once = times[:3]
            pack = PackCost(
                beside=reference.key,
                pair_us=(alt.us - grp.us) / (pairs - 1),
                t_step_us={
                    k: (t.us - once.us) / (repeats - 1) for k, t in zip(keys, times[3:])
                },
                pmode=mode,
                rounds=min(t.rounds for t in times),
                calls=timing.calls,
                measured=CostTable.today(),
            )
            if cache is not None:
                cache.put(entry, pack)
            ran.append(name)
        table.record_pack(keys, pack)
        table.save()
        log(
            f"pack {name}: entry {table.pack_entry(name):.1f} us, steps "
            + ", ".join(f"{t:.2f}" for t in pack.t_step_us.values())
            + ("" if name in ran else "  (cached)")
        )
    return ran
