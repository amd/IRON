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
and what lets the checks in this module run once, when the class is created.
A stream's tile dimension may also be a tunable: choosing the tile is what
tuning is for, and inference never reads a stream.

Nothing in this module imports mlir-aie. Everything that generates MLIR lives
in :mod:`iron.common.build`, which reads the declarations made here.
"""

from __future__ import annotations

import dataclasses
from dataclasses import MISSING, Field
from pathlib import Path
from typing import Any, Callable, ClassVar, Generic, Iterator, TypeVar

import numpy as np
from ml_dtypes import bfloat16

from abc import ABCMeta

from .utils import get_shim_dma_limit, serialize_param

# Short spellings in artifact stems, for the fields every family shares.
_NAME_ALIASES = {
    "num_aie_columns": "c",
    "num_channels": "ch",
    "tile_size": "t",
    "size": "sz",
    "scalar_factor": "sf",
    "rows": "r",
    "cols": "n",
}


class Untunable(ValueError):
    """No legal tuning exists for this overlay on this device.

    An expected outcome, not a bug: raised by :meth:`Overlay.tuning` so the
    caller learns at tune time rather than from a design that compiles and
    then hangs.
    """


class Incompatible(ValueError):
    """An operator's extents do not fit the overlay it was declared against."""


class DeclarationError(TypeError):
    """A class body violates the declaration rules; raised at class creation."""


_TIER = "iron.tier"  # dataclass Field.metadata key: "dim" | "tunable"


# --------------------------------------------------------------------------
# Field specifiers
# --------------------------------------------------------------------------


def dim(default: Any = MISSING, *, repr: bool = True, init: bool = True) -> Any:
    """Declare a compile-time dimension field.

    A ``dim()`` field may appear in a shape. On an overlay it is overlay-tier
    (changing it rebuilds the array); on an operator it is sequence-tier
    (changing it rebuilds the instruction stream only).
    """
    return _specifier("dim", default, repr, init)


def tunable(default: Any = MISSING, *, repr: bool = True, init: bool = True) -> Any:
    """Declare a tuning knob: a field :meth:`Overlay.tuning` may set.

    A tunable never appears in a shape. ``None`` as the default means "tuning
    fills it from the device". ``init=False`` fixes a subclass's value of an
    inherited field (a kernel that only works with one channel per column).
    """
    return _specifier("tunable", default, repr, init)


def _specifier(tier: str, default: Any, repr_: bool, init: bool = True) -> Field:
    kwargs: dict[str, Any] = {"metadata": {_TIER: tier}, "repr": repr_, "init": init}
    if default is not MISSING:
        kwargs["default"] = default
    return dataclasses.field(**kwargs)


def _tier_of(f: Field) -> str | None:
    return f.metadata.get(_TIER) if f.metadata else None


# --------------------------------------------------------------------------
# Dimension references
# --------------------------------------------------------------------------


class DimRef:
    """A reference to a ``dim()`` field of a declared class.

    After ``@operator`` processes a class, each field is re-attached to the
    class as a ``DimRef``, so ``GEMVOverlay.K`` names the dimension from
    outside the class body while ``ov.K`` on an instance is the integer. A
    non-data descriptor: instance attributes take precedence.
    """

    __slots__ = ("owner", "name", "tier", "default")

    def __init__(
        self, owner: type, name: str, tier: str | None, default=MISSING
    ) -> None:
        self.owner = owner
        self.name = name
        self.tier = tier
        self.default = default

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        # An init=False field is read from the class attribute, which is now
        # this object: serve its default. Anything else has no value yet.
        if self.default is not MISSING:
            return self.default
        raise AttributeError(self.name)

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, DimRef)
            and other.owner is self.owner
            and other.name == self.name
        )

    def __hash__(self) -> int:
        return hash((id(self.owner), self.name))

    def __repr__(self) -> str:
        return f"{self.owner.__qualname__}.{self.name}"


class _Optional:
    """A leading dimension that is present only when greater than one.

    ``In(optional(num_batches), M, K)`` declares ``(M, K)`` for a single batch
    and ``(num_batches, M, K)`` otherwise, which is how batched operators
    already spell their host shapes. Inference reads the rank to tell the two
    apart.
    """

    __slots__ = ("ref",)

    def __init__(self, ref) -> None:
        self.ref = ref

    def __repr__(self) -> str:
        return f"optional({self.ref!r})"


def optional(ref) -> _Optional:
    """Mark a leading dimension as omitted when it equals one. See :class:`_Optional`."""
    return _Optional(ref)


class _Select:
    """A shape chosen by a flag: ``select(b_col_maj, (N, K), (K, N))``.

    The flag is a field with a default or one the caller passes explicitly;
    it is never inferred. The only conditional shapes in the tree are GEMM's
    layout flags, which transpose a declared shape rather than resize it.
    """

    __slots__ = ("flag", "when_true", "when_false")

    def __init__(self, flag, when_true, when_false) -> None:
        self.flag = flag
        self.when_true = tuple(when_true)
        self.when_false = tuple(when_false)

    def __repr__(self) -> str:
        return f"select({self.flag!r}, {self.when_true!r}, {self.when_false!r})"


def select(flag, when_true, when_false) -> _Select:
    """A conditional shape. See :class:`_Select`."""
    return _Select(flag, when_true, when_false)


_DimSpec = Any  # Field (own class, pre-processing) | DimRef | int | _Optional


def _describe(spec) -> str:
    if isinstance(spec, Field):
        return spec.name if spec.name else "<field>"
    return repr(spec)


# --------------------------------------------------------------------------
# Members
# --------------------------------------------------------------------------


class Shim:
    """A pinned shim endpoint: column and DMA channel on row 0."""

    __slots__ = ("col", "channel")

    def __init__(self, col: int, channel: int | None = None) -> None:
        self.col = col
        self.channel = channel

    def __repr__(self) -> str:
        return f"Shim(col={self.col}, channel={self.channel})"


class Xclbin:
    """An overlay someone else built: a downloaded xclbin, pinned by digest.

    Declared as a class attribute of an :class:`Overlay` that has no
    ``design()``. Every stream of such an overlay is pinned with ``via=`` and
    every resident has an ``address``, because nothing else says where its
    endpoints are; the library emits the sequence against those pins.
    """

    def __init__(
        self, *, url: str, sha256: str, filename: str, kernel_name: str = "MLIR_AIE"
    ) -> None:
        self.url = url
        self.sha256 = sha256
        self.filename = filename
        self.kernel_name = kernel_name

    def __repr__(self) -> str:
        return f"Xclbin({self.filename})"


class _Member:
    """Base of everything declared unannotated in an ``@operator`` class body.

    ``__set_name__`` gives the member its name from the language, and the
    class body gives it its order. On an instance, ``__get__`` returns the
    bound form built by ``@operator`` (a :class:`BoundBuffer`,
    :class:`BoundStream` or :class:`BoundValue`).
    """

    name: str = ""
    owner: type | None = None

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name
        self.owner = owner

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        try:
            return instance._bound[self.name]
        except (AttributeError, KeyError):
            raise AttributeError(
                f"{type(instance).__name__}.{self.name} is not bound yet"
            ) from None


class _Buffer(_Member):
    """A host buffer: shape in extents, a dtype, and the stream it moves through."""

    direction: ClassVar[str] = ""

    def __init__(
        self,
        *dims: _DimSpec,
        dtype: Any = bfloat16,
        to: "StreamIn | None" = None,
        from_: "StreamOut | None" = None,
    ) -> None:
        self.dims = tuple(dims)
        self.dtype = dtype
        self.to = to
        self.from_ = from_

    def __repr__(self) -> str:
        return f"{type(self).__name__}({', '.join(_describe(d) for d in self.dims)})"


