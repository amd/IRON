# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a recorded graph passes around in place of a buffer."""

from __future__ import annotations

import dataclasses
from collections.abc import Callable, Iterator, Mapping
from math import prod
from typing import Annotated, Any, TypeVar

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import Affine, PerCall, TensorAccessPattern
from aie.utils import bfp
from ml_dtypes import bfloat16

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


@dataclasses.dataclass(eq=False)
class Buffer:
    """A buffer of the graph, which every handle on it shares: renaming it
    (a returned intermediate becoming ``out``) renames them all.

    Attributes:
        name: What a step calls it (``BufferRef``).
        role: input, output, weight, state or intermediate.
        shape: Its shape as made, before any reshape.
        dtype: Its element type as made.
    """

    name: str
    role: str
    shape: tuple[int, ...]
    dtype: Any

    @property
    def nbytes(self) -> int:
        return (prod(self.shape) if self.shape else 1) * bfp.itemsize(self.dtype)


@dataclasses.dataclass(frozen=True)
class Dense:
    """A contiguous run of the buffer from element ``offset``, which any
    operator takes; None is the whole buffer, in any shape.
    """

    offset: int | None = None


@dataclasses.dataclass(frozen=True)
class Strided:
    """What ``tap`` walks of the buffer, which only a copy takes.

    Attributes:
        tap: The pattern over the buffer seen as its ``tensor_dims``, or
            several walked in turn (a gather's rows, fixed when recorded).
        offset: A per-call element offset (``keys[:, pos]``), or None.
        repeat: Per walk, the runs of its first dimension each call
            (``Handle.at``), or None.
        length: The entries of each walk's second dimension each call, or
            None.
        window: For a run from a per-call start, ``x[s : s + W]``: its axis,
            ``s``, ``W`` and the axis's length, which a bound (``[:n]``)
            keeps the run inside; else None.
    """

    tap: TensorAccessPattern | tuple[TensorAccessPattern, ...]
    offset: Affine | None = None
    repeat: tuple[Affine, ...] | None = None
    length: Affine | None = None
    window: tuple[int, Affine, int, int] | None = None


@dataclasses.dataclass(frozen=True)
class Gather:
    """The rows of a whole table the 1-D integer handle ``rows`` names each
    call (``table[ids]``), which only ``Copy`` of it alone takes.
    """

    rows: Handle


