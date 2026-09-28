# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a traced graph passes around in place of a buffer."""

from __future__ import annotations

import dataclasses
from collections.abc import Mapping
from math import prod

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.utils import bfp
from ml_dtypes import bfloat16

from ..declare import Operator
from ..declare.operator import graph_tracer


class Handle:
    """A traced tensor: a buffer of the graph, with a shape and a dtype.

    Carries no data. ``h[key]`` takes numpy's basic indexing (integers,
    unit-step slices, an ellipsis) and, on one axis, a per-call
    :class:`Value`: ``keys[:, pos]``. A contiguous static region is a slice:
    part of the parent's buffer, which any operator takes. Any other view
    (a strided region, a transpose, a per-call index) is an access pattern
    over the parent's buffer, which only a copy takes, since a DMA walks it.
    """

    __slots__ = (
        "shape",
        "dtype",
        "name",
        "role",
        "parent",
        "start",
        "tap",
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
        tap=None,
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
        # over the parent's buffer, for a view
        self.tap: TensorAccessPattern | None = tap
        # A per-call index, as the element offset it moves the view by.
        self.index_by: Affine | None = index_by
        # axis -> the count of that axis's leading entries valid this call
        # (``x[:n]``); the rest are padding.
        self.bounds: dict[int, Affine] = dict(bounds or {})

    @property
    def elements(self) -> int:
        return prod(self.shape) if self.shape else 1

    @property
    def nbytes(self) -> int:
        return self.elements * bfp.itemsize(self.dtype)

    @property
    def buffer_name(self) -> str:
        """The name the runlist uses: a slice is ``parent[start:stop]`` in bytes;
        a view is a pattern over its parent's buffer, so it is the parent's.
        """
        if self.parent is None:
            return self.name
        if self.tap is not None:
            return self.parent.buffer_name
        item = bfp.itemsize(self.dtype)
        return f"{self.parent.buffer_name}[{self.start * item}:{(self.start + self.elements) * item}]"

    def reshape(self, *shape) -> "Handle":
        """The same buffer seen with another shape (no data moves)."""
        if len(shape) == 1 and isinstance(shape[0], (tuple, list)):
            shape = tuple(shape[0])
        if prod(shape) != self.elements:
            raise ValueError(f"cannot reshape {self!r} to {list(shape)}")
        if self.tap is not None:
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
        if self.tap is not None:
            raise ValueError(
                f"cannot transpose a view {self!r}; transpose what it views"
            )
        if sorted(axes) != list(range(len(self.shape))):
            raise ValueError(
                f"axes {axes} do not permute a shape of rank {len(self.shape)}"
            )
        whole = TensorAccessPattern.from_slice(self.shape, ())
        shape = tuple(self.shape[a] for a in axes)
        tap = TensorAccessPattern(
            self.shape, 0, shape, [whole.strides[a] for a in axes]
        )
        bounds = {axes.index(axis): b for axis, b in self.bounds.items()}
        return Handle(shape, self.dtype, self.name, "view", self, 0, tap, bounds=bounds)

    def __getitem__(self, key) -> "Handle":
        if self.tap is not None or self.parent is not None:
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
            if isinstance(entry, slice) and isinstance(entry.stop, (Value, Affine)):
                # x[:n]: the first n along this axis are the valid ones.
                stop = entry.stop.affine()
                if entry.start not in (None, 0) or entry.step not in (None, 1):
                    raise ValueError(f"{stop} bounds an axis from its start: [:{stop}]")
                if stop.value.kind != "scratchpad":
                    raise ValueError(
                        f"{stop} is {stop.value.kind}; only a Scratchpad value can "
                        f"bound an axis, since it patches a transfer's size"
                    )
                # Keyed by the axis of the result: an index before it drops one.
                bounds[len(shape)] = stop
                static.append(slice(None))
                shape.append(n)
            elif isinstance(entry, (Value, Affine)):
                entry = entry.affine()
                if index_by is not None:
                    raise ValueError("one axis at most is indexed by a per-call value")
                if entry.value.kind != "scratchpad":
                    raise ValueError(
                        f"{entry} is {entry.value.kind}; only a Scratchpad value can "
                        f"index a view, since it moves a transfer's base address"
                    )
                index_by = entry * prod(self.shape[axis + 1 :])
                static.append(0)
            elif isinstance(entry, slice):
                if entry.step not in (None, 1):
                    raise ValueError("only unit steps are supported")
                static.append(entry)
                shape.append(len(range(*entry.indices(n))))
            else:
                static.append(int(entry))
        tap = TensorAccessPattern.from_slice(
            self.shape, tuple(static)
        )  # checks ranges, empties
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
        if index_by is None and tap.contiguous:
            return Handle(
                shape, self.dtype, self.name, "slice", self, tap.offset, bounds=bounds
            )
        return Handle(
            shape, self.dtype, self.name, "view", self, 0, tap, index_by, bounds=bounds
        )

    def __repr__(self) -> str:
        return f"Handle({self.buffer_name!r}, {list(self.shape)}, {bfp.dtype_name(self.dtype)})"


class State:
    """A tensor that persists on the device across calls (a KV cache).

    Created with :func:`state` and held by the graph.
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

    # Inside a graph's body a state is viewed like a handle: the tracer
    # decides what stands for it (a handle when tracing, its host tensor
    # when the reference runs).
    def _as_operand(self):
        tracer = graph_tracer.get()
        if tracer is None:
            raise TypeError(f"{self!r} is viewed inside a graph's body")
        return tracer.state_as(self)

    def __getitem__(self, key):
        return self._as_operand()[key]

    def reshape(self, *shape):
        return self._as_operand().reshape(*shape)

    def transpose(self, *axes):
        return self._as_operand().transpose(*axes)


def state(shape, dtype=bfloat16, name=None) -> State:
    """Declare device-resident state a graph holds."""
    return State(shape, dtype, name)


def _rescale_bounds(h: Handle, shape) -> dict[int, Affine]:
    """The bounds of ``h`` on its reshape to ``shape``: a bound on the leading
    axis survives when that axis is merged with the axes after it or split
    into leading ones, the count rescaled by the factor.
    """
    if not h.bounds:
        return {}
    (axis, count), *more = h.bounds.items()
    if more or axis != 0:
        raise ValueError(
            f"cannot reshape {h!r}: a bound is carried through a reshape on the "
            f"leading axis only"
        )
    old, new = h.shape[0], int(shape[0])
    if new % old == 0:
        # Each row becomes new // old rows: as many more of them are valid.
        return {0: count * (new // old)}
    group = old // new
    if old % new == 0 and count.scale % group == 0 and count.bias % group == 0:
        # Rows are grouped old // new to a row: as many fewer are valid.
        return {0: Affine(count.value, count.scale // group, count.bias // group)}
    raise ValueError(
        f"cannot reshape {h!r} to {list(shape)}: the bound on its leading axis "
        f"({count}) does not divide into the new leading axis"
    )


class Value:
    """A per-call scalar parameter of a graph's body.

    Integer arithmetic on one makes an :class:`Affine`: ``position + 1`` or
    ``chunk * 32`` is what an operator is bound to, and the graph computes
    it from ``position`` on every call.
    """

    __slots__ = ("name", "kind", "dtype")

    def __init__(self, name, kind, dtype):
        self.name, self.kind, self.dtype = name, kind, dtype

    def affine(self) -> Affine:
        """This value as an expression: itself, once."""
        return Affine(self)

    def __add__(self, k: int) -> Affine:
        return self.affine() + k

    def __sub__(self, k: int) -> Affine:
        return self.affine() - k

    def __mul__(self, k: int) -> Affine:
        return self.affine() * k

    __radd__, __rmul__ = __add__, __mul__

    def __repr__(self) -> str:
        return f"Value({self.name!r}, {self.kind}[{np.dtype(self.dtype).name}])"


@dataclasses.dataclass(frozen=True)
class Affine:
    """``scale * value + bias`` over the integers: what a binding writes.

    Closed under adding and multiplying by integers, so ``(p + 1) * 64`` is
    ``Affine(p, 64, 64)``. Evaluated per call from the graph's values.
    """

    value: Value
    scale: int = 1
    bias: int = 0

    def affine(self) -> Affine:
        return self

    def __add__(self, k: int) -> Affine:
        if not isinstance(k, (int, np.integer)):
            return NotImplemented
        return Affine(self.value, self.scale, self.bias + int(k))

    def __sub__(self, k: int) -> Affine:
        return self + (-k)

    def __mul__(self, k: int) -> Affine:
        if not isinstance(k, (int, np.integer)):
            return NotImplemented
        return Affine(self.value, self.scale * int(k), self.bias * int(k))

    __radd__, __rmul__ = __add__, __mul__

    @property
    def dtype(self):
        return self.value.dtype

    @property
    def name(self) -> str:
        """An identifier for the expression: ``p``, ``p_x64``, ``p_x64_p64``,
        ``p_m1`` (a device symbol carries it, so it names the word).
        """
        text = self.value.name + (f"_x{self.scale}" if self.scale != 1 else "")
        if self.bias:
            text += f"_{'p' if self.bias > 0 else 'm'}{abs(self.bias)}"
        return text

    def evaluate(self, values: Mapping[str, int]) -> int:
        """The number this expression is for the graph's ``values``, by name."""
        return self.scale * int(values[self.value.name]) + self.bias

    def __str__(self) -> str:
        text = self.value.name + (f" * {self.scale}" if self.scale != 1 else "")
        if self.bias:
            text += f" {'+' if self.bias > 0 else '-'} {abs(self.bias)}"
        return text


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
