# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An operator's operands: the host buffers it is called with.

Each with an ``obj_shape=`` is its own stream into the array.
"""

from __future__ import annotations

import dataclasses
import itertools
import math
from collections.abc import Sequence
from contextvars import ContextVar
from typing import TYPE_CHECKING, Any

import numpy as np
from aie.dialects.aie import DMAChannelDir, WireBundle, get_target_model
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import DmaEndpoint, ObjectFifo, Packet, Port, TaskGroup, Transport
from aie.iron.dataflow.objectfifo import ObjectFifoLink
from aie.iron.device import AnyMemTile
from aie.utils import bfp, coded
from aie.utils.compile.jit.operator import Unresolvable
from aie.utils.compile.jit.params import OperatorParam, PerCallMember, Select, resolve
from ml_dtypes import bfloat16

from .value import ExtentWord, Value

if TYPE_CHECKING:
    from ..design import OperatorRuntime
    from .operator import Operator

# The OperatorRuntime whose sequence body is running, which fill/drain emit through.
active_runtime: ContextVar[OperatorRuntime | None] = ContextVar(
    "active_runtime", default=None
)


@dataclasses.dataclass
class Join:
    """How each lane of an output is joined in a memtile from per-core fifos, which the build's cores write.

    Attributes:
        offsets: Each core's offset in a lane's object, in elements.
        obj_types: Each core's object type.
        depths: Each core fifo's depth.
        tiles: Each lane's memtile.
    """

    offsets: list[int]
    obj_types: list[Any]
    depths: list[int]
    tiles: list[Any]


class Operand:
    """An operand as one operator holds it (``op.x``).

    The resolved ``In``, ``Out`` or ``InOut``, read through on use (a shape may follow a
    tunable), and its bound ``lane_handles``. An ``InOut`` keeps what its stream does
    not drain. ``lane_fifos`` holds the fifos ``fifos()`` made for each lane, kept past
    binding so another reader can add more ends to one already bound.

    A fed input reads ``fed_from``'s lanes (or one fifo's, a lane source), or ``staged`` fifos where ``Staging``
    restaged them; an output lists every input it ``feeds``, and one that
    ``keeps_host`` drains to the host too, its inputs reading ends of their own.
    Where a composition chose an edge's depth, which names the edge's reading
    end, ``chosen_depth`` holds it: on a fed input, the depth of the end it
    reads through; on an output, that of the end its lanes bind for their
    first on-chip reader (spliced, each core's fifo); on an input the
    cascade fills, its fifos' own.
    An output and the input it carries to over the cascade each hold the
    other as ``cascade`` (``cascade_to``). An output whose lanes are each
    joined in a memtile from its cores' fifos holds the ``join``, and each
    lane's ``core_fifos``, those its build's cores write. Where a
    composition ``splices`` a stage into it, those are fifos of the cores'
    own, and the stage's outputs write the join (``join_from``), each
    holding the output ``into`` which it writes; the stage's host operands
    move ``along`` that output's lanes, in its host order.
    """

    def __init__(self, member: Any, op: Operator) -> None:
        self.op = op
        self.lane_handles: list[Any] = []
        self.lane_fifos: list[Any] = []
        self.fed_from: Operand | ObjectFifo | None = None
        self.staged: list[ObjectFifo] | None = None
        self.feeds: list[Operand] = []
        self.keeps_host = False
        # Its host transfers ride packet flows, sharing the shim's channels.
        self.packeted = False
        self.chosen_depth: int | None = None
        self.cascade: Operand | None = None
        self.join: Join | None = None
        self.core_fifos: list[list[ObjectFifo]] = []
        self.splices = False
        self.along: Operand | None = None
        self.into: Operand | None = None
        self.read_lanes: set[int] = set()
        self._decl = member.of(op)

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):  # unset while a copy is made
            raise AttributeError(name)
        prop = vars(Operand).get(name)
        if isinstance(prop, property):
            # One of this class's properties raised: raise its error again,
            # not the declaration's lacking the name.
            return prop.__get__(self)
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

    def device_form(self, value: np.ndarray) -> np.ndarray:
        """``value``, this operand's logical tensor, as its host buffer holds it.

        A coded operand's rows encoded, any other as it is.

        Raises:
            ValueError: A row holds more exceptions than the capacity.
        """
        if not self.coded:
            return value
        return coded.encode_rows(np.asarray(value, bfloat16), self.capacity)

    def logical_form(self, data: np.ndarray) -> np.ndarray:
        """Return ``data``, this operand's host buffer, as the logical tensor a reference reads.

        A coded operand's rows decoded, any other as it is.
        """
        if not self.coded:
            return data
        rows = np.asarray(data).reshape(self.shape)
        return coded.decode_rows(rows, self.logical_shape[-1])

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
            ValueError: Not one handle per lane, the operand is bound already,
                or it is fed: a fed input takes its lanes from ``fifos()``.
        """
        if self.fed_from is not None:
            raise ValueError(
                f"{self.name} is fed on-chip: its build must "
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
        join: Join | None = None,
        **objectfifo_kwargs: Any,
    ) -> list[Any]:
        """Return a fifo per lane, bound as this operand's lanes.

        Plain (``readers=None``, ``tiles=None``), returns the build's end of each: an
        input's consumer end, an output's producer end. A fed input gets its source's
        ends or fifos the same way, through ``Operand.reader``; a ``staged`` input
        reads fifos built for it. An output given a ``join`` returns, for each lane,
        the fifos its cores write (``core_fifos``), which the lane joins in a memtile.

        Args:
            depth: Fifo depth; ``l1_depth`` when None.
            readers: Several consumer ends a lane instead of one, each lane
                then its own list of them; refused on an output, which has
                one producer.
            tiles: Places each lane's host end and returns the fifo itself,
                one per lane, rather than an end.
            obj_type: The fifo element type; this operand's own when None.
            join: Joins each lane of an output in a memtile from its cores'
                fifos.
            objectfifo_kwargs: Reach every lane's ``ObjectFifo(...)``.

        Raises:
            ValueError: ``readers`` and ``tiles`` are both given, ``readers``
                is asked of an output, ``tiles`` does not name one tile a
                lane, or ``join`` is asked of an input.
        """
        if readers is not None and tiles is not None:
            raise ValueError(f"{self.name}.fifos(): readers= and tiles= do not combine")
        if join is not None and not self.drains:
            raise ValueError(f"{self.name} is an input: join= joins an output's lanes")
        source, staged = self.fed_from, self.staged
        if isinstance(source, ObjectFifo):
            # The composition made the fifo, and its depth with it.
            reading = source.depth
            if tiles is not None:
                return [source]
            if readers is None:
                return [source.cons(reading)]
            return [[source.cons(reading) for _ in range(readers)]]
        if source is not None:
            if tiles is not None:
                return list(source.lane_fifos if staged is None else staged)
            exact = self.chosen_depth is not None
            reading = self.chosen_depth if exact else depth
            ends = [
                (
                    [
                        source.reader(lane, reading, exact=exact)
                        for _ in range(readers or 1)
                    ]
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
        if self.chosen_depth is not None and self.fills:
            depth = self.chosen_depth
        depth = self.l1_depth if depth is None else depth
        obj_type = self.obj_type if obj_type is None else obj_type
        lane_tiles = [None] * self.lanes if tiles is None else tiles
        if len(lane_tiles) != self.lanes:
            raise ValueError(
                f"{self.name} has {self.lanes} lanes; tiles has {len(lane_tiles)}"
            )
        # Packet flows share a shim's sending channel only where they pin it.
        port = Port.dma(0) if self.packeted else None
        if self.packeted:
            objectfifo_kwargs.setdefault("transport", Transport.dma(packet=Packet()))
        made = [
            ObjectFifo(obj_type, depth=depth, **objectfifo_kwargs)
            for _ in range(self.lanes)
        ]
        self.lane_fifos = made
        if self.drains:
            spliced = self.splices and join is not None
            # Spliced, the first on-chip reader is each core's stage.
            reading = None if spliced else self.chosen_depth
            self.bind([f.cons(reading, tile=t) for f, t in zip(made, lane_tiles)])
            if join is not None:
                self.join = join
                self.core_fifos = [
                    (
                        [
                            ObjectFifo(t, depth=max(d, self.chosen_depth or 0))
                            for t, d in zip(join.obj_types, join.depths)
                        ]
                        if spliced
                        else f.prod().join(
                            join.offsets,
                            tile=join.tiles[lane],
                            depths=join.depths,
                            obj_types=join.obj_types,
                        )
                    )
                    for lane, f in enumerate(made)
                ]
                return self.core_fifos
            if tiles is not None:
                return made
            return [f.prod() for f in made]
        self.bind([f.prod(tile=t, port=port) for f, t in zip(made, lane_tiles)])
        if tiles is not None:
            return made
        if readers is None:
            return [f.cons() for f in made]
        return [[f.cons() for _ in range(readers)] for f in made]

    def join_from(self, lane: int, stages: Sequence[Operand]) -> None:
        """Join lane ``lane`` in its memtile from ``stages``, one output a core, at the ``join``'s offsets.

        Each of ``stages`` is a one-lane output on chip, writing the core's
        place in the join (its ``into``).

        Raises:
            ValueError: This output splices no stage into a join, or
                ``stages`` are not one a core of the join's object types.
        """
        join = self.join
        if not self.splices or join is None:
            raise ValueError(f"{self.name} splices no stage into a join of its lanes")
        types = [s.obj_type for s in stages]
        if types != join.obj_types or any(s.lanes != 1 for s in stages):
            raise ValueError(
                f"{self.name}'s lane {lane} joins one lane of {join.obj_types}, one "
                f"a core; the stages write {types}"
            )
        for s in stages:
            s.into = self
        tile = join.tiles[lane]
        if tile is AnyMemTile:
            tile = tile.copy()
        ObjectFifoLink(
            [s.reader(0) for s in stages],
            self.lane_fifos[lane].prod(),
            tile,
            join.offsets,
            [],
        )

    def feed(self, source: Operand | ObjectFifo, staged: bool = False) -> None:
        """Take this input's stream on-chip from ``source``, another operator's output or one fifo (a lane source).

        Neither is a host transfer; several inputs may each be fed one source.
        A lane source feeds a one-lane input its objects as they come: whose
        elements they are is the composition's, which made the fifo.

        Args:
            source: The output, its lanes bound, whose stream this input
                reads, or a fifo whose consumer end it reads.
            staged: Where the lanes do not meet directly, restage them
                through memtiles (``Staging``) rather than refuse.

        Raises:
            ValueError: This is not a streamed input, ``source`` not a bound
                output, this is a held (``replicate``) input, ``source`` is
                pinned rather than streamed, a lane source feeds more than
                one lane or objects of another type, or, unless ``staged``
                and ``Staging`` takes them, their lanes or objects differ or
                a lane's host access pattern does not visit the same
                elements in the same order on both sides.
        """
        drains = source.drains if isinstance(source, Operand) else True
        if not (self.streamed and self.fills) or not drains:
            raise ValueError(
                f"{self.name} can be fed only as a streamed input, from an output"
            )
        if self.replicate:
            raise ValueError(
                f"{self.name} holds one line the whole call, every core meeting "
                f"it: it cannot be fed a source's per-iteration stream"
            )
        if isinstance(source, ObjectFifo):
            if self.lanes != 1 or source.obj_type != self.obj_type:
                raise ValueError(
                    f"{self.name} reads {self.lanes} lanes of {self.obj_type}; a "
                    f"lane source feeds one lane of {source.obj_type}"
                )
            self.fed_from = source
            return
        if any(isinstance(h, DmaEndpoint) for h in source.handles):
            raise ValueError(
                f"{source.name} is pinned to shim channels, not a fifo: it "
                f"cannot feed {self.name} on-chip"
            )
        mismatch = self._mismatch(source)
        if mismatch is not None and not staged:
            raise ValueError(mismatch)
        if source.keeps_host:
            # The host's drain keeps each lane's bound end.
            source.read_lanes.update(range(source.lanes))
        if mismatch is not None:
            self.staged = Staging(source, self).build()
        self.fed_from = source
        source.feeds.append(self)

    def _mismatch(self, source: Operand) -> str | None:
        """Return how ``source``'s lanes fail to meet this input's as they are, or None where each lane carries the same objects in the same order."""
        if len(source.handles) != self.lanes or source.obj_type != self.obj_type:
            return (
                f"{source.name} streams {len(source.handles)} lanes of "
                f"{source.obj_type}, but {self.name} reads {self.lanes} lanes of "
                f"{self.obj_type}"
            )
        mine = {lane: tap for lane, tap, _, _ in self.transfers()}
        theirs = {lane: tap for lane, tap, _, _ in source.transfers()}
        lane = next(
            (k for k in sorted(mine) if not theirs[k].compare_access_orders(mine[k])),
            None,
        )
        if lane is None:
            return None
        return (
            f"{self.name} and {source.name} disagree on lane {lane}'s host access "
            f"order: {source.name} visits {theirs[lane]}, {self.name} visits "
            f"{mine[lane]}"
        )

    def cascade_to(self, sink: Operand) -> list[tuple[Any, Any]]:
        """Carry this output's stream to ``sink``, another operator's input, over the cascade.

        Neither is a host transfer, unless this output ``keeps_host``. Both
        are built, each lane on fifos of its own: a relay on the producer's
        core reads this output's lane and puts it on the cascade, and one on
        the consumer's core gets it and writes ``sink``'s.

        Returns:
            Each lane's two ends the relays take: a reading end of this
            output and ``sink``'s writing end.

        Raises:
            ValueError: This is not a bound output or ``sink`` a bound,
                streamed input of its own, either is pinned to shim
                channels, or their lanes do not carry the same objects in the
                same order.
        """
        if (
            not self.drains
            or not (sink.streamed and sink.fills)
            or sink.fed_from is not None
            or any(isinstance(h, DmaEndpoint) for h in self.handles + sink.handles)
        ):
            raise ValueError(
                f"{self.name} can carry over the cascade only from an output to "
                f"a streamed input of its own, each on fifos rather than pinned "
                f"to shim channels"
            )
        mismatch = sink._mismatch(self)
        if mismatch is not None:
            raise ValueError(mismatch)
        if self.keeps_host:
            # The host's drain keeps each lane's bound end.
            self.read_lanes.update(range(self.lanes))
        ends = [(self.reader(lane), sink.handles[lane]) for lane in range(sink.lanes)]
        self.cascade, sink.cascade = sink, self
        return ends

    def moved_per_lane(self) -> dict[int, int]:
        """Return the elements each lane moves in a call, by lane.

        Raises:
            ValueError: A transfer's count is staged, known only to the sequence.
        """
        moved: dict[int, int] = {}
        for lane, tap, _, _ in self.transfers():
            n = tap.numel
            if not isinstance(n, int | np.integer):
                raise ValueError(
                    f"{self.name}'s lane {lane} moves a count only the sequence knows"
                )
            moved[lane] = moved.get(lane, 0) + int(n)
        return moved

    def reader(self, lane: int, depth: int | None = None, exact: bool = False) -> Any:
        """Return a consumer end of output lane ``lane`` for an on-chip reader.

        The first call returns the end bound for the lane's drain; later calls return
        a new end of the lane's fifo, ``depth`` deep (else the fifo's own), and never
        shallower than the objects the lane moves in a call. A later reader can wait
        on what an earlier one computes from the same stream (a residual add read by a
        norm and, past the projections, by the next add), and a broadcast advances at
        its slowest reader: with fewer buffers the writer stalls before the earlier
        reader has its input, and the array deadlocks. ``exact`` takes ``depth`` as
        it is: a composition's chosen depth, which the dataflow analysis has held
        free of that deadlock.

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
        fifo = self.lane_fifos[lane]
        moved = self.moved_per_lane().get(lane, 0)
        whole = -(-moved // math.prod(self.obj_shape))
        if exact:
            return fifo.cons(depth)
        own = fifo.depth if depth is None else depth
        return fifo.cons(max(whole, own or 1))

    @property
    def on_chip(self) -> bool:
        """Whether this operand's stream stays on-chip, fed to or from another operator, on the cascade or spliced into a stage, with no host transfer."""
        if self.fills and self.cascade is not None:
            return True
        if (self.splices and self.join is not None) or self.into is not None:
            return True
        return self.fed_from is not None or (
            (bool(self.feeds) or self.cascade is not None) and not self.keeps_host
        )

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

        Returns the ``Task``, or None for an on-chip operand fed from another
        operator's output. A per-call ``Value`` is patched into the descriptor on a
        full ELF; on an xclbin it regenerates the instruction stream every call.

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
        group: TaskGroup | None = None,
        wait: bool = False,
        offset_parameter: Value | None = None,
        length_parameter: Value | None = None,
        length_unit: int | None = None,
        repeat_parameter: Value | None = None,
        managed: bool = True,
    ):
        """Drain lane ``lane`` of this operand's stream to the host.

        Emits nothing and returns None for an on-chip operand, fed to another
        operator's input. The arguments are ``fill``'s, and a drain the sequence
        must see finish before it ends passes ``wait=True``.
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
        """Return the ``(lane, tap, length_parameter, length_unit)`` transfers.

        Moving ``along`` another output's lanes, that output's. Else what an operator
        writing its own sequence describes (``lane_transfers``), else derived: the
        whole buffer (one lane or replicated) or one block of the first non-batch axis
        per lane; under a bound, round-robin by tile instead.

        Raises:
            ValueError: ``along`` moves another count of elements, no ``obj_shape=``, or the split does not divide, cannot
                bound that axis, or does not fit a descriptor.
        """
        name = f"{type(self.op).__name__}.{self.name}"
        along = self.along
        if along is not None:
            if along.elements != self.elements:
                raise ValueError(
                    f"{name} moves along {along.name}'s lanes, whose {along.elements} "
                    f"elements are not its {self.elements}"
                )
            return [
                (
                    lane,
                    TensorAccessPattern(
                        tuple(self.shape), tap.offset, tap.sizes, tap.strides
                    ),
                    word,
                    unit,
                )
                for lane, tap, word, unit in along.transfers()
            ]
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


class Staging:
    """``source``'s lanes restaged through memtiles into ``sink``'s, where they do not meet directly.

    Each of ``sink``'s lanes joined from whole lanes of ``source``, or each lane of
    ``source`` split among ``sink``'s. Derived from both operands' ``transfers()`` and
    checked element for element against them, so every lane of ``sink`` reads, round by
    round, what the host round trip gives it. A per-call bound is honored only where
    both sides move the same whole rounds every call.

    ``joins`` holds, per lane of ``sink``, the lanes of ``source`` joined into
    it and each one's slot of a round, in elements; ``splits``, per lane of
    ``source``, the lanes of ``sink`` it is split into and each one's slot.

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
        # Per side, under a bound: the graph expression, rows per tile,
        # elements per tile, and length unit.
        bounds: list[tuple[Any, int, int, int | None] | None] = []
        for side in (source, sink):
            transfers = side.transfers()
            bounded = side.bounded
            if bounded is None and any(w is not None for _, _, w, _ in transfers):
                # A per-call length with no declared bound: no round count to compare.
                raise ValueError(
                    f"{edge}: {side.name}'s lanes move a per-call length, but "
                    f"no bound of its operator names it"
                )
            if bounded is None:
                bounds.append(None)
            else:
                extent, axis, word = bounded
                assert isinstance(word, ExtentWord), "a bound's per-call word"
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
        # A memtile's rounds are fixed at build: a short round would stall it,
        # so both sides must move whole rounds.
        if (bounds[0] is None) != (bounds[1] is None):
            raise ValueError(
                f"{edge}: one side is bounded per call and the other moves its "
                f"whole buffer"
            )
        produced_bound, consumed_bound = bounds
        if produced_bound is not None:
            assert consumed_bound is not None, "both sides bounded, checked above"
            graph_p, rows_p, round_p, _ = produced_bound
            graph_c, rows_c, round_c, _ = consumed_bound
            # One round count works for every value only where both extents
            # are one linear expression of it, a round apart.
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
        units = (
            (None, None)
            if bounds[0] is None or bounds[1] is None
            else (bounds[0][3], bounds[1][3])
        )

        dev = sink.op.dev
        if dev is None:
            raise Unresolvable("Staging needs a bound device")
        tm = get_target_model(dev.resolve())
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
                # must still be whole 32-bit words.
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
        """Wire the plan at memtiles over ends of ``source``'s lanes (``Operand.reader``).

        Returns:
            Per lane of ``sink``, the fifo it reads, of ``sink``'s ``obj_type`` at
            its consumers.
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
        """Return a memtile fifo whose objects join ``ends``' objects.

        Args:
            ends: The producer ends joined into one fifo's objects.
            slots: Each end's slot of the joined object, in elements.
            read_as: The type its consumers read objects as, where given.
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
            if branch is None:
                raise TypeError(
                    "a Select() with a None branch picks no stream, not a dimension"
                )
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
