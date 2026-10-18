# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a traced graph passes around in place of a buffer."""

from __future__ import annotations

import dataclasses
from collections.abc import Iterator, Mapping
from math import prod
from typing import Annotated, TypeVar

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.utils import bfp
from ml_dtypes import bfloat16

from ..declare.operand import slots
from ..declare.operator import graph_tracer
from ..image.packaging import Kind
from ..image.step import BufferRef

T = TypeVar("T")

Scratchpad = Annotated[T, Kind.SCRATCHPAD.value]
"""A per-call value patched into a DMA descriptor or read by a core.

Free per call (a few words and a sync), works under full ELF, cannot change a
DMA size or stride. Values are limited to 30 bits.
"""

Carried = Annotated[T, Kind.CARRIED.value]
"""A scratchpad value a graph computes for its own next call, returned last
with ``iron.carry(name=...)``: an integer expression of its values
(``position + 1``) or a one-element handle (a sampled token). The host writes
it only to seed the first call.
"""


class Handle:
    """A traced tensor: a buffer of the graph, with a shape and a dtype.

    ``h[key]`` takes numpy's basic indexing, on one axis a per-call
    value (``keys[:, pos]``), and on the leading axis an integer array
    of rows fixed when the graph is traced (``table[ids]``) or a 1-D integer
    handle naming the rows each call takes. A contiguous static region is a
    slice any operator takes; any other view, a gather included, is an
    access pattern only a copy takes.
    """

    __slots__ = (
        "shape",
        "dtype",
        "_name",
        "_role",
        "parent",
        "start",
        "tap",
        "index_by",
        "bounds",
        "gather_by",
        "repeat",
        "length",
        "window",
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
        gather_by=None,
        repeat=None,
        length=None,
        window=None,
    ):
        self.shape = tuple(int(s) for s in shape)
        self.dtype = dtype
        self.name = name
        self.role = role
        self.parent = parent
        self.start = start  # a slice's element offset into the parent
        # a gather's is one pattern per row
        self.tap: TensorAccessPattern | tuple[TensorAccessPattern, ...] | None = tap
        self.index_by: Affine | None = index_by  # a view's per-call element offset
        # axis -> its leading entries valid this call (``x[:n]``)
        self.bounds: dict[int, Affine] = {
            axis: n.affine() if isinstance(n, PerCall) else n
            for axis, n in (bounds or {}).items()
        }
        # The handle whose ids pick the rows each call, for a gather.
        self.gather_by: Handle | None = gather_by
        # A view's runs of each walk's first dimension, and entries of its
        # second, each call (``at``).
        self.repeat: tuple[Affine, ...] | None = repeat
        self.length: Affine | None = length
        # A run from a per-call start, ``x[s : s + W]``: its axis, s, W and
        # the axis's length, until a bound (``[:n]``) keeps it inside.
        self.window: tuple[int, Affine, int, int] | None = window

    @property
    def root(self) -> Handle:
        """The whole buffer this handle is, or is a slice or view of."""
        h = self
        while h.parent is not None:
            h = h.parent
        return h

    @property
    def name(self) -> str:
        """The name of the buffer: its root's."""
        return self.root._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def role(self) -> str:
        """input, output, weight, state or intermediate: its root's."""
        return self.root._role

    @role.setter
    def role(self, role: str) -> None:
        self._role = role

    @property
    def elements(self) -> int:
        return prod(self.shape) if self.shape else 1

    @property
    def nbytes(self) -> int:
        return self.elements * bfp.itemsize(self.dtype)

    def ref(self) -> BufferRef:
        """Where a step finds this handle: a slice is part of its parent's
        buffer, a view all of it.
        """
        if self.parent is None:
            return BufferRef(self.name)
        parent = self.parent.ref()
        if self.tap is not None:
            return parent
        start = parent.start + self.start * bfp.itemsize(self.dtype)
        return BufferRef(parent.root, start, self.nbytes)

    def reshape(self, *shape) -> "Handle":
        """The same buffer seen with another shape (no data moves)."""
        if len(shape) == 1 and isinstance(shape[0], (tuple, list)):
            shape = tuple(shape[0])
        if prod(shape) != self.elements:
            raise ValueError(f"cannot reshape {self!r} to {list(shape)}")
        if self.tap is not None or self.gather_by is not None:
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
        if self.tap is not None or self.gather_by is not None:
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
        return Handle(
            shape, self.dtype, self.name, self.role, self, 0, tap, bounds=bounds
        )

    @property
    def T(self) -> "Handle":
        """``transpose(1, 0)``, as numpy's ``.T`` of a matrix."""
        return self.transpose(1, 0)

    def _bound(self, key) -> "Handle":
        """A run from a per-call start bounded per call, ``x[s : s + W][:n]``:
        every call keeps ``s + n`` inside the axis, checked before it.
        """
        axis, start, width, n = self.window
        entries = list(key) if isinstance(key, tuple) else [key]
        entries += [slice(None)] * (len(self.shape) - len(entries))
        run = entries[axis]
        if (
            any(
                not isinstance(e, slice) or not e.start is e.stop is e.step is None
                for i, e in enumerate(entries)
                if i != axis
            )
            or not isinstance(run, slice)
            or run.start not in (None, 0)
            or run.step not in (None, 1)
            or not isinstance(run.stop, (PerCall, Affine))
        ):
            raise IndexError(
                f"{self!r} runs from a per-call start: bound its axis {axis} per "
                f"call from its start, [:n], and take every other axis whole"
            )
        stop = run.stop.affine()
        tracer = graph_tracer.get()
        if tracer is not None:
            tracer.limit(stop, 0, width + 1, self)
            tracer.limit(start, 0, n + 1, self, stop)
        return Handle(
            self.shape,
            self.dtype,
            self.name,
            self.role,
            self.parent,
            self.start,
            self.tap,
            self.index_by,
            {**self.bounds, axis: stop},
        )

    def __getitem__(self, key) -> "Handle":
        if self.window is not None:
            return self._bound(key)
        if self.tap is not None:
            raise TypeError(
                f"{self!r} is a view, which only a copy takes; index what it views"
            )
        if self.parent is not None:
            # A slice: indexed as a buffer of its own, then placed in its parent.
            whole = Handle(
                self.shape, self.dtype, self.name, self.role, bounds=self.bounds
            )
            return whole[key]._placed(self.parent, self.start)
        entries = list(key) if isinstance(key, tuple) else [key]
        rank = len(self.shape)
        # By identity: an array entry compares elementwise.
        ellipses = [i for i, e in enumerate(entries) if e is Ellipsis]
        if len(ellipses) > 1:
            raise IndexError("an index can only have a single ellipsis ('...')")
        if ellipses:
            at = ellipses[0]
            fill = [slice(None)] * (rank - (len(entries) - 1))
            entries = entries[:at] + fill + entries[at + 1 :]
        if len(entries) > rank:
            raise IndexError(f"too many indices for shape {self.shape}")
        entries += [slice(None)] * (rank - len(entries))
        if isinstance(entries[0], _Viewed):
            entries[0] = entries[0]._as_operand()
        if isinstance(entries[0], Handle):
            ids = entries[0]
            if (
                ids.tap is not None
                or len(ids.shape) != 1
                or not np.issubdtype(np.dtype(ids.dtype), np.integer)
                or rank < 2
            ):
                raise IndexError(
                    f"a gather per call takes a whole 1-D integer handle, or "
                    f"its first rows per call, as the rows of a table of rank 2 "
                    f"or more; got {ids!r} on {self!r}"
                )
            if not all(isinstance(e, slice) and e == slice(None) for e in entries[1:]):
                raise IndexError("a gather takes the whole of every axis but the first")
            if self.role not in ("weight", "state") or self.bounds:
                raise TypeError(
                    f"a gather per call reads a whole table the graph holds, not "
                    f"{self!r}"
                )
            shape = (ids.shape[0], *self.shape[1:])
            return Handle(
                shape, self.dtype, self.name, self.role, self, 0, gather_by=ids
            )
        if isinstance(entries[0], np.ndarray):
            ids, n = entries[0], self.shape[0]
            if ids.ndim != 1 or not np.issubdtype(ids.dtype, np.integer) or rank < 2:
                raise IndexError(
                    f"a gather takes a 1-D integer array of rows of a table of "
                    f"rank 2 or more; got {ids.dtype} {ids.shape} on {self!r}"
                )
            if not all(isinstance(e, slice) and e == slice(None) for e in entries[1:]):
                raise IndexError("a gather takes the whole of every axis but the first")
            if self.bounds:
                raise TypeError(f"{self!r} is bounded per call; gather what it bounds")
            if not len(ids) or ((ids < -n) | (ids >= n)).any():
                raise IndexError(f"gathering {ids} from the {n} rows of {self!r}")
            whole = TensorAccessPattern.full(self.shape)
            rows = tuple(whole[int(i) % n] for i in ids)
            shape = (len(ids), *self.shape[1:])
            return Handle(shape, self.dtype, self.name, self.role, self, 0, rows)
        for axis in self.bounds:
            if isinstance(entries[axis], slice) and entries[axis] != slice(None):
                raise TypeError(
                    f"{self!r} is bounded per call on axis {axis}; index it, take "
                    f"all of it, or slice what it bounds"
                )
        index_by = window = None
        static, shape, bounds = [], [], {}
        tracer = graph_tracer.get()
        for axis, (entry, n) in enumerate(zip(entries, self.shape)):
            if isinstance(entry, slice) and isinstance(entry.start, (PerCall, Affine)):
                # x[s : s + W]: a fixed width W from a per-call start s.
                start = entry.start
                start = start.affine() if isinstance(start, PerCall) else start
                stop = entry.stop
                stop = stop.affine() if isinstance(stop, PerCall) else stop
                width = None
                if isinstance(stop, Affine) and entry.step in (None, 1):
                    width = (
                        stop.add - start.add if start.down else stop.bias - start.bias
                    )
                    if stop != start + width:
                        width = None
                if width is None or not 0 < width <= n:
                    raise IndexError(
                        f"a run from a per-call start takes a fixed width, "
                        f"[s : s + W] with 0 < W <= {n}, not [{entry.start}:"
                        f"{entry.stop}]"
                    )
                if index_by is not None:
                    raise ValueError("one axis at most is indexed by a per-call value")
                if start.value.kind is Kind.DISPATCH_TIME:
                    raise ValueError(
                        f"{start} is a DispatchTime value; only a Scratchpad value can "
                        f"start a run, since it moves a transfer's base address"
                    )
                if tracer is not None:
                    tracer.limit(start, 0, n, self)
                index_by = start * prod(self.shape[axis + 1 :])
                window = (len(shape), start, width, n)
                static.append(slice(0, width))
                shape.append(width)
                continue
            if axis in self.bounds and isinstance(entry, slice):
                bounds[len(shape)] = self.bounds[axis]
                static.append(entry)
                shape.append(n)
            elif isinstance(entry, slice) and isinstance(entry.stop, (PerCall, Affine)):
                stop = entry.stop.affine()
                if entry.start not in (None, 0) or entry.step not in (None, 1):
                    raise ValueError(f"{stop} bounds an axis from its start: [:{stop}]")
                if stop.value.kind is Kind.DISPATCH_TIME:
                    raise ValueError(
                        f"{stop} is a DispatchTime value; only a Scratchpad value can "
                        f"bound an axis, since it patches a transfer's size"
                    )
                if tracer is not None:
                    tracer.limit(stop, 0, n + 1, self)
                # Keyed by the axis of the result: an index before it drops one.
                bounds[len(shape)] = stop
                static.append(slice(None))
                shape.append(n)
            elif isinstance(entry, (PerCall, Affine)):
                # An index may floor (a slot per chunk, ``position // C``).
                if isinstance(entry, PerCall):
                    entry = entry.affine()
                if index_by is not None:
                    raise ValueError("one axis at most is indexed by a per-call value")
                if entry.value.kind is Kind.DISPATCH_TIME:
                    raise ValueError(
                        f"{entry} is a DispatchTime value; only a Scratchpad value can "
                        f"index a view, since it moves a transfer's base address"
                    )
                if tracer is not None:
                    tracer.limit(entry, 0, n, self)
                index_by = entry * prod(self.shape[axis + 1 :])
                static.append(0)
            elif isinstance(entry, slice):
                if entry.step not in (None, 1):
                    raise ValueError("only unit steps are supported")
                static.append(entry)
                shape.append(len(range(*entry.indices(n))))
            else:
                static.append(int(entry))
        tap = TensorAccessPattern.full(self.shape)[tuple(static)]
        if bounds and index_by is None and tuple(shape) == self.shape:
            return Handle(
                self.shape,
                self.dtype,
                self.name,
                self.role,
                self.parent,
                self.start,
                bounds=bounds,
            )
        view = self._view(tap, shape, index_by, bounds)
        view.window = window
        return view

    def __setitem__(self, key, value) -> None:
        """``self[key] = value``: a copy of ``value`` into that view."""
        _write(self[key], value)

    def _placed(self, parent: Handle, start: int) -> Handle:
        """This handle of a buffer of its own, as the run of ``parent``
        from its element ``start``.

        Raises:
            TypeError: It gathers per call, which reads a whole table.
        """
        if self.gather_by is not None:
            raise TypeError(
                f"a gather per call reads a whole table, not a slice of {parent!r}"
            )
        tap = None
        if self.parent is not None and self.tap is None:
            start += self.start
        elif self.tap is not None:
            taps = self.tap if isinstance(self.tap, tuple) else (self.tap,)
            moved = tuple(
                TensorAccessPattern(parent.shape, t.offset + start, t.sizes, t.strides)
                for t in taps
            )
            start, tap = 0, moved if isinstance(self.tap, tuple) else moved[0]
        placed = Handle(
            self.shape,
            self.dtype,
            parent.name,
            parent.role,
            parent,
            start,
            tap,
            self.index_by,
            self.bounds,
        )
        placed.window = self.window
        return placed

    def at(
        self,
        tap: TensorAccessPattern | tuple[TensorAccessPattern, ...],
        shape,
        *,
        bounds=None,
        repeat=None,
        length=None,
    ):
        """What ``tap`` walks, as ``shape``: a slice if contiguous, else a view.

        ``repeat`` runs ``tap``'s first dimension that many times a call, and
        ``length`` takes that many entries of its second, each a per-call
        value; ``bounds`` then gives the rows the view moves a call. A tuple
        of patterns is walked in turn, each repeated by its entry of a tuple
        ``repeat``, all cut to one ``length``.

        Raises:
            ValueError: With ``repeat`` or ``length``, a pattern is not four
                dimensions one shim descriptor holds, the patterns and
                repeats differ in number, or no ``bounds``.
        """
        walks = tap if isinstance(tap, tuple) else (tap,)
        if isinstance(tap, tuple) and (
            not isinstance(repeat, tuple) or len(repeat) != len(tap)
        ):
            raise ValueError(
                f"{len(tap)} patterns walked in turn take a repeat each, not {repeat}"
            )
        if repeat is not None or length is not None:
            dev = aie_utils.get_current_device()
            for walk in walks:
                sizes, strides = slots(walk.sizes, walk.strides)
                padded = TensorAccessPattern(
                    walk.tensor_dims, walk.offset, sizes, strides
                )
                if (
                    walk.rank != 4
                    or dev is None
                    or not dev.dma_bd_fits(0, 0, padded, self.dtype)
                ):
                    raise ValueError(
                        f"{walk} takes a per-call repeat or length as one shim "
                        f"descriptor: four dimensions, the repeated first, within "
                        f"a descriptor's limits"
                    )
            if not bounds:
                raise ValueError(
                    f"a walk of {tap} by a per-call repeat or length bounds the "
                    f"rows it moves a call: give bounds"
                )
            repeats = None
            if repeat is not None:
                # A repeat count may be clamped; a length patches a size, linear.
                repeats = tuple(
                    r if isinstance(r, Affine) else r.affine()
                    for r in (repeat if isinstance(tap, tuple) else (repeat,))
                )
            length = None if length is None else length.affine()
            tracer = graph_tracer.get()
            if tracer is not None:
                for walk, r in zip(walks, repeats or ()):
                    tracer.limit(r, 1, walk.sizes[0] + 1, self)
                if length is not None:
                    hi = min(walk.sizes[1] for walk in walks)
                    tracer.limit(length, 1, hi + 1, self)
            return Handle(
                shape,
                self.dtype,
                self.name,
                self.role,
                self,
                0,
                tap,
                bounds=bounds,
                repeat=repeats,
                length=length,
            )
        return self._view(tap, shape, None, bounds)

    def _view(self, tap: TensorAccessPattern, shape, index_by, bounds) -> Handle:
        """What ``tap`` walks from the per-call element offset ``index_by``:
        a slice if contiguous and not offset per call, else a view.
        """
        dense = tap.coalesce()
        offset = tap.offset
        if (
            index_by is None
            and isinstance(offset, (int, np.integer))
            and dense.rank == 1
            and 1 in (dense.sizes[0], dense.strides[0])
        ):
            return Handle(
                shape,
                self.dtype,
                self.name,
                self.role,
                self,
                int(offset),
                bounds=bounds,
            )
        return Handle(
            shape,
            self.dtype,
            self.name,
            self.role,
            self,
            0,
            tap,
            index_by,
            bounds=bounds,
        )

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        """A held array on the left of an operator defers to the handle;
        any other numpy function on a handle is refused.
        """
        name = _OPERATORS.get(ufunc)
        if method == "__call__" and name and len(inputs) == 2 and not kwargs:
            a, b = inputs
            if a is self:
                return getattr(self, f"__{name}__")(b)
            if hasattr(self, f"__r{name}__"):
                return getattr(self, f"__r{name}__")(a)
        raise TypeError(
            f"numpy's {ufunc.__name__} cannot compute {self!r}: a handle is a "
            f"buffer of a traced graph. Use + - * / @ on it, iron.functional, "
            f"or an operator's step()"
        )

    def __add__(self, other) -> "Handle":
        """``self + other``, elementwise, or ``other`` a row added to every
        row, or a number added to every element.
        """
        from iron.operators.elementwise_add import ElementwiseAdd, RowwiseAdd

        return _broadcast(ElementwiseAdd, RowwiseAdd, self, other)

    def __mul__(self, other) -> "Handle":
        """``self * other``, elementwise, or every row times the row
        ``other``, or every element times a number.
        """
        from iron.operators.elementwise_mul import ElementwiseMul, RowwiseMul

        return _broadcast(ElementwiseMul, RowwiseMul, self, other)

    __radd__ = __add__
    __rmul__ = __mul__

    def __neg__(self) -> "Handle":
        return self * -1

    def __sub__(self, other) -> "Handle":
        """``self - other``: one AXPY step for a handle of this shape."""
        from iron.operators.axpy import AXPY

        if isinstance(other, _Viewed):
            other = other._as_operand()
        if isinstance(other, Handle) and other.shape == self.shape:
            return AXPY.step(other, self, scalar_factor=-1.0)
        return self + (-other)

    def __rsub__(self, other) -> "Handle":
        return -self + other

    def __truediv__(self, other) -> "Handle":
        """``self`` over a number, as ``self`` times its reciprocal."""
        if not _is_number(other):
            raise TypeError(f"{self!r} is divided by a number, not {other!r}")
        return self * (1 / other)

    def __matmul__(self, other) -> "Handle":
        """``self @ W.T``, ``W`` a weight as ``torch.nn.Linear`` stores it
        ``(out, in)``: ``iron.functional.linear(self, W)``.
        """
        import iron.functional as F

        return F.linear(self, _untransposed(self, other))

    def __rmatmul__(self, other) -> "Handle":
        """``W @ self``, ``self`` one row: ``iron.functional.linear(self, W)``."""
        import iron.functional as F

        if len(self.shape) != 1:
            raise TypeError(
                f"W @ {self!r} takes one row; for rows write x @ W.T, W (out, in)"
            )
        return F.linear(self, other)

    def __repr__(self) -> str:
        return f"Handle({str(self.ref())!r}, {list(self.shape)}, {bfp.dtype_name(self.dtype)})"


