# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a traced graph passes around in place of a buffer."""

from __future__ import annotations

from math import prod

import numpy as np
from ml_dtypes import bfloat16

from aie.utils import bfp

from ..declare import Operator, Overlay


class Handle:
    """A traced tensor: a buffer of the graph, with a shape and a dtype.

    Carries no data. ``h[a:b]`` is a static slice along the leading axis; it
    is a view into the parent's buffer, so it costs nothing at run time.
    """

    __slots__ = ("shape", "dtype", "name", "role", "parent", "start")

    def __init__(self, shape, dtype, name, role, parent=None, start=0):
        self.shape = tuple(int(s) for s in shape)
        self.dtype = dtype
        self.name = name
        self.role = role  # input | output | weight | state | intermediate | slice
        self.parent = parent
        self.start = start  # element offset into the parent, for a slice

    @property
    def elements(self) -> int:
        return prod(self.shape) if self.shape else 1

    @property
    def nbytes(self) -> int:
        return self.elements * bfp.itemsize(self.dtype)

    @property
    def buffer_name(self) -> str:
        """The name the runlist uses: a slice is ``parent[start:stop]`` in bytes."""
        if self.parent is None:
            return self.name
        item = bfp.itemsize(self.dtype)
        return f"{self.parent.buffer_name}[{self.start * item}:{(self.start + self.elements) * item}]"

    def reshape(self, *shape) -> "Handle":
        """The same buffer seen with another shape (no data moves)."""
        if len(shape) == 1 and isinstance(shape[0], (tuple, list)):
            shape = tuple(shape[0])
        if prod(shape) != self.elements:
            raise ValueError(f"cannot reshape {self!r} to {list(shape)}")
        return Handle(shape, self.dtype, self.name, self.role, self.parent, self.start)

    def __getitem__(self, index) -> "Handle":
        if self.parent is not None:
            raise TypeError("slicing a slice is not supported; slice the parent")
        n = self.shape[0]
        if isinstance(index, int):
            if not -n <= index < n:
                raise IndexError(f"index {index} out of range for {self.shape}")
            index = index % n
            start, stop, shape = index, index + 1, self.shape[1:]
        elif isinstance(index, slice):
            if index.step not in (None, 1):
                raise ValueError("only unit steps are supported")
            start, stop, _ = index.indices(n)
            if stop <= start:
                raise ValueError(f"empty slice {index}")
            shape = (stop - start,) + self.shape[1:]
        else:
            raise TypeError("a handle is sliced along its leading axis only")
        inner = prod(self.shape[1:]) if len(self.shape) > 1 else 1
        return Handle(shape, self.dtype, self.name, "slice", self, start * inner)

    def __repr__(self) -> str:
        return f"Handle({self.buffer_name!r}, {list(self.shape)}, {bfp.dtype_name(self.dtype)})"


class State:
    """A tensor that persists on the device across calls (a KV cache).

    Created outside the graph function with :func:`state` and closed over.
    Zero when the graph is first uploaded; read and written through
    :meth:`CompiledGraph.buffer`.
    """

    __slots__ = ("shape", "dtype", "name", "host")

    def __init__(self, shape, dtype=bfloat16, name=None):
        self.shape = tuple(int(s) for s in shape)
        self.dtype = dtype
        self.name = name
        self.host = None  # the reference path's copy, made on first use

    def __repr__(self) -> str:
        return f"State({self.name or ''}{list(self.shape)})"


def state(shape, dtype=bfloat16, name=None) -> State:
    """Declare device-resident state a graph function closes over."""
    return State(shape, dtype, name)


class Value:
    """A per-call scalar parameter of a graph function."""

    __slots__ = ("name", "kind", "dtype")

    def __init__(self, name, kind, dtype):
        self.name, self.kind, self.dtype = name, kind, dtype

    def __repr__(self) -> str:
        return f"Value({self.name!r}, {self.kind}[{np.dtype(self.dtype).name}])"


def is_operand(x) -> bool:
    """A graph handle, a state, or a host tensor (a weight)."""
    if isinstance(x, (Handle, State)):
        return True
    if isinstance(x, (Overlay, Operator, type)):
        return False
    return hasattr(x, "shape") and hasattr(x, "dtype")


def _tensor_dtype(t):
    dt = getattr(t, "dtype", None)
    name = str(dt)
    return {
        "bfloat16": bfloat16,
        "float32": np.float32,
        "int32": np.int32,
        "int8": np.int8,
        "uint8": np.uint8,
        "int16": np.int16,
    }.get(name, dt)
