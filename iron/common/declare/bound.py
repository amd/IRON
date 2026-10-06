# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an instance's member attribute returns.

A declaration is class-level and symbolic. Binding it to an instance turns
every ``DimRef`` into an integer (``Shape.resolve``).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.utils import bfp

from .field import DimRef, OptionalDim, Shape
from .member import DispatchTime, Extent, Shim, _Buffer, _Value

if TYPE_CHECKING:
    from .operator import Operator


@dataclass(frozen=True)
class Lane:
    """One fifo of an operand's stream: what ``array()`` binds a shim end to
    and a sequence fills or drains.
    """

    buffer: BoundBuffer
    index: int = 0

    def bind(self, handle) -> None:
        """Bind the shim end of a fifo to this lane."""
        handles = self.buffer._handles
        if handles[self.index] is not None:
            raise ValueError(f"{self.buffer.name}[{self.index}] is already bound")
        handles[self.index] = handle

    @property
    def handle(self):
        h = self.buffer._handles[self.index]
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
    def shim(self) -> Shim | None:
        """The declared shim endpoint of this lane, if pinned."""
        via = self.buffer.member.via
        if isinstance(via, Shim):
            return via if self.buffer.count == 1 else None
        return None if via is None else via[self.index]


class BoundBuffer:
    """A buffer on an operator instance: concrete shape and dtype, and, with
    a ``tile=``, its stream's tile, lanes and fifo handles.
    """

    def __init__(self, member: _Buffer, op: "Operator") -> None:
        self.member = member
        self._op = op
        self.name = member.name
        self.direction = member.direction
        self._handle_slots: list[Any] | None = None

    def _resolve(self, shape: Shape) -> tuple[int, ...]:
        try:
            return shape.resolve(self._op)
        except ValueError as e:
            raise ValueError(
                f"{self.name}: {e}. Resolve the operator first (resolved(dev))"
            ) from None

    # Resolved on use rather than at construction: a shape, dtype or tile
    # may depend on a tunable the device fills (flm/gemm's B layout), and an
    # unresolved operator must still be usable as a value.
    @property
    def shape(self) -> tuple[int, ...]:
        return self.member.shape.resolve(self._op)

    @property
    def dtype(self):
        dtype = self.member.dtype
        return dtype.of(self._op) if isinstance(dtype, DimRef) else dtype

    @property
    def elements(self) -> int:
        return int(np.prod(self.shape)) if self.shape else 1

    @property
    def tap(self) -> TensorAccessPattern:
        """The whole buffer, one linear run."""
        return TensorAccessPattern.full((self.elements,))

    @property
    def nbytes(self) -> int:
        # bfp.itemsize covers ordinary dtypes too, and is the only thing that
        # reports the 9 bytes a block-float block occupies: the marker class
        # is not a numpy dtype, so np.dtype() raises on it.
        return self.elements * bfp.itemsize(self.dtype)

    # The host's view. Only block floating point makes the host and the array
    # disagree on the unit: numpy has no block-float dtype, so the host buffer
    # is the equivalent run of bytes while the array, the sequence and every
    # descriptor count blocks.
    @property
    def host_shape(self) -> tuple[int, ...]:
        return (self.nbytes,) if bfp.is_bfp(self.dtype) else tuple(self.shape)

    @property
    def host_dtype(self):
        return np.uint8 if bfp.is_bfp(self.dtype) else self.dtype

    @property
    def flat_type(self):
        """The runtime-sequence argument type: the buffer flattened to 1-D.

        In the buffer's own element units, the units its transfers use. A
        packed operand declared in block-float blocks lowers to a memref of
        blocks, so a descriptor's offset and length count blocks, as the
        array and the core do.
        """
        return np.ndarray[(self.elements,), np.dtype[self.dtype]]

    # -- the stream, for a buffer declared with a tile= --------------------

    @property
    def streamed(self) -> bool:
        """Whether the buffer is its own stream (declared with ``tile=``)."""
        return self.member.tile is not None

    def _stream(self) -> _Buffer:
        if self.member.tile is None:
            raise TypeError(f"{self.name} is declared without a tile=: no stream")
        return self.member

    @property
    def tile_shape(self) -> tuple[int, ...]:
        """What one fifo element holds."""
        return self._resolve(self._stream().tile)

    @property
    def tile(self):
        """The fifo element type of this buffer's stream: ``np.ndarray[shape, dtype]``."""
        return np.ndarray[self.tile_shape, np.dtype[self.dtype]]

    @property
    def count(self) -> int:
        """How many lanes (fifos) the stream is replicated over."""
        per = self._stream().per
        return 1 if per is None else math.prod(self._resolve(per))

    @property
    def depth(self) -> int:
        """The declared fifo depth of this buffer's stream."""
        return self._stream().depth

    @property
    def replicate(self) -> bool:
        return self._stream().replicate

    @property
    def _handles(self) -> list[Any]:
        if self._handle_slots is None:
            self._handle_slots = [None] * self.count
        return self._handle_slots

    def lane(self, index: int = 0) -> Lane:
        """One lane of the stream, to bind a fifo's shim end to or fill/drain."""
        if not 0 <= index < self.count:
            raise IndexError(f"{self.name} has {self.count} lanes")
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
        for d in self.member.shape.dims:
            if not isinstance(d, OptionalDim):
                break
            if Shape.dim(d.ref, self._op) > 1:
                n += 1
        return n

    def extent_axis(self, extent: Extent) -> int | None:
        """The axis of this operand that ``extent``'s field sizes, or None."""
        return self.member.shape.axis_of(extent.field.name, self._op)

    def extent_unit(self, axis: int) -> int:
        """The rows along ``axis`` one round-robin unit of this operand holds
        under a bound: what the operator says (``Operator.extent_unit``),
        else the stream tile's rows there.
        """
        unit = self._op.extent_unit(self.name)
        if unit is not None:
            return unit
        tile_shape = self.tile_shape if self.streamed else ()
        k = axis - (len(self.shape) - len(tile_shape))
        return tile_shape[k] if k >= 0 else 1

    @property
    def bounded(self) -> tuple[Extent, int, "BoundValue"] | None:
        """``(extent, axis, word)`` when a bound extent sizes an axis of this
        operand: the extent, the axis, and the per-call word of tiles per
        lane the derived sequence patches its descriptors with.
        """
        op = self._op
        for name in op.bound_extents:
            extent = op.value(name).member
            assert isinstance(extent, Extent)
            axis = self.extent_axis(extent)
            if axis is not None:
                return extent, axis, op.value(f"{name}_{self.name}")
        return None

    def __getitem__(self, index) -> "BufferView":
        """A basic slice of this buffer, for ``rt.fill``/``rt.drain`` in an override.

        A slice start may be a ``Scratchpad`` value, in which case the
        transfer's base address is patched per call.
        """
        return BufferView(self, index)

    def __repr__(self) -> str:
        return (
            f"<{self.direction.value} {self.name} {self.shape} "
            f"{bfp.dtype_name(self.dtype)}>"
        )


