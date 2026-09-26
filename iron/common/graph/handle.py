# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a traced graph passes around in place of a buffer."""

from __future__ import annotations

from math import prod

import numpy as np
from aie.utils import bfp
from ml_dtypes import bfloat16

from ..declare import Operator
from ..tiling import Walk


class Handle:
    """A traced tensor: a buffer of the graph, with a shape and a dtype.

    Carries no data. ``h[key]`` takes numpy's basic indexing (integers,
    unit-step slices, an ellipsis) and, on one axis, a per-call
    :class:`Value`: ``keys[:, pos]``. A contiguous static region is a slice:
    part of the parent's buffer, which any operator takes. Any other view
    (a strided region, a transpose, a per-call index) is a walk over the
    parent's buffer, which only a copy takes, since a DMA walks it.
    """

    __slots__ = (
        "shape",
        "dtype",
        "name",
        "role",
        "parent",
        "start",
        "walk",
        "index_by",
        "bounds",
    )

    def __init__(
        self,
        shape,
        dtype,
        name,
        role,
        parent=None,
        start=0,
        walk=None,
        index_by=None,
        bounds=None,
    ):
        self.shape = tuple(int(s) for s in shape)
        self.dtype = dtype
        self.name = name
        # input | output | weight | state | intermediate | slice | view
        self.role = role
        self.parent = parent
        self.start = start  # element offset into the parent, for a slice
        self.walk: Walk | None = walk  # over the parent's buffer, for a view
        self.index_by: tuple[Value, int] | None = index_by  # (value, axis stride)
        # axis -> (value, scale): the first value * scale entries of that axis
        # are the valid ones this call (``x[:n]``); the rest are padding.
        self.bounds: dict[int, tuple[Value, int]] = dict(bounds or {})

    @property
    def elements(self) -> int:
        return prod(self.shape) if self.shape else 1

    @property
    def nbytes(self) -> int:
        return self.elements * bfp.itemsize(self.dtype)

    @property
    def buffer_name(self) -> str:
        """The name the runlist uses: a slice is ``parent[start:stop]`` in bytes;
        a view is walked over its parent's buffer, so it is the parent's.
        """
        if self.parent is None:
            return self.name
        if self.walk is not None:
            return self.parent.buffer_name
        item = bfp.itemsize(self.dtype)
        return f"{self.parent.buffer_name}[{self.start * item}:{(self.start + self.elements) * item}]"

    def reshape(self, *shape) -> "Handle":
        """The same buffer seen with another shape (no data moves)."""
        if len(shape) == 1 and isinstance(shape[0], (tuple, list)):
            shape = tuple(shape[0])
        if prod(shape) != self.elements:
            raise ValueError(f"cannot reshape {self!r} to {list(shape)}")
        if self.walk is not None:
            raise ValueError(f"cannot reshape a view {self!r}; reshape what it views")
        bounds = _rescale_bounds(self, shape)
        return Handle(
            shape,
            self.dtype,
            self.name,
            self.role,
            self.parent,
            self.start,
            bounds=bounds,
        )

    def transpose(self, *axes) -> "Handle":
        """The same buffer walked with its axes permuted (no data moves)."""
        if len(axes) == 1 and isinstance(axes[0], (tuple, list)):
            axes = tuple(axes[0])
        if self.walk is not None:
            raise ValueError(
                f"cannot transpose a view {self!r}; transpose what it views"
            )
        walk = Walk.permuted(self.shape, axes)
        shape = tuple(self.shape[a] for a in axes)
        bounds = {axes.index(axis): b for axis, b in self.bounds.items()}
        return Handle(
            shape, self.dtype, self.name, "view", self, 0, walk, bounds=bounds
        )

    def __getitem__(self, key) -> "Handle":
        if self.walk is not None or self.parent is not None:
            raise TypeError("slicing a slice is not supported; slice the parent")
        entries = list(key) if isinstance(key, tuple) else [key]
        rank = len(self.shape)
        if entries.count(Ellipsis) > 1:
            raise IndexError("an index can only have a single ellipsis ('...')")
        if Ellipsis in entries:
            at = entries.index(Ellipsis)
            fill = [slice(None)] * (rank - (len(entries) - 1))
            entries = entries[:at] + fill + entries[at + 1 :]
        if len(entries) > rank:
            raise IndexError(f"too many indices for shape {self.shape}")
        entries += [slice(None)] * (rank - len(entries))
        # A bounded axis may be indexed (one row of it, ``x[last]``), which
        # drops the bound; it may not be sliced again.
        for axis in self.bounds:
            if isinstance(entries[axis], slice):
                raise TypeError(
                    f"{self!r} is bounded per call on axis {axis}; index it or "
                    f"slice what it bounds"
                )
        index_by = None
        static, shape, bounds = [], [], {}
        for axis, (entry, n) in enumerate(zip(entries, self.shape)):
            if isinstance(entry, slice) and isinstance(entry.stop, Value):
                # x[:n]: the first n along this axis are the valid ones.
                if entry.start not in (None, 0) or entry.step not in (None, 1):
                    raise ValueError(
                        f"{entry.stop.name} bounds an axis from its start: [:{entry.stop.name}]"
                    )
                if entry.stop.kind != "scratchpad":
                    raise ValueError(
                        f"{entry.stop.name} is {entry.stop.kind}; only a Scratchpad "
                        f"value can bound an axis, since it patches a transfer's size"
                    )
                bounds[axis] = (entry.stop, 1)
                static.append(slice(None))
                shape.append(n)
            elif isinstance(entry, Value):
                if index_by is not None:
                    raise ValueError("one axis at most is indexed by a per-call value")
                if entry.kind != "scratchpad":
                    raise ValueError(
                        f"{entry.name} is {entry.kind}; only a Scratchpad value can "
                        f"index a view, since it moves a transfer's base address"
                    )
                index_by = (entry, prod(self.shape[axis + 1 :]))
                static.append(0)
            elif isinstance(entry, slice):
                if entry.step not in (None, 1):
                    raise ValueError("only unit steps are supported")
                static.append(entry)
                shape.append(len(range(*entry.indices(n))))
            else:
                static.append(int(entry))
        walk = Walk.slice(self.shape, tuple(static))  # checks ranges, empties
        if bounds and tuple(shape) == self.shape:
            # The whole buffer, bounded: the same handle with the bound on it.
            return Handle(
                self.shape,
                self.dtype,
                self.name,
                self.role,
                self.parent,
                self.start,
                bounds=bounds,
            )
        if index_by is None and walk.contiguous:
            return Handle(
                shape, self.dtype, self.name, "slice", self, walk.offset, bounds=bounds
            )
        return Handle(
            shape, self.dtype, self.name, "view", self, 0, walk, index_by, bounds=bounds
        )

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
        # The reference path's copy, made on first use.
        self.host: np.ndarray | None = None

    def __repr__(self) -> str:
        return f"State({self.name or ''}{list(self.shape)})"

    # Inside a graph function a state is viewed like a handle: the tracer
    # decides what stands for it (a handle when tracing, its host tensor
    # when the reference runs).
    def _as_operand(self):
        from .trace import current  # imports this module

        tracer = current()
        if tracer is None:
            raise TypeError(f"{self!r} is viewed inside a graph function")
        return tracer.state_as(self)

    def __getitem__(self, key):
        return self._as_operand()[key]

    def reshape(self, *shape):
        return self._as_operand().reshape(*shape)

    def transpose(self, *axes):
        return self._as_operand().transpose(*axes)


