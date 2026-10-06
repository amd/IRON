# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generating and compiling the MLIR module for one declared operator."""

from __future__ import annotations

import functools
import hashlib
import inspect
import re
from typing import Any

import aie.utils as aie_utils
from aie.iron import (
    CompileTime,
    DispatchTime,
    Flow,
    Lock,
    PacketFlow,
    Program,
    Runtime,
    ScratchpadParameter,
    TileDma,
    Worker,
    WorkerRuntimeBarrier,
)
from aie.utils.compile.jit.compilabledesign import CompilableDesign

from .. import declare
from ..declare import Operator
from ..declare.bound import BoundValue
from .external import ExternalSequence
from .runtime import Sequence
from .target import Target


def device_symbol(op: Operator, value: BoundValue) -> str:
    """The symbol a per-call value is written through: the instance's name,
    the value's, and the graph value bound to it, unless ``value_symbol``
    names one.
    """
    own = op.value_symbol(value)
    if own is not None:
        return own
    bound = op.bound_values.get(value.name)
    return f"{op.name}_{value.name}" + (f"_{bound}" if bound else "")


def build_design(op: Operator, image: str = "elf", **dispatch):
    """The MLIR module for one declared operator, on the bound device.

    Args:
        image: ``"elf"``, where a per-call value is a scratchpad parameter,
            or ``"xclbin"``, which has none: there it is a dispatch-time
            scalar, given by symbol in ``dispatch``.
    """
    dev = op.dev
    op = op.resolved(dev).copy()  # a build binds streams; each gets its own
    if op.external is not None:
        return ExternalSequence.module(dev, op)
    target = Target(dev, image)

    # Before array(), which may hand a core-read value to a worker.
    values = op.values
    for value in values:
        value.symbol = device_symbol(op, value)
        value.ssa = None
        value.targets = []
        if image == "elf" and not isinstance(value.member, declare.DispatchTime):
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

    built = op.build_array(target) or []
    workers = [w for w in built if isinstance(w, Worker)]
    barriers = tuple(b for b in built if isinstance(b, WorkerRuntimeBarrier))

    # Raises if any stream is unbound.
    handles = [h for b in op.buffers if b.streamed for h in b.handles]

    buffers = op.buffers
    fn_args: list[Any] = [b.flat_type for b in buffers]
    fn_args.append(handles)
    params = [v.param for v in values]

    def sequence(*args):
        rt_data = {b.name: a for b, a in zip(buffers, args)}
        if image != "elf":
            for value, scalar in zip(values, args[len(buffers) + 1 :]):
                value.ssa = scalar
        seq = Sequence(op, rt_data, image, barriers)
        if not op.own_preamble:
            seq.preamble()
        seq.run()

    rt = Runtime(sequence, fn_args + params)
    # Before resolving: the sequence body, generated last, may address any of it.
    for obj in built:
        if isinstance(obj, (Flow, PacketFlow)):
            rt.add_flow(obj)
        elif isinstance(obj, Lock):
            rt.add_lock(obj)
        elif isinstance(obj, TileDma):
            rt.add_tile_dma(obj)
        elif not isinstance(obj, (Worker, WorkerRuntimeBarrier)):
            raise TypeError(
                f"{type(op).__name__}.array() returns Workers, WorkerRuntimeBarriers, "
                f"Flows, PacketFlows, Locks and TileDmas; got {obj!r}"
            )
    prog = Program(op.device(target), rt, workers=workers)
    if op.trace is not None:
        if op.trace.reuse_output_buffer:
            raise ValueError(
                f"{type(op).__name__}: a full ELF consolidates its outputs, so "
                f"its trace takes a buffer of its own (reuse_output_buffer=False)"
            )
        traced = [w for w in workers if w.trace is not None] or list(workers)[:1]
        prog.enable_trace(op.trace.trace_size, workers=traced)
    return prog.resolve_program()


class OperatorDesign:
    """One operator's design as ``CompilableDesign`` compiles and caches it:
    ``build_design``, or ``Operator.exported_design``.

    The cache key is ``CompilableDesign``'s recipe; ``identity`` adds the
    fields the operator's repr leaves out.
    """

    # An object address in the key would re-key the cache every process.
    _ADDRESS = re.compile(r"0x[0-9a-f]{6,}")

    def __init__(self, op: Operator, image: str = "elf"):
        self.op = op
        self.image = image
        P = inspect.Parameter
        build = op.exported_design(image)
        if build is None:
            build = functools.partial(build_design, op=op, image=image)
            params = [
                P(
                    device_symbol(op, v),
                    P.KEYWORD_ONLY,
                    annotation=DispatchTime[v.dtype],
                )
                for v in op.values
                if image != "elf"
            ]
        else:
            params = list(inspect.signature(build).parameters.values())
        self.build = build

        def generator(op: CompileTime[Operator], identity: CompileTime[str], **kwargs):
            return build(**kwargs)

        keys = [
            P("op", P.KEYWORD_ONLY, annotation=CompileTime[Operator]),
            P("identity", P.KEYWORD_ONLY, annotation=CompileTime[str]),
        ]
        setattr(generator, "__signature__", inspect.Signature([*params, *keys]))
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
        """The design's device symbol in a fused image, stable across source edits."""
        return f"{type(self.op).__name__}_{self.identity[:8]}"

    def compilable(self, **options) -> CompilableDesign:
        """The ``CompilableDesign``, given ``options``, the operator's
        ``aiecc_flags`` added to theirs.
        """
        flags = [*options.pop("aiecc_flags", ()), *self.op.aiecc_flags]
        return CompilableDesign(
            self.generator,
            compile_kwargs={"op": self.op, "identity": self.identity},
            aiecc_flags=flags,
            **options,
        )

    def compile(self, **options) -> CompilableDesign:
        """Compile the design, or find it in the cache."""
        # The key reads the current device: bound first, keys before and after agree.
        aie_utils.ensure_current_device()
        design = self.compilable(**options)
        design.compile()
        return design
