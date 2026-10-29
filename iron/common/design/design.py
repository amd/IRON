# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generating and compiling the MLIR module for one declared operator."""

from __future__ import annotations

import dataclasses
import functools
import hashlib
import inspect
import re
from collections.abc import Hashable, Mapping, Sequence

import aie.utils as aie_utils
from aie import ir
from aie.dialects.aie import CoreOp, DeviceOp
from aie.iron import (
    CompileTime,
    DeviceConfiguration,
    DispatchTime,
    Flow,
    Lock,
    PacketFlow,
    Program,
    ScratchpadParameter,
    Worker,
)
from aie.utils.compile.jit.compilabledesign import CompilableDesign

from ..declare import Operator
from ..declare.operand import Operand
from .runtime import MergedRuntime, OperatorRuntime


class OperatorDesign:
    """One operator's design (``module``, or ``Operator.exported_design``) as
    ``CompilableDesign`` compiles and caches it; ``identity`` adds to the cache
    key the fields the operator's repr leaves out.
    """

    # An object address in the key would re-key the cache every process.
    _ADDRESS = re.compile(r"0x[0-9a-f]{6,}")

    def __init__(self, op: Operator, full_elf: bool = True):
        if op.reference_only:
            raise TypeError(f"{type(op).__name__} is reference-only: it has no kernel")
        # Keyed by what it builds: a replaced copy of a resolved operator
        # resolves afresh, and may resolve to other tunables than it holds.
        op = self.op = op.resolved(op.dev)
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

        def generator(
            op: CompileTime[Operator],
            identity: CompileTime[str],
            **kwargs,
        ):
            return build(**kwargs)

        keys = [
            P("op", P.KEYWORD_ONLY, annotation=CompileTime[Operator]),
            P("identity", P.KEYWORD_ONLY, annotation=CompileTime[str]),
        ]
        setattr(generator, "__signature__", inspect.Signature([*params, *keys]))
        self.generator = generator

    def module(self, **dispatch):
        """The operator's MLIR module on the bound device; on an xclbin, which has no
        parameter scratchpad, ``dispatch`` is each per-call value's scalar by symbol.
        """
        array = BuiltArray(self, dispatch=dispatch)
        prog = array.program()
        if array.traced:
            prog.enable_trace(array.op.trace.trace_size, workers=array.traced)
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
        """The design's device symbol in a full ELF, stable across source edits."""
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

    def compile(
        self, image: CompilableDesign | None = None, **options
    ) -> CompilableDesign:
        """Compile the design, or find it in the cache. ``image``, for an insts_only
        stream, is the design it runs on: the compile fails, naming each resource
        laid out otherwise than there, rather than run against it.
        """
        # The key reads the current device: bound first, keys before and after agree.
        aie_utils.ensure_current_device()
        design = self.compilable(**options)
        design.compile(image=image)
        return design


