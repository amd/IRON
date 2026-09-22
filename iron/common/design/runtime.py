# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Transfers and Sequence: the runtime sequence of one operator.

:class:`Transfers` decides what goes through a sequence; :class:`Sequence`
lowers each transfer to MLIR tasks. The same base serves
:class:`~iron.common.external.ExternalSequence`, which emits words instead.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Any

import numpy as np

from aie.extras.dialects import arith
from aie.helpers.util import np_dtype_to_mlir_type
from aie.iron import TaskGroup, sync_parameters

from ..declare import (
    BoundBuffer,
    BoundStream,
    BoundValue,
    BufferView,
    Operator,
    Overlay,
)
from ..declare.bound import _StreamSlot
from ..tiling import Access, encode, legalize, split, whole
from .target import Target


class Transfers:
    """What an operator's sequence issues, over either way of issuing it.

    A concrete sequence supplies ``op``, ``ov`` and the ``fill``/``drain``/
    ``group`` surface; this decides what goes through it -- the overlay's own
    sequence, the operator's ``design(rt)`` override, or the one derived from
    the declarations. :class:`Sequence` lowers a transfer to MLIR tasks;
    :class:`~iron.common.external.ExternalSequence` emits it as words for a
    downloaded image.
    """

    def run(self) -> None:
        """The transfers: the overlay's sequence when it owns one, else the
        operator's override, else the one derived from the declarations."""
        if self.ov.has_sequence():
            self.ov.sequence(self.op, self)
        elif self.op.has_design_override():
            self.op.design(self)
        else:
            self._derived()

    def _derived(self) -> None:
        with self.group() as tg:
            for buf in self.op.inputs:
                stream = buf.stream(self.ov)
                if stream is None:
                    raise ValueError(
                        f"{type(self.op).__name__}.{buf.name} names no stream (to=), so its "
                        f"sequence cannot be derived; add to= or override design(rt)"
                    )
                for slot, accesses in plan(buf, stream):
                    for acc in accesses:
                        self.fill(slot, (buf, acc), group=tg)
            for buf in self.op.outputs:
                stream = buf.stream(self.ov)
                if stream is None:
                    raise ValueError(
                        f"{type(self.op).__name__}.{buf.name} names no stream (from_=), so its "
                        f"sequence cannot be derived; add from_= or override design(rt)"
                    )
                for slot, accesses in plan(buf, stream):
                    for acc in accesses:
                        self.drain(slot, (buf, acc), group=tg, wait=True)