_OPERATORS = {
    np.add: "add",
    np.multiply: "mul",
    np.subtract: "sub",
    np.matmul: "matmul",
    np.true_divide: "truediv",
}


def _is_number(x) -> bool:
    return isinstance(x, (int, float, np.integer, np.floating)) and not isinstance(
        x, bool
    )


def _untransposed(x: Handle, w) -> Handle | np.ndarray:
    """``W``, given ``w`` its transpose ``W.T``: a held array's numpy
    transpose, or a weight handle's ``transpose()``.

    Raises:
        TypeError: ``w`` is not a 2-D weight's transpose.
    """
    if isinstance(w, np.ndarray) and w.ndim == 2 and w.T.flags.c_contiguous:
        return w.T
    if isinstance(w, _Viewed):
        w = w._as_operand()
    if (
        isinstance(w, Handle)
        and w.parent is not None
        and w.tap is not None
        and len(w.shape) == 2
        and w.parent.shape == w.shape[::-1]
    ):
        flipped = TensorAccessPattern.full(w.parent.shape).permute((1, 0))
        if (w.tap.offset, w.tap.sizes, w.tap.strides) == (
            flipped.offset,
            flipped.sizes,
            flipped.strides,
        ):
            return w.parent
    raise TypeError(
        f"{x!r} @ w takes w a weight's transpose, x @ W.T with W (out, in) as "
        f"torch.nn.Linear stores it; got {w!r:.80}"
    )


