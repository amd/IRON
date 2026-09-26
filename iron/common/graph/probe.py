# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measuring what :mod:`.narrowing` trades, on the NPU.

Every figure is the time of one full-ELF run: ``D0`` for the dispatch, a
configure per device the runlist enters (``base`` plus each member's load),
the empty reset configure ``R`` when the entries are odd, and each step's
``t_step``. Two kinds of measurement fill the model:

- :func:`measure_steps`, per design and width: a sequence running it once
  and one running it ``repeats`` times. The difference over the extra steps
  is ``t_step``; the single run less ``t_step`` is ``alone`` = ``D0 + base
  + load + R``. Each narrower width is also run once on the inputs its
  default ran on, and is a candidate only if its output is bit-identical.
- :func:`calibrate`, once per device on a pair A, B of measured designs:
  ``A B A B ...`` against ``A A ... B B ...`` (the same steps, 2p configures
  against 2) gives the mean configure ``(E(A) + E(B)) / 2``; the grouped
  run less its steps gives ``D0 + E(A) + E(B)``, hence ``D0``; the two
  ``alone`` figures then give ``R``; and ``[A, B]`` as one pack gives the
  pack's configure, hence the part of a configure that is not a design's
  (``base``), as ``E(A) + E(B) - E(pack)``.

A round runs every configuration ``calls`` times, and the figure is the
median over ``rounds`` of each round's median, the configurations of one
measurement interleaved. Only the run is timed
(:attr:`~iron.common.image.callable.SequenceCallable.last_elapsed`), not
the host syncs around it. Hold the NPU: nothing else may dispatch meanwhile.
"""

from __future__ import annotations

import dataclasses
import statistics
import subprocess
from collections.abc import Mapping, Sequence

import numpy as np

from ..declare import BoundBuffer, BoundValue, Operator
from ..design import device_symbol
from ..image.callable import SequenceCallable
from ..image.sequence import OperatorSequence
from ..image.packaging import EACH_STEP, FUSED, Mode
from .narrowing import Calibration, CostTable, StepCost, Variant, cost_key


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
    """``nbytes`` of data in ``dtype``, as bytes: normal values for a float
    dtype, small integers otherwise."""
    dtype = np.dtype(dtype)
    if dtype.kind == "f" or dtype.name == "bfloat16":
        n = nbytes // dtype.itemsize
        return rng.standard_normal(n, dtype=np.float32).astype(dtype).view(np.uint8)
    return rng.integers(0, 4, nbytes, dtype=np.uint8)


def _values(op: Operator) -> list[BoundValue]:
    """Every per-call value ``op`` drives, its own and its overlay's."""
    return list(op.values) + list(op.ov.values)


class Standalone:
    """A runlist of operators built alone into a full ELF, loaded, with its
    inputs filled with seeded random data. With ``distinct`` every step runs
    on buffers of its own, as a graph's steps do: a step repeated on the
    buffers it just read finds them in whatever cache the SoC keeps, which no
    graph step reading another layer's weights does. Without it, each
    operator's steps share its buffers (for steps far larger than any
    cache, whose copies would not fit the host). ``values`` sets every per-call value an
    operator drives, by the value's name; the tuner cannot know what a value
    means, so a design that takes one is measured at what its caller gives.
    ``inputs`` does the same for input buffers, by buffer name: random bytes
    are no representative content for a buffer whose values steer the work,
    such as a draw row's temperature and top-k. ``mode`` is how the
    runlist is packaged (:mod:`iron.common.image.packaging`)."""

    def __init__(
        self,
        name: str,
        runlist: Sequence[Operator],
        coresident: Sequence[Sequence[Operator]] = (),
        values: Mapping[str, int] | None = None,
        seed: int = 0,
        distinct: bool = True,
        inputs: Mapping[str, np.ndarray] | None = None,
        mode: Mode = FUSED,
    ):
        self.steps = list(runlist)
        firsts = {}
        for k, op in enumerate(self.steps):
            firsts.setdefault(id(op), k)
        # The buffers step k runs on are slot k's.
        self._slot = [
            k if distinct else firsts[id(op)] for k, op in enumerate(self.steps)
        ]
        self._filled = sorted(set(self._slot))
        in_names, out_names = [], []
        for k in self._filled:
            op = self.steps[k]
            for buf, name_ in zip(op.buffers, self._names(k, op)):
                (out_names if buf.direction == "out" else in_names).append(name_)
        self.sequence = OperatorSequence(
            name,
            [(op, *self._names(self._slot[k], op)) for k, op in enumerate(self.steps)],
            in_names,
            out_names,
            dispatch=mode.dispatch,
            share_designs=True,
            coresident=coresident,
        ).compile()
        self.callable = self.sequence.get_callable()
        rng = np.random.default_rng(seed)
        for k in self._filled:
            op = self.steps[k]
            for buf, name_ in zip(op.buffers, self._names(k, op)):
                if buf.direction in ("in", "inout"):
                    self._bytes(name_)[: buf.nbytes] = self._content(buf, inputs, rng)
        ops = {id(op): op for op in self.steps}.values()
        symbols = {
            device_symbol(op, v): np.int32(self._value(values, v))
            for op in ops
            for v in _values(op)
        }
        if symbols:
            self.callable.write_values(symbols)

    @staticmethod
    def _value(values: Mapping[str, int] | None, v: BoundValue) -> int:
        if values is None or v.name not in values:
            raise ValueError(
                f"per-call value {v.name!r} needs a representative value to be measured"
            )
        return values[v.name]

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
        return self.callable.get_buffer(name).numpy_view().view(np.uint8)

    def output_bytes(self) -> bytes:
        """What the steps wrote, after one run: every out and in-out buffer."""
        self.callable()
        return b"".join(
            self._bytes(name)[: buf.nbytes].tobytes()
            for k in self._filled
            for buf, name in zip(self.steps[k].buffers, self._names(k, self.steps[k]))
            if buf.direction in ("out", "inout")
        )


def time_interleaved(runs: Sequence[SequenceCallable], timing: Timing) -> list[float]:
    """Each loaded image's median of per-round medians, microseconds, of the
    run alone, interleaved."""
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


# A step whose buffers exceed this runs its repeats on one copy of them:
# nothing of that size stays in a cache, and the copies would not fit.
DISTINCT_BYTES = 256 * 2**20


def measure_steps(
    table: CostTable,
    found: Sequence[Variant],
    timing: Timing = Timing(),
    repeats: int = 9,
    values: Mapping[str, int] | None = None,
    inputs: Mapping[str, np.ndarray] | None = None,
) -> dict[str, StepCost]:
    """Measure every width in ``found`` (a design's :func:`.variants`, the
    default first) and record each in ``table``. ``values`` and ``inputs``
    are :class:`Standalone`'s."""
    mode = pmode()
    distinct = sum(b.nbytes for b in found[0].op.buffers) <= DISTINCT_BYTES
    short = [
        Standalone(f"probe1_{v.key}", [v.op], values=values, inputs=inputs)
        for v in found
    ]
    long = [
        Standalone(
            f"probe{repeats}_{v.key}",
            [v.op] * repeats,
            values=values,
            distinct=distinct,
            inputs=inputs,
        )
        for v in found
    ]
    reference = short[0].output_bytes()
    exact = [run.output_bytes() == reference for run in short]
    times = time_interleaved([r.callable for r in short + long], timing)
    n = len(found)
    out = {}
    for i, v in enumerate(found):
        t_step = (times[n + i] - times[i]) / (repeats - 1)
        cost = StepCost(
            t_step_us=t_step,
            alone_us=times[i] - t_step,
            exact=exact[i],
            pmode=mode,
            rounds=timing.rounds,
            calls=timing.calls,
            measured=CostTable.today(),
        )
        table.record_step(v.key, cost)
        out[v.key] = cost
    return out


def calibrate(
    table: CostTable,
    a: Operator,
    b: Operator,
    timing: Timing = Timing(),
    pairs: int = 4,
    values: Mapping[str, int] | None = None,
) -> Calibration:
    """Split a configure's cost for two measured designs ``a`` and ``b``
    (see the module docstring), and record it in ``table``."""
    ka, kb = cost_key(a), cost_key(b)
    ta, tb = table.steps[ka].t_step_us, table.steps[kb].t_step_us
    tag = f"{ka}_{kb}"
    runs = [
        Standalone(f"cal_alt{pairs}_{tag}", [a, b] * pairs, values=values),
        Standalone(f"cal_grp{pairs}_{tag}", [a] * pairs + [b] * pairs, values=values),
        Standalone(f"cal_pack_{tag}", [a, b], coresident=[[a, b]], values=values),
        Standalone(f"cal_a_{tag}", [a], values=values),
        Standalone(f"cal_b_{tag}", [b], values=values),
    ]
    alt, grp, pack, alone_a, alone_b = time_interleaved(
        [r.callable for r in runs], timing
    )
    switch = (alt - grp) / (2 * pairs - 2)  # (E(a) + E(b)) / 2
    dispatch = grp - pairs * (ta + tb) - 2 * switch
    reset = ((alone_a - ta) + (alone_b - tb) - 2 * switch) / 2 - dispatch
    entry_pack = pack - ta - tb - reset - dispatch
    cal = Calibration(
        dispatch_us=dispatch,
        reset_us=reset,
        base_us=2 * switch - entry_pack,
        switch_us=switch,
        pmode=pmode(),
        rounds=timing.rounds,
        calls=timing.calls,
        measured=CostTable.today(),
        mode=FUSED.name,
    )
    table.record_calibration((ka, kb), cal)
    return cal


def calibrate_each_step(
    table: CostTable,
    a: Operator,
    b: Operator,
    timing: Timing = Timing(),
    pairs: int = 4,
    repeats: int = 9,
    values: Mapping[str, int] | None = None,
) -> Calibration:
    """The boundary costs of dispatching every step alone, for two measured
    designs ``a`` and ``b``, recorded in ``table`` as an ``each_step``
    calibration.

    ``a`` once against ``a`` ``repeats`` times gives what a step's dispatch
    adds to its full-ELF ``t_step``; ``A B A B ...`` against ``A A ... B B
    ...`` (the same steps, 2p design changes against 2) gives what a change
    of design between two dispatches adds.
    """
    ka, kb = cost_key(a), cost_key(b)
    ta = table.steps[ka].t_step_us
    tag = f"{ka}_{kb}"
    runs = [
        Standalone(f"es1_{tag}", [a], values=values, mode=EACH_STEP),
        Standalone(f"es{repeats}_{tag}", [a] * repeats, values=values, mode=EACH_STEP),
        Standalone(
            f"es_alt{pairs}_{tag}", [a, b] * pairs, values=values, mode=EACH_STEP
        ),
        Standalone(
            f"es_grp{pairs}_{tag}",
            [a] * pairs + [b] * pairs,
            values=values,
            mode=EACH_STEP,
        ),
    ]
    one, many, alt, grp = time_interleaved([r.callable for r in runs], timing)
    switch = (alt - grp) / (2 * pairs - 2)
    cal = Calibration(
        dispatch_us=(many - one) / (repeats - 1) - ta,
        reset_us=0.0,
        base_us=switch,
        switch_us=switch,
        pmode=pmode(),
        rounds=timing.rounds,
        calls=timing.calls,
        measured=CostTable.today(),
        mode=EACH_STEP.name,
    )
    table.record_calibration((ka, kb), cal)
    return cal


def measure_each_step(
    table: CostTable,
    ops: Sequence[Operator],
    reference: tuple[Operator, Operator],
    timing: Timing = Timing(),
    pairs: int = 4,
    values: Mapping[str, int] | None = None,
    inputs: Mapping[str, np.ndarray] | None = None,
) -> dict[str, float]:
    """Each design in ``ops`` (already in ``table``), entered by a dispatch of
    its own right after another design's: its ``each_step_us``.

    A step entered from another design costs ``E`` (its dispatch, its
    configuration, its time), so two designs alternating ``pairs`` times run
    ``pairs * (E(a) + E(b))``. Against a fixed reference pair ``r, s``,
    ``E(v) = (T(v, r) + T(v, s) - T(r, s)) / 2`` per round; the reference
    designs' own figures follow from the first ``v``. ``values`` and
    ``inputs`` are :class:`Standalone`'s, for ``ops``.
    """
    r, s = reference
    tag = f"{cost_key(r)}_{cost_key(s)}"
    rs = Standalone(f"es_ref{pairs}_{tag}", [r, s] * pairs, mode=EACH_STEP)
    out: dict[str, float] = {}
    for op in ops:
        key = cost_key(op)
        runs = [
            rs,
            Standalone(
                f"es_{key}_r",
                [op, r] * pairs,
                values=values,
                inputs=inputs,
                mode=EACH_STEP,
            ),
            Standalone(
                f"es_{key}_s",
                [op, s] * pairs,
                values=values,
                inputs=inputs,
                mode=EACH_STEP,
            ),
        ]
        t_rs, t_vr, t_vs = (
            t / pairs for t in time_interleaved([x.callable for x in runs], timing)
        )
        e_v = (t_vr + t_vs - t_rs) / 2
        out[key] = e_v
        for ref, other in ((r, t_vr), (s, t_vs)):
            out.setdefault(cost_key(ref), other - e_v)
    for key, e in out.items():
        table.steps[key] = dataclasses.replace(table.steps[key], each_step_us=e)
    return out
