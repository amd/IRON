# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generating and compiling the MLIR module for one declared operator."""

from __future__ import annotations

import functools
import hashlib
import inspect
import re
from pathlib import Path
from typing import Any

import aie
import aie.utils as aie_utils
from aie.iron import (
    Buffer,
    DispatchTime,
    Flow,
    Lock,
    PacketFlow,
    Program,
    Runtime,
    ScratchpadParameter,
    TileDma,
)
from aie.utils.compile.jit.compilabledesign import CompilableDesign
from aie.utils.trace import events as trace_events

from ..declare import Operator
from ..declare.bound import BoundValue
from .external import ExternalSequence
from .runtime import Sequence
from .target import Target

# What a traced core records: its DMA ports running, the kernel's
# event0()/event1() markers, and its stalls and vector instructions.
CORE_EVENTS = [
    trace_events.PortEvent(
        trace_events.CoreEvent.PORT_RUNNING_0, trace_events.WireBundle.DMA, 0, True
    ),
    trace_events.PortEvent(
        trace_events.CoreEvent.PORT_RUNNING_1, trace_events.WireBundle.DMA, 1, True
    ),
    trace_events.PortEvent(
        trace_events.CoreEvent.PORT_RUNNING_2, trace_events.WireBundle.DMA, 0, False
    ),
    trace_events.CoreEvent.INSTR_EVENT_0,
    trace_events.CoreEvent.INSTR_EVENT_1,
    trace_events.CoreEvent.MEMORY_STALL,
    trace_events.CoreEvent.LOCK_STALL,
    trace_events.CoreEvent.INSTR_VECTOR,
]


def device_symbol(op: Operator, value: BoundValue) -> str:
    """The device symbol of a per-call value: stable across processes, unique per instance.

    The host writes the value through the parameter scratchpad under this
    symbol: the instance's name, the value's name, and the graph value's
    name when a graph binds one, so two instances alike in every field but
    reading different graph values write through different symbols. An
    operator may override it through its ``value_symbol`` hook.
    """
    own = op.value_symbol(value)
    if own is not None:
        return own
    bound = op.bound_values.get(value.name)
    return f"{op.name}_{value.name}" + (f"_{bound}" if bound else "")


def build_design(op: Operator, image: str = "elf", **dispatch):
    """Generate the MLIR module for one declared operator, for the bound device.

    ``image`` is what the module is built for: on ``"elf"`` a per-call value
    is a scratchpad parameter; on ``"xclbin"``, which has no scratchpad (XRT
    gives one to a module run only), it is a dispatch-time scalar of the
    sequence, handed in by name in ``dispatch`` (:class:`OperatorDesign`
    declares them as the generator's parameters).
    """
    dev = op.dev
    op = op.resolved(dev).copy()  # a build binds streams; each gets its own
    if op.external is not None:
        # A downloaded image: no array to build, only the sequence against
        # its pins.
        return ExternalSequence.module(dev, op)
    target = Target(dev, image)

    # Per-call values get their device parameters before the array is built,
    # so a core-read value can be handed to a worker by array().
    values = op.values
    for value in values:
        value.symbol = device_symbol(op, value)
        value.ssa = None
        value.targets = []
        if image == "elf" and value.kind != "dispatch":
            value.param = ScratchpadParameter(value.symbol, value.dtype)
        elif image == "elf":
            raise ValueError(
                f"{type(op).__name__}.{value.name} is a DispatchTime value, which a "
                f"full ELF cannot carry (its stream is fixed at build time); "
                f"package as xclbin"
            )
        else:
            if value.symbol not in dispatch:
                raise ValueError(
                    f"{type(op).__name__}.{value.name}: no dispatch parameter "
                    f"{value.symbol!r} was handed to build_design"
                )
            value.param = dispatch[value.symbol]

    workers = op.build_array(target)
    if workers is None:
        workers = []

    streams = list(op.streams.values())
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
        seq = Sequence(op, rt_data, target)
        if not op.own_preamble:
            seq.preamble()
        seq.run()

    rt = Runtime(sequence, fn_args + params)
    # What array() registered on the target: before the program resolves,
    # since the sequence body, which runs last, may address all of it.
    for obj in target.registered:
        if isinstance(obj, (Flow, PacketFlow)):
            rt.add_flow(obj)
        elif isinstance(obj, Lock):
            rt.add_lock(obj)
        elif isinstance(obj, TileDma):
            rt.add_tile_dma(obj)
        elif isinstance(obj, Buffer):
            rt.add_buffer(obj)
        else:
            raise TypeError(
                f"target.register takes a Flow, PacketFlow, Lock, TileDma or "
                f"Buffer, got {obj!r}"
            )
    prog = Program(op.device(target), rt, workers=workers)
    if op.trace is not None:
        if op.trace.reuse_output_buffer:
            raise ValueError(
                f"{type(op).__name__}: a full ELF consolidates its outputs, so "
                f"its trace takes a buffer of its own (reuse_output_buffer=False)"
            )
        # The workers array() marked with Worker(trace=), or the first.
        traced = [w for w in workers if w.trace is not None] or list(workers)[:1]
        prog.enable_trace(
            op.trace.trace_size, workers=traced, coretile_events=CORE_EVENTS
        )
    return prog.resolve_program()