class In(_Buffer):
    """A buffer the host fills and the array reads."""

    direction = "in"

    def __init__(self, *dims, dtype=bfloat16, to=None) -> None:
        super().__init__(*dims, dtype=dtype, to=to)


class Out(_Buffer):
    """A buffer the array writes and the host reads."""

    direction = "out"

    def __init__(self, *dims, dtype=bfloat16, from_=None) -> None:
        super().__init__(*dims, dtype=dtype, from_=from_)


class InOut(_Buffer):
    """A buffer read and written in place."""

    direction = "inout"


class _Stream(_Member):
    """A stream into or out of the array, in tile units.

    ``per=`` names the overlay dimension the stream is replicated over (one
    fifo per column, say), or a tuple of dimensions whose product is the
    count (columns x channels); ``broadcast=True`` is one fifo every worker
    consumes. ``via=`` pins the shim endpoint(s). ``depth`` is the fifo depth.
    """

    direction: ClassVar[str] = ""

    def __init__(
        self,
        *dims: _DimSpec,
        dtype: Any = bfloat16,
        per: _DimSpec | None = None,
        broadcast: bool = False,
        replicate: bool = False,
        via: Shim | list[Shim] | None = None,
        depth: int = 2,
    ) -> None:
        if per is not None and broadcast:
            raise DeclarationError(
                "a stream is either per=<dim> or broadcast, not both"
            )
        if replicate and per is None:
            raise DeclarationError(
                "replicate=True needs per=<dim>: every slot receives the whole buffer"
            )
        self.dims = tuple(dims)
        self.dtype = dtype
        self.per = per
        self.broadcast = broadcast
        # per= slots that each receive the whole buffer (one fill per slot)
        # rather than a share of it.
        self.replicate = replicate
        self.via = via
        self.depth = depth

    def __repr__(self) -> str:
        return f"{type(self).__name__}({', '.join(_describe(d) for d in self.dims)})"


class StreamIn(_Stream):
    """A stream entering the array; its shim end is a producer (MM2S)."""

    direction = "in"


class StreamOut(_Stream):
    """A stream leaving the array; its shim end is a consumer (S2MM)."""

    direction = "out"


class ValueSpec:
    """``Scratchpad[np.int32]``: the annotation of a graph function's per-call parameter."""

    __slots__ = ("kind", "dtype")

    def __init__(self, kind: str, dtype: Any) -> None:
        self.kind, self.dtype = kind, dtype

    def __repr__(self) -> str:
        return f"{self.kind}[{np.dtype(self.dtype).name}]"


class _Value(_Member):
    """A per-call scalar. See :class:`Scratchpad` and :class:`DispatchTime`."""

    kind: ClassVar[str] = ""

    def __init__(self, dtype: Any = np.int32) -> None:
        self.dtype = dtype

    def __class_getitem__(cls, dtype) -> ValueSpec:
        return ValueSpec(cls.kind, dtype)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({np.dtype(self.dtype).name})"


class Scratchpad(_Value):
    """A per-call value patched into a DMA descriptor or read by a core.

    Free per call (a few words and a sync), works under full ELF, cannot
    change a DMA size or stride. Values are limited to 30 bits; ``float32``
    is unsupported by the scratchpad encoding.
    """

    kind = "scratchpad"

    def __init__(self, dtype: Any = np.int32) -> None:
        if np.dtype(dtype).kind == "f":
            raise DeclarationError(
                "Scratchpad values cannot be floating point: the scratchpad "
                "encoding zeroes the top two bits of the value"
            )
        super().__init__(dtype)


class DispatchTime(_Value):
    """A per-call value the instruction stream is regenerated around.

    Can change DMA sizes, strides and offsets; costs a stream regeneration
    and a buffer allocation per call; cannot be packaged as a full ELF.
    """

    kind = "dispatch"


class Resident(_Member):
    """A value the sequence writes into the array before the first DMA.

    Overlay-side: a runtime parameter (trip count, RTP) a core reads. The
    sequence's preamble writes every resident the overlay declares.
    """

    def __init__(
        self,
        dtype: Any = np.int32,
        *,
        address: int | None = None,
        lock: int | None = None,
        optional: bool = False,
    ) -> None:
        self.dtype = dtype
        self.address = address
        self.lock = lock
        # A resident only some configurations of the overlay allocate (a
        # parameter word omitted when its value is a compile-time constant).
        # The preamble skips it when design() left it unbound.
        self.optional = optional

    def __repr__(self) -> str:
        return f"Resident({np.dtype(self.dtype).name})"


# --------------------------------------------------------------------------
# Bound members (what an instance's attribute returns)
# --------------------------------------------------------------------------


class BoundStream:
    """A stream on an overlay instance: concrete tile, count, and fifo handles.

    Resolved lazily, because a tile or a ``per=`` count may name a tunable
    that is ``None`` until :meth:`Overlay.tuned` fills it.
    """

    def __init__(self, member: _Stream, overlay: "Overlay") -> None:
        self.member = member
        self.overlay = overlay
        self.name = member.name
        self.direction = member.direction
        self.broadcast = member.broadcast
        self.replicate = member.replicate
        self.depth = member.depth
        self.via = member.via
        self._handle_slots: list[Any] | None = None

    def _resolve(self, spec) -> int:
        try:
            return _resolve_dim(spec, self.overlay)
        except Incompatible as e:
            raise Incompatible(
                f"stream {self.name!r}: {e}. Tune the overlay first (tuned(dev))"
            ) from None

    @property
    def shape(self) -> tuple[int, ...]:
        return tuple(self._resolve(d) for d in self.member.dims)

    @property
    def dtype(self):
        return _resolve_dtype(self.member.dtype, self.overlay)

    @property
    def count(self) -> int:
        if self.member.per is None:
            return 1
        n = 1
        for ref in self.member.per:
            n *= int(self._resolve(ref))
        return n

    @property
    def _handles(self) -> list[Any]:
        if self._handle_slots is None:
            self._handle_slots = [None] * self.count
        return self._handle_slots

    @property
    def tile(self):
        """The ObjectFifo element type: ``np.ndarray[shape, dtype]``."""
        return np.ndarray[self.shape, np.dtype[self.dtype]]  # type: ignore[misc]

    @property
    def elements(self) -> int:
        return int(np.prod(self.shape))

    def bind(self, handle, index: int = 0) -> None:
        """Bind the shim end of a fifo to this stream (or to one of its slots)."""
        if self._handles[index] is not None:
            raise ValueError(f"stream {self.name!r}[{index}] is already bound")
        self._handles[index] = handle

    def __getitem__(self, index: int) -> "_StreamSlot":
        if not 0 <= index < self.count:
            raise IndexError(f"stream {self.name!r} has {self.count} slots")
        return _StreamSlot(self, index)

    def __iter__(self) -> Iterator["_StreamSlot"]:
        return (self[i] for i in range(self.count))

    def __len__(self) -> int:
        return self.count

    @property
    def handle(self):
        if self.count != 1:
            raise ValueError(f"stream {self.name!r} is per-{self.count}; index it")
        return self._require(0)

    @property
    def handles(self) -> list[Any]:
        return [self._require(i) for i in range(self.count)]

    def pin(self, index: int = 0) -> Shim | None:
        """The declared shim endpoint of slot ``index``, if pinned."""
        via = self.via
        if via is None:
            return None
        if isinstance(via, Shim):
            return via if self.count == 1 else None
        return via[index]

    def _require(self, index: int):
        h = self._handles[index]
        if h is None:
            raise ValueError(
                f"stream {self.name!r}[{index}] was never bound: the overlay's "
                f"design() must call .bind() on every declared stream"
            )
        return h

    def __repr__(self) -> str:
        return f"<{self.direction} stream {self.name} {self.shape} x{self.count}>"


