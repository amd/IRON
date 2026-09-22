# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The operator model's declaration layer: overlays, operators, and their members.

An operator's fields sort by what a change rebuilds. Fields that configure the
array (tile shapes, columns, dtypes, kernel flags) live on an :class:`Overlay`;
fields that size the host buffers (extents, batch counts) live on an
:class:`Operator` declared against that overlay; values that change per call
are :class:`Scratchpad` or :class:`DispatchTime` members. Each layer has an
ABI: the overlay's is its **streams** (in tile units), the operator's is its
**buffers** (in extents), and a buffer names the stream it feeds or drains, so
direction, dtype, tile shape and shim binding agree by construction.

Declarations are class-level. A dimension is a dataclass field declared with
:func:`dim`, a tuning knob is one declared with :func:`tunable`, and a shape is
written in the class body using the field's bare name::

    @operator
    class GEMVOverlay(Overlay):
        K: int = dim()
        num_aie_columns: int = tunable(8)
        tile_size_output: int = tunable(64)

        a = StreamIn(tile_size_output, K, per=num_aie_columns)
        b = StreamIn(K, broadcast=True)
        c = StreamOut(tile_size_output, per=num_aie_columns)

    @operator
    class GEMV(Operator[GEMVOverlay]):
        M: int = dim()
        num_batches: int = dim(1)

        A = In(optional(num_batches), M, GEMVOverlay.K, to=GEMVOverlay.a)
        B = In(optional(num_batches), GEMVOverlay.K, to=GEMVOverlay.b)
        C = Out(optional(num_batches), M, from_=GEMVOverlay.c)

The shape rule: a host buffer's dimension is a ``dim()`` field or an integer
literal, nothing else. Not a tunable, not a per-call value, not an
expression. That is what makes inference a lookup (:meth:`Operator.infer`)
and what lets the checks in :mod:`.decorator` run once, at class creation.
A stream's tile dimension may also be a tunable: choosing the tile is what
tuning is for, and inference never reads a stream.

Nothing here imports mlir-aie. Everything that generates MLIR lives in
:mod:`iron.common.build`, which reads the declarations made here.

The package reads bottom-up: :mod:`.field` is what a class body writes,
:mod:`.member` what it declares alongside its fields, :mod:`.bound` what an
instance's attribute gives back, :mod:`.overlay` and :mod:`.operator` the two
layers themselves, and :mod:`.decorator` the checks both go through at class
creation. :mod:`.naming` is how either one spells its own label.
"""

from .bound import (
    BoundBuffer,
    BoundResident,
    BoundStream,
    BoundValue,
    BufferView,
)
from .decorator import operator
from .field import (
    DeclarationError,
    DimRef,
    Incompatible,
    Untunable,
    dim,
    optional,
    select,
    tunable,
)
from .member import (
    DispatchTime,
    In,
    InOut,
    Out,
    Resident,
    Scratchpad,
    Shim,
    StreamIn,
    StreamOut,
    ValueSpec,
    Xclbin,
)
from .operator import O, Operator
from .overlay import Overlay, get_shim_dma_limit

__all__ = [
    "BoundBuffer",
    "BoundResident",
    "BoundStream",
    "BoundValue",
    "BufferView",
    "DeclarationError",
    "DimRef",
    "DispatchTime",
    "In",
    "InOut",
    "Incompatible",
    "O",
    "Operator",
    "Out",
    "Overlay",
    "Resident",
    "Scratchpad",
    "Shim",
    "StreamIn",
    "StreamOut",
    "Untunable",
    "ValueSpec",
    "Xclbin",
    "dim",
    "get_shim_dma_limit",
    "operator",
    "optional",
    "select",
    "tunable",
]
