# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The shared elementwise template: N flat buffers in, one of the same size out.

One overlay builds the array for every elementwise kernel IRON ships. It
places one core per (column, channel), each streaming fixed-size lines in
and out; the operator declares a flat buffer per stream, and its runtime
sequence is derived -- the buffer is split evenly across the cores' fifos
and drained back the same way.

``ChanneledUnaryOverlay`` and ``BinaryElementwiseOverlay`` are the two stream
shapes, and nothing more: the design reads the streams it was declared with,
so a subclass with a third input needs no new code here.

The core's trip count is a :class:`~iron.common.declare.Resident` the
sequence writes before the first transfer, so the array does not depend on
the extent and one overlay serves every size (OPERATOR_MODEL_PLAN.md §3).
This is where the template parts company with upstream's
:func:`aie.iron.algorithms.transform_parallel`, which is otherwise the same
design: that one takes the tensor at build time and folds the trip count
into the core program, and owns the runtime sequence so it can issue the
taps. An overlay here returns workers and leaves the sequence to the
library, which is what lets several operators fuse into one image.

A concrete operator is two small subclasses, one per layer, and names the
kernel each core calls::

    @operator
    class ReLUOverlay(ChanneledUnaryOverlay):
        def kernel(self, target):
            return kernels.relu_sized(self.line_size)

    @operator
    class ReLU(ChanneledUnaryOperator[ReLUOverlay]):
        def reference(self, x): ...

