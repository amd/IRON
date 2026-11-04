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

from ..declare.operand import concrete
from ..declare.operator import graph_recorder
from ..declare.precision import Precision
from ..image.packaging import Kind
from ..image.step import BufferRef
from .coded import Source

T = TypeVar("T")

Scratchpad = Annotated[T, Kind.SCRATCHPAD.value]
"""A per-call value patched into a DMA descriptor or read by a core: free per
call, works under full ELF, cannot change a DMA size or stride; 30 bits at most.
"""

Carried = Annotated[T, Kind.CARRIED.value]
"""A scratchpad value a graph computes for its next call and returns last with
``iron.carry(name=...)``: an expression of its values (``position + 1``) or a
one-element handle (a sampled token); the host seeds only the first call.
"""


@dataclasses.dataclass(eq=False)
class Buffer:
    """A graph buffer every handle on it shares, so renaming it renames them all.

    A returned intermediate becoming ``out`` is one such rename. ``role`` is
    input, output, weight, state or intermediate; ``shape`` and ``dtype`` are
    as made.
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
    """A contiguous run of the buffer from element ``offset``, which any operator takes.

    None is the whole buffer, in any shape.
    """

    offset: int | None = None


@dataclasses.dataclass(frozen=True)
class Strided:
    """What ``tap`` walks of the buffer, which only a copy takes.

    Per call, ``offset`` moves it, ``repeat`` and ``length`` size its first
    two dimensions, and ``window`` holds ``x[s : s + W]``'s axis, ``s``,
    ``W`` and axis length.
    """

    tap: TensorAccessPattern | tuple[TensorAccessPattern, ...]
    offset: Affine | None = None
    repeat: tuple[Affine, ...] | None = None
    length: Affine | None = None
    window: tuple[int, Affine, int, int] | None = None


@dataclasses.dataclass(frozen=True)
class Gather:
    """The rows of a whole table the 1-D integer handle ``rows`` names each call.

    As ``table[ids]``, which only ``Copy`` of it alone takes.
    """

    rows: Handle


@dataclasses.dataclass(frozen=True, eq=False)
class Handle:
    """A recorded tensor: its place in a graph buffer, shape, dtype, and per-axis bound.

    ``layout`` is where it is in the buffer; ``valid`` holds, per axis, the
    leading entries valid this call (``x[:n]``).

    ``h[key]`` takes numpy's basic indexing, a per-call value on one axis
    (``keys[:, pos]``), and leading-axis rows, fixed (``table[ids]``) or a 1-D
    integer handle's per call; any view but a contiguous static slice is a copy's.
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
        """Make a new buffer ``name`` of ``shape``, whole."""
        shape = tuple(int(s) for s in shape)
        return cls(Buffer(name, role, shape, dtype), shape, dtype)

    def valid_index(self, values: Mapping[str, int]) -> tuple[slice, ...]:
        """Return the index of the entries valid in a call with per-call ``values``.

        Each bounded axis cut to its count, the others whole.
        """
        key = [slice(None)] * len(self.shape)
        for axis, count in self.valid.items():
            key[axis] = slice(count.evaluate(values))
        return tuple(key)

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
        """Return where a step finds this handle.

        A part of its buffer for a contiguous run, else all of it.
        """
        match self.layout:
            case Dense(offset=int(offset)):
                return BufferRef(
                    self.name, offset * bfp.itemsize(self.dtype), self.nbytes
                )
        return BufferRef(self.name)

    def _start(self) -> int:
        """Return the element this contiguous handle starts at in its buffer."""
        assert isinstance(self.layout, Dense), "a contiguous handle"
        return self.layout.offset or 0

    def _over_buffer(self, tap):
        """Return ``tap`` (or each of several) over this handle, as over its buffer.

        Unchanged on the whole buffer, else moved by where this part starts
        in it, over the buffer's shape as made (flat in another dtype).
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
        """Return the same buffer seen with another shape (no data moves)."""
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
        """Return the same buffer walked with its axes permuted (no data moves)."""
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
    def T(self) -> Handle:  # noqa: N802 -- numpy's name
        """``transpose(1, 0)``, as numpy's ``.T`` of a matrix."""
        return self.transpose(1, 0)

    def _bounded_run(self, key) -> Handle:
        """Return a run from a per-call start bounded per call, ``x[s : s + W][:n]``.

        Every call keeps ``s + n`` inside the axis, checked before it.
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
        """Return this handle of ``part`` seen as a buffer of its own.

        Placed in ``part``'s buffer; a per-call gather, which reads a whole
        table, raises.
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
        """Return what ``tap`` walks, as ``shape``: a slice if contiguous, else a view.

        Per call, ``repeat`` runs each pattern's first dimension (a tuple, one
        per pattern of a tuple ``tap``) and ``length`` takes entries of its
        second; ``bounds`` then gives the rows the view moves a call.

        Raises:
            ValueError: With ``repeat`` or ``length``: a pattern is not one shim
                descriptor, repeats don't match patterns, or no ``bounds``.
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
                (size0,) = concrete(walk.sizes[:1], walk)
                recorder.limit(r, 1, size0 + 1, self)
            if length is not None:
                sizes1 = concrete([walk.sizes[1] for walk in walks], walks)
                recorder.limit(length, 1, min(sizes1) + 1, self)
        layout = Strided(self._over(tap), repeat=repeats, length=length)
        return Handle(self.buffer, shape, self.dtype, bounds, layout)

    def _over(self, tap):
        """Return ``tap`` over this handle as over its buffer.

        Given over the whole buffer in another shape, over this one's.
        """
        if self.layout != Dense():
            return self._over_buffer(tap)

        def shaped(t):
            if tuple(t.tensor_dims) == self.shape:
                return t
            return TensorAccessPattern(self.shape, t.offset, t.sizes, t.strides)

        return tuple(map(shaped, tap)) if isinstance(tap, tuple) else shaped(tap)

    def _view(self, tap, shape, index_by, valid, window=None) -> Handle:
        """Return what ``tap`` walks from the per-call element offset ``index_by``.

        A slice if contiguous and not offset per call, else a view.
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
        """Defer to the handle for a held array on the left of an operator.

        Refuse any other numpy function on a handle.
        """
        name = _OPERATORS.get(ufunc)
        if method == "__call__" and name and len(inputs) == 2 and not kwargs:
            a, b = inputs
            if a is self:
                return vars(Handle)[f"__{name}__"](self, b)
            reflected = vars(Handle).get(f"__r{name}__")
            if reflected is not None:
                return reflected(self, a)
        raise TypeError(
            f"numpy's {ufunc.__name__} cannot compute {self!r}: a handle is a "
            f"buffer of a recorded graph. Use + - * / @ on it, iron.functional, "
            f"or an operator's step()"
        )

    def __add__(self, other) -> "Handle":
        """Return ``self + other``, elementwise.

        Or ``other`` a row added to every row, or a number added to every
        element.
        """
        from iron.operators.elementwise_add import ElementwiseAdd, RowwiseAdd  # a cycle

        return _broadcast(ElementwiseAdd, RowwiseAdd, self, other)

    def __mul__(self, other) -> "Handle":
        """Return ``self * other``, elementwise.

        Or every row times the row ``other``, or every element times a
        number.
        """
        from iron.operators.elementwise_mul import ElementwiseMul, RowwiseMul  # a cycle

        return _broadcast(ElementwiseMul, RowwiseMul, self, other)

    __radd__ = __add__
    __rmul__ = __mul__

    def __neg__(self) -> "Handle":
        return self * -1

    def __sub__(self, other) -> "Handle":
        """``self - other``: one AXPY step for a handle of this shape."""
        from iron.operators.axpy import AXPY  # a cycle

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
        """Return ``self @ W.T`` for one row ``self``, GEMV at ``Precision.HIGHEST``.

        ``W`` is stored ``(out, in)`` as ``torch.nn.Linear`` does.

        Raises:
            TypeError: ``self`` is several rows, whose precision the caller
                chooses (``iron.functional.linear``).
        """
        import iron.functional as F  # a cycle

        if prod(self.shape[:-1]) != 1:
            raise TypeError(
                f"{self!r} @ W.T: rows take a precision, "
                "iron.functional.linear(x, W, precision=...)"
            )
        return F.linear(self, _untransposed(self, other), precision=Precision.HIGHEST)

    def __rmatmul__(self, other) -> "Handle":
        """``W @ self``, ``self`` one row: as ``self @ W.T``."""
        import iron.functional as F  # a cycle

        if len(self.shape) != 1:
            raise TypeError(
                f"W @ {self!r} takes one row; for rows, "
                "iron.functional.linear(x, W, precision=...)"
            )
        return F.linear(self, other, precision=Precision.HIGHEST)

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
    """``W`` from ``w``, its transpose ``W.T`` (a held array or a weight handle).

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
    """``whole`` of ``x`` and ``y`` of its shape, else ``rowwise`` of ``x`` and a row ``y``.

    ``rowwise`` applies where ``x`` has two axes or more; a number ``y`` is a
    constant row, and both being commutative, a row times a matrix is the
    matrix's ``rowwise``.
    """
    if _is_number(y):
        recorder = graph_recorder.get()
        y = recorder.constant(y, x.shape[-1] if x.shape else 1, x.dtype)
    if len(x.shape) == 1 and is_operand(y) and len(y.shape) > 1:
        x, y = (y if isinstance(y, Handle) else graph_recorder.get().operand(y)), x
    shape = tuple(y.shape) if is_operand(y) else ()
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
    from iron.operators.copy import Copy  # a cycle

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
    def T(self):  # noqa: N802 -- numpy's name
        return self._as_operand().T

    def at(self, tap, shape, *, bounds=None, repeat=None, length=None):
        """``Handle.at`` of the tensor as the recorder views it."""
        return self._as_operand().at(
            tap, shape, bounds=bounds, repeat=repeat, length=length
        )


class State(_Viewed):
    """A tensor that persists on the device across calls (a KV cache), zero when first uploaded.

    Read and written through ``CompiledGraph.read`` and ``write``, and held
    in ``host`` across ``Graph.reference`` calls.
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


