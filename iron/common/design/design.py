# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generating and compiling the MLIR module for one declared operator."""

from __future__ import annotations

import functools
import hashlib
import inspect
import re
from collections.abc import Hashable, Mapping

import aie.utils as aie_utils
from aie import ir
from aie.dialects import aie
from aie.iron import (
    Buffer,
    CompileTime,
    DeviceConfiguration,
    DispatchTime,
    Flow,
    Lock,
    PacketFlow,
    Program,
    ScratchpadParameter,
    TileDma,
    Worker,
    WorkerRuntimeBarrier,
)
from aie.iron.dataflow.objectfifo import ObjectFifoHandle, ObjectFifoLink
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
        """
        if self.op.external is not None:
            dev = self.op.dev
            op = self.op.resolved(dev).copy()  # a build binds streams
            runtime = ShippedRuntime(op, dev, op.build_array())
            return Program(dev, runtime).resolve_program()
        array = BuiltArray(self, dispatch=dispatch)
        prog = Program(
            array.op.device(),
            OperatorRuntime(array.op, array.built),
            workers=array.workers,
        )
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


class BuiltArray:
    """One design's array, built on a resolved copy of its operator.

    Designs of one array (``identities``) build it once: each runs its own
    sequence over it (``runtime``).

    Args:
        design: The design to build.
        words: On a full ELF, design symbol -> the scratchpad word it shares
            with others that always hold the same number.
        dispatch: On an xclbin, each per-call value's dispatch-time scalar,
            by device symbol.

    Attributes:
        design: The design built.
        op: The copy, its array built and its operands' lanes bound.
        built: What its ``array()`` returned.
        workers: The workers among them.
        traced: The workers a traced operator traces, else none.

    Raises:
        ValueError: A full ELF is asked to carry a `DispatchTime` value, an
            xclbin is given no scalar for a value, or a trace would reuse
            an output a full ELF consolidates.
    """

    def __init__(
        self,
        design: OperatorDesign,
        words: Mapping[str, str] | None = None,
        dispatch: Mapping[str, object] | None = None,
    ):
        words = words or {}
        dispatch = dispatch or {}
        self._words, self._dispatch = words, dispatch
        op = design.op.resolved(design.op.dev).copy()  # a build binds streams
        # Before array(), which may hand a core-read value to a worker.
        for value in op.values:
            if design.full_elf and not isinstance(value, declare.DispatchTime):
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
        before = set(vars(op))
        self.built = op.build_array() or []
        # What array() kept on the operator for its sequence to program.
        self._kept = {name: vars(op)[name] for name in vars(op).keys() - before}
        self.design = design
        self.op = op
        self.workers = [w for w in self.built if isinstance(w, Worker)]
        self.traced: list[Worker] = []
        if op.trace is not None:
            if op.trace.reuse_output_buffer:
                raise ValueError(
                    f"{type(op).__name__}: a full ELF consolidates its outputs, so "
                    f"its trace takes a buffer of its own (reuse_output_buffer=False)"
                )
            self.traced = [w for w in self.workers if w.trace is not None]
            self.traced = self.traced or self.workers[:1]

    @functools.cached_property
    def reads(self) -> frozenset[str]:
        """The scratchpad words this design's cores read: beside its
        ``array_key``, all its array depends on.

        Read off the design built anew and resolved alone, since a core
        reads a word through the parameter its function closes over.
        """
        alone = BuiltArray(self.design, self._words, self._dispatch)
        module = Program(
            alone.op.device(),
            OperatorRuntime(alone.op, alone.built),
            workers=alone.workers,
        ).resolve_program()
        words: set[str] = set()

        def read(op: ir.Operation) -> ir.WalkResult:
            if op.name == "aiex.read_scratchpad_parameter":
                words.add(ir.FlatSymbolRefAttr(op.attributes["parameter"]).value)
            return ir.WalkResult.ADVANCE

        for device in module.body.operations:
            if isinstance(device, aie.DeviceOp):
                for op in device.body_region.blocks[0].operations:
                    if isinstance(op, aie.CoreOp):
                        op.operation.walk(read)
        return frozenset(words)

    def namespace(self, prefix: str) -> None:
        """Prefix each symbol this array names with ``prefix``, so it keeps
        its own beside another array's in one device configuration.

        A shim channel's symbol keeps its name: a sequence may address the
        channel by it, and two arrays pinning one channel do not pack anyway.
        """
        # aie.iron scopes a symbol by its DeviceConfiguration alone and has no
        # rename, so each name is set where the configuration's resolve reads it.
        handles = [h for w in self.workers for h in w.fifos]
        handles += [
            h
            for b in self.op.buffers
            for h in b.lane_handles
            if isinstance(h, ObjectFifoHandle)
        ]
        fifos = {}
        while handles:
            fifo = handles.pop()._object_fifo
            if id(fifo) in fifos:
                continue
            fifos[id(fifo)] = fifo
            for end in [fifo._prod, *fifo._cons]:
                if end is not None and isinstance(end.endpoint, ObjectFifoLink):
                    handles += [*end.endpoint._srcs, *end.endpoint._dsts]
        for fifo in fifos.values():
            if fifo.name is not None:
                fifo.name = prefix + fifo.name
        reached = [*(a for w in self.workers for a in w.flat_fn_args), *self.built]
        reached += [h for b in self.op.buffers for h in b.lane_handles]
        for tile_dma in [r for r in reached if isinstance(r, TileDma)]:
            buffers, locks = tile_dma.all_buffers_and_locks()
            reached += [*buffers, *locks]
        named = {
            id(r): r for r in reached if isinstance(r, (Buffer, Lock, Flow, PacketFlow))
        }
        for resource in named.values():
            if resource._name is not None:
                resource._name = prefix + resource._name

    def runtime(self, other: BuiltArray, name: str) -> OperatorRuntime:
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
        for value in [*op.residents, *(v.name for v in op.values)]:
            op.value(value).targets = self.op.value(value).targets
        vars(op).update(self._kept)
        # A sequence fills only flows it registers, which the configuration
        # keeps once; tile DMAs and shim channels are the owner's to declare.
        reached = (WorkerRuntimeBarrier, Flow, PacketFlow, Lock)
        return OperatorRuntime(
            op, [b for b in self.built if isinstance(b, reached)], name=name
        )


def identities(arrays: Mapping[str, BuiltArray]) -> dict[str, Hashable]:
    """What each of ``arrays`` is, equal where two are one array: its
    ``array_key``, and where another shares that, the words its cores read
    (``BuiltArray.reads``).
    """
    keys = [a.op.array_key() for a in arrays.values()]
    return {
        name: key if keys.count(key) == 1 else (key, array.reads)
        for (name, array), key in zip(arrays.items(), keys)
    }


def configuration(name: str, arrays: Mapping[str, BuiltArray]) -> DeviceConfiguration:
    """``arrays`` as one device configuration named ``name``: one array per
    identity, and each entry's runtime sequence over it, named
    ``sequence`` where there is one, else for its key. Where there are
    several arrays, each one's symbols take its first entry's key as a
    prefix.

    Raises:
        ValueError: The arrays are built for different devices.
    """
    of = identities(arrays)
    owners: dict[Hashable, BuiltArray] = {}
    firsts: dict[Hashable, str] = {}
    for key, array in arrays.items():
        owners.setdefault(of[key], array)
        firsts.setdefault(of[key], key)
    if len(owners) > 1:
        for identity, owner in owners.items():
            owner.namespace(f"{firsts[identity]}__")
    kinds = {type(a.op.device()).__name__ for a in owners.values()}
    if len(kinds) != 1:
        raise ValueError(f"{list(arrays)} are built for different devices {kinds}")
    runtimes = [
        owners[of[key]].runtime(array, "sequence" if len(arrays) == 1 else key)
        for key, array in arrays.items()
    ]
    first = next(iter(owners.values()))
    configured = DeviceConfiguration(
        name,
        first.op.device(),
        workers=[w for owner in owners.values() for w in owner.workers],
        runtimes=runtimes,
    )
    traced = [owner for owner in owners.values() if owner.traced]
    if traced:
        configured.enable_trace(
            traced[0].op.trace.trace_size,
            workers=[w for owner in traced for w in owner.traced],
        )
    return configured
