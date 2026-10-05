# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The sequence for an image IRON did not build.

An operator declared with ``image=`` (``Xclbin``)
has no array to build: every core program, memtile buffer and stream-switch
route comes from the downloaded image. What the sequence must supply is the
other half of a dispatch, and the declaration carries everything it needs:
each operand's shim column and channel (``via=``), each value's address in
core data memory and the lock a core waits on before reading it. flm's
shipped ``mm`` binary is the one that does today.

Transfers are emitted as shim DMA tasks on the pinned allocations, at most
``depth`` outstanding per lane (the image's memtiles hold that many
objects, so a further transfer would overwrite one still in use). Task
groups have no meaning here and are accepted as no-ops, so an operator's
``sequence(rt)`` reads the same against a built or a shipped image.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Any

import numpy as np
from aie.dialects import aie, aiex
from aie.dialects.aie import (
    DMAChannelDir,
    get_target_model,
)
from aie.helpers.taplib import TensorAccessPattern
from aie.helpers.util import np_ndarray_type_to_memref_type
from aie.ir import Context, InsertionPoint, Location, Module

from ..declare import Operator
from ..declare.bound import BoundBuffer, BoundStream, _StreamSlot
from .runtime import Transfers


class _NoGroup:
    def finish(self) -> None:
        pass


