# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measuring what ``narrowing`` trades, on the NPU.

A full-ELF run costs ``D0`` (dispatch), a configure per device entered
(``base`` plus each member's load), the reset configure ``R`` when the
entries are odd, and each step's ``t_step``.

- ``measure_steps``: one run against ``repeats`` runs of a design gives
  ``t_step`` and ``alone = D0 + base + load + R``. A narrower width is a
  candidate only if its output is bit-identical to the default's.
- ``calibrate``, on measured designs A, B: ``A B A B ...`` against
  ``A A ... B B ...`` gives ``(E(A) + E(B)) / 2``; the grouped run gives
  ``D0``, the ``alone`` figures ``R``, and ``[A, B]`` packed gives ``base`` as
  ``E(A) + E(B) - E(pack)``.

Figures are medians of per-round medians, interleaved; nothing else may
dispatch meanwhile.
"""

from __future__ import annotations

import dataclasses
import statistics
import subprocess
from collections.abc import Mapping, Sequence

import numpy as np

from ..declare import Direction, Operator
from ..declare.bound import BoundBuffer, BoundValue
from ..design import device_symbol
from ..image.callable import FullELFCallable, StepCallable
from ..image.sequence import OperatorSequence
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
    """``nbytes`` of normal floats or small integers, as bytes."""
    dtype = np.dtype(dtype)
    if dtype.kind == "f" or dtype.name == "bfloat16":
        n = nbytes // dtype.itemsize
        return rng.standard_normal(n, dtype=np.float32).astype(dtype).view(np.uint8)
    return rng.integers(0, 4, nbytes, dtype=np.uint8)


class Standalone:
    """A runlist of operators built alone into a loaded full ELF, its inputs
    seeded random data.

    Args:
        distinct: Every step runs on buffers of its own, as a graph's do, so
            no step finds its inputs in a SoC cache.
        values: Each per-call value by name: the tuner cannot know what a
            value means.
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
            dispatch="fused",
            share_designs=True,
            coresident=coresident,
        ).compile()
        self.callable = self.sequence.get_callable()
        rng = np.random.default_rng(seed)
        for k in self._filled:
            op = self.steps[k]
            for buf, name_ in zip(op.buffers, self._names(k, op)):
                if buf.direction.fills:
                    self._bytes(name_)[: buf.nbytes] = self._content(buf, inputs, rng)
        ops = {id(op): op for op in self.steps}.values()
        symbols = {
            device_symbol(op, v): np.int32(self._value(values, v))
            for op in ops
            for v in op.values
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


# Past this nothing stays in a cache, and the repeats' copies would not fit.
DISTINCT_BYTES = 256 * 2**20


def measure_steps(
    table: CostTable,
    found: Sequence[Variant],
    timing: Timing = Timing(),
    repeats: int = 9,
    values: Mapping[str, int] | None = None,
    inputs: Mapping[str, np.ndarray] | None = None,
) -> dict[str, StepCost]:
    """Measure every width in ``found`` (the default first) into ``table``."""
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
    """Split a configure's cost over measured designs ``a`` and ``b`` into ``table``."""
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
    )
    table.record_calibration((ka, kb), cal)
    return cal
