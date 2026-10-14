# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The runtime sequence of one operator, as aie.iron's ``Runtime``."""

from __future__ import annotations

from math import prod
from typing import Any, NamedTuple

import numpy as np
from aie.dialects.aie import DMAChannelDir, shim_dma_allocation
from aie.extras.dialects import arith
from aie.helpers.taplib import TensorAccessPattern
from aie.ir import IntegerType
from aie.iron import (
    Buffer,
    Flow,
    Lock,
    PacketFlow,
    Runtime,
    TaskGroup,
    TileDma,
    Worker,
    WorkerRuntimeBarrier,
    sync_parameters,
)
from aie.iron.device import Tile

from ..declare import DispatchTime, Operator, Value
from ..declare.operand import BufferView, Lane, Operand
from ..declare.value import PlaceWord
from .bd import BdLimits


class ShimChannel(NamedTuple):
    """A shim DMA channel the runtime sequence reaches by ``symbol``.

    aie.iron allocates the shim end of a route it fills or drains, one end
    per route; an ``array()`` whose route joins two shims names the other
    end with one of these.
    """

    symbol: str
    tile: Tile
    direction: DMAChannelDir
    channel: int


class OperatorRuntime(Runtime):
    """The runtime sequence of one operator: aie.iron's ``Runtime``, whose
    body runs the preamble and then the operator's ``sequence(rt)``, or the
    sequence derived from its declaration.

    It is what ``sequence(rt)`` receives: ``fill``/``drain`` take an
    operand's lane (or a one-lane operand) and a buffer, a slice of one or
    ``(buffer, TensorAccessPattern)``.

    Args:
        op: The resolved operator, its array built and its operands' lanes
            bound (a shipped image's has no array).
        built: What its ``array()`` returned: its workers and barriers, and
            the flows, locks, tile DMAs and shim channels only the sequence
            reaches.

    Attributes:
        barriers: The barriers the preamble opens.
        channels: The shim channels the sequence names beside the routes
            aie.iron allocates.
        buffers: Buffers the sequence writes that no worker places: a
            shipped image's parameter block.
    """

    def __init__(self, op: Operator, built: list = ()) -> None:
        self.op = op
        self.barriers = tuple(b for b in built if isinstance(b, WorkerRuntimeBarrier))
        self.channels = [c for c in built if isinstance(c, ShimChannel)]
        self.buffers: list[Buffer] = []
        self._tensors: dict[str, Any] = {}
        # Raises if any stream of a built array is unbound.
        handles = (
            [h for b in op.buffers if b.streamed for h in b.handles]
            if op.external is None
            else []
        )
        super().__init__(
            self.body,
            [
                *(b.flat_type for b in op.buffers),
                handles,
                *(v.param for v in op.values),
            ],
        )
        # Before resolving: the sequence body, generated last, may address any of it.
        for obj in built:
            if isinstance(obj, (Flow, PacketFlow)):
                self.add_flow(obj)
            elif isinstance(obj, Lock):
                self.add_lock(obj)
            elif isinstance(obj, TileDma):
                self.add_tile_dma(obj)
            elif not isinstance(obj, (Worker, WorkerRuntimeBarrier, ShimChannel)):
                raise TypeError(
                    f"{type(op).__name__}.array() returns Workers, "
                    f"WorkerRuntimeBarriers, Flows, PacketFlows, Locks, TileDmas "
                    f"and ShimChannels; got {obj!r}"
                )

    def body(self, *args) -> None:
        """The sequence body aie.iron runs: the operator's runtime tensors,
        its lanes' handles, then each per-call value, a dispatch-time scalar
        where it is not a scratchpad word.
        """
        buffers = self.op.buffers
        self._tensors = {b.name: a for b, a in zip(buffers, args)}
        for value, arg in zip(self.op.values, args[len(buffers) + 1 :]):
            if not value.scratchpad:
                value.ssa = arg
        if not self.op.own_preamble:
            self.preamble()
        self.run()

    def resolve(self, loc=None, ip=None, *, device=None, **options) -> None:
        # aie.iron names a shim channel through the route it starts or ends,
        # and places a buffer through the worker that reads it; these have
        # neither, so they are declared at device scope ahead of the sequence.
        for symbol, tile, direction, channel in self.channels:
            device.resolve_tile(tile)
            shim_dma_allocation(symbol, tile.op, direction, channel)
        for buffer in self.buffers:
            device.resolve_tile(buffer.tile)
            buffer.resolve()
        super().resolve(loc, ip, device=device, **options)

    def run(self) -> None:
        if self.op.has_sequence_override():
            self.op.sequence(self)
            return
        tg = TaskGroup()
        riders = {b.name for b in self.op.prepare_inputs} | {
            b.name for b in self.op.finish_inputs if not b.streamed
        }
        for buf in self.op.inputs:
            if buf.name in riders:
                continue  # filled into the stream it prepares or rides (fill)
            for slot, tap, size_by in buf.transfers():
                self.fill(slot, (buf, tap), group=tg, size_by=size_by)
        for buf in self.op.outputs:
            for slot, tap, size_by in buf.transfers():
                self.drain(slot, (buf, tap), group=tg, wait=True, size_by=size_by)
        tg.finish()

    def fill(
        self,
        stream,
        source,
        *,
        group=None,
        wait=False,
        offset_by=None,
        size_by=None,
        managed=True,
        finishing=None,
        repeat_by=None,
    ):
        """Fill ``stream`` from ``source``; a prepared input's lane is then
        filled with each of the operator's ``prepare_inputs``, which its
        cores acquire with the tile. A fill of a fed input's lane from that
        input takes its whole share, an output tile's worth at a time, each
        followed by that output tile of each finish input riding it,
        re-read to fill a tile.

        Args:
            offset_by: A per-call value moving the base address.
            size_by: ``{dim: value}``, a per-call size of one descriptor
                dimension (0 the outermost).
            repeat_by: A per-call value, the task's repeat count: the
                pattern runs it plus one times, at most the pattern's
                outermost size, its iteration stopping early. A full ELF
                writes it to the queue push from the scratchpad.
            managed: False hands the queue slot and descriptors to the
                compiler, which frees them after a later wait; joins no group.
            finishing: For a fill of a fed input, the part of the lane's
                share of the output it computes (a pattern over the
                output), where it is not the whole: a hand-written
                sequence filling a lane in pieces.

        Raises:
            ValueError: A fed input's lane is filled with a per-call offset
                or size, or with other than its share and no ``finishing``.
        """
        lane = self._lane(stream)
        riding = [e for e in self.op.finish_inputs if not e.streamed]
        buffer, tap, sliced_by = self._resolve(source, stream)
        if lane.buffer.feed and riding and buffer.name == lane.buffer.name:
            name = f"{type(self.op).__name__}.{buffer.name}"
            if offset_by or size_by or sliced_by or repeat_by:
                raise ValueError(
                    f"{name}: the finish's inputs ride it an output tile at a "
                    f"time, so it moves by no per-call offset or size"
                )
            if finishing is None and tap != buffer.transfers()[lane.index][1]:
                raise ValueError(
                    f"{name}: the finish's inputs ride it an output tile at a "
                    f"time, so a fill of lane {lane.index} is its whole share"
                )
            (out,) = self.op.outputs
            line = prod(out.tile_shape)
            share = finishing or out.transfers()[lane.index][1]
            tiles = prod(share.sizes) // line
            reads = prod(buffer.tile_shape) // line
            task = None
            for held, finished in zip(
                self._chunks(tap, tiles), self._chunks(share, tiles)
            ):
                task = self._transfer(
                    "fill", lane, (buffer, held), group, wait, None, None, managed
                )
                for e in riding:
                    self._transfer(
                        "fill",
                        lane,
                        (e, finished.repeat(reads)),
                        group,
                        wait,
                        None,
                        None,
                        managed,
                    )
            return task
        task = self._transfer(
            "fill", stream, source, group, wait, offset_by, size_by, managed, repeat_by
        )
        if not lane.buffer.prepare:
            return task
        for extra in self.op.prepare_inputs:
            self._transfer(
                "fill", stream, (extra, extra.tap), group, wait, None, None, managed
            )
        return task

    @staticmethod
    def _chunks(tap: TensorAccessPattern, n: int) -> list[TensorAccessPattern]:
        """``tap`` as ``n`` consecutive walks of equal length, in order.

        Raises:
            ValueError: No dimension of ``tap`` splits into them.
        """
        tap = tap.coalesce()
        size = prod(tap.sizes) // n
        for d in reversed(range(tap.rank) if size * n == prod(tap.sizes) else ()):
            inner = prod(tap.sizes[d + 1 :])
            if size % inner == 0 and tap.sizes[d] % (size // inner) == 0:
                split = tap.split(d, size // inner)
                return [
                    split[
                        tuple(int(i) for i in np.unravel_index(k, split.sizes[: d + 1]))
                    ]
                    for k in range(n)
                ]
        raise ValueError(f"{tap} does not split into {n} walks of {size} elements")

    def drain(
        self,
        stream,
        dest,
        *,
        group=None,
        wait=True,
        offset_by=None,
        size_by=None,
        managed=True,
        repeat_by=None,
    ):
        """Drain ``stream`` into ``dest``; see ``fill`` for the other forms."""
        return self._transfer(
            "drain", stream, dest, group, wait, offset_by, size_by, managed, repeat_by
        )

    def _transfer(
        self,
        verb: str,
        stream,
        what,
        group,
        wait: bool,
        offset_by=None,
        size_by=None,
        managed=True,
        repeat_by=None,
    ):
        fn = getattr(self._lane(stream).handle, verb)
        buffer, tap, sliced_by = self._resolve(what, stream)
        placed = next(
            (
                v
                for v in self.op.values
                if isinstance(v, PlaceWord) and v.buffer == buffer.name
            ),
            None,
        )
        if placed is not None and (offset_by is not None or sliced_by is not None):
            raise ValueError(
                f"{type(self.op).__name__}.{buffer.name} is placed in a larger "
                f"buffer, {placed.name} moving its transfers; a transfer of it "
                f"takes no per-call offset of its own"
            )
        offset_by = placed or offset_by or sliced_by
        into, start = buffer.placement
        if (into, start) != (buffer.elements, 0):
            tap = TensorAccessPattern(
                (into,), tap.offset + start, tap.sizes, tap.strides
            )
        if offset_by is not None and offset_by.param is None:
            raise ValueError(
                f"{offset_by.name} has no device parameter: the operator does not use "
                f"it (uses_value) or the build has not created it yet"
            )
        sizes_by = self._sizes_by(size_by)
        if repeat_by is not None:
            if not isinstance(repeat_by, Value):
                raise TypeError(
                    f"repeat_by takes a value member's word (op.value(name)), "
                    f"got {repeat_by!r}"
                )
            if repeat_by.param is None:
                raise ValueError(
                    f"{repeat_by.name} has no device parameter: the operator does "
                    f"not use it (uses_value) or the build has not created it yet"
                )
            if 0 in sizes_by:
                raise ValueError(
                    f"{type(self.op).__name__}.{buffer.name}: a per-call repeat "
                    f"count is the outermost dimension's size, which size_by "
                    f"also sets"
                )
        data = self._tensors[buffer.name]
        if managed:
            common = dict(wait=wait, group=group)
        else:
            if group is not None:
                raise ValueError("an unmanaged transfer joins no group")
            common = dict(wait=wait, managed=False)
        # A per-call size lands in one descriptor's length, a repeat count in
        # its push; an offset patches every split piece.
        per_call = sizes_by or repeat_by is not None
        if per_call and not BdLimits.of(self.op.dev, 0, 0).fits(tap, buffer.dtype):
            raise ValueError(
                f"{type(self.op).__name__}.{buffer.name}: {tap} moves by a per-call "
                f"size, so it must fit one buffer descriptor, and does not"
            )
        dynamic = offset_by is not None and offset_by.ssa is not None
        dynamic = dynamic or any(v.ssa is not None for v in sizes_by.values())
        dynamic = dynamic or (repeat_by is not None and repeat_by.ssa is not None)
        if not dynamic:
            length = {}
            if sizes_by:
                ((dim, value),) = sizes_by.items()
                sizes, _ = BdLimits.slots(tap.sizes, tap.strides)
                if dim == 0 or prod(sizes[1:dim]) != 1:
                    raise ValueError(
                        f"{type(self.op).__name__}.{buffer.name}: {tap} is bounded "
                        f"on dimension {dim}, which is not the outermost a "
                        f"descriptor's length ends"
                    )
                length = dict(
                    length_parameter=value.param, length_unit=prod(sizes[dim + 1 :])
                )
            if repeat_by is not None:
                length["repeat_parameter"] = repeat_by.param
            return fn(
                data,
                tap=tap,
                offset_parameter=offset_by.param if offset_by is not None else None,
                **length,
                **common,
            )
        sizes, strides = BdLimits.slots(tap.sizes, tap.strides)
        for dim, value in sizes_by.items():
            # A unit dimension's stride is normalised to 0, which a dynamic
            # size may not have; its count never passes 1, so the stride the
            # next block would have moves the same bytes.
            if sizes[dim] == 1 and strides[dim] == 0:
                inner = zip(sizes[dim + 1 :], strides[dim + 1 :])
                strides[dim] = max(n * stride for n, stride in inner)
            sizes[dim] = value.ssa
        if repeat_by is not None:
            sizes[0] = repeat_by.ssa + arith.constant(1, IntegerType.get_signless(32))
        offset: Any = tap.offset
        if offset_by is not None and offset_by.ssa is not None:
            offset = offset_by.ssa
            if tap.offset:
                offset = offset + arith.constant(
                    int(tap.offset), IntegerType.get_signless(32)
                )
        return fn(
            data,
            tap=TensorAccessPattern(tap.tensor_dims, offset, sizes, strides),
            **common,
        )

    def _sizes_by(self, size_by) -> dict[int, Value]:
        if not size_by:
            return {}
        if len(size_by) > 1:
            raise ValueError(
                f"a per-call size bounds one dimension, the descriptor's length; "
                f"got dimensions {sorted(size_by)}"
            )
        out = {}
        for dim, value in size_by.items():
            if not isinstance(value, Value):
                raise TypeError(
                    f"size_by takes a value member's word (op.value(name)), got "
                    f"{value!r} for dimension {dim}"
                )
            if isinstance(value, DispatchTime):
                raise ValueError(
                    f"{value.name} is a DispatchTime value; a per-call size is a "
                    f"scratchpad word patched into the descriptor"
                )
            if value.param is None:
                raise ValueError(
                    f"{value.name} has no device parameter: the operator does not "
                    f"use it (uses_value) or the build has not created it yet"
                )
            if not 0 <= int(dim) < 4:
                raise ValueError(f"a descriptor has dimensions 0..3, not {dim}")
            out[int(dim)] = value
        return out

    @staticmethod
    def _lane(stream) -> Lane:
        if isinstance(stream, Operand):
            if stream.count != 1:
                raise ValueError(f"{stream.name} is per-{stream.count}; name a lane")
            return stream.lane(0)
        if isinstance(stream, Lane):
            return stream
        raise TypeError(
            f"fill/drain take an operand's lane, or an operand that is its own "
            f"one-lane stream, got {stream!r}"
        )

    def _resolve(
        self, what, stream
    ) -> tuple[Operand, TensorAccessPattern, Value | None]:
        """``(buffer, tap, offset_by)`` of what a transfer moves."""
        if isinstance(what, TensorAccessPattern):
            return self._lane(stream).buffer, what, None
        if isinstance(what, Operand):
            return what, what.tap, None
        if isinstance(what, BufferView):
            return what.buffer, what.tap, what.offset_by
        if (
            isinstance(what, tuple)
            and len(what) == 2
            and isinstance(what[0], Operand)
            and isinstance(what[1], TensorAccessPattern)
        ):
            return what[0], what[1], None
        raise TypeError(
            f"fill/drain take a buffer, a slice of one, a TensorAccessPattern or "
            f"(buffer, TensorAccessPattern); got {what!r}"
        )

    def data(self, buffer: Operand):
        return self._tensors[buffer.name]

    def preamble(self, **values) -> None:
        """Residents, then the parameter sync, then barriers, before any DMA.

        An ``own_preamble`` operator's sequence calls it itself, ``values``
        overriding residents by name.
        """
        op = self.op
        residents = op.residents
        unknown = set(values) - set(residents)
        if unknown:
            raise ValueError(
                f"{type(op).__name__} has no resident {sorted(unknown)} to override"
            )
        values = {**residents, **values}
        writes: dict[int, tuple] = {}  # id(buffer) -> (buffer, {index: value})
        for name in residents:
            res = op.value(name)
            if res.optional and not res.targets:
                continue  # this configuration does not allocate it
            if not res.targets:
                raise ValueError(
                    f"{type(op).__name__}.{name}: array() never bound this value"
                )
            for buf, index in res.targets:
                writes.setdefault(id(buf), (buf, {}))[1][index] = values[name]
        for buf, words in writes.values():
            for index in sorted(words):
                buf[index] = words[index]
        # Without a scratchpad, a core-read value is written from the per-call scalar.
        for value in op.values:
            for buf, index in value.targets:
                if value.ssa is None:
                    raise ValueError(
                        f"{value.name} is bound to a runtime-parameter buffer but is "
                        f"not a dispatch-time scalar here; bind only under an image "
                        f"without a scratchpad (an xclbin image)"
                    )
                buf[index] = value.ssa
        # A barrier opens its core, which reads its per-call words at once.
        if any(value.scratchpad for value in op.values):
            sync_parameters()
        for b in self.barriers:
            b.set(1)
