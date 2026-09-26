# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an operator declares besides its fields.

Buffers are the host ABI, and an operand declared with a tile is its own
stream into the array, so direction, dtype and shim binding agree by
construction. The other members are values no host buffer carries: a
:class:`Value` written once per build, or per call when a graph binds it,
and a :class:`Scratchpad` or :class:`DispatchTime` written per call.
"""

from __future__ import annotations

import contextvars
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Generic, TypeVar, overload

import numpy as np
from ml_dtypes import bfloat16

from .field import DeclarationError, _describe, _DimSpec

if TYPE_CHECKING:
    from typing import Self

    # Named in the subclasses' base expressions as strings (bound imports member).
    from .bound import BoundBuffer, BoundStream, BoundValue  # noqa: F401


B = TypeVar("B")  # the bound form an instance serves


class Shim:
    """A pinned shim endpoint: column and DMA channel on row 0."""

    __slots__ = ("col", "channel")

    def __init__(self, col: int, channel: int | None = None) -> None:
        self.col = col
        self.channel = channel

    def __repr__(self) -> str:
        return f"Shim(col={self.col}, channel={self.channel})"


class Xclbin:
    """An image someone else built: a downloaded xclbin, pinned by digest.

    Given as ``image=`` when a class is declared (``class Shipped(GEMM,
    image=Xclbin(...))``). Every stream of such a class is pinned with
    ``via=`` and every derived value has an ``address``, because nothing else
    records where its endpoints are; the library emits the sequence against
    those pins.
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


class _Member(Generic[B]):
    """Base of everything declared unannotated in an Operator body.

    ``__set_name__`` gives the member its name and the class body gives it
    its order. On an instance, ``__get__`` returns the bound form built as
    the class is created (a :class:`BoundBuffer`, :class:`BoundStream` or
    :class:`BoundValue`). ``B`` is that type, so a type checker sees
    ``op.A`` as it.
    """

    name: str = ""
    owner: type | None = None

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name
        self.owner = owner

    @overload
    def __get__(self, instance: None, owner: type | None = None) -> Self: ...
    @overload
    def __get__(self, instance: object, owner: type | None = None) -> B: ...
    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        try:
            return instance._bound[self.name]
        except (AttributeError, KeyError):
            raise AttributeError(
                f"{type(instance).__name__}.{self.name} is not bound yet"
            ) from None


class _Buffer(_Member["BoundBuffer"]):
    """A host buffer: shape in extents, a dtype, and the stream it moves through.

    With ``tile=`` the buffer is its own stream into (or out of) the array:
    ``tile`` is what one fifo element holds, in the units a core reads
    (its dimensions may be knobs), ``per=`` the field the stream is
    replicated over, ``depth`` the fifo depth, ``via=`` a pinned shim
    endpoint. Without it the buffer is an argument of a sequence written by
    hand (:meth:`Operator.sequence`).
    """

    direction: ClassVar[str] = ""

    def __init__(
        self,
        *dims: _DimSpec,
        dtype: Any = bfloat16,
        tile: Any = None,
        per: _DimSpec | None = None,
        depth: int = 2,
        via: "Shim | list[Shim] | None" = None,
        replicate: bool = False,
        broadcast: bool = False,
    ) -> None:
        self.dims = tuple(dims)
        self.dtype = dtype
        self.stream: _Stream | None = None
        if tile is not None:
            tile = tuple(tile) if isinstance(tile, (tuple, list)) else (tile,)
            kind = StreamIn if self.direction == "in" else StreamOut
            self.stream = kind(
                *tile,
                dtype=dtype,
                per=per,
                depth=depth,
                via=via,
                replicate=replicate,
                broadcast=broadcast,
            )

    def __set_name__(self, owner: type, name: str) -> None:
        super().__set_name__(owner, name)
        if self.stream is not None:
            self.stream.__set_name__(owner, name)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({', '.join(_describe(d) for d in self.dims)})"


class In(_Buffer):
    """A buffer the host fills and the array reads."""

    direction = "in"


class Out(_Buffer):
    """A buffer the array writes and the host reads."""

    direction = "out"


class _Stream(_Member["BoundStream"]):
    """An operand's stream into or out of the array, in tile units.

    ``per=`` names the field the stream is replicated over (one fifo per
    column, say), or a tuple of fields whose product is the count (columns
    x channels); ``broadcast=True`` is one fifo every worker consumes.
    ``via=`` pins the shim endpoint(s). ``depth`` is the fifo depth.
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


class _Value(_Member["BoundValue"]):
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


# The extents a ``derive`` reads, recorded while an operator evaluates one
# (see Operator._per_call_derived); None when nothing is recording.
_extent_reads: contextvars.ContextVar[set[str] | None] = contextvars.ContextVar(
    "iron.extent_reads", default=None
)


class Extent(_Value):
    """A shape field a graph may bound per call.

    ``valid = Extent(size)`` reads as ``size`` on an instance until a graph
    bounds an operand the field sizes (``x[:n]``); from then on it is per
    call, and so is every :class:`Value` whose ``derive`` reads it, which the
    host evaluates with the call's bound and writes as a word. The image is
    built for the field's full value, so a bound is at most it. The field is
    a ``param()``.
    """

    kind = "scratchpad"

    def __init__(self, field: Any, dtype: Any = np.int32) -> None:
        super().__init__(dtype)
        self.field = field  # a Field in the class body; the DimRef once declared

    @overload
    def __get__(self, instance: None, owner: type | None = None) -> Self: ...
    @overload
    def __get__(self, instance: object, owner: type | None = None) -> int: ...
    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        reads = _extent_reads.get()
        if reads is not None:
            reads.add(self.name)
        bound = instance.__dict__.get("_extents", {}).get(self.name)
        if bound is not None:
            return bound
        return getattr(instance, self.field.name)

    def __repr__(self) -> str:
        return f"Extent({self.field!r})"


class Value(_Value):
    """A value the array reads: a per-call one when a graph binds it, else
    written once per build, before the first DMA.

    ``derive`` gives the once-per-build value from the operator (a trip count
    from the extents); a graph binding a handle to it makes it per-call
    instead, lowered as a :class:`Scratchpad` value is. ``address``/``lock``
    place it for an image IRON did not build.
    """

    kind = "scratchpad"

    def __init__(
        self,
        dtype: Any = np.int32,
        *,
        derive: Callable[[Any], Any] | None = None,
        address: int | None = None,
        lock: int | None = None,
        optional: bool = False,
    ) -> None:
        if np.dtype(dtype).kind == "f":
            raise DeclarationError(
                "a Value cannot be floating point (the scratchpad encoding)"
            )
        super().__init__(dtype)
        self.derive = derive
        self.address = address
        self.lock = lock
        self.optional = optional

    def __repr__(self) -> str:
        return f"Value({np.dtype(self.dtype).name})"
