# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The sequence for an image IRON did not build.

An operator declared with ``image=`` (:class:`~iron.common.declare.Xclbin`)
has no array to build: every core program, memtile buffer and stream-switch
route comes from the downloaded image. What the sequence must supply is the
other half of a dispatch, and the declaration carries everything it needs:
each operand's shim column and channel (``via=``), each value's address in
core data memory and the lock a core waits on before reading it. flm's
shipped ``mm`` binary is the one that does today.

Transfers are emitted as shim DMA tasks on the pinned allocations, at most
``depth`` outstanding per lane (the image's memtiles hold that many
objects, so a further transfer would overwrite one still in use). Task
groups have no meaning here and are accepted as no-ops, so an operator's
``sequence(rt)`` reads the same against a built or a shipped image.
"""

from __future__ import annotations

import hashlib
import urllib.request
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import numpy as np
from aie.dialects import aie, aiex
from aie.dialects.aie import (
    DMAChannelDir,
    get_target_model,  # pyright: ignore[reportAttributeAccessIssue]  # not in _aie.pyi
)
from aie.extras.context import mlir_mod_ctx
from aie.ir import BF16Type, F32Type, IntegerType, MemRefType
from aie.utils.compile import NPU_CACHE_HOME
from ml_dtypes import bfloat16

from .declare import Operator
from .declare.bound import BoundBuffer, BoundStream, _StreamSlot
from .design import Transfers
from .tiling import Access

# Core-tile lock registers, 16 bytes apart from this base. A hardware fact
# the Python bindings do not expose.
LOCK_ADDRESS_BASE = 0x1F000


class _NoGroup:
    def finish(self) -> None:
        pass


class ExternalSequence(Transfers):
    """What an operator's ``sequence(rt)`` receives against a shipped image.

    The same surface :class:`~iron.common.design.Sequence` offers, lowering a
    transfer to words for a downloaded image instead of MLIR tasks.
    """

    def __init__(self, op: Operator, rt_data: dict[str, Any], emit):
        self.op = op
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
                "per-call offsets are not supported on a shipped image"
            )
        key = self._key(stream)
        depth = self._depth(stream)
        buffer, accesses = self._resolve(what, stream)
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
    def _lane(stream) -> _StreamSlot | BoundStream:
        if isinstance(stream, BoundBuffer):
            stream = stream.lanes  # an operand that is its own stream
        if isinstance(stream, (_StreamSlot, BoundStream)):
            return stream
        raise TypeError(
            f"fill/drain take a stream, one lane of it, or an operand that is its "
            f"own stream, got {stream!r}"
        )

    def _key(self, stream) -> tuple[str, int]:
        lane = self._lane(stream)
        if isinstance(lane, _StreamSlot):
            return (lane.stream.name, lane.index)
        return (lane.name, 0)

    def _depth(self, stream) -> int:
        lane = self._lane(stream)
        s = lane.stream if isinstance(lane, _StreamSlot) else lane
        return s.member.depth

    def _resolve(self, what, stream) -> tuple[BoundBuffer, list[Access]]:
        if isinstance(what, Access):
            lane = self._lane(stream)
            s = lane.stream if isinstance(lane, _StreamSlot) else lane
            if s.buffer is None:
                raise TypeError(
                    f"an Access alone names no buffer; {stream!r} is not an "
                    f"operand's own stream, so give (buffer, Access)"
                )
            return s.buffer, [what]
        if isinstance(what, BoundBuffer):
            n = what.elements
            return what, [Access(n, 0, (1, 1, 1, n), (0, 0, 0, 1))]
        if isinstance(what, tuple) and len(what) == 2 and isinstance(what[1], Access):
            return what[0], [what[1]]
        raise TypeError(
            f"an external sequence takes a buffer, an Access on an operand's own "
            f"stream, or (buffer, Access); got {what!r}"
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


def write_residents(op: Operator, core_tiles, emit) -> None:
    """Write every resident value's words into every core, then release the locks.

    A value may be one word or a sequence of words written at consecutive
    addresses. All writes precede the first lock release, so no core reads
    a half-written buffer.
    """
    values = op.resident_values()
    residents = list(op.residents.values())
    for res in residents:
        if res.name not in values:
            raise ValueError(
                f"{type(op).__name__}.resident_values() does not supply {res.name}"
            )
    unknown = set(values) - {r.name for r in residents}
    if unknown:
        raise ValueError(
            f"{type(op).__name__}.resident_values() names {sorted(unknown)}, which "
            f"{type(op).__name__} does not declare"
        )
    for col, row in core_tiles:
        for res in residents:
            words = values[res.name]
            if isinstance(words, (int, np.integer)):
                words = [words]
            assert res.address is not None, "a value written into a shipped image"
            for i, word in enumerate(words):
                emit.write32(res.address + 4 * i, int(word), col, row)
    for col, row in core_tiles:
        for res in residents:
            if res.lock is not None:
                emit.write32(LOCK_ADDRESS_BASE + 16 * res.lock, 1, col, row)


def run_sequence(op: Operator, rt_data, core_tiles, emit) -> None:
    """The values, then the operator's sequence, then the trailing awaits."""
    write_residents(op, core_tiles, emit)
    seq = ExternalSequence(op, rt_data, emit)
    seq.run()
    seq.finish()


# --------------------------------------------------------------------------
# The MLIR module
# --------------------------------------------------------------------------


def _elem_type(dtype):
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
        aiex.npu_write32(address, value, column=col, row=row)

    def start(self, key, buffer, offset, sizes, strides):
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
        aiex.dma_await_task(task)


def fetch(image, directory=None) -> Path:
    """The downloaded image, by digest: fetched unless a file of the pinned
    content is already there.

    Into the JIT cache's own root by default (``NPU_CACHE_HOME``'s
    ``prebuilt/``), so an external image is found where every other built
    artifact is and no caller has to name a directory for it.
    """
    if directory is None:
        directory = Path(NPU_CACHE_HOME) / "prebuilt"
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


def build_external(dev, op: Operator):
    """The module whose runtime sequence drives ``op``'s downloaded image."""
    tm = get_target_model(dev.resolve())
    core_tiles = [
        (col, row)
        for row in range(1 + tm.get_num_mem_tile_rows(), tm.rows())
        for col in range(dev.cols)
    ]
    buffers = op.buffers

    with mlir_mod_ctx() as ctx:
        types = [MemRefType.get((b.elements,), _elem_type(b.dtype)) for b in buffers]

        npu: Any = dev.resolve()  # Device.resolve() is annotated -> None upstream

        # region_op annotates its decorator as the op it builds; a checker sees the
        # decorated function as not callable.
        @aie.device(npu)  # pyright: ignore[reportCallIssue]
        def device_body():
            shim: dict[int, Any] = {}
            allocations: dict[tuple[str, int], str] = {}
            for s in op.streams.values():
                for i in range(s.count):
                    pin = s.pin(i)
                    if pin is None or pin.channel is None:
                        raise ValueError(
                            f"{type(op).__name__}.{s.name}[{i}] has no (column, "
                            f"channel) pin; a shipped image's streams need one"
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
                run_sequence(op, rt_data, core_tiles, _MLIREmitter(allocations))

        return ctx.module
