# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a traced graph passes around in place of a buffer."""

from __future__ import annotations

import dataclasses
from collections.abc import Iterator, Mapping
from math import prod

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.utils import bfp
from ml_dtypes import bfloat16

from ..declare.operator import graph_tracer


class Handle:
    """A traced tensor: a buffer of the graph, with a shape and a dtype.

    ``h[key]`` takes numpy's basic indexing and, on one axis, a per-call
    ``Value`` (``keys[:, pos]``). A contiguous static region is a slice any
    operator takes; any other view is an access pattern only a copy takes.
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
        shape = tuple(self.shape[a] for a in axes)
        tap = TensorAccessPattern.full(self.shape).permute(axes)
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
        tap = TensorAccessPattern.full(self.shape)[
            tuple(static)
        ]  # checks ranges, empties
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
        dense = tap.coalesce()
        offset = tap.offset
        if (
            index_by is None
            and isinstance(offset, (int, np.integer))
            and dense.rank == 1
            and 1 in (dense.sizes[0], dense.strides[0])
        ):
            return Handle(
                shape, self.dtype, self.name, "slice", self, int(offset), bounds=bounds
            )
        return Handle(
            shape, self.dtype, self.name, "view", self, 0, tap, index_by, bounds=bounds
        )

    def __repr__(self) -> str:
        return f"Handle({self.buffer_name!r}, {list(self.shape)}, {bfp.dtype_name(self.dtype)})"


class _Viewed:
    """A tensor the graph holds, viewed inside its body like a handle
    (``keys[:, pos]``): the tracer decides what stands for it, a handle when
    tracing, its host tensor when the reference runs.
    """

    __slots__ = ()

    def _as_operand(self):
        tracer = graph_tracer.get()
        if tracer is None:
            raise TypeError(f"{self!r} is viewed inside a graph's body")
        return tracer.viewed(self)

    def __getitem__(self, key):
        return self._as_operand()[key]

    def reshape(self, *shape):
        return self._as_operand().reshape(*shape)

    def transpose(self, *axes):
        return self._as_operand().transpose(*axes)


class State(_Viewed):
    """A tensor that persists on the device across calls (a KV cache).

    Created with ``state`` and held by the graph.
    Zero when the graph is first uploaded; read and written through
    ``CompiledGraph.buffer``.
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


def state(shape, dtype=bfloat16, name=None) -> State:
    """Declare device-resident state a graph holds."""
    return State(shape, dtype, name)


class Weight(_Viewed):
    """A weight the graph's body views, ``rope[position]``: uploaded once,
    as any tensor the graph holds is, and viewed as a state is. Created with
    ``weight``.
    """

    __slots__ = ("array",)

    def __init__(self, array):
        self.array = np.asarray(array)

    @property
    def shape(self) -> tuple[int, ...]:
        return self.array.shape

    @property
    def dtype(self):
        return self.array.dtype

    def __array__(self, dtype=None, copy=None):
        return self.array if dtype is None else self.array.astype(dtype)

    def __repr__(self) -> str:
        return f"Weight({list(self.shape)}, {bfp.dtype_name(self.dtype)})"


