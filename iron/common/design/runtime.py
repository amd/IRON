# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The runtime sequence of one operator, as aie.iron's ``Runtime``."""

from __future__ import annotations

import functools
from math import prod
from typing import Any

from aie.dialects.aie import shim_dma_allocation
from aie.dialects.aiex import shim_dims
from aie.extras.dialects import arith
from aie.helpers.taplib import TensorAccessPattern
from aie.ir import IntegerType
from aie.iron import (
    Buffer,
    DmaEndpoint,
    Flow,
    Lock,
    PacketFlow,
    Runtime,
    Task,
    TaskGroup,
    TileDma,
    Worker,
    sync_parameters,
)
from aie.iron.runtime.dmatask import emit_shim_transfer

from ..declare import Built, Operator, Value
from ..declare.operand import Operand, active_runtime


class OperatorRuntime(Runtime):
    """The runtime sequence of one operator: aie.iron's ``Runtime``, whose
    body runs the preamble and then the operator's ``sequence(rt)``, or the
    sequence derived from its declaration.

    It is what ``sequence(rt)`` receives, whose transfers are the
    operands' own ``fill``/``drain``, emitted here (``transfer``). A managed
    transfer on a pinned lane (``Operand.pin``) keeps at most the operand's
    ``depth`` in flight, and the sequence's end awaits them.

    Args:
        op: The resolved operator, its array built and its operands' lanes
            bound or pinned.
        built: What its ``build()`` made: its workers, and the flows,
            locks, tile DMAs, pinned endpoints and buffers only the sequence
            reaches, and its cores' runtime parameters.
        name: The sequence's symbol; the Program names it when None.

    Attributes:
        built: What the build made, which ``sequence`` may read.
        pins: Each pinned lane this runtime declares, by its symbol.
        buffers: Buffers no worker places, declared whatever a shape's
            sequence reaches: a shipped image's parameter blocks, or a
            pool only descriptors address.
    """

    def __init__(self, op: Operator, built: Built, name: str | None = None) -> None:
        self.op = op
        self.built = built
        self.buffers = [b for b in built.objects if isinstance(b, Buffer)]
        self._tensors: dict[str, Any] = {}
        self._queues: dict[str, list[Task]] = {}
        # Raises if any stream of a built array is unbound.
        lanes = [
            (b, i, h) for b in op.buffers if b.streamed for i, h in enumerate(b.handles)
        ]
        # A shared array's pins are declared by the runtime of the array that built them.
        ours = {id(e) for e in built.objects if isinstance(e, DmaEndpoint)}
        self.pins = {f"{b.name}_{i}": h for b, i, h in lanes if id(h) in ours}
        if len(self.pins) != len(ours):
            raise TypeError(
                f"{type(op).__name__}.build() makes a DmaEndpoint no operand "
                f"is pinned to"
            )
        handles = [h for _, _, h in lanes if not isinstance(h, DmaEndpoint)]
        super().__init__(
            self.body,
            [
                *(b.flat_type for b in op.buffers),
                handles,
                *(v.param for v in op.values),
            ],
            name=name,
        )
        # Before resolving: the sequence body, generated last, may address any of it.
        for obj in built.objects:
            if isinstance(obj, (Flow, PacketFlow)):
                self.add_flow(obj)
            elif isinstance(obj, Lock):
                self.add_lock(obj)
            elif isinstance(obj, TileDma):
                self.add_tile_dma(obj)
            elif not isinstance(obj, (Worker, DmaEndpoint, Buffer)):
                raise TypeError(
                    f"{type(op).__name__}.build() makes Workers, Flows, "
                    f"PacketFlows, Locks, TileDmas, the DmaEndpoints it pinned "
                    f"and Buffers; got {obj!r}"
                )

    def body(self, *args) -> None:
        """The sequence body aie.iron runs: the operator's runtime tensors,
        its lanes' handles, then each per-call value, a dispatch-time scalar
        where it is not a scratchpad word.
        """
        buffers = self.op.buffers
        self._tensors = {b.name: a for b, a in zip(buffers, args)}
        for value, arg in zip(self.op.values, args[len(buffers) + 1 :]):
            if not value.in_scratchpad:
                value.ssa = arg
        token = active_runtime.set(self)
        try:
            if not self.op.own_preamble:
                self.preamble()
            self.run()
        finally:
            active_runtime.reset(token)
        for queue in self._queues.values():
            for task in queue:
                task.await_()

    def resolve(self, loc=None, ip=None, *, device=None, **options) -> None:
        self.declare(device)
        super().resolve(loc, ip, device=device, **options)

    def declare(self, device) -> None:
        """Its pins and buffers, at ``device`` scope ahead of the sequence:
        aie.iron names a shim channel through the route it starts or ends,
        and places a buffer through the worker that reads it, and these
        have neither.
        """
        for symbol, end in self.pins.items():
            device.resolve_tile(end.tile)
            shim_dma_allocation(symbol, end.tile.op, end.direction, end.channel)
        for buffer in self.buffers:
            device.resolve_tile(buffer.tile)
            buffer.resolve()

    def run(self) -> None:
        if self.op.has_sequence_override():
            self.op.sequence(self)
            return
        tg = TaskGroup()
        for buf in self.op.inputs:
            for lane, tap, word, unit in buf.transfers():
                buf.fill(
                    tap, lane=lane, group=tg, length_parameter=word, length_unit=unit
                )
        for buf in self.op.outputs:
            for lane, tap, word, unit in buf.transfers():
                buf.drain(
                    tap,
                    lane=lane,
                    group=tg,
                    wait=True,
                    length_parameter=word,
                    length_unit=unit,
                )
        tg.finish()

    def transfer(
        self,
        verb: str,
        operand: Operand,
        tap: TensorAccessPattern | None,
        *,
        lane: int | None,
        group,
        wait: bool,
        source: Operand | None = None,
        offset_parameter: Value | None = None,
        length_parameter: Value | None = None,
        length_unit: int | None = None,
        repeat_parameter: Value | None = None,
        managed: bool = True,
    ):
        """``operand.fill``/``operand.drain`` (``verb``): one transfer of
        ``source``'s (else ``operand``'s) ``tap`` through lane ``lane`` of
        ``operand``'s stream, its per-call words lowered for the image: a
        scratchpad parameter on a full ELF, the pattern's sizes and offset
        on an xclbin. See ``Operand.fill``.
        """
        if lane is None:
            if operand.lanes != 1:
                raise ValueError(f"{operand.name} is per-{operand.lanes}; name a lane")
            lane = 0
        buffer = operand if source is None else source
        tap = buffer.tap if tap is None else tap
        handle = operand.handles[lane]
        pinned = isinstance(handle, DmaEndpoint)
        symbol = f"{operand.name}_{lane}"
        fn = (
            functools.partial(emit_shim_transfer, symbol)
            if pinned
            else getattr(handle, verb)
        )
        for value in (offset_parameter, length_parameter, repeat_parameter):
            if value is None:
                continue
            if not isinstance(value, Value):
                raise TypeError(
                    f"a per-call parameter is a value member (self.count), "
                    f"got {value!r}"
                )
            if value.param is None:
                raise ValueError(
                    f"{value.name} has no device parameter: it is not per call "
                    f"here (Value.per_call), or the build has not created it yet"
                )
        if length_parameter is not None and length_parameter.dispatch:
            raise ValueError(
                f"{length_parameter.name} is a DispatchTime value; a per-call "
                f"length is a scratchpad word patched into the descriptor"
            )
        _, sizes, strides = shim_dims(tap)
        dim, scale = None, 1
        if length_parameter is not None:
            # A patched descriptor's length ends at its outermost dimension
            # below the iteration; an xclbin's stream, regenerated per call,
            # sizes any dimension of length_unit-element units. A unit may
            # span several steps of the dimension, as a linear run's elements.
            patched = length_parameter.ssa is None
            dim = next(
                (
                    d
                    for d in range(1, 4)
                    if (prod(sizes[1:d]) == 1 or not patched)
                    and length_unit % prod(sizes[d + 1 :]) == 0
                    and prod(sizes[d:]) % length_unit == 0
                ),
                None,
            )
            if dim is None:
                raise ValueError(
                    f"{type(self.op).__name__}.{buffer.name}: {tap} has no "
                    f"descriptor dimension of {length_unit}-element units"
                    + (" below the iteration, outermost" if patched else "")
                )
            scale = length_unit // prod(sizes[dim + 1 :])
        data = self._tensors[buffer.name]
        if pinned and managed:
            # The image's memtiles hold depth objects: past that, wait for the oldest.
            queue = self._queues.setdefault(symbol, [])
            if len(queue) == operand.depth:
                queue.pop(0).await_()
            common = dict(wait=True, managed=False)
        elif managed:
            common = dict(wait=wait, group=group)
        else:
            if group is not None:
                raise ValueError("an unmanaged transfer joins no group")
            common = dict(wait=wait, managed=False)
        # A per-call size lands in one descriptor's length, a repeat count in
        # its push; an offset patches every split piece.
        per_call = length_parameter is not None or repeat_parameter is not None
        if per_call and not buffer.fits(tap):
            raise ValueError(
                f"{type(self.op).__name__}.{buffer.name}: {tap} moves by a per-call "
                f"size, so it must fit one buffer descriptor, and does not"
            )
        dynamic = any(
            v is not None and v.ssa is not None
            for v in (offset_parameter, length_parameter, repeat_parameter)
        )
        if not dynamic:
            task = fn(
                data,
                tap=tap,
                offset_parameter=(
                    None if offset_parameter is None else offset_parameter.param
                ),
                length_parameter=(
                    None if length_parameter is None else length_parameter.param
                ),
                length_unit=None if length_parameter is None else length_unit,
                repeat_parameter=(
                    None if repeat_parameter is None else repeat_parameter.param
                ),
                **common,
            )
            if pinned and managed:
                queue.append(task)
            return task
        if dim is not None:
            # A unit dimension's stride is normalised to 0, which a dynamic
            # size may not have; its count never passes 1, so the stride the
            # next block would have moves the same bytes.
            if sizes[dim] == 1 and strides[dim] == 0:
                inner = zip(sizes[dim + 1 :], strides[dim + 1 :])
                strides[dim] = max(n * stride for n, stride in inner)
            sizes[dim] = length_parameter.ssa
            if scale > 1:
                sizes[dim] = arith.muli(
                    length_parameter.ssa,
                    arith.constant(scale, IntegerType.get_signless(32)),
                )
        if repeat_parameter is not None:
            sizes[0] = repeat_parameter.ssa + arith.constant(
                1, IntegerType.get_signless(32)
            )
        offset: Any = tap.offset
        if offset_parameter is not None and offset_parameter.ssa is not None:
            offset = offset_parameter.ssa
            if tap.offset:
                offset = offset + arith.constant(
                    int(tap.offset), IntegerType.get_signless(32)
                )
        task = fn(
            data,
            tap=TensorAccessPattern(tap.tensor_dims, offset, sizes, strides),
            **common,
        )
        if pinned and managed:
            queue.append(task)
        return task

    def data(self, buffer: Operand):
        return self._tensors[buffer.name]

    def preamble(self, **values) -> None:
        """Each core's runtime parameters, then the parameter sync, then each
        core's barrier, before any DMA. A shipped image's parameter blocks
        (its ``buffers``) each hold the residents' words in declaration
        order; its sequence releases them.

        An ``own_preamble`` operator's sequence calls it itself, ``values``
        overriding residents by name.

        Raises:
            ValueError: ``values`` names no resident of the operator, or a
                parameter block holds another number of words.
        """
        op = self.op
        residents = op.residents
        unknown = set(values) - set(residents)
        if unknown:
            raise ValueError(
                f"{type(op).__name__} has no resident {sorted(unknown)} to override"
            )
        # Without a scratchpad, a per-call word a core reads is the dispatch-time scalar.
        words = {v.name: v.ssa for v in op.values if not v.in_scratchpad}
        words.update(residents, **values)
        for rtp in self.built.rtps:
            rtp.write(words)
        block = []
        for word in (words[name] for name in residents):
            block += word if isinstance(word, (list, tuple)) else [word]
        for buffer in self.buffers if op.external is not None else ():
            if len(block) != prod(buffer.shape):
                raise ValueError(
                    f"{type(op).__name__}'s parameter block holds "
                    f"{prod(buffer.shape)} words; its residents are {len(block)}"
                )
            for i, word in enumerate(block):
                buffer[i] = word
        if any(value.in_scratchpad for value in op.values):
            sync_parameters()
        for rtp in self.built.rtps:
            rtp.barrier.set(1)


class MergedRuntime(Runtime):
    """Operator runtimes run back to back as one sequence
    (``Runtime.merge``), declaring each array's pins and buffers once.
    """

    runtimes: list[OperatorRuntime]

    @classmethod
    def merge(cls, runtimes, name=None) -> MergedRuntime:
        merged = super().merge(runtimes, name)
        merged.runtimes = list(runtimes)
        return merged

    def resolve(self, loc=None, ip=None, *, device=None, **options) -> None:
        # Steps of one design share its array: one runtime declares it.
        for runtime in {id(r.op): r for r in self.runtimes}.values():
            runtime.declare(device)
        super().resolve(loc, ip, device=device, **options)