class OperatorDesign:
    """One operator's design as ``CompilableDesign`` compiles it.

    The generator is :func:`build_design` bound to the operator, or the
    design another tool exports for it (:meth:`Operator.exported_design`).
    It runs inside ``compile()``, so the kernels it declares are the ones
    built; on an xclbin its per-call values are its ``DispatchTime``
    parameters, so the two images are two modules and two cache keys.

    The cache key is what the module is a function of, which the generator's
    code alone does not spell: the operator's design key, the image, and the
    source that generates the text (the operator's modules, IRON's common
    tree, mlir-aie's Python frontend and bindings).
    """

    _AIE = Path(inspect.getfile(aie)).resolve().parent
    TREES = (Path(__file__).resolve().parents[1], _AIE / "iron", _AIE / "dialects")
    # Compiled, and large: by size and time rather than by content.
    BINDINGS = _AIE / "_mlir_libs"
    # An object address in the key would re-key the cache every process.
    _ADDRESS = re.compile(r"0x[0-9a-f]{6,}")

    def __init__(self, op: Operator, image: str = "elf"):
        self.op = op
        self.image = image
        generator = op.exported_design(image)
        if generator is None:
            generator = functools.partial(build_design, op=op, image=image)
            P = inspect.Parameter
            dispatch = [
                P(
                    device_symbol(op, v),
                    P.KEYWORD_ONLY,
                    annotation=DispatchTime[v.dtype],
                )
                for v in op.values
                if image != "elf"
            ]
            setattr(generator, "__signature__", inspect.Signature(dispatch))
        self.generator = generator

    @functools.cached_property
    def identity(self) -> str:
        """What the module is built from, sources aside."""
        text = repr((self.op.design_key(), self.image))
        if self._ADDRESS.search(text):
            raise ValueError(
                f"{type(self.op).__name__}'s design key {text!r} embeds an object "
                f"address, which would give it a new compile-cache key in every "
                f"process; give the field a stable repr"
            )
        return hashlib.sha256(text.encode()).hexdigest()[:24]

    @property
    def name(self) -> str:
        """The design's device symbol in a fused image: stable across source
        edits, so aiecc's device cache keeps it.
        """
        return f"{type(self.op).__name__}_{self.identity[:8]}"

    @property
    def sources(self) -> list[str]:
        """The modules the design is defined in: the generator's and every
        class the operator's is built from.
        """
        generator = self.generator
        function = getattr(generator, "func", generator)
        files = set()
        for obj in (function, *type(self.op).__mro__):
            try:
                files.add(inspect.getsourcefile(obj))
            except TypeError:
                pass  # a builtin
        return sorted(f for f in files if f)

    @property
    def key(self) -> str:
        return f"{self.identity}:{self.source_digest(tuple(self.sources))}"

    def compile(self, **options) -> CompilableDesign:
        """Compile (or find in the cache) the design; ``options`` are
        ``CompilableDesign``'s (``aiecc_flags``, ``insts_only``, ...).
        """
        # The key reads the current device, which compile() binds from inside;
        # binding first makes a key computed before and after agree.
        aie_utils.ensure_current_device()
        design = CompilableDesign(self.generator, key=self.key, **options)
        design.compile()
        return design

    @classmethod
    @functools.cache
    def source_digest(cls, files: tuple = ()) -> str:
        """A digest of the source that generates MLIR: the trees every
        design shares, and ``files`` besides.

        Read once per process: a process runs the code it imported, so an
        edit made while it runs is the next process's to see, in its key and
        its text alike.
        """
        h = hashlib.sha256()
        if files:
            h.update(cls.source_digest().encode())
            for path in files:
                h.update(Path(path).read_bytes())
            return h.hexdigest()
        for root in cls.TREES:
            for path in sorted(root.rglob("*.py")):
                h.update(path.read_bytes())
        for path in sorted(cls.BINDINGS.glob("*.so")):
            stat = path.stat()
            h.update(f"{path.name}:{stat.st_size}:{stat.st_mtime_ns}".encode())
        return h.hexdigest()