class _StreamSlot:
    __slots__ = ("stream", "index")

    def __init__(self, stream: BoundStream, index: int) -> None:
        self.stream = stream
        self.index = index

    def bind(self, handle) -> None:
        self.stream.bind(handle, self.index)

    @property
    def handle(self):
        return self.stream._require(self.index)

    @property
    def name(self) -> str:
        return f"{self.stream.name}{self.index}"

    @property
    def shim(self) -> Shim | None:
        return self.stream.pin(self.index)


class BoundBuffer:
    """A buffer on an operator instance: concrete shape and dtype."""

    def __init__(self, member: _Buffer, op: "Operator") -> None:
        self.member = member
        self._op = op
        self.name = member.name
        self.direction = member.direction
        self.to = member.to
        self.from_ = member.from_

    # Resolved on use, not at construction: a shape or dtype may follow a
    # tunable the device fills (flm/gemm's B layout), and an operator on an
    # untuned overlay is still a valid thing to hold.
    @property
    def shape(self) -> tuple[int, ...]:
        return _resolve_shape(self.member.dims, self._op)

    @property
    def dtype(self):
        return _resolve_dtype(self.member.dtype, self._op)

    @property
    def elements(self) -> int:
        return int(np.prod(self.shape)) if self.shape else 1

    @property
    def nbytes(self) -> int:
        return self.elements * np.dtype(self.dtype).itemsize

    @property
    def flat_type(self):
        """The runtime-sequence argument type: the buffer flattened to 1-D."""
        return np.ndarray[(self.elements,), np.dtype[self.dtype]]  # type: ignore[misc]

    def stream(self, overlay: "Overlay") -> BoundStream | None:
        """The bound stream this buffer feeds or drains on ``overlay``."""
        member = self.to if self.direction == "in" else self.from_
        if member is None:
            return None
        return getattr(overlay, member.name)

    @property
    def batch_axes(self) -> int:
        """Leading ``optional()`` dimensions that are present on this instance."""
        n = 0
        for d in self.member.dims:
            if not isinstance(d, _Optional):
                break
            if _resolve_dim(d.ref, self._op) > 1:
                n += 1
        return n

    def __getitem__(self, index) -> "BufferView":
        """A basic slice of this buffer, for ``rt.fill``/``rt.drain`` in an override.

        A slice start may be a :class:`Scratchpad` value, in which case the
        transfer's base address is patched per call.
        """
        return BufferView(self, index)

    def __repr__(self) -> str:
        return (
            f"<{self.direction} {self.name} {self.shape} {np.dtype(self.dtype).name}>"
        )


class BufferView:
    """``buffer[index]``: a slice of a bound buffer, resolved to a transfer by the build."""

    def __init__(self, buffer: BoundBuffer, index) -> None:
        self.buffer = buffer
        self.index = index if isinstance(index, tuple) else (index,)
        self.offset_by: BoundValue | None = None
        static = []
        for idx in self.index:
            if isinstance(idx, slice) and isinstance(idx.start, BoundValue):
                if idx.stop is not None or idx.step is not None:
                    raise ValueError(
                        f"{buffer.name}[{idx}]: a per-call start takes the whole axis"
                    )
                if self.offset_by is not None:
                    raise ValueError(
                        f"{buffer.name}: only one axis may start at a per-call value"
                    )
                if idx.start.kind != "scratchpad":
                    raise ValueError(
                        f"{buffer.name}: {idx.start.name} is {idx.start.kind}; only a "
                        f"Scratchpad value can move a transfer's base address"
                    )
                self.offset_by = idx.start
                static.append(slice(None))
            else:
                static.append(idx)
        self.static_index = tuple(static)

    def pattern(self) -> tuple[int, list[int], list[int]]:
        """``(offset, sizes, strides)`` of the static part of the slice."""
        from .tiling import view

        return view(self.buffer.shape, self.static_index)

    def __repr__(self) -> str:
        return f"{self.buffer.name}[{self.index}]"


class BoundValue:
    """A per-call value on an operator (or, for a core-read Scratchpad, an overlay).

    On a full ELF ``param`` is the upstream ``ScratchpadParameter`` the
    build creates. On an image without a scratchpad (xclbin, spike S2) the
    value is lowered as a dispatch-time scalar of the sequence: ``param`` is
    the dispatch parameter, ``ssa`` its live value inside the sequence body,
    an offset use adds it to the transfer's offset, and a core-read use is a
    resident the preamble writes from it (``bind``, as a Resident binds).
    """

    def __init__(self, member: _Value, owner) -> None:
        self.member = member
        self.name = member.name
        self.kind = member.kind
        self.dtype = member.dtype
        self.param = None  # the upstream ScratchpadParameter, set by the build
        self.symbol: str | None = None
        self.ssa = None  # the sequence's scalar, when lowered at dispatch time
        self.targets: list[tuple[Any, int]] = []

    def bind(self, buffers, index: int = 0) -> None:
        """Bind to one runtime-parameter buffer, or one per worker; the preamble
        writes ``[index]`` from the per-call value (an image without a scratchpad)."""
        if not isinstance(buffers, (list, tuple)):
            buffers = [buffers]
        self.targets.extend((b, index) for b in buffers)

    def __repr__(self) -> str:
        return f"<{self.kind} {self.name} {np.dtype(self.dtype).name}>"


class BoundResident:
    """A resident on an overlay instance; ``bind()`` names what the preamble writes."""

    def __init__(self, member: Resident, overlay: "Overlay") -> None:
        self.member = member
        self.name = member.name
        self.dtype = member.dtype
        self.address = member.address
        self.lock = member.lock
        self.optional = member.optional
        self.targets: list[tuple[Any, int]] = []

    def bind(self, buffers, index: int = 0) -> None:
        """Bind to one runtime-parameter buffer, or one per worker; the preamble writes ``[index]``."""
        if not isinstance(buffers, (list, tuple)):
            buffers = [buffers]
        self.targets.extend((b, index) for b in buffers)

    def __repr__(self) -> str:
        return f"<resident {self.name} {np.dtype(self.dtype).name}>"


# --------------------------------------------------------------------------
# Resolution
# --------------------------------------------------------------------------


def _lookup_ref(ref: DimRef, instance) -> Any:
    """Follow a DimRef from an instance: its own class, or its overlay's class."""
    if isinstance(instance, ref.owner):
        return getattr(instance, ref.name)
    ov = getattr(instance, "ov", None)
    if ov is not None and isinstance(ov, ref.owner):
        return getattr(ov, ref.name)
    raise DeclarationError(
        f"{ref!r} is not reachable from {type(instance).__name__}: a shape may "
        f"reference the class's own fields or its overlay's"
    )


def _resolve_dim(spec, instance) -> int:
    if isinstance(spec, bool):
        raise DeclarationError(f"{spec!r} is not a dimension")
    if isinstance(spec, (int, np.integer)):
        return int(spec)
    if isinstance(spec, DimRef):
        value = _lookup_ref(spec, instance)
        if value is None:
            raise Incompatible(
                f"{spec!r} is None; it must be set before the shape can be resolved"
            )
        return int(value)
    if isinstance(spec, Field):
        # A same-class reference the decorator did not rewrite: resolve by name.
        return int(getattr(instance, spec.name))
    raise DeclarationError(f"cannot resolve {spec!r} as a dimension")


