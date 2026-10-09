# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The shared elementwise array: one core per (column, channel), each
streaming fixed-size lines of every declared operand through its kernel.

A ``replicate=True`` input is one line each core holds for the whole call
and every line meets (``RowwiseMul``'s row).

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
import aie.dialects.memref as memref
import numpy as np
from aie.helpers.util import np_ndarray_type_to_memref_type
from aie.iron import Buffer, ObjectFifo, Worker, WorkerRuntimeBarrier, ceildiv
from aie.iron.controlflow import if_, range_
from aie.iron.kernel import ExternalFunction
from aie.iron.kernels import Param
from aie.utils.verify import Tolerance

from .declare import (
    Direction,
    Divisors,
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


@dataclasses.dataclass(frozen=True)
class KernelCall:
    """One kernel call an elementwise operator's core makes over a line.

    Args:
        kernel: The kernel called.
        scalars: The scalar arguments its contract leaves unbound, in order.
        operands: Each input tile, in the kernel's order: an input of the
            operator by name, or None, the line the call before it wrote.
    """

    kernel: ExternalFunction
    scalars: tuple = ()
    operands: tuple[str | None, ...] = ()


class _Chains:
    """The chains of steps a core applies to a line it holds (``Finish``,
    ``Prepare``): the chain of each design its array serves, a design's
    selected by its ``{kind}_chain`` word.

    A kernel reads and writes through restrict pointers, so the calls of a
    chain alternate between the line and a scratch line of the core's own.
    """

    kind: ClassVar[str] = ""
    scratch_name: ClassVar[str] = ""

    def __init__(self, op: Operator, chains, line: int, dtype, cores: int) -> None:
        self.op = op
        self.chains = chains
        self.line = line
        self.dtype = dtype
        self.select = len(chains) > 1
        # Each distinct kernel call once, by its step and its place in the
        # step: its kernel, argument positions and scalars.
        self.steps: dict[tuple, tuple[ExternalFunction, list[int], dict]] = {}
        # Per chain, its calls in order: the step, its place, its operands.
        self.calls: list[list[tuple]] = [[] for _ in chains]
        for chain, calls in zip(chains, self.calls):
            for link in chain:
                if not isinstance(link.op, Elementwise):
                    raise TypeError(
                        f"a {self.kind} step is Elementwise, not {link.op!r}"
                    )
                if not cores:
                    continue
                for j, call in enumerate(link.op.chain()):
                    calls.append((link, j, call.operands))
                    self.steps.setdefault(
                        (link.array_key(), j),
                        (
                            call.kernel,
                            *link.op._arguments(
                                call.kernel, call.scalars, len(call.operands), 1
                            ),
                        ),
                    )
        self.rtps = [
            Buffer(_I32, name=f"{self.kind}_{k}", use_write_rtp=True)
            for k in range(cores if self.select else 0)
        ]
        self.scratch = [
            Buffer(
                np.ndarray[(line,), np.dtype[dtype]], name=f"{self.scratch_name}_{k}"
            )
            for k in range(cores if any(chains) else 0)
        ]
        self.fifos: list[list[ObjectFifo]] = []

    @property
    def arity(self) -> int:
        """How many arguments ``args`` gives a core."""
        return len(self.steps) + self.select + len(self.fifos) + bool(self.scratch)

    def args(self, core: int) -> list:
        """What core ``core``'s function is given for the chains, together."""
        return [
            *(k for k, _, _ in self.steps.values()),
            *self.rtps[core : core + 1],
            *(of[core].cons() for of in self.fifos),
            *self.scratch[core : core + 1],
        ]

    def bind(self) -> None:
        if self.select:
            self.op.value(f"{self.kind}_chain").bind(self.rtps)

    def read(self, args):
        """The chain a core applies, read between its barrier's wait and release."""
        return args[len(self.steps)][0] if self.select else None

    def _odd(self, args, mode, tile):
        """``args``' scratch line where the selected chain makes an odd
        number of calls, else ``tile``.
        """
        odd = [i for i, c in enumerate(self.calls) if len(c) % 2]
        if not odd:
            return tile
        if len(odd) == len(self.calls):
            return args[-1]
        chosen = functools.reduce(arith.ori, (mode == i for i in odd))
        held = tile.op if isinstance(tile, Buffer) else tile
        return arith.select(chosen, args[-1].op, held)

    def _ends(self, calls: int, tile, scratch) -> tuple:
        """Where a chain of ``calls`` calls over ``tile`` starts, and the
        line it alternates with.
        """
        raise NotImplementedError

    def _ride(self, feed, n: int) -> list:
        """The next ``n`` tiles of ``feed``, a consumer end, acquired and
        each seen as a line: the steps' inputs riding another stream.
        """
        held = feed.acquire(n)
        held = [held[i] for i in range(n)] if n > 1 else [held]
        line = np_ndarray_type_to_memref_type(
            np.ndarray[(self.line,), np.dtype[self.dtype]]
        )
        return [
            memref.reinterpret_cast(line, h, [], [], [], [0], [self.line], [1])
            for h in held
        ]

    def _run(self, args, mode, tile, extras) -> None:
        """Run the selected chain over ``tile`` (``_ends``), ``extras`` its
        steps' other input tiles, in order.
        """
        kernels = dict(zip(self.steps, args))
        for i, calls in enumerate(self.calls):
            if not calls:
                continue
            with if_(mode == i) if self.select else nullcontext():
                start, other = self._ends(len(calls), tile, args[-1])
                given = iter(extras)
                src, values = start, {}
                for n, (link, j, operands) in enumerate(calls):
                    names = [b.name for b in link.op.inputs]
                    if j == 0:
                        values = {
                            name: src if k == link.at else next(given)
                            for k, name in enumerate(names)
                        }
                    dst = other if n % 2 == 0 else start
                    _, positions, scalars = self.steps[(link.array_key(), j)]
                    ins = [src if o is None else values[o] for o in operands]
                    tiles = dict(zip(positions, [*ins, dst]))
                    kernels[(link.array_key(), j)](
                        *(
                            tiles[p] if p in tiles else scalars[p]
                            for p in range(len(tiles) + len(scalars))
                        )
                    )
                    values.pop(names[link.at], None)
                    src = dst

    @staticmethod
    def _through(links, steps, gates, x, lo, hi, extras, dtype) -> tuple:
        """``x`` and the interval ``[lo, hi]`` around it, flat float64,
        through each of ``steps``: its input anywhere in the interval, its
        output anywhere its gate admits around what it makes of that.
        """
        given = iter(extras)
        for link, step, gate in zip(links, steps, gates):
            others = [
                np.asarray(next(given)).reshape(-1)
                for _ in range(len(link.op.inputs) - 1)
            ]
            args = [link.operands(v.astype(dtype), others) for v in (x, lo, hi)]
            made = [np.asarray(step.reference(*a), np.float64).ravel() for a in args]
            x = made[0]
            lo, hi = _interval(gate, made, [tuple(a) for a in args], dtype)
        return x, lo, hi

    @staticmethod
    def _steps(links, x: np.ndarray, extras, line: int) -> np.ndarray:
        """``x`` through ``links`` on the host, each step given its share of ``extras``."""
        given = iter(extras)
        for link in links:
            others = [
                np.asarray(next(given)).reshape(-1)
                for _ in range(len(link.op.inputs) - 1)
            ]
            step = link.op.over(x.size, line)
            x = np.asarray(
                step.reference(*link.operands(x.reshape(-1), others))
            ).reshape(x.shape)
        return x


class Finish(_Chains):
    """The steps a producer's cores apply to each tile of its output declared
    ``Out(..., finish=True)`` before releasing it, the producer writing
    where the selected chain's first call reads.

    Args:
        op: The producer.
        cores: The cores applying it, on the array side; none on the host.
    """

    kind = "finish"
    scratch_name = "finished"

    def __init__(self, op: Operator, cores: int = 0) -> None:
        # The one output, where a chain has steps (Operator.resolved checks).
        self.out = op.outputs[-1]
        super().__init__(
            op, op.finishes or (op.finish,), self.out.finish_line, self.out.dtype, cores
        )
        # Each step's other inputs, streamed per core as the output is, or
        # riding the producer's fed input.
        self.streamed = [e for e in op.finish_inputs if e.streamed]
        self.riding = len(op.finish_inputs) - len(self.streamed)
        self.fifos = [
            [
                ObjectFifo(e.tile, name=f"{e.name}_{k}", depth=e.depth)
                for k in range(cores)
            ]
            for e in self.streamed
        ]

    def bind(self) -> None:
        super().bind()
        for e, of in zip(self.streamed, self.fifos):
            for k, fifo in enumerate(of):
                e.lane(k).bind(fifo.prod())

    def target(self, args, mode, tile):
        """Where the producer writes ``tile``: where the chain's first call reads."""
        return self._odd(args, mode, tile)

    def apply(self, args, mode, tile, feed=None) -> None:
        """Run the selected chain over the tile the producer wrote, ending in ``tile``.

        Args:
            feed: The consumer end of the producer's fed input, whose next
                tiles hold the riding inputs' share of ``tile``, in order.
        """
        at = len(self.steps) + self.select
        # Only a lone chain has extras (Operator._finish_at).
        fifos = args[at : at + len(self.fifos)]
        if not self.riding:
            self._run(args, mode, tile, [f.acquire(1) for f in fifos])
            for f in fifos:
                f.release(1)
            return
        self._run(args, mode, tile, self._ride(feed, self.riding))
        feed.release(self.riding)

    def _ends(self, calls: int, tile, scratch) -> tuple:
        # The last call writes the tile.
        return (tile, scratch) if calls % 2 == 0 else (scratch, tile)

    def reference(self, y: np.ndarray, *extras: np.ndarray) -> np.ndarray:
        """``y``, the producer's output, through its own chain on the host,
        each step given its ``extras`` (the producer's ``finish_inputs``).
        """
        return self._steps(self.op.finish, y, extras, self.line)

    def tolerance(self) -> Tolerance:
        """The producer's gate carried through its chain: each step's input
        is anywhere the gate before it admits, and its output anywhere its
        own gate admits around what it makes of that.
        """
        plain = dataclasses.replace(self.op, finish=(), finishes=())
        n = len(plain.inputs)
        own = plain.gate() or Tolerance.default_for(self.out.dtype)
        dtype = self.out.dtype
        steps = [link.op.over(self.out.elements, self.line) for link in self.op.finish]
        gates = [s.gate() or Tolerance.default_for(dtype) for s in steps]

        def bound(*inputs):
            x = np.asarray(plain.reference(*inputs[:n]))
            shape, x = x.shape, x.astype(dtype).astype(np.float64).ravel()
            lo, hi = _interval(own, [x], [inputs[:n]], dtype)
            x, lo, hi = self._through(
                self.op.finish, steps, gates, x, lo, hi, inputs[n:], dtype
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


class Prepare(_Chains):
    """The steps a consumer's cores apply to each tile of its input declared
    ``In(..., prepare=True)`` after acquiring it, the consumer reading where
    the selected chain's last call wrote. A step's other inputs are tiles
    of the same stream, filled after the prepared one, so a core acquires
    ``tiles`` of it at once.

    Args:
        op: The consumer.
        cores: The cores applying it, on the array side; none on the host.
    """

    kind = "prepare"
    scratch_name = "prepared"

    def __init__(self, op: Operator, cores: int = 0) -> None:
        self.into = next(b for b in op.inputs if b.member.prepare)
        super().__init__(
            op,
            op.prepares or (op.prepare,),
            (
                math.prod(self.into.tile_shape)
                if self.into.streamed
                else self.into.shape[-1]
            ),
            self.into.dtype,
            cores,
        )
        self.tiles = 1 + len(op.prepare_inputs)
        # The prepared input's fifo: its own depth, and room for the steps' inputs.
        self.depth = (
            self.into.depth + len(op.prepare_inputs) if self.into.streamed else None
        )

    def apply(self, args, mode, held, feed=None):
        """Run the selected chain over ``held`` and return the line it ended in.

        Args:
            held: The ``tiles`` a core acquired of the prepared input's
                stream, or the line it holds of an untiled one.
            feed: For an untiled prepared input, the consumer end of the
                ``feed=True`` input, whose next tiles hold the steps' inputs.
        """
        if feed is None:
            tile, *extras = held if self.tiles > 1 else (held,)
            self._run(args, mode, tile, extras)
            return self._odd(args, mode, tile)
        riding = self.tiles - 1
        self._run(args, mode, held, self._ride(feed, riding) if riding else [])
        if riding:
            feed.release(riding)
        return self._odd(args, mode, held)

    def _ends(self, calls: int, tile, scratch) -> tuple:
        return tile, scratch

    def reference(self, x: np.ndarray, *extras: np.ndarray) -> np.ndarray:
        """``x``, the consumer's prepared input, through its own chain on
        the host, each step given its ``extras`` (the consumer's
        ``prepare_inputs``).
        """
        return self._steps(self.op.prepare, x, extras, self.line)

    def tolerance(self) -> Tolerance:
        """The consumer's gate around what it makes of the prepared input,
        widened by the interval the prologue's gates admit of that input
        carried through the consumer, which is linear in it: the consumer
        of the interval's radius and the magnitudes of its other inputs, in
        float32 and unrounded. For a consumer without a finish.
        """
        plain = dataclasses.replace(self.op, prepare=(), prepares=())
        (out,) = plain.outputs
        own = plain.gate() or Tolerance.default_for(out.dtype)
        n = len(plain.inputs)
        at = [b.name for b in plain.inputs].index(self.into.name)
        dtype = self.into.dtype
        steps = [
            link.op.over(self.into.elements, self.line) for link in self.op.prepare
        ]
        gates = [s.gate() or Tolerance.default_for(dtype) for s in steps]

        def bound(*inputs):
            x = np.asarray(inputs[at])
            v = x.astype(np.float64).ravel()
            v, lo, hi = self._through(
                self.op.prepare, steps, gates, v, v, v, inputs[n:], dtype
            )
            prepared = list(inputs[:n])
            prepared[at] = v.astype(dtype).reshape(x.shape)
            y = np.asarray(plain.reference(*prepared))
            spread = [np.abs(np.asarray(i, np.float32)) for i in inputs[:n]]
            spread[at] = np.maximum(hi - v, v - lo).astype(np.float32).reshape(x.shape)
            spread = np.asarray(plain.reference(*spread), np.float64)
            y64 = y.astype(np.float64).ravel()
            ylo, yhi = _interval(own, [y64], [tuple(prepared)], out.dtype)
            radius = np.maximum(yhi - y64, y64 - ylo)
            return (spread.ravel() + radius).reshape(y.shape)

        return Tolerance.bounded(
            bound,
            max_mismatch_frac=sum(t.max_mismatch_frac for t in [own, *gates]),
            note=f"{own.note}; after "
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
    tile_size: int = auto(
        domain=Divisors(
            of=lambda op: op.outputs[0].elements,
            step=64,
            cap=lambda op: op.tile_cap,
            span=3,
        )
    )

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

    def chain(self) -> tuple[KernelCall, ...]:
        """The kernel calls a core makes over one line, in order, when
        another operator's core applies this one (``Finish``, ``Prepare``):
        ``kernel()`` over the inputs, unless an operator with an array of its
        own makes more.
        """
        extra = {b.name for b in self.finish_inputs}
        names = tuple(b.name for b in self.inputs if b.name not in extra)
        return (KernelCall(self.kernel(), self.scalars(), names),)

    def _arguments(
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
                f"{type(self).__name__}: an elementwise kernel writes its output; "
                f"{kernel.name} accumulates into one"
            )
        roles = contract.roles
        scalars = dict(contract.parameter_bindings)
        free = [i for i, r in enumerate(roles) if r is Param and i not in scalars]
        if len(free) != len(given):
            raise ValueError(
                f"{type(self).__name__}: {kernel.name} leaves {len(free)} scalar(s) "
                f"unbound; {len(given)} given"
            )
        scalars.update(zip(free, given))
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

    def at_line(self, line: int, dtype, dev, ordered: bool = True, at: int = 0) -> Self:
        own = type(self).array is not Elementwise.array
        if own and type(self).chain is Elementwise.chain:
            raise ValueError(f"{type(self).__name__}'s cores run an array of their own")
        streamed = [np.dtype(b.dtype) for b in self.buffers if b.streamed]
        if len(self.outputs) != 1 or streamed != [np.dtype(dtype)] * len(streamed):
            raise ValueError(
                f"{type(self).__name__} streams {[str(d) for d in streamed]}, not "
                f"{np.dtype(dtype)} tiles in and one out"
            )
        op = self.over(line, line).resolved(dev)
        tile = op.inputs[at].name
        for j, call in enumerate(op.chain()):
            if j and tile in call.operands:
                raise ValueError(
                    f"{type(self).__name__}: a call after its first names "
                    f"{tile}, the line the first overwrites"
                )
            # A factory refuses a line it does not run at.
            op._arguments(call.kernel, call.scalars, len(call.operands), 1)
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
        n = len(inputs) - len(op.finish_inputs)
        _, scalars = op._arguments(op.kernel(), op.scalars(), n, 1)
        # A held line is one row every call broadcasts against.
        lines = iter(
            x.reshape(1 if b.replicate else op.lines, -1, copy=False)
            for b, x in zip(op.inputs, inputs[:n])
        )
        y = contract.reference(
            *(
                scalars[i] if i in scalars else next(lines)
                for i in contract.reference_indices()
            )
        )
        y = np.asarray(y).astype(out.host_dtype, copy=False)
        y = y.reshape(out.host_shape, copy=False)
        return Finish(op).reference(y, *inputs[n:]) if op.finish else y

    def array(self, target) -> list:
        finish = Finish(self, self.cores)
        streams = [
            b for b in self.buffers if b.streamed and b not in self.finish_inputs
        ]
        ins = [b for b in streams if b.direction is Direction.IN]
        outs = [b for b in streams if b.direction.drains]
        n_in = len(ins)
        cores = self.cores
        kernel = self.kernel()
        positions, scalars = self._arguments(kernel, self.scalars(), n_in, len(outs))
        order = {i: k for k, i in enumerate(positions)}
        n_args = len(positions) + len(scalars)

        def slot(k: int) -> str:
            col, chan = divmod(k, self.num_channels)
            return f"{col}" if self.num_channels == 1 else f"{col}_{chan}"

        def fifos(stream, name):
            # A held line, acquired once per call, is one fifo per lane that
            # the cores of its lane share.
            if stream.replicate:
                return [
                    ObjectFifo(stream.tile, name=f"{name}_held_{j}", depth=1)
                    for j in range(stream.count)
                ]
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
        n_fifos = n_in + len(outs)
        held = [s.replicate for s in ins] + [False] * len(outs)

        def core_fn(*args):
            fifos = args[:n_fifos]
            kernel_fn, count, barrier = args[n_fifos : n_fifos + 3]
            rest = args[n_fifos + 3 :]
            barrier.wait_for_value(1)
            n = count.read() if dynamic else count[0]
            mode = finish.read(rest)
            barrier.release_with_value(1)
            kept = {j: f.acquire(1) for j, f in enumerate(fifos) if held[j]}
            for _ in range_(n):
                elements = [
                    kept[j] if held[j] else f.acquire(1) for j, f in enumerate(fifos)
                ]
                tile = elements[-1]
                elements[-1] = finish.target(rest, mode, tile)
                kernel_fn(
                    *(
                        elements[order[i]] if i in order else scalars[i]
                        for i in range(n_args)
                    )
                )
                finish.apply(rest, mode, tile)
                for j, f in enumerate(fifos):
                    if not held[j]:
                        f.release(1)
            for j in kept:
                fifos[j].release(1)

        workers = [
            Worker(
                core_fn,
                [of[k % len(of)].cons() for of in of_ins]
                + [of[k].prod() for of in of_outs]
                + [kernel, counts[k], barriers[k], *finish.args(k)],
            )
            for k in range(cores)
        ]
        for k in range(cores):
            for stream, of in zip(ins, of_ins):
                if k < len(of):
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

    over = UnaryElementwise.over


class Rowwise(Elementwise):
    """``rows`` rows of ``tile_size`` elements in, the same out, one kernel
    call per row. For a kernel that reduces over its line, so the line is a
    ``param()``: another line would compute something else.
    """

    test = Testing(Sweep(rows=True))

    rows: int = param()
    valid = Extent(rows)
    tile_size: int = param()

    tile_cap: ClassVar[int] = 8192

    x = In(
        rows,
        tile_size,
        tile=(tile_size,),
        per=(Elementwise.num_aie_columns, Elementwise.num_channels),
    )
    y = Out(
        rows,
        tile_size,
        tile=(tile_size,),
        per=(Elementwise.num_aie_columns, Elementwise.num_channels),
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

    def at_line(self, line: int, dtype, dev, ordered: bool = True, at: int = 0) -> Self:
        if not ordered:
            raise ValueError(
                f"{type(self).__name__} reduces over rows, which a core holding "
                f"its block in an order of its own does not hold"
            )
        return super().at_line(line, dtype, dev, ordered, at)
