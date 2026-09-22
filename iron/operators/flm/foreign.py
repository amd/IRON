# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The sequence for an overlay IRON did not build.

:class:`Foreign` is the mixin a prebuilt overlay adds to answer the two
questions the library asks of an overlay it cannot design: where the image
file is (:meth:`Overlay.prebuilt`) and what module drives it
(:meth:`Overlay.build`). flm's shipped ``mm`` binary is the one such overlay
there is; the machinery lives here rather than in :mod:`iron.common` for
that reason.

A foreign overlay (:class:`~iron.common.declare.Xclbin` on the class) has no
``design()``: every core program, memtile buffer and stream-switch route
comes from the downloaded image. What the sequence must supply is the other
half of a dispatch, and the declaration carries everything it needs: each
stream slot's shim column and channel (``via=``), each resident's address
in core data memory and the lock a core waits on before reading it.

Transfers are emitted as shim DMA tasks on the pinned allocations, at most
``depth`` outstanding per slot (the image's memtiles hold that many
objects, so a further transfer would overwrite one still in use). Task
groups have no meaning here and are accepted as no-ops, so an operator's
``design(rt)`` reads the same against a built or a foreign overlay.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Any

import numpy as np
from ml_dtypes import bfloat16

from iron.common.declare import (
    BoundBuffer,
    BoundStream,
    Operator,
    Overlay,
    _StreamSlot,
)
from iron.common.tiling import Access

# Core-tile lock registers, 16 bytes apart from this base. A hardware fact
# the Python bindings do not expose.
LOCK_ADDRESS_BASE = 0x1F000


class _NoGroup:
    def finish(self) -> None:
        pass


class ForeignSequence:
    """What an operator's ``design(rt)`` receives against a foreign overlay."""

    def __init__(self, op: Operator, ov: Overlay, rt_data: dict[str, Any], emit):
        self.op = op
        self.ov = ov
        self._rt_data = rt_data
        self._emit = emit
        self._queues: dict[tuple[str, int], list] = {}

    # -- transfers ---------------------------------------------------------

    def fill(self, stream, source, *, group=None, wait=False, offset_by=None):
        self._transfer(stream, source, offset_by)

    def drain(self, stream, dest, *, group=None, wait=True, offset_by=None):
        self._transfer(stream, dest, offset_by)

    def _transfer(self, stream, what, offset_by) -> None:
        if offset_by is not None:
            raise NotImplementedError(
                "per-call offsets are not supported on a foreign overlay"
            )
        key = self._key(stream)
        depth = self._depth(stream)
        buffer, accesses = self._resolve(what)
        data = self._rt_data[buffer.name]
        queue = self._queues.setdefault(key, [])
        for acc in accesses:
            if len(queue) == depth:
                self._emit.await_(queue.pop(0))
            queue.append(
                self._emit.start(
                    key, data, acc.offset, list(acc.sizes), list(acc.strides)
                )
            )

    @staticmethod
    def _key(stream) -> tuple[str, int]:
        if isinstance(stream, _StreamSlot):
            return (stream.stream.name, stream.index)
        if isinstance(stream, BoundStream):
            return (stream.name, 0)
        raise TypeError(f"fill/drain take a stream or a stream slot, got {stream!r}")

    @staticmethod
    def _depth(stream) -> int:
        s = stream.stream if isinstance(stream, _StreamSlot) else stream
        return s.member.depth

    @staticmethod
    def _resolve(what) -> tuple[BoundBuffer, list[Access]]:
        if isinstance(what, BoundBuffer):
            n = what.elements
            return what, [Access(n, 0, (1, 1, 1, n), (0, 0, 0, 1))]
        if isinstance(what, tuple) and len(what) == 2 and isinstance(what[1], Access):
            return what[0], [what[1]]
        raise TypeError(
            f"a foreign sequence takes a buffer or (buffer, Access); got {what!r}"
        )

    def finish(self) -> None:
        """Await every outstanding transfer; the end of the sequence."""
        for queue in self._queues.values():
            for task in queue:
                self._emit.await_(task)
            queue.clear()

    # -- structure (no-ops: the queues above are the only ordering) ----------

    @contextmanager
    def group(self):
        yield _NoGroup()

    def new_group(self):
        return _NoGroup()

    def data(self, buffer: BoundBuffer):
        return self._rt_data[buffer.name]


def write_residents(op: Operator, ov: Overlay, core_tiles, emit) -> None:
    """Write every resident's words into every core, then release the locks.

    A resident's value may be one word or a sequence of words written at
    consecutive addresses. All writes precede the first lock release, so no
    core reads a half-written buffer.
    """
    values = ov.resident_values(op)
    residents = list(ov.residents.values())
    for res in residents:
        if res.name not in values:
            raise ValueError(
                f"{type(ov).__name__}.{res.name} is a Resident but "
                f"{type(op).__name__}.residents() does not supply it"
            )
    unknown = set(values) - {r.name for r in residents}
    if unknown:
        raise ValueError(
            f"{type(op).__name__}.residents() names {sorted(unknown)}, which "
            f"{type(ov).__name__} does not declare"
        )
    for col, row in core_tiles:
        for res in residents:
            words = values[res.name]
            if isinstance(words, (int, np.integer)):
                words = [words]
            for i, word in enumerate(words):
                emit.write32(res.address + 4 * i, int(word), col, row)
    for col, row in core_tiles:
        for res in residents:
            if res.lock is not None:
                emit.write32(LOCK_ADDRESS_BASE + 16 * res.lock, 1, col, row)