:mod:`aie.iron.kernels` is where a kernel comes from: its factories return
the ``ExternalFunction`` for a symbol, its source and its argument types,
and handle aie2's LUT tables. An overlay whose kernel takes more than the
line length (leaky_relu's alpha) or takes its arguments in another order
(axpy's scalar) overrides :meth:`ElementwiseOverlay.kernel_call`.
"""

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING, ClassVar

import numpy as np

from aie.iron import ObjectFifo, Worker
from aie.iron.kernel import ExternalFunction
from aie.iron.controlflow import range_
from aie.utils.verify import Tolerance

from .declare import (
    O,
    Incompatible,
    In,
    Operator,
    Out,
    Overlay,
    Resident,
    StreamIn,
    StreamOut,
    Untunable,
    dim,
    operator,
    tunable,
)
from .declare.member import _Stream
from .tiling import bank_elements

if TYPE_CHECKING:
    from .design.target import Target

# The line an elementwise core streams when nothing else is asked for: small
# enough to divide any extent a model has, at some cost in DMA efficiency.
# Call sites that know their extent pass tile_size for performance.
DEFAULT_TILE = 256

_I32 = np.ndarray[(1,), np.dtype[np.int32]]  # type: ignore[misc]


@operator
class ElementwiseOverlay(Overlay):
    """The array for an elementwise kernel over lines of ``line_size`` elements.

    Subclasses declare the streams (see the two below) and implement
    :meth:`kernel`. ``tile_cap`` is the largest line this kernel holds; a
    line spanning more than one local-memory bank drops the fifo depth to
    one.
    """

    # None: every column the device's shim budget allows, one channel each,
    # DEFAULT_TILE lines.
    num_aie_columns: int | None = tunable(None)
    num_channels: int = tunable(1)
    tile_size: int | None = tunable(None)
    # min(tile_size, tile_cap); filled by tuning, never set by a caller.
    line_size: int | None = tunable(None, repr=False)

    count = Resident(np.int32)  # lines each core processes; written per sequence

    # The line a core streams when nothing else is asked for, and the
    # largest it will hold: a line spanning more than one local-memory bank
    # drops the fifo depth to one.
    default_tile: ClassVar[int] = DEFAULT_TILE
    tile_cap: ClassVar[int] = 4096

    def tuning(self, dev) -> "ElementwiseOverlay":
        tile_size = self.default_tile if self.tile_size is None else self.tile_size
        cols = self.num_aie_columns
        if dev is not None:
            if cols is None:
                cols = self.shim_columns(dev, self.num_channels)
            self.check_shim_columns(dev, cols, self.num_channels)
        elif cols is None:
            raise Untunable("num_aie_columns defaults from the device; none given")
        return dataclasses.replace(
            self,
            num_aie_columns=cols,
            tile_size=tile_size,
            line_size=min(tile_size, self.tile_cap),
        )

    @property
    def cores(self) -> int:
        return self.num_aie_columns * self.num_channels

    # -- the kernel --------------------------------------------------------

    def kernel(self, target: Target) -> ExternalFunction:
        """The ``ExternalFunction`` each core calls, over one line.

        Usually a factory from :mod:`aie.iron.kernels` at ``self.line_size``;
        ``target.kernel(...)`` declares one upstream does not offer.
        """
        raise NotImplementedError(f"{type(self).__name__} declares no kernel()")

    def tolerance(self, target: Target) -> Tolerance | None:
        """The contract of the one kernel every core runs; ``None`` for a
        kernel declared without one."""
        contract = self.kernel(target).contract
        return None if contract is None else contract.tolerance

    def kernel_call(self, kernel, *elements) -> None:
        """Call the kernel on this core's acquired elements: inputs, then the
        output, then the line length."""
        kernel(*elements, self.line_size)

    # -- the array ----------------------------------------------------------

    def design(self, target) -> list:
        streams = [m for m in self._members if isinstance(m, _Stream)]
        ins = [getattr(self, m.name) for m in streams if m.direction == "in"]
        outs = [getattr(self, m.name) for m in streams if m.direction == "out"]
        n_in = len(ins)
        cores = self.cores
        kernel = self.kernel(target)

        def slot(k: int) -> str:
            col, chan = divmod(k, self.num_channels)
            return f"{col}" if self.num_channels == 1 else f"{col}_{chan}"

        def fifos(stream, name):
            # A line spanning more than one bank cannot be double-buffered in
            # what is left of local memory.
            depth = 1 if stream.elements > bank_elements(stream.dtype) else 2
            return [
                ObjectFifo(stream.tile, name=f"{name}_{slot(k)}", depth=depth)
                for k in range(cores)
            ]

        of_ins = [fifos(s, f"in{i}") for i, s in enumerate(ins)]
        of_outs = [
            fifos(s, f"out{i}" if len(outs) > 1 else "out") for i, s in enumerate(outs)
        ]
        counts = [target.rtp(_I32, name=f"count_{slot(k)}") for k in range(cores)]
        barriers = [target.barrier() for _ in range(cores)]

        def core_fn(*args):
            fifos_in = args[:n_in]
            fifos_out = args[n_in : n_in + len(outs)]
            kernel_fn, count, barrier = args[-3:]
            barrier.wait_for_value(1)
            for _ in range_(count[0]):
                elements = [f.acquire(1) for f in fifos_in + fifos_out]
                self.kernel_call(kernel_fn, *elements)
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
                stream[k].bind(of[k].prod())
            for stream, of in zip(outs, of_outs):
                stream[k].bind(of[k].cons())
        self.count.bind(counts)
        return workers


@operator
class ElementwiseOperator(Operator[O]):
    """What every elementwise operator's buffers have in common."""

    size: int = dim()

    def compatible(self) -> None:
        ov = self.ov
        unit = ov.num_aie_columns * ov.tile_size
        if self.size % unit:
            raise Incompatible(
                f"size ({self.size}) must be a multiple of "
                f"num_aie_columns * tile_size ({unit})"
            )
        per_core = self.size // ov.cores
        if per_core % ov.line_size:
            raise Incompatible(
                f"size ({self.size}) leaves each of the {ov.cores} cores "
                f"{per_core} elements, not a multiple of the "
                f"{ov.line_size}-element line"
            )

    def residents(self) -> dict[str, int]:
        ov = self.ov
        return {"count": self.size // ov.cores // ov.line_size}


# --------------------------------------------------------------------------
# The two stream shapes
# --------------------------------------------------------------------------


@operator
class ChanneledUnaryOverlay(ElementwiseOverlay):
    """One line in, one line out, per (column, channel)."""

    x = StreamIn(
        ElementwiseOverlay.line_size,
        per=(ElementwiseOverlay.num_aie_columns, ElementwiseOverlay.num_channels),
    )
    y = StreamOut(
        ElementwiseOverlay.line_size,
        per=(ElementwiseOverlay.num_aie_columns, ElementwiseOverlay.num_channels),
    )


@operator
class ChanneledUnaryOperator(ElementwiseOperator[O]):
    """A flat buffer in, a flat buffer of the same size out."""

    x = In(ElementwiseOperator.size, to=ChanneledUnaryOverlay.x)
    y = Out(ElementwiseOperator.size, from_=ChanneledUnaryOverlay.y)


@operator
class BinaryElementwiseOverlay(ElementwiseOverlay):
    """Two lines in, one line out. Each core's two input channels halve the
    columns the shim budget allows, so ``num_channels`` stays at one."""

    a = StreamIn(
        ElementwiseOverlay.line_size,
        per=(ElementwiseOverlay.num_aie_columns, ElementwiseOverlay.num_channels),
    )
    b = StreamIn(
        ElementwiseOverlay.line_size,
        per=(ElementwiseOverlay.num_aie_columns, ElementwiseOverlay.num_channels),
    )
    y = StreamOut(
        ElementwiseOverlay.line_size,
        per=(ElementwiseOverlay.num_aie_columns, ElementwiseOverlay.num_channels),
    )


@operator
class BinaryElementwiseOperator(ElementwiseOperator[O]):
    """Two flat buffers in, one of the same size out."""

    a = In(ElementwiseOperator.size, to=BinaryElementwiseOverlay.a)
    b = In(ElementwiseOperator.size, to=BinaryElementwiseOverlay.b)
    y = Out(ElementwiseOperator.size, from_=BinaryElementwiseOverlay.y)
