# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The shared elementwise design: N flat buffers in, one of the same size out.

One array serves every elementwise kernel IRON ships. It places one core per
(column, channel), each streaming fixed-size lines in and out. An operator
declares a flat buffer per stream with the line as its tile, and its
runtime sequence is derived: the buffer is split evenly across the cores'
fifos and drained back the same way.

``UnaryElementwise`` and ``BinaryElementwise`` are the two flat
operand shapes, and ``Rowwise`` a matrix whose rows are the lines, for
a kernel that reduces over its line (a norm). The array reads whatever
operands are declared, so an operator with a third input needs no new code
here.

The core's trip count is a ``Value`` the sequence
writes before the first transfer, so the array does not depend on the
extent and one array serves every size. This is
the one difference from upstream's
``aie.iron.algorithms.transform_parallel``, which is otherwise the same
design: it takes the tensor at build time, folds the trip count into the
core program, and owns the runtime sequence so it can issue the taps. An
array here returns workers and leaves the sequence to the library, which
lets several operators fuse into one image.

A concrete operator is one small subclass, naming the kernel each core
calls:

```python
class ReLU(UnaryElementwise):
    def kernel(self):
        return eltwise.relu_sized(self.tile_size)
```

Kernels come from ``aie.iron.kernels``: its factories return the
``ExternalFunction`` for a symbol, its source and its argument types, handle
aie2's LUT tables, and carry the contract the operator is tested by: the
reference and the tolerance. A core calls the kernel in its contract's
argument order: the acquired elements, the scalars the factory binds (the
line length) and the free ones ``scalars()`` supplies (leaky_relu's alpha,
axpy's factor), so the operator and the kernel agree by construction. A
field the kernel or its scalars read is declared ``param(..., array=True)``,
since the array bakes it in.
"""

from __future__ import annotations

import dataclasses
from typing import ClassVar, Self

import numpy as np
from aie.iron import Buffer, ObjectFifo, Worker, WorkerRuntimeBarrier, ceildiv
from aie.iron.controlflow import range_
from aie.iron.kernel import ExternalFunction
from aie.iron.kernels import Param
from aie.utils.verify import Tolerance

from .declare import (
    Extent,
    In,
    Incompatible,
    Operator,
    Out,
    Unresolvable,
    Value,
    auto,
    param,
)
from .testing import Sweep, Testing

# The line an elementwise core streams when nothing else is asked for: small
# enough to divide any extent a model has, at some cost in DMA efficiency.
# Call sites that know their extent pass tile_size for performance.
DEFAULT_TILE = 256

_I32 = np.ndarray[(1,), np.dtype[np.int32]]


class Elementwise(Operator):
    """The array for an elementwise kernel over lines of ``tile_size`` elements.

    Subclasses declare the operands with the line as their tile, one lane
    per (column, channel) (see the two below), and implement ``kernel``.
    ``tile_cap`` is the largest line the kernel holds, so a larger tile is
    refused rather than split; a line spanning more than one local-memory
    bank drops the fifo depth to one.
    """

    # Left None, the columns resolve to the most the device's shim budget
    # allows that give every core whole lines, and the tile to default_tile.
    num_aie_columns: int = auto()
    num_channels: int = auto(1)
    tile_size: int = auto()

    # The lines each core processes: written once per build, before the
    # first transfer, so the array does not depend on the extent; per call
    # when a graph bounds the extent (``x[:n]``), read by each core.
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
            raise Incompatible(
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
        """How many lines the operands hold; each core streams an equal share."""
        (out,) = self.outputs
        return out.elements // self.tile_size

    @property
    def valid_elements(self) -> int:
        """The elements a call processes: the whole operand, or the bounded
        extent's worth (the templates read their ``Extent``).
        """
        (out,) = self.outputs
        return out.elements

    # -- the kernel --------------------------------------------------------

    def kernel(self) -> ExternalFunction:
        """The ``ExternalFunction`` each core calls, over one line.

        Usually a factory from ``aie.iron.kernels`` at ``self.tile_size``;
        an ``ExternalFunction`` with a ``KernelContract`` declares one
        upstream does not offer.
        """
        raise NotImplementedError(f"{type(self).__name__} declares no kernel()")

    def scalars(self) -> tuple:
        """The values of the kernel's free scalar ``Param`` arguments, those its
        contract leaves unbound, in argument order.
        """
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
        """The contract of the one kernel every core runs; ``None`` for a
        kernel declared without one.
        """
        contract = self.kernel().contract
        return None if contract is None else contract.tolerance

    def ops(self) -> int:
        """The contract's count per call, one per output element unless it
        states one, over every line.
        """
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
        # Views of the operands as the kernel's (calls, n) lines, never copies;
        # the one pass over the data is the cast, the store's bf16 rounding.
        lines = iter(x.reshape(op.lines, -1, copy=False) for x in inputs)
        y = contract.reference(
            *(
                scalars[i] if i in scalars else next(lines)
                for i in contract.reference_indices()
            )
        )
        y = np.asarray(y).astype(out.host_dtype, copy=False)
        return y.reshape(out.host_shape, copy=False)

    # -- the array ----------------------------------------------------------

    def array(self, target) -> list:
        streams = list(self.streams.values())
        ins = [s for s in streams if s.direction == "in"]
        outs = [s for s in streams if s.direction == "out"]
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
            # A line spanning more than one bank cannot be double-buffered in
            # what is left of local memory.
            depth = target.fifo_depth(stream.elements, stream.dtype)
            return [
                ObjectFifo(stream.tile, name=f"{name}_{slot(k)}", depth=depth)
                for k in range(cores)
            ]

        of_ins = [fifos(s, f"in{i}") for i, s in enumerate(ins)]
        of_outs = [
            fifos(s, f"out{i}" if len(outs) > 1 else "out") for i, s in enumerate(outs)
        ]
        # The trip count: written once per build into an RTP, or, when a
        # graph bounds the extent, a scratchpad word each core reads per call.
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

        # The kernel's contract knows its stack; None is the core's default.
        stack_size = None if kernel.contract is None else kernel.contract.stack_bytes
        workers = [
            Worker(
                core_fn,
                [of[k].cons() for of in of_ins]
                + [of[k].prod() for of in of_outs]
                + [kernel, counts[k], barriers[k]],
                stack_size=stack_size,
            )
            for k in range(cores)
        ]
        for k in range(cores):
            for stream, of in zip(ins, of_ins):
                stream[k].bind(of[k].prod())
            for stream, of in zip(outs, of_outs):
                stream[k].bind(of[k].cons())
        if not dynamic:
            self.count.bind(counts)
        return workers + barriers


# --------------------------------------------------------------------------
# The operand shapes
# --------------------------------------------------------------------------


class UnaryElementwise(Elementwise):
    """A flat buffer in, a flat buffer of the same size out."""

    test = Testing(Sweep())
    size: int = param()
    valid = Extent(size)  # size, or fewer per call: x[:n] in a graph

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
    """Two flat buffers in, one of the same size out. Each core's two input
    channels halve the columns the shim budget allows, so ``num_channels``
    stays at one.
    """

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
    call per row.

    For a kernel that reduces over its line, so the line is the row: it is
    in the host shape (``rows x tile_size``) and a ``param()`` here rather
    than the tunable the base declares, since a different line would compute
    something else.
    """

    test = Testing(Sweep(rows=True))

    rows: int = param()
    valid = Extent(rows)  # rows, or fewer per call
    # Required here, though the base defaults it: every field is keyword-only.
    tile_size: int = param()
    # One core by default: a core takes whole rows, and the row count is the
    # extent. Call sites with many rows spread them over columns.
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