def run_sequence(op: Operator, ov: Overlay, rt_data, core_tiles, emit) -> None:
    """Residents, then the operator's sequence, then the trailing awaits."""
    from iron.common.build import run_design

    write_residents(op, ov, core_tiles, emit)
    seq = ForeignSequence(op, ov, rt_data, emit)
    run_design(op, ov, seq)
    seq.finish()


# --------------------------------------------------------------------------
# The MLIR module
# --------------------------------------------------------------------------


def _elem_type(dtype):
    from aie.ir import BF16Type, F32Type, IntegerType

    dt = np.dtype(dtype)
    if dtype is bfloat16 or dt == np.dtype(bfloat16):
        return BF16Type.get()
    if dt == np.float32:
        return F32Type.get()
    if dt.kind in "iu":
        return IntegerType.get_signless(dt.itemsize * 8)
    raise TypeError(f"no MLIR element type for {dt}")


class _MLIREmitter:
    def __init__(self, allocations: dict[tuple[str, int], str]) -> None:
        self._allocs = allocations

    def write32(self, address, value, col, row) -> None:
        from aie.dialects import aiex

        aiex.npu_write32(address, value, column=col, row=row)

    def start(self, key, buffer, offset, sizes, strides):
        from aie.dialects import aiex

        task = aiex.shim_dma_single_bd_task(
            self._allocs[key],
            buffer,
            offset=offset,
            sizes=sizes,
            strides=strides,
            issue_token=True,
        )
        aiex.dma_start_task(task)
        return task

    def await_(self, task) -> None:
        from aie.dialects import aiex

        aiex.dma_await_task(task)


def fetch(image, directory) -> Path:
    """The downloaded image, by digest: fetched into ``directory`` unless a
    file of the pinned content is already there."""
    import hashlib
    import urllib.request

    target = Path(directory) / image.filename

    def digest(path):
        with open(path, "rb") as f:
            return hashlib.file_digest(f, "sha256").hexdigest()

    if target.exists() and digest(target) == image.sha256:
        return target
    if not image.url.startswith("https://"):
        raise ValueError(f"refusing to download over {image.url!r}")
    target.parent.mkdir(parents=True, exist_ok=True)
    # Beside the target and renamed, so an interrupted fetch cannot leave a
    # truncated file that a later run reports as a digest mismatch.
    partial = target.with_suffix(target.suffix + ".part")
    with urllib.request.urlopen(image.url, timeout=60) as response:
        partial.write_bytes(response.read())
    if (got := digest(partial)) != image.sha256:
        partial.unlink()
        raise RuntimeError(f"{image.url} has SHA-256 {got}, expected {image.sha256}")
    partial.replace(target)
    return target


def build_foreign(dev, op: Operator):
    """The module whose runtime sequence drives ``op.ov``'s downloaded image."""
    from aie.dialects import aie, aiex
    from aie.dialects.aie import DMAChannelDir, get_target_model
    from aie.extras.context import mlir_mod_ctx
    from aie.ir import MemRefType

    ov = op.ov
    tm = get_target_model(dev.resolve())
    core_tiles = [
        (col, row)
        for row in range(1 + tm.get_num_mem_tile_rows(), tm.rows())
        for col in range(dev.cols)
    ]
    buffers = op.buffers

    with mlir_mod_ctx() as ctx:
        types = [MemRefType.get((b.elements,), _elem_type(b.dtype)) for b in buffers]

        @aie.device(dev.resolve())
        def device_body():
            shim: dict[int, Any] = {}
            allocations: dict[tuple[str, int], str] = {}
            for s in ov.streams.values():
                for i in range(s.count):
                    pin = s.pin(i)
                    if pin is None or pin.channel is None:
                        raise ValueError(
                            f"{type(ov).__name__}.{s.name}[{i}] has no (column, "
                            f"channel) pin; a foreign overlay's streams need one"
                        )
                    tile = shim.setdefault(pin.col, aie.tile(pin.col, 0))
                    name = f"{s.name}_{i}"
                    direction = (
                        DMAChannelDir.MM2S
                        if s.direction == "in"
                        else DMAChannelDir.S2MM
                    )
                    aie.shim_dma_allocation(name, tile, direction, pin.channel)
                    allocations[(s.name, i)] = name

            @aiex.runtime_sequence(*types)
            def sequence(*args):
                rt_data = {b.name: a for b, a in zip(buffers, args)}
                run_sequence(op, ov, rt_data, core_tiles, _MLIREmitter(allocations))

        return ctx.module


class Foreign:
    """An overlay whose image is downloaded rather than built.

    Mix in beside the operator's overlay base and declare an
    :class:`~iron.common.declare.Xclbin`; the two hooks the library asks for
    are answered here.
    """

    def prebuilt(self, directory) -> Path:
        return fetch(self.foreign, directory)

    def build(self, dev, op: Operator):
        return build_foreign(dev, op)
