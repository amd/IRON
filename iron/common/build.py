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
(``xclbin_design``, ``fuse_mlir``) see nothing new: they call it with
the operator bound by name, exactly as they call ``my_matvec`` today.

Everything that touches mlir-aie is imported inside the functions that need
it, so the declaration layer stays importable without the toolchain.
"""

from __future__ import annotations

import hashlib
import inspect
from contextlib import contextmanager
import dataclasses
from pathlib import Path
from typing import Any, Callable

import numpy as np

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
# A design and its arguments, as CompilableDesign runs it
# --------------------------------------------------------------------------


@dataclasses.dataclass
class DesignGenerator:
    """A design function and the arguments it is generated with.

    ``fn`` is the function (an operator's design is ``build_design`` over the
    operator); a design loaded from a file names ``source_path`` and
    ``fn_name`` instead (swiglu_prefill_stream's exported text). Called for
    its MLIR text; ``resolve()`` hands ``CompilableDesign`` the function and
    its keyword arguments to run inside ``compile()``.
    """

    fn: Callable | None = None
    kwargs: dict = dataclasses.field(default_factory=dict)
    source_path: Path | None = None
    fn_name: str | None = None
    args: tuple = ()

    def resolve(self) -> tuple[Callable, tuple, dict]:
        if self.fn is not None:
            return self.fn, self.args, self.kwargs
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            self.source_path.name, self.source_path
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, self.fn_name), self.args, self.kwargs

    def __call__(self) -> str:
        fn, args, kwargs = self.resolve()
        return str(fn(*args, **kwargs))


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
        image: str = "elf",
        use_chess: bool = False,
    ):
        from pathlib import Path

        from iron.operators._kernels import target_arch

        self.dev = dev
        self.kernels_dir = Path(kernels_dir)
        self.arch = target_arch(dev)  # "aie2" | "aie2p"
        self.func_prefix = func_prefix
        self.verbose = verbose
        # xchesscc rather than Peano, from the context; every kernel of one
        # design must agree, which upstream enforces when it compiles them.
        self.use_chess = use_chess
        self.trace_size = trace_size
        # "elf": per-call values reach the array through the parameter
        # scratchpad. "xclbin": there is none (spike S2); they are dispatch-
        # time scalars of the sequence, and a core-read value is a resident
        # the sequence writes (bind it to the runtime-parameter buffer).
        self.image = image
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
            func_prefix=self.func_prefix,
            use_chess=self.use_chess,
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


def _plus(ssa, constant: int):
    """``ssa + constant`` as a sequence value; the scalar alone when constant is 0."""
    if not constant:
        return ssa
    from aie.extras.dialects import arith
    from aie.helpers.util import np_dtype_to_mlir_type

    return ssa + arith.constant(int(constant), np_dtype_to_mlir_type(np.int32))


def run_design(op: Operator, ov: Overlay, seq) -> None:
    """The transfers: the overlay's sequence when it owns one, else the
    operator's override, else the one derived from the declarations."""
    if ov.has_sequence():
        ov.sequence(op, seq)
    elif op.has_design_override():
        op.design(seq)
    else:
        _derived(seq, op, ov)


def _preamble(rt: Sequence, op: Operator, ov: Overlay, target: Target) -> None:
    """Residents, then barriers, then the parameter sync, before any DMA."""
    values = ov.resident_values(op)
    writes: dict[int, tuple] = {}  # id(buffer) -> (buffer, {index: value})
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
            writes.setdefault(id(buf), (buf, {}))[1][index] = values[name]
    # One buffer at a time, its words in order: the order the hand-written
    # sequences wrote, so a converted operator's instruction stream matches.
    for buf, words in writes.values():
        for index in sorted(words):
            buf[index] = words[index]
    # A core-read value on an image without a scratchpad: written from the
    # sequence's per-call scalar, after the residents, before the barriers.
    for value in list(ov.values) + list(op.values):
        for buf, index in value.targets:
            if value.ssa is None:
                raise ValueError(
                    f"{value.name} is bound to a runtime-parameter buffer but is "
                    f"not a dispatch-time scalar here; bind only under an image "
                    f"without a scratchpad (target.image != 'elf')"
                )
            buf[index] = value.ssa
    unknown = set(values) - set(ov.residents)
    if unknown:
        raise ValueError(
            f"{type(op).__name__}.residents() names {sorted(unknown)}, which "
            f"{type(ov).__name__} does not declare"
        )
    for b in target.barriers:
        b.set(1)
    if target.image == "elf" and (op.values or ov.values):
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


def value_symbol(op: Operator, value: BoundValue) -> str:
    """The device symbol of a per-call value: stable across processes, unique per instance.

    What the host writes through the parameter scratchpad; the operator's
    own ``value_symbol`` override (a legacy spelling) wins when it exists.
    """
    owner = op if value.name in {v.name for v in op.values} else op.ov
    return owner.value_symbol(value) or f"{op.name}_{value.name}"


_symbol = value_symbol


def build_design(
    dev,
    kernels_dir,
    op: Operator,
    func_prefix: str = "",
    verbose: bool = False,
    trace_size: int = 0,
    code: str = "",
    image: str = "elf",
    use_chess: bool = False,
    **dispatch,
):
    """Generate the MLIR module for one declared operator.

    Called by :mod:`iron.common.jit_compile`'s compile functions and by
    ``fuse_mlir`` through the
    operator's ``DesignGenerator``; ``code`` exists only to reach the cache
    key (see :func:`mlir_artifact_for`).
    """
    from aie.iron import Program, Runtime, ScratchpadParameter
    from aie.iron.kernels._common import _EXTERN_CACHE

    # aie.iron.kernels' factories memoize the ExternalFunction they return,
    # and a returned one holds MLIR operations from the context it was
    # resolved in. Every generation must start from an empty cache or a
    # second design gets a kernel bound to a dead context. CompilableDesign
    # clears it when it generates; this is the same entry point for the
    # paths that call a design directly -- fusion's per-child generation
    # and the lowering gates.
    _EXTERN_CACHE.clear()

    op = op.tuned(dev)
    ov = op.ov
    if ov.external is not None:
        # A downloaded image: no array to build, only the sequence against
        # the pins the overlay declares, which the overlay itself emits.
        return ov.build(dev, op)
    target = Target(
        dev, kernels_dir, func_prefix, verbose, trace_size, image, use_chess
    )
    target.base_dir = getattr(op.context, "base_dir", None)

    # Per-call values get their device parameters before the array is built,
    # so a core-read value can be handed to a worker by the overlay's design.
    # On a full ELF they are scratchpad parameters; on an xclbin, which has
    # no scratchpad (spike S2), every one is a dispatch-time scalar of the
    # sequence, handed in by the generator's keyword parameters (see
    # ``mlir_artifact_for``), and DispatchTime members are always that.
    values = list(ov.values) + list(op.values)
    for value in values:
        value.symbol = value_symbol(op, value)
        value.ssa = None
        value.targets = []
        if image == "elf" and value.kind != "dispatch":
            value.param = ScratchpadParameter(value.symbol, value.dtype)
        elif image == "elf":
            raise ValueError(
                f"{type(op).__name__}.{value.name} is a DispatchTime value, which a "
                f"full ELF cannot carry (its stream is fixed at build time); "
                f"package as xclbin (OPERATOR_MODEL_PLAN.md §6, §8)"
            )
        else:
            if value.symbol not in dispatch:
                raise ValueError(
                    f"{type(op).__name__}.{value.name}: no dispatch parameter "
                    f"{value.symbol!r} was handed to build_design"
                )
            value.param = dispatch[value.symbol]

    workers = ov.design(target)
    if workers is None:
        workers = []

    streams = list(ov.streams.values())
    handles = [h for s in streams for h in s.handles]  # raises if any stream is unbound

    buffers = op.buffers
    fn_args: list[Any] = [b.flat_type for b in buffers]
    fn_args.append(handles)
    params = [v.param for v in values]

    def sequence(*args):
        rt_data = {b.name: a for b, a in zip(buffers, args)}
        if image != "elf":
            # A dispatch parameter arrives in the body as its live scalar.
            for value, scalar in zip(values, args[len(buffers) + 1 :]):
                value.ssa = scalar
        seq = Sequence(op, ov, rt_data)
        _preamble(seq, op, ov, target)
        run_design(op, ov, seq)
        # A declared stream slot this extent never transfers on (mem_copy's
        # idle cores at a small size) still needs a shim endpoint, or the
        # program cannot be resolved. Place it on any shim tile.
        idle = [h for h in handles if id(h) not in seq.used]
        if idle:
            from aie.iron.device import AnyShimTile
            from aie.iron.runtime.endpoint import RuntimeEndpoint

            for h in idle:
                h.endpoint = RuntimeEndpoint(AnyShimTile)
                rt._fifos.add(h)

    rt = Runtime(sequence, fn_args + params)
    prog = Program(ov.device(target), rt, workers=workers)
    if trace_size:
        from iron.operators._trace import maybe_enable_trace

        maybe_enable_trace(prog, trace_size, workers)
    return prog.resolve_program()


def _design_code(op: Operator) -> str:
    """A digest of the overlay's and operator's class source, for the cache key.

    ``CompilableDesign`` hashes the design *function* by its code, and
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


def dispatch_parameters(op: Operator) -> list[tuple[str, Any]]:
    """The (symbol, dtype) of every per-call value, as dispatch-time scalars."""
    return [
        (value_symbol(op, v), v.dtype) for v in list(op.ov.values) + list(op.values)
    ]


def generator_for(op: Operator, image: str = "elf") -> DesignGenerator:
    """The generator ``CompilableDesign`` runs for ``op``: ``build_design`` over it.

    ``image`` is the image the module is built for: on ``"xclbin"`` its
    per-call values are the generator's dispatch-time parameters, so the two
    images are two modules and two cache keys.
    """
    return DesignGenerator(
        fn=build_design,
        kwargs={
            "op": op,
            "image": image,
            "dispatch": dispatch_parameters(op) if image != "elf" else [],
            "code": _design_code(op),
            "use_chess": op.context.use_chess,
            # Spelled here, not bound by name from the operator: the
            # device reaches the cache key by identity, the kernel tree
            # by path (pointing IRON at another tree changes the key).
            "dev": op.dev,
            "kernels_dir": op.kernels_dir,
        },
    )
