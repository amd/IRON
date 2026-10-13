# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An operator's operands: the host buffers it is called with, each with a
``tile=`` its own stream into the array.
"""

from __future__ import annotations

import copy
import math
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Self

import aie.iron
import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron.device import Tile
from aie.utils import bfp
from ml_dtypes import bfloat16

from .field import DimRef
from .shape import OptionalDim, Shape, _DimSpec
from .member import Member
from .value import DispatchTime, Extent, Value

if TYPE_CHECKING:
    from .operator import Operator


@dataclass(frozen=True)
class Lane:
    """One fifo of an operand's stream: what ``array()`` binds a shim end to
    and a sequence fills or drains.
    """

    buffer: Operand
    index: int = 0

    def bind(self, handle) -> None:
        handles = self.buffer.lane_handles
        if handles[self.index] is not None:
            raise ValueError(f"{self.buffer.name}[{self.index}] is already bound")
        handles[self.index] = handle

    @property
    def handle(self):
        h = self.buffer.lane_handles[self.index]
        if h is None:
            raise ValueError(
                f"{self.buffer.name}[{self.index}] was never bound: array() must "
                f"call .bind() on every operand's lane"
            )
        return h

    @property
    def name(self) -> str:
        return f"{self.buffer.name}{self.index}"

    @property
    def shim(self) -> Tile | None:
        """The shim tile this lane is pinned to (``via=``), if any."""
        via = self.buffer.via
        if isinstance(via, Tile):
            return via if self.buffer.count == 1 else None
        return None if via is None else via[self.index]


class Operand(Member["Operand"]):
    """A host buffer: shape in extents, a dtype, and the stream it moves through.

    Declared in an operator's body; on an instance, ``op.x`` is the operand
    bound to it (`of`), its shape and tile resolved.

    Args:
        dims: The host shape.
        dtype: The element type.
        tile: What one fifo element holds, in the units a core reads. With
            one the buffer is its own stream; without one it is an argument
            of a hand-written `Operator.sequence`.
        per: The field (or fields, multiplied) the stream is replicated over.
        depth: The fifo depth.
        via: The shim tile of each lane, mlir-aie's `Tile` (one for a
            one-lane stream): a stream into a shipped image is pinned.
        channel: The shim DMA channel every lane of a pinned stream uses.
        replicate: Every `per=` lane gets the whole buffer, not a share.
        broadcast: One fifo every worker consumes.
        when: A bool `Param()`; the operand and its stream exist only where
            it is true, and a call giving the operand by keyword sets it.
        finish: The cores apply the operator's `finish` to each tile of
            this output before releasing it (`Finish`), so a consumer folds
            into them. `True`, or the block of the output one core fills
            of a tile, in an order of its own (GEMM's C, joined from a
            column's cores): a step there must not depend on the order.
        prepare: The cores apply the operator's `prepare` to each tile of
            this input after acquiring it (`Prepare`), so the step that
            produced it folds into them. The operator's output must be
            linear in it, which its tolerance relies on. Without a tile, a
            hand-written sequence carries it, a line its innermost
            dimension, and the prologue's inputs ride the `feed=True` input.
        feed: The finish's inputs ride this input's stream rather than
            streams of their own: after the tiles a core reads for one
            output tile, the next tile of this stream holds that output
            tile's input of each (`Finish.apply`), so the finish takes no
            input channel of the core's and no shim channel. An untiled
            prepared input's prologue inputs ride it too, a tile each,
            where the operator's cores take them (`Prepare.apply`).
    """

    fills: ClassVar[bool]
    drains: ClassVar[bool]

    def __init__(
        self,
        *dims: _DimSpec,
        dtype: Any = bfloat16,
        tile: Any = None,
        per: _DimSpec | None = None,
        depth: int = 2,
        via: Tile | list[Tile] | None = None,
        channel: int | None = None,
        replicate: bool = False,
        broadcast: bool = False,
        when: _DimSpec | None = None,
        finish: bool | tuple[_DimSpec, ...] = False,
        prepare: bool = False,
        feed: bool = False,
    ) -> None:
        if per is not None and broadcast:
            raise TypeError("a stream is either per=<dim> or broadcast, not both")
        if replicate and per is None:
            raise TypeError(
                "replicate=True needs per=<dim>: every slot receives the whole buffer"
            )
        # A step over a line sees a tile as a run of the output's elements.
        if finish and (
            isinstance(tile, (tuple, list))
            and len(tile) != 1
            or tile is None
            or not self.drains
        ):
            raise TypeError(
                "finish=True names a streamed output of one-dimensional tiles, "
                "which a core finishes"
            )
        if prepare and (
            isinstance(tile, (tuple, list)) and len(tile) != 1 or self.drains
        ):
            raise TypeError(
                "prepare=True names an input of one-dimensional tiles, or of "
                "none, which a core prepares"
            )
        if feed and (tile is None or self.drains):
            raise TypeError("feed=True names a streamed input, which a finish rides")
        self.dims = Shape(tuple(dims))
        self.declared_dtype = dtype
        self.when = when
        self.tile_dims = (
            None
            if tile is None
            else Shape(tuple(tile) if isinstance(tile, (tuple, list)) else (tile,))
        )
        self.per = (
            None if per is None else Shape(per if isinstance(per, tuple) else (per,))
        )
        self.depth = depth
        self.via = via
        self.channel = channel
        self.replicate = replicate
        self.broadcast = broadcast
        self.finish = bool(finish)
        self.finish_block = None if isinstance(finish, bool) else Shape(finish)
        self.prepare = prepare
        self.feed = feed
        self.op: Operator | None = None
        self.lane_handles: list[Any] = []

    def of(self, op: Operator) -> Self:
        """This operand on ``op``: its shape resolved there, its lanes unbound."""
        bound = copy.copy(self)
        bound.op = op
        bound.lane_handles = []
        return bound

    def _resolve(self, shape: Shape) -> tuple[int, ...]:
        try:
            return shape.resolve(self.op)
        except ValueError as e:
            raise ValueError(
                f"{self.name}: {e}. Resolve the operator first (resolved(dev))"
            ) from None

    # Resolved on use: a shape may depend on a tunable the device fills.
    @property
    def shape(self) -> tuple[int, ...]:
        return self.dims.resolve(self.op)

    @property
    def dtype(self):
        dtype = self.declared_dtype
        return dtype.of(self.op) if isinstance(dtype, DimRef) else dtype

    @property
    def elements(self) -> int:
        return int(np.prod(self.shape)) if self.shape else 1

    @property
    def tap(self) -> TensorAccessPattern:
        return TensorAccessPattern.full((self.elements,))

    @property
    def nbytes(self) -> int:
        # np.dtype() raises on the block-float marker class.
        return self.elements * bfp.itemsize(self.dtype)

    # numpy has no block-float dtype: the host sees bytes where the array counts blocks.
    @property
    def host_shape(self) -> tuple[int, ...]:
        return (self.nbytes,) if bfp.is_bfp(self.dtype) else tuple(self.shape)

    @property
    def host_dtype(self):
        return np.uint8 if bfp.is_bfp(self.dtype) else self.dtype

    @property
    def placement(self) -> tuple[int, int]:
        """The elements of the runtime tensor this buffer is, and the one it
        starts at: a larger buffer's, where a graph placed it in one
        (``Operator.placed``).
        """
        return next(
            (
                (into, start)
                for name, into, start in self.op.placements
                if name == self.name
            ),
            (self.elements, 0),
        )

    @property
    def held_nbytes(self) -> int:
        """The bytes of the runtime tensor this buffer is (``placement``)."""
        return self.placement[0] * bfp.itemsize(self.dtype)

    @property
    def flat_type(self):
        """The runtime-sequence argument type: the runtime tensor
        (``placement``) flattened to 1-D, in its own element units (blocks,
        for block float).
        """
        return np.ndarray[(self.placement[0],), np.dtype[self.dtype]]

    @property
    def streamed(self) -> bool:
        return self.tile_dims is not None

    @property
    def tile_shape(self) -> tuple[int, ...]:
        if self.tile_dims is None:
            raise TypeError(f"{self.name} is declared without a tile=: no stream")
        return self._resolve(self.tile_dims)

    @property
    def tile(self):
        """The fifo element type: ``np.ndarray[shape, dtype]``."""
        return np.ndarray[self.tile_shape, np.dtype[self.dtype]]

    @property
    def finish_line(self) -> int:
        """The elements a core finishes at once: its block of a tile, or the tile."""
        block = self.finish_block
        return math.prod(self.tile_shape if block is None else self._resolve(block))

    @property
    def count(self) -> int:
        """The stream's lanes (fifos)."""
        if self.tile_dims is None:
            raise TypeError(f"{self.name} is declared without a tile=: no stream")
        return 1 if self.per is None else math.prod(self._resolve(self.per))

    def lane(self, index: int = 0) -> Lane:
        if not 0 <= index < self.count:
            raise IndexError(f"{self.name} has {self.count} lanes")
        if not self.lane_handles:
            self.lane_handles = [None] * self.count
        return Lane(self, index)

    def bind(self, handle, index: int = 0) -> None:
        self.lane(index).bind(handle)

    @property
    def handle(self):
        if self.count != 1:
            raise ValueError(f"{self.name} is per-{self.count}; name a lane")
        return self.lane(0).handle

    @property
    def handles(self) -> list[Any]:
        return [self.lane(i).handle for i in range(self.count)]

    @property
    def batch_axes(self) -> int:
        """Leading ``OptionalDim()`` dimensions that are present on this instance."""
        n = 0
        for d in self.dims.dims:
            if not isinstance(d, OptionalDim):
                break
            if Shape.dim(d.ref, self.op) > 1:
                n += 1
        return n

    def extent_axis(self, extent: Extent) -> int | None:
        return self.dims.axis_of(extent.field.name, self.op)

    def extent_unit(self, axis: int) -> int:
        """The rows along ``axis`` of one round-robin unit under a bound:
        ``Operator.extent_unit``, else the stream tile's.
        """
        unit = self.op.extent_unit(self.name)
        if unit is not None:
            return unit
        tile_shape = self.tile_shape if self.streamed else ()
        k = axis - (len(self.shape) - len(tile_shape))
        return tile_shape[k] if k >= 0 else 1

    @property
    def bounded(self) -> tuple[Extent, int, Value] | None:
        """``(extent, axis, word)`` when a bound extent sizes an axis, ``word``
        the per-call tiles per lane.
        """
        op = self.op
        for name in op.bound_extents:
            extent = op.value(name)
            assert isinstance(extent, Extent)
            axis = self.extent_axis(extent)
            if axis is not None:
                return extent, axis, op.value(f"{name}_{self.name}")
        return None

    def __getitem__(self, index) -> BufferView:
        """A basic slice for ``rt.fill``/``rt.drain``; a ``Scratchpad`` start
        patches the base address per call.
        """
        return BufferView(self, index)

    def __repr__(self) -> str:
        if self.op is None:
            return f"{type(self).__name__}({self.dims})"
        return f"<{type(self).__name__} {self.name} {self.shape} {bfp.dtype_name(self.dtype)}>"


# mlir-aie's markers type-check as `type[np.ndarray]`; at runtime they are classes.
class In(Operand, aie.iron.In):  # pyright: ignore[reportGeneralTypeIssues]
    """A buffer the host fills and the array reads."""

    fills = True
    drains = False


class Out(Operand, aie.iron.Out):  # pyright: ignore[reportGeneralTypeIssues]
    """A buffer the array writes and the host reads."""

    fills = False
    drains = True


class InOut(Operand, aie.iron.InOut):  # pyright: ignore[reportGeneralTypeIssues]
    """A buffer the host fills and the array writes in place; what the
    stream does not drain stays as the host gave it.
    """

    fills = True
    drains = True


class BufferView:
    """``buffer[index]``: a slice of an operand, resolved to a transfer by the build."""

    def __init__(self, buffer: Operand, index) -> None:
        self.buffer = buffer
        self.index = index if isinstance(index, tuple) else (index,)
        self.offset_by: Value | None = None
        static = []
        for idx in self.index:
            if isinstance(idx, slice) and isinstance(idx.start, Value):
                if idx.stop is not None or idx.step is not None:
                    raise ValueError(
                        f"{buffer.name}[{idx}]: a per-call start takes the whole axis"
                    )
                if self.offset_by is not None:
                    raise ValueError(
                        f"{buffer.name}: only one axis may start at a per-call value"
                    )
                if isinstance(idx.start, DispatchTime):
                    raise ValueError(
                        f"{buffer.name}: {idx.start.name} is a DispatchTime value; "
                        f"only a Scratchpad value can move a transfer's base address"
                    )
                self.offset_by = idx.start
                static.append(slice(None))
            else:
                static.append(idx)
        self.static_index = tuple(static)

    @property
    def tap(self) -> TensorAccessPattern:
        return TensorAccessPattern.full(self.buffer.shape)[self.static_index]

    def __repr__(self) -> str:
        return f"{self.buffer.name}[{self.index}]"
