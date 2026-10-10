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
- ``measure_points``: a design run at each of its call's operating points
  (``Call.points``, where they write it different bound extents) against
  as many steps at the call's own values, interleaved, gives its step at
  each point (``StepCost.points``).
- ``measure_graph``: every design of the versions it is given, each in a
  ``Call`` of its version, then its operating points, then the
  calibrations, then each design's entry.
- ``check_model``: a tuned version timed against the untuned one, each
  beside the model's prediction for it.

Figures are medians of per-round medians, interleaved, of the run alone (the
callable's ``last_elapsed``), a setting far behind the fastest over fewer
rounds (``Timing``). Nothing else may dispatch meanwhile: a round starts
once no other process holds the NPU, and is timed again if one holds it
when the round ends.
"""

from __future__ import annotations

import dataclasses
import hashlib
import json
import math
import os
import statistics
import subprocess
import sys
import tempfile
import time
from collections.abc import Callable, Collection, Hashable, Mapping, Sequence
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
from aie.iron.device import Device
from aie.utils import bfp

from ..declare import Direction, Operator
from ..declare.bound import BoundBuffer, BoundValue
from ..declare.operator import _PlaceWord
from ..design import OperatorDesign, device_symbol
from ..image.callable import FullELFCallable, StepCallable
from ..image.sequence import OperatorSequence
from .compiled import CompiledGraph
from .costcache import Accuracy, CostCache, Measurement, Pairing, Shift
from .fold import Made, folded, foldings, replaced
from .narrowing import (
    CONFIDENCE,
    FIT_CACHE,
    Calibration,
    CostTable,
    JointNarrowing,
    PackCost,
    PointCost,
    Runlist,
    StepCost,
    Variant,
    cost_key,
    cost_keys,
    fit_verdict,
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
    """A run's per-round medians, microseconds, and their median ``us``."""

    round_us: tuple[float, ...]

    @property
    def us(self) -> float:
        return statistics.median(self.round_us)

    @property
    def rounds(self) -> int:
        return len(self.round_us)


def standard_error(samples: Sequence[float]) -> float | None:
    """The standard error of the median of ``samples``, taken as normal
    (sqrt(pi / 2) times the mean's); None from fewer than two.
    """
    if len(samples) < 2:
        return None
    return math.sqrt(math.pi / 2) * statistics.stdev(samples) / math.sqrt(len(samples))


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


def others() -> set[int]:
    """The processes other than this one holding a context on the NPU, by
    pid, as ``xrt-smi`` reports its partitions.
    """
    with tempfile.TemporaryDirectory() as d:
        report = Path(d) / "partitions.json"
        subprocess.run(
            ["xrt-smi", "examine", "-r", "aie-partitions", "-f", "JSON", "-o", report],
            capture_output=True,
            check=True,
        )
        devices = json.loads(report.read_text())["devices"]
    return {
        int(context["pid"])
        for device in devices
        for partition in device["aie_partitions"].get("partitions", [])
        for context in partition.get("hw_contexts", [])
    } - {os.getpid()}


# Seconds between looks at an NPU another process holds, and the most waited.
IDLE_POLL = 5.0
IDLE_WAIT = 1800.0


def wait_idle(log: Callable[[str], None] = print) -> None:
    """Return once no other process holds a context on the NPU (``others``).

    Raises:
        TimeoutError: Another has held one for ``IDLE_WAIT`` seconds. Two
            processes measuring at once would each wait for the other.
    """
    held, told = others(), set()
    start = time.monotonic()
    while held:
        if held != told:
            log(f"    the NPU is in use by pid {sorted(held)}: waiting")
            told = held
        if time.monotonic() - start > IDLE_WAIT:
            raise TimeoutError(
                f"pid {sorted(held)} has held the NPU for {IDLE_WAIT:.0f} s; "
                f"measure once it is idle"
            )
        time.sleep(IDLE_POLL)
        held = others()


class Awake:
    """While entered, the calling thread on the CPUs the NPU's completions
    interrupted since ``before`` (``interrupts``), and a spinner at nice 19
    on each of their SMT siblings.

    A core in deep idle when a completion arrives adds its exit latency to
    the run, but only once the gap between completions is long enough for
    the idle governor to choose it: a probe's long runs would carry it and
    its short ones not. A busy sibling holds the core shallow without
    delaying the completion work on it, and the waiting thread is woken on
    that core.
    """

    IRQ = "xdna_mailbox"

    def __init__(self, before: Mapping[str, int]):
        self.cpus: set[int] = set()
        for irq, count in self.interrupts().items():
            if count > before.get(irq, 0):
                self.cpus |= self._cpus(f"/proc/irq/{irq}/effective_affinity_list")
        self.siblings: set[int] = set()
        for cpu in self.cpus:
            self.siblings |= self._cpus(
                f"/sys/devices/system/cpu/cpu{cpu}/topology/thread_siblings_list"
            )
        self.siblings -= self.cpus
        self._affinity: set[int] | None = None
        self._spinners: list[subprocess.Popen] = []

    @classmethod
    def interrupts(cls) -> dict[str, int]:
        """Each NPU completion interrupt's count over every CPU, by number."""
        counts = {}
        for line in Path("/proc/interrupts").read_text().splitlines():
            fields = line.split()
            if fields and fields[-1] == cls.IRQ:
                counts[fields[0].rstrip(":")] = sum(
                    int(f) for f in fields[1:] if f.isdigit()
                )
        return counts

    @staticmethod
    def _cpus(path: str) -> set[int]:
        cpus = set()
        for part in Path(path).read_text().strip().split(","):
            first, _, last = part.partition("-")
            cpus.update(range(int(first), int(last or first) + 1))
        return cpus

    def __enter__(self) -> Awake:
        if self.cpus:
            self._affinity = os.sched_getaffinity(0)
            os.sched_setaffinity(0, self.cpus)
        for cpu in sorted(self.siblings):
            spinner = subprocess.Popen([sys.executable, "-c", "while True: pass"])
            os.sched_setaffinity(spinner.pid, {cpu})
            os.setpriority(os.PRIO_PROCESS, spinner.pid, 19)
            self._spinners.append(spinner)
        return self

    def __exit__(self, *exc) -> None:
        for spinner in self._spinners:
            spinner.kill()
            spinner.wait()
        self._spinners.clear()
        if self._affinity is not None:
            os.sched_setaffinity(0, self._affinity)
            self._affinity = None


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
        load: Write the per-call values now; with `False` the image is built
            and seeded, and `load()` writes them.
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
        load: bool = True,
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
            coresident=coresident,
        ).compile()
        self.callable = self.sequence.get_callable()
        rng = np.random.default_rng(seed)
        self._before: dict[str, np.ndarray] = {}
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
                    content = self._content(buf, inputs.get(op, {}), rng)
                    at = buf.placement[1] * bfp.itemsize(buf.dtype)
                    self._bytes(name_)[at : at + buf.nbytes] = content
                    if buf.direction.drains:
                        self._before[name_] = content.copy()
        ops = {id(op): op for op in self.steps}.values()
        artifacts = self.sequence.artifacts
        # An extent read only through its derivations has no word in a full
        # ELF; an xclbin chain has no parameter table, its values dispatch-time.
        self._symbols = {
            device_symbol(op, v): np.int32(self._value(op, self._values[op], v))
            for op in ops
            for v in op.values
            if artifacts.kind == "xclbin"
            or device_symbol(op, v) in artifacts.parameters
        }
        if load:
            self.load()

    def load(self) -> None:
        """Write the per-call values, which loads a full ELF that holds any;
        any other image is loaded by its first run.
        """
        if self._symbols:
            self.callable.write_values(self._symbols)

    @staticmethod
    def _value(op: Operator, values: Mapping[str, int], v: BoundValue) -> int:
        # Each operand here is a buffer of its own: a placed one at its run.
        if isinstance(v.member, _PlaceWord):
            return 0
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
        return self.callable.get_storage(name).numpy_view().view(np.uint8)

    def address(self, name: str) -> int:
        """The device address of buffer ``name``."""
        view = self.callable.get_storage(name)
        root = view.storage.binding_handle(0, view.storage.nbytes)
        return root.address() + view.storage_offset

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
                at = buf.placement[1] * bfp.itemsize(buf.dtype)
                data = self._before.get(name, self._bytes(name)[at : at + buf.nbytes])
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
            at = buf.placement[1] * bfp.itemsize(buf.dtype)
            data = self.callable.get_storage(name).numpy().view(np.uint8)
            data = data[at : at + buf.nbytes].reshape(*buf.shape, -1)
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
    want = op.call_reference(inputs, values=values)
    for which, gate in gates.items():
        for name, verdict in op.judge(inputs, written, gate, want).items():
            if not verdict:
                detail = f"{name} under {which} gate: {verdict.detail}"
                return Accuracy(False, detail)
    return Accuracy(True, "")


