# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The shared elementwise array: one core per (column, channel), each
streaming fixed-size lines of every declared operand through its kernel.

A concrete operator is one small subclass naming the kernel:

```python
class ReLU(UnaryElementwise):
    def kernel(self):
        return eltwise.relu_sized(self.tile_size)
```

A core calls the kernel in its contract's argument order, with the scalars
the factory binds and those ``scalars()`` supplies. A field either reads is
``param(..., array=True)``.
"""

from __future__ import annotations

import dataclasses
import functools
import math
from contextlib import nullcontext
from typing import ClassVar, Self

import aie.dialects.arith as arith
import numpy as np
from aie.iron import Buffer, ObjectFifo, Worker, WorkerRuntimeBarrier, ceildiv
from aie.iron.controlflow import if_, range_
from aie.iron.kernel import ExternalFunction
from aie.iron.kernels import Param
from aie.utils.verify import Tolerance

from .declare import (
    Direction,
    Extent,
    In,
    Operator,
    Out,
    Unresolvable,
    Value,
    auto,
    param,
)
from .testing import Sweep, Testing

# Small enough to divide any extent a model has, at some DMA efficiency.
DEFAULT_TILE = 256

_I32 = np.ndarray[(1,), np.dtype[np.int32]]


def _rounded(t: np.ndarray, dtype, toward: float) -> np.ndarray:
    """``t`` rounded to ``dtype`` toward ``toward`` (an infinity), as float64."""
    r = t.astype(dtype)
    past = r.astype(np.float64) > t if toward < 0 else r.astype(np.float64) < t
    r = np.where(past, np.nextafter(r, np.asarray(-toward, dtype)), r)
    return r.astype(np.float64)


def _interval(
    tol: Tolerance, values: list[np.ndarray], args: list[tuple], dtype
) -> tuple[np.ndarray, np.ndarray]:
    """The outputs of ``dtype`` ``tol`` admits for any of ``values``.

    Args:
        tol: The tolerance an output is held to.
        values: Correctly rounded outputs, as float64.
        args: Each value's reference arguments, for a bound tolerance.
        dtype: The output's element type.

    Returns:
        The least and the greatest admitted output, elementwise.
    """
    lo, hi = [], []
    scale = max(
        float(np.max(np.abs(v), where=np.isfinite(v), initial=0)) for v in values
    )
    for v, a in zip(values, args):
        match tol.kind:
            case "bound":
                e = np.broadcast_to(np.ravel(tol.bound(*a)).astype(np.float64), v.shape)
            case "relative":
                r = tol.rtol or 0.0
                e = np.maximum(tol.atol or 0.0, 2 * r * np.abs(v) / (1 - r))
            case _:
                e = np.full(v.shape, tol.atol or 0.0)
        if tol.range_frac is not None:
            e = np.maximum(e, tol.range_frac * scale)
        low, high = _rounded(v - e, dtype, np.inf), _rounded(v + e, dtype, -np.inf)
        if tol.kind == "ulps":
            down = up = v.astype(dtype)
            for _ in range(tol.ulps):
                down = np.nextafter(down, np.asarray(-np.inf, dtype))
                up = np.nextafter(up, np.asarray(np.inf, dtype))
            low = np.minimum(low, down.astype(np.float64))
            high = np.maximum(high, up.astype(np.float64))
        finite = np.isfinite(v)
        lo.append(np.where(finite, low, v))
        hi.append(np.where(finite, high, v))
    return np.minimum.reduce(lo), np.maximum.reduce(hi)


class Finish:
    """The steps a producer's cores apply to each tile of its output declared
    ``Out(..., finish=True)`` before releasing it: the chain of each design
    its array serves, a design's selected by its ``finish_chain`` word.

    A step's kernel reads and writes through restrict pointers, so the
    steps alternate between the output tile and a scratch tile of the
    core's own, the producer writing where the chain's first step reads.

    Args:
        op: The producer.
        cores: The cores applying it, on the array side; none on the host.
    """

    def __init__(self, op: Operator, cores: int = 0) -> None:
        self.op = op
        self.chains = op.finishes or (op.finish,)
        # The one output, where a chain has steps (Operator.resolved checks).
        self.out = op.outputs[-1]
        self.line = math.prod(self.out.tile_shape)
        self.select = len(self.chains) > 1
        # Each distinct step once: its kernel, argument positions and scalars.
        self.steps: dict[tuple, tuple[ExternalFunction, list[int], dict]] = {}
        for link in [link for chain in self.chains for link in chain]:
            if not isinstance(link, Elementwise):
                raise TypeError(f"a finish step is Elementwise, not {link!r}")
            if cores and link.array_key() not in self.steps:
                kernel = link.kernel()
                self.steps[link.array_key()] = (kernel, *link._arguments(kernel, 1, 1))
        self.rtps = [
            Buffer(_I32, name=f"finish_{k}", use_write_rtp=True)
            for k in range(cores if self.select else 0)
        ]
        self.scratch = [
            Buffer(self.out.tile, name=f"finished_{k}")
            for k in range(cores if any(self.chains) else 0)
        ]

    @property
    def stack_bytes(self) -> int | None:
        sizes = [
            k.contract.stack_bytes
            for k, _, _ in self.steps.values()
            if k.contract is not None and k.contract.stack_bytes is not None
        ]
        return max(sizes, default=None)

    def args(self, core: int) -> list:
        """What core ``core``'s function is given for the finish, last."""
        return [
            *(k for k, _, _ in self.steps.values()),
            *self.rtps[core : core + 1],
            *self.scratch[core : core + 1],
        ]

    def bind(self) -> None:
        if self.select:
            self.op.value("finish_chain").bind(self.rtps)

    def read(self, args):
        """The chain a core applies, read between its barrier's wait and release."""
        return args[len(self.steps)][0] if self.select else None

    def target(self, args, mode, tile):
        """Where the producer writes ``tile``: where the chain's first step reads."""
        odd = [i for i, c in enumerate(self.chains) if len(c) % 2]
        if not odd:
            return tile
        if len(odd) == len(self.chains):
            return args[-1]
        chosen = functools.reduce(arith.ori, (mode == i for i in odd))
        return arith.select(chosen, args[-1].op, tile)

    def apply(self, args, mode, tile) -> None:
        """Run the selected chain over the tile the producer wrote, ending in ``tile``."""
        kernels = dict(zip(self.steps, args))
        for i, chain in enumerate(self.chains):
            if not chain:
                continue
            with if_(mode == i) if self.select else nullcontext():
                src = tile if len(chain) % 2 == 0 else args[-1]
                for j, link in enumerate(chain):
                    dst = tile if (len(chain) - j) % 2 else args[-1]
                    key = link.array_key()
                    _, positions, scalars = self.steps[key]
                    tiles = {p: t for p, t in zip(positions, (src, dst))}
                    kernels[key](
                        *(
                            tiles[p] if p in tiles else scalars[p]
                            for p in range(len(tiles) + len(scalars))
                        )
                    )
                    src = dst

    def reference(self, y: np.ndarray) -> np.ndarray:
        """``y``, the producer's output, through its own chain on the host."""
        for link in self.op.finish:
            y = np.asarray(link.over(y.size, self.line).reference(y)).reshape(y.shape)
        return y

    def tolerance(self) -> Tolerance:
        """The producer's gate carried through its chain: each step's input
        is anywhere the gate before it admits, and its output anywhere its
        own gate admits around what it makes of that.
        """
        plain = dataclasses.replace(self.op, finish=(), finishes=())
        own = plain.gate() or Tolerance.default_for(self.out.dtype)
        dtype = self.out.dtype
        steps = [link.over(self.out.elements, self.line) for link in self.op.finish]
        gates = [s.gate() or Tolerance.default_for(dtype) for s in steps]

        def bound(*inputs):
            x = np.asarray(plain.reference(*inputs))
            shape, x = x.shape, x.astype(dtype).astype(np.float64).ravel()
            lo, hi = _interval(own, [x], [inputs], dtype)
            for step, gate in zip(steps, gates):
                ends = [x, lo, hi]
                made = [
                    np.asarray(step.reference(v.astype(dtype)), np.float64).ravel()
                    for v in ends
                ]
                x = made[0]
                lo, hi = _interval(
                    gate, made, [(v.astype(dtype),) for v in ends], dtype
                )
            return np.maximum(hi - x, x - lo).reshape(shape)

        return Tolerance.bounded(
            bound,
            max_mismatch_frac=sum(t.max_mismatch_frac for t in [own, *gates]),
            note=f"{own.note}; through "
            + ", then ".join(
                f"{type(s).__name__} ({g.note})" for s, g in zip(steps, gates)
            ),
        )