@dataclasses.dataclass(frozen=True, eq=False)
class Handle:
    """A recorded tensor: where it is in a buffer of the graph, its shape,
    its dtype, and the leading entries of each axis valid this call.

    ``h[key]`` takes numpy's basic indexing, on one axis a per-call
    value (``keys[:, pos]``), and on the leading axis an integer array
    of rows fixed when the graph is recorded (``table[ids]``) or a 1-D integer
    handle naming the rows each call takes. A contiguous static region is a
    slice any operator takes (``Dense``); any other view, a gather included,
    is an access pattern only a copy takes (``Strided``, ``Gather``).

    Attributes:
        buffer: The buffer it is, or is a part or view of.
        shape: Its shape.
        dtype: Its element type.
        valid: Axis -> its leading entries valid this call (``x[:n]``).
        layout: Where in ``buffer`` it is.
    """

    buffer: Buffer
    shape: tuple[int, ...]
    dtype: Any
    valid: Mapping[int, Affine] = dataclasses.field(default_factory=dict)
    layout: Dense | Strided | Gather = Dense()

    def __post_init__(self) -> None:
        object.__setattr__(self, "shape", tuple(int(s) for s in self.shape))
        valid = {
            axis: n.affine() if isinstance(n, PerCall) else n
            for axis, n in self.valid.items()
        }
        object.__setattr__(self, "valid", valid)

    @classmethod
    def whole(cls, shape, dtype, name: str, role: str) -> Handle:
        """A new buffer ``name`` of ``shape``, whole."""
        shape = tuple(int(s) for s in shape)
        return cls(Buffer(name, role, shape, dtype), shape, dtype)

    @property
    def name(self) -> str:
        return self.buffer.name

    @property
    def role(self) -> str:
        return self.buffer.role

    @property
    def elements(self) -> int:
        return prod(self.shape) if self.shape else 1

    @property
    def nbytes(self) -> int:
        return self.elements * bfp.itemsize(self.dtype)

    def ref(self) -> BufferRef:
        """Where a step finds this handle: a part of its buffer for a
        contiguous run, else all of it.
        """
        match self.layout:
            case Dense(offset=int(offset)):
                return BufferRef(
                    self.name, offset * bfp.itemsize(self.dtype), self.nbytes
                )
        return BufferRef(self.name)

    def _start(self) -> int:
        """The element this contiguous handle starts at in its buffer."""
        assert isinstance(self.layout, Dense), "a contiguous handle"
        return self.layout.offset or 0

    def _over_buffer(self, tap):
        """``tap`` (or each of several) over this handle, as over its
        buffer: unchanged on the whole buffer, else moved by where this part
        starts in it, over the buffer's shape as made (flat in another dtype).
        """
        if self.layout == Dense():
            return tap
        buffer, start = self.buffer, self._start()
        dims = buffer.shape
        if bfp.dtype_name(buffer.dtype) != bfp.dtype_name(self.dtype):
            dims = (buffer.nbytes // bfp.itemsize(self.dtype),)

        def moved(t):
            return TensorAccessPattern(dims, t.offset + start, t.sizes, t.strides)

        return tuple(map(moved, tap)) if isinstance(tap, tuple) else moved(tap)

    def reshape(self, *shape) -> Handle:
        """The same buffer seen with another shape (no data moves)."""
        if len(shape) == 1 and isinstance(shape[0], (tuple, list)):
            shape = tuple(shape[0])
        if prod(shape) != self.elements:
            raise ValueError(f"cannot reshape {self!r} to {list(shape)}")
        if not isinstance(self.layout, Dense):
            raise ValueError(f"cannot reshape a view {self!r}; reshape what it views")
        return dataclasses.replace(
            self, shape=shape, valid=_rescale_bounds(self, shape)
        )

    def transpose(self, *axes) -> Handle:
        """The same buffer walked with its axes permuted (no data moves)."""
        if len(axes) == 1 and isinstance(axes[0], (tuple, list)):
            axes = tuple(axes[0])
        if not isinstance(self.layout, Dense):
            raise ValueError(
                f"cannot transpose a view {self!r}; transpose what it views"
            )
        if sorted(axes) != list(range(len(self.shape))):
            raise ValueError(
                f"axes {axes} do not permute a shape of rank {len(self.shape)}"
            )
        shape = tuple(self.shape[a] for a in axes)
        tap = TensorAccessPattern.full(self.shape).permute(axes)
        valid = {axes.index(axis): b for axis, b in self.valid.items()}
        return Handle(
            self.buffer, shape, self.dtype, valid, Strided(self._over_buffer(tap))
        )

    @property
    def T(self) -> Handle:
        """``transpose(1, 0)``, as numpy's ``.T`` of a matrix."""
        return self.transpose(1, 0)

    def _bounded_run(self, key) -> Handle:
        """A run from a per-call start bounded per call, ``x[s : s + W][:n]``:
        every call keeps ``s + n`` inside the axis, checked before it.
        """
        assert isinstance(self.layout, Strided) and self.layout.window is not None
        axis, start, width, n = self.layout.window
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
        stop = _count(run.stop)
        recorder = graph_recorder.get()
        if recorder is not None:
            recorder.limit(stop, 0, width + 1, self)
            recorder.limit(start, 0, n + 1, self, stop)
        layout = dataclasses.replace(self.layout, window=None)
        valid = {**self.valid, axis: stop}
        return dataclasses.replace(self, valid=valid, layout=layout)

    def __getitem__(self, key) -> Handle:
        match self.layout:
            case Strided(window=tuple()):
                return self._bounded_run(key)
            case Strided() | Gather():
                raise TypeError(
                    f"{self!r} is a view, which only a copy takes; index what it views"
                )
            case Dense(offset=int()):
                # A part: indexed as a buffer of its own, then placed in its buffer.
                whole = dataclasses.replace(self, layout=Dense())
                return whole[key]._within(self)
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
                not isinstance(ids.layout, Dense)
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
            if self.role not in ("weight", "state") or self.valid:
                raise TypeError(
                    f"a gather per call reads a whole table the graph holds, not "
                    f"{self!r}"
                )
            shape = (ids.shape[0], *self.shape[1:])
            return Handle(self.buffer, shape, self.dtype, layout=Gather(ids))
        if isinstance(entries[0], np.ndarray):
            ids, n = entries[0], self.shape[0]
            if ids.ndim != 1 or not np.issubdtype(ids.dtype, np.integer) or rank < 2:
                raise IndexError(
                    f"a gather takes a 1-D integer array of rows of a table of "
                    f"rank 2 or more; got {ids.dtype} {ids.shape} on {self!r}"
                )
            if not all(isinstance(e, slice) and e == slice(None) for e in entries[1:]):
                raise IndexError("a gather takes the whole of every axis but the first")
            if self.valid:
                raise TypeError(f"{self!r} is bounded per call; gather what it bounds")
            if not len(ids) or ((ids < -n) | (ids >= n)).any():
                raise IndexError(f"gathering {ids} from the {n} rows of {self!r}")
            whole = TensorAccessPattern.full(self.shape)
            rows = tuple(whole[int(i) % n] for i in ids)
            shape = (len(ids), *self.shape[1:])
            return Handle(self.buffer, shape, self.dtype, layout=Strided(rows))
        for axis in self.valid:
            if isinstance(entries[axis], slice) and entries[axis] != slice(None):
                raise TypeError(
                    f"{self!r} is bounded per call on axis {axis}; index it, take "
                    f"all of it, or slice what it bounds"
                )
        index_by = window = None
        static, shape, valid = [], [], {}
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
                    if start.mod is not None:
                        width = stop.post - start.post
                    elif start.down:
                        width = stop.add - start.add
                    else:
                        width = stop.bias - start.bias
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
                if recorder is not None:
                    recorder.limit(start, 0, n, self)
                index_by = start * prod(self.shape[axis + 1 :])
                window = (len(shape), start, width, n)
                static.append(slice(0, width))
                shape.append(width)
                continue
            if axis in self.valid and isinstance(entry, slice):
                valid[len(shape)] = self.valid[axis]
                static.append(entry)
                shape.append(n)
            elif isinstance(entry, slice) and isinstance(entry.stop, (PerCall, Affine)):
                stop = _count(entry.stop)
                if entry.start not in (None, 0) or entry.step not in (None, 1):
                    raise ValueError(f"{stop} bounds an axis from its start: [:{stop}]")
                if recorder is not None:
                    recorder.limit(stop, 0, n + 1, self)
                # Keyed by the axis of the result: an index before it drops one.
                valid[len(shape)] = stop
                static.append(slice(None))
                shape.append(n)
            elif isinstance(entry, (PerCall, Affine)):
                # An index may floor (a slot per chunk, ``position // C``).
                if isinstance(entry, PerCall):
                    entry = entry.affine()
                if index_by is not None:
                    raise ValueError("one axis at most is indexed by a per-call value")
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
        if valid and index_by is None and tuple(shape) == self.shape:
            return dataclasses.replace(self, valid=valid)
        return self._view(tap, shape, index_by, valid, window)

    def __setitem__(self, key, value) -> None:
        """``self[key] = value``: a copy of ``value`` into that view."""
        _write(self[key], value)

    def _within(self, part: Handle) -> Handle:
        """This handle of ``part`` seen as a buffer of its own, as where it is
        in ``part``'s buffer.

        Raises:
            TypeError: It gathers per call, which reads a whole table.
        """
        match self.layout:
            case Gather():
                raise TypeError(
                    f"a gather per call reads a whole table, not a slice of {part!r}"
                )
            case Strided(tap=tap):
                layout = dataclasses.replace(self.layout, tap=part._over_buffer(tap))
            case _:
                layout = Dense(part._start() + self._start())
        return dataclasses.replace(self, buffer=part.buffer, layout=layout)

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
                repeats differ in number (a tuple of either takes a tuple of the
                other), or no ``bounds``.
        """
        if not isinstance(self.layout, Dense):
            raise ValueError(f"cannot walk a view {self!r}; walk what it views")
        walks = tap if isinstance(tap, tuple) else (tap,)
        each: tuple = repeat if isinstance(repeat, tuple) else (repeat,)
        if isinstance(repeat, tuple) != isinstance(tap, tuple) or len(each) != len(
            walks
        ):
            raise ValueError(
                f"{len(walks)} pattern(s) take a repeat each, not {repeat}"
            )
        if repeat is None and length is None:
            return self._view(tap, shape, None, bounds or {})
        dev = aie_utils.get_current_device()
        for walk in walks:
            if (
                walk.rank != 4
                or dev is None
                or not dev.dma_bd_fits(0, 0, walk, self.dtype)
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
            repeats = tuple(r if isinstance(r, Affine) else r.affine() for r in each)
        length = None if length is None else length.affine()
        recorder = graph_recorder.get()
        if recorder is not None:
            for walk, r in zip(walks, repeats or ()):
                recorder.limit(r, 1, walk.sizes[0] + 1, self)
            if length is not None:
                hi = min(walk.sizes[1] for walk in walks)
                recorder.limit(length, 1, hi + 1, self)
        layout = Strided(self._over(tap), repeat=repeats, length=length)
        return Handle(self.buffer, shape, self.dtype, bounds, layout)

    def _over(self, tap):
        """``tap`` over this handle as over its buffer: given over the whole
        buffer in another shape, over this one's.
        """
        if self.layout != Dense():
            return self._over_buffer(tap)

        def shaped(t):
            if tuple(t.tensor_dims) == self.shape:
                return t
            return TensorAccessPattern(self.shape, t.offset, t.sizes, t.strides)

        return tuple(map(shaped, tap)) if isinstance(tap, tuple) else shaped(tap)

    def _view(self, tap, shape, index_by, valid, window=None) -> Handle:
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
            layout = Dense(self._start() + int(offset))
        else:
            layout = Strided(self._over(tap), index_by, window=window)
        return Handle(self.buffer, shape, self.dtype, valid, layout)

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
        and isinstance(w.layout, Strided)
        and isinstance(w.layout.tap, TensorAccessPattern)
        and w.layout.offset is None
        and len(w.shape) == 2
        and tuple(w.layout.tap.tensor_dims) == w.shape[::-1]
    ):
        tap = w.layout.tap
        flipped = TensorAccessPattern.full(w.shape[::-1]).permute((1, 0))
        if (tap.offset, tap.sizes, tap.strides) == (
            flipped.offset,
            flipped.sizes,
            flipped.strides,
        ):
            return Handle(w.buffer, w.shape[::-1], w.dtype)
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
        rows = x.elements // x.shape[-1]
        if rows == 1 and rowwise.segments_for(x.shape[-1]) is None:
            # One row no core holds: the row is an operand of its shape, streamed.
            return whole.step(x.reshape(x.shape[-1]), y).reshape(x.shape)
        return rowwise.step(x.reshape(rows, x.shape[-1]), y).reshape(x.shape)
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
        self.array = np.asanyarray(array)

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
    if not h.valid:
        return {}
    (axis, count), *more = h.valid.items()
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
        self._next: dict[str, Handle | Affine | int] = {}
        for name, v in next_values.items():
            if isinstance(v, Affine) and not v.linear:
                raise TypeError(f"{name}: {v} is not linear in {v.value.name}")
            self._next[name] = v.affine() if isinstance(v, PerCall) else v

    def __getitem__(self, name: str) -> Handle | Affine | int:
        return self._next[name]

    def __iter__(self) -> Iterator[str]:
        return iter(self._next)

    def __len__(self) -> int:
        return len(self._next)

    def __repr__(self) -> str:
        items = ", ".join(f"{k}={v!r}" for k, v in self._next.items())
        return f"Carry({items})"


def _count(n: PerCall | Affine) -> Affine:
    """A per-call count of rows, which may be clamped (``min(p + 1, W)``)."""
    if isinstance(n, PerCall):
        return n.affine()
    if n.mod is not None or n.down:
        raise TypeError(f"{n} is not linear in {n.value.name}")
    return n


def clamp(
    x: PerCall | Affine, lo: int | None = None, hi: int | None = None
) -> Affine | int:
    """A per-call value's expression ``x`` held to ``[lo, hi]``, a bound of
    None none; the nearer bound itself where ``x`` never reaches the range."""
    return (x if isinstance(x, Affine) else x.affine()).clamp(lo, hi)


def carry(**next_values: Handle | Affine | PerCall | int) -> Carry:
    """Return with a graph's outputs the next value of each carried value:
    ``return logits, iron.carry(token=sampled, position=position + 1)``.
    """
    return Carry(**next_values)


def on_host(fn: Callable[..., None], *reads, writes=()) -> None:
    """Run ``fn(*reads, *writes)`` on the host between the steps recorded
    before and after it; a full ELF ends a command there and waits on it, so
    a graph with one has no device loop.

    Args:
        fn: Called on numpy arrays, each read as the device left it and cut
            to its bounds, then each write; what it leaves of a write keeps
            what it last wrote there.
        *reads: Contiguous handles, states or weights.
        writes: Contiguous parts of states no step writes; steps after
            this read what ``fn`` wrote.

    Raises:
        TypeError: No graph's body is being recorded.
    """
    recorder = graph_recorder.get()
    if recorder is None:
        raise TypeError("on_host records into a graph's body")
    recorder.on_host(fn, reads, writes)


def is_operand(x) -> bool:
    """A graph handle, a state or weight (or a view of one), or a host tensor."""
    return isinstance(x, (Handle, State, Weight, np.ndarray, np.generic))