class Sequence(Transfers):
    """The runtime sequence of one operator, opened by the library.

    ``fill``/``drain`` take a stream (or one slot of a ``per=`` stream) and
    a buffer or a slice of one (``op.A``, ``op.A[:, r0:r1, :]``), turn the
    slice into legal descriptors, and issue them in order. Transfers are
    enrolled in the current group; ``group()`` opens one and finishes it on
    exit.
    """

    def __init__(self, op: Operator, ov: Overlay, rt_data: dict[str, Any]):
        self.op = op
        self.ov = ov
        self._rt_data = rt_data
        self._group = None
        # The shim handles this sequence issued a transfer on; the build
        # places the declared ones it did not touch (see build_design).
        self.used: set = set()

    # -- transfers ---------------------------------------------------------

    def fill(self, stream, source, *, group=None, wait: bool = False, offset_by=None):
        return self._transfer("fill", stream, source, group, wait, offset_by)

    def drain(self, stream, dest, *, group=None, wait: bool = True, offset_by=None):
        return self._transfer("drain", stream, dest, group, wait, offset_by)

    def _transfer(self, verb: str, stream, what, group, wait: bool, offset_by=None):
        handle = self._handle(stream)
        self.used.add(id(handle))
        buffer, accesses, sliced_by = self._resolve(what)
        offset_by = offset_by or sliced_by
        if offset_by is not None and offset_by.param is None:
            raise ValueError(
                f"{offset_by.name} has no device parameter: the operator does not use "
                f"it (uses_value) or the build has not created it yet"
            )
        data = self._rt_data[buffer.name]
        dynamic = offset_by is not None and offset_by.ssa is not None
        offset_parameter = (
            offset_by.param if offset_by is not None and not dynamic else None
        )
        tasks = []
        for i, acc in enumerate(accesses):
            last = i == len(accesses) - 1
            fn = getattr(handle, verb)
            common = dict(
                wait=wait and last,
                group=group if group is not None else self._group,
            )
            if dynamic:
                # The dispatch-time form: the same pattern, its offset the
                # per-call scalar plus the static one, regenerated per call.
                if not isinstance(acc, Access):
                    raise TypeError(
                        f"{offset_by.name}: a dispatch-time offset needs an Access, "
                        f"got {acc!r}"
                    )
                tasks.append(
                    fn(
                        data,
                        sizes=list(acc.sizes),
                        strides=list(acc.strides),
                        offset=_plus(offset_by.ssa, acc.offset),
                        transfer_len=acc.count,
                        **common,
                    )
                )
            else:
                tasks.append(
                    fn(
                        data,
                        acc.tap() if isinstance(acc, Access) else acc,
                        offset_parameter=offset_parameter,
                        **common,
                    )
                )
        return tasks[-1] if len(tasks) == 1 else tasks

    def _handle(self, stream):
        if isinstance(stream, _StreamSlot):
            return stream.handle
        if isinstance(stream, BoundStream):
            return stream.handle
        raise TypeError(f"fill/drain take a stream or a stream slot, got {stream!r}")

    def _resolve(self, what) -> tuple[BoundBuffer, list[Access], BoundValue | None]:
        if isinstance(what, BoundBuffer):
            return (
                what,
                [Access(what.elements, 0, (1, 1, 1, what.elements), (0, 0, 0, 1))],
                None,
            )
        if isinstance(what, BufferView):
            offset, sizes, strides = what.pattern()
            accesses = legalize(
                what.buffer.elements, offset, sizes, strides, what.buffer.dtype
            )
            return what.buffer, accesses, what.offset_by
        if (
            isinstance(what, tuple)
            and len(what) == 2
            and isinstance(what[0], BoundBuffer)
        ):
            buffer, acc = what
            if isinstance(acc, Access):
                return buffer, [acc], None
            if hasattr(acc, "sizes") and hasattr(acc, "strides"):
                # an upstream TensorAccessPattern (or a TensorTiler2D entry): pass it through
                return buffer, [acc], None
            raise TypeError(
                "(buffer, Access) or (buffer, TensorAccessPattern) expected"
            )
        raise TypeError(
            f"fill/drain take a buffer, a slice of one, or (buffer, Access); got {what!r}"
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

    def sync_parameters(self) -> None:
        sync_parameters()

    def data(self, buffer: BoundBuffer):
        """The runtime-sequence argument for ``buffer`` (for hand-rolled transfers)."""
        return self._rt_data[buffer.name]

    def preamble(self, target: Target) -> None:
        """Residents, then barriers, then the parameter sync, before any DMA."""
        values = self.ov.resident_values(self.op)
        writes: dict[int, tuple] = {}  # id(buffer) -> (buffer, {index: value})
        for name, res in self.ov.residents.items():
            if res.optional and not res.targets:
                continue  # this configuration does not allocate it
            if name not in values:
                raise ValueError(
                    f"{type(self.ov).__name__}.{name} is a Resident but "
                    f"{type(self.op).__name__}.residents() does not supply it"
                )
            if not res.targets:
                raise ValueError(
                    f"{type(self.ov).__name__}.{name}: design() never bound this Resident"
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
        for value in list(self.ov.values) + list(self.op.values):
            for buf, index in value.targets:
                if value.ssa is None:
                    raise ValueError(
                        f"{value.name} is bound to a runtime-parameter buffer but is "
                        f"not a dispatch-time scalar here; bind only under an image "
                        f"without a scratchpad (target.image != 'elf')"
                    )
                buf[index] = value.ssa
        unknown = set(values) - set(self.ov.residents)
        if unknown:
            raise ValueError(
                f"{type(self.op).__name__}.residents() names {sorted(unknown)}, which "
                f"{type(self.ov).__name__} does not declare"
            )
        for b in target.barriers:
            b.set(1)
        if target.image == "elf" and (self.op.values or self.ov.values):
            self.sync_parameters()


def plan(buffer: BoundBuffer, stream: BoundStream) -> list[tuple[Any, list[Access]]]:
    """How ``buffer`` moves through ``stream``: ``[(slot, [Access, ...]), ...]``.

    A single-slot or broadcast stream takes the whole buffer in one linear
    transfer. A ``per=`` stream splits the buffer's first non-batch axis
    across its slots; leading batch axes become repeats, coalesced into one
    iterated descriptor when the slot rules allow and unrolled otherwise.
    """
    if stream.count == 1:
        return [(stream, encode(whole(buffer.shape), buffer.elements, buffer.dtype))]
    if stream.replicate:
        everything = encode(whole(buffer.shape), buffer.elements, buffer.dtype)
        return [(stream[i], everything) for i in range(stream.count)]
    axis = buffer.batch_axes
    if axis >= len(buffer.shape):
        raise ValueError(
            f"{buffer.name} {buffer.shape} has no axis to split across the "
            f"{stream.count} slots of stream {stream.name!r}"
        )
    try:
        blocks = split(buffer.shape, stream.count, axis)
    except ValueError as e:
        raise ValueError(
            f"{buffer.name} {buffer.shape} does not divide across stream "
            f"{stream.name!r}: {e}. Check {type(buffer._op).__name__}.compatible()"
        ) from None
    return [(stream[b.slot], encode(b, buffer.elements, buffer.dtype)) for b in blocks]


def _plus(ssa, constant: int):
    """``ssa + constant`` as a sequence value; the scalar alone when constant is 0."""
    if not constant:
        return ssa
    return ssa + arith.constant(int(constant), np_dtype_to_mlir_type(np.int32))
