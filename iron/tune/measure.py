# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Timing designs on the NPU.

A design's step is the excess of ``repeats`` runs of it over one run, per
extra step, so the dispatch cancels (``measure``). Runs are interleaved
round by round, timed only while no other process holds the NPU, and a
figure whose calls waited for a CPU (``CPU_WAIT_US``) is refused. Every
figure is kept in a ``Cache`` keyed on what it follows, so a design is
timed once per NPU and power mode.
"""

from __future__ import annotations

import dataclasses
import datetime
import hashlib
import json
import math
import os
import re
import statistics
import subprocess
import uuid
from collections.abc import Callable, Hashable, Mapping, Sequence
from pathlib import Path

import numpy as np
from aie.iron import Out
from aie.utils import bfp
from aie.utils.benchmark import Stats, run_interleaved
from aie.utils.compile import NPU_CACHE_HOME

from iron.common.declare import Operand, Operator
from iron.common.declare.value import Value
from iron.common.design import OperatorDesign
from iron.common.graph.record import Recording
from iron.common.image.callable import ImageCallable
from iron.common.image.link import FullELF, PerStep
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, SequenceStep


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


def standard_error(samples: Sequence[float]) -> float | None:
    """``Stats``' standard error of the median of ``samples``; None from
    fewer than two.
    """
    if len(samples) < 2:
        return None
    return Stats.from_samples(list(samples)).median_se_us


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


def _sample(dtype, nbytes: int, rng: np.random.Generator) -> np.ndarray:
    dtype = np.dtype(dtype)
    if dtype.kind == "f" or dtype.name == "bfloat16":
        n = nbytes // dtype.itemsize
        return rng.standard_normal(n, dtype=np.float32).astype(dtype).view(np.uint8)
    return rng.integers(0, 4, nbytes, dtype=np.uint8)


class Standalone:
    """A runlist of operators built alone into a loaded image, its inputs
    seeded random data.

    Args:
        full_elf: How the runlist is packaged: one full ELF, else an xclbin
            per design dispatched step by step.
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
        values: Mapping[Operator, Mapping[str, int]] | None = None,
        seed: int = 0,
        distinct: bool = True,
        inputs: Mapping[Operator, Mapping[str, np.ndarray]] | None = None,
        full_elf: bool = True,
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
                (out_names if buf.role is Out else in_names).append(name_)
        steps = [
            SequenceStep(op, tuple(map(BufferRef, self._names(self._slot[k], op))))
            for k, op in enumerate(self.steps)
        ]
        # Configure the array every call, as a design beside others in a
        # model's image is, so one timed alone pays that too.
        packaging = FullELF(reconfigure=True) if full_elf else PerStep()
        self.sequence = Image(
            Recording.of_steps(name, steps, in_names, out_names), packaging
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
                elif buf.fills:
                    content = self._content(buf, inputs.get(op, {}), rng)
                    self._bytes(name_)[: buf.nbytes] = content
                    if buf.drains:
                        self._before[name_] = content.copy()
        ops = {id(op): op for op in self.steps}.values()
        artifacts = self.sequence.artifacts
        # An extent read only through its derivations has no word in a full
        # ELF; an xclbin chain has no parameter table, its values dispatch-time.
        self._symbols = {
            v.symbol: np.int32(self._value(op, self._values[op], v))
            for op in ops
            for v in op.values
            if not artifacts.full_elf or v.symbol in artifacts.parameters
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
    def _value(op: Operator, values: Mapping[str, int], v: Value) -> int:
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
        buf: Operand,
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
            if buf.fills:
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
            if not buf.drains:
                continue
            under = [slice(None)] * len(buf.shape)
            for extent in op.bound_extents:
                axis = buf.extent_axis(op.value(extent))
                if axis is not None:
                    under[axis] = slice(0, self._values[op][extent])
            data = self.callable.get_storage(name).numpy().view(np.uint8)
            data = data[: buf.nbytes].reshape(*buf.shape, -1)
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
) -> str | None:
    """Why ``op``'s output ``written`` on ``inputs`` may not replace that of
    ``default``, the setting it would replace: it must be within the
    default's gate and its own. None where it may.

    Only a bit-identical setting is admitted where a gate is missing or
    exact, or ``values`` bound an extent short of its length.
    """
    gates = {
        "the default's": default.resolved().tolerance(),
        "its own": op.resolved().tolerance(),
    }
    if any(g is None or g.kind == "exact" for g in gates.values()):
        return "only a bit-identical output is admitted"
    values = values or {}
    for extent in op.bound_extents:
        if values.get(extent) != vars(op)[op.value(extent).bounds.name]:
            return "only a bit-identical output is admitted under a bound"
    want = op._call_reference(inputs, values=values)
    for which, gate in gates.items():
        for name, verdict in op.judge(inputs, written, gate, want).items():
            if not verdict:
                return f"{name} under {which} gate: {verdict.detail}"
    return None


def time_interleaved(
    runs: Sequence[ImageCallable],
    timing: Timing,
    groups: Sequence[Hashable | None] = (),
    fastest: float = math.inf,
    log: Callable[[str], None] = print,
) -> list[Stats]:
    """Each loaded image's per-round medians, microseconds (``samples_us``),
    each call's figure the time the image itself took, which its
    ``KernelResult`` carries: mlir-aie's ``run_interleaved``, whose arguments
    and errors these are.
    """
    return run_interleaved(
        list(runs),
        rounds=timing.rounds,
        calls=timing.calls,
        settle=timing.settle,
        cutoff=timing.cutoff,
        groups=list(groups) or None,
        fastest_us=fastest,
        completion_cores=True,
        idle=True,
        log=log,
    )


# The device contexts the driver holds at once; each run timed keeps one.
CONTEXTS = 16

# Past this nothing stays in a cache, and the repeats' copies would not fit.
DISTINCT_BYTES = 256 * 2**20


@dataclasses.dataclass(frozen=True)
class Measurement:
    """One design's step, as ``measure`` timed it.

    Attributes:
        t_step_us: Its time per step, the median of `round_us`.
        round_us: Its time per step as each round measured it. Two
            measurements of one `run` were timed round for round together,
            so their rounds pair.
        output: The sha256 of what one run wrote, so two settings run on
            the same inputs compare without a rerun.
        run: Which ``time_interleaved`` call timed it.
        pmode: The NPU's power mode.
        calls: The runs a round timed.
        default_round_us: The rounds of the default timed beside it in its
            `run`; empty for the default itself.
        measured: The day, as an ISO date.
    """

    t_step_us: float
    round_us: tuple[float, ...]
    output: str
    run: str
    pmode: str
    calls: int
    default_round_us: tuple[float, ...] = ()
    measured: str = dataclasses.field(
        default_factory=lambda: datetime.date.today().isoformat()
    )

    def against_default(self) -> tuple[float, float | None]:
        """``difference`` from the default timed beside it."""
        default = self.default_round_us
        return self.difference(
            dataclasses.replace(
                self, t_step_us=statistics.median(default), round_us=default
            )
        )

    def difference(self, other: Measurement) -> tuple[float, float | None]:
        """How much longer a step of this one takes than one of ``other``,
        and that difference's standard error: round by round where the two
        were timed in one run, else from each one's own.
        """
        delta = self.t_step_us - other.t_step_us
        if self.run == other.run:
            return delta, standard_error(
                [a - b for a, b in zip(self.round_us, other.round_us)]
            )
        noises = [standard_error(m.round_us) for m in (self, other)]
        if None in noises:
            return delta, None
        return delta, math.hypot(*noises)


class Cache:
    """Every design measured on one NPU platform at one power mode, one
    JSON file each under ``root/<platform>/<power mode>/``.

    An entry is keyed on what its time follows: the design's build (its
    recipe and the sources, tools and device it is compiled with, as
    mlir-aie's compile cache keys it), the per-call values it was run at,
    the contents of the inputs it was given and its packaging. Editing how a
    design is generated therefore misses rather than reusing a stale time.
    """

    def __init__(
        self,
        platform: str,
        mode: str,
        root: Path = Path(NPU_CACHE_HOME) / "iron" / "costs",
    ):
        self.mode = mode
        slug = re.sub(r"[^a-z0-9]+", "-", platform.lower()).strip("-")
        self.directory = Path(root) / slug / mode

    @classmethod
    def here(cls) -> Cache:
        """The cache of this NPU at its present power mode."""
        report = platform()
        return cls(report["Name"], report["Power Mode"])

    @staticmethod
    def key(
        op: Operator,
        values: Mapping[str, int] | None = None,
        inputs: Mapping[str, np.ndarray] | None = None,
        full_elf: bool = True,
    ) -> str:
        """The entry ``op``, resolved for the current device, is kept in as
        run at ``values`` on ``inputs`` (random where not given), packaged
        as one full ELF or not.
        """
        design = OperatorDesign(op.resolved()).compilable()
        given = sorted(
            (name, hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest())
            for name, a in (inputs or {}).items()
        )
        key = (
            design.recipe_hash,
            design.artifact_hash,
            sorted((values or {}).items()),
            given,
            full_elf,
        )
        return hashlib.sha256(repr(key).encode()).hexdigest()[:32]

    def get(self, key: str) -> Measurement | None:
        """The measurement at ``key``; None if there is none, or it was
        written with other fields than ``Measurement`` has.
        """
        path = self.directory / f"{key}.json"
        if not path.exists():
            return None
        fields = json.loads(path.read_text())
        if fields.keys() != {f.name for f in dataclasses.fields(Measurement)}:
            return None
        return Measurement(
            **{
                **fields,
                "round_us": tuple(fields["round_us"]),
                "default_round_us": tuple(fields["default_round_us"]),
            }
        )

    def put(self, key: str, m: Measurement) -> None:
        write(self.directory / f"{key}.json", json.dumps(dataclasses.asdict(m)) + "\n")


def write(path: Path, text: str) -> None:
    """Write ``text`` to ``path`` whole, as another process may read it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_suffix(f".{os.getpid()}")
    partial.write_text(text)
    partial.replace(path)


def measure(
    ops: Sequence[Operator],
    *,
    full_elf: bool,
    timing: Timing = Timing(),
    repeats: int = 9,
    values: Mapping[str, int] | None = None,
    inputs: Mapping[str, np.ndarray] | None = None,
    cache: Cache | None = None,
    remeasure: bool = False,
    log: Callable[[str], None] = print,
) -> dict[int, Measurement]:
    """Time each of ``ops``, settings of one design with the default first,
    as many at once as the device's contexts hold. Every batch times the
    default too, so each other setting pairs with it round by round.

    Args:
        values: The per-call values each is run at.
        inputs: What its input buffers hold, by name, where random bytes
            would not be representative.
        cache: Settings it holds are taken from it rather than run, unless
            `remeasure`; those run are written to it.

    Returns:
        Each one timed, by its index in ``ops``. One other than the default
        that does not build is left out, and reported to ``log``.

    Raises:
        RuntimeError: The default does not build.
    """
    mode = pmode()
    if cache is not None and cache.mode != mode:
        raise ValueError(f"the cost cache is for power mode {cache.mode}, not {mode}")
    keys = [
        None if cache is None else cache.key(op, values, inputs, full_elf) for op in ops
    ]
    out: dict[int, Measurement] = {}
    if cache is not None and not remeasure:
        for i, key in enumerate(keys):
            if (m := cache.get(key)) is not None:
                out[i] = m
    todo = [i for i in range(len(ops)) if i not in out]
    if not todo:
        return out
    if 0 not in todo:
        todo.insert(0, 0)  # the default, timed beside the others
    distinct = sum(b.nbytes for b in ops[0].resolved().buffers) <= DISTINCT_BYTES
    # Each setting is two runs, each holding a context; one pair is the default's.
    size = CONTEXTS // 2 - 1
    fastest = math.inf
    others = todo[1:]
    for begin in range(0, max(len(others), 1), size):
        batch = [todo[0]] + others[begin : begin + size]
        log(f"    timing {len(batch)} settings, {len(others) - begin} to go")
        built, short, long = [], [], []
        for i in batch:
            try:
                one = Standalone(
                    f"probe1_{i}",
                    [ops[i]],
                    values={ops[i]: values or {}},
                    inputs={ops[i]: inputs or {}},
                    full_elf=full_elf,
                    load=False,
                )
                many = Standalone(
                    f"probe{repeats}_{i}",
                    [ops[i]] * repeats,
                    values={ops[i]: values or {}},
                    distinct=distinct,
                    inputs={ops[i]: inputs or {}},
                    full_elf=full_elf,
                    load=False,
                )
            except RuntimeError as e:
                # The placer passed it, but the build did not.
                if i == 0:
                    raise
                log(f"    {ops[i]} does not build, not measured: {e}")
                continue
            # Not caught: a failed load is the device's state, not the design's.
            one.load()
            many.load()
            built.append(i)
            short.append(one)
            long.append(many)
        outputs = [run.digest() for run in short]
        # The default is timed in full; the others stop once far behind.
        groups = [None if i == 0 else i for i in built] * 2
        times = time_interleaved(
            [r.callable for r in short + long], timing, groups, fastest, log
        )
        run = uuid.uuid4().hex
        n = len(built)
        steps = [
            tuple(
                (many - one) / (repeats - 1)
                for one, many in zip(times[j].samples_us, times[n + j].samples_us)
            )
            for j in range(n)
        ]
        for j, i in enumerate(built):
            out[i] = Measurement(
                statistics.median(steps[j]),
                steps[j],
                outputs[j],
                run,
                mode,
                timing.calls,
                () if i == 0 else steps[0],
            )
            if cache is not None:
                cache.put(keys[i], out[i])
        fastest = min(fastest, *(times[n + j].median_us for j in range(n)))
        # A probe holds its context while it lives; the next batch needs them.
        del short, long
    return out