class ExternalSequence(Transfers):
    """What an operator's ``sequence(rt)`` receives against a shipped image.

    The same surface ``Sequence`` offers, lowering a
    transfer to shim DMA tasks on the image's pinned channels instead of
    ObjectFIFO fills. ``module`` is the whole module for one operator.
    """

    def __init__(
        self,
        op: Operator,
        rt_data: dict[str, Any],
        allocations: dict[tuple[str, int], str],
        locks: dict[tuple[int, int, int], Any],
    ):
        self.op = op
        self._rt_data = rt_data
        self._allocations = allocations
        self._locks = locks
        self._queues: dict[tuple[str, int], list] = {}

    @classmethod
    def module(cls, dev, op: Operator) -> Module:
        """The module whose runtime sequence drives ``op``'s downloaded image."""
        npu: Any = dev.resolve()  # Device.resolve() is annotated -> None upstream
        tm = get_target_model(npu)
        core_tiles = [
            (col, row)
            for row in range(1 + tm.get_num_mem_tile_rows(), tm.rows())
            for col in range(dev.cols)
        ]
        buffers = op.buffers
        residents = [op.value(name) for name in op.residents]
        lock_ids = sorted({v.lock for v in residents if v.lock is not None})

        loc = Location.unknown(Context())
        module = Module.create(loc)
        with loc.context, loc, InsertionPoint(module.body):
            types = [np_ndarray_type_to_memref_type(b.flat_type) for b in buffers]

            @aie.device(npu)
            def device_body():
                tiles: dict[tuple[int, int], Any] = {}

                def tile(col, row):
                    return tiles.setdefault((col, row), aie.tile(col, row))

                allocations = {}
                for s in op.streams.values():
                    for i in range(s.count):
                        pin = s.pin(i)
                        if pin is None or pin.channel is None:
                            raise ValueError(
                                f"{type(op).__name__}.{s.name}[{i}] has no (column, "
                                f"channel) pin; a shipped image's streams need one"
                            )
                        name = f"{s.name}_{i}"
                        direction = (
                            DMAChannelDir.MM2S
                            if s.direction == "in"
                            else DMAChannelDir.S2MM
                        )
                        aie.shim_dma_allocation(
                            name, tile(pin.col, 0), direction, pin.channel
                        )
                        allocations[(s.name, i)] = name
                locks = {
                    (col, row, lock_id): aie.lock(tile(col, row), lock_id=lock_id)
                    for col, row in core_tiles
                    for lock_id in lock_ids
                }

                @aiex.runtime_sequence(*types)
                def sequence(*args):
                    rt_data = {b.name: a for b, a in zip(buffers, args)}
                    seq = cls(op, rt_data, allocations, locks)
                    seq.write_residents(core_tiles)
                    seq.run()
                    seq.finish()

            return module

    def write_residents(self, core_tiles) -> None:
        """Write every resident value's words into every core, then release the locks.

        A value may be one word or a sequence of words written at consecutive
        addresses. All writes precede the first lock release, so no core reads
        a half-written buffer.
        """
        values = self.op.residents
        residents = [self.op.value(name) for name in values]
        for col, row in core_tiles:
            for res in residents:
                words = values[res.name]
                if isinstance(words, (int, np.integer)):
                    words = [words]
                assert res.address is not None, "a value written into a shipped image"
                for i, word in enumerate(words):
                    aiex.npu_write32(
                        res.address + 4 * i, int(word), column=col, row=row
                    )
        for col, row in core_tiles:
            for res in residents:
                if res.lock is not None:
                    aiex.set_lock_value(self._locks[(col, row, res.lock)], 1)

    # -- transfers ---------------------------------------------------------

    def fill(self, stream, source, *, group=None, wait=False, offset_by=None):
        self._transfer(stream, source, offset_by)

    def drain(self, stream, dest, *, group=None, wait=True, offset_by=None):
        self._transfer(stream, dest, offset_by)

    def _transfer(self, stream, what, offset_by) -> None:
        if offset_by is not None:
            raise NotImplementedError(
                "per-call offsets are not supported on a shipped image"
            )
        key = self._key(stream)
        depth = self._depth(stream)
        buffer, tap = self._resolve(what, stream)
        queue = self._queues.setdefault(key, [])
        if len(queue) == depth:
            aiex.dma_await_task(queue.pop(0))
        task = aiex.shim_dma_single_bd_task(
            self._allocations[key],
            self._rt_data[buffer.name],
            tap=tap,
            issue_token=True,
        )
        aiex.dma_start_task(task)
        queue.append(task)

    @staticmethod
    def _lane(stream) -> _StreamSlot | BoundStream:
        if isinstance(stream, BoundBuffer):
            stream = stream.lanes  # an operand that is its own stream
        if isinstance(stream, (_StreamSlot, BoundStream)):
            return stream
        raise TypeError(
            f"fill/drain take a stream, one lane of it, or an operand that is its "
            f"own stream, got {stream!r}"
        )

    def _key(self, stream) -> tuple[str, int]:
        lane = self._lane(stream)
        if isinstance(lane, _StreamSlot):
            return (lane.stream.name, lane.index)
        return (lane.name, 0)

    def _depth(self, stream) -> int:
        lane = self._lane(stream)
        s = lane.stream if isinstance(lane, _StreamSlot) else lane
        return s.member.depth

    def _resolve(self, what, stream) -> tuple[BoundBuffer, TensorAccessPattern]:
        if isinstance(what, TensorAccessPattern):
            lane = self._lane(stream)
            s = lane.stream if isinstance(lane, _StreamSlot) else lane
            if s.buffer is None:
                raise TypeError(
                    f"a TensorAccessPattern alone names no buffer; {stream!r} is not "
                    f"an operand's own stream, so give (buffer, tap)"
                )
            return s.buffer, what
        if isinstance(what, BoundBuffer):
            return what, what.tap
        if (
            isinstance(what, tuple)
            and len(what) == 2
            and isinstance(what[1], TensorAccessPattern)
        ):
            return what[0], what[1]
        raise TypeError(
            f"an external sequence takes a buffer, a TensorAccessPattern on an "
            f"operand's own stream, or (buffer, tap); got {what!r}"
        )

    def finish(self) -> None:
        """Await every outstanding transfer; the end of the sequence."""
        for queue in self._queues.values():
            for task in queue:
                aiex.dma_await_task(task)
            queue.clear()

    # -- structure (no-ops: the queues above are the only ordering) ----------

    @contextmanager
    def group(self):
        yield _NoGroup()

    def new_group(self):
        return _NoGroup()

    def data(self, buffer: BoundBuffer):
        return self._rt_data[buffer.name]
