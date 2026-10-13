# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The runtime sequence for an image IRON did not build.

An operator declared with ``image=`` (``Xclbin``) has no array to build:
every core program, memtile buffer and stream-switch route comes from the
downloaded image. What the sequence must supply is the other half of a
dispatch, and the declaration carries everything it needs: each operand's
shim tile and channel (``via=``, ``channel=``), each value's address in core
data memory and the lock a core waits on before reading it. flm's shipped
``mm`` binary is the one that does today.

Transfers are emitted as shim DMA tasks on the pinned channels, at most
``depth`` outstanding per lane (the image's memtiles hold that many
objects, so a further transfer would overwrite one still in use). Task
groups have no meaning here and are accepted as no-ops, so an operator's
``sequence(rt)`` reads the same against a built or a shipped image.
"""

from __future__ import annotations

import numpy as np
from aie.dialects.aie import DMAChannelDir
from aie.iron import Buffer, Lock, Task
from aie.iron.device import Tile
from aie.iron.runtime.dmatask import emit_shim_transfer

from ..declare import Operator
from .runtime import OperatorRuntime, ShimChannel


class ShippedRuntime(OperatorRuntime):
    """What an operator's ``sequence(rt)`` receives against a shipped image.

    ``OperatorRuntime`` with each transfer lowered to a shim DMA task on the
    image's pinned channel instead of an ObjectFIFO fill, its body first
    writing the image's parameter block and releasing the locks its cores
    wait on.

    Args:
        op: The resolved operator, declared with ``image=``.
        dev: The device the image runs on.

    Attributes:
        writes: Each parameter-block buffer and the words written to it.
    """

    def __init__(self, op: Operator, dev) -> None:
        shims = {col: Tile(col, 0) for col in range(dev.cols)}
        channels: dict[tuple[str, int], ShimChannel] = {}
        for s in op.buffers:
            if not s.streamed:
                continue
            for i in range(s.count):
                pin = s.lane(i).shim
                if pin is None or s.channel is None:
                    raise ValueError(
                        f"{type(op).__name__}.{s.name}[{i}] has no shim tile and "
                        f"channel pin; a shipped image's streams need one"
                    )
                channels[(s.name, i)] = ShimChannel(
                    f"{s.name}_{i}",
                    shims[pin.col],
                    DMAChannelDir.S2MM if s.drains else DMAChannelDir.MM2S,
                    s.channel,
                )

        cores = [Tile(col, row) for row in dev.core_rows for col in range(dev.cols)]
        self.writes: list[tuple[Buffer, list[int]]] = []
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
                self.writes.append((buffer, words))
        locks = [
            Lock(tile, lock_id=lock_id)
            for tile in cores
            for lock_id in sorted({op.value(n).lock for n in op.residents} - {None})
        ]
        super().__init__(op, [*channels.values(), *locks])
        self.buffers = [buffer for buffer, _ in self.writes]
        self._symbols = {key: channel.symbol for key, channel in channels.items()}
        self._queues: dict[tuple[str, int], list[Task]] = {}

    def body(self, *args) -> None:
        # Every word precedes the first release, so no core reads a
        # half-written block.
        for buffer, words in self.writes:
            for i, word in enumerate(words):
                buffer[i] = word
        for lock in self.locks:
            lock.set(1)
        self._tensors = {b.name: a for b, a in zip(self.op.buffers, args)}
        self.run()
        self.finish()

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
    ) -> None:
        buffer, tap, sliced_by = self._resolve(what, stream)
        per_call = (offset_by, sliced_by, size_by, repeat_by)
        if any(v is not None for v in per_call):
            raise NotImplementedError(
                "per-call offsets, sizes and repeat counts are not supported on a "
                "shipped image"
            )
        lane = self._lane(stream)
        key = (lane.buffer.name, lane.index)
        queue = self._queues.setdefault(key, [])
        if len(queue) == lane.buffer.depth:
            queue.pop(0).await_()
        queue.append(
            emit_shim_transfer(
                self._symbols[key],
                self._tensors[buffer.name],
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