def _broadcast(whole, rowwise, x: Handle, y) -> Handle:
    """``whole`` of ``x`` and ``y`` of its shape, or, ``x`` of two axes or
    more, ``rowwise`` of ``x`` and ``y`` a row as wide as its last axis.

    Both are commutative, so a row handle times a matrix is the matrix's
    ``rowwise``. A number ``y`` is a row of it, one constant buffer per
    number, width and dtype (rounded to ``x``'s dtype).

    Raises:
        TypeError: ``y`` is neither.
    """
    if _is_number(y):
        tracer = graph_tracer.get()
        y = tracer.constant(y, x.shape[-1] if x.shape else 1, x.dtype)
    if len(x.shape) == 1 and len(getattr(y, "shape", ())) > 1:
        x, y = (y if isinstance(y, Handle) else graph_tracer.get().operand(y)), x
    shape = tuple(getattr(y, "shape", ()))
    if len(x.shape) > 1 and shape == x.shape[-1:]:
        rows = x.elements // shape[0]
        return rowwise.step(x.reshape(rows, shape[0]), y).reshape(x.shape)
    if shape == x.shape:
        return whole.step(x, y)
    raise TypeError(
        f"{whole.__name__} of {x!r} takes an operand of its shape or a row of "
        f"{x.shape[-1] if x.shape else 1}, not {type(y).__name__} {list(shape)}"
    )


