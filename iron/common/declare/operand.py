# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An operator's operands: the host buffers it is called with.

Each with an ``obj_shape=`` is its own stream into the array.
"""

from __future__ import annotations

import math
from contextvars import ContextVar
from typing import TYPE_CHECKING, Any

import numpy as np
from aie.dialects.aie import DMAChannelDir
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import DmaEndpoint, TaskGroup
from aie.utils import bfp
from aie.utils.compile.jit.params import OperatorParam, PerCallMember, Select, resolve

from .value import Value

if TYPE_CHECKING:
    from ..design import OperatorRuntime
    from .operator import Operator

# The OperatorRuntime whose sequence body is running, which fill/drain emit through.
active_runtime: ContextVar[OperatorRuntime | None] = ContextVar(
    "active_runtime", default=None
)


class Operand:
    """An operand as one operator holds it (``op.x``).

    The resolved ``In``, ``Out`` or ``InOut``, read through on use (a shape
    may follow a tunable), and its bound ``lane_handles``. An ``InOut``
    keeps what its stream does not drain.
    """

    def __init__(self, member: Any, op: Operator) -> None:
        self.op = op
        self.lane_handles: list[Any] = []
        self._decl = member.of(op)

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):  # unset while a copy is made
            raise AttributeError(name)
        if hasattr(type(self), name):
            # One of this class's properties raised: raise its error again,
            # not the declaration's lacking the name.
            return getattr(type(self), name).__get__(self)
        return getattr(self._decl, name)

    role = property(lambda self: type(self._decl))

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
    def flat_type(self):
        """The runtime-sequence argument type: this buffer flattened to 1-D.

        In its own element units (blocks, for block float).
        """
        return np.ndarray[(self.elements,), np.dtype[self.dtype]]

    @property
    def obj_type(self):
        """The fifo element type: ``np.ndarray[shape, dtype]``."""
        return np.ndarray[self.obj_shape, np.dtype[self.dtype]]

    @property
    def l1_depth(self) -> int:
        """The depth a core-side fifo of this operand's tiles can have: two, or one.

        One when a tile spans more than a hardware bank of the bound
        device's core memory.
        """
        dev = self.op.dev
        assert dev is not None, "l1_depth is read during build(), with a device bound"
        # Half a programmer bank: at the whole one, two 16 KB streams no longer fit.
        bank = dev.core_memory_bytes // (2 * dev.core_memory_banks)
        obj_bytes = math.prod(self.obj_shape) * bfp.itemsize(self.dtype)
        return 1 if obj_bytes > bank else 2

    def bind(self, handles) -> None:
        """Bind each lane, in lane order, to the fifo end ``build()`` built for it.

        A one-lane operand may take its handle bare.

        Raises:
            ValueError: Not one handle per lane, or the operand is bound already.
        """
        handles = list(handles) if isinstance(handles, (list, tuple)) else [handles]
        if len(handles) != self.lanes:
            raise ValueError(
                f"{self.name} has {self.lanes} lanes; bind() was given "
                f"{len(handles)} handles"
            )
        if self.lane_handles:
            raise ValueError(f"{self.name} is already bound")
        self.lane_handles = handles

    def pin(self, endpoints: list[DmaEndpoint]) -> None:
        """Pin each lane, in order, to a shim ``DmaEndpoint`` built elsewhere.

        ``DmaEndpoint`` is MM2S for an input, S2MM for an output, so its
        transfers are shim DMA tasks; ``build()`` returns the endpoints
        among its objects.

        Raises:
            ValueError: An endpoint moves the other way or names no channel,
                or ``bind`` refuses the endpoints.
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
                f"{self.name} was never bound: build() must bind() every "
                f"streamed operand"
            )
        return self.lane_handles

    def fill(
        self,
        tap: TensorAccessPattern | None = None,
        *,
        lane: int | None = None,
        group: TaskGroup | None = None,
        wait: bool = False,
        source: Operand | None = None,
        offset_parameter: Value | None = None,
        length_parameter: Value | None = None,
        length_unit: int | None = None,
        repeat_parameter: Value | None = None,
        managed: bool = True,
    ):
        """Fill ``lane`` of this operand's stream from the host in ``sequence(rt)``.

        Returns the ``Task``. A per-call ``Value`` is patched into the
        descriptor on a full ELF; on an xclbin it regenerates the
        instruction stream every call.

        Args:
            tap: The walk over ``source``; all of it where None.
            lane: Required unless the operand has one lane.
            group: The ``TaskGroup`` this transfer's ``Task`` joins, or None
                for its own wait; an unmanaged transfer joins no group.
            wait: End with an await rather than a free.
            source: Another input whose data rides this operand's lane.
            offset_parameter: A per-call element offset of ``tap``.
            length_parameter: A per-call count of ``length_unit`` elements
                sizing ``tap``'s outermost dimension below the iteration, in
                whole 16-byte units; ``tap`` must fit one descriptor.
            length_unit: The element count one ``length_parameter`` unit
                counts, matching a descriptor dimension's inner product.
            repeat_parameter: A per-call count of extra runs of ``tap``, at
                most its outermost size less one.
            managed: False hands the queue slot and descriptors to the
                compiler, which frees them after a later wait; joins no group.
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
        )

    def drain(
        self,
        tap: TensorAccessPattern | None = None,
        *,
        lane: int | None = None,
        group: TaskGroup | None = None,
        wait: bool = False,
        offset_parameter: Value | None = None,
        length_parameter: Value | None = None,
        length_unit: int | None = None,
        repeat_parameter: Value | None = None,
        managed: bool = True,
    ):
        """Drain lane ``lane`` of this operand's stream to the host.

        The arguments are ``fill``'s, and a drain the sequence must see
        finish before it ends passes ``wait=True``.
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
        runtime = active_runtime.get()
        if runtime is None or runtime.op is not self.op:
            raise ValueError(
                f"{self.name}.fill/drain run in the operator's sequence(rt)"
            )
        return runtime

    @property
    def batch_axes(self) -> int:
        """1 if a leading ``T | None`` dimension is present on this instance, else 0."""
        dims = self.dims
        if (
            dims
            and isinstance(dims[0], OperatorParam)
            and dims[0].name in self.op.declaration.nullable
        ):
            return 1 if vars(self.op)[dims[0].name] is not None else 0
        return 0

    def extent_axis(self, extent: PerCallMember) -> int | None:
        """Return the axis of the resolved shape that ``extent`` bounds sizes.

        None where no axis matches, or ``extent`` bounds no parameter.
        """
        if extent.bounds is None:
            return None
        return axis_of(self.dims, extent.bounds.name, self.op)

    def fits(self, tap: TensorAccessPattern) -> bool:
        """Whether one buffer descriptor of a lane's shim tile holds ``tap``.

        ``tap`` is a pattern over this operand.
        """
        dev = self.op.dev
        assert (
            dev is not None
        ), "fits() is read during sequence derivation, with a device bound"
        # Every shim tile's descriptor is alike; column 0's stands for a lane's.
        return dev.dma_bd_fits(0, 0, tap, self.dtype)

    def split(self, elements: int) -> tuple[int, int] | None:
        """Return a contiguous run of ``elements`` of this operand as ``(d1, d0)``.

        ``d0`` is the largest a lane's shim descriptor holds as its
        innermost dimension with ``d1`` beside it, or None where no ``d0`` does.
        """
        dev = self.op.dev
        assert (
            dev is not None
        ), "split() is read during sequence derivation, with a device bound"
        for d0 in range(elements, 0, -1):
            if elements % d0:
                continue
            # The run inside a strided walk, so neither dimension is exempt
            # from its wrap as a linear transfer is.
            probe = TensorAccessPattern(
                (8 * elements,),
                0,
                [1, 2, elements // d0, d0],
                [0, 4 * elements, d0, 1],
            )
            if dev.dma_bd_fits(0, 0, probe, self.dtype):
                return elements // d0, d0
        return None

    def extent_unit(self, axis: int) -> int:
        """Return the rows along ``axis`` of one round-robin unit under a bound.

        ``Operator.extent_unit``'s, else the stream tile's.
        """
        unit = self.op.extent_unit(self.name)
        if unit is not None:
            return unit
        obj_shape = self.obj_shape if self.streamed else ()
        k = axis - (len(self.shape) - len(obj_shape))
        return obj_shape[k] if k >= 0 else 1

    @property
    def bounded(self) -> tuple[Value, int, Value] | None:
        """``(extent, axis, word)`` when a bound extent sizes an axis.

        ``word`` is the per-call tiles per lane.
        """
        op = self.op
        for name in op.bound_extents:
            extent = op.value(name)
            axis = self.extent_axis(extent)
            if axis is not None:
                return extent, axis, op.value(f"{name}_{self.name}")
        return None

    def transfers(
        self,
    ) -> list[tuple[int, TensorAccessPattern, Value | None, int | None]]:
        """Return the derived ``(lane, tap, length_parameter, length_unit)`` transfers.

        The whole buffer (one lane or replicated) or one block of the first
        non-batch axis per lane; under a bound, round-robin by tile instead.

        Raises:
            ValueError: No ``obj_shape=``, or the split does not divide, cannot
                bound that axis, or does not fit a descriptor.
        """
        name = f"{type(self.op).__name__}.{self.name}"
        if not self.streamed:
            raise ValueError(
                f"{name} has no obj_shape=, so its sequence cannot be derived; add "
                f"obj_shape= or override sequence(rt)"
            )
        count, shape = self.lanes, self.shape
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
        halves = self.split(run)
        if halves is None:
            raise ValueError(
                f"{self.name}: a {run}-element tile does not fit one descriptor"
            )
        dev = self.op.dev
        assert (
            dev is not None
        ), "transfers() is read during sequence derivation, with a device bound"
        # A unit D1 is stripped, which would drop the tile count into D1's
        # wrap; past it, a tile split in two keeps the count on D2, which has
        # none (and a half of no whole granules fits no descriptor below).
        wrap = (1 << dev.get_dma_bd_wrap_bits(0, 0)) - 1
        if halves[0] == 1 and tiles > wrap and run % 2 == 0:
            halves = (2, run // 2)
        iterations = shape[0] if axis else 1
        tiled = TensorAccessPattern.full((iterations, tiles, lanes, run))
        out = []
        for lane in range(lanes):
            tap = tiled[:, :, lane].split(2, halves[1])
            if not self.fits(tap):
                raise ValueError(
                    f"{self.name} {shape}: the round-robin split over {lanes} "
                    f"lanes does not fit one descriptor per lane"
                )
            for k in range(count) if self.replicate else [lane]:
                out.append((k, tap, word, run))
        return out

    def __getitem__(self, index) -> TensorAccessPattern:
        """Return a basic slice of this operand.

        As the pattern ``fill``/``drain`` take.
        """
        return TensorAccessPattern.full(self.shape)[index]

    def __repr__(self) -> str:
        return repr(self._decl)


def concrete(values, where) -> tuple[int, ...]:
    """Return a static pattern's sizes, strides or offset as ints.

    Args:
        values: Entries read off a ``TensorAccessPattern``, which mlir-aie
            types as possibly symbolic.
        where: What they were read from, for the error.

    Raises:
        TypeError: An entry is a symbolic value; only a per-call bound makes
            one, never a pattern an operator builds.
    """
    out = tuple(int(v) for v in values if isinstance(v, (int, np.integer)))
    if len(out) != len(values):
        raise TypeError(f"{where}: a symbolic size, stride or offset, read as static")
    return out


def axis_of(dims: tuple, name: str, op) -> int | None:
    """Return the axis of ``dims`` resolved on ``op`` that the parameter ``name`` sizes.

    Or None. A ``T | None`` dimension that is None is left out, and a
    ``Select`` is the branch its flag picks.
    """
    axis = 0
    for d in dims:
        if isinstance(d, Select):
            branch = d.branch(op)
            inner = axis_of(branch, name, op)
            if inner is not None:
                return axis + inner
            axis += len(resolve(branch, op))
            continue
        if isinstance(d, OperatorParam):
            if d.name in op.declaration.nullable and vars(op)[d.name] is None:
                continue
            if d.name == name:
                return axis
        axis += 1
    return None


def param_names(dims: tuple) -> set[str]:
    """Return the parameters ``dims`` name, through ``Select``."""
    out: set[str] = set()
    for d in dims:
        if isinstance(d, OperatorParam):
            out.add(d.name)
        elif isinstance(d, Select):
            out |= param_names((d.flag, *d.when_true, *d.when_false))
    return out
