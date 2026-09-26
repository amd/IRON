# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generating the MLIR module for one declared operator."""

from __future__ import annotations

import hashlib
import inspect
from typing import Any

from aie.iron import Program, Runtime, ScratchpadParameter
from aie.iron.device import AnyShimTile
from aie.iron.runtime.endpoint import RuntimeEndpoint

from ..declare import Operator
from ..declare.bound import BoundValue
from ..kernels import kernels_dir
from ..tracing import maybe_enable_trace
from .generator import DesignGenerator
from .runtime import Sequence
from .target import Target


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


def build_design(
    dev,
    kernels_dir,
    op: Operator,
    trace_size: int = 0,
    code: str = "",
    image: str = "elf",
    **dispatch,
):
    """Generate the MLIR module for one declared operator.

    Called by :mod:`iron.common.image.jit_compile`'s compile functions and by
    ``fuse_mlir`` through the
    operator's ``DesignGenerator``; ``code`` exists only to reach the cache
    key (see :func:`mlir_artifact_for`).
    """
    op = op.resolved(dev).copy()  # a build binds streams; each gets its own
    if op.external is not None:
        # A downloaded image: no array to build, only the sequence against
        # its pins. external imports this package, so the name is local.
        from ..external import build_external

        return build_external(dev, op)
    target = Target(dev, kernels_dir, trace_size, image)

    # Per-call values get their device parameters before the array is built,
    # so a core-read value can be handed to a worker by array().
    # On a full ELF they are scratchpad parameters; on an xclbin, which has
    # no scratchpad (spike S2), every one is a dispatch-time scalar of the
    # sequence, handed in by the generator's keyword parameters (see
    # ``mlir_artifact_for``), and DispatchTime members are always that.
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
                f"package as xclbin (OPERATOR_MODEL_PLAN.md §6, §8)"
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
        seq = Sequence(op, rt_data)
        seq.preamble(target)
        seq.run()
        # A declared stream slot this extent never transfers on (mem_copy's
        # idle cores at a small size) still needs a shim endpoint, or the
        # program cannot be resolved. Place it on any shim tile.
        idle = [h for h in handles if id(h) not in seq.used]
        if idle:
            for h in idle:
                h.endpoint = RuntimeEndpoint(AnyShimTile)
                rt._fifos.add(h)

    rt = Runtime(sequence, fn_args + params)
    prog = Program(op.device(target), rt, workers=workers)
    if trace_size:
        maybe_enable_trace(prog, trace_size, workers)
    return prog.resolve_program()


def _design_code(op: Operator) -> str:
    """A digest of the operator's class source, its declared bases included,
    for the cache key.

    ``CompilableDesign`` hashes the design function by its code, and that
    function is :func:`build_design` for every declared operator. The code
    that varies is the classes', so it is hashed here.
    """
    h = hashlib.sha256()
    for cls in reversed(type(op).__mro__):
        if not issubclass(cls, Operator) or cls is Operator:
            continue
        try:
            h.update(inspect.getsource(cls).encode())
        except (OSError, TypeError):
            h.update(cls.__qualname__.encode())
    return h.hexdigest()[:24]


def dispatch_parameters(op: Operator) -> list[tuple[str, Any]]:
    """The (symbol, dtype) of every per-call value, as dispatch-time scalars."""
    return [(device_symbol(op, v), v.dtype) for v in op.values]


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
            # Passed explicitly rather than read from the operator: the
            # device reaches the cache key by identity, the kernel tree
            # by path (pointing IRON at another tree changes the key).
            "dev": op.dev,
            "kernels_dir": kernels_dir(),
            # The operator's own trace request inserts the trace flows; a
            # sequence's trace_size only keeps the lowered module to read.
            "trace_size": op.trace_size,
        },
    )