class _Param(np.ndarray):
    """A ``param``.

    An array a graph holds as a weight, and where in a file it was read from, if it was
    (``source``).
    """

    source: Source | None = None


class Weight(_Viewed):
    """A tensor the body indexes per call (``iron.weight(table)[ids]``).

    One buffer with the array it wraps.
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
    """Return a tensor a graph's body indexes per call (``iron.weight(table)[ids]``)."""
    return Weight(array)


def _rescale_bounds(h: Handle, shape) -> dict[int, Affine]:
    """Return the bounds of ``h`` reshaped to ``shape``.

    A leading-axis bound, rescaled as that axis merges or splits.
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
    """The next values of a graph's carried values, by name.

    Recorded, an ``Affine`` or a one-element ``Handle``; returned from a
    call, a number.
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
    """Return a per-call count of rows, which may be clamped (``min(p + 1, W)``)."""
    if isinstance(n, PerCall):
        return n.affine()
    if n.mod is not None or n.down:
        raise TypeError(f"{n} is not linear in {n.value.name}")
    return n


def clamp(
    x: PerCall | Affine, lo: int | None = None, hi: int | None = None
) -> Affine | int:
    """Return a per-call value's expression ``x`` held to ``[lo, hi]``, a bound of None none.

    The nearer bound itself where ``x`` never reaches the range.
    """
    return (x if isinstance(x, Affine) else x.affine()).clamp(lo, hi)


def carry(**next_values: Handle | Affine | PerCall | int) -> Carry:
    """Return with a graph's outputs the next value of each carried value.

    ``return logits, iron.carry(token=sampled, position=position + 1)``.
    """
    return Carry(**next_values)


def on_host(fn: Callable[..., None], *reads, writes=()) -> None:
    """Run ``fn(*reads, *writes)`` on the host between the steps around it.

    A full ELF ends a command there, so the graph has no device loop. Each is
    contiguous: reads cut to their bounds, writes parts of states no step writes.

    Raises:
        TypeError: No graph's body is being recorded.
    """
    recorder = graph_recorder.get()
    if recorder is None:
        raise TypeError("on_host records into a graph's body")
    recorder.on_host(fn, reads, writes)


def is_operand(x) -> bool:
    """Check that ``x`` is a graph handle, a state or weight (or a view of one), or a host tensor."""
    return isinstance(x, (Handle, State, Weight, np.ndarray, np.generic))