def state(shape, dtype=bfloat16, name=None) -> State:
    """Declare device-resident state a graph function closes over."""
    return State(shape, dtype, name)


def _rescale_bounds(h: Handle, shape) -> dict[int, tuple["Value", int]]:
    """The bounds of ``h`` on its reshape to ``shape``: a bound on the leading
    axis survives when that axis is merged with the axes after it or split
    into leading ones, the count rescaled by the factor.
    """
    if not h.bounds:
        return {}
    (axis, (value, scale)), *more = h.bounds.items()
    if more or axis != 0:
        raise ValueError(
            f"cannot reshape {h!r}: a bound is carried through a reshape on the "
            f"leading axis only"
        )
    old, new = h.shape[0], int(shape[0])
    if new == old:
        return {0: (value, scale)}
    if new % old == 0:
        # Each row becomes new // old rows: as many more of them are valid.
        return {0: (value, scale * (new // old))}
    if old % new == 0 and scale % (old // new) == 0:
        # Rows are grouped old // new to a row: as many fewer are valid.
        return {0: (value, scale // (old // new))}
    raise ValueError(
        f"cannot reshape {h!r} to {list(shape)}: the bound on its leading axis "
        f"({value.name} x {scale}) does not divide into the new leading axis"
    )


class Value:
    """A per-call scalar parameter of a graph function."""

    __slots__ = ("name", "kind", "dtype")

    def __init__(self, name, kind, dtype):
        self.name, self.kind, self.dtype = name, kind, dtype

    def __repr__(self) -> str:
        return f"Value({self.name!r}, {self.kind}[{np.dtype(self.dtype).name}])"


def is_operand(x) -> bool:
    """A graph handle, a state (or a view of one), or a host tensor (a weight)."""
    if isinstance(x, (Handle, State, _HostView)):
        return True
    if isinstance(x, (Operator, type)):
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


class _HostViews:
    """A state as the reference views it: ``[key]`` keeps the key for the
    operator; a reshape or transpose is numpy's own view of the host tensor.
    """

    def __init__(self, state: State) -> None:
        self.state = state

    def __getitem__(self, key):
        return _HostView(self.state, key)

    def reshape(self, *shape):
        assert self.state.host is not None
        return self.state.host.reshape(*shape)

    def transpose(self, *axes):
        assert self.state.host is not None
        return self.state.host.transpose(*axes)


class _HostView:
    def __init__(self, state: State, key) -> None:
        self.state, self.key = state, key
