# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The shared elementwise array: one core per (column, channel), each
streaming fixed-size lines of every declared operand through its kernel.

A ``replicate=True`` input is one line each core holds for the whole call
and every line meets (``RowwiseMul``'s row).

A concrete operator is one small subclass naming its kernel:

```python
class ReLU(UnaryElementwise):
    def kernel(self):
        return eltwise.relu_sized(self.tile_size)
```

A core calls the kernel in its contract's argument order, with the scalars
the factory binds and those ``scalars()`` supplies. A parameter either reads
is declared ``array=True`` unless a stream names it.
"""

from __future__ import annotations

import dataclasses
from collections.abc import Iterable, Mapping
from typing import ClassVar, Self

import numpy as np
from aie.iron import In, ObjectFifo, Out, Worker, ceildiv
from aie.iron.controlflow import range_
from aie.iron.device import Device
from aie.iron.kernel import ExternalFunction
from aie.iron import kernels
from aie.iron.kernels import eltwise
from aie.utils.compile.utils import resolve_target_arch
from aie.utils.verify import Tolerance, Verdict, round_to
from aie.utils.compile.jit.params import divisors, param, per_call, tunable, widths
from ml_dtypes import bfloat16

from .declare import Built, Operand, Operator, Rtp, Unresolvable
from .testing import Case, Testing

# Small enough to divide any extent a model has, at some DMA efficiency.
DEFAULT_TILE = 256

LENGTHS = (1024, 2048, 4096, 8192)

# Takes the widest grid most of a millisecond, several times the dispatch cost.
BENCH_ELEMENTS = 1 << 23
BENCH_TILE = 4096


def _rounded(t: np.ndarray, dtype, toward: float, strict: bool) -> np.ndarray:
    """The ``dtype`` value nearest ``t`` on the side of ``toward`` (an
    infinity), past ``t`` where ``strict``, as float64.
    """
    r = t.astype(dtype)
    w = r.astype(np.float64)
    short = (w < t if toward > 0 else w > t) | (strict & (w == t))
    return np.where(short, np.nextafter(r, np.asarray(toward, dtype)), r).astype(
        np.float64
    )


def _interval(
    tol: Tolerance, values: list[np.ndarray], args: list[tuple], dtype
) -> tuple[np.ndarray, np.ndarray]:
    """The outputs of ``dtype`` ``tol`` admits for any of ``values``, as
    ``compare`` decides it.

    Args:
        tol: The tolerance an output is held to.
        values: Correctly rounded outputs, as float64.
        args: Each value's reference arguments, for a bound tolerance.
        dtype: The output's element type.

    Returns:
        The least and the greatest admitted output, elementwise.
    """
    lo, hi = [], []
    ulps = tol.kind == "ulps"
    centres = [
        (round_to(v, bfloat16) if ulps else v.astype(np.float32)).astype(np.float64)
        for v in values
    ]
    scale = max(
        float(np.max(np.abs(c), where=np.isfinite(c), initial=0)) for c in centres
    )
    for v, c, a in zip(values, centres, args):
        # Each test compare passes on is an interval around the centre:
        # (radius below, radius above, whether its bound is strict).
        tests = []
        match tol.kind:
            case "bound":
                e = np.broadcast_to(np.ravel(tol.bound(*a)).astype(np.float64), c.shape)
                tests.append((e, e, False))
            case "relative":
                r = tol.rtol or 0.0
                floor = np.finfo(np.float32).tiny if tol.atol is None else tol.atol
                away = np.maximum(floor, 2 * r * np.abs(c) / (1 - r))
                near = np.maximum(floor, 2 * r * np.abs(c) / (1 + r))
                tests.append(
                    (np.where(c < 0, away, near), np.where(c < 0, near, away), True)
                )
            case "ulps":
                if tol.atol is not None:
                    tests.append((tol.atol, tol.atol, True))
            case "exact":
                c = c.astype(dtype).astype(np.float64)
        if tol.range_frac is not None and tol.kind in ("relative", "ulps"):
            tests.append((tol.range_frac * scale, tol.range_frac * scale, False))
        low, high = c, c
        for below, above, strict in tests:
            low = np.minimum(low, _rounded(c - below, dtype, np.inf, strict))
            high = np.maximum(high, _rounded(c + above, dtype, -np.inf, strict))
        if ulps:
            down = up = c.astype(dtype)
            for _ in range(tol.ulps):
                down = np.nextafter(down, np.asarray(-np.inf, dtype))
                up = np.nextafter(up, np.asarray(np.inf, dtype))
            low = np.minimum(low, down.astype(np.float64))
            high = np.maximum(high, up.astype(np.float64))
        finite = np.isfinite(v)
        lo.append(np.where(finite, low, v))
        hi.append(np.where(finite, high, v))
    return np.minimum.reduce(lo), np.maximum.reduce(hi)


class Sweep:
    """The cases of an elementwise operator. At the regular length: one core,
    and the grid of the most cores its shim budget allows (every grid between
    runs the same loop over its cores). At the other lengths, the extensive
    suite: the smallest and the largest tile.

    Args:
        channels: None leaves the count to the operator (a binary one).
        tile_cap: Else the class's ``tile_cap``.
        regular: The one length in the default suite; None for all.
        rows: A length is that many elements in rows of ``tile_size``
            (a ``Rowwise`` operator).
        bench: The length of one CI-tracked case at the widest grid; None
            adds none.
        lower: Flags its first default case ``Case.lower``.
        **extra: Given to every case.
    """

    def __init__(
        self,
        lengths: Iterable[int] = LENGTHS,
        *,
        channels: Iterable[int] | None = (1, 2),
        tile_cap: int | None = None,
        regular: int | None = 2048,
        rows: bool = False,
        bench: int | None = BENCH_ELEMENTS,
        lower: bool = False,
        **extra,
    ):
        self.lengths = tuple(lengths)
        self.bench = bench
        self.lower = lower
        self.channels = None if channels is None else tuple(channels)
        self.tile_cap = tile_cap
        self.regular = regular
        self.rows = rows
        self.extra = extra

    def _kwargs(self, length: int, cols: int, chans: int, tile: int) -> dict:
        kwargs = dict(rows=length // tile) if self.rows else dict(size=length)
        kwargs["num_aie_columns"] = cols
        if self.channels is not None:
            kwargs["num_channels"] = chans
        kwargs.update(tile_size=tile, **self.extra)
        return kwargs

    def __call__(self, cls, dev: Device) -> list[Case]:
        cap = cls.tile_cap if self.tile_cap is None else self.tile_cap
        grids = [
            (length, cols, chans, min(length // (cols * chans), cap))
            for length in self.lengths
            for chans in self.channels or (1,)
            for cols in range(1, cls.shim_columns(dev, chans, self.extra) + 1)
        ]
        grids = [g for g in grids if g[1] * g[2] * g[3] == g[0]]
        regular = [g for g in grids if g[0] == self.regular]
        others = [g for g in grids if g[0] != self.regular]
        picked = [g for g in regular if g[1:3] == (1, 1)]
        if regular:
            picked.append(max(regular, key=lambda g: (g[1] * g[2], g[2])))
        if others:
            picked += [min(others, key=lambda g: g[3]), max(others, key=lambda g: g[3])]
        out = [
            Case(self._kwargs(*g), extensive=g[0] != self.regular)
            for g in dict.fromkeys(picked)
        ]
        if self.lower:
            i = next(i for i, c in enumerate(out) if not c.extensive)
            out[i] = dataclasses.replace(out[i], lower=True)
        if self.bench is not None:
            chans = max(self.channels or (1,))
            tile = min(BENCH_TILE, cap)
            cols = next(
                c
                for c in range(cls.shim_columns(dev, chans, self.extra), 0, -1)
                if self.bench % (c * chans * tile) == 0
            )
            out.append(
                Case(
                    self._kwargs(self.bench, cols, chans, tile),
                    bench=True,
                )
            )
        return out


@dataclasses.dataclass(frozen=True)
class KernelCall:
    """One kernel call an elementwise operator's core makes over a line.

    Args:
        kernel: The kernel called.
        scalars: The scalar arguments its contract leaves unbound, in order.
        operands: Each input tile, in the kernel's order: an input of the
            operator (``self.x``), or None, the line the call before it wrote.
    """

    kernel: ExternalFunction
    scalars: tuple = ()
    operands: tuple[Operand | None, ...] = ()


class Elementwise(Operator):
    """The array for an elementwise kernel over lines of ``tile_size`` elements.

    Subclasses declare the operands with the line as their tile, most split
    over every core (``per=CORES``), and implement ``kernel``. ``tile_cap``
    is the largest line the kernel holds.
    """

    num_aie_columns: int = tunable(domain=widths)
    num_channels: int = tunable(default=1, domain=widths)
    tile_size: int = tunable(
        domain=lambda op, dev, t: divisors(
            t, of=op.outputs[0].elements, step=64, cap=op.tile_cap, span=3
        ),
    )

    count = per_call(
        derive=lambda op: ceildiv(op.valid_elements, op.cores * op.tile_size),
    )

    default_tile: ClassVar[int] = DEFAULT_TILE
    tile_cap: ClassVar[int] = 4096

    def resolve(self, dev) -> Self:
        tile_size = self.default_tile if self.tile_size is None else self.tile_size
        if tile_size > self.tile_cap:
            raise Unresolvable(
                f"tile_size={tile_size} exceeds the {self.tile_cap}-element line "
                f"one core holds ({type(self).__name__}.tile_cap)"
            )
        (out,) = self.outputs
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            self.num_channels,
            fits=lambda c: out.elements % (c * self.num_channels * tile_size) == 0,
        )
        return self.replace(num_aie_columns=cols, tile_size=tile_size)

    def compatible(self) -> None:
        (out,) = self.outputs
        share = self.cores * self.tile_size
        if out.elements % share:
            raise ValueError(
                f"{type(self).__name__}: {out.elements} elements do not divide "
                f"into whole {self.tile_size}-element lines over "
                f"{self.num_aie_columns} columns x {self.num_channels} channels "
                f"({share} per pass); give a tile_size= or num_aie_columns= "
                f"that divides it"
            )

    @property
    def cores(self) -> int:
        return self.num_aie_columns * self.num_channels

    @property
    def lines(self) -> int:
        (out,) = self.outputs
        return out.elements // self.tile_size

    @property
    def valid_elements(self) -> int:
        """The elements a call processes, the bounded extent's worth if bound."""
        (out,) = self.outputs
        return out.elements

    def chain(self) -> tuple[KernelCall, ...]:
        """The kernel calls a core makes over one line, in order, which
        ``reference`` and ``judge`` follow: ``kernel()`` over the inputs,
        unless an operator with an array of its own makes more.
        """
        config = self.layout()
        return (KernelCall(config.kernel(), config.scalars(), tuple(self.inputs)),)

    def over(self, elements: int, line: int) -> Self:
        """This operator over ``elements`` elements in lines of ``line``, on
        one core.

        Raises:
            ValueError: Its shape is not a run of lines.
        """
        raise ValueError(f"{type(self).__name__} is not a run of lines")

    def tolerance(self) -> Tolerance | None:
        kernel = self.layout().kernel()
        if kernel.contract is None:
            return None
        return kernel.contract_for(resolve_target_arch(self.dev)).tolerance

    def ops(self) -> int:
        contract = self.layout().kernel().contract
        per_call = None if contract is None else contract.ops_per_call
        return super().ops() if per_call is None else per_call * self.lines

    def reference(self, *inputs):
        """The kernel contract's reference, line by line: what the cores compute.

        Elements short of a whole line, a bounded call's valid ones, are run
        padded with zeros to whole lines, as the device runs whole tiles.
        """
        (out,) = self.outputs
        line = self.default_tile if self.tile_size is None else self.tile_size
        if out.elements % line:
            whole = -(-out.elements // line) * line
            padded = [
                (
                    x
                    if b.replicate
                    else np.concatenate(
                        [np.ravel(x), np.zeros(whole - np.size(x), np.asarray(x).dtype)]
                    )
                )
                for b, x in zip(self.inputs, inputs)
            ]
            y = np.asarray(self.over(whole, line).reference(*padded))
            return y.reshape(-1)[: out.elements].reshape(out.host_shape)
        op, lines, scalars = self._kernel_arguments(inputs)
        (out,) = op.outputs
        y = (
            op.layout()
            .kernel()
            .expected(lines, scalars=scalars, arch=resolve_target_arch(op.dev))
        )
        y = np.asarray(y).astype(out.host_dtype, copy=False)
        return y.reshape(out.host_shape, copy=False)

    def judge(
        self,
        inputs: Mapping[str, np.ndarray],
        written: Mapping[str, np.ndarray],
        tolerance: Tolerance,
        expected: Mapping[str, np.ndarray] | None = None,
    ) -> dict[str, Verdict]:
        """Its output held to its reference by its kernel's ``judge``, line
        by line, where a core makes the one kernel call; as any operator's
        where it makes more.
        """
        op = self.resolved()
        if len(op.chain()) > 1:
            return super().judge(inputs, written, tolerance, expected)
        if expected is None:
            expected = self._call_reference(inputs)
        _, lines, scalars = self._kernel_arguments([inputs[b.name] for b in op.inputs])
        (out,) = op.outputs
        verdict = (
            op.layout()
            .kernel()
            .judge(
                written[out.name],
                expected[out.name],
                calls=op.lines,
                tolerance=tolerance,
                inputs=lines,
                scalars=scalars,
                arch=resolve_target_arch(op.dev),
            )
        )
        return {out.name: verdict}

    def _kernel_arguments(self, inputs) -> tuple[Self, list[np.ndarray], tuple]:
        """The resolved operator, ``inputs`` as the lines its cores take and
        the scalars, as its kernel's contract takes them.

        Raises:
            NotImplementedError: The kernel declares no reference.
        """
        op = self.resolved()
        config = op.layout()
        kernel = config.kernel()
        arch = resolve_target_arch(op.dev)
        contract = None if kernel.contract is None else kernel.contract_for(arch)
        if contract is None or contract.reference is None:
            raise NotImplementedError(
                f"{type(self).__name__}: its kernel declares no reference; "
                f"define reference()"
            )
        _, scalars = config.arguments(kernel, op.chain()[0].scalars, len(inputs), 1)
        # A held line is one row every call broadcasts against; cut into
        # segments, each line meets its own.
        segments = config.held_segments()
        lines = [
            (
                np.tile(np.reshape(x, (segments, -1)), (op.lines // segments, 1))
                if b.replicate and segments > 1
                else x.reshape(1 if b.replicate else op.lines, -1, copy=False)
            )
            for b, x in zip(op.inputs, inputs)
        ]
        return (
            op,
            lines,
            tuple(scalars[i] for i in contract.reference_indices() if i in scalars),
        )

    def kernel(self) -> ExternalFunction:
        """The ``ExternalFunction`` each core calls over one line."""
        raise NotImplementedError(f"{type(self).__qualname__} declares no kernel()")

    def scalars(self) -> tuple:
        """The kernel's scalar arguments its contract leaves unbound, in order."""
        return ()

    def held_segments(self) -> int:
        """The lines each held input is cut into, which a core holds all of
        and meets, in turn, with that many lines of every other input.
        """
        return 1

    def arguments(
        self, kernel: ExternalFunction, given: tuple, n_in: int, n_out: int
    ) -> tuple[list[int], dict]:
        """Where each tile goes in a call, and the scalar arguments.

        Args:
            kernel: The kernel called.
            given: The scalars its contract leaves unbound, in order.
            n_in: The input tiles a call is given.
            n_out: The output tiles a call is given.

        Returns:
            The argument positions of the inputs then the outputs, in the
            order a core acquires them, and the scalar values by position.
        """
        contract = kernel.contract
        if contract is None:
            return list(range(n_in + n_out)), {}
        if contract.accumulates:
            raise ValueError(
                f"{type(self).__qualname__}: an elementwise kernel writes its output; "
                f"{kernel.name} accumulates into one"
            )
        roles = contract.roles
        scalars = dict(contract.parameter_bindings)
        free = [
            i for i, r in enumerate(roles) if r is kernels.Param and i not in scalars
        ]
        if len(free) != len(given):
            raise ValueError(
                f"{type(self).__qualname__}: {kernel.name} leaves {len(free)} scalar(s) "
                f"unbound; {len(given)} given"
            )
        scalars.update(zip(free, given))
        outs = list(contract.out_indices)
        ins = [i for i in range(len(roles)) if i not in scalars and i not in outs]
        if (len(ins), len(outs)) != (n_in, n_out):
            raise ValueError(
                f"{type(self).__qualname__}: {kernel.name} takes {len(ins)} input and "
                f"{len(outs)} output tile(s); it is given {n_in} and {n_out}"
            )
        return ins + outs, scalars

    def build(self) -> Built:
        streams = [b for b in self.buffers if b.streamed]
        ins = [b for b in streams if b.role is In]
        outs = [b for b in streams if b.drains]
        n_in = len(ins)
        cores = self.cores
        kernel = self.kernel()
        positions, scalars = self.arguments(kernel, self.scalars(), n_in, len(outs))
        order = {i: k for k, i in enumerate(positions)}
        n_args = len(positions) + len(scalars)

        def slot(k: int) -> str:
            col, chan = divmod(k, self.num_channels)
            return f"{col}" if self.num_channels == 1 else f"{col}_{chan}"

        segments = self.held_segments()

        def fifos(stream, name):
            # A held line, acquired once per call, is one fifo per lane that
            # the cores of its lane share.
            if stream.replicate:
                return [
                    ObjectFifo(stream.obj_type, depth=segments)
                    for j in range(stream.lanes)
                ]
            depth = stream.l1_depth
            return [ObjectFifo(stream.obj_type, depth=depth) for k in range(cores)]

        of_ins = [fifos(s, f"in{i}") for i, s in enumerate(ins)]
        of_outs = [
            fifos(s, f"out{i}" if len(outs) > 1 else "out") for i, s in enumerate(outs)
        ]
        rtps = [Rtp([self.count]) for _ in range(cores)]
        n_fifos = n_in + len(outs)
        held = [s.replicate for s in ins] + [False] * len(outs)

        def core_fn(*args):
            fifos = args[:n_fifos]
            kernel_fn, rtp = args[n_fifos:]
            n = rtp.read()[self.count]
            kept = {j: f.acquire(segments) for j, f in enumerate(fifos) if held[j]}
            for _ in range_(n):
                for s in range(segments):
                    elements = [
                        (
                            (kept[j] if segments == 1 else kept[j][s])
                            if held[j]
                            else f.acquire(1)
                        )
                        for j, f in enumerate(fifos)
                    ]
                    kernel_fn(
                        *(
                            elements[order[i]] if i in order else scalars[i]
                            for i in range(n_args)
                        )
                    )
                    for j, f in enumerate(fifos):
                        if not held[j]:
                            f.release(1)
            for j in kept:
                fifos[j].release(segments)

        workers = [
            Worker(
                core_fn,
                [of[k % len(of)].cons() for of in of_ins]
                + [of[k].prod() for of in of_outs]
                + [kernel, rtps[k]],
            )
            for k in range(cores)
        ]
        for stream, of in zip(ins, of_ins):
            stream.bind([f.prod() for f in of])
        for stream, of in zip(outs, of_outs):
            stream.bind([f.cons() for f in of])
        return Built(workers, rtps)


# An operand split over every core: one lane per (column, channel).
CORES = (Elementwise.num_aie_columns, Elementwise.num_channels)


class UnaryElementwise(Elementwise):
    """A flat buffer in, a flat buffer of the same size out."""

    test = Testing(Sweep())
    size: int = param()
    valid = per_call(bounds=size)

    x = In(
        size,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
    )
    y = Out(
        size,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
    )

    @property
    def valid_elements(self) -> int:
        return self.valid

    def over(self, elements: int, line: int) -> Self:
        one = {
            n: 1
            for n in ("num_aie_columns", "num_channels")
            if n in self.declaration.tunables
        }
        return self.replace(size=elements, tile_size=line, bound_values={}, **one)


class BinaryElementwise(Elementwise):
    """Two flat buffers in, one of the same size out."""

    test = Testing(Sweep(channels=None))
    size: int = param()
    valid = per_call(bounds=size)

    a = In(
        size,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
    )
    b = In(
        size,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
    )
    y = Out(
        size,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
    )

    @property
    def valid_elements(self) -> int:
        return self.valid

    over = UnaryElementwise.over


class Rowwise(Elementwise):
    """``rows`` rows of ``tile_size`` elements in, the same out, one kernel
    call per row. For a kernel that reduces over its line, so the line is a
    ``field()``: another line would compute something else.
    """

    test = Testing(Sweep(rows=True))

    rows: int = param()
    valid = per_call(bounds=rows)
    tile_size: int = param(array=True)

    tile_cap: ClassVar[int] = 8192

    x = In(
        rows,
        tile_size,
        obj_shape=(tile_size,),
        per=CORES,
    )
    y = Out(
        rows,
        tile_size,
        obj_shape=(tile_size,),
        per=CORES,
    )

    @property
    def valid_elements(self) -> int:
        return self.valid * self.tile_size

    def over(self, elements: int, line: int) -> Self:
        if line != self.tile_size:
            raise ValueError(
                f"{type(self).__name__} reduces over rows of {self.tile_size}, "
                f"not a {line}-element tile"
            )
        one = {
            n: 1
            for n in ("num_aie_columns", "num_channels")
            if n in self.declaration.tunables
        }
        return self.replace(rows=elements // line, bound_values={}, **one)


class WeightedRowwise(Rowwise):
    """A ``Rowwise`` kernel's rows, optionally times a learned ``weight`` row.

    Weighted, two cores per (column, channel) are pipelined: one calls the
    kernel, the next multiplies by the weight row, which halves the line a
    core holds.
    """

    # The longest weighted row: the weight row beside each line halves it.
    weighted_cap: ClassVar[int] = 4096

    test = Testing(
        [
            Sweep(rows=True),
            Sweep(rows=True, tile_cap=weighted_cap, lower=True, weighted=True),
        ]
    )

    weighted: bool = param(default=False)

    x = In(
        Rowwise.rows,
        Rowwise.tile_size,
        obj_shape=(Rowwise.tile_size,),
        per=CORES,
    )
    # Shared by every column of a channel: counted once per channel.
    weight = In(
        Rowwise.tile_size,
        obj_shape=(Rowwise.tile_size,),
        per=(Elementwise.num_channels,),
        replicate=True,
        when=weighted,
    )
    y = Out(
        Rowwise.rows,
        Rowwise.tile_size,
        obj_shape=(Rowwise.tile_size,),
        per=CORES,
    )

    def validate(self) -> None:
        if self.weighted and self.tile_size > self.weighted_cap:
            raise ValueError(
                f"{type(self).__name__}: tile_size ({self.tile_size}) must be at "
                f"most {self.weighted_cap} when weighted, since the multiplying "
                f"core holds the weight row beside each line"
            )

    def chain(self) -> tuple[KernelCall, ...]:
        if not self.weighted:
            return super().chain()
        config = self.layout()
        return (
            KernelCall(config.kernel(), config.scalars(), (self.x,)),
            KernelCall(eltwise.mul_sized(self.tile_size), (), (None, self.weight)),
        )

    def reference(self, x, weight=None):
        """The kernels' references in turn, the kernel's row rounded to bf16."""
        normed = super().reference(x)
        if weight is None:
            return normed
        y = eltwise.mul_sized(self.tile_size).contract.reference(normed, weight)
        return y.astype(normed.dtype)

    def tolerance(self) -> Tolerance | None:
        own = super().tolerance()
        if not self.weighted:
            return own
        tiny = float(np.finfo(np.float32).tiny)

        def bound(x, weight):
            # Each kernel's ulp, and the product's of a row one ulp off; or the
            # first kernel's atol, scaled by the weight that multiplies it.
            y = np.abs(np.asarray(self.reference(x, weight), np.float32))
            ulp = np.exp2(np.floor(np.log2(np.maximum(y, tiny))) - 7)
            w = np.abs(np.asarray(weight, np.float32)).reshape(-1)
            scaled = (own.atol or 0.0) * np.resize(w, y.size).reshape(y.shape)
            return np.maximum(2 * ulp, scaled)

        return Tolerance.bounded(
            bound,
            note="the row's kernel then mul_sized, one ulp each; atol is the "
            "first kernel's times |weight|",
        )

    def build(self) -> Built:
        if not self.weighted:
            return super().build()
        tile_ty = self.x.obj_type
        weights_ty = self.weight.obj_type
        cols, chans = self.num_aie_columns, self.num_channels
        depth = self.x.l1_depth
        kernel = self.kernel()
        positions, scalars = self.arguments(kernel, self.scalars(), 1, 1)
        n_args = len(positions) + len(scalars)
        eltwise_mul = eltwise.mul_sized(self.tile_size)
        of_ins = [
            ObjectFifo(tile_ty, depth=depth) for i in range(cols) for j in range(chans)
        ]
        of_ws = [ObjectFifo(weights_ty, depth=depth) for j in range(chans)]
        of_mid = [
            ObjectFifo(tile_ty, depth=depth) for i in range(cols) for j in range(chans)
        ]
        of_outs = [
            ObjectFifo(tile_ty, depth=depth) for i in range(cols) for j in range(chans)
        ]
        n_cores = cols * chans
        rtps = [Rtp([self.count]) for _ in range(2 * n_cores)]

        def core_kernel(of_in, of_out, kernel_fn, rtp):
            n = rtp.read()[self.count]
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                tiles = dict(zip(positions, (elem_in, elem_out)))
                kernel_fn(
                    *(tiles[i] if i in tiles else scalars[i] for i in range(n_args))
                )
                of_in.release(1)
                of_out.release(1)

        def core_mul(of_in, of_w, of_out, mul, rtp):
            n = rtp.read()[self.count]
            elem_w = of_w.acquire(1)
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                mul(elem_in, elem_w, elem_out, self.tile_size)
                of_in.release(1)
                of_out.release(1)
            of_w.release(1)

        workers = []
        for i in range(cols):
            for j in range(chans):
                k = i * chans + j
                workers.append(
                    Worker(
                        core_kernel,
                        [
                            of_ins[k].cons(),
                            of_mid[k].prod(),
                            kernel,
                            rtps[k],
                        ],
                    )
                )
        for i in range(cols):
            for j in range(chans):
                k = i * chans + j
                workers.append(
                    Worker(
                        core_mul,
                        [
                            of_mid[k].cons(),
                            of_ws[j].cons(),
                            of_outs[k].prod(),
                            eltwise_mul,
                            rtps[n_cores + k],
                        ],
                    )
                )
        self.x.bind([f.prod() for f in of_ins])
        self.y.bind([f.cons() for f in of_outs])
        self.weight.bind([f.prod() for f in of_ws])
        return Built(workers, rtps)


class RowBroadcast(Rowwise):
    """``rows`` rows of ``tile_size`` elements, each met elementwise by one
    ``row``. A row wider than ``tile_cap`` is cut into ``segments`` lines of
    ``line`` elements, each met by its own segment of ``row``, which a core
    holds whole: the same sums, in more calls.
    """

    # Rows past the cap: cut in two (Whisper's 5120-wide bias) and in six.
    test = Testing(
        [
            Sweep(rows=True),
            Case(dict(rows=64, tile_size=5120), id="wide_row", lower=True),
            Case(dict(rows=8, tile_size=12288), id="wider_row"),
        ]
    )

    segments: int = tunable(init=False)
    line: int = tunable(init=False)

    x = In(
        Rowwise.rows,
        Rowwise.tile_size,
        obj_shape=(line,),
        per=CORES,
    )
    row = In(
        Rowwise.tile_size,
        obj_shape=(line,),
        per=(Elementwise.num_channels,),
        replicate=True,
    )
    y = Out(
        Rowwise.rows,
        Rowwise.tile_size,
        obj_shape=(line,),
        per=CORES,
    )

    def resolve(self, dev) -> Self:
        W = self.tile_size
        # A core holds the row and two lines each of x and y: as much as a
        # row at the cap takes.
        segments = next(
            (
                s
                for s in range(1, W + 1)
                if W % s == 0 and W + 4 * (W // s) <= 5 * self.tile_cap
            ),
            None,
        )
        if segments is None:
            raise Unresolvable(
                f"{type(self).__name__}: a {W}-element row and its lines do not "
                f"fit a core beside {4 * self.tile_cap} elements of x and y"
            )
        (out,) = self.outputs
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            self.num_channels,
            fits=lambda c: out.elements % (c * self.num_channels * W) == 0,
        )
        return self.replace(num_aie_columns=cols, segments=segments, line=W // segments)

    @property
    def lines(self) -> int:
        (out,) = self.outputs
        return out.elements // self.line

    def held_segments(self) -> int:
        return self.segments