def _flag_value(flag, instance) -> bool:
    if isinstance(flag, DimRef):
        value = _lookup_ref(flag, instance)
        if value is None:
            raise Incompatible(
                f"{flag!r} is None; a select() on it needs a tuned overlay"
            )
        return bool(value)
    if isinstance(flag, Field):
        return bool(getattr(instance, flag.name))
    return bool(flag)


def _resolve_shape(dims, instance) -> tuple[int, ...]:
    out: list[int] = []
    for d in dims:
        if isinstance(d, _Optional):
            n = _resolve_dim(d.ref, instance)
            if n > 1:
                out.append(n)
            continue
        if isinstance(d, _Select):
            branch = d.when_true if _flag_value(d.flag, instance) else d.when_false
            out.extend(_resolve_shape(branch, instance))
            continue
        out.append(_resolve_dim(d, instance))
    return tuple(out)


def _resolve_dtype(spec, instance):
    if isinstance(spec, DimRef):
        return _lookup_ref(spec, instance)
    if isinstance(spec, Field):
        return getattr(instance, spec.name)
    return spec


# --------------------------------------------------------------------------
# The decorator
# --------------------------------------------------------------------------


def _members_of(cls: type) -> list[_Member]:
    """Members declared in this class body and its ``@operator`` bases, in order.

    The most derived class's body order wins for the members it declares;
    inherited members it does not redeclare follow, in their own order. So a
    subclass that inserts a buffer between two inherited ones (a weight
    between an input and an output) gets the order it wrote. A member the
    subclass sets to ``None`` is hidden.
    """
    ordered: dict[str, _Member] = {}
    seen: set[str] = set()
    for klass in cls.__mro__:
        for name, value in vars(klass).items():
            if name in seen:
                continue
            seen.add(name)
            # A subclass hides an inherited member by assigning it None: a
            # external overlay of a built one keeps its fields and streams but
            # not its residents, whose block the image lays out differently.
            if isinstance(value, _Member):
                ordered[name] = value
    return list(ordered.values())


def _rewrite_refs(specs: tuple, cls: type, fields_by_obj: dict[int, Field]) -> tuple:
    """Replace same-class Field objects in a member's dims with DimRefs."""
    out = []
    for spec in specs:
        if isinstance(spec, _Optional):
            out.append(_Optional(_rewrite_refs((spec.ref,), cls, fields_by_obj)[0]))
        elif isinstance(spec, _Select):
            out.append(
                _Select(
                    _rewrite_refs((spec.flag,), cls, fields_by_obj)[0],
                    _rewrite_refs(spec.when_true, cls, fields_by_obj),
                    _rewrite_refs(spec.when_false, cls, fields_by_obj),
                )
            )
        elif isinstance(spec, Field):
            f = fields_by_obj.get(id(spec))
            if f is None:
                raise DeclarationError(
                    f"{cls.__name__}: a shape references a field object that is "
                    f"not one of this class's fields"
                )
            out.append(getattr(cls, f.name))  # the DimRef re-attached to the class
        else:
            out.append(spec)
    return tuple(out)


def _check_dim_ref(
    cls: type, member: _Member, spec, what: str, *, allow_tunable: bool
) -> None:
    """The shape rule.

    A host buffer's dimension is a ``dim()`` field or an integer: never a
    tunable (inference would cycle through tuning) and never an expression.
    A stream's tile dimension may also be a tunable, since choosing the tile
    is what tuning is for; inference never reads a stream.
    """
    if isinstance(spec, _Optional):
        _check_dim_ref(cls, member, spec.ref, what, allow_tunable=allow_tunable)
        return
    if isinstance(spec, _Select):
        for d in spec.when_true + spec.when_false:
            _check_dim_ref(cls, member, d, what, allow_tunable=allow_tunable)
        return
    if isinstance(spec, bool):
        raise DeclarationError(
            f"{cls.__name__}.{member.name}: {spec!r} is not a {what}"
        )
    if isinstance(spec, (int, np.integer)):
        return
    if isinstance(spec, DimRef):
        allowed = ("dim", "tunable") if allow_tunable else ("dim",)
        if spec.tier not in allowed:
            why = (
                "a tunable; a host shape may not depend on tuning"
                if spec.tier == "tunable"
                else "not declared with dim()"
            )
            raise DeclarationError(
                f"{cls.__name__}.{member.name}: {what} {spec!r} is {why}. A "
                f"shape dimension is a dim() field or an integer literal"
            )
        return
    raise DeclarationError(
        f"{cls.__name__}.{member.name}: {what} {spec!r} is not a dim() field or an "
        f"integer. Expressions are not allowed in shapes; declare the result as a field"
    )


def operator(cls: type) -> type:
    """Process an :class:`Overlay` or :class:`Operator` subclass.

    Applies ``dataclass`` (identity equality; the base supplies ``__eq__``),
    resolves the field objects the class body captured in its shapes to
    names, re-attaches every field as a :class:`DimRef`, checks the shape
    rule, and records the members in declaration order.
    """
    if not (issubclass(cls, Overlay) or issubclass(cls, Operator)):
        raise DeclarationError(
            f"@operator applies to Overlay or Operator subclasses, not {cls}"
        )

    # Members must be unannotated, or dataclass would make them constructor args.
    annotations = cls.__dict__.get("__annotations__", {})
    for name, value in list(vars(cls).items()):
        if isinstance(value, _Member) and name in annotations:
            raise DeclarationError(
                f"{cls.__name__}.{name}: members are declared without an "
                f"annotation; annotating one turns it into a constructor argument"
            )

    # The Field objects the class body bound to bare names, before dataclass
    # processing renames/replaces them.
    pre_fields = {id(v): v for v in vars(cls).values() if isinstance(v, Field)}

    # Overlays get the generated repr; Operators define their own on the base.
    cls = dataclasses.dataclass(cls, eq=False, repr=issubclass(cls, Overlay))  # type: ignore[call-overload]

    fields = {f.name: f for f in dataclasses.fields(cls)}
    fields_by_obj = {i: f for i, f in pre_fields.items()}
    # dataclass reuses the same Field object and sets .name, so identity holds.
    for f in fields.values():
        fields_by_obj.setdefault(id(f), f)

    # Re-attach every field as a DimRef on the class.
    for f in fields.values():
        setattr(cls, f.name, DimRef(cls, f.name, _tier_of(f), f.default))

    members = _members_of(cls)
    for m in members:
        if m.owner is not cls:
            continue  # inherited; already processed on its own class
        if isinstance(m, (_Buffer, _Stream)):
            m.dims = _rewrite_refs(m.dims, cls, fields_by_obj)
            if isinstance(m.dtype, Field):
                m.dtype = getattr(cls, fields_by_obj[id(m.dtype)].name)
            for d in m.dims:
                _check_dim_ref(
                    cls, m, d, "dimension", allow_tunable=isinstance(m, _Stream)
                )
        if isinstance(m, _Stream) and m.per is not None:
            per = m.per if isinstance(m.per, tuple) else (m.per,)
            per = _rewrite_refs(per, cls, fields_by_obj)
            for ref in per:
                if not isinstance(ref, DimRef) or ref.tier is None:
                    raise DeclarationError(
                        f"{cls.__name__}.{m.name}: per={ref!r} must be a dim() or tunable() field"
                    )
            m.per = per

    cls._members = tuple(members)  # type: ignore[attr-defined]
    cls._dim_fields = tuple(f.name for f in fields.values() if _tier_of(f) == "dim")  # type: ignore[attr-defined]
    cls._tunable_fields = tuple(
        f.name for f in fields.values() if _tier_of(f) == "tunable"
    )  # type: ignore[attr-defined]

    if issubclass(cls, Overlay):
        _finish_overlay(cls)
    else:
        _finish_operator(cls, fields)
    return cls


