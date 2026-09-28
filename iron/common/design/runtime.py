# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Transfers and Sequence: the runtime sequence of one operator.

:class:`Transfers` decides what goes through a sequence; :class:`Sequence`
lowers each transfer to MLIR tasks. The same base serves
:class:`~iron.common.design.external.ExternalSequence`, which emits words instead.
"""

from __future__ import annotations

from contextlib import contextmanager
from math import prod
from typing import Any

import aie.utils as aie_utils
from aie.extras.dialects import arith
from aie.helpers.taplib import BdLimits, TensorAccessPattern
from aie.ir import IntegerType
from aie.iron import TaskGroup, sync_parameters

from ..declare import Operator
from ..declare.bound import (
    BoundBuffer,
    BoundStream,
    BoundValue,
    BufferView,
    _StreamSlot,
)
from .target import Target


class Transfers:
    """What an operator's sequence issues, over either way of issuing it.

    A concrete sequence supplies ``op`` and the ``fill``/``drain``/``group``
    surface; this decides what goes through it: the operator's
    ``sequence(rt)`` override, or the one derived from the declarations.
    :class:`Sequence` lowers a transfer to MLIR tasks;
    :class:`~.external.ExternalSequence` as shim DMA tasks on a downloaded
    image's pinned channels.

    A transfer is a ``TensorAccessPattern`` over the flat buffer. A constant
    one is issued as it is: the compiler splits one a buffer descriptor
    cannot hold (``aie-decompose-large-dma-bd``). One patched per call must
    fit a descriptor as given, so it is built to (``BdLimits``).
    """

    op: Operator

    def fill(
        self, stream, source, *, group=None, wait=False, offset_by=None, size_by=None
    ):
        raise NotImplementedError

    def drain(
        self, stream, dest, *, group=None, wait=True, offset_by=None, size_by=None
    ):
        raise NotImplementedError

    def group(self):
        raise NotImplementedError

    def run(self) -> None:
        """The transfers: the operator's override, else the one derived from
        the declarations.
        """
        if self.op.has_sequence_override():
            self.op.sequence(self)
        else:
            self._derived()

    def _derived(self) -> None:
        with self.group() as tg:
            for buf in self.op.inputs:
                for slot, tap, size_by in self.plan(buf):
                    self.fill(slot, (buf, tap), group=tg, size_by=size_by)
            for buf in self.op.outputs:
                for slot, tap, size_by in self.plan(buf):
                    self.drain(slot, (buf, tap), group=tg, wait=True, size_by=size_by)

    def plan(
        self, buf: BoundBuffer
    ) -> list[tuple[Any, TensorAccessPattern, dict | None]]:
        """The derived transfers of one operand, ``(slot, tap, size_by)``
        each: the declared split across its lanes, or the round-robin one
        with its patched dimension under a bound. An override that keeps the
        derived movement for some operands issues them from here.
        """
        stream = self._stream_of(buf)
        bounded = buf.bounded
        if bounded is None:
            return [(slot, tap, None) for slot, tap in self.split(buf, stream)]
        extent, axis, word = bounded
        if axis != buf.batch_axes:
            raise ValueError(
                f"{type(self.op).__name__}.{buf.name}: {extent.name} bounds axis "
                f"{axis}, but the derived sequence splits axis {buf.batch_axes}; "
                f"override sequence(rt) to bound another axis"
            )
        return [
            (slot, tap, {dim: word})
            for slot, tap, dim in self.round_robin(buf, stream, axis)
        ]

    @staticmethod
    def split(
        buffer: BoundBuffer, stream: BoundStream
    ) -> list[tuple[Any, TensorAccessPattern]]:
        """How ``buffer`` moves through ``stream``: ``[(slot, tap), ...]``.

        A single-slot or broadcast stream takes the whole buffer in one linear
        transfer. A ``per=`` stream splits the buffer's first non-batch axis
        across its slots, slot ``i`` taking the ``i``-th block of rows out of
        every leading index.
        """
        if stream.count == 1:
            return [(stream, buffer.tap)]
        if stream.replicate:
            return [(stream[i], buffer.tap) for i in range(stream.count)]
        shape, axis = buffer.shape, buffer.batch_axes
        if axis >= len(shape):
            raise ValueError(
                f"{buffer.name} {shape} has no axis to split across the "
                f"{stream.count} slots of stream {stream.name!r}"
            )
        share, remainder = divmod(shape[axis], stream.count)
        if remainder:
            raise ValueError(
                f"{buffer.name} {shape} does not divide across stream "
                f"{stream.name!r}: {shape[axis]} rows (axis {axis}) over "
                f"{stream.count} slots. Check {type(buffer._op).__name__}.compatible()"
            )
        leading = (slice(None),) * axis
        return [
            (
                stream[i],
                TensorAccessPattern.from_slice(
                    shape, leading + (slice(i * share, (i + 1) * share),)
                ),
            )
            for i in range(stream.count)
        ]

    @staticmethod
    def round_robin(
        buffer: BoundBuffer, stream: BoundStream, axis: int
    ) -> list[tuple[Any, TensorAccessPattern, int]]:
        """How ``buffer`` moves through ``stream`` when ``axis`` is bounded per
        call: ``[(slot, tap, dim), ...]``, ``dim`` the descriptor dimension a
        call patches with the tiles per lane.

        The tiles along ``axis`` go round-robin over the lanes: lane ``k`` takes
        tiles ``k, k + lanes, k + 2*lanes, ...``, so every lane has one fixed
        offset, one fixed stride and the one patched count, on D2. An axis
        before it iterates; a tile is a run split over D1 and D0. The
        descriptor is built for the full extent; a call shortens it.
        """
        shape, dtype = buffer.shape, buffer.dtype
        lanes = 1 if stream.replicate else stream.count
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
        shim = aie_utils.ensure_current_device(required=True).bd_limits(0, 0)
        halves = shim.factor(run, shim.granule(dtype))
        if halves is None:
            raise ValueError(
                f"{buffer.name}: a {run}-element tile does not fit one descriptor"
            )
        hi, lo = halves
        iterations, step = (shape[0], prod(shape[1:])) if axis else (1, 0)
        sizes = [iterations, tiles, hi, lo]
        strides = [step, lanes * run, lo, 1]
        out = []
        for lane in range(lanes):
            tap = TensorAccessPattern((buffer.elements,), lane * run, sizes, strides)
            if not shim.fits(tap, dtype):
                raise ValueError(
                    f"{buffer.name} {shape}: the round-robin split over {lanes} lanes "
                    f"does not fit one descriptor per lane"
                )
            slots = range(stream.count) if stream.replicate else [lane]
            for s in slots:
                out.append((stream[s] if stream.count > 1 else stream, tap, 1))
        return out

    def _stream_of(self, buf: BoundBuffer) -> BoundStream:
        if buf.lanes is None:
            raise ValueError(
                f"{type(self.op).__name__}.{buf.name} has no tile=, so its "
                f"sequence cannot be derived; add tile= or override sequence(rt)"
            )
        return buf.lanes


class Sequence(Transfers):
    """The runtime sequence of one operator, opened by the library.

    ``fill``/``drain`` take a stream (or one slot of a ``per=`` stream) and
    a buffer, a slice of one (``op.A``, ``op.A[:, r0:r1, :]``) or a
    ``TensorAccessPattern`` over it, and issue it as one transfer. Transfers
    are enrolled in the current group; ``group()`` opens one and finishes it
    on exit.
    """

    def __init__(
        self, op: Operator, rt_data: dict[str, Any], target: Target | None = None
    ):
        self.op = op
        self._rt_data = rt_data
        self.target = target
        self._group = None

    # -- transfers ---------------------------------------------------------

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
    ):
        """Fill ``stream`` from ``source``. ``offset_by`` moves the transfer's
        base address by a per-call value; ``size_by`` (``{dim: value}``)
        patches the descriptor's size on those dimensions per call, the
        outermost being 0. Both take scratchpad-kind values.

        ``managed=False`` hands the transfer's queue slot and descriptors to
        the compiler, which frees them once a later wait proves it done; it
        joins no group, and only a ``wait`` one returns a token.
        """
        return self._transfer(
            "fill", stream, source, group, wait, offset_by, size_by, managed
        )

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
        """Drain ``stream`` into ``dest``; see :meth:`fill` for the other forms."""
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
        fn = getattr(self._handle(stream), verb)
        buffer, tap, sliced_by = self._resolve(what, stream)
        offset_by = offset_by or sliced_by
        if offset_by is not None and offset_by.param is None:
            raise ValueError(
                f"{offset_by.name} has no device parameter: the operator does not use "
                f"it (uses_value) or the build has not created it yet"
            )
        sizes_by = self._sizes_by(size_by)
        data = self._rt_data[buffer.name]
        if managed:
            common = dict(wait=wait, group=group if group is not None else self._group)
        else:
            if group is not None:
                raise ValueError("an unmanaged transfer joins no group")
            common = dict(wait=wait, managed=False)
        # A per-call offset or size lands in one descriptor, so the pattern
        # must fit one: the compiler cannot split a descriptor a call patches.
        if (offset_by is not None or sizes_by) and not aie_utils.ensure_current_device(
            required=True
        ).bd_limits(0, 0).fits(tap, buffer.dtype):
            raise ValueError(
                f"{type(self.op).__name__}.{buffer.name}: {tap} moves by a per-call "
                f"offset or size, so it must fit one buffer descriptor, and does not"
            )
        dynamic = offset_by is not None and offset_by.ssa is not None
        dynamic = dynamic or any(v.ssa is not None for v in sizes_by.values())
        if not dynamic:
            return fn(
                data,
                tap=tap,
                offset_parameter=offset_by.param if offset_by is not None else None,
                size_parameters=(
                    {dim: value.param for dim, value in sizes_by.items()}
                    if sizes_by
                    else None
                ),
                **common,
            )
        # The dispatch-time form: the same pattern with the per-call scalars
        # in place of the constants, regenerated per call; the descriptor's
        # length is the product mlir-aie takes of them.
        sizes, strides = BdLimits.slots(tap.sizes, tap.strides)
        for dim, value in sizes_by.items():
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
            sizes=sizes,
            strides=strides,
            offset=offset,
            **common,
        )

    def _sizes_by(self, size_by) -> dict[int, BoundValue]:
        """The checked ``{dim: value}`` of a per-call size."""
        if not size_by:
            return {}
        out = {}
        for dim, value in size_by.items():
            if not isinstance(value, BoundValue):
                raise TypeError(
                    f"size_by takes a value member's word (op.value(name)), got "
                    f"{value!r} for dimension {dim}"
                )
            if value.kind != "scratchpad":
                raise ValueError(
                    f"{value.name} is {value.kind}; a per-call size is a scratchpad "
                    f"word patched into the descriptor"
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

    def _handle(self, stream):
        if isinstance(stream, BoundBuffer):
            stream = stream.lanes  # an operand that is its own stream
        if isinstance(stream, (_StreamSlot, BoundStream)):
            return stream.handle
        raise TypeError(
            f"fill/drain take a stream, one lane of it, or an operand that is its "
            f"own stream, got {stream!r}"
        )

    def _resolve(
        self, what, stream
    ) -> tuple[BoundBuffer, TensorAccessPattern, BoundValue | None]:
        """``(buffer, tap, offset_by)`` of what a transfer moves: a buffer, a
        slice of one, ``(buffer, tap)``, or a tap alone on an operand's own
        stream.
        """
        if isinstance(what, TensorAccessPattern):
            buffer = stream.stream if isinstance(stream, _StreamSlot) else stream
            if isinstance(buffer, BoundStream):
                buffer = buffer.buffer
            if not isinstance(buffer, BoundBuffer):
                raise TypeError(
                    f"{what!r} alone names no buffer; {stream!r} is not an "
                    f"operand's own stream, so give (buffer, tap)"
                )
            return buffer, what, None
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

    # -- structure ---------------------------------------------------------

    @contextmanager
    def group(self):
        """Open a task group; transfers issued inside join it; finished on exit."""
        tg = TaskGroup()
        previous, self._group = self._group, tg
        try:
            yield tg
        finally:
            self._group = previous
            tg.finish()

    def new_group(self):
        """A task group the caller finishes itself (for hand-rolled pipelines)."""
        return TaskGroup()

    def data(self, buffer: BoundBuffer):
        """The runtime-sequence argument for ``buffer`` (for hand-rolled transfers)."""
        return self._rt_data[buffer.name]

    def preamble(self, target: Target | None = None, **values) -> None:
        """Residents, then barriers, then the parameter sync, before any DMA.

        The build runs it ahead of the sequence unless the operator sets
        ``own_preamble``; such a sequence calls it itself, where and as often
        as it needs, and may override resident values by name for that
        writing (a slab of a larger dispatch, say).
        """
        op = self.op
        target = target or self.target
        if target is None:
            raise ValueError("preamble() needs the Target the array was built on")
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
        # One buffer at a time, its words in order: the order the hand-written
        # sequences wrote, so a converted operator's instruction stream matches.
        for buf, words in writes.values():
            for index in sorted(words):
                buf[index] = words[index]
        # A core-read value on an image without a scratchpad: written from the
        # sequence's per-call scalar, after the residents, before the barriers.
        for value in op.values:
            for buf, index in value.targets:
                if value.ssa is None:
                    raise ValueError(
                        f"{value.name} is bound to a runtime-parameter buffer but is "
                        f"not a dispatch-time scalar here; bind only under an image "
                        f"without a scratchpad (target.image != 'elf')"
                    )
                buf[index] = value.ssa
        for b in target.barriers:
            b.set(1)
        if target.image == "elf" and op.values:
            sync_parameters()