def time_interleaved(
    runs: Sequence[FullELFCallable | StepCallable],
    timing: Timing,
    groups: Sequence[Hashable | None] = (),
    fastest: float = math.inf,
    log: Callable[[str], None] = print,
) -> list[Timed]:
    """Each loaded image's median of per-round medians, microseconds.

    A round starts once no other process holds the NPU (``wait_idle``), and
    one that ends with another holding it is timed again. The cores the
    runs' completions interrupt are held ``Awake`` throughout.

    Args:
        groups: Per run, the setting it measures, where the runs are
            settings of one design; a setting is timed no further once its
            slowest run is past ``timing.cutoff`` times the fastest
            setting's (``Timing``). None marks a run never stopped. Every
            run is timed every round if not given.
        fastest: The slowest run of the fastest setting timed before these.
        log: Where waiting for the NPU, or a round timed again, is reported.
    """
    for run in runs:
        run()  # warm: first-run setup lands on nobody's figure
    # Which interrupts a call raises, its first one's setup aside.
    before = Awake.interrupts()
    for run in runs:
        run()
    medians: list[list[float]] = [[] for _ in runs]
    live = set(range(len(runs)))
    wait_idle(log)
    r = 0
    with Awake(before):
        while r < timing.rounds:
            timed = {}
            for i, run in enumerate(runs):
                if i not in live:
                    continue
                times = []
                for _ in range(timing.calls):
                    run()
                    times.append(run.last_elapsed)
                timed[i] = statistics.median(times) * 1e6
            held = others()
            if held:
                log(
                    f"    pid {sorted(held)} used the NPU during a round: timing it again"
                )
                wait_idle(log)
                continue
            for i, us in timed.items():
                medians[i].append(us)
            r += 1
            if not groups or r < timing.settle:
                continue
            slowest: dict[Hashable, float] = {}
            for i in live:
                us = statistics.median(medians[i])
                slowest[groups[i]] = max(slowest.get(groups[i], 0.0), us)
            bar = timing.cutoff * min([fastest, *slowest.values()])
            live = {i for i in live if groups[i] is None or slowest[groups[i]] <= bar}
    return [Timed(tuple(m)) for m in medians]


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
    earlier: Collection[str] = (),
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
            Any other but the default is priced so beside the default,
            which each batch times. A one-run figure is its own: one run's
            noise exceeds the drift.
        fit_cache: Where a width that does not build is recorded as
            refused (``refuse``), so ``fitting`` leaves it out from then on.
        log: Where a width that does not build is reported.
        earlier: Widths run earlier in this search, taken from `cache` even
            under `remeasure`.

    Returns:
        The widths run on the device, by key. One other than the default
        that does not build is left out of it and of ``table``.

    Raises:
        RuntimeError: The default or a twin does not build.
        ValueError: `cache` or `table` is for another power mode than the
            NPU's, or a twin is not in `table`.
    """
    mode = pmode()
    if cache is not None and cache.mode != mode:
        raise ValueError(f"the cost cache is for power mode {cache.mode}, not {mode}")
    table.measures_at(mode)
    twins = list(twins) or [None] * len(found)
    for t in twins:
        if t is not None and t.key not in table.steps:
            raise ValueError(f"twin {t.key} is not in the table")
    default = found[0]
    partners = [twins[0]] + [default if t is None else t for t in twins[1:]]
    entries = [
        None if cache is None else cache.key(v.resolved, values, inputs, table.dispatch)
        for v in found
    ]
    besides = [
        (
            None
            if cache is None or p is None
            else cache.beside_key(
                (
                    entries[0]
                    if p is default
                    else cache.key(p.resolved, values, inputs, table.dispatch)
                ),
                e,
            )
        )
        for p, e in zip(partners, entries)
    ]
    held: dict[str, Measurement] = {}
    near: dict[str, Measurement] = {}
    if cache is not None:
        for v, entry, beside in zip(found, entries, besides):
            if remeasure and v.key not in earlier:
                continue
            m = cache.get(entry, Measurement)
            b = None if beside is None else cache.get(beside, Measurement)
            if m is not None and (beside is None or b is not None):
                held[v.key] = m
                if b is not None:
                    near[v.key] = b
    todo = [
        (v, e, p, b)
        for v, e, p, b in zip(found, entries, partners, besides)
        if v.key not in held
    ]
    distinct = sum(b.nbytes for b in default.op.buffers) <= DISTINCT_BYTES
    measured: dict[str, Measurement] = {}
    fastest = math.inf
    # Each run is two contexts; a batch keeps two for the default it is priced beside.
    size = (CONTEXTS - 2 * any(p is default for p in partners)) // (
        4 if any(t is not None for t in twins) else 2
    )
    failed: set[str] = set()
    batches = math.ceil(len(todo) / size)
    log(f"    {len(todo)} to run, {len(held)} from the cache, {batches} batches")
    for begin in range(0, len(todo), size):
        batch = todo[begin : begin + size]
        log(f"    batch {begin // size + 1}/{batches}: building {len(batch)}")
        own = {v.key for v, _, _, _ in batch}
        # A twin is stopped with the width it is run beside; the default never is.
        group_of = {
            p.key: v.key for v, _, p, _ in batch if p is not None and p is not default
        }
        designs, short, long = [], [], []
        for d in [v for v, _, _, _ in batch] + list(
            {
                p.key: p for _, _, p, _ in batch if p is not None and p.key not in own
            }.values()
        ):
            if group_of.get(d.key, d.key) in failed:
                continue
            try:
                one = Standalone(
                    f"probe1_{d.key}",
                    [d.op],
                    values={d.op: values or {}},
                    inputs={d.op: inputs or {}},
                    dispatch=table.dispatch,
                    load=False,
                )
                many = Standalone(
                    f"probe{repeats}_{d.key}",
                    [d.op] * repeats,
                    values={d.op: values or {}},
                    distinct=distinct,
                    inputs={d.op: inputs or {}},
                    dispatch=table.dispatch,
                    load=False,
                )
            except RuntimeError as e:
                # The placer passed it, but the build did not. The default
                # is the graph's own and a twin was measured, so both build.
                if d is default or d.key not in own:
                    raise
                failed.add(d.key)
                refuse({d.key: OperatorDesign(d.resolved)}, str(e), fit_cache)
                log(f"{dict(d.tunables)} does not build, not measured: {e}")
                continue
            # A load that fails is the device's state, not a verdict on the design.
            one.load()
            many.load()
            designs.append(d)
            short.append(one)
            long.append(many)
        if not own - failed:
            continue
        log(f"    batch {begin // size + 1}/{batches}: timing {len(designs)} runs")
        # The default is the untuned graph's figure: always timed in full.
        groups = [
            None if d is default else group_of.get(d.key, d.key) for d in designs
        ] * 2
        outputs = [run.digest() for run in short]
        times = time_interleaved(
            [r.callable for r in short + long], timing, groups, fastest, log
        )
        n = len(designs)
        ran: dict[str, Measurement] = {}
        slowest: dict[str, float] = {}
        for i, d in enumerate(designs):
            t_step = (times[n + i].us - times[i].us) / (repeats - 1)
            ran[d.key] = Measurement(
                t_step_us=t_step,
                # A design's two runs are stopped together, so their rounds pair.
                round_us=[
                    (many - one) / (repeats - 1)
                    for one, many in zip(times[i].round_us, times[n + i].round_us)
                ],
                alone_us=times[i].us - t_step,
                output=outputs[i],
                pmode=mode,
                calls=timing.calls,
            )
            of = group_of.get(d.key, d.key)
            slowest[of] = max(slowest.get(of, 0.0), times[n + i].us)
        for v, entry, p, beside in batch:
            if v.key in failed:
                continue
            measured[v.key] = ran[v.key]
            if p is not None:
                near[v.key] = ran[p.key]
            if cache is not None:
                cache.put(entry, ran[v.key])
                if p is not None:
                    cache.put(beside, ran[p.key])
        fastest = min(fastest, *slowest.values())
        # A probe holds its context while it lives; the next batch needs them.
        del short, long
    found, entries, partners = zip(
        *((v, e, p) for v, e, p in zip(found, entries, partners) if v.key not in failed)
    )
    known = held | measured
    reference = known[default.key].output
    judging = [
        (v, e)
        for v, e in zip(found, entries)
        if v is default or known[v.key].output != reference
    ]
    accurate = judged(*zip(*judging), table.dispatch, values, inputs, cache, remeasure)
    # A width is priced at its partner's figure plus their difference in the
    # run that timed both, so a drift between that run and the partner's own
    # does not reach it.
    priced: dict[str, tuple[float, float | None]] = {}
    off_twin: float | None = None
    for v, p in zip(found, partners):
        m = known[v.key]
        if p is None:
            priced[v.key] = (m.t_step_us, standard_error(m.round_us))
        else:
            delta = m.t_step_us - near[v.key].t_step_us
            paired = standard_error(
                [s - r for s, r in zip(m.round_us, near[v.key].round_us)]
            )
            if p is default:
                priced[v.key] = (priced[default.key][0] + delta, paired)
            else:
                # Against its default through the twins: theirs, and each
                # one's difference from its twin.
                twin = table.steps[p.key]
                noises = [twin.noise_us, paired] + ([] if v is default else [off_twin])
                if v is default:
                    off_twin = paired
                priced[v.key] = (
                    twin.t_step_us + delta,
                    (
                        None
                        if None in noises
                        else math.sqrt(sum(noise**2 for noise in noises))
                    ),
                )
        table.record_step(v.key, m.cost(reference, v.key in accurate, *priced[v.key]))
    return {key: table.steps[key] for key in measured}


def judged(
    found: Sequence[Variant],
    entries: Sequence[str | None],
    dispatch: str,
    values: Mapping[str, int] | None = None,
    inputs: Mapping[str, np.ndarray] | None = None,
    cache: CostCache | None = None,
    remeasure: bool = False,
) -> set[str]:
    """The settings of ``found`` that ``judge`` finds within their gates,
    each run once at ``values`` on ``inputs``, packaged as ``dispatch``:
    ``found[0]`` the default, each other one whose output is not the
    default's; none where the default's own gate refuses it.

    Args:
        entries: Each setting's entry in `cache`, whose verdicts are taken
            from it unless `remeasure`; those judged are written to it.
    """
    accurate: set[str] = set()
    if len(found) < 2:
        return accurate
    default = found[0]
    for v, entry in zip(found, entries):
        key = (
            None
            if cache is None
            else cache.judged_key(entries[0], entry, default.op, v.op)
        )
        verdict = None if key is None or remeasure else cache.get(key, Accuracy)
        if verdict is None:
            run = Standalone(
                f"judge_{v.key}",
                [v.op],
                values={v.op: values or {}},
                inputs={v.op: inputs or {}},
                dispatch=dispatch,
            )
            run.digest()
            verdict = judge(
                default.op, v.op, run.inputs(), run.written(), values
            ) or Accuracy(False, "not judged")
            del run
            if key is not None:
                cache.put(key, verdict)
        if verdict.within:
            accurate.add(v.key)
        elif v is default:
            break  # a default its own gate refuses admits no inexact width
    return accurate


# A round times each run at an operating point for about this long at most:
# a long run's shift from its call's values dwarfs its noise.
POINT_ROUND_S = 0.5


def measure_points(
    table: CostTable,
    found: Sequence[Variant],
    points: Mapping[str, tuple[float, Mapping[str, int]]],
    values: Mapping[str, int] | None = None,
    inputs: Mapping[str, np.ndarray] | None = None,
    timing: Timing = Timing(),
    repeats: int = 9,
    cache: CostCache | None = None,
    remeasure: bool = False,
) -> list[str]:
    """Measure into ``table`` each setting of ``found`` (the default first,
    each in the table) at each of ``points``: ``repeats`` steps there against
    as many at ``values``, interleaved, give how much longer a step there
    takes than ``StepCost.t_step_us``, so a drift since that was measured
    does not reach it. A setting whose output at a point is not the
    default's there is judged there (``judged``). A setting not accurate at
    ``values`` is left out: the tuner takes it nowhere.

    Args:
        points: Per label, the share of the calls priced that run there and
            the per-call values `found` is written there (``Call.op_points``).
        values: The per-call values its ``t_step_us`` is measured at.
        inputs: What `found`'s input buffers hold, by buffer name.
        timing: How long to time them; a round's runs take fewer calls
            where they are long (``POINT_ROUND_S``).
        cache: Points it holds are taken from it rather than run, unless
            `remeasure`; those run are written to it.

    Returns:
        The points run on the device, each ``"key@label"``.

    Raises:
        ValueError: A setting is not in `table`, the points and the call's
            values need more runs than the device's contexts hold, or
            `cache` is for another power mode than the NPU's.
    """
    for v in found:
        if v.key not in table.steps:
            raise ValueError(f"{v.key} is not in the table")
    if len(points) + 1 > CONTEXTS:
        raise ValueError(f"{len(points)} points need more than {CONTEXTS} contexts")
    mode = pmode()
    if cache is not None and cache.mode != mode:
        raise ValueError(f"the cost cache is for power mode {cache.mode}, not {mode}")
    found = [v for v in found if table.steps[v.key].accurate]
    labels = list(points)
    # Each setting's entry at each point, and its shift's from its own.
    entries: dict[tuple[str, str], str | None] = {}
    kept: dict[tuple[str, str], str | None] = {}
    shifts: dict[tuple[str, str], Shift] = {}
    for v in found:
        for label in labels:
            if cache is None:
                entries[v.key, label] = kept[v.key, label] = None
                continue
            entries[v.key, label] = cache.key(
                v.resolved, points[label][1], inputs, table.dispatch
            )
            kept[v.key, label] = cache.point_key(
                cache.key(v.resolved, values, inputs, table.dispatch),
                entries[v.key, label],
            )
            held = None if remeasure else cache.get(kept[v.key, label], Shift)
            if held is not None:
                shifts[v.key, label] = held
    todo = [v for v in found if any((v.key, l) not in shifts for l in labels)]
    distinct = sum(b.nbytes for b in found[0].op.buffers) <= DISTINCT_BYTES
    runs_each = len(labels) + 1
    size = CONTEXTS // runs_each
    ran = []
    for begin in range(0, len(todo), size):
        batch = todo[begin : begin + size]
        runs = [
            Standalone(
                f"point{repeats}_{v.key}",
                [v.op] * repeats,
                values={v.op: at},
                distinct=distinct,
                inputs={v.op: inputs or {}},
                dispatch=table.dispatch,
            )
            for v in batch
            for at in [values or {}] + [points[label][1] for label in labels]
        ]
        outputs = [run.digest() for run in runs]
        for run in runs:
            run.callable()  # past the first run's setup
        slowest = max(run.callable.last_elapsed for run in runs)
        calls = max(1, min(timing.calls, int(POINT_ROUND_S / slowest)))
        times = time_interleaved(
            [run.callable for run in runs], dataclasses.replace(timing, calls=calls)
        )
        # A probe holds its context while it lives; the next batch needs them.
        del runs
        for i, v in enumerate(batch):
            own = times[i * runs_each]
            for j, label in enumerate(labels, 1):
                there = times[i * runs_each + j]
                shifts[v.key, label] = Shift(
                    shift_us=(there.us - own.us) / repeats,
                    # No run is stopped early, so their rounds pair.
                    round_us=[
                        (t - o) / repeats for o, t in zip(own.round_us, there.round_us)
                    ],
                    output=outputs[i * runs_each + j],
                    pmode=mode,
                    calls=calls,
                )
                if cache is not None:
                    cache.put(kept[v.key, label], shifts[v.key, label])
                ran.append(f"{v.key}@{label}")
    default = found[0]
    costs: dict[str, dict[str, PointCost]] = {v.key: {} for v in found}
    for label in labels:
        weight, at = points[label]
        reference = shifts[default.key, label].output
        judging = [
            v for v in found if v is default or shifts[v.key, label].output != reference
        ]
        accurate = judged(
            judging,
            [entries[v.key, label] for v in judging],
            table.dispatch,
            at,
            inputs,
            cache,
            remeasure,
        )
        for v in found:
            shift = shifts[v.key, label]
            exact = shift.output == reference
            costs[v.key][label] = PointCost(
                weight=weight,
                t_step_us=table.steps[v.key].t_step_us + shift.shift_us,
                noise_us=standard_error(shift.round_us),
                exact=exact,
                accurate=exact or v.key in accurate,
                calls=shift.calls,
            )
    for v in found:
        table.record_step(
            v.key, dataclasses.replace(table.steps[v.key], points=costs[v.key])
        )
    return ran


# Past this many settings, a design's tunables are searched one at a time.
EXHAUSTIVE = 32


def line(found: Sequence[Variant], through: Variant, i: int) -> list[Variant]:
    """The settings of ``found`` a coordinate descent tries for the ``i``-th
    tunable from ``through``: at each of its values, the setting that
    differs from ``through`` in the fewest other tunables, the first in
    ``found`` on a tie. Where tunables are coupled, a value is reached by
    moving the others with it.

    Returns:
        One setting per value, in ``found``'s order of the values.
    """
    at: dict[Hashable, list[Variant]] = {}
    for v in found:
        at.setdefault(v.tunables[i][1], []).append(v)
    return [
        min(vs, key=lambda v: sum(a != b for a, b in zip(v.tunables, through.tunables)))
        for vs in at.values()
    ]


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
    descent, each tunable's ``line`` through the fastest accurate setting so
    far, from the default until a pass over the tunables moves it no further.
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
            moves = line(found, best, i)
            batch = [default] + [v for v in moves if v is not default]
            ran |= measure_steps(
                table,
                batch,
                timing,
                repeats,
                values,
                inputs,
                cache,
                remeasure,
                [twin_of[v.key] for v in batch] if twins else (),
                fit_cache,
                log,
                ran,
            )
            built = [v for v in moves if v.key in table.steps]
            found = [v for v in found if v not in moves or v in built]
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
    log: Callable[[str], None] = print,
    values: Mapping[Operator, Mapping[str, int]] | None = None,
) -> Calibration:
    """Split a configure's cost over measured designs ``a`` and ``b`` into
    ``table``: on an xclbin chain, the mean of their loads and the dispatch,
    which the runs of one design alone give with the grouped run.

    Args:
        log: Where waiting for the NPU is reported (``time_interleaved``).
        values: Per operator, each per-call value by name, as its steps
            were measured at (``Standalone``).
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
            values=values,
        )
        for name, runlist in runlists.items()
    ]
    timed = time_interleaved([r.callable for r in runs], timing, log=log)
    # Each run's median, then its rounds, which were interleaved: every figure
    # is derived from the medians and, for its noise, round by round.
    times = np.array([(t.us, *t.round_us) for t in timed])
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
    figures = {
        name: np.broadcast_to(us, times.shape[1])
        for name, us in dict(
            dispatch=dispatch, reset=reset, base=base, switch=switch
        ).items()
    }
    noises = {name: standard_error(us[1:]) for name, us in figures.items()}
    negative = {
        name: round(float(us[0]), 1)
        for name, us in figures.items()
        if us[0] < -CONFIDENCE * (noises[name] or 0.0)
    }
    if negative:
        raise RuntimeError(
            f"calibration {ka}/{kb}: negative {negative} us; measure it with the "
            f"NPU otherwise idle, in the session that measured both steps"
        )
    # A figure within its noise of zero is zero: no load is priced below it.
    figures = {name: max(float(us[0]), 0.0) for name, us in figures.items()}
    cal = Calibration(
        dispatch_us=figures["dispatch"],
        reset_us=figures["reset"],
        base_us=figures["base"],
        switch_us=figures["switch"],
        pmode=pmode(),
        rounds=timing.rounds,
        calls=timing.calls,
        switch_noise_us=noises["switch"],
        base_noise_us=noises["base"],
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
    log: Callable[[str], None] = print,
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
        log: Where waiting for the NPU is reported (``time_interleaved``).

    Returns:
        The settings run on the device, each ``"reference>key"``.

    Raises:
        ValueError: A design is not in `table`, or `cache` or `table` is
            for another power mode than the NPU's.
        RuntimeError: A load is measured below zero by more than its noise.
    """
    for v in [reference, *found]:
        if v.key not in table.steps:
            raise ValueError(f"{v.key} is not in the table")
    mode = pmode()
    if cache is not None and cache.mode != mode:
        raise ValueError(f"the cost cache is for power mode {cache.mode}, not {mode}")
    table.measures_at(mode)
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
        times = time_interleaved([r.callable for r in runs], timing, log=log)
        for i, (v, entry) in enumerate(batch):
            alt, grp = times[2 * i], times[2 * i + 1]
            rounds = min(alt.rounds, grp.rounds)
            pair_us = (alt.us - grp.us) / (pairs - 1)
            load = pair_us - table.load(reference.key) - 2 * table.base_us
            pair_noise = standard_error(
                [
                    (a - g) / (pairs - 1)
                    for a, g in zip(alt.round_us[:rounds], grp.round_us[:rounds])
                ]
            )
            noise = math.hypot(
                pair_noise or 0.0,
                table.load_noise(reference.key) or 0.0,
                2 * (table.base_noise_us or 0.0),
            )
            if load < -CONFIDENCE * noise:
                raise RuntimeError(
                    f"load of {v.key} beside {reference.key}: negative "
                    f"{load:.1f} us; measure it with the NPU otherwise idle, in "
                    f"the session that measured the calibrations"
                )
            paired[v.key] = Pairing(
                pair_us=pair_us,
                pmode=mode,
                rounds=rounds,
                calls=timing.calls,
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
class Point:
    """A share of a version's calls, run at one set of its per-call values.

    Attributes:
        weight: The share; a call's points' weights sum to 1.
        values: The graph's per-call values there, by name.
    """

    weight: float
    values: Mapping[str, int]


@dataclasses.dataclass(frozen=True)
class Call:
    """One call of a traced graph version, as its designs are measured at:
    the graph's per-call values, and what any buffer whose contents a step's
    time follows holds, by graph buffer name. A graph ``folded`` from
    another names it in ``folded_from``: a design of its own is then priced
    beside the one whose step it took. ``points`` are the values the
    version's calls run at, where they differ from call to call: a design
    whose work they change is priced over them (``op_points``).
    """

    traced: TracedGraph
    values: Mapping[str, int] = dataclasses.field(default_factory=dict)
    contents: Mapping[str, np.ndarray] = dataclasses.field(default_factory=dict)
    folded_from: TracedGraph | None = None
    points: Sequence[Point] = ()

    @classmethod
    def admitted(
        cls,
        traced: TracedGraph,
        dev,
        values: Mapping[str, int] | None = None,
        contents: Mapping[str, np.ndarray] | None = None,
        points: Sequence[Point] = (),
    ) -> list[Call]:
        """The calls a version's tuning is priced by: ``traced`` with
        ``values``, ``contents`` and ``points``, then ``traced`` folded each
        way it folds on ``dev`` (``foldings``) and with each of those folds
        alone.
        """
        values, contents = values or {}, contents or {}
        made = Made(dev)
        ways, _ = foldings(traced, dev, made=made)
        for fold in dict.fromkeys(f for applied in ways for f in applied):
            trial, applied = folded(traced, dev, (fold,), made=made)
            ways.setdefault(frozenset(applied), (trial, applied))
        return [cls(traced, values, contents, None, points)] + [
            cls(trial, values, contents, traced, points)
            for trial, applied in ways.values()
            if applied
        ]

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

    def op_points(self, op: Operator) -> dict[str, tuple[float, dict[str, int]]]:
        """Where ``op``'s work differs over this call's ``points``: each set
        of bound extents they write it, labelled (``"kv_valid=1024"``), with
        the points' summed weight and the per-call values of the first.
        Empty where every point writes it alike, as where it has no bound
        extent: no other per-call value changes what it moves or computes.
        """
        out: dict[str, tuple[float, dict[str, int]]] = {}
        for point in self.points:
            values = self.op_values(op, point.values)
            label = ",".join(f"{e}={values[e]}" for e in sorted(op.bound_extents))
            weight, first = out.get(label, (0.0, values))
            out[label] = (weight + point.weight, first)
        return out if len(out) > 1 else {}

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
    whose step it took; one whose default the placer refuses is left out,
    so its fold is never priced. ``versions`` are the graphs the calls are
    of, as traced, and ``dev`` the device. ``points`` holds the operating points
    of each design whose work its call's points change (``Call.op_points``).
    """

    first: dict[str, tuple[Operator, Call]]
    settings: dict[str, list[Variant]]
    twin_of: dict[str, str]
    refused: dict[str, str]
    versions: tuple[TracedGraph, ...]
    dev: Device
    points: dict[str, dict[str, tuple[float, dict[str, int]]]]

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
        for key, (op, _) in list(first.items()):
            found = variants(op.probed(), dev, pinned[key])
            # A fold's design has no traced build vouching for its default;
            # where the placer refuses it, the fold stays unpriced.
            if key in twin_of:
                why = fit_verdict({key: OperatorDesign(found[0].resolved)}, fit_cache)
                if why is not None:
                    refused[found[0].key] = why
                    del first[key], twin_of[key]
                    continue
            settings[key], why = fitting(found, fit_cache)
            refused.update(why)
        if not set(twin_of.values()) <= settings.keys():
            raise ValueError("a call is folded from a graph no call measures")
        versions = tuple(c.traced for c in calls if c.folded_from is None)
        points = {
            key: at for key, (op, call) in first.items() if (at := call.op_points(op))
        }
        return cls(first, settings, twin_of, refused, versions, dev, points)

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

    def unpointed(self, table: CostTable) -> list[str]:
        """The operating points ``measure_points`` would run: each of a
        design's ``points`` that a setting ``table`` holds accurate lacks,
        ``"key@label"``.
        """
        return [
            f"{v.key}@{label}"
            for key, points in self.points.items()
            for v in self.settings[key]
            if v.key in table.steps and table.steps[v.key].accurate
            for label in points
            if label not in (table.steps[v.key].points or {})
        ]

    def calibrated(
        self, table: CostTable, triangle: tuple[type[Operator], ...] | None
    ) -> list[tuple[Variant, Variant]]:
        """The designs each pair of ``triangle``'s operator classes is
        calibrated between, ``(a, b)``, ``(a, c)`` and ``(b, c)``: the first
        design of each class, at its narrowest setting ``table`` holds whose
        other tunables are the default's. None calibrates nothing.
        """
        if triangle is None:
            return []
        by_class: dict[type[Operator], Variant] = {}
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
            by_class.setdefault(type(op), narrowest)
        a, b, c = triangle
        return [(by_class[x], by_class[y]) for x, y in ((a, b), (a, c), (b, c))]

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

    def missing(
        self, table: CostTable, triangle: tuple[type[Operator], ...] | None
    ) -> list[str]:
        """What ``measure_graph`` would run for ``table`` next, in its
        return's terms: the ``unmeasured`` settings, else the ``unpointed``
        operating points (``"key@label"``), else the calibrations of
        ``triangle`` the table lacks (``"a|b"``), which are between measured
        designs, else the ``unloaded`` settings (``"reference>key"``), else
        the ``unpacked`` packs (``CostTable.pack_name``).
        """
        designs = self.unmeasured(table)
        if designs:
            return designs
        points = self.unpointed(table)
        if points:
            return points
        chosen = self.calibrated(table, triangle)
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
    triangle: tuple[type[Operator], ...] | None,
    timing: Timing = Timing(),
    repeats: int = 9,
    remeasure: bool = False,
    log: Callable[[str], None] = print,
    cache: CostCache | None = None,
) -> list[str]:
    """Measure every design of ``calls``' graphs into ``table``, saved as it
    goes: each at the settings ``variants`` gives that ``search`` runs, in
    the first call that runs it, then each accurate setting at its call's
    operating points (``measure_points``), then the configure cost between
    each pair of ``triangle``'s operator classes (``Designs.calibrated``),
    which determines each one's entry, each other setting's entry beside
    the first of those (``measure_loads``), and on a full ELF the packs the
    versions' tunings take, each as one device (``measure_packs``), until
    they take none the table lacks or ``PACK_ROUNDS`` have (logging those
    still lacking). Designs, entries,
    packs and calibrations already in the table or ``cache`` (this NPU's
    ``cost_cache()`` if not given) are kept unless ``remeasure``; those the
    graphs no longer have are dropped from the table. A design a folded
    call has of its own is measured beside the one whose step it took, at
    each setting both have that the other's ``search`` measured
    (``measure_steps``' `twins`); the call it is folded from comes first.

    Returns:
        The design keys, operating points (``"key@label"``), calibration
        pairs (``"a|b"``), entries (``"reference>key"``) and packs
        (``CostTable.pack_name``) run on the device.

    Raises:
        ValueError: ``table`` is measured at another power mode than the
            NPU's and not ``remeasure``, which drops its entries at another
            first.
    """
    dev = aie_utils.ensure_current_device()
    table.measures(dev)
    mode = pmode()
    if remeasure:
        for entries in (table.steps, table.calibrations, table.packs):
            for k in [k for k, c in entries.items() if c.pmode != mode]:
                del entries[k]
    table.measures_at(mode)
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

    for key, (op, call) in designs.first.items():
        points = designs.points.get(key, {})
        settings = [v for v in found[key] if v.key in table.steps]
        held = {v.key: table.steps[v.key].points or {} for v in settings}
        if not points:
            for v in settings:
                if held[v.key]:
                    table.record_step(
                        v.key, dataclasses.replace(table.steps[v.key], points=None)
                    )
            continue
        weights = {label: weight for label, (weight, _) in points.items()}
        if not remeasure and all(
            {label: p.weight for label, p in held[v.key].items()} == weights
            for v in settings
            if table.steps[v.key].accurate
        ):
            continue
        name = type(op).__name__
        log(
            f"{name}: {len(points)} points of {len(settings)} settings, started "
            f"{time.strftime('%H:%M:%S')}"
        )
        pointed = measure_points(
            table,
            settings,
            points,
            call.op_values(op),
            call.op_inputs(op),
            timing,
            repeats,
            cache,
            remeasure,
        )
        ran += pointed
        table.save()
        for v in settings:
            for label, p in (table.steps[v.key].points or {}).items():
                log(
                    f"    {dict(v.tunables)} at {label} ({p.weight:.3f}): t_step "
                    f"{p.t_step_us:8.2f} us  exact {p.exact}  accurate {p.accurate}"
                    + ("" if f"{v.key}@{label}" in pointed else "  (cached)")
                )

    chosen = designs.calibrated(table, triangle)
    wanted = {f"{a.key}|{b.key}" for a, b in chosen}
    for k in [k for k in table.calibrations if k not in wanted]:
        del table.calibrations[k]
    op_values = {
        v.key: call.op_values(op)
        for key, (op, call) in designs.first.items()
        for v in found[key]
    }
    for a, b in chosen:
        pair = f"{a.key}|{b.key}"
        names = f"{type(a.op).__name__}/{type(b.op).__name__}"
        if not remeasure and pair in table.calibrations:
            log(f"calibration {names}: in the table")
            continue
        entry = cache.pair_key(
            cache.key(a.resolved, op_values[a.key], dispatch=table.dispatch),
            cache.key(b.resolved, op_values[b.key], dispatch=table.dispatch),
        )
        cal = None if remeasure else cache.get(entry, Calibration)
        if cal is None:
            cal = calibrate(
                table,
                a.op,
                b.op,
                timing,
                log=log,
                values={a.op: op_values[a.key], b.op: op_values[b.key]},
            )
            cache.put(entry, cal)
            ran.append(pair)
        else:
            table.record_calibration((a.key, b.key), cal)
        table.save()
        log(
            f"calibration {names}: D0 {cal.dispatch_us:.1f}  "
            f"R {cal.reset_us:.1f}  base {cal.base_us:.1f}  "
            f"switch {cal.switch_us:.1f} us" + ("" if pair in ran else "  (cached)")
        )

    if not chosen:
        log("no calibration triangle: no design's load is measured")
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
            log=log,
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
    else:
        unpacked = designs.unpacked(table)
        if unpacked:
            log(
                f"after {PACK_ROUNDS} rounds the tuning still takes "
                f"{len(unpacked)} packs the table lacks, priced by their "
                f"members: {[table.pack_name(d) for d in unpacked]}"
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
            members, at the values and on the inputs of the call it first
            runs in where it is a setting of `designs`.
        cache: Packs it holds are taken from it rather than run, unless
            `remeasure`; those run are written to it.

    Returns:
        The packs run on the device, by ``CostTable.pack_name``.

    Raises:
        ValueError: `table` prices an xclbin chain, a key is no setting of
            `designs`, a pack has more members than the device's contexts
            measure at once or holds every reference, or `cache` or `table`
            is for another power mode than the NPU's.
        RuntimeError: A pack's entry is measured below zero by more than its
            noise.
    """
    if table.dispatch != "fused":
        raise ValueError(f"{table.path} prices an xclbin chain: it packs no designs")
    mode = pmode()
    if cache is not None and cache.mode != mode:
        raise ValueError(f"the cost cache is for power mode {cache.mode}, not {mode}")
    table.measures_at(mode)
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
        if reference.key in of:
            _, op, call = of[reference.key]
            values[reference.op] = call.op_values(op)
            inputs[reference.op] = call.op_inputs(op)
        name = table.pack_name(keys)
        entry = None
        if cache is not None:
            entry = cache.pack_key(
                cache.key(
                    reference.resolved,
                    values.get(reference.op),
                    inputs.get(reference.op),
                    table.dispatch,
                ),
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
            times = time_interleaved([r.callable for r in runs], timing, log=log)
            del runs
            alt, grp, once = times[:3]
            rounds = min(alt.rounds, grp.rounds)
            pair_us = (alt.us - grp.us) / (pairs - 1)
            entry_us = pair_us - table.load(reference.key) - table.base_us
            pair_noise = standard_error(
                [
                    (a - g) / (pairs - 1)
                    for a, g in zip(alt.round_us[:rounds], grp.round_us[:rounds])
                ]
            )
            noise = math.hypot(
                pair_noise or 0.0,
                table.load_noise(reference.key) or 0.0,
                table.base_noise_us or 0.0,
            )
            if entry_us < -CONFIDENCE * noise:
                raise RuntimeError(
                    f"pack {name} beside {reference.key}: negative entry "
                    f"{entry_us:.1f} us; measure it with the NPU otherwise idle, "
                    f"in the session that measured the calibrations"
                )
            pack = PackCost(
                beside=reference.key,
                pair_us=pair_us,
                t_step_us={
                    k: (t.us - once.us) / (repeats - 1) for k, t in zip(keys, times[3:])
                },
                pmode=mode,
                rounds=min(t.rounds for t in times),
                calls=timing.calls,
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
