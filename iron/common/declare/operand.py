# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An operator's operands: the host buffers it is called with, each with an
``obj_type=`` its own stream into the array.
"""

from __future__ import annotations

import copy
import math
from dataclasses import Field
from typing import TYPE_CHECKING, Any, ClassVar, Self

import aie.iron
import numpy as np
from aie.dialects.aie import AIETileType, DMAChannelDir
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import DmaEndpoint
from aie.utils import bfp
from ml_dtypes import bfloat16

from .field import ParamSpec
from .shape import Shape, _DimSpec
from .member import Member
from .value import DispatchTime, Extent, Value

if TYPE_CHECKING:
    from .operator import Operator


class Operand(Member["Operand"]):
    """A host buffer: shape in extents, a dtype, and the stream it moves through.

    Declared in an operator's body; on an instance, ``op.x`` is the operand
    bound to it (`of`), its shape and tile resolved.

    Args:
        dims: The host shape.
        dtype: The element type.
        obj_type: What one fifo element holds, in the units a core reads
            (upstream's `ObjectFifo.obj_type`, a shape here rather than an
            `np.ndarray` type). With one the buffer is its own stream;
            without one it is an argument of a hand-written
            `Operator.sequence`.
        per: The field (or fields, multiplied) the stream is replicated over.
        depth: The fifo depth.
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
    # AIE2 and AIE2P both have eight 8 KB banks of core memory; the target
    # model gives the total (Device.core_memory_bytes) but not the banking,
    # so this is interim, keyed by device name until it reads the model.
    L1_BANK_BYTES: ClassVar[dict[str, int]] = {"npu1": 8192, "npu2": 8192}

    def __init__(
        self,
        *dims: _DimSpec,
        dtype: Any = bfloat16,
        obj_type: Any = None,
        per: _DimSpec | None = None,
        depth: int = 2,
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
            isinstance(obj_type, (tuple, list))
            and len(obj_type) != 1
            or obj_type is None
            or not self.drains
        ):
            raise TypeError(
                "finish=True names a streamed output of one-dimensional tiles, "
                "which a core finishes"
            )
        if prepare and (
            isinstance(obj_type, (tuple, list)) and len(obj_type) != 1 or self.drains
        ):
            raise TypeError(
                "prepare=True names an input of one-dimensional tiles, or of "
                "none, which a core prepares"
            )
        if feed and (obj_type is None or self.drains):
            raise TypeError("feed=True names a streamed input, which a finish rides")
        self.dims = Shape(tuple(dims))
        self.declared_dtype = dtype
        self.when = when
        self.obj_dims = (
            None
            if obj_type is None
            else Shape(
                tuple(obj_type) if isinstance(obj_type, (tuple, list)) else (obj_type,)
            )
        )
        self.per = (
            None if per is None else Shape(per if isinstance(per, tuple) else (per,))
        )
        self.depth = depth
        self.replicate = replicate
        self.broadcast = broadcast
        self.finish = bool(finish)
        self.finish_block = None if isinstance(finish, bool) else Shape(finish)
        self.prepare = prepare
        self.feed = feed
        self.op: Operator | None = None
        self.lane_handles: list[Any] = []
        # The OperatorRuntime whose sequence body is running, which fill/drain emit through.
        self.runtime = None

    def of(self, op: Operator) -> Self:
        """This operand on ``op``: its shape resolved there, its lanes unbound."""
        bound = copy.copy(self)
        bound.op = op
        bound.lane_handles = []
        bound.runtime = None
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
        return vars(self.op)[dtype.name] if isinstance(dtype, Field) else dtype

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
        return self.obj_dims is not None

    @property
    def obj_shape(self) -> tuple[int, ...]:
        if self.obj_dims is None:
            raise TypeError(f"{self.name} is declared without an obj_type=: no stream")
        return self._resolve(self.obj_dims)

    @property
    def obj_type(self):
        """The fifo element type: ``np.ndarray[shape, dtype]``."""
        return np.ndarray[self.obj_shape, np.dtype[self.dtype]]

    @property
    def l1_depth(self) -> int:
        """The depth a core-side fifo of this operand's tiles can have: two,
        or one when a tile spans more than an L1 bank of the bound device.
        """
        obj_bytes = math.prod(self.obj_shape) * np.dtype(self.dtype).itemsize
        return 1 if obj_bytes > self.L1_BANK_BYTES[self.op.dev.name] else 2

    @property
    def finish_line(self) -> int:
        """The elements a core finishes at once: its block of a tile, or the tile."""
        block = self.finish_block
        return math.prod(self.obj_shape if block is None else self._resolve(block))

    @property
    def count(self) -> int:
        """The stream's lanes (fifos)."""
        if self.obj_dims is None:
            raise TypeError(f"{self.name} is declared without an obj_type=: no stream")
        return 1 if self.per is None else math.prod(self._resolve(self.per))

    def bind(self, handles) -> None:
        """Bind each lane to the fifo end ``array()`` built for it.

        Args:
            handles: One handle per lane, in lane order, or the handle of a
                one-lane operand.

        Raises:
            ValueError: Another number of handles than lanes, or the operand
                is bound already.
        """
        handles = list(handles) if isinstance(handles, (list, tuple)) else [handles]
        if len(handles) != self.count:
            raise ValueError(
                f"{self.name} has {self.count} lanes; bind() was given "
                f"{len(handles)} handles"
            )
        if self.lane_handles:
            raise ValueError(f"{self.name} is already bound")
        self.lane_handles = handles

    def pin(self, endpoints: list[DmaEndpoint]) -> None:
        """Pin each lane to a shim DMA channel of routes built elsewhere (a
        shipped image's, or two shims an ``array()`` joins): a transfer of
        the lane is a shim DMA task on it. ``array()`` returns the endpoints
        among what it built.

        Args:
            endpoints: One mlir-aie ``DmaEndpoint`` per lane, in lane order:
                a shim tile, MM2S for an input or S2MM for an output, and a
                channel.

        Raises:
            ValueError: An endpoint moves the other way or names no channel,
                another number of endpoints than lanes, or the operand is
                bound already.
        """
        moves = DMAChannelDir.S2MM if self.drains else DMAChannelDir.MM2S
        for e in endpoints:
            if e.direction != moves or e.channel is None:
                raise ValueError(
                    f"{self.name} moves {moves} on a channel it names, not {e}"
                )
        self.bind(endpoints)

    @property
    def handles(self) -> list[Any]:
        if not self.lane_handles:
            raise ValueError(
                f"{self.name} was never bound: array() must bind() every "
                f"streamed operand"
            )
        return self.lane_handles

    def fill(
        self,
        tap: TensorAccessPattern | None = None,
        *,
        lane: int | None = None,
        group=None,
        wait: bool = False,
        source: Operand | None = None,
        offset_parameter: Value | None = None,
        length_parameter: Value | None = None,
        length_unit: int | None = None,
        repeat_parameter: Value | None = None,
        managed: bool = True,
        finishing: TensorAccessPattern | None = None,
    ):
        """Fill lane ``lane`` of this operand's stream from the host, in a
        ``sequence(rt)``: mlir-aie's ``ObjectFifoHandle.fill`` on the lane's
        fifo, or a shim DMA task on a pinned lane.

        A prepared input's lane is then filled with each of the operator's
        ``prepare_inputs``, which its cores acquire with the tile. A fill of
        a fed input's lane from that input takes its whole share, an output
        tile's worth at a time, each followed by that output tile of each
        finish input riding it.

        A per-call parameter is a ``Value`` of the operator: on a full ELF its
        scratchpad word, patched into the descriptor; on an xclbin a
        dispatch-time scalar, which regenerates the instruction stream per
        call.

        Args:
            tap: The walk over ``source``; all of it where None.
            lane: The lane; may be left out of a one-lane operand only.
            group: The ``TaskGroup`` the transfer joins.
            wait: The transfer concludes with an await rather than a free.
            source: The operand whose data moves through this one's lane,
                where it is not this one (a prologue input riding it).
            offset_parameter: A per-call element offset of ``tap``.
            length_parameter: A per-call count of ``length_unit`` elements:
                one descriptor's length, its outermost dimension below the
                iteration, in whole 16-byte units; the pattern must fit one
                descriptor.
            length_unit: The elements one unit of ``length_parameter`` is.
            repeat_parameter: A per-call count of extra runs of ``tap``, at
                most its outermost size less one.
            managed: False hands the queue slot and descriptors to the
                compiler, which frees them after a later wait; joins no
                group.
            finishing: For a fill of a fed input, the part of the lane's
                share of the output it computes (a pattern over the
                output), where it is not the whole: a hand-written sequence
                filling a lane in pieces.

        Returns:
            The transfer's ``Task``.

        Raises:
            ValueError: ``lane`` is left out of a multi-lane operand, a fed
                input's lane is filled with a per-call parameter or with other
                than its share and no ``finishing``, or a per-call length's
                pattern does not fit one descriptor.
        """
        return self._runtime().transfer(
            "fill",
            self,
            tap,
            lane=lane,
            group=group,
            wait=wait,
            source=source,
            offset_parameter=offset_parameter,
            length_parameter=length_parameter,
            length_unit=length_unit,
            repeat_parameter=repeat_parameter,
            managed=managed,
            finishing=finishing,
        )

    def drain(
        self,
        tap: TensorAccessPattern | None = None,
        *,
        lane: int | None = None,
        group=None,
        wait: bool = False,
        offset_parameter: Value | None = None,
        length_parameter: Value | None = None,
        length_unit: int | None = None,
        repeat_parameter: Value | None = None,
        managed: bool = True,
    ):
        """Drain lane ``lane`` of this operand's stream to the host; the
        arguments are ``fill``'s, and a drain the sequence must see finish
        before it ends passes ``wait=True``.
        """
        return self._runtime().transfer(
            "drain",
            self,
            tap,
            lane=lane,
            group=group,
            wait=wait,
            offset_parameter=offset_parameter,
            length_parameter=length_parameter,
            length_unit=length_unit,
            repeat_parameter=repeat_parameter,
            managed=managed,
        )

    def _runtime(self):
        if self.runtime is None:
            raise ValueError(
                f"{self.name}.fill/drain run in the operator's sequence(rt)"
            )
        return self.runtime

    @property
    def batch_axes(self) -> int:
        """1 if a leading ``T | None`` dimension is present on this instance, else 0."""
        dims = self.dims.dims
        if (
            dims
            and ParamSpec.of(dims[0]) is not None
            and dims[0].name in self.op.declaration.nullable
        ):
            return 1 if vars(self.op)[dims[0].name] is not None else 0
        return 0

    def extent_axis(self, extent: Extent) -> int | None:
        return self.dims.axis_of(extent.field.name, self.op)

    def extent_unit(self, axis: int) -> int:
        """The rows along ``axis`` of one round-robin unit under a bound:
        ``Operator.extent_unit``, else the stream tile's.
        """
        unit = self.op.extent_unit(self.name)
        if unit is not None:
            return unit
        obj_shape = self.obj_shape if self.streamed else ()
        k = axis - (len(self.shape) - len(obj_shape))
        return obj_shape[k] if k >= 0 else 1

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

    def transfers(
        self,
    ) -> list[tuple[int, TensorAccessPattern, Value | None, int | None]]:
        """The derived ``(lane, tap, length_parameter, length_unit)``
        transfers of this operand.

        Unbounded, the whole buffer for a one-lane or replicated stream,
        else the first non-batch axis in one block per lane. Under a bound,
        round-robin by tile: lane ``k`` takes tiles ``k, k + lanes, ...``,
        so each lane has a fixed offset and stride and one length a call
        patches, counting tiles of ``length_unit`` elements.

        Raises:
            ValueError: The operand has no obj_type=, does not divide across
                its lanes, or is bounded on an axis the split cannot bound or
                in tiles no descriptor holds.
        """
        # design/ imports declare, so BdLimits is imported where it is used.
        from ..design.bd import BdLimits

        name = f"{type(self.op).__name__}.{self.name}"
        if not self.streamed:
            raise ValueError(
                f"{name} has no obj_type=, so its sequence cannot be derived; add "
                f"obj_type= or override sequence(rt)"
            )
        count, shape = self.count, self.shape
        bounded = self.bounded
        if bounded is None:
            if count == 1:
                return [(0, self.tap, None, None)]
            if self.replicate:
                return [(i, self.tap, None, None) for i in range(count)]
            axis = self.batch_axes
            if axis >= len(shape) or shape[axis] % count:
                raise ValueError(
                    f"{self.name} {shape} does not divide across its {count} lanes "
                    f"on axis {axis}. Check {type(self.op).__name__}.compatible()"
                )
            parts = TensorAccessPattern.full(shape).partition(count, axis)
            return [(i, parts[i], None, None) for i in range(count)]
        extent, axis, word = bounded
        if axis != self.batch_axes:
            raise ValueError(
                f"{name}: {extent.name} bounds axis {axis}, but the derived "
                f"sequence splits axis {self.batch_axes}; override sequence(rt) "
                f"to bound another axis"
            )
        lanes = 1 if self.replicate else count
        inner = math.prod(shape[axis + 1 :])
        tile_rows = self.extent_unit(axis)
        if shape[axis] % (lanes * tile_rows):
            raise ValueError(
                f"{self.name} {shape}: axis {axis} does not divide into "
                f"{tile_rows}-row tiles over {lanes} lanes"
            )
        if axis > 1:
            raise ValueError(
                f"{self.name} {shape}: bounding axis {axis} needs {axis + 3} "
                f"descriptor dimensions; a descriptor has four"
            )
        tiles = shape[axis] // (lanes * tile_rows)
        run = tile_rows * inner
        shim = BdLimits.of(self.op.dev, AIETileType.ShimNOCTile)
        granule = shim.granule(self.dtype)
        halves = shim.factor(run, granule)
        if halves is None:
            raise ValueError(
                f"{self.name}: a {run}-element tile does not fit one descriptor"
            )
        # A unit D1 is stripped, which would drop the tile count into D1's
        # wrap; past it, a tile split in two keeps the count on D2, which has none.
        if halves[0] == 1 and tiles > shim.wrap and run % (2 * granule) == 0:
            halves = (2, run // 2)
        iterations = shape[0] if axis else 1
        tiled = TensorAccessPattern.full((iterations, tiles, lanes, run))
        out = []
        for lane in range(lanes):
            tap = tiled[:, :, lane].split(2, halves[1])
            if not shim.fits(tap, self.dtype):
                raise ValueError(
                    f"{self.name} {shape}: the round-robin split over {lanes} "
                    f"lanes does not fit one descriptor per lane"
                )
            for k in range(count) if self.replicate else [lane]:
                out.append((k, tap, word, run))
        return out

    def __getitem__(self, index) -> TensorAccessPattern:
        """A basic slice of this operand, as the pattern ``fill``/``drain`` take."""
        return TensorAccessPattern.full(self.shape)[index]

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
