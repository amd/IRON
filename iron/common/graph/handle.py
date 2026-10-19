# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a recorded graph passes around in place of a buffer."""

from __future__ import annotations

from collections.abc import Iterator, Mapping
from math import prod
from typing import Annotated, TypeVar

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import Affine, PerCall, TensorAccessPattern
from aie.utils import bfp
from ml_dtypes import bfloat16

from ..declare.operand import slots
from ..declare.operator import graph_recorder
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
    """A recorded tensor: a buffer of the graph, with a shape and a dtype.

    ``h[key]`` takes numpy's basic indexing, on one axis a per-call
    value (``keys[:, pos]``), and on the leading axis an integer array
    of rows fixed when the graph is recorded (``table[ids]``) or a 1-D integer
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
        recorder = graph_recorder.get()
        if recorder is not None:
            recorder.limit(stop, 0, width + 1, self)
            recorder.limit(start, 0, n + 1, self, stop)
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
        recorder = graph_recorder.get()
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
                if start.value.marker is Kind.DISPATCH_TIME:
                    raise ValueError(
                        f"{start} is a DispatchTime value; only a Scratchpad value can "
                        f"start a run, since it moves a transfer's base address"
                    )
                if recorder is not None:
                    recorder.limit(start, 0, n, self)
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
                if stop.value.marker is Kind.DISPATCH_TIME:
                    raise ValueError(
                        f"{stop} is a DispatchTime value; only a Scratchpad value can "
                        f"bound an axis, since it patches a transfer's size"
                    )
                if recorder is not None:
                    recorder.limit(stop, 0, n + 1, self)
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
                if entry.value.marker is Kind.DISPATCH_TIME:
                    raise ValueError(
                        f"{entry} is a DispatchTime value; only a Scratchpad value can "
                        f"index a view, since it moves a transfer's base address"
                    )
                if recorder is not None:
                    recorder.limit(entry, 0, n, self)
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
            recorder = graph_recorder.get()
            if recorder is not None:
                for walk, r in zip(walks, repeats or ()):
                    recorder.limit(r, 1, walk.sizes[0] + 1, self)
                if length is not None:
                    hi = min(walk.sizes[1] for walk in walks)
                    recorder.limit(length, 1, hi + 1, self)
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
            f"buffer of a recorded graph. Use + - * / @ on it, iron.functional, "
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
        recorder = graph_recorder.get()
        y = recorder.constant(y, x.shape[-1] if x.shape else 1, x.dtype)
    if len(x.shape) == 1 and len(getattr(y, "shape", ())) > 1:
        x, y = (y if isinstance(y, Handle) else graph_recorder.get().operand(y)), x
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
    """A tensor the graph holds, viewed inside its body as the recorder says."""

    __slots__ = ()

    def _as_operand(self) -> Handle:
        recorder = graph_recorder.get()
        if recorder is None:
            raise TypeError(f"{self!r} is viewed inside a graph's body")
        return recorder.operand(self)

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
        """``Handle.at`` of the tensor as the recorder views it."""
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


class Carry(Mapping[str, "Handle | Affine | int"]):
    """The next values of a graph's carried values, by name: recorded, an
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
