# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The runtime sequence of one operator."""

from __future__ import annotations

from math import prod
from typing import Any

import numpy as np
from aie.extras.dialects import arith
from aie.helpers.taplib import TensorAccessPattern
from aie.ir import IntegerType
from aie.iron import TaskGroup, WorkerRuntimeBarrier, sync_parameters

from ..declare import DispatchTime, Operator
from ..declare.bound import BoundBuffer, BoundValue, BufferView, Lane
from ..declare.operator import _PlaceWord
from .bd import BdLimits


class Sequence:
    """The runtime sequence of one operator: its ``sequence(rt)`` override, or
    the one derived from the declarations.

    ``fill``/``drain`` take an operand's lane (or a one-lane operand) and a
    buffer, a slice of one or ``(buffer, TensorAccessPattern)``.
    """

    def __init__(
        self,
        op: Operator,
        rt_data: dict[str, Any],
        image: str = "elf",
        barriers: tuple[WorkerRuntimeBarrier, ...] = (),
    ):
        self.op = op
        self._rt_data = rt_data
        self.image = image
        self.barriers = barriers

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
            for slot, tap, size_by in self.plan(buf):
                self.fill(slot, (buf, tap), group=tg, size_by=size_by)
        for buf in self.op.outputs:
            for slot, tap, size_by in self.plan(buf):
                self.drain(slot, (buf, tap), group=tg, wait=True, size_by=size_by)
        tg.finish()

    def plan(
        self, buf: BoundBuffer
    ) -> list[tuple[Any, TensorAccessPattern, dict | None]]:
        """The derived ``(slot, tap, size_by)`` transfers of one operand:
        ``split``, or ``round_robin`` under a bound.
        """
        if not buf.streamed:
            raise ValueError(
                f"{type(self.op).__name__}.{buf.name} has no tile=, so its "
                f"sequence cannot be derived; add tile= or override sequence(rt)"
            )
        bounded = buf.bounded
        if bounded is None:
            return [(slot, tap, None) for slot, tap in self.split(buf)]
        extent, axis, word = bounded
        if axis != buf.batch_axes:
            raise ValueError(
                f"{type(self.op).__name__}.{buf.name}: {extent.name} bounds axis "
                f"{axis}, but the derived sequence splits axis {buf.batch_axes}; "
                f"override sequence(rt) to bound another axis"
            )
        return [
            (slot, tap, {dim: word}) for slot, tap, dim in self.round_robin(buf, axis)
        ]

    @staticmethod
    def split(buffer: BoundBuffer) -> list[tuple[Lane, TensorAccessPattern]]:
        """``[(lane, tap), ...]``: the whole buffer for a one-lane or broadcast
        stream, else the first non-batch axis in one block per lane.
        """
        count = buffer.count
        if count == 1:
            return [(buffer.lane(0), buffer.tap)]
        if buffer.replicate:
            return [(buffer.lane(i), buffer.tap) for i in range(count)]
        shape, axis = buffer.shape, buffer.batch_axes
        if axis >= len(shape) or shape[axis] % count:
            raise ValueError(
                f"{buffer.name} {shape} does not divide across its {count} lanes "
                f"on axis {axis}. Check {type(buffer._op).__name__}.compatible()"
            )
        parts = TensorAccessPattern.full(shape).partition(count, axis)
        return [(buffer.lane(i), parts[i]) for i in range(count)]

    @staticmethod
    def round_robin(
        buffer: BoundBuffer, axis: int
    ) -> list[tuple[Lane, TensorAccessPattern, int]]:
        """``[(lane, tap, dim), ...]`` with ``axis`` bounded per call, ``dim``
        the descriptor dimension a call patches.

        Lane ``k`` takes tiles ``k, k + lanes, ...``, so each lane has a fixed
        offset and stride and one patched count.
        """
        shape, dtype = buffer.shape, buffer.dtype
        count = buffer.count
        lanes = 1 if buffer.replicate else count
        inner = prod(shape[axis + 1 :])
        tile_rows = buffer.extent_unit(axis)
        if shape[axis] % (lanes * tile_rows):
            raise ValueError(
                f"{buffer.name} {shape}: axis {axis} does not divide into {tile_rows}-row "
                f"tiles over {lanes} lanes"
            )
        if axis > 1:
            raise ValueError(
                f"{buffer.name} {shape}: bounding axis {axis} needs {axis + 3} "
                f"descriptor dimensions; a descriptor has four"
            )
        tiles = shape[axis] // (lanes * tile_rows)
        run = tile_rows * inner
        shim = BdLimits.of(buffer._op.dev, 0, 0)
        halves = shim.factor(run, shim.granule(dtype))
        if halves is None:
            raise ValueError(
                f"{buffer.name}: a {run}-element tile does not fit one descriptor"
            )
        iterations = shape[0] if axis else 1
        tiled = TensorAccessPattern.full((iterations, tiles, lanes, run))
        out = []
        for lane in range(lanes):
            tap = tiled[:, :, lane].split(2, halves[1])
            if not shim.fits(tap, dtype):
                raise ValueError(
                    f"{buffer.name} {shape}: the round-robin split over {lanes} lanes "
                    f"does not fit one descriptor per lane"
                )
            slots = range(count) if buffer.replicate else [lane]
            for s in slots:
                out.append((buffer.lane(s), tap, 1))
        return out

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
        if lane.buffer.member.feed and riding and buffer.name == lane.buffer.name:
            name = f"{type(self.op).__name__}.{buffer.name}"
            if offset_by or size_by or sliced_by:
                raise ValueError(
                    f"{name}: the finish's inputs ride it an output tile at a "
                    f"time, so it moves by no per-call offset or size"
                )
            if finishing is None and tap != self.split(buffer)[lane.index][1]:
                raise ValueError(
                    f"{name}: the finish's inputs ride it an output tile at a "
                    f"time, so a fill of lane {lane.index} is its whole share"
                )
            (out,) = self.op.outputs
            line = prod(out.tile_shape)
            share = finishing or self.split(out)[lane.index][1]
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
            "fill", stream, source, group, wait, offset_by, size_by, managed
        )
        if not lane.buffer.member.prepare:
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
    ):
        """Drain ``stream`` into ``dest``; see ``fill`` for the other forms."""
        return self._transfer(
            "drain", stream, dest, group, wait, offset_by, size_by, managed
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
    ):
        fn = getattr(self._lane(stream).handle, verb)
        buffer, tap, sliced_by = self._resolve(what, stream)
        placed = next(
            (
                v
                for v in self.op.values
                if isinstance(v.member, _PlaceWord) and v.member.buffer == buffer.name
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
        data = self._rt_data[buffer.name]
        if managed:
            common = dict(wait=wait, group=group)
        else:
            if group is not None:
                raise ValueError("an unmanaged transfer joins no group")
            common = dict(wait=wait, managed=False)
        # A per-call size lands in one descriptor's length; an offset patches every split piece.
        if sizes_by and not BdLimits.of(self.op.dev, 0, 0).fits(tap, buffer.dtype):
            raise ValueError(
                f"{type(self.op).__name__}.{buffer.name}: {tap} moves by a per-call "
                f"size, so it must fit one buffer descriptor, and does not"
            )
        dynamic = offset_by is not None and offset_by.ssa is not None
        dynamic = dynamic or any(v.ssa is not None for v in sizes_by.values())
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

    def _sizes_by(self, size_by) -> dict[int, BoundValue]:
        if not size_by:
            return {}
        if len(size_by) > 1:
            raise ValueError(
                f"a per-call size bounds one dimension, the descriptor's length; "
                f"got dimensions {sorted(size_by)}"
            )
        out = {}
        for dim, value in size_by.items():
            if not isinstance(value, BoundValue):
                raise TypeError(
                    f"size_by takes a value member's word (op.value(name)), got "
                    f"{value!r} for dimension {dim}"
                )
            if isinstance(value.member, DispatchTime):
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
        if isinstance(stream, BoundBuffer):
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
    ) -> tuple[BoundBuffer, TensorAccessPattern, BoundValue | None]:
        """``(buffer, tap, offset_by)`` of what a transfer moves."""
        if isinstance(what, TensorAccessPattern):
            return self._lane(stream).buffer, what, None
        if isinstance(what, BoundBuffer):
            return what, what.tap, None
        if isinstance(what, BufferView):
            return what.buffer, what.tap, what.offset_by
        if (
            isinstance(what, tuple)
            and len(what) == 2
            and isinstance(what[0], BoundBuffer)
            and isinstance(what[1], TensorAccessPattern)
        ):
            return what[0], what[1], None
        raise TypeError(
            f"fill/drain take a buffer, a slice of one, a TensorAccessPattern or "
            f"(buffer, TensorAccessPattern); got {what!r}"
        )

    def data(self, buffer: BoundBuffer):
        return self._rt_data[buffer.name]

    def preamble(self, **values) -> None:
        """Residents, then barriers, then the parameter sync, before any DMA.

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
        for b in self.barriers:
            b.set(1)
        if self.image == "elf" and op.values:
            sync_parameters()