class BufferView:
    """``buffer[index]``: a slice of a bound buffer, resolved to a transfer by the build."""

    def __init__(self, buffer: BoundBuffer, index) -> None:
        self.buffer = buffer
        self.index = index if isinstance(index, tuple) else (index,)
        self.offset_by: BoundValue | None = None
        static = []
        for idx in self.index:
            if isinstance(idx, slice) and isinstance(idx.start, BoundValue):
                if idx.stop is not None or idx.step is not None:
                    raise ValueError(
                        f"{buffer.name}[{idx}]: a per-call start takes the whole axis"
                    )
                if self.offset_by is not None:
                    raise ValueError(
                        f"{buffer.name}: only one axis may start at a per-call value"
                    )
                if isinstance(idx.start.member, DispatchTime):
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
        """The static part of the slice, over the buffer's shape."""
        return TensorAccessPattern.full(self.buffer.shape)[self.static_index]

    def __repr__(self) -> str:
        return f"{self.buffer.name}[{self.index}]"


class BoundValue:
    """A value on an operator: per call, or written once per build.

    On a full ELF ``param`` is the upstream ``ScratchpadParameter`` the
    build creates. On an image without a scratchpad (an xclbin run has none) the
    value is lowered as a dispatch-time scalar of the sequence: ``param`` is
    the dispatch parameter, ``ssa`` its live value inside the sequence body,
    an offset use adds it to the transfer's offset, and a core-read use is a
    resident the preamble writes from it (``bind``).
    """

    def __init__(self, member: _Value, owner) -> None:
        self.member = member
        self.name = member.name
        self.dtype = member.dtype
        self.param: Any = None  # the upstream ScratchpadParameter, set by the build
        self.symbol: str | None = None
        self.ssa = None  # the sequence's scalar, when lowered at dispatch time
        self.targets: list[tuple[Any, int]] = []
        # A Value written once per build has a resident's placement.
        self.address = member.address
        self.lock = member.lock
        self.optional = member.optional
        self.derive = member.derive

    def bind(self, buffers, index: int = 0) -> None:
        """Bind to one runtime-parameter buffer, or one per worker; the preamble
        writes ``[index]`` from the per-call value (an image without a scratchpad).
        """
        if not isinstance(buffers, (list, tuple)):
            buffers = [buffers]
        self.targets.extend((b, index) for b in buffers)

    def __repr__(self) -> str:
        return f"<{self.member.kind} {self.name} {np.dtype(self.dtype).name}>"
