# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generating and compiling the MLIR module for one declared operator."""

from __future__ import annotations

import functools
import hashlib
import inspect
import re

import aie.utils as aie_utils
from aie.iron import CompileTime, DispatchTime, Program, ScratchpadParameter, Worker
from aie.utils.compile.jit.compilabledesign import CompilableDesign

from .. import declare
from ..declare import Operator
from .runtime import OperatorRuntime
from .shipped import ShippedRuntime


class OperatorDesign:
    """One operator's design as ``CompilableDesign`` compiles and caches it:
    ``module``, or ``Operator.exported_design``.

    The cache key is ``CompilableDesign``'s recipe; ``identity`` adds the
    fields the operator's repr leaves out.
    """

    # An object address in the key would re-key the cache every process.
    _ADDRESS = re.compile(r"0x[0-9a-f]{6,}")

    def __init__(self, op: Operator, full_elf: bool = True):
        self.op = op
        self.full_elf = full_elf
        P = inspect.Parameter
        build = op.exported_design()
        if build is None:
            build = self.module
            params = [
                P(
                    v.symbol,
                    P.KEYWORD_ONLY,
                    annotation=DispatchTime[v.dtype],
                )
                for v in op.values
                if not full_elf
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

    def module(self, **dispatch):
        """The MLIR module for the operator, on the bound device.

        Args:
            **dispatch: On an xclbin, which has no parameter scratchpad, each
                per-call value's dispatch-time scalar, by device symbol.

        Raises:
            ValueError: A full ELF is asked to carry a `DispatchTime` value,
                or an xclbin is given no scalar for a value.
        """
        dev = self.op.dev
        op = self.op.resolved(dev).copy()  # a build binds streams; each gets its own
        if op.external is not None:
            runtime = ShippedRuntime(op, dev, op.build_array())
            return Program(dev, runtime).resolve_program()
        # Before array(), which may hand a core-read value to a worker.
        for value in op.values:
            if self.full_elf and not isinstance(value, declare.DispatchTime):
                value.param = ScratchpadParameter(value.symbol, value.dtype)
            elif self.full_elf:
                raise ValueError(
                    f"{type(op).__name__}.{value.name} is a DispatchTime value, "
                    f"which a full ELF cannot carry (its stream is fixed at build "
                    f"time); compile with full_elf=False"
                )
            elif value.symbol not in dispatch:
                raise ValueError(
                    f"{type(op).__name__}.{value.name}: no dispatch parameter "
                    f"{value.symbol!r} was handed to the build"
                )
            else:
                value.param = dispatch[value.symbol]
        built = op.build_array() or []
        workers = [w for w in built if isinstance(w, Worker)]
        prog = Program(op.device(), OperatorRuntime(op, built), workers=workers)
        if op.trace is not None:
            if op.trace.reuse_output_buffer:
                raise ValueError(
                    f"{type(op).__name__}: a full ELF consolidates its outputs, so "
                    f"its trace takes a buffer of its own (reuse_output_buffer=False)"
                )
            traced = [w for w in workers if w.trace is not None] or list(workers)[:1]
            prog.enable_trace(op.trace.trace_size, workers=traced)
        return prog.resolve_program()

    @functools.cached_property
    def identity(self) -> str:
        """What the module is built from, sources aside."""
        # Part of every compile-cache key: a new spelling rebuilds every design.
        image = "elf" if self.full_elf else "xclbin"
        text = repr((self.op.design_key(), image))
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