def _finish_overlay(cls: type) -> None:
    images = [v for v in vars(cls).values() if isinstance(v, Xclbin)]
    if len(images) > 1:
        raise DeclarationError(f"{cls.__name__} declares more than one Xclbin")
    if images:
        cls._external = images[0]  # type: ignore[attr-defined]
    for m in cls._members:  # type: ignore[attr-defined]
        if isinstance(m, (_Buffer, DispatchTime)):
            raise DeclarationError(
                f"{cls.__name__}.{m.name}: an Overlay declares streams, residents and "
                f"core-read Scratchpad values; buffers and DispatchTime values belong "
                f"on the Operator"
            )
        if images and isinstance(m, _Stream) and m.via is None:
            raise DeclarationError(
                f"{cls.__name__}.{m.name}: a stream of an external overlay must be "
                f"pinned with via=; nothing else says which shim it uses"
            )
        if images and isinstance(m, Resident) and m.address is None:
            raise DeclarationError(
                f"{cls.__name__}.{m.name}: a resident of an external overlay needs "
                f"an address; the sequence writes it there"
            )

    if not images:
        return
    for hook in ("prebuilt", "build"):
        if getattr(cls, hook) is getattr(Overlay, hook):
            raise DeclarationError(
                f"{cls.__name__} declares an Xclbin, so nothing builds its array: "
                f"it must supply {hook}() (iron.common.external.External "
                f"does, for a downloaded image)"
            )


def _finish_operator(cls: type, fields: dict[str, Field]) -> None:
    overlay_cls = _overlay_class_of(cls)
    cls._overlay_class = overlay_cls  # type: ignore[attr-defined]
    for m in cls._members:  # type: ignore[attr-defined]
        if isinstance(m, (_Stream, Resident)):
            raise DeclarationError(
                f"{cls.__name__}.{m.name}: an Operator declares buffers and per-call "
                f"values; streams and residents belong on the Overlay"
            )
        if isinstance(m, _Buffer):
            target = m.to if m.direction == "in" else m.from_
            if m.direction == "inout":
                target = m.to or m.from_
            if target is not None and not isinstance(target, _Stream):
                raise DeclarationError(
                    f"{cls.__name__}.{m.name}: to=/from_= must name a stream, got {target!r}"
                )
            if (
                target is not None
                and overlay_cls is not None
                and not issubclass(overlay_cls, target.owner)  # type: ignore[arg-type]
            ):
                raise DeclarationError(
                    f"{cls.__name__}.{m.name}: stream {target!r} belongs to "
                    f"{target.owner.__name__}, not to {overlay_cls.__name__}"  # type: ignore[union-attr]
                )
            if m.to is not None and m.to.direction != "in":
                raise DeclarationError(
                    f"{cls.__name__}.{m.name}: to= must be a StreamIn"
                )
            if m.from_ is not None and m.from_.direction != "out":
                raise DeclarationError(
                    f"{cls.__name__}.{m.name}: from_= must be a StreamOut"
                )
            for d in m.dims:
                ref = d.ref if isinstance(d, _Optional) else d
                if (
                    isinstance(ref, DimRef)
                    and not issubclass(cls, ref.owner)
                    and overlay_cls is not None
                ):
                    if not issubclass(overlay_cls, ref.owner):
                        raise DeclarationError(
                            f"{cls.__name__}.{m.name}: {ref!r} is neither a field of "
                            f"{cls.__name__} nor of its overlay {overlay_cls.__name__}"
                        )

    # Classic construction: overlay fields as keyword arguments. The operator
    # builds the overlay itself. Untyped, and goes away once every call site
    # passes an overlay.
    if overlay_cls is not None:
        generated_init = cls.__init__

        def __init__(self, ov=None, *args, **kwargs):
            if ov is None or not isinstance(ov, Overlay):
                if ov is not None:
                    args = (ov,) + args
                ov, kwargs = type(self)._split_kwargs(dict(kwargs))
            generated_init(self, ov, *args, **kwargs)

        __init__.__wrapped__ = generated_init  # type: ignore[attr-defined]
        cls.__init__ = __init__  # type: ignore[misc]


def _overlay_class_of(cls: type) -> type | None:
    """The ``O`` in ``class X(Operator[O])``, searched up the bases."""
    for klass in cls.__mro__:
        for base in getattr(klass, "__orig_bases__", ()):
            args = getattr(base, "__args__", ())
            for a in args:
                if isinstance(a, type) and issubclass(a, Overlay):
                    return a
    return None


# --------------------------------------------------------------------------
# Overlay
# --------------------------------------------------------------------------


