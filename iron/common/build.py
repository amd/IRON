# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The library-owned build of a declared operator: Runtime, Program, and the sequence.

A declared :class:`~iron.common.declare.Operator` never constructs a
``Runtime`` or a ``Program``. :func:`build_design` does, from the
declaration: it tunes the overlay for the device, calls the overlay's
``design(target)`` to build the array and bind its streams, opens the runtime
sequence from the operator's buffers in declaration order, runs the
preamble (residents, barriers, parameter sync), then either derives the
fill/drain sequence from the buffer-to-stream bindings or hands a
:class:`Sequence` to the operator's ``design(rt)`` override.

``build_design`` is also the one design function every declared operator
compiles through, so the existing compile and fusion paths
(``compile_xclbin_insts``, ``fuse_mlir``) see nothing new: they call it with
the operator bound by name, exactly as they call ``my_matvec`` today.

Everything that touches mlir-aie is imported inside the functions that need
it, so the declaration layer stays importable without the toolchain.
"""

from __future__ import annotations

import hashlib
import inspect
from contextlib import contextmanager
from typing import Any

import numpy as np

from .compilation import DesignGenerator, PythonGeneratedMLIRArtifact
from .declare import (
    BoundBuffer,
    BoundStream,
    BoundValue,
    BufferView,
    Operator,
    Overlay,
    _StreamSlot,
)
from .tiling import Access, encode, legalize, split, whole

# --------------------------------------------------------------------------
# What an overlay's design() receives
# --------------------------------------------------------------------------


class Target:
    """The device and build context an overlay's ``design()`` is given.

    Carries what a design used to receive as loose parameters (``dev``,
    ``kernels_dir``, ``func_prefix``, ``verbose``) and applies the fusion
    prefix inside :meth:`kernel`, so an overlay never handles it.
    """

    def __init__(
        self,
        dev,
        kernels_dir,
        func_prefix: str = "",
        verbose: bool = False,
        trace_size: int = 0,
    ):
        from pathlib import Path

        from .device_utils import get_kernel_dir

        self.dev = dev
        self.kernels_dir = Path(kernels_dir)
        self.arch = get_kernel_dir(dev)  # "aie2" | "aie2p"
        self.func_prefix = func_prefix
        self.verbose = verbose
        self.trace_size = trace_size
        self.base_dir = None  # the IRON checkout; set by build_design from the context
        self.barriers: list[Any] = []

    def kernel_source(self, name: str):
        """``<kernels_dir>/<arch>/<name>.cc``: the per-architecture kernel tree."""
        return self.kernels_dir / self.arch / f"{name}.cc"

    def kernel(
        self,
        name: str,
        arg_types,
        *,
        source=None,
        compile_flags=(),
        bundled_sources=(),
        include_dirs=None,
        object_file_name=None,
        symbol_prefix=None,
        prebuilt=None,
    ):
        """Declare a kernel the array calls; the fusion prefix is applied here."""
        from iron.operators._kernels import declare_kernel

        return declare_kernel(
            name,
            arg_types,
            source=source,
            prebuilt=prebuilt,
            func_prefix=self.func_prefix,
            compile_flags=list(compile_flags),
            include_dirs=include_dirs,
            object_file_name=object_file_name,
            bundled_sources=bundled_sources,
            symbol_prefix=symbol_prefix,
        )

    def barrier(self, initial_value: int = 0):
        """A worker/runtime barrier the preamble sets to 1 after writing residents."""
        from aie.iron import WorkerRuntimeBarrier

        b = WorkerRuntimeBarrier(initial_value)
        self.barriers.append(b)
        return b

    def rtp(self, arr_type, name: str | None = None, initial_value=None):
        """A runtime-parameter buffer a core reads and the preamble writes."""
        from aie.iron import Buffer

        return Buffer(
            arr_type, name=name, initial_value=initial_value, use_write_rtp=True
        )

    def log(self, *args) -> None:
        if self.verbose:
            print(*args)


# --------------------------------------------------------------------------
# What an operator's design(rt) receives, and what the derivation uses
# --------------------------------------------------------------------------


class Sequence:
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

    # -- transfers ---------------------------------------------------------

    def fill(self, stream, source, *, group=None, wait: bool = False, offset_by=None):
        return self._transfer("fill", stream, source, group, wait, offset_by)

    def drain(self, stream, dest, *, group=None, wait: bool = True, offset_by=None):
        return self._transfer("drain", stream, dest, group, wait, offset_by)

    def _transfer(self, verb: str, stream, what, group, wait: bool, offset_by=None):
        handle = self._handle(stream)
        buffer, accesses, sliced_by = self._resolve(what)
        offset_by = offset_by or sliced_by
        if offset_by is not None and offset_by.param is None:
            raise ValueError(
                f"{offset_by.name} has no device parameter: the operator does not use "
                f"it (uses_value) or the build has not created it yet"
            )
        data = self._rt_data[buffer.name]
        offset_parameter = offset_by.param if offset_by is not None else None
        tasks = []
        for i, acc in enumerate(accesses):
            last = i == len(accesses) - 1
            fn = getattr(handle, verb)
            tasks.append(
                fn(
                    data,
                    acc.tap() if isinstance(acc, Access) else acc,
                    wait=wait and last,
                    group=group if group is not None else self._group,
                    offset_parameter=offset_parameter,
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
        from aie.iron import TaskGroup

        tg = TaskGroup()
        previous, self._group = self._group, tg
        try:
            yield tg
        finally:
            self._group = previous
            tg.finish()

    def new_group(self):
        """A task group the caller finishes itself (for hand-rolled pipelines)."""
        from aie.iron import TaskGroup

        return TaskGroup()

    def sync_parameters(self) -> None:
        from aie.iron import sync_parameters

        sync_parameters()

    def data(self, buffer: BoundBuffer):
        """The runtime-sequence argument for ``buffer`` (for hand-rolled transfers)."""
        return self._rt_data[buffer.name]


# --------------------------------------------------------------------------
# Deriving the sequence
# --------------------------------------------------------------------------


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


def _preamble(rt: Sequence, op: Operator, ov: Overlay, target: Target) -> None:
    """Residents, then barriers, then the parameter sync, before any DMA."""
    values = op.residents()
    for name, res in ov.residents.items():
        if res.optional and not res.targets:
            continue  # this configuration does not allocate it
        if name not in values:
            raise ValueError(
                f"{type(ov).__name__}.{name} is a Resident but "
                f"{type(op).__name__}.residents() does not supply it"
            )
        if not res.targets:
            raise ValueError(
                f"{type(ov).__name__}.{name}: design() never bound this Resident"
            )
        for buf, index in res.targets:
            buf[index] = values[name]
    unknown = set(values) - set(ov.residents)
    if unknown:
        raise ValueError(
            f"{type(op).__name__}.residents() names {sorted(unknown)}, which "
            f"{type(ov).__name__} does not declare"
        )
    for b in target.barriers:
        b.set(1)
    if op.values or ov.values:
        rt.sync_parameters()


def _derived(rt: Sequence, op: Operator, ov: Overlay) -> None:
    with rt.group() as tg:
        for buf in op.inputs:
            stream = buf.stream(ov)
            if stream is None:
                raise ValueError(
                    f"{type(op).__name__}.{buf.name} names no stream (to=), so its "
                    f"sequence cannot be derived; add to= or override design(rt)"
                )
            for slot, accesses in plan(buf, stream):
                for acc in accesses:
                    rt.fill(slot, (buf, acc), group=tg)
        for buf in op.outputs:
            stream = buf.stream(ov)
            if stream is None:
                raise ValueError(
                    f"{type(op).__name__}.{buf.name} names no stream (from_=), so its "
                    f"sequence cannot be derived; add from_= or override design(rt)"
                )
            for slot, accesses in plan(buf, stream):
                for acc in accesses:
                    rt.drain(slot, (buf, acc), group=tg, wait=True)


# --------------------------------------------------------------------------
# The design function
# --------------------------------------------------------------------------


def _symbol(op: Operator, value: BoundValue) -> str:
    """The device symbol of a per-call value: stable across processes, unique per instance."""
    return f"{op.name}_{value.name}"


def build_design(
    dev,
    kernels_dir,
    op: Operator,
    func_prefix: str = "",
    verbose: bool = False,
    trace_size: int = 0,
    code: str = "",
):
    """Generate the MLIR module for one declared operator.

    Called by ``compile_xclbin_insts`` and ``fuse_mlir`` through the
    operator's ``DesignGenerator``; ``code`` exists only to reach the cache
    key (see :func:`mlir_artifact_for`).
    """
    from aie.iron import Program, Runtime, ScratchpadParameter

    op = op.tuned(dev)
    ov = op.ov
    target = Target(dev, kernels_dir, func_prefix, verbose, trace_size)
    target.base_dir = getattr(op.context, "base_dir", None)

    # Per-call values get their device parameters before the array is built,
    # so a core-read value can be handed to a worker by the overlay's design.
    for value in ov.values:
        value.symbol = ov.value_symbol(value) or _symbol(op, value)
        value.param = ScratchpadParameter(value.symbol, value.dtype)
    for value in op.values:
        if value.kind == "dispatch":
            raise NotImplementedError(
                f"{type(op).__name__}.{value.name} is a DispatchTime value; generated "
                f"sequences arrive with the packaging step (OPERATOR_MODEL_PLAN.md §8)"
            )
        value.symbol = op.value_symbol(value) or _symbol(op, value)
        value.param = ScratchpadParameter(value.symbol, value.dtype)

    workers = ov.design(target)
    if workers is None:
        workers = []

    streams = list(ov.streams.values())
    handles = [h for s in streams for h in s.handles]  # raises if any stream is unbound

    buffers = op.buffers
    fn_args: list[Any] = [b.flat_type for b in buffers]
    fn_args.append(handles)
    params = [v.param for v in ov.values] + [v.param for v in op.values]

    def sequence(*args):
        rt_data = {b.name: a for b, a in zip(buffers, args)}
        rt = Sequence(op, ov, rt_data)
        _preamble(rt, op, ov, target)
        if op.has_design_override():
            op.design(rt)
        else:
            _derived(rt, op, ov)

    rt = Runtime(sequence, fn_args + params)
    prog = Program(ov.device(target), rt, workers=workers)
    if trace_size:
        from iron.operators._trace import maybe_enable_trace

        maybe_enable_trace(prog, trace_size, workers)
    return prog.resolve_program()


def _design_code(op: Operator) -> str:
    """A digest of the overlay's and operator's class source, for the cache key.

    ``compile_xclbin_insts`` hashes the design *function* by its code, and
    that function is :func:`build_design` for every declared operator. The
    code that actually varies is the two classes', so it is spelled here.
    """
    h = hashlib.sha256()
    for cls in (type(op.ov), type(op)):
        try:
            h.update(inspect.getsource(cls).encode())
        except (OSError, TypeError):
            h.update(cls.__qualname__.encode())
    return h.hexdigest()[:24]


def mlir_artifact_for(
    op: Operator, filename: str | None = None
) -> PythonGeneratedMLIRArtifact:
    """The artifact the existing compile path expects, carrying ``build_design``.

    ``filename`` names the module for an operator whose stem is not its own
    name (flm/gemm's configuration-only build).
    """
    return PythonGeneratedMLIRArtifact(
        filename or f"{op.name}.mlir",
        DesignGenerator(
            fn=build_design, bind_from=op, kwargs={"op": op, "code": _design_code(op)}
        ),
    )
