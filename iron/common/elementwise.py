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
import math
from typing import ClassVar, Self

import numpy as np
from aie.iron import Buffer, ObjectFifo, Worker, WorkerRuntimeBarrier, ceildiv
from aie.iron.controlflow import range_
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

    def tolerance(self) -> Tolerance | None:
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
        return y.reshape(out.host_shape, copy=False)

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

        def core_fn(*args):
            fifos_in = args[:n_in]
            fifos_out = args[n_in : n_in + len(outs)]
            kernel_fn, count, barrier = args[-3:]
            barrier.wait_for_value(1)
            n = count.read() if dynamic else count[0]
            for _ in range_(n):
                elements = [f.acquire(1) for f in fifos_in + fifos_out]
                kernel_fn(
                    *(
                        elements[order[i]] if i in order else scalars[i]
                        for i in range(n_args)
                    )
                )
                for f in fifos_in + fifos_out:
                    f.release(1)

        workers = [
            Worker(
                core_fn,
                [of[k].cons() for of in of_ins]
                + [of[k].prod() for of in of_outs]
                + [kernel, counts[k], barriers[k]],
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
    )

    @property
    def valid_elements(self) -> int:
        return self.valid


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
    )

    @property
    def valid_elements(self) -> int:
        return self.valid * self.tile_size
