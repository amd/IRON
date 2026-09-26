# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Transfers and Sequence: the runtime sequence of one operator.

:class:`Transfers` decides what goes through a sequence; :class:`Sequence`
lowers each transfer to MLIR tasks. The same base serves
:class:`~iron.common.external.ExternalSequence`, which emits words instead.
"""

from __future__ import annotations

import inspect
from contextlib import contextmanager
from math import prod
from typing import Any

from aie.extras.dialects import arith
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
from ..tiling import (
    Access,
    _pack_exact,
    encode,
    granule_elements,
    legalize,
    split,
    split_run,
    whole,
)
from .target import Target


class Transfers:
    """What an operator's sequence issues, over either way of issuing it.

    A concrete sequence supplies ``op`` and the ``fill``/``drain``/``group``
    surface; this decides what goes through it: the operator's
    ``sequence(rt)`` override, or the one derived from the declarations.
    :class:`Sequence` lowers a transfer to MLIR tasks;
    :class:`~iron.common.external.ExternalSequence` emits it as words for a
    downloaded image.
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
                for slot, acc, size_by in self.plan(buf):
                    self.fill(slot, (buf, acc), group=tg, size_by=size_by)
            for buf in self.op.outputs:
                for slot, acc, size_by in self.plan(buf):
                    self.drain(slot, (buf, acc), group=tg, wait=True, size_by=size_by)

    def plan(self, buf: BoundBuffer) -> list[tuple[Any, Access, dict | None]]:
        """The derived transfers of one operand, ``(slot, access, size_by)``
        each: the declared split across its lanes, or the round-robin one
        with its patched dimension under a bound. An override that keeps the
        derived movement for some operands issues them from here.
        """
        stream = self._stream_of(buf)
        bounded = buf.bounded
        if bounded is None:
            return [
                (slot, acc, None)
                for slot, accesses in transfers(buf, stream)
                for acc in accesses
            ]
        extent, axis, word = bounded
        if axis != buf.batch_axes:
            raise ValueError(
                f"{type(self.op).__name__}.{buf.name}: {extent.name} bounds axis "
                f"{axis}, but the derived sequence splits axis {buf.batch_axes}; "
                f"override sequence(rt) to bound another axis"
            )
        return [
            (slot, acc, {dim: word})
            for slot, acc, dim in bounded_transfers(buf, stream, axis)
        ]

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
    a buffer or a slice of one (``op.A``, ``op.A[:, r0:r1, :]``), turn the
    slice into legal descriptors, and issue them in order. Transfers are
    enrolled in the current group; ``group()`` opens one and finishes it on
    exit.
    """

    def __init__(self, op: Operator, rt_data: dict[str, Any]):
        self.op = op
        self._rt_data = rt_data
        self._group = None
        # The shim handles this sequence issued a transfer on; the build
        # places the declared ones it did not touch (see build_design).
        self.used: set = set()

    # -- transfers ---------------------------------------------------------

    def fill(
        self, stream, source, *, group=None, wait=False, offset_by=None, size_by=None
    ):
        """Fill ``stream`` from ``source``. ``offset_by`` moves the transfer's
        base address by a per-call value; ``size_by`` (``{dim: value}``)
        patches the descriptor's size on those dimensions per call, the
        outermost being 0. Both take scratchpad-kind values.
        """
        return self._transfer("fill", stream, source, group, wait, offset_by, size_by)

    def drain(
        self, stream, dest, *, group=None, wait=True, offset_by=None, size_by=None
    ):
        """Drain ``stream`` into ``dest``; see :meth:`fill` for the per-call forms."""
        return self._transfer("drain", stream, dest, group, wait, offset_by, size_by)

    def _transfer(
        self, verb: str, stream, what, group, wait: bool, offset_by=None, size_by=None
    ):
        handle = self._handle(stream)
        self.used.add(id(handle))
        buffer, accesses, sliced_by = self._resolve(what, stream)
        offset_by = offset_by or sliced_by
        if offset_by is not None and offset_by.param is None:
            raise ValueError(
                f"{offset_by.name} has no device parameter: the operator does not use "
                f"it (uses_value) or the build has not created it yet"
            )
        sizes_by = self._sizes_by(size_by)
        data = self._rt_data[buffer.name]
        dynamic = offset_by is not None and offset_by.ssa is not None
        dynamic = dynamic or any(v.ssa is not None for v in sizes_by.values())
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
                # The dispatch-time form: the same pattern with the per-call
                # scalars in place of the constants, regenerated per call.
                if not isinstance(acc, Access):
                    raise TypeError(
                        f"a dispatch-time offset or size needs an Access, got {acc!r}"
                    )
                sizes: list[Any] = list(acc.sizes)
                for dim, value in sizes_by.items():
                    sizes[dim] = value.ssa
                offset = (
                    _plus(offset_by.ssa, acc.offset)
                    if offset_by is not None and offset_by.ssa is not None
                    else acc.offset
                )
                tasks.append(
                    fn(
                        data,
                        sizes=sizes,
                        strides=list(acc.strides),
                        offset=offset,
                        transfer_len=acc.count,
                        **common,
                    )
                )
            else:
                patched = {}
                if sizes_by:
                    if not isinstance(acc, Access):
                        raise TypeError(f"a per-call size needs an Access, got {acc!r}")
                    if "size_parameters" not in inspect.signature(fn).parameters:
                        raise NotImplementedError(
                            f"{type(self.op).__name__}: a per-call size on a full ELF "
                            f"needs mlir-aie's size-kind scratchpad parameter "
                            f"(fill/drain(size_parameters={{dim: param}})), which this "
                            f"toolchain does not have (LENGTH_FREE_PLAN.md)"
                        )
                    patched["size_parameters"] = {
                        dim: value.param for dim, value in sizes_by.items()
                    }
                tasks.append(
                    fn(
                        data,
                        acc.tap() if isinstance(acc, Access) else acc,
                        offset_parameter=offset_parameter,
                        **patched,
                        **common,
                    )
                )
        return tasks[-1] if len(tasks) == 1 else tasks

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
    ) -> tuple[BoundBuffer, list[Access], BoundValue | None]:
        if not isinstance(what, (BoundBuffer, BufferView, tuple)):
            # A descriptor alone: the buffer is the one the stream belongs to.
            buffer = stream if isinstance(stream, BoundBuffer) else _buffer_of(stream)
            if buffer is None:
                raise TypeError(
                    f"{what!r} alone names no buffer; {stream!r} is not an "
                    f"operand's own stream, so give (buffer, descriptor)"
                )
            what = (buffer, what)
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

    def data(self, buffer: BoundBuffer):
        """The runtime-sequence argument for ``buffer`` (for hand-rolled transfers)."""
        return self._rt_data[buffer.name]

    def preamble(self, target: Target) -> None:
        """Residents, then barriers, then the parameter sync, before any DMA."""
        op = self.op
        values = op.resident_values()
        writes: dict[int, tuple] = {}  # id(buffer) -> (buffer, {index: value})
        for name, res in op.residents.items():
            if res.optional and not res.targets:
                continue  # this configuration does not allocate it
            if name not in values:
                raise ValueError(
                    f"{type(op).__name__}.resident_values() does not supply {name}"
                )
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
        unknown = set(values) - set(op.residents)
        if unknown:
            raise ValueError(
                f"{type(op).__name__}.resident_values() names {sorted(unknown)}, which "
                f"{type(op).__name__} does not declare"
            )
        for b in target.barriers:
            b.set(1)
        if target.image == "elf" and op.values:
            sync_parameters()


def transfers(
    buffer: BoundBuffer, stream: BoundStream
) -> list[tuple[Any, list[Access]]]:
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


def extent_unit(buffer: BoundBuffer, axis: int) -> int:
    """The rows along ``axis`` one round-robin unit of ``buffer`` holds: what
    the operator says (``extent_unit``), else the stream tile's rows there.
    """
    unit = buffer._op.extent_unit(buffer.name)
    if unit is not None:
        return unit
    tile_shape = buffer.lanes.shape if buffer.lanes is not None else ()
    k = axis - (len(buffer.shape) - len(tile_shape))
    return tile_shape[k] if k >= 0 else 1


def bounded_transfers(
    buffer: BoundBuffer, stream: BoundStream, axis: int
) -> list[tuple[Any, Access, int]]:
    """How ``buffer`` moves through ``stream`` when ``axis`` is bounded per
    call: ``[(slot, access, dim), ...]``, ``dim`` the descriptor dimension a
    call patches with the tiles per lane.

    The tiles along ``axis`` go round-robin over the lanes: lane ``k`` takes
    tiles ``k, k + lanes, k + 2*lanes, ...``, so every lane has one fixed
    offset, one fixed stride and the one patched count. Axes before it are
    repeats. The descriptor is built for the full extent; a call shortens it.
    """
    shape, dtype = buffer.shape, buffer.dtype
    lanes = 1 if stream.replicate else stream.count
    inner = prod(shape[axis + 1 :]) if axis + 1 < len(shape) else 1
    tile_rows = extent_unit(buffer, axis)
    if shape[axis] % (lanes * tile_rows):
        raise ValueError(
            f"{buffer.name} {shape}: axis {axis} does not divide into {tile_rows}-row "
            f"tiles over {lanes} lanes"
        )
    tiles = shape[axis] // (lanes * tile_rows)
    run = tile_rows * inner
    leading = [(shape[i], prod(shape[i + 1 :])) for i in range(axis)]
    gran = granule_elements(dtype)
    halves = split_run(run, gran)
    if halves is None:
        raise ValueError(
            f"{buffer.name}: a {run}-element tile does not fit one descriptor"
        )
    hi, lo = halves
    run_dims = ([(hi, lo)] if hi != 1 else [(1, 0)]) + [(lo, 1)]
    dims = leading + [(tiles, lanes * run)] + run_dims
    if len(dims) > 4:
        raise ValueError(
            f"{buffer.name} {shape}: bounding axis {axis} needs {len(dims)} "
            f"descriptor dimensions; a descriptor has four"
        )
    dim = 4 - len(run_dims) - 1  # where the tile count lands once padded to four
    out = []
    for lane in range(lanes):
        acc = _pack_exact(buffer.elements, lane * run, dims, gran)
        if acc is None:
            raise ValueError(
                f"{buffer.name} {shape}: the round-robin split over {lanes} lanes "
                f"does not fit one descriptor per lane"
            )
        slots = range(stream.count) if stream.replicate else [lane]
        for s in slots:
            out.append((stream[s] if stream.count > 1 else stream, acc, dim))
    return out


def _buffer_of(stream) -> BoundBuffer | None:
    """The operand a stream or one of its lanes is the own stream of."""
    if isinstance(stream, _StreamSlot):
        stream = stream.stream
    return stream.buffer if isinstance(stream, BoundStream) else None


def _plus(ssa, constant: int):
    """``ssa + constant`` as a sequence value; the scalar alone when constant is 0."""
    if not constant:
        return ssa
    return ssa + arith.constant(int(constant), IntegerType.get_signless(32))
