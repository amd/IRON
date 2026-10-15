# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The runtime sequence of one operator, as aie.iron's ``Runtime``."""

from __future__ import annotations

import functools
from math import prod
from typing import Any

import numpy as np
from aie.dialects.aie import AIETileType, shim_dma_allocation
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

from ..declare import DispatchTime, Operator, Value
from ..declare.operand import Operand
from ..declare.value import PlaceWord
from .bd import BdLimits


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
        built: What its ``array()`` returned: its workers, and the flows,
            locks, tile DMAs, pinned endpoints and buffers only the sequence
            reaches.
        name: The sequence's symbol; the Program names it when None.

    Attributes:
        pins: Each pinned lane this runtime declares, by its symbol.
        buffers: Buffers no worker places, declared whatever a shape's
            sequence reaches: a shipped image's parameter blocks, or a
            pool only descriptors address.
    """

    def __init__(self, op: Operator, built: list = (), name: str | None = None) -> None:
        self.op = op
        self.buffers = [b for b in built if isinstance(b, Buffer)]
        self._tensors: dict[str, Any] = {}
        self._queues: dict[str, list[Task]] = {}
        # Raises if any stream of a built array is unbound.
        lanes = [
            (b, i, h) for b in op.buffers if b.streamed for i, h in enumerate(b.handles)
        ]
        # A shared array's pins are declared by the runtime of the array that built them.
        ours = {id(e) for e in built if isinstance(e, DmaEndpoint)}
        self.pins = {f"{b.name}_{i}": h for b, i, h in lanes if id(h) in ours}
        if len(self.pins) != len(ours):
            raise TypeError(
                f"{type(op).__name__}.array() returns a DmaEndpoint no operand "
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
        for obj in built:
            if isinstance(obj, (Flow, PacketFlow)):
                self.add_flow(obj)
            elif isinstance(obj, Lock):
                self.add_lock(obj)
            elif isinstance(obj, TileDma):
                self.add_tile_dma(obj)
            elif not isinstance(obj, (Worker, DmaEndpoint, Buffer)):
                raise TypeError(
                    f"{type(op).__name__}.array() returns Workers, Flows, "
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
        for b in buffers:
            b.runtime = self
        for value, arg in zip(self.op.values, args[len(buffers) + 1 :]):
            if not value.in_scratchpad:
                value.ssa = arg
        if not self.op.own_preamble:
            self.preamble()
        self.run()
        for queue in self._queues.values():
            for task in queue:
                task.await_()

    def resolve(self, loc=None, ip=None, *, device=None, **options) -> None:
        # aie.iron names a shim channel through the route it starts or ends,
        # and places a buffer through the worker that reads it; these have
        # neither, so they are declared at device scope ahead of the sequence.
        for symbol, end in self.pins.items():
            device.resolve_tile(end.tile)
            shim_dma_allocation(symbol, end.tile.op, end.direction, end.channel)
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
                continue  # filled into the stream it prepares or rides (transfer)
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
        finishing: TensorAccessPattern | None = None,
    ):
        """``operand.fill``/``operand.drain`` (``verb``): see ``Operand.fill``."""
        if lane is None:
            if operand.count != 1:
                raise ValueError(f"{operand.name} is per-{operand.count}; name a lane")
            lane = 0
        buffer = operand if source is None else source
        tap = buffer.tap if tap is None else tap
        per_call = (offset_parameter, length_parameter, repeat_parameter)
        riding = [e for e in self.op.finish_inputs if not e.streamed]
        if verb == "fill" and operand.feed and riding and buffer is operand:
            name = f"{type(self.op).__name__}.{buffer.name}"
            if any(v is not None for v in per_call):
                raise ValueError(
                    f"{name}: the finish's inputs ride it an output tile at a "
                    f"time, so it moves by no per-call offset or size"
                )
            if finishing is None and tap != buffer.transfers()[lane][1]:
                raise ValueError(
                    f"{name}: the finish's inputs ride it an output tile at a "
                    f"time, so a fill of lane {lane} is its whole share"
                )
            (out,) = self.op.outputs
            line = prod(out.obj_shape)
            share = finishing or out.transfers()[lane][1]
            tiles = prod(share.sizes) // line
            reads = prod(buffer.obj_shape) // line
            task = None
            for held, finished in zip(
                self._chunks(tap, tiles), self._chunks(share, tiles)
            ):
                task = self._emit(
                    verb, operand, lane, buffer, held, group, wait, managed
                )
                for e in riding:
                    self._emit(
                        verb,
                        operand,
                        lane,
                        e,
                        finished.repeat(reads),
                        group,
                        wait,
                        managed,
                    )
            return task
        task = self._emit(
            verb,
            operand,
            lane,
            buffer,
            tap,
            group,
            wait,
            managed,
            offset_parameter,
            length_parameter,
            length_unit,
            repeat_parameter,
        )
        if verb == "fill" and operand.prepare:
            for extra in self.op.prepare_inputs:
                self._emit(verb, operand, lane, extra, extra.tap, group, wait, managed)
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

    def _emit(
        self,
        verb: str,
        operand: Operand,
        lane: int,
        buffer: Operand,
        tap: TensorAccessPattern,
        group,
        wait: bool,
        managed: bool,
        offset_parameter: Value | None = None,
        length_parameter: Value | None = None,
        length_unit: int | None = None,
        repeat_parameter: Value | None = None,
    ):
        """One transfer of ``buffer``'s ``tap`` through lane ``lane`` of
        ``operand``'s stream, its per-call words lowered for the image: a
        scratchpad parameter on a full ELF, the pattern's sizes and offset
        on an xclbin.
        """
        handle = operand.handles[lane]
        pinned = isinstance(handle, DmaEndpoint)
        symbol = f"{operand.name}_{lane}"
        fn = (
            functools.partial(emit_shim_transfer, symbol)
            if pinned
            else getattr(handle, verb)
        )
        placed = next(
            (
                v
                for v in self.op.values
                if isinstance(v, PlaceWord) and v.buffer == buffer.name
            ),
            None,
        )
        if placed is not None and offset_parameter is not None:
            raise ValueError(
                f"{type(self.op).__name__}.{buffer.name} is placed in a larger "
                f"buffer, {placed.name} moving its transfers; a transfer of it "
                f"takes no per-call offset of its own"
            )
        offset_parameter = placed or offset_parameter
        into, start = buffer.placement
        if (into, start) != (buffer.elements, 0):
            tap = TensorAccessPattern(
                (into,), tap.offset + start, tap.sizes, tap.strides
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
        if isinstance(length_parameter, DispatchTime):
            raise ValueError(
                f"{length_parameter.name} is a DispatchTime value; a per-call "
                f"length is a scratchpad word patched into the descriptor"
            )
        sizes, strides = BdLimits.slots(tap.sizes, tap.strides)
        dim = scale = None
        if length_parameter is not None:
            # A patched descriptor's length ends at its outermost dimension
            # below the iteration; an xclbin's stream, regenerated per call,
            # sizes any dimension of length_unit-element units.
            patched = length_parameter.ssa is None
            dim = next(
                (
                    d
                    for d in range(1, 4)
                    if (prod(sizes[1:d]) == 1 or not patched)
                    and prod(sizes[d + 1 :]) == length_unit
                ),
                None,
            )
            if dim is None and prod(sizes[1:3]) == 1 and sizes[3] % length_unit == 0:
                # One linear run, whose length counts its elements: units of them.
                dim, scale = 3, length_unit
            if dim is None:
                raise ValueError(
                    f"{type(self.op).__name__}.{buffer.name}: {tap} has no "
                    f"descriptor dimension of {length_unit}-element units"
                    + (" below the iteration, outermost" if patched else "")
                )
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
        if per_call and not BdLimits.of(self.op.dev, AIETileType.ShimNOCTile).fits(
            tap, buffer.dtype
        ):
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
            if scale is not None:
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
        for rtp in op.rtps:
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
        for rtp in op.rtps:
            rtp.barrier.set(1)