def _write(view: Handle, value) -> None:
    from iron.operators.copy import Copy

    Copy.step(value, view)


class _Viewed:
    """A tensor the graph holds, viewed inside its body as the tracer says."""

    __slots__ = ()

    def _as_operand(self) -> Handle:
        tracer = graph_tracer.get()
        if tracer is None:
            raise TypeError(f"{self!r} is viewed inside a graph's body")
        return tracer.operand(self)

    def __getitem__(self, key):
        if isinstance(key, _Viewed):  # a gather by the ids a state holds
            key = key._as_operand()
        return self._as_operand()[key]

    def __setitem__(self, key, value) -> None:
        """``self[key] = value``: a copy of ``value`` into that view."""
        _write(self[key], value)

    def reshape(self, *shape):
        return self._as_operand().reshape(*shape)

    def transpose(self, *axes):
        return self._as_operand().transpose(*axes)

    @property
    def T(self):
        return self._as_operand().T

    def at(self, tap, shape, *, bounds=None, repeat=None, length=None):
        """``Handle.at`` of the tensor as the tracer views it."""
        return self._as_operand().at(
            tap, shape, bounds=bounds, repeat=repeat, length=length
        )


class State(_Viewed):
    """A tensor that persists on the device across calls (a KV cache), zero
    when first uploaded; read and written through ``CompiledGraph.read`` and
    ``write``, and held in ``host`` across ``Graph.reference`` calls.
    """

    __slots__ = ("shape", "dtype", "name", "host")

    def __init__(self, shape, dtype=bfloat16, name=None):
        self.shape = tuple(int(s) for s in shape)
        self.dtype = dtype
        self.name = name
        self.host: np.ndarray | None = None

    def __repr__(self) -> str:
        return f"State({self.name or ''}{list(self.shape)})"


