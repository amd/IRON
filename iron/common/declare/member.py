# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an operator declares besides its fields.

Buffers are the host ABI, and an operand declared with a tile is its own
stream into the array, so direction, dtype and shim binding agree by
construction. The other members are values no host buffer carries: a
``Value`` written once per build, or per call when a graph binds it,
and a ``Scratchpad`` or ``DispatchTime`` written per call.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Generic,
    Mapping,
    TypeVar,
    overload,
)

import numpy as np
from ml_dtypes import bfloat16

from .field import Shape, _DimSpec

if TYPE_CHECKING:
    from typing import Self

    # Named in the subclasses' base expressions as strings (bound imports member).
    from .bound import BoundBuffer, BoundValue


B = TypeVar("B")  # the bound form an instance serves


@dataclass(frozen=True)
class Shim:
    """A pinned shim endpoint: column and DMA channel on row 0."""

    col: int
    channel: int | None = None


class Direction(Enum):
    """Which way a buffer moves between the host and the array."""

    IN = "in"
    OUT = "out"
    INOUT = "inout"

    @property
    def fills(self) -> bool:
        """The host fills it: an input of a call."""
        return self is not Direction.OUT

    @property
    def drains(self) -> bool:
        """The host reads it back: an output of a call, its stream leaving the array."""
        return self is not Direction.IN


class _Member(Generic[B]):
    """Base of everything declared unannotated in an Operator body.

    ``__set_name__`` gives the member its name and the class body gives it
    its order. On an instance, ``__get__`` returns the bound form built as
    the class is created (a ``BoundBuffer`` or ``BoundValue``). ``B`` is
    that type, so a type checker sees ``op.A`` as it.
    """

    name: str = ""
    owner: type | None = None
    # The flag an optional operand is declared when=; None for a member
    # every instance has.
    when: _DimSpec | None = None

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
            if self.when is not None and not getattr(instance, self.when.name, True):
                raise AttributeError(
                    f"{type(instance).__name__}.{self.name} is declared when="
                    f"{self.when.name}, which is False on this instance"
                ) from None
            raise AttributeError(
                f"{type(instance).__name__}.{self.name} is not bound yet"
            ) from None


class _Buffer(_Member["BoundBuffer"]):
    """A host buffer: shape in extents, a dtype, and the stream it moves through.

    With ``tile=`` the buffer is its own stream into (or out of) the array:
    ``tile`` is what one fifo element holds, in the units a core reads
    (its dimensions may be tunables), ``per=`` the field the stream is
    replicated over (one fifo per column, say), or a tuple of fields whose
    product is the count (columns x channels), ``depth`` the fifo depth,
    ``via=`` a pinned shim endpoint. ``broadcast=True`` is one fifo every
    worker consumes; ``replicate=True`` gives every ``per=`` lane the whole
    buffer rather than a share of it. Without a tile the buffer is an
    argument of a sequence written by hand (``Operator.sequence``).

    ``when=`` a boolean ``param()`` makes the operand optional: it, and its
    stream, exist only on an instance where the field is true. A call gives
    it by keyword, its name (``RMSNorm(x, weight=w)``), which sets the field
    (see ``Operator.call_operands``).
    """

    direction: ClassVar[Direction]

    def __init__(
        self,
        *dims: _DimSpec,
        dtype: Any = bfloat16,
        tile: Any = None,
        per: _DimSpec | None = None,
        depth: int = 2,
        via: Shim | list[Shim] | None = None,
        replicate: bool = False,
        broadcast: bool = False,
        when: _DimSpec | None = None,
    ) -> None:
        if per is not None and broadcast:
            raise TypeError("a stream is either per=<dim> or broadcast, not both")
        if replicate and per is None:
            raise TypeError(
                "replicate=True needs per=<dim>: every slot receives the whole buffer"
            )
        self.shape = Shape(tuple(dims))
        self.dtype = dtype
        self.when = when
        self.tile = (
            None
            if tile is None
            else Shape(tuple(tile) if isinstance(tile, (tuple, list)) else (tile,))
        )
        self.per = (
            None if per is None else Shape(per if isinstance(per, tuple) else (per,))
        )
        self.depth = depth
        self.via = via
        self.replicate = replicate
        self.broadcast = broadcast

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.shape})"


