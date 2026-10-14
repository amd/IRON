# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The runtime sequence for an image IRON did not build.

An operator declared with ``image=`` (``Xclbin``) has no array to build:
every core program, memtile buffer and stream-switch route comes from the
downloaded image. What the sequence must supply is the other half of a
dispatch: each operand's shim tile and channel (``via=``, ``channel=``), and
what the operator's ``array()`` places of the image, its parameter blocks
(``Buffer(address=)``) and the locks its cores wait on before reading them
(``Lock(lock_id=)``). flm's shipped ``mm`` binary is the one that does today.

Transfers are emitted as shim DMA tasks on the pinned channels, at most
``depth`` outstanding per lane (the image's memtiles hold that many
objects, so a further transfer would overwrite one still in use). Task
groups have no meaning here and are accepted as no-ops, so an operator's
``sequence(rt)`` reads the same against a built or a shipped image.
"""

from __future__ import annotations

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
        built: What its ``array()`` placed: parameter blocks and the locks
            that release them.
    """

    def __init__(self, op: Operator, dev, built: list) -> None:
        shims = {col: Tile(col, 0) for col in range(dev.cols)}
        channels: dict[tuple[str, int], ShimChannel] = {}
        for s in op.buffers:
            if not s.streamed:
                continue
            pins = [s.via] if isinstance(s.via, Tile) else s.via
            for i in range(s.count):
                pin = None if pins is None or len(pins) != s.count else pins[i]
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

        locks = [obj for obj in built if isinstance(obj, Lock)]
        blocks = [obj for obj in built if isinstance(obj, Buffer)]
        if len(locks) + len(blocks) != len(built):
            raise TypeError(
                f"{type(op).__name__}.array() places parameter blocks and locks "
                f"of a shipped image, which builds nothing else"
            )
        super().__init__(op, [*channels.values(), *locks])
        self.buffers = blocks
        self._symbols = {key: channel.symbol for key, channel in channels.items()}
        self._queues: dict[tuple[str, int], list[Task]] = {}

    def body(self, *args) -> None:
        # Every word precedes the first release, so no core reads a
        # half-written block.
        self.preamble()
        for lock in self.locks:
            lock.set(1)
        self._tensors = {b.name: a for b, a in zip(self.op.buffers, args)}
        for b in self.op.buffers:
            b.runtime = self
        self.run()
        self.finish()

    def _emit(
        self,
        verb: str,
        operand,
        lane: int,
        buffer,
        tap,
        group,
        wait: bool,
        managed: bool,
        offset_parameter=None,
        length_parameter=None,
        length_unit=None,
        repeat_parameter=None,
    ) -> None:
        per_call = (offset_parameter, length_parameter, repeat_parameter)
        if any(v is not None for v in per_call):
            raise NotImplementedError(
                "per-call offsets, sizes and repeat counts are not supported on a "
                "shipped image"
            )
        key = (operand.name, lane)
        queue = self._queues.setdefault(key, [])
        if len(queue) == operand.depth:
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
