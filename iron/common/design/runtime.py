# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The runtime sequence of one operator, as aie.iron's ``Runtime``."""

from __future__ import annotations

import functools
from collections.abc import Callable, Sequence
from math import prod
from typing import Any, cast

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
from ..declare.operand import Operand, active_runtime, concrete


class OperatorRuntime(Runtime):
    """The ``rt`` an operator's ``sequence(rt)`` receives.

    aie.iron's ``Runtime`` running the preamble, then that sequence or the
    one its declaration derives. A managed transfer on a pinned lane keeps
    at most the operand's ``depth`` in flight, all awaited at the
    sequence's end.

    Args:
        op: The resolved operator, its array built and its operands' lanes
            bound or pinned.
        name: The sequence's symbol; the Program names it when None.

    Attributes:
        built: What the operator's ``build()`` made, which ``sequence`` may read.
        pins: Each pinned lane this runtime declares, by its symbol.
        buffers: Buffers no worker places: a shipped image's parameter blocks,
            or a pool only descriptors address.
    """

    def __init__(self, op: Operator, built: Built, name: str | None = None) -> None:
        self.op = op
        self.built = built
        self.buffers = [b for b in built.objects if isinstance(b, Buffer)]
        self._tensors: dict[str, Any] = {}
        self._queues: dict[str, list[Task]] = {}
        self.group: TaskGroup | None = None
        # Raises if any stream of a built array is unbound. A stream kept
        # on-chip has no host end.
        lanes = [
            (b, i, h)
            for b in op.buffers
            if b.streamed and not b.on_chip
            for i, h in enumerate(b.handles)
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
                *(b.flat_type for b in self.host_buffers),
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

    @property
    def host_buffers(self) -> list[Operand]:
        """The operands the host passes: all but those kept on-chip."""
        return [b for b in self.op.buffers if not b.on_chip]

    def body(self, *args) -> None:
        """Record the sequence body, given the operator's runtime tensors, its lanes' handles.

        Then each per-call value not in the scratchpad as its scalar.
        """
        self.take(*args)
        token = active_runtime.set(self)
        try:
            if not self.op.own_preamble:
                self.preamble()
            self.run()
        finally:
            active_runtime.reset(token)
        self.await_queues()

    def take(self, *args) -> None:
        """Hold ``body``'s arguments: the host tensors and per-call scalars."""
        buffers = self.host_buffers
        self._tensors = {b.name: a for b, a in zip(buffers, args)}
        for value, arg in zip(self.op.values, args[len(buffers) + 1 :]):
            if not value.in_scratchpad:
                value.ssa = arg

    def await_queues(self) -> None:
        """Await every managed transfer still in flight."""
        for queue in self._queues.values():
            for task in queue:
                task.await_()

    def resolve(self, loc=None, ip=None, *, device=None, **options) -> None:
        self.declare(device)
        super().resolve(loc, ip, device=device, **options)

    def declare(self, device) -> None:
        """Its pins and buffers, at ``device`` scope ahead of the sequence.

        aie.iron names a shim channel by its route and places a buffer by
        the worker that reads it, and these have neither.
        """
        for symbol, end in self.pins.items():
            device.resolve_tile(end.tile)
            shim_dma_allocation(symbol, end.tile.op, end.direction, end.channel)
        for buffer in self.buffers:
            device.resolve_tile(buffer.tile)
            buffer.resolve()

    def task_group(self) -> TaskGroup:
        """Return the group a sequence issues transfers in.

        A fused sequence's own while it runs, else a new one.
        """
        return TaskGroup() if self.group is None else self.group

    def finish(self, tg: TaskGroup) -> None:
        """Finish ``tg``, unless it is a fused sequence's, finished once every operator in it has issued."""
        if tg is not self.group:
            tg.finish()

    def run(self) -> None:
        if self.op.has_sequence_override():
            self.op.sequence(self)
            return
        tg = self.task_group()
        self.issue(tg)
        self.finish(tg)

    def issue(self, tg: TaskGroup) -> None:
        """Fill every host input and drain every host output in ``tg``.

        The drains awaited when ``tg`` finishes; an on-chip operand's fill/drain emit
        nothing.
        """
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
        """``Operand.fill``/``drain`` (``verb``): ``source``'s (else ``operand``'s) ``tap``.

        Through ``lane`` of ``operand``'s stream, its per-call words a
        scratchpad parameter on a full ELF, the pattern's sizes and offset
        on an xclbin.
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
        # Read before a per-call size or repeat is patched in below, so still concrete.
        static_sizes, static_strides = concrete(sizes, tap), concrete(strides, tap)
        dim = scale = None
        if length_parameter is not None:
            assert length_unit is not None, "length_unit accompanies length_parameter"
            # A patched descriptor's length ends at its outermost dimension
            # below the iteration; an xclbin's stream, regenerated per call,
            # sizes any dimension of length_unit-element units.
            patched = length_parameter.ssa is None
            dim = next(
                (
                    d
                    for d in range(1, 4)
                    if (prod(static_sizes[1:d]) == 1 or not patched)
                    and prod(static_sizes[d + 1 :]) == length_unit
                ),
                None,
            )
            if (
                dim is None
                and prod(static_sizes[1:3]) == 1
                and static_sizes[3] % length_unit == 0
            ):
                # One linear run, whose length counts its elements: units of them.
                dim, scale = 3, length_unit
            if dim is None:
                raise ValueError(
                    f"{type(self.op).__name__}.{buffer.name}: {tap} has no "
                    f"descriptor dimension of {length_unit}-element units"
                    + (" below the iteration, outermost" if patched else "")
                )
        data = self._tensors[buffer.name]
        common: dict[str, Any]
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
            # dim is set only inside the length_parameter is not None branch above.
            assert length_parameter is not None
            # A unit dimension's stride is normalised to 0, which a dynamic
            # size may not have; its count never passes 1, so the stride the
            # next block would have moves the same bytes.
            if sizes[dim] == 1 and strides[dim] == 0:
                # dim's own size and stride are patched below, but nothing past
                # it, which stays concrete.
                inner = zip(static_sizes[dim + 1 :], static_strides[dim + 1 :])
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
                    concrete((tap.offset,), tap)[0], IntegerType.get_signless(32)
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
        """Write each core's runtime parameters, the parameter sync, then each core's barrier, before any DMA.

        A shipped image's parameter blocks (``buffers``) get the residents'
        words in declaration order, for its sequence to release. An
        ``own_preamble`` operator's sequence calls it, ``values`` overriding
        residents.

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
    """Operator runtimes run back to back as one sequence (``Runtime.merge``).

    Declaring each array's pins and buffers once.
    """

    runtimes: list[OperatorRuntime]

    @classmethod
    def merge(
        cls,
        runtimes: Sequence[Runtime],
        name: str | None = None,
        run: Callable[[Sequence[tuple[Runtime, tuple]]], None] | None = None,
    ) -> MergedRuntime:
        # Runtime.merge() builds cls(...), so this is really a MergedRuntime;
        # its own declared return type is the non-generic base.
        merged = cast(MergedRuntime, super().merge(runtimes, name, run))
        checked: list[OperatorRuntime] = []
        for runtime in runtimes:
            assert isinstance(
                runtime, OperatorRuntime
            ), "MergedRuntime merges OperatorRuntime steps"
            checked.append(runtime)
        merged.runtimes = checked
        return merged

    @classmethod
    def fuse(cls, runtimes, name=None) -> MergedRuntime:
        """Operator runtimes whose streams meet on-chip, as one sequence.

        Each runs its preamble, then all their transfers go in one task group that
        finishes once (``task_group``), since an operator's input completes only once a
        later operator drains.
        """

        def run(calls) -> None:
            for runtime, args in calls:
                runtime.take(*args)
                token = active_runtime.set(runtime)
                try:
                    if not runtime.op.own_preamble:
                        runtime.preamble()
                finally:
                    active_runtime.reset(token)
            tg = TaskGroup()
            for runtime, _ in calls:
                token = active_runtime.set(runtime)
                runtime.group = tg
                try:
                    runtime.run()
                finally:
                    runtime.group = None
                    active_runtime.reset(token)
            tg.finish()
            for runtime, _ in calls:
                runtime.await_queues()

        return cls.merge(runtimes, name, run)

    def resolve(self, loc=None, ip=None, *, device=None, **options) -> None:
        # Steps of one design share its array: one runtime declares it.
        for runtime in {id(r.op): r for r in self.runtimes}.values():
            runtime.declare(device)
        super().resolve(loc, ip, device=device, **options)
