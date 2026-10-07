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

Transfers are emitted as shim DMA tasks on the pinned channels, at most
``depth`` outstanding per lane (the image's memtiles hold that many
objects, so a further transfer would overwrite one still in use). Task
groups have no meaning here and are accepted as no-ops, so an operator's
``sequence(rt)`` reads the same against a built or a shipped image.
"""

from __future__ import annotations

from typing import Any, NamedTuple

import numpy as np
from aie.dialects.aie import DMAChannelDir, shim_dma_allocation
from aie.iron import Buffer, Lock, Program, Runtime, Task
from aie.iron.device import Tile
from aie.iron.runtime.dmatask import emit_shim_transfer

from ..declare import Direction, Operator
from .runtime import Sequence


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


class ImageRuntime(Runtime):
    """A ``Runtime`` against channels and buffers an image already has.

    aie.iron names a shim channel through the route it starts or ends, and
    places a buffer through the worker that reads it; a shipped image has
    both already, so they are declared here, at device scope, ahead of the
    sequence.
    """

    def __init__(
        self,
        seq_fn,
        fn_args,
        channels: list[ShimChannel],
        buffers: list[Buffer],
    ):
        super().__init__(seq_fn, fn_args)
        self.channels = channels
        self.buffers = buffers

    def resolve(self, loc=None, ip=None, *, device=None, **options) -> None:
        assert device is not None, "a Program resolves its runtime on its device"
        for symbol, tile, direction, channel in self.channels:
            device.resolve_tile(tile)
            shim_dma_allocation(symbol, tile.op, direction, channel)
        for buffer in self.buffers:
            assert buffer.tile is not None
            device.resolve_tile(buffer.tile)
            buffer.resolve()
        super().resolve(loc, ip, device=device, **options)


class ExternalSequence(Sequence):
    """What an operator's ``sequence(rt)`` receives against a shipped image.

    ``Sequence`` with each transfer lowered to a shim DMA task on the
    image's pinned channel instead of an ObjectFIFO fill. ``module`` is the
    whole module for one operator.
    """

    def __init__(self, op: Operator, rt_data: dict[str, Any], channels: dict):
        super().__init__(op, rt_data)
        self._channels = channels
        self._queues: dict[tuple[str, int], list[Task]] = {}

    @classmethod
    def module(cls, dev, op: Operator):
        """The module whose runtime sequence drives ``op``'s downloaded image."""
        shims = {col: Tile(col, 0) for col in range(dev.cols)}
        channels = {}
        for s in op.buffers:
            if not s.streamed:
                continue
            for i in range(s.count):
                pin = s.lane(i).shim
                if pin is None or pin.channel is None:
                    raise ValueError(
                        f"{type(op).__name__}.{s.name}[{i}] has no (column, "
                        f"channel) pin; a shipped image's streams need one"
                    )
                direction = (
                    DMAChannelDir.MM2S
                    if s.direction is Direction.IN
                    else DMAChannelDir.S2MM
                )
                channels[(s.name, i)] = ShimChannel(
                    f"{s.name}_{i}",
                    shims[pin.col],
                    direction,
                    pin.channel,
                )

        cores = [Tile(col, row) for row in dev.core_rows for col in range(dev.cols)]
        writes: list[tuple[Buffer, list[int]]] = []
        locks: list[Lock] = []
        for tile in cores:
            for name, words in op.residents.items():
                res = op.value(name)
                assert res.address is not None, "a value written into a shipped image"
                words = [int(w) for w in np.atleast_1d(words)]
                buffer = Buffer(
                    np.ndarray[(len(words),), np.dtype[np.int32]],
                    name=f"{name}_{tile.col}_{tile.row}",
                    tile=tile,
                    use_write_rtp=True,
                    address=res.address,
                )
                writes.append((buffer, words))
        for tile in cores:
            for lock_id in sorted({op.value(n).lock for n in op.residents} - {None}):
                locks.append(Lock(tile, lock_id=lock_id))

        buffers = op.buffers

        def sequence(*args):
            # Every word precedes the first release, so no core reads a
            # half-written block.
            for buffer, words in writes:
                for i, word in enumerate(words):
                    buffer[i] = word
            for lock in locks:
                lock.set(1)
            seq = cls(
                op,
                {b.name: a for b, a in zip(buffers, args)},
                {key: symbol for key, (symbol, *_) in channels.items()},
            )
            seq.run()
            seq.finish()

        rt = ImageRuntime(
            sequence,
            [b.flat_type for b in buffers],
            list(channels.values()),
            [buffer for buffer, _ in writes],
        )
        for lock in locks:
            rt.add_lock(lock)
        return Program(dev, rt).resolve_program()

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
    ) -> None:
        buffer, tap, sliced_by = self._resolve(what, stream)
        if offset_by is not None or sliced_by is not None or size_by is not None:
            raise NotImplementedError(
                "per-call offsets and sizes are not supported on a shipped image"
            )
        lane = self._lane(stream)
        key = (lane.buffer.name, lane.index)
        queue = self._queues.setdefault(key, [])
        if len(queue) == lane.buffer.depth:
            queue.pop(0).await_()
        queue.append(
            emit_shim_transfer(
                self._channels[key],
                self._rt_data[buffer.name],
                tap=tap,
                wait=True,
                managed=False,
            )
        )

    def finish(self) -> None:
        """Await every outstanding transfer; the end of the sequence."""
        for queue in self._queues.values():
            for task in queue:
                task.await_()
            queue.clear()