class BuiltArray:
    """One design's array, built on a resolved copy of its operator (``op``), its
    operands' lanes bound. Designs of one array (``identities``) build it once,
    each running its own sequence over it (``runtime``).

    Args:
        words: On a full ELF, design symbol -> the scratchpad word it shares
            with others that always hold the same number.
        dispatch: On an xclbin, each per-call value's dispatch-time scalar,
            by device symbol.

    Raises:
        ValueError: A full ELF is asked to carry a ``DispatchTime`` value, an
            xclbin is given no scalar for a value, or a trace would reuse
            an output a full ELF consolidates.
    """

    def __init__(
        self,
        design: OperatorDesign,
        words: Mapping[str, str] | None = None,
        dispatch: Mapping[str, object] | None = None,
        fed: Mapping[str, Operand] | None = None,
    ):
        words = words or {}
        dispatch = dispatch or {}
        fed = fed or {}
        self._words, self._dispatch = words, dispatch
        op = design.op.copy()  # a build binds streams
        # Before build(), which may hand a core-read value to a worker.
        for value in op.values:
            if design.full_elf and not value.dispatch:
                value.param = ScratchpadParameter(
                    words.get(value.symbol, value.symbol), value.dtype
                )
            elif design.full_elf:
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
        view = op.layout()
        operands = {b.name: b for b in view.buffers}
        for name, source in fed.items():
            operands[name].feed(source)
        self.built = view.build()
        for mine, built in zip(op.buffers, view.buffers):
            mine.lane_handles = built.lane_handles
            mine.fed_from = built.fed_from
        self.design = design
        self.op = op
        self.workers = [w for w in self.built.objects if isinstance(w, Worker)]
        self.traced: list[Worker] = []
        if op.trace is not None:
            if op.trace.reuse_output_buffer:
                raise ValueError(
                    f"{type(op).__name__}: its trace takes a buffer of its own "
                    f"(reuse_output_buffer=False), since a full ELF consolidates "
                    f"its outputs and an xclbin's build is traced the same way"
                )
            self.traced = [w for w in self.workers if w.trace is not None]
            self.traced = self.traced or self.workers[:1]

    def program(self) -> Program:
        """This array alone with its operator's own sequence."""
        return Program(
            self.op.array_device(),
            OperatorRuntime(self.op, self.built),
            workers=self.workers,
        )

    @functools.cached_property
    def reads(self) -> frozenset[str]:
        """The scratchpad words this design's cores read: beside its ``array_key``,
        all its array depends on. Read off the design built anew and resolved alone,
        since a core reads a word through the parameter its function closes over.
        """
        alone = BuiltArray(self.design, self._words, self._dispatch)
        module = alone.program().resolve_program()
        words: set[str] = set()

        def read(op: ir.Operation) -> ir.WalkResult:
            if op.name == "aiex.read_scratchpad_parameter":
                words.add(ir.FlatSymbolRefAttr(op.attributes["parameter"]).value)
            return ir.WalkResult.ADVANCE

        for device in module.body.operations:
            if isinstance(device, DeviceOp):
                for op in device.body_region.blocks[0].operations:
                    if isinstance(op, CoreOp):
                        op.operation.walk(read)
        return frozenset(words)

    def runtime(self, other: BuiltArray, name: str | None) -> OperatorRuntime:
        """``other``'s runtime sequence over this array, named ``name``.

        Raises:
            ValueError: ``other`` is another array.
        """
        if other is self:
            return OperatorRuntime(self.op, self.built, name=name)
        if other.op.array_key() != self.op.array_key():
            raise ValueError(
                f"{type(other.op).__name__} builds another array than "
                f"{type(self.op).__name__}; its sequence cannot run over this one"
            )
        op = other.op
        for mine, theirs in zip(op.buffers, self.op.buffers):
            mine.lane_handles = theirs.lane_handles
        # A sequence fills only flows it registers, which the configuration
        # keeps once; tile DMAs and shim channels are the owner's to declare.
        # It writes the owner's runtime parameters, and reads what else the
        # owner's build kept.
        reached = (Flow, PacketFlow, Lock)
        return OperatorRuntime(
            op,
            dataclasses.replace(
                self.built,
                objects=[b for b in self.built.objects if isinstance(b, reached)],
            ),
            name=name,
        )


def identities(arrays: Mapping[str, BuiltArray]) -> dict[str, Hashable]:
    """What each of ``arrays`` is, equal where two are one array: its ``array_key``,
    and where another shares that, the words its cores read (``BuiltArray.reads``).
    """
    keys = [a.op.array_key() for a in arrays.values()]
    return {
        name: key if keys.count(key) == 1 else (key, array.reads)
        for (name, array), key in zip(arrays.items(), keys)
    }


def configuration(
    name: str, arrays: Mapping[str, BuiltArray], steps: Sequence[str] = ()
) -> DeviceConfiguration:
    """``arrays`` as one device configuration ``name``: one array per identity, and
    each entry's sequence over it, ``sequence`` if it is alone, else named for its
    key. Given ``steps`` (keys of ``arrays``), one ``sequence`` runs theirs in order.

    Raises:
        ValueError: The arrays are built for different devices, or traced
            with different trace sizes.
    """
    of = identities(arrays)
    owners: dict[Hashable, BuiltArray] = {}
    for key, array in arrays.items():
        owners.setdefault(of[key], array)
    kinds = {type(a.op.array_device()).__name__ for a in owners.values()}
    if len(kinds) != 1:
        raise ValueError(f"{list(arrays)} are built for different devices {kinds}")
    traced = [owner for owner in owners.values() if owner.traced]
    sizes = {owner.op.trace.trace_size for owner in traced}
    if len(sizes) > 1:
        raise ValueError(
            f"{name}: its traced arrays ask for trace sizes {sorted(sizes)}; one "
            f"configuration has one trace buffer, so give them one size"
        )
    runtimes = (
        [
            MergedRuntime.merge(
                [owners[of[k]].runtime(arrays[k], None) for k in steps], "sequence"
            )
        ]
        if steps
        else [
            owners[of[key]].runtime(array, "sequence" if len(arrays) == 1 else key)
            for key, array in arrays.items()
        ]
    )
    first = next(iter(owners.values()))
    configured = DeviceConfiguration(
        name,
        first.op.array_device(),
        workers=[w for owner in owners.values() for w in owner.workers],
        runtimes=runtimes,
    )
    if traced:
        configured.enable_trace(
            sizes.pop(),
            workers=[w for owner in traced for w in owner.traced],
        )
    return configured