class In(_Buffer):
    """A buffer the host fills and the array reads."""

    direction = Direction.IN


class Out(_Buffer):
    """A buffer the array writes and the host reads."""

    direction = Direction.OUT


class InOut(_Buffer):
    """A buffer the host fills and the array writes in place: its stream,
    with ``tile=``, leaves the array, and the sequence writes back only what
    it drains (a record of the tokens so far, say), leaving the rest as the
    host gave it. A call takes it as an input and returns it.
    """

    direction = Direction.INOUT


def present(member: _Member, flags: Mapping[str, Any]) -> bool:
    """Whether an operand (or its stream) exists under ``flags``, the field
    values an instance holds or a call gives; a ``when=`` flag left out
    reads as its default.
    """
    when = member.when
    return when is None or bool(flags.get(when.name, when.default))


class ValueSpec:
    """``Scratchpad[np.int32]``: the annotation of a graph body's per-call parameter.

    ``carried`` marks a value the graph computes for its own next call
    (``Carried``).
    """

    __slots__ = ("kind", "dtype", "carried")

    def __init__(self, kind: str, dtype: Any, carried: bool = False) -> None:
        self.kind, self.dtype, self.carried = kind, dtype, carried

    def __repr__(self) -> str:
        text = f"{self.kind}[{np.dtype(self.dtype).name}]"
        return f"carried {text}" if self.carried else text


class _Value(_Member["BoundValue"]):
    """A per-call scalar. See ``Scratchpad`` and ``DispatchTime``."""

    kind: ClassVar[str] = ""
    carried: ClassVar[bool] = False
    # A Value's own: how the host derives it once per build and where a
    # shipped image places it.
    derive: Callable[[Any], Any] | None = None
    address: int | None = None
    lock: int | None = None
    optional: bool = False

    def __init__(self, dtype: Any = np.int32) -> None:
        self.dtype = dtype

    def __class_getitem__(cls, dtype) -> ValueSpec:
        return ValueSpec(cls.kind, dtype, cls.carried)

    if TYPE_CHECKING:
        # A graph body's parameter annotated ``Scratchpad[T]`` is the graph's
        # per-call value (a number in its reference), on which integer
        # arithmetic is an expression the graph computes per call.
        def __add__(self, k: int) -> Any: ...
        def __sub__(self, k: int) -> Any: ...
        def __mul__(self, k: int) -> Any: ...
        def __radd__(self, k: int) -> Any: ...
        def __rmul__(self, k: int) -> Any: ...

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
            raise TypeError(
                "Scratchpad values cannot be floating point: the scratchpad "
                "encoding zeroes the top two bits of the value"
            )
        super().__init__(dtype)


class Carried(Scratchpad):
    """A scratchpad value a graph computes for its own next call.

    The graph's body returns the next value last, with
    ``iron.carry(name=...)``: an integer expression of its values
    (``position + 1``) or a one-element integer handle it computed (a
    sampled token). The host writes it only to seed the first call; after
    that each call's carry is the next's.
    """

    carried = True


class DispatchTime(_Value):
    """A per-call value the instruction stream is regenerated around.

    Can change DMA sizes, strides and offsets; costs a stream regeneration
    and a buffer allocation per call; cannot be packaged as a full ELF.
    """

    kind = "dispatch"


class Extent(_Value):
    """A shape field a graph may bound per call.

    ``valid = Extent(size)`` reads as ``size`` on an instance until a graph
    bounds an operand the field sizes (``x[:n]``); from then on it is per
    call, and so is every ``Value`` whose ``derive`` reads it, which the
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
        # The extents a derive reads, recorded on the copy Operator._per_call_derived probes.
        reads = instance.__dict__.get("_extent_reads")
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
    instead, lowered as a ``Scratchpad`` value is. ``address``/``lock``
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
            raise TypeError(
                "a Value cannot be floating point (the scratchpad encoding)"
            )
        super().__init__(dtype)
        self.derive = derive
        self.address = address
        self.lock = lock
        self.optional = optional

    def __repr__(self) -> str:
        return f"Value({np.dtype(self.dtype).name})"
