# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The operator model's declaration layer: operators and their members.

An operator is one class. Its fields fall into two tiers by what a change
rebuilds. Fields named in an operand's tile, plus fields marked
``array=True``, form the array tier; one array serves every extent of the
other fields, which size the host buffers and reach only the runtime
sequence. Values a graph binds per call are :class:`Value`,
:class:`Scratchpad` or :class:`DispatchTime` members.

Declarations are class-level. :func:`param` declares a dimension field,
:func:`auto` declares a tunable the library resolves, and a shape in the class
body uses the field's bare name. An operand with ``tile=`` is its own
stream into the array::

    class GEMV(Operator):
        M: int = param()
        K: int = param()
        num_batches: int = param(default=1)
        num_aie_columns: int = auto()
        tile_size_output: int = auto(64)

        A = In(optional(num_batches), M, K, tile=(tile_size_output, K), per=(num_aie_columns,))
        B = In(optional(num_batches), K, tile=(K,), per=(num_aie_columns,))
        C = Out(optional(num_batches), M, tile=(tile_size_output,), per=(num_aie_columns,))
        tiles = Value(np.int32, derive=lambda op: op.M // (op.num_aie_columns * op.tile_size_output))

A host buffer's dimension is a ``param()`` field or an integer literal:
never a tunable, a per-call value or an expression. This keeps inference a
lookup (:mod:`.infer`) and lets :mod:`.creation` check a class once, as its
body finishes. A tile's dimension may also be a tunable, since resolution
chooses the tile and inference never reads one. A :class:`Profile` applied
in a scope fills the tunables a call site leaves open, by operator shape,
before resolution runs.

:mod:`iron.common.design` generates MLIR from these declarations, and
:mod:`iron.common.image` builds and runs it; this package does neither. The
little of mlir-aie it touches (the device a name is keyed on, the shim DMA
channels that bound :meth:`Operator.shim_columns`) describes the target,
not a design.

Module by module: :mod:`.field` is what a class body writes, :mod:`.member`
what it declares alongside its fields, :mod:`.bound` what an instance's
attribute returns, :mod:`.infer` how operand shapes fill a declaration's
dimension fields, :mod:`.operator` the class itself, and :mod:`.creation`
the checks run as a class body finishes.
"""

from .field import (
    DeclarationError,
    Incompatible,
    Unresolvable,
    auto,
    optional,
    param,
    select,
)
from .member import DispatchTime, Extent, In, Out, Scratchpad, Shim, Value, Xclbin
from .operator import Operator
from .profile import Profile

__all__ = [
    "DeclarationError",
    "DispatchTime",
    "Extent",
    "In",
    "Incompatible",
    "Operator",
    "Out",
    "Profile",
    "Scratchpad",
    "Shim",
    "Unresolvable",
    "Value",
    "Xclbin",
    "auto",
    "optional",
    "param",
    "select",
]