class Elementwise(Operator):
    """The array for an elementwise kernel over lines of ``tile_size`` elements.

    Subclasses declare the operands with the line as their tile and
    implement ``kernel``. ``tile_cap`` is the largest line the kernel holds.
    """

    num_aie_columns: int = auto()
    num_channels: int = auto(1)
    tile_size: int = auto()

    count = Value(
        np.int32,
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
        return dataclasses.replace(self, num_aie_columns=cols, tile_size=tile_size)

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

    def kernel(self) -> ExternalFunction:
        """The ``ExternalFunction`` each core calls over one line."""
        raise NotImplementedError(f"{type(self).__name__} declares no kernel()")

    def scalars(self) -> tuple:
        """The kernel's scalar arguments its contract leaves unbound, in order."""
        return ()

    def _arguments(
        self, kernel: ExternalFunction, n_in: int, n_out: int
    ) -> tuple[list[int], dict]:
        """Where each tile goes in a call, and the scalar arguments.

        Args:
            kernel: The kernel called.
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
                f"{type(self).__name__}: an elementwise kernel writes its output; "
                f"{kernel.name} accumulates into one"
            )
        roles = contract.roles
        scalars = dict(contract.parameter_bindings)
        free = [i for i, r in enumerate(roles) if r is Param and i not in scalars]
        if len(free) != len(self.scalars()):
            raise ValueError(
                f"{type(self).__name__}: {kernel.name} leaves {len(free)} scalar(s) "
                f"unbound; scalars() gives {len(self.scalars())}"
            )
        scalars.update(zip(free, self.scalars()))
        outs = list(contract.out_indices)
        ins = [i for i in range(len(roles)) if i not in scalars and i not in outs]
        if (len(ins), len(outs)) != (n_in, n_out):
            raise ValueError(
                f"{type(self).__name__}: {kernel.name} takes {len(ins)} input and "
                f"{len(outs)} output tile(s); it is given {n_in} and {n_out}"
            )
        return ins + outs, scalars

    def over(self, elements: int, line: int) -> Self:
        """This operator over ``elements`` elements in lines of ``line``, on
        one core.

        Raises:
            ValueError: Its shape is not a run of lines.
        """
        raise ValueError(f"{type(self).__name__} is not a run of lines")

    def at_line(self, line: int, dtype, dev) -> Self:
        if type(self).array is not Elementwise.array:
            raise ValueError(f"{type(self).__name__}'s cores run an array of their own")
        streamed = [np.dtype(b.dtype) for b in self.buffers if b.streamed]
        if streamed != [np.dtype(dtype)] * 2:
            raise ValueError(
                f"{type(self).__name__} streams {[str(d) for d in streamed]}, not "
                f"one {np.dtype(dtype)} tile in and one out"
            )
        op = self.over(line, line).resolved(dev)
        kernel = op.kernel()  # its factory refuses a line it does not run at
        op._arguments(kernel, 1, 1)
        return op

    def tolerance(self) -> Tolerance | None:
        if self.finish:
            return Finish(self).tolerance()
        contract = self.kernel().contract
        return None if contract is None else contract.tolerance

    def ops(self) -> int:
        contract = self.kernel().contract
        per_call = None if contract is None else contract.ops_per_call
        return super().ops() if per_call is None else per_call * self.lines

    def reference(self, *inputs):
        """The kernel contract's reference, line by line: what the cores compute."""
        op = self.resolved()
        contract = op.kernel().contract
        if contract is None or contract.reference is None:
            raise NotImplementedError(
                f"{type(self).__name__}: its kernel declares no reference; "
                f"define reference()"
            )
        (out,) = op.outputs
        _, scalars = op._arguments(op.kernel(), len(inputs), 1)
        lines = iter(x.reshape(op.lines, -1, copy=False) for x in inputs)
        y = contract.reference(
            *(
                scalars[i] if i in scalars else next(lines)
                for i in contract.reference_indices()
            )
        )
        y = np.asarray(y).astype(out.host_dtype, copy=False)
        y = y.reshape(out.host_shape, copy=False)
        return Finish(op).reference(y) if op.finish else y

    def array(self, target) -> list:
        streams = [b for b in self.buffers if b.streamed]
        ins = [b for b in streams if b.direction is Direction.IN]
        outs = [b for b in streams if b.direction.drains]
        n_in = len(ins)
        cores = self.cores
        kernel = self.kernel()
        positions, scalars = self._arguments(kernel, n_in, len(outs))
        order = {i: k for k, i in enumerate(positions)}
        n_args = len(positions) + len(scalars)

        def slot(k: int) -> str:
            col, chan = divmod(k, self.num_channels)
            return f"{col}" if self.num_channels == 1 else f"{col}_{chan}"

        def fifos(stream, name):
            depth = target.fifo_depth(math.prod(stream.tile_shape), stream.dtype)
            return [
                ObjectFifo(stream.tile, name=f"{name}_{slot(k)}", depth=depth)
                for k in range(cores)
            ]

        of_ins = [fifos(s, f"in{i}") for i, s in enumerate(ins)]
        of_outs = [
            fifos(s, f"out{i}" if len(outs) > 1 else "out") for i, s in enumerate(outs)
        ]
        # A bounded extent makes the trip count a per-call scratchpad word.
        dynamic = self.uses_value("count") and target.image == "elf"
        counts = (
            [self.count.param] * cores
            if dynamic
            else [
                Buffer(_I32, name=f"count_{slot(k)}", use_write_rtp=True)
                for k in range(cores)
            ]
        )
        barriers = [WorkerRuntimeBarrier() for _ in range(cores)]
        finish = Finish(self, cores)
        n_fifos = n_in + len(outs)

        def core_fn(*args):
            fifos = args[:n_fifos]
            kernel_fn, count, barrier = args[n_fifos : n_fifos + 3]
            rest = args[n_fifos + 3 :]
            barrier.wait_for_value(1)
            n = count.read() if dynamic else count[0]
            mode = finish.read(rest)
            barrier.release_with_value(1)
            for _ in range_(n):
                elements = [f.acquire(1) for f in fifos]
                tile = elements[-1]
                elements[-1] = finish.target(rest, mode, tile)
                kernel_fn(
                    *(
                        elements[order[i]] if i in order else scalars[i]
                        for i in range(n_args)
                    )
                )
                finish.apply(rest, mode, tile)
                for f in fifos:
                    f.release(1)

        stacks = [
            s
            for s in (
                kernel.contract and kernel.contract.stack_bytes,
                finish.stack_bytes,
            )
            if s is not None
        ]
        workers = [
            Worker(
                core_fn,
                [of[k].cons() for of in of_ins]
                + [of[k].prod() for of in of_outs]
                + [kernel, counts[k], barriers[k], *finish.args(k)],
                stack_size=max(stacks, default=None),
            )
            for k in range(cores)
        ]
        for k in range(cores):
            for stream, of in zip(ins, of_ins):
                stream.lane(k).bind(of[k].prod())
            for stream, of in zip(outs, of_outs):
                stream.lane(k).bind(of[k].cons())
        if not dynamic:
            self.count.bind(counts)
        finish.bind()
        return workers + barriers


class UnaryElementwise(Elementwise):
    """A flat buffer in, a flat buffer of the same size out."""

    test = Testing(Sweep())
    size: int = param()
    valid = Extent(size)

    x = In(
        size,
        tile=(Elementwise.tile_size,),
        per=(Elementwise.num_aie_columns, Elementwise.num_channels),
    )
    y = Out(
        size,
        tile=(Elementwise.tile_size,),
        per=(Elementwise.num_aie_columns, Elementwise.num_channels),
        finish=True,
    )

    @property
    def valid_elements(self) -> int:
        return self.valid

    def over(self, elements: int, line: int) -> Self:
        one = {
            n: 1
            for n in ("num_aie_columns", "num_channels")
            if n in self._tunable_fields
        }
        return dataclasses.replace(
            self, size=elements, tile_size=line, bound_values={}, **one
        )


class BinaryElementwise(Elementwise):
    """Two flat buffers in, one of the same size out."""

    test = Testing(Sweep(channels=None))
    size: int = param()
    valid = Extent(size)

    a = In(
        size,
        tile=(Elementwise.tile_size,),
        per=(Elementwise.num_aie_columns, Elementwise.num_channels),
    )
    b = In(
        size,
        tile=(Elementwise.tile_size,),
        per=(Elementwise.num_aie_columns, Elementwise.num_channels),
    )
    y = Out(
        size,
        tile=(Elementwise.tile_size,),
        per=(Elementwise.num_aie_columns, Elementwise.num_channels),
        finish=True,
    )

    @property
    def valid_elements(self) -> int:
        return self.valid


class Rowwise(Elementwise):
    """``rows`` rows of ``tile_size`` elements in, the same out, one kernel
    call per row. For a kernel that reduces over its line, so the line is a
    ``param()``: another line would compute something else.
    """

    test = Testing(Sweep(rows=True))

    rows: int = param()
    valid = Extent(rows)
    tile_size: int = param()
    num_aie_columns: int = auto(1)

    tile_cap: ClassVar[int] = 8192

    x = In(
        rows,
        tile_size,
        tile=(tile_size,),
        per=(num_aie_columns, Elementwise.num_channels),
    )
    y = Out(
        rows,
        tile_size,
        tile=(tile_size,),
        per=(num_aie_columns, Elementwise.num_channels),
        finish=True,
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
            if n in self._tunable_fields
        }
        return dataclasses.replace(self, rows=elements // line, bound_values={}, **one)