def weight(array) -> Weight:
    """Declare a weight a graph's body views, not only passes whole."""
    return Weight(array)


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

    Integer arithmetic on one makes an ``Affine``: ``position + 1`` or
    ``chunk * 32`` is what an operator is bound to, and the graph computes
    it from ``position`` on every call. A ``carried`` one the graph computes
    for its own next call (``Carried``).
    """

    __slots__ = ("name", "kind", "dtype", "carried")

    def __init__(self, name, kind, dtype, carried: bool = False):
        self.name, self.kind, self.dtype = name, kind, dtype
        self.carried = carried

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
        kind = f"carried {self.kind}" if self.carried else self.kind
        return f"Value({self.name!r}, {kind}[{np.dtype(self.dtype).name}])"


@dataclasses.dataclass(frozen=True)
class Affine:
    """An integer expression in one graph value ``v``, evaluated per call:

    ```text
    ((v * scale + bias) >> down) * mul + add
    ```

    where ``>>`` floors. A binding writes a linear one (``down`` 0, kept in
    ``scale`` and ``bias``, so ``(p + 1) * 64`` is ``Affine(p, 64, 64)``).
    Sums, products and floor divisions by a power of two (and so
    ``ceildiv``) with integers are expressions too, which is how an
    operator's derivation run on its bound gives the Emit row of what it
    derives; anything else (a comparison, two expressions, another divisor)
    raises ``TypeError``.
    """

    value: Value
    scale: int = 1
    bias: int = 0
    down: int = 0
    mul: int = 1
    add: int = 0

    def affine(self) -> Affine:
        """This expression, which a binding takes only while it is linear.

        Raises:
            TypeError: it floors.
        """
        if self.down:
            raise TypeError(f"{self} is not linear in {self.value.name}")
        return self

    def __add__(self, k: int) -> Affine:
        if isinstance(k, bool) or not isinstance(k, (int, np.integer)):
            return NotImplemented
        if self.down:
            return dataclasses.replace(self, add=self.add + int(k))
        return dataclasses.replace(self, bias=self.bias + int(k))

    def __sub__(self, k: int) -> Affine:
        return self + (-k)

    def __rsub__(self, k: int) -> Affine:
        return -self + k

    def __neg__(self) -> Affine:
        return self * -1

    def __mul__(self, k: int) -> Affine:
        if isinstance(k, bool) or not isinstance(k, (int, np.integer)):
            return NotImplemented
        k = int(k)
        if self.down:
            return dataclasses.replace(self, mul=self.mul * k, add=self.add * k)
        return dataclasses.replace(self, scale=self.scale * k, bias=self.bias * k)

    __radd__, __rmul__ = __add__, __mul__

    def __floordiv__(self, d: int) -> Affine:
        if isinstance(d, bool) or not isinstance(d, (int, np.integer)):
            return NotImplemented
        d = int(d)
        if d < 0:
            return (-self) // -d
        if d == 0 or d & (d - 1):
            raise TypeError(f"no expression for a floor division by {d}")
        k = d.bit_length() - 1
        if not self.down:
            return dataclasses.replace(self, down=k)
        # floor((floor(u / 2^a) + c) / 2^k) = floor((u + c 2^a) / 2^(a+k))
        if self.mul == 1:
            bias = self.bias + (self.add << self.down)
            return Affine(self.value, self.scale, bias, self.down + k)
        if self.mul % d == 0:  # the floored term divides exactly
            return dataclasses.replace(self, mul=self.mul // d, add=self.add // d)
        raise TypeError(f"no expression for ({self}) // {d}")

    def __bool__(self):
        raise TypeError(f"{self} has no truth value: it is computed per call")

    def __index__(self):
        raise TypeError(f"{self} is not a number: it is computed per call")

    __int__ = __index__

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
        v = int(values[self.value.name])
        return ((self.scale * v + self.bias) >> self.down) * self.mul + self.add

    def __str__(self) -> str:
        text = self.value.name + (f" * {self.scale}" if self.scale != 1 else "")
        if self.bias:
            text += f" {'+' if self.bias > 0 else '-'} {abs(self.bias)}"
        if self.down:
            text = f"({text}) >> {self.down}"
            if self.mul != 1:
                text = f"({text}) * {self.mul}"
            if self.add:
                text += f" {'+' if self.add > 0 else '-'} {abs(self.add)}"
        return text


class Carry(Mapping[str, "Handle | Affine | int"]):
    """The next values of a graph's carried values, by name: what
    ``carry`` makes.

    Traced, each is an ``Affine`` of the current values or a
    one-element integer ``Handle`` the graph computed. Returned from a
    call, each is the number the next call takes.
    """

    __slots__ = ("_next",)

    def __init__(self, **next_values: Handle | Affine | Value | int):
        self._next: dict[str, Handle | Affine | int] = {
            name: v.affine() if isinstance(v, (Value, Affine)) else v
            for name, v in next_values.items()
        }

    def __getitem__(self, name: str) -> Handle | Affine | int:
        return self._next[name]

    def __iter__(self) -> Iterator[str]:
        return iter(self._next)

    def __len__(self) -> int:
        return len(self._next)

    def __repr__(self) -> str:
        items = ", ".join(f"{k}={v!r}" for k, v in self._next.items())
        return f"Carry({items})"


def carry(**next_values: Handle | Affine | Value | int) -> Carry:
    """Return with a graph's outputs the next value of each carried value:
    ``return logits, iron.carry(token=sampled, position=position + 1)``.
    """
    return Carry(**next_values)


def is_operand(x) -> bool:
    """A graph handle, a state or weight (or a view of one), or a host tensor."""
    return isinstance(x, (Handle, State, Weight, _HostView, np.ndarray, np.generic))


def _tensor_dtype(t):
    dt = t.dtype
    name = str(dt)
    return {
        "bfloat16": bfloat16,
        "float32": np.float32,
        "int32": np.int32,
        "int8": np.int8,
        "uint8": np.uint8,
        "int16": np.int16,
    }.get(name, dt)


class _HostView:
    """A state as the reference views it: reshaped, then indexed, both kept,
    so an operator that takes views gets the whole host tensor and the
    pattern (``pattern``) and writes it in place, as the device does. A
    transpose is numpy's own view of the host tensor.
    """

    def __init__(self, state: State, shape, key=None) -> None:
        self.state, self.shape, self.key = state, tuple(shape), key

    def __getitem__(self, key):
        if self.key is not None:
            raise TypeError(f"a view of {self.state!r} is indexed once")
        return _HostView(self.state, self.shape, key)

    def reshape(self, *shape):
        if self.key is not None:
            raise ValueError(f"cannot reshape a view of {self.state!r}")
        if len(shape) == 1 and isinstance(shape[0], (tuple, list)):
            shape = tuple(shape[0])
        return _HostView(self.state, shape)

    def transpose(self, *axes):
        return self.tensor().transpose(*axes)

    def pattern(self) -> Handle:
        """The view as the traced graph has it, over the state's buffer."""
        s = self.state
        whole = Handle(s.shape, s.dtype, s.name, "state").reshape(self.shape)
        return whole if self.key is None else whole[self.key]

    def tensor(self) -> np.ndarray:
        """The host tensor, viewed by numpy."""
        assert self.state.host is not None
        view = self.state.host.reshape(self.shape)
        return view if self.key is None else view[self.key]