class Overlay:
    """What configures the array. Subclass, decorate with ``@operator``.

    Declare ``dim()`` and ``tunable()`` fields, streams, and residents in the
    class body; implement :meth:`tuning` to fill tunables from the device and
    :meth:`design` to build the array and bind each stream to a fifo's shim
    end. See the module docstring for the shape.
    """

    _members: ClassVar[tuple[_Member, ...]] = ()
    _dim_fields: ClassVar[tuple[str, ...]] = ()
    _tunable_fields: ClassVar[tuple[str, ...]] = ()
    _external: ClassVar[Xclbin | None] = None

    @property
    def external(self) -> Xclbin | None:
        """The downloaded image this overlay is, if IRON did not build it."""
        return type(self)._external

    # -- placement ---------------------------------------------------------

    @classmethod
    def shim_columns(cls, dev, num_channels: int = 1) -> int:
        """How many of ``dev``'s columns this overlay's shim budget allows.

        One core per (column, channel) fills one fifo per input stream from
        the shim and drains one per output, so a column costs
        ``max(inputs, outputs) * num_channels`` channels in the busier
        direction. A ``replicate`` stream is shared by every column of a
        channel, so it is paid once per channel rather than per column.
        """
        streams = [m for m in cls._members if isinstance(m, _Stream)]
        shared = [m for m in streams if m.replicate]
        per_core = [m for m in streams if not m.replicate]
        directions = [m.direction for m in per_core]
        cost = max(directions.count("in"), directions.count("out")) * num_channels
        fixed = len(shared) * num_channels
        limit = get_shim_dma_limit(dev)
        return max(1, min(dev.cols, (limit - fixed) // cost))

    def check_shim_columns(self, dev, cols: int, num_channels: int = 1) -> None:
        """Raise :class:`Untunable` if ``cols`` exceeds the shim budget."""
        allowed = type(self).shim_columns(dev, num_channels)
        if cols > allowed:
            raise Untunable(
                f"{type(self).__name__} with {cols} columns x {num_channels} "
                f"channels exceeds this device's shim DMA budget; "
                f"{allowed} columns fit"
            )

    # -- an overlay IRON does not design() ---------------------------------

    def prebuilt(self) -> Path:
        """The file the declared :class:`Xclbin` names, fetched if it is not
        already in the cache."""
        raise NotImplementedError(
            f"{type(self).__name__} declares an Xclbin but no prebuilt()"
        )

    def build(self, dev, op: "Operator"):
        """The MLIR module for ``op`` on this overlay, when ``design()`` does
        not build the array: a runtime sequence against the prebuilt image."""
        raise NotImplementedError(
            f"{type(self).__name__} declares an Xclbin but no build()"
        )

    # -- the sequence, when the overlay owns it -----------------------------

    def sequence(self, op: "Operator", rt) -> None:
        """The runtime sequence for ``op`` on this overlay, when the overlay
        rather than the operator knows it: a external image consumes its
        transfers in the order it was built for, whatever operator drives it.
        Takes precedence over the operator's ``design(rt)``."""
        raise NotImplementedError

    @classmethod
    def has_sequence(cls) -> bool:
        return cls.sequence is not Overlay.sequence

    def resident_values(self, op: "Operator") -> dict[str, Any]:
        """The words for this overlay's residents, from ``op``. By default the
        operator's own ``residents()``; an external overlay lays the operator's
        values out into the block its image reads."""
        return op.residents()

    def __post_init__(self) -> None:
        self._tuned = False
        self._specialised: dict[str, Any] = {}
        self.validate()
        self._bind()

    # -- declared surface --------------------------------------------------

    def validate(self) -> None:
        """Check the compile-time fields. Runs at construction and after tuning."""

    def tuning(self, dev) -> "Overlay":
        """Return a copy with every tunable filled for ``dev``; raise :class:`Untunable`.

        Sees the device and nothing else, so a tuned overlay serves every
        extent. The default fills nothing.
        """
        return self

    def device(self, target):
        """The device the Program is built for; the current device by default.

        An overlay that builds for a column subset (gemm's NPU1Col1/NPU1Col2)
        returns that variant.
        """
        return target.dev

    def design(self, target) -> list:
        """Build the array for ``target`` and return its workers.

        ``target`` (:class:`iron.common.build.Target`) carries the device,
        the kernel tree, and ``kernel()``/``barrier()`` helpers that apply
        the fusion prefix so the overlay never sees it. Must call
        ``.bind(handle)`` on every declared stream (or on every slot of a
        ``per=`` stream) with the shim end of the fifo that carries it, and
        ``.bind(buffers)`` on every declared resident.
        """
        raise NotImplementedError(f"{type(self).__name__}.design() is not implemented")

    # -- library surface ---------------------------------------------------

    def tuned(self, dev) -> "Overlay":
        if self._tuned:
            return self
        new = self.tuning(dev)
        if not isinstance(new, type(self)):
            raise TypeError(
                f"{type(self).__name__}.tuning() must return a {type(self).__name__}, "
                f"got {type(new).__name__}"
            )
        missing = [n for n in self._tunable_fields if getattr(new, n) is None]
        if missing:
            raise Untunable(
                f"{type(self).__name__}.tuning() left {missing} unset for {dev}"
            )
        new.validate()
        new._tuned = True
        new._specialised = dict(self._specialised)
        new._bind()
        return new

    def for_extent(self, **overrides) -> "Overlay":
        """A specialised copy: tunables set for one extent, at the cost of sharing."""
        bad = [k for k in overrides if k not in self._tunable_fields]
        if bad:
            raise TypeError(f"for_extent() sets non-tunable fields {bad}")
        new = dataclasses.replace(self, **overrides)
        new._specialised = {**self._specialised, **overrides}
        new._tuned = self._tuned
        new._bind()
        return new

    @property
    def specialised(self) -> bool:
        return bool(self._specialised)

    def value_symbol(self, value: "BoundValue") -> str | None:
        """An explicit device symbol for a core-read per-call value, or ``None``."""
        return None

    def design_key(self) -> tuple:
        """Identity for sharing: the class and every compared field value."""
        return (type(self).__qualname__,) + tuple(
            (f.name, getattr(self, f.name))
            for f in dataclasses.fields(self)
            if f.compare
        )

    def copy(self) -> "Overlay":
        """A fresh instance with the same fields and tuning state.

        A build works on a copy, so anything ``compatible()`` records on the
        overlay for one operator never reaches another that shares it.
        """
        new = dataclasses.replace(self)
        new._tuned = self._tuned
        new._specialised = dict(self._specialised)
        new._bind()
        return new

    def __eq__(self, other) -> bool:
        if not isinstance(other, Overlay):
            return NotImplemented
        return self.design_key() == other.design_key()

    def __hash__(self) -> int:
        return hash(self.design_key())

    @property
    def streams(self) -> dict[str, BoundStream]:
        return {
            m.name: self._bound[m.name] for m in self._members if isinstance(m, _Stream)
        }

    @property
    def residents(self) -> dict[str, BoundResident]:
        return {
            m.name: self._bound[m.name]
            for m in self._members
            if isinstance(m, Resident)
        }

    @property
    def values(self) -> list[BoundValue]:
        """Core-read per-call values this overlay declares."""
        return [self._bound[m.name] for m in self._members if isinstance(m, _Value)]

    def _bind(self) -> None:
        bound: dict[str, Any] = {}
        for m in self._members:
            if isinstance(m, _Stream):
                bound[m.name] = BoundStream(m, self)
            elif isinstance(m, Resident):
                bound[m.name] = BoundResident(m, self)
            elif isinstance(m, _Value):
                bound[m.name] = BoundValue(m, self)
        self._bound = bound

    def name_parts(self) -> list[str]:
        return [
            f"{_NAME_ALIASES.get(f.name, f.name)}{serialize_param(getattr(self, f.name))}"
            for f in dataclasses.fields(self)
            if f.repr and getattr(self, f.name) is not None
        ]


# --------------------------------------------------------------------------
# Operator
# --------------------------------------------------------------------------

O = TypeVar("O", bound=Overlay)


class _OperatorMeta(ABCMeta):
    """``GEMV(w, h)`` inside a graph function records a step; anything else constructs.

    The class tells the two apart by whether it received graph handles (or
    host tensors, which a graph closes over as weights); see
    :mod:`iron.common.graph`. Outside a graph the call constructs as usual.
    """

    def __call__(cls, *args, **kwargs):
        from . import graph as _graph

        tracer = _graph.current()
        if tracer is not None and args and all(_graph.is_operand(a) for a in args):
            return tracer.call(cls, args, kwargs)
        return super().__call__(*args, **kwargs)


@dataclasses.dataclass(eq=False, repr=True)
class Operator(Generic[O], metaclass=_OperatorMeta):
    """A host ABI declared against an overlay. Subclass, decorate with ``@operator``.

    Declare ``dim()`` fields and buffers (``In``/``Out``/``InOut`` naming their
    streams) in the class body. Implement :meth:`reference`; optionally
    :meth:`compatible` and :meth:`design` (an override for a sequence the
    library cannot derive).
    """

    ov: O

    _members: ClassVar[tuple[_Member, ...]] = ()
    _dim_fields: ClassVar[tuple[str, ...]] = ()
    _tunable_fields: ClassVar[tuple[str, ...]] = ()
    _overlay_class: ClassVar[type | None] = None

    def __post_init__(self) -> None:
        if self._overlay_class is not None and not isinstance(
            self.ov, self._overlay_class
        ):
            raise TypeError(
                f"{type(self).__name__} is declared against {self._overlay_class.__name__}, "
                f"got {type(self.ov).__name__}"
            )
        self.validate()
        self._bind()

    # -- declared surface --------------------------------------------------

    def validate(self) -> None:
        """Check the sequence-tier fields on their own. Runs at construction."""

    def compatible(self) -> None:
        """Check the extents against the tuned overlay; raise :class:`Incompatible`."""

    def reference(self, *inputs):
        raise NotImplementedError(
            f"{type(self).__name__}.reference() is not implemented"
        )

    def design(self, rt) -> None:
        """Override to write the runtime sequence by hand; otherwise it is derived.

        ``rt`` is an :class:`iron.common.build.Sequence`: ``rt.fill(stream,
        view)``, ``rt.drain(stream, view)``, ``rt.group()``. The preamble
        (residents, barriers, parameter sync) has already run.
        """
        raise NotImplementedError

    def residents(self) -> dict[str, int]:
        """Values for the overlay's residents (trip counts, RTPs), from the extents."""
        return {}

    @classmethod
    def has_design_override(cls) -> bool:
        return cls.design is not Operator.design

    # -- library surface ---------------------------------------------------

    @classmethod
    def overlay_defaults(cls, kwargs: dict) -> None:
        """Fill, in place, overlay tunables this operator's own extent decides.

        An overlay is tuned from the device alone, so a tunable whose right
        value follows from the operator's shape (a copy's transfer size from
        its sizes) is defaulted here, at construction, when it was not
        given. The default fills nothing.
        """

    @classmethod
    def _split_kwargs(cls, kwargs: dict) -> tuple["Overlay", dict]:
        """Split keyword arguments into the overlay's and the operator's own."""
        overlay_cls = cls._overlay_class
        assert overlay_cls is not None
        cls.overlay_defaults(kwargs)
        names = {f.name for f in dataclasses.fields(overlay_cls) if f.init}
        ov_kwargs = {k: kwargs.pop(k) for k in list(kwargs) if k in names}
        return overlay_cls(**ov_kwargs), kwargs

    def value_symbol(self, value: "BoundValue") -> str | None:
        """An explicit device symbol for a per-call value, or ``None`` for the default."""
        return None

    def design_key(self):
        """Identity for sharing a build: the class, the overlay's key, every compared field.

        Two operators with equal keys generate byte-identical MLIR, so a
        sequence builds, prefixes and configures the design once.
        """
        return (
            type(self).__qualname__,
            self.ov.design_key(),
            tuple(
                (f.name, getattr(self, f.name))
                for f in dataclasses.fields(self)
                if f.compare and f.name != "ov"
            ),
        )

    def tuned(self, dev) -> "Operator":
        """A copy bound to its own tuned copy of the overlay, with :meth:`compatible` checked."""
        ov = self.ov.tuned(dev).copy()
        new = dataclasses.replace(self, ov=ov)
        # What a graph bound on this instance is part of it, not of a field:
        # the build works on the copy, and a copy that forgot would silently
        # drop the per-call value from the sequence.
        if self.used_values:
            new.__dict__["_used_values"] = set(self.used_values)
        new.compatible()
        return new

    @property
    def buffers(self) -> list[BoundBuffer]:
        return [self._bound[m.name] for m in self._members if isinstance(m, _Buffer)]

    @property
    def inputs(self) -> list[BoundBuffer]:
        return [b for b in self.buffers if b.direction in ("in", "inout")]

    @property
    def outputs(self) -> list[BoundBuffer]:
        return [b for b in self.buffers if b.direction in ("out", "inout")]

    @property
    def values(self) -> list[BoundValue]:
        """The per-call values this instance uses (see :meth:`uses_value`)."""
        return [
            self._bound[m.name]
            for m in self._members
            if isinstance(m, _Value) and self.uses_value(m.name)
        ]

    def uses_value(self, name: str) -> bool:
        """Whether this instance drives the declared per-call value ``name``.

        A value an instance does not use gets no device parameter and no
        sync. The default is every declared value; an operator whose values
        are optional (a strided copy with or without a patched offset)
        overrides this, and a graph binding one calls :meth:`use_value`.
        """
        return True

    def use_value(self, name: str) -> None:
        """Record that a graph binds the per-call value ``name`` on this instance."""
        if not any(isinstance(m, _Value) and m.name == name for m in self._members):
            raise TypeError(
                f"{type(self).__name__} declares no per-call value {name!r}"
            )
        self.__dict__.setdefault("_used_values", set()).add(name)

    @property
    def used_values(self) -> frozenset:
        return frozenset(self.__dict__.get("_used_values", ()))

    # -- graph functions ---------------------------------------------------

    @classmethod
    def resolve_class(cls, n_operands: int, kwargs: dict) -> type:
        """The class a graph call with ``n_operands`` operands constructs.

        The default is the class itself; a family that picks a subclass from
        its arguments (RMSNorm with a weight) overrides.
        """
        return cls

    def __call__(self, *args, **kwargs):
        """An explicit instance applied to graph handles records a step."""
        from . import graph as _graph

        tracer = _graph.current()
        if tracer is None:
            raise TypeError(
                f"{type(self).__name__} instances are called on graph handles inside "
                f"an @iron.graph function; outside one, compile() and get_callable()"
            )
        return tracer.call(self, args, kwargs)

    def _bind(self) -> None:
        bound: dict[str, Any] = {}
        for m in self._members:
            if isinstance(m, _Buffer):
                bound[m.name] = BoundBuffer(m, self)
            elif isinstance(m, _Value):
                bound[m.name] = BoundValue(m, self)
        self._bound = bound

    # -- inference ---------------------------------------------------------

    @classmethod
    def from_spec(
        cls,
        name: str,
        *,
        inputs: dict[str, tuple[int, ...]],
        outputs: dict[str, tuple[int, ...]],
        dtype: Any = bfloat16,
        key: str = "",
        params: dict[str, Any] | None = None,
        generator: Callable | None = None,
    ) -> type:
        """An operator class from an exported description, at run time.

        The dynamic escape for a design whose shapes come from a file rather
        than a formula (swiglu_prefill_stream's stream-dse export). ``inputs``
        and ``outputs`` are literal shapes in argument order; ``params`` are
        the numbers that identify the instance (they become ``dim()`` fields
        with those defaults and reach the name); ``key`` identifies the
        generated design, for sharing; ``generator`` replaces
        :meth:`generator`, since the sequence is not derived. The
        overlay is a stand-in carrying only ``key``.
        """
        import types

        def overlay_ns(ns):
            ns["__module__"] = cls.__module__
            ns["__annotations__"] = {"key": str}
            ns["key"] = dim(key, repr=False)

        overlay_cls = operator(
            types.new_class(f"{name}Overlay", (Overlay,), {}, overlay_ns)
        )

        def operator_ns(ns):
            ns["__module__"] = cls.__module__
            ns["__annotations__"] = {}
            for pname, value in (params or {}).items():
                ns["__annotations__"][pname] = type(value)
                ns[pname] = dim(value)
            for bname, shape in inputs.items():
                ns[bname] = In(*shape, dtype=dtype)
            for bname, shape in outputs.items():
                ns[bname] = Out(*shape, dtype=dtype)
            ns["design_key"] = lambda self: self.ov.key or None
            if generator is not None:
                ns["generator"] = generator

        return operator(
            types.new_class(name, (cls[overlay_cls],), {}, operator_ns)  # type: ignore[index]
        )

    @classmethod
    def infer(cls, *operand_shapes, outputs=(), **given) -> dict[str, Any]:
        """Bind dimension fields from operand shapes, in ``In`` declaration order.

        A lookup, not a solver: each declared dimension is a field or a
        literal. Returns ``{field: value}`` for both the operator's and the
        overlay's fields; ``given`` pins values and is checked for agreement.
        ``outputs`` are the shapes of caller-supplied ``Out`` buffers, in
        declaration order, which bind the same way.
        """
        ins = [
            m
            for m in cls._members
            if isinstance(m, _Buffer) and m.direction in ("in", "inout")
        ]
        if len(operand_shapes) != len(ins):
            raise TypeError(
                f"{cls.__name__} takes {len(ins)} operand(s) "
                f"({', '.join(m.name for m in ins)}), got {len(operand_shapes)}"
            )
        outs = [
            m for m in cls._members if isinstance(m, _Buffer) and m.direction == "out"
        ]
        if outputs and len(outputs) != len(outs):
            raise TypeError(
                f"{cls.__name__} produces {len(outs)} output(s) "
                f"({', '.join(m.name for m in outs)}), got {len(outputs)}"
            )
        pairs = list(zip(ins, operand_shapes)) + list(zip(outs, outputs))
        bound: dict[str, Any] = dict(given)
        origin: dict[str, str] = {k: "given" for k in given}

        def bind(ref: DimRef, value: int, where: str) -> None:
            key = ref.name
            if key in bound and bound[key] != value:
                raise ValueError(
                    f"{cls.__name__}: {ref!r} is {value} from {where} but "
                    f"{bound[key]} from {origin[key]}"
                )
            bound[key] = value
            origin.setdefault(key, where)

        for m, shape in pairs:
            shape = tuple(int(s) for s in shape)
            dims = list(m.dims)
            leading = dims[0] if dims and isinstance(dims[0], _Optional) else None
            if leading is not None:
                if len(shape) == len(dims):
                    bind(leading.ref, shape[0], f"{m.name}.shape[0]")
                    shape = shape[1:]
                elif len(shape) == len(dims) - 1:
                    bind(leading.ref, 1, f"{m.name} (rank {len(shape)})")
                else:
                    raise ValueError(
                        f"{cls.__name__}: operand {m.name} has rank {len(shape)}, "
                        f"declared {m!r}"
                    )
                dims = dims[1:]
            expanded: list = []
            for d in dims:
                if isinstance(d, _Select):
                    flag = d.flag
                    if flag.name in bound:
                        value = bound[flag.name]
                    else:
                        fld = next(
                            (
                                f
                                for f in dataclasses.fields(flag.owner)
                                if f.name == flag.name
                            ),
                            None,
                        )
                        if fld is None or fld.default is MISSING:
                            raise ValueError(
                                f"{cls.__name__}: {flag!r} selects {m.name}'s shape and "
                                f"has no default; pass it explicitly"
                            )
                        value = fld.default
                    expanded.extend(d.when_true if value else d.when_false)
                else:
                    expanded.append(d)
            dims = expanded
            if len(dims) == 1 and len(shape) != 1:
                # A flat buffer takes an operand of any rank: its one
                # dimension is the element count.
                shape = (int(np.prod(shape)) if shape else 1,)
            if len(shape) != len(dims):
                raise ValueError(
                    f"{cls.__name__}: operand {m.name} has rank {len(shape)} {shape}, "
                    f"declared rank {len(dims)} {m!r}"
                )
            for i, (d, n) in enumerate(zip(dims, shape)):
                if isinstance(d, DimRef):
                    bind(d, n, f"{m.name}.shape[{i}]")
                elif int(d) != n:
                    raise ValueError(
                        f"{cls.__name__}: operand {m.name}.shape[{i}] is {n}, declared {d}"
                    )
        return bound

    @classmethod
    def infer_kwargs(cls, kwargs) -> dict[str, Any]:
        """The part of ``kwargs`` that :meth:`infer` takes: both layers' dimension
        fields and the flags that select a buffer's shape."""
        names = set(cls._dim_fields)
        if cls._overlay_class:
            names.update(cls._overlay_class._dim_fields)
        for m in cls._members:
            if isinstance(m, _Buffer):
                names.update(d.flag.name for d in m.dims if isinstance(d, _Select))
        return {k: v for k, v in kwargs.items() if k in names}

    @classmethod
    def from_operands(cls, *operand_shapes, **overrides) -> "Operator":
        """Construct an operator (and its overlay) from operand shapes."""
        values = cls.infer(*operand_shapes, **cls.infer_kwargs(overrides))
        kwargs = {**overrides, **values}
        return cls(**kwargs)  # classic-construction path splits overlay fields

    # -- the image of one operator on its own -------------------------------

    @property
    def dev(self):
        """The device a design is generated for."""
        import aie.utils as aie_utils

        return aie_utils.get_current_device()

    # Bytes of trace buffer to emit; 0 disables tracing. A plain attribute
    # rather than a property: OperatorSequence and LayerNorm assign it.
    trace_size = 0

    @property
    def name(self) -> str:
        """This instance's label: the class, every shown field of both layers,
        the device. It names the per-call value symbols a host writes through
        and the kernel instances a chained image carries; nothing on disk,
        which the compile cache keys by content."""
        import aie.utils as aie_utils

        own = [
            f"{_NAME_ALIASES.get(f.name, f.name)}{serialize_param(getattr(self, f.name))}"
            for f in dataclasses.fields(self)
            if f.name != "ov" and f.repr and getattr(self, f.name) is not None
        ]
        base = type(self).__name__ + "_" + "_".join(own + self.ov.name_parts())
        dev = aie_utils.get_current_device()
        return f"{base}_{dev.resolve().name}"

    def generator(self, image: str = "elf"):
        """The design generator :class:`CompilableDesign` runs for this operator."""
        from .build import generator_for

        return generator_for(self, image=image)

    def compile(self, record: str = "memory") -> "Operator":
        """Build this operator's own image, once; sets :attr:`artifacts`.

        ``record="disk"`` also writes the :class:`~iron.common.artifacts.Artifacts`
        record beside the image; by default it is only kept in memory.
        """
        if getattr(self, "_artifacts", None) is None:
            self._artifacts = self._build()
            if record == "disk":
                self._artifacts.dump()
        return self

    @property
    def artifacts(self):
        """The record of what :meth:`compile` produced (None before)."""
        return getattr(self, "_artifacts", None)

    def _members_io(self):
        """The declared buffers, without resolving a shape: their names alone."""
        return [m for m in self._members if isinstance(m, _Buffer)]

    def buffer_map(self) -> dict[str, tuple[str, int, int]]:
        """Each buffer as ``(arena, position, nbytes)``, for an image's record.

        From the tuned operator: a shape may follow a tunable the device
        fills (flm/gemm's B layout), and the built image's buffers are the
        tuned ones. A standalone operator has no arena plan -- its buffers
        are the kernel's positional arguments.
        """
        tuned = self.ov._tuned and self or self.tuned(self.dev)
        return {b.name: ("arg", i, b.nbytes) for i, b in enumerate(tuned.buffers)}

    def _build(self):
        """Compile to an xclbin and an instruction stream, or, on an external
        overlay, to the stream alone against the downloaded image."""
        from .artifacts import Artifacts, Design, Step
        from .jit_compile import insts_design, xclbin_design

        image = self.ov.external
        if image is None:
            design = xclbin_design(self.generator(), kernel_name="MLIR_AIE")
            entry = design.get_cache_entry()
            picture, insts = entry.xclbin, entry.insts
        else:
            picture = self.ov.prebuilt()
            design = insts_design(self.generator())
            entry = design.get_cache_entry()
            insts = entry.insts
        self._design = design
        return Artifacts(
            kind="xclbin",
            image=picture,
            insts=insts,
            entry=entry,
            designs=(
                Design(
                    name=self.name,
                    operators=(self.name,),
                    entry=entry,
                    image=picture,
                    insts=insts,
                ),
            ),
            steps=(Step(0, self.name, self.name, tuple(b.name for b in self.buffers)),),
            buffers={b.name: ("arg", i, b.nbytes) for i, b in enumerate(self.buffers)},
        )

    def get_callable(self):
        """The loaded image, ready to call on device tensors."""
        import aie.utils as aie_utils
        from aie.utils.npukernel import NPUKernel

        self.compile()
        image = self.ov.external
        npu_kernel = NPUKernel(
            xclbin_path=str(self.artifacts.image),
            kernel_name="MLIR_AIE" if image is None else image.kernel_name,
            insts_path=str(self.artifacts.insts),
        )
        handle = aie_utils.DefaultNPURuntime.load(npu_kernel)

        def call(*args):
            return aie_utils.DefaultNPURuntime.run(handle, list(args))

        return call

    def __repr__(self) -> str:
        own = ", ".join(
            f"{f.name}={getattr(self, f.name)!r}"
            for f in dataclasses.fields(self)
            if f.repr and f.name != "ov"
        )
        return f"{type(self).__name__}({self.ov!r}, {own})"
