# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An operator's operands: the host buffers it is called with, each with an
``obj_shape=`` its own stream into the array.
"""

from __future__ import annotations

import itertools
import math
from contextvars import ContextVar
from typing import TYPE_CHECKING, Any

import numpy as np
from aie.dialects.aie import DMAChannelDir, WireBundle, get_target_model
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import DmaEndpoint, ObjectFifo
from aie.iron.dataflow.objectfifo import ObjectFifoLink
from aie.iron.device import AnyMemTile
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
    """An operand as one operator holds it (``op.x``): the resolved ``In``, ``Out``
    or ``InOut``, read through on use (a shape may follow a tunable), and its
    bound ``lane_handles``. An ``InOut`` keeps what its stream does not drain.
    ``lane_fifos`` is the ``ObjectFifo`` ``fifos()`` made each lane from, kept
    past binding so a fed consumer with several readers, or ``fifos()`` asked
    for several, can add more ends to the one already bound.

    A fed input reads ``fed_from``'s lanes, or, ``staged``, the fifo a
    ``Staging`` restaged them into for each of its lanes; an output lists
    every input it ``feeds``.
    """

    def __init__(self, member: Any, op: Operator) -> None:
        self.op = op
        self.lane_handles: list[Any] = []
        self.lane_fifos: list[Any] = []
        self.fed_from: Operand | None = None
        self.staged: list[ObjectFifo] | None = None
        self.feeds: list[Operand] = []
        self.read_lanes: set[int] = set()
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
        """The runtime-sequence argument type: this buffer flattened to 1-D,
        in its own element units (blocks, for block float).
        """
        return np.ndarray[(self.elements,), np.dtype[self.dtype]]

    @property
    def obj_type(self):
        """The fifo element type: ``np.ndarray[shape, dtype]``."""
        return np.ndarray[self.obj_shape, np.dtype[self.dtype]]

    @property
    def l1_depth(self) -> int:
        """The depth a core-side fifo of this operand's tiles can have: two,
        or one when a tile spans more than a hardware bank of the bound
        device's core memory.
        """
        dev = self.op.dev
        # Half a programmer bank: at the whole one, two 16 KB streams no longer fit.
        bank = dev.core_memory_bytes // (2 * dev.core_memory_banks)
        obj_bytes = math.prod(self.obj_shape) * bfp.itemsize(self.dtype)
        return 1 if obj_bytes > bank else 2

    def bind(self, handles) -> None:
        """Bind each lane, in lane order, to the fifo end ``build()`` built for
        it; a one-lane operand may take its handle bare.

        Raises:
            ValueError: Not one handle per lane, the operand is bound already,
                or it is fed: a fed input takes its lanes from ``fifos()``.
        """
        if self.fed_from is not None:
            raise ValueError(
                f"{self.name} is fed from {self.fed_from.name}: its build must "
                f"take its lanes from fifos(), not bind()"
            )
        handles = list(handles) if isinstance(handles, (list, tuple)) else [handles]
        if len(handles) != self.lanes:
            raise ValueError(
                f"{self.name} has {self.lanes} lanes; bind() was given "
                f"{len(handles)} handles"
            )
        if self.lane_handles:
            raise ValueError(f"{self.name} is already bound")
        self.lane_handles = handles

    def fifos(
        self,
        depth: int | None = None,
        *,
        readers: int | None = None,
        tiles: list | None = None,
        obj_type: Any = None,
        **objectfifo_kwargs: Any,
    ) -> list[Any]:
        """A fifo per lane, ``depth`` deep (else ``l1_depth``), of ``obj_type``
        (else this operand's own), bound as this operand's lanes. Plain
        (``readers=None``, ``tiles=None``), returns the build's end of each:
        an input's consumer end, an output's producer end.

        ``readers`` several consumer ends a lane instead of one -- a lane
        several cores read -- each lane then its own list of them (even at
        ``readers=1``, so a caller that always indexes a lane's list need not
        special-case one reader), not a bare end; refused on an output, which
        has one producer. ``tiles`` places each lane's host end (the shim
        tile its runtime transfer binds to) and, since placement is usually
        followed by more of the fifo's own wiring (a ``split()``, ``join()``
        or ``forward()``), returns the fifo itself, one per lane, rather than
        an end. ``objectfifo_kwargs`` reach every lane's ``ObjectFifo(...)``.

        A fed input gets its source's ends or fifos the same way, each end
        from ``Operand.reader``, so the end bound for the source's drain is
        read rather than left a dangling extra consumer; ``tiles`` and
        ``obj_type`` are the source's own, already built, as is the depth of
        that first end. A ``staged`` input reads fifos built for it, each end
        ``depth`` deep (else ``l1_depth``).

        Raises:
            ValueError: ``readers`` and ``tiles`` are both given, ``readers``
                is asked of an output, or ``tiles`` does not name one tile a
                lane.
        """
        if readers is not None and tiles is not None:
            raise ValueError(f"{self.name}.fifos(): readers= and tiles= do not combine")
        source, staged = self.fed_from, self.staged
        if source is not None:
            if tiles is not None:
                return list(source.lane_fifos if staged is None else staged)
            ends = [
                (
                    [source.reader(lane, depth) for _ in range(readers or 1)]
                    if staged is None
                    else [
                        staged[lane].cons(self.l1_depth if depth is None else depth)
                        for _ in range(readers or 1)
                    ]
                )
                for lane in range(self.lanes)
            ]
            return [lane[0] for lane in ends] if readers is None else ends
        if readers is not None and self.drains:
            raise ValueError(
                f"{self.name} is an output: readers= reads a streamed input's "
                f"lane, not an output's own"
            )
        depth = self.l1_depth if depth is None else depth
        obj_type = self.obj_type if obj_type is None else obj_type
        lane_tiles = [None] * self.lanes if tiles is None else tiles
        if len(lane_tiles) != self.lanes:
            raise ValueError(
                f"{self.name} has {self.lanes} lanes; tiles has {len(lane_tiles)}"
            )
        made = [
            ObjectFifo(obj_type, depth=depth, **objectfifo_kwargs)
            for _ in range(self.lanes)
        ]
        self.lane_fifos = made
        if self.drains:
            self.bind([f.cons(tile=t) for f, t in zip(made, lane_tiles)])
            if tiles is not None:
                return made
            return [f.prod() for f in made]
        self.bind([f.prod(tile=t) for f, t in zip(made, lane_tiles)])
        if tiles is not None:
            return made
        if readers is None:
            return [f.cons() for f in made]
        return [[f.cons() for _ in range(readers)] for f in made]

    def feed(self, source: Operand, staged: bool = False) -> None:
        """Take this input's stream on-chip from ``source``, another operator's
        output: its cores read the fifos ``source``'s cores write, so neither
        is a host transfer. Several inputs may each be fed one source.

        Args:
            source: The output, its lanes bound, whose stream this input reads.
            staged: Where the lanes do not meet directly, restage them
                through memtiles (``Staging``) rather than refuse.

        Raises:
            ValueError: This is not a streamed input, ``source`` not a bound
                output, this is a held (``replicate``) input, ``source`` is
                pinned rather than streamed, or, unless ``staged`` and
                ``Staging`` takes them, their lanes or objects differ or a
                lane's host access pattern does not visit the same elements
                in the same order on both sides.
        """
        if not (self.streamed and self.fills) or not source.drains:
            raise ValueError(
                f"{self.name} can be fed only as a streamed input, from an output"
            )
        if self.replicate:
            raise ValueError(
                f"{self.name} holds one line the whole call, every core meeting "
                f"it: it cannot be fed a source's per-iteration stream"
            )
        if any(isinstance(h, DmaEndpoint) for h in source.handles):
            raise ValueError(
                f"{source.name} is pinned to shim channels, not a fifo: it "
                f"cannot feed {self.name} on-chip"
            )
        mismatch = None
        if len(source.handles) != self.lanes or source.obj_type != self.obj_type:
            mismatch = (
                f"{source.name} streams {len(source.handles)} lanes of "
                f"{source.obj_type}, but {self.name} reads {self.lanes} lanes of "
                f"{self.obj_type}"
            )
        else:
            mine = {lane: tap for lane, tap, _, _ in self.transfers()}
            theirs = {lane: tap for lane, tap, _, _ in source.transfers()}
            lane = next(
                (
                    k
                    for k in sorted(mine)
                    if not theirs[k].compare_access_orders(mine[k])
                ),
                None,
            )
            if lane is not None:
                mismatch = (
                    f"{self.name} and {source.name} disagree on lane {lane}'s "
                    f"host access order: {source.name} visits {theirs[lane]}, "
                    f"{self.name} visits {mine[lane]}"
                )
        if mismatch is not None and not staged:
            raise ValueError(mismatch)
        if mismatch is not None:
            self.staged = Staging(source, self).build()
        self.fed_from = source
        source.feeds.append(self)

    def reader(self, lane: int, depth: int | None = None) -> Any:
        """A consumer end of output lane ``lane`` for an on-chip reader: the end
        bound for its drain, which no host transfer takes once fed, then a new
        one of the lane's fifo for each reader after, ``depth`` deep (else the
        fifo's own).

        Raises:
            ValueError: The lane has a reader already and its build bound the
                lane without ``fifos()``, so it has no fifo to add one to.
        """
        if lane not in self.read_lanes:
            self.read_lanes.add(lane)
            return self.handles[lane]
        if not self.lane_fifos:
            raise ValueError(
                f"{self.name} was bound without fifos(), so its lane {lane} has "
                f"no fifo to add another reader to"
            )
        return self.lane_fifos[lane].cons(depth)

    @property
    def on_chip(self) -> bool:
        """Whether this operand's stream stays on-chip, fed to or from another
        operator, with no host transfer."""
        return self.fed_from is not None or bool(self.feeds)

    def pin(self, endpoints: list[DmaEndpoint]) -> None:
        """Pin each lane, in lane order, to a shim ``DmaEndpoint`` (MM2S for an
        input, S2MM for an output) of routes built elsewhere, so its transfers
        are shim DMA tasks; ``build()`` returns the endpoints among its objects.

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
        group=None,
        wait: bool = False,
        source: Operand | None = None,
        offset_parameter: Value | None = None,
        length_parameter: Value | None = None,
        length_unit: int | None = None,
        repeat_parameter: Value | None = None,
        managed: bool = True,
    ):
        """Fill ``lane`` of this operand's stream from the host in
        ``sequence(rt)``; returns the ``Task``, or None and emits nothing for
        an on-chip operand, fed on-chip from another operator's output. A
        per-call ``Value`` is patched into the descriptor on a full ELF; on an
        xclbin it regenerates the instruction stream every call.

        Args:
            tap: The walk over ``source``; all of it where None.
            lane: Required unless the operand has one lane.
            wait: End with an await rather than a free.
            source: Another input whose data rides this operand's lane.
            offset_parameter: A per-call element offset of ``tap``.
            length_parameter: A per-call count of ``length_unit`` elements
                sizing ``tap``'s outermost dimension below the iteration, in
                whole 16-byte units; ``tap`` must fit one descriptor.
            repeat_parameter: A per-call count of extra runs of ``tap``, at
                most its outermost size less one.
            managed: False hands the queue slot and descriptors to the
                compiler, which frees them after a later wait; joins no group.
        """
        if self.on_chip:
            return None
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
        group=None,
        wait: bool = False,
        offset_parameter: Value | None = None,
        length_parameter: Value | None = None,
        length_unit: int | None = None,
        repeat_parameter: Value | None = None,
        managed: bool = True,
    ):
        """Drain lane ``lane`` of this operand's stream to the host, or emit
        nothing and return None for an on-chip operand, fed to another
        operator's input; the arguments are ``fill``'s, and a drain the
        sequence must see finish before it ends passes ``wait=True``.
        """
        if self.on_chip:
            return None
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
        """The axis of the resolved shape the parameter ``extent`` bounds
        sizes, or None.
        """
        return axis_of(self.dims, extent.bounds.name, self.op)

    def fits(self, tap: TensorAccessPattern) -> bool:
        """Whether one buffer descriptor of a lane's shim tile holds
        ``tap``, a pattern over this operand.
        """
        # Every shim tile's descriptor is alike; column 0's stands for a lane's.
        return self.op.dev.dma_bd_fits(0, 0, tap, self.dtype)

    def split(self, elements: int) -> tuple[int, int] | None:
        """A contiguous run of ``elements`` of this operand as ``(d1, d0)``:
        the largest ``d0`` a lane's shim descriptor holds as its innermost
        dimension with ``d1`` beside it, or None where no ``d0`` does.
        """
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
            if self.op.dev.dma_bd_fits(0, 0, probe, self.dtype):
                return elements // d0, d0
        return None

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
    def bounded(self) -> tuple[Value, int, Value] | None:
        """``(extent, axis, word)`` when a bound extent sizes an axis, ``word``
        the per-call tiles per lane.
        """
        op = self.op
        for name in op.bound_extents:
            extent = op.value(name)
            axis = self.extent_axis(extent)
            if axis is None:
                continue
            word = f"{name}_{self.name}"
            if word not in {v.name for v in op.values}:
                raise ValueError(
                    f"{type(op).__name__}.{self.name}: {name} bounds it, but no "
                    f"per-call word {word!r} counts its tiles; its own "
                    f"sequence(rt) moves it"
                )
            return extent, axis, op.value(word)
        return None

    def transfers(
        self,
    ) -> list[tuple[int, TensorAccessPattern, Value | None, int | None]]:
        """The ``(lane, tap, length_parameter, length_unit)`` transfers: what
        an operator writing its own sequence describes (``lane_transfers``),
        else derived: the whole buffer (one lane or replicated) or one block
        of the first non-batch axis per lane; under a bound, round-robin by
        tile instead.

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
        described = self.op.lane_transfers(self)
        if described is not None:
            return described
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
        if tile_rows == 0:
            raise ValueError(
                f"{name}: {type(self.op).__name__}.extent_unit({axis!r}) is 0, so "
                f"this operand's sequence is not derived; it must override sequence(rt)"
            )
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
        # A unit D1 is stripped, which would drop the tile count into D1's
        # wrap; past it, a tile split in two keeps the count on D2, which has
        # none (and a half of no whole granules fits no descriptor below).
        wrap = (1 << self.op.dev.get_dma_bd_wrap_bits(0, 0)) - 1
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
        """A basic slice of this operand, as the pattern ``fill``/``drain`` take."""
        return TensorAccessPattern.full(self.shape)[index]

    def __repr__(self) -> str:
        return repr(self._decl)


class Staging:
    """``source``'s lanes restaged through memtiles into ``sink``'s, where they
    do not meet directly: each of ``sink``'s lanes joined from whole lanes of
    ``source`` (each a slot of a memtile object, filled a round at a time),
    or each lane of ``source`` split among ``sink``'s (a round per object of
    it). Derived from both operands' ``transfers()`` and checked element for
    element against them, so every lane of ``sink`` reads, round by round,
    what the host round trip gives it.

    ``joins`` holds, per lane of ``sink``, the lanes of ``source`` joined into
    it and each one's slot of a round, in elements; ``splits``, per lane of
    ``source``, the lanes of ``sink`` it is split into and each one's slot.

    A per-call bound is honored where both sides follow one graph value and
    move, a tile a lane, the same elements a call, in tiles of whole rounds:
    every call is then the same whole rounds on both sides.

    Raises:
        ValueError: The two are not one buffer, a side's lanes do not visit
            each element once or in whole objects, a bound is not honored as
            above, neither a join nor a split reproduces ``sink``'s order, or
            a memtile cannot take one: a split to more lanes than its DMA
            channels, or a round past its memory. A join of more lanes than a
            memtile takes is a join of joins.
    """

    def __init__(self, source: Operand, sink: Operand) -> None:
        self.source, self.sink = source, sink
        edge = (
            f"{type(source.op).__name__}.{source.name} -> "
            f"{type(sink.op).__name__}.{sink.name}"
        )
        if source.nbytes != sink.nbytes or source.dtype != sink.dtype:
            raise ValueError(
                f"{edge}: {source.shape} and {sink.shape} of "
                f"{bfp.dtype_name(source.dtype)} and {bfp.dtype_name(sink.dtype)} "
                f"are not one buffer"
            )
        streams: list[list[np.ndarray]] = []
        # Per side, under a bound: the graph expression its extent follows,
        # the extent every lane together moves a tile at a time and those
        # elements, and a lane's tile.
        bounds: list[tuple[Any, int, int, int] | None] = []
        for side in (source, sink):
            transfers = side.transfers()
            bounded = side.bounded
            if bounded is None:
                bounds.append(None)
            else:
                extent, axis, word = bounded
                (unit,) = {u for _, _, _, u in transfers}
                rows = word.divisor(side.op)
                bounds.append(
                    (
                        side.op.bound_values.get(extent.name),
                        rows,
                        rows * math.prod(side.shape[axis + 1 :]),
                        unit,
                    )
                )
            taps = {lane: tap for lane, tap, _, _ in transfers}
            if len(transfers) != side.lanes or sorted(taps) != list(range(side.lanes)):
                raise ValueError(f"{edge}: {side.name} has not one transfer a lane")
            obj = math.prod(side.obj_shape)
            index = np.arange(side.elements)
            stream = [taps[lane].gather(index) for lane in range(side.lanes)]
            if any(len(s) % obj for s in stream) or not np.array_equal(
                np.sort(np.concatenate(stream)), index
            ):
                raise ValueError(
                    f"{edge}: {side.name}'s lanes do not visit each element once, "
                    f"in whole {side.obj_shape} objects"
                )
            streams.append(stream)
        produced, consumed = streams
        produce, consume = math.prod(source.obj_shape), math.prod(sink.obj_shape)
        # A memtile's rounds are fixed at build: a call bounded short of a whole
        # round would stall it, so both sides must move the same whole rounds.
        if (bounds[0] is None) != (bounds[1] is None):
            raise ValueError(
                f"{edge}: one side is bounded per call and the other moves its "
                f"whole buffer"
            )
        if bounds[0] is not None:
            (graph_p, rows_p, round_p, _), (graph_c, rows_c, round_c, _) = bounds
            # A call moves ceil(extent / rows) rounds a side: one count for
            # every value where the two extents are one linear expression
            # of it, a round of each side's rows apart.
            if (
                graph_p is None
                or graph_c is None
                or graph_p.value.name != graph_c.value.name
                or not (graph_p.linear and graph_c.linear)
                or round_p != round_c
                or graph_p.scale * rows_c != graph_c.scale * rows_p
                or graph_p.bias * rows_c != graph_c.bias * rows_p
            ):
                raise ValueError(
                    f"{edge}: bounded per call by "
                    f"{None if graph_p is None else graph_p.name} in rounds of "
                    f"{round_p} elements and by "
                    f"{None if graph_c is None else graph_c.name} in rounds of "
                    f"{round_c}: not one graph value moving whole rounds alike"
                )
        units = (None, None) if bounds[0] is None else (bounds[0][3], bounds[1][3])

        tm = get_target_model(sink.op.dev.resolve())
        row = next(r for r in range(tm.rows()) if tm.is_mem_tile(0, r))
        self.fan_in = tm.get_num_dest_switchbox_connections(0, row, WireBundle.DMA)
        channels_out = tm.get_num_source_switchbox_connections(0, row, WireBundle.DMA)
        self.capacity = tm.get_mem_tile_size()
        self.item = bfp.itemsize(sink.dtype)

        self.joins: list[tuple[list[int], list[int]]] = []
        self.splits: list[tuple[list[int], list[int]]] = []
        owner = np.empty(source.elements, dtype=np.int64)
        for lane, stream in enumerate(produced):
            owner[stream] = lane
        groups = [
            [int(k) for k in lanes[np.argsort(first)]]
            for lanes, first in (
                np.unique(owner[stream], return_index=True) for stream in consumed
            )
        ]
        if sorted(k for group in groups for k in group) == list(range(source.lanes)):
            for group, stream in zip(groups, consumed):
                rounds = math.gcd(
                    *(len(produced[k]) // produce for k in group),
                    len(stream) // consume,
                )
                # The most rounds, so the smallest memtile object, whose slots
                # are whole 32-bit words.
                for k in range(rounds, 0, -1):
                    slots = [len(produced[j]) // k for j in group]
                    if rounds % k or any(s * self.item % 4 for s in slots):
                        continue
                    joined = np.concatenate(
                        [produced[j].reshape(k, -1) for j in group], axis=1
                    )
                    if np.array_equal(joined.reshape(-1), stream):
                        break
                else:
                    raise ValueError(
                        f"{edge}: joining lanes {group} of {source.name}, at any "
                        f"round, does not give a lane of {sink.name} its host order"
                    )
                if sum(slots) * self.item > self.capacity:
                    raise ValueError(
                        f"{edge}: a round of {sum(slots)} elements is past a "
                        f"memtile's {self.capacity} bytes"
                    )
                tile_p, tile_c = units
                if tile_p is not None and any(
                    tile_p % s or tile_p // s * sum(slots) != tile_c for s in slots
                ):
                    raise ValueError(
                        f"{edge}: a call's bound moves {tile_p}-element tiles of "
                        f"{source.name} and {tile_c} of {sink.name}, not whole "
                        f"rounds of slots {slots}"
                    )
                self.joins.append((group, slots))
            return
        reader = np.empty(sink.elements, dtype=np.int64)
        for lane, stream in enumerate(consumed):
            reader[stream] = lane
        for stream in produced:
            lanes, first = np.unique(reader[stream], return_index=True)
            group = [int(k) for k in lanes[np.argsort(first)]]
            rounds = len(stream) // produce
            slots = [len(consumed[j]) // rounds for j in group]
            if any(len(consumed[j]) % rounds for j in group) or any(
                s % consume or s * self.item % 4 for s in slots
            ):
                split = None
            else:
                split = np.concatenate(
                    [consumed[j].reshape(rounds, -1) for j in group], axis=1
                )
            if split is None or not np.array_equal(split.reshape(-1), stream):
                raise ValueError(
                    f"{edge}: neither a join of whole lanes of {source.name} nor "
                    f"a split of each of its objects gives {sink.name}'s lanes "
                    f"their host order"
                )
            tile_p, tile_c = units
            if tile_p is not None and any(
                tile_p // produce * s != tile_c for s in slots
            ):
                raise ValueError(
                    f"{edge}: a call's bound moves {tile_p}-element tiles of "
                    f"{source.name} and {tile_c} of {sink.name}, not whole rounds "
                    f"of its {produce}-element objects"
                )
            if len(group) > channels_out:
                raise ValueError(
                    f"{edge}: a lane of {source.name} splits into {len(group)} "
                    f"lanes of {sink.name} in one memtile, which sends {channels_out}"
                )
            self.splits.append((group, slots))
        if sorted(k for group, _ in self.splits for k in group) != list(
            range(sink.lanes)
        ):
            raise ValueError(
                f"{edge}: a lane of {sink.name} takes parts of two lanes of "
                f"{source.name}, which no one join or split gives"
            )

    def build(self) -> list[ObjectFifo]:
        """Wire the plan at memtiles over ends of ``source``'s lanes
        (``Operand.reader``); returns, per lane of ``sink``, the fifo it reads,
        of ``sink``'s ``obj_type`` at its consumers.
        """
        source, sink = self.source, self.sink
        fifos: list[Any] = [None] * sink.lanes
        for lane, (group, slots) in enumerate(self.joins):
            ends = [source.reader(k) for k in group]
            # More lanes than a memtile takes join in parts first, each part
            # one link's output and the next's input, on another memtile.
            while len(ends) > self.fan_in:
                parts = math.ceil(len(ends) / math.ceil(len(ends) / self.fan_in))
                joined, sizes = [], []
                for at in range(0, len(ends), parts):
                    part = slots[at : at + parts]
                    fifo = self.joined(ends[at : at + parts], part, None)
                    joined.append(fifo.cons())
                    sizes.append(sum(part))
                ends, slots = joined, sizes
            fifos[lane] = self.joined(ends, slots, sink.obj_type)
        for lane, (group, slots) in enumerate(self.splits):
            outs = source.reader(lane).split(
                list(itertools.accumulate(slots[:-1], initial=0)),
                obj_types=[sink.obj_type] * len(group),
            )
            for k, out in zip(group, outs):
                fifos[k] = out
        return fifos

    def joined(self, ends: list, slots: list[int], read_as: Any) -> ObjectFifo:
        """A memtile fifo whose objects join ``ends``' objects, each its slot
        (``slots``, in elements); its consumers read objects of ``read_as``
        where given.
        """
        obj = np.ndarray[(sum(slots),), np.dtype[self.sink.dtype]]
        fifo = ObjectFifo(
            obj,
            depth=2 if 2 * sum(slots) * self.item <= self.capacity else 1,
            consumer_obj_type=None if read_as in (None, obj) else read_as,
        )
        # One source is a forward, which takes no offsets.
        offsets = list(itertools.accumulate(slots[:-1], initial=0))
        ObjectFifoLink(
            ends, fifo.prod(), AnyMemTile, offsets if len(ends) > 1 else [], []
        )
        return fifo


def axis_of(dims: tuple, name: str, op) -> int | None:
    """The axis of ``dims`` resolved on ``op`` that the parameter ``name``
    sizes, or None. A ``T | None`` dimension that is None is left out, and a
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
    """The parameters ``dims`` name, through ``Select``."""
    out: set[str] = set()
    for d in dims:
        if isinstance(d, OperatorParam):
            out.add(d.name)
        elif isinstance(d, Select):
            out |= param_names((d.flag, *d.when_true, *d.when_false))
    return out