def state(shape, dtype=bfloat16, name=None) -> State:
    """Declare device-resident state a graph holds."""
    return State(shape, dtype, name)


class Weight(_Viewed):
    """A tensor the body indexes per call (``iron.weight(table)[ids]``),
    one buffer with the array it wraps.
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
    """A tensor a graph's body indexes per call (``iron.weight(table)[ids]``)."""
    return Weight(array)


def _rescale_bounds(h: Handle, shape) -> dict[int, Affine]:
    """The bounds of ``h`` reshaped to ``shape``: a leading-axis bound,
    rescaled as that axis merges or splits.
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
        return {0: count * (new // old)}
    group = old // new
    if old % new == 0 and count.scale % group == 0 and count.bias % group == 0:
        return {0: Affine(count.value, count.scale // group, count.bias // group)}
    raise ValueError(
        f"cannot reshape {h!r} to {list(shape)}: the bound on its leading axis "
        f"({count}) does not divide into the new leading axis"
    )


class PerCall:
    """A per-call scalar parameter of a graph's body; integer arithmetic on
    one makes an ``Affine``.
    """

    __slots__ = ("name", "kind", "dtype")

    def __init__(self, name: str, kind: Kind, dtype):
        self.name, self.kind, self.dtype = name, kind, dtype

    def affine(self) -> Affine:
        return Affine(self)

    def __add__(self, k: int) -> Affine:
        return self.affine() + k

    def __sub__(self, k: int) -> Affine:
        return self.affine() - k

    def __mul__(self, k: int) -> Affine:
        return self.affine() * k

    __radd__, __rmul__ = __add__, __mul__

    def __rsub__(self, k: int) -> Affine:
        return k - self.affine()

    def __neg__(self) -> Affine:
        return -self.affine()

    def __floordiv__(self, d: int | Affine) -> Affine | int:
        return self.affine() // d

    def __mod__(self, m: int) -> Affine:
        return self.affine() % m

    def __eq__(self, other) -> bool:
        if isinstance(other, (PerCall, Affine)):
            return self is other
        raise TypeError(f"{self} has no value to compare: it is given per call")

    __hash__ = object.__hash__

    def __bool__(self):
        raise TypeError(f"{self} has no truth value: it is given per call")

    def __index__(self):
        raise TypeError(f"{self} is not a number: it is given per call")

    __int__ = __index__

    def __repr__(self) -> str:
        return f"PerCall({self.name!r}, {self.kind.name}[{np.dtype(self.dtype).name}])"


@dataclasses.dataclass(frozen=True)
class Affine:
    """An integer expression in one graph value ``v``, evaluated per call:

    ```text
    clamp(((v * scale + bias) >> down) * mul + add, lo, hi) % mod
    ```

    where ``>>`` floors, a bound of None is none and ``mod``, a power of
    two, wraps (a ring's row) where it is not None. A binding writes a
    linear one (``down`` 0, kept in ``scale`` and ``bias``, so
    ``(p + 1) * 64`` is ``Affine(p, 64, 64)``).
    Sums, products and floor divisions by a power of two (and so
    ``ceildiv``) with integers are expressions too, which is how an
    operator's derivation run on its bound gives the Emit row of what it
    derives. So are the sum and difference of two linear expressions in one
    value, and the quotient of two that are multiples of one another, an
    integer where the value cancels (``n - n`` is 0, ``(4 * n) // n`` is 4).
    ``clamp`` holds one to a range (``(p - 512).clamp(lo=0)``), which a sum,
    product or floor division by an integer carries. Anything else (a
    comparison, another divisor, two values) raises ``TypeError``.
    """

    value: PerCall
    scale: int = 1
    bias: int = 0
    down: int = 0
    mul: int = 1
    add: int = 0
    lo: int | None = None
    hi: int | None = None
    mod: int | None = None

    @property
    def clamped(self) -> bool:
        return self.lo is not None or self.hi is not None

    def clamp(self, lo: int | None = None, hi: int | None = None) -> Affine:
        """This expression held to ``[lo, hi]`` as well, a bound of None none."""
        if self.mod is not None:
            raise TypeError(f"no expression clamps ({self}) after it wraps")
        if lo is None or self.lo is not None and self.lo > lo:
            lo = self.lo
        if hi is None or self.hi is not None and self.hi < hi:
            hi = self.hi
        if lo is not None and hi is not None and lo > hi:
            raise ValueError(f"{self} held to [{lo}, {hi}] holds no value")
        return dataclasses.replace(self, lo=lo, hi=hi)

    def __mod__(self, m: int) -> Affine:
        if isinstance(m, bool) or not isinstance(m, (int, np.integer)):
            return NotImplemented
        m = int(m)
        if m <= 0 or m & (m - 1):
            raise TypeError(f"no expression for ({self}) % {m}: a ring is 2^k rows")
        if self.mod is not None and self.mod % m:
            raise TypeError(f"no expression for ({self}) % {m}")
        return dataclasses.replace(self, mod=m)

    def affine(self) -> Affine:
        """This expression, as a binding takes it.

        Raises:
            TypeError: It floors, is clamped or wraps.
        """
        if self.down or self.clamped or self.mod is not None:
            raise TypeError(f"{self} is not linear in {self.value.name}")
        return self

    def __add__(self, k: int | Affine) -> Affine | int:
        if isinstance(k, Affine):
            if k.value is not self.value or self.down or k.down:
                return NotImplemented
            if self.clamped or k.clamped or (self.mod, k.mod) != (None, None):
                return NotImplemented
            scale = self.scale + k.scale
            if not scale:
                return self.bias + k.bias
            return Affine(self.value, scale, self.bias + k.bias)
        if isinstance(k, bool) or not isinstance(k, (int, np.integer)):
            return NotImplemented
        k = int(k)
        if self.mod is not None:
            return NotImplemented
        if self.clamped:
            lo, hi = (None if b is None else b + k for b in (self.lo, self.hi))
            return (dataclasses.replace(self, lo=None, hi=None) + k).clamp(lo, hi)
        if self.down:
            return dataclasses.replace(self, add=self.add + k)
        return dataclasses.replace(self, bias=self.bias + k)

    def __sub__(self, k: int | Affine) -> Affine | int:
        return self + (-k)

    def __rsub__(self, k: int) -> Affine:
        return -self + k

    def __neg__(self) -> Affine:
        return self * -1

    def __mul__(self, k: int) -> Affine:
        if isinstance(k, bool) or not isinstance(k, (int, np.integer)):
            return NotImplemented
        k = int(k)
        if self.mod is not None:
            # (x % m) * k is (x * k) % (m * k) for k > 0, a ring row's elements.
            if k <= 0 or k & (k - 1):
                raise TypeError(f"no expression for ({self}) * {k}")
            return dataclasses.replace(self, mod=None) * k % (self.mod * k)
        if self.clamped:
            lo, hi = (None if b is None else b * k for b in (self.lo, self.hi))
            if k < 0:
                lo, hi = hi, lo
            return (dataclasses.replace(self, lo=None, hi=None) * k).clamp(lo, hi)
        if self.down:
            return dataclasses.replace(self, mul=self.mul * k, add=self.add * k)
        return dataclasses.replace(self, scale=self.scale * k, bias=self.bias * k)

    __radd__, __rmul__ = __add__, __mul__

    def __floordiv__(self, d: int | Affine) -> Affine | int:
        if self.mod is not None:
            raise TypeError(f"no expression for ({self}) // {d}")
        if self.clamped:
            # A floor division by a positive divisor keeps the bounds' order.
            if isinstance(d, bool) or not isinstance(d, (int, np.integer)) or d <= 0:
                raise TypeError(f"no expression for ({self}) // {d}")
            lo, hi = (None if b is None else b // int(d) for b in (self.lo, self.hi))
            return (dataclasses.replace(self, lo=None, hi=None) // d).clamp(lo, hi)
        if isinstance(d, Affine):
            # floor(q u / u) = q, wherever u is not 0
            linear = not (self.down or d.down) and d.value is self.value
            if linear and d.scale and self.scale % d.scale == 0:
                q = self.scale // d.scale
                if self.bias == q * d.bias:
                    return q
            raise TypeError(f"no expression for ({self}) // ({d})")
        if isinstance(d, bool) or not isinstance(d, (int, np.integer)):
            return NotImplemented
        d = int(d)
        if d < 0:
            return (-self) // -d
        if d == 0 or d & (d - 1):
            raise TypeError(f"no expression for a floor division by {d}")
        if self.mul != 1:
            if self.mul % d == 0:  # the floored term divides exactly
                return dataclasses.replace(self, mul=self.mul // d, add=self.add // d)
            raise TypeError(f"no expression for ({self}) // {d}")
        # floor((floor(u / 2^a) + c) / 2^k) = floor((u + c 2^a) / 2^(a+k))
        scale, bias = self.scale, self.bias + (self.add << self.down)
        k = self.down + d.bit_length() - 1
        while k and scale % 2 == 0 and bias % 2 == 0:
            scale, bias, k = scale // 2, bias // 2, k - 1
        if scale % (1 << k) == 0:  # floor(s v / 2^k + b / 2^k) is linear
            return Affine(self.value, scale >> k, bias >> k)
        return Affine(self.value, scale, bias, k)

    def __eq__(self, other) -> bool:
        if isinstance(other, Affine):
            # The value by identity: PerCall has no value to compare.
            terms = [f.name for f in dataclasses.fields(self)[1:]]
            return self.value is other.value and all(
                getattr(self, n) == getattr(other, n) for n in terms
            )
        if isinstance(other, (int, float, np.integer, np.floating)):
            raise TypeError(f"{self} has no value to compare: it is computed per call")
        return NotImplemented

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
        """An identifier for the device symbol: ``p``, ``p_x64``, ``p_x64_p64``, ``p_m1``."""
        text = self.value.name + (f"_x{self.scale}" if self.scale != 1 else "")
        if self.bias:
            text += f"_{'p' if self.bias > 0 else 'm'}{abs(self.bias)}"
        if self.down:
            if self.mul != 1:
                text += f"_d{self.down}_x{'m' if self.mul < 0 else ''}{abs(self.mul)}"
            else:
                text += f"_d{self.down}"
            if self.add:
                text += f"_{'p' if self.add > 0 else 'm'}{abs(self.add)}"
        for tag, b in (("lo", self.lo), ("hi", self.hi)):
            if b is not None:
                text += f"_{tag}{'m' if b < 0 else ''}{abs(b)}"
        if self.mod is not None:
            text += f"_mod{self.mod}"
        return text

    def evaluate(self, values: Mapping[str, int]) -> int:
        v = int(values[self.value.name])
        x = ((self.scale * v + self.bias) >> self.down) * self.mul + self.add
        if self.lo is not None:
            x = max(x, self.lo)
        if self.hi is not None:
            x = min(x, self.hi)
        return x if self.mod is None else x % self.mod

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
        if self.clamped:
            text = f"clamp({text}, {self.lo}, {self.hi})"
        if self.mod is not None:
            text = f"({text}) % {self.mod}"
        return text


class Carry(Mapping[str, "Handle | Affine | int"]):
    """The next values of a graph's carried values, by name: traced, an
    ``Affine`` or a one-element ``Handle``; returned from a call, a number.
    """

    __slots__ = ("_next",)

    def __init__(self, **next_values: Handle | Affine | PerCall | int):
        self._next: dict[str, Handle | Affine | int] = {
            name: v.affine() if isinstance(v, (PerCall, Affine)) else v
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


def clamp(x: PerCall | Affine, lo: int | None = None, hi: int | None = None) -> Affine:
    """A per-call value's expression ``x`` held to ``[lo, hi]``, a bound of
    None none."""
    return (x if isinstance(x, Affine) else x.affine()).clamp(lo, hi)


def carry(**next_values: Handle | Affine | PerCall | int) -> Carry:
    """Return with a graph's outputs the next value of each carried value:
    ``return logits, iron.carry(token=sampled, position=position + 1)``.
    """
    return Carry(**next_values)


def is_operand(x) -> bool:
    """A graph handle, a state or weight (or a view of one), or a host tensor."""
    return isinstance(x, (Handle, State, Weight, np.ndarray, np.generic))
