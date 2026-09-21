# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The two shared operator families: channeled unary and binary elementwise.

Each is an overlay/operator pair in the declared form (see
:mod:`iron.common.declare`). The overlay builds one core per column (and
per channel, for the unary family), each streaming fixed-size lines in and
out; the operator declares a flat buffer per stream, and its runtime
sequence is derived: the buffer is split evenly across the cores' fifos and
drained back the same way.

The core's trip count is a :class:`~iron.common.declare.Resident` the
sequence writes before the first transfer, so the array does not depend on
the extent and one overlay serves every size (OPERATOR_MODEL_PLAN.md §3).
Before this the count was a compile-time constant derived from ``size``.

A concrete operator is two small subclasses, one per layer::

    @operator
    class ReLUOverlay(ChanneledUnaryOverlay):
        kernel_name: ClassVar[str] = "relu"
        kernel_fn_name: ClassVar[str] = "relu_bf16_size"

    @operator
    class ReLU(ChanneledUnaryOperator[ReLUOverlay]):
        def reference(self, x): ...

Overlays with an extra kernel argument (leaky_relu's alpha, axpy's scalar
factor) add a field and override :meth:`kernel_arg_types` and
:meth:`kernel_call`.
"""

from __future__ import annotations

import dataclasses
from typing import Any, ClassVar

import numpy as np
from ml_dtypes import bfloat16

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
from .device_utils import lut_sources
from .utils import device_columns, get_shim_dma_limit

# The line an elementwise core streams when nothing else is asked for: small
# enough to divide any extent a model has, at some cost in DMA efficiency.
# Call sites that know their extent pass tile_size for performance.
DEFAULT_TILE = 256

_I32 = np.ndarray[(1,), np.dtype[np.int32]]  # type: ignore[misc]


# --------------------------------------------------------------------------
# Channeled unary: one input, one output, one core per (column, channel)
# --------------------------------------------------------------------------


@operator
class ChanneledUnaryOverlay(Overlay):
    """The array for a unary kernel over lines of ``line_size`` elements.

    Subclasses set ``kernel_name`` (the ``.cc`` under the arch's kernel dir),
    ``kernel_fn_name`` (the symbol), ``needs_lut_ops`` for aie2 kernels that
    reach ``lut_based_ops.cpp``'s tables from C++, and ``tile_cap`` (the
    largest line one core holds; lines above 4096 elements need a fifo depth
    of one to fit local memory).
    """

    # None: every column of the device, one channel each, DEFAULT_TILE lines.
    num_aie_columns: int | None = tunable(None)
    num_channels: int = tunable(1)
    tile_size: int | None = tunable(None)
    # min(tile_size, tile_cap); filled by tuning, never set by a caller.
    line_size: int | None = tunable(None, repr=False)

    x = StreamIn(line_size, per=(num_aie_columns, num_channels))
    y = StreamOut(line_size, per=(num_aie_columns, num_channels))
    count = Resident(np.int32)  # lines each core processes; written per sequence

    kernel_name: ClassVar[str]
    kernel_fn_name: ClassVar[str]
    # The object the kernel is compiled to; None names it after the symbol.
    kernel_object: ClassVar[str | None] = None
    needs_lut_ops: ClassVar[bool] = False
    tile_cap: ClassVar[int] = 4096

    def tuning(self, dev) -> "ChanneledUnaryOverlay":
        tile_size = DEFAULT_TILE if self.tile_size is None else self.tile_size
        cols = self.num_aie_columns
        if dev is not None:
            limit = get_shim_dma_limit(dev)
            if cols is None:
                cols = min(device_columns(dev), limit // self.num_channels)
            if cols * self.num_channels > limit:
                raise Untunable(
                    f"num_aie_columns * num_channels ({cols * self.num_channels}) "
                    f"exceeds ShimDMA limit of {limit} for this device"
                )
        elif cols is None:
            raise Untunable("num_aie_columns defaults from the device; none given")
        return dataclasses.replace(
            self,
            num_aie_columns=cols,
            tile_size=tile_size,
            line_size=min(tile_size, self.tile_cap),
        )

    # -- hooks for kernels with extra arguments -----------------------------

    def kernel_arg_types(self, line_type) -> list:
        return [line_type, line_type, np.int32]

    def kernel_call(self, kernel, elem_in, elem_out) -> None:
        kernel(elem_in, elem_out, self.line_size)

    # -- the array ----------------------------------------------------------

    def design(self, target) -> list:
        from aie.iron import ObjectFifo, Worker
        from aie.iron.controlflow import range_

        line_type = self.x.tile
        cols, chans = self.num_aie_columns, self.num_channels
        # Lines above one 8 KB bank need a depth of one to fit local memory.
        depth = 1 if self.line_size > 4096 else 2

        kernel = target.kernel(
            self.kernel_fn_name,
            self.kernel_arg_types(line_type),
            source=target.kernel_source(self.kernel_name),
            bundled_sources=lut_sources(target.dev) if self.needs_lut_ops else (),
            object_file_name=self.kernel_object,
        )

        of_ins = [
            ObjectFifo(line_type, name=f"in{i}_{j}", depth=depth)
            for i in range(cols)
            for j in range(chans)
        ]
        of_outs = [
            ObjectFifo(line_type, name=f"out{i}_{j}", depth=depth)
            for i in range(cols)
            for j in range(chans)
        ]
        counts = [
            target.rtp(_I32, name=f"count{i}_{j}")
            for i in range(cols)
            for j in range(chans)
        ]
        barriers = [target.barrier() for _ in range(cols * chans)]

        def core_fn(of_in, of_out, kernel_line, count, barrier):
            barrier.wait_for_value(1)
            n = count[0]
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                self.kernel_call(kernel_line, elem_in, elem_out)
                of_in.release(1)
                of_out.release(1)

        workers = [
            Worker(
                core_fn,
                [of_ins[k].cons(), of_outs[k].prod(), kernel, counts[k], barriers[k]],
            )
            for k in range(cols * chans)
        ]
        for k in range(cols * chans):
            self.x[k].bind(of_ins[k].prod())
            self.y[k].bind(of_outs[k].cons())
        self.count.bind(counts)
        return workers


@operator
class ChanneledUnaryOperator(Operator[O]):
    """A flat buffer in, a flat buffer of the same size out, split across the cores."""

    size: int = dim()

    x = In(size, to=ChanneledUnaryOverlay.x)
    y = Out(size, from_=ChanneledUnaryOverlay.y)

    def compatible(self) -> None:
        ov = self.ov
        unit = ov.num_aie_columns * ov.tile_size
        if self.size % unit:
            raise Incompatible(
                f"size ({self.size}) must be a multiple of "
                f"num_aie_columns * tile_size ({unit})"
            )
        per_core = self.size // (ov.num_aie_columns * ov.num_channels)
        if per_core % ov.line_size:
            raise Incompatible(
                f"size ({self.size}) leaves each of the "
                f"{ov.num_aie_columns * ov.num_channels} cores {per_core} elements, "
                f"not a multiple of the {ov.line_size}-element line"
            )

    def residents(self) -> dict[str, int]:
        ov = self.ov
        return {
            "count": self.size // (ov.num_aie_columns * ov.num_channels) // ov.line_size
        }


# --------------------------------------------------------------------------
# Binary elementwise: two inputs, one output, one core per column
# --------------------------------------------------------------------------


@operator
class BinaryElementwiseOverlay(Overlay):
    """The array for a binary elementwise kernel over tiles of ``per_tile`` elements.

    Each core uses two shim DMA channels (one per input), so the ShimDMA
    limit is enforced as ``num_aie_columns * 2``.
    """

    # None: DEFAULT_TILE, and as many columns as the device's shim budget
    # allows two channels each.
    tile_size: int | None = tunable(None)
    num_aie_columns: int | None = tunable(None)
    # min(tile_size, 4096); filled by tuning, never set by a caller.
    per_tile: int | None = tunable(None, repr=False)

    a = StreamIn(per_tile, per=num_aie_columns)
    b = StreamIn(per_tile, per=num_aie_columns)
    y = StreamOut(per_tile, per=num_aie_columns)
    count = Resident(np.int32)

    kernel_name: ClassVar[str]
    kernel_fn_name: ClassVar[str]
    def tuning(self, dev) -> "BinaryElementwiseOverlay":
        tile_size = DEFAULT_TILE if self.tile_size is None else self.tile_size
        cols = self.num_aie_columns
        if dev is not None:
            limit = get_shim_dma_limit(dev)
            if cols is None:
                cols = min(device_columns(dev), limit // 2)
            if cols * 2 > limit:
                raise Untunable(
                    f"num_aie_columns ({cols}) exceeds ShimDMA limit "
                    f"of {limit // 2} columns for this device"
                )
        elif cols is None:
            raise Untunable("num_aie_columns defaults from the device; none given")
        return dataclasses.replace(
            self,
            num_aie_columns=cols,
            tile_size=tile_size,
            per_tile=min(tile_size, 4096),
        )

    def kernel_source(self, target):
        return target.kernel_source(self.kernel_name)

    def kernel_arg_types(self, tile_type) -> list:
        return [tile_type, tile_type, tile_type, np.int32]

    def kernel_call(self, kernel, elem_a, elem_b, elem_out) -> None:
        kernel(elem_a, elem_b, elem_out, self.per_tile)

    def design(self, target) -> list:
        from aie.iron import ObjectFifo, Worker
        from aie.iron.controlflow import range_

        tile_type = self.a.tile
        cols = self.num_aie_columns

        kernel = target.kernel(
            self.kernel_fn_name,
            self.kernel_arg_types(tile_type),
            source=self.kernel_source(target),
        )
        of_as = [ObjectFifo(tile_type, name=f"in1_{i}") for i in range(cols)]
        of_bs = [ObjectFifo(tile_type, name=f"in2_{i}") for i in range(cols)]
        of_ys = [ObjectFifo(tile_type, name=f"out_{i}") for i in range(cols)]
        counts = [target.rtp(_I32, name=f"count_{i}") for i in range(cols)]
        barriers = [target.barrier() for _ in range(cols)]

        def core_body(of_a, of_b, of_y, kernel_fn, count, barrier):
            barrier.wait_for_value(1)
            n = count[0]
            for _ in range_(n):
                elem_a = of_a.acquire(1)
                elem_b = of_b.acquire(1)
                elem_y = of_y.acquire(1)
                self.kernel_call(kernel_fn, elem_a, elem_b, elem_y)
                of_a.release(1)
                of_b.release(1)
                of_y.release(1)

        workers = [
            Worker(
                core_body,
                [
                    of_as[i].cons(),
                    of_bs[i].cons(),
                    of_ys[i].prod(),
                    kernel,
                    counts[i],
                    barriers[i],
                ],
            )
            for i in range(cols)
        ]
        for i in range(cols):
            self.a[i].bind(of_as[i].prod())
            self.b[i].bind(of_bs[i].prod())
            self.y[i].bind(of_ys[i].cons())
        self.count.bind(counts)
        return workers


@operator
class BinaryElementwiseOperator(Operator[O]):
    """Two flat buffers in, one of the same size out, split across the cores."""

    size: int = dim()

    a = In(size, to=BinaryElementwiseOverlay.a)
    b = In(size, to=BinaryElementwiseOverlay.b)
    y = Out(size, from_=BinaryElementwiseOverlay.y)

    def compatible(self) -> None:
        ov = self.ov
        unit = ov.num_aie_columns * ov.tile_size
        if self.size % unit:
            raise Incompatible(
                f"size ({self.size}) must be a multiple of "
                f"num_aie_columns * tile_size ({unit})"
            )
        n = ov.per_tile * ov.num_aie_columns
        if self.size % n:
            raise Incompatible(
                f"Number of elements ({self.size}) must be a multiple of {n}."
            )

    def residents(self) -> dict[str, int]:
        ov = self.ov
        return {"count": self.size // (ov.per_tile * ov.num_aie_columns)}
