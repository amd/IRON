# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an operator declares besides its fields: its buffers (the host ABI,
each with a tile its own stream) and the scalar values no buffer carries.
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
    NoReturn,
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
    """Base of everything declared unannotated in an Operator body; on an
    instance it reads as its bound form ``B``.
    """

    name: str = ""
    owner: type | None = None
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

    Args:
        dims: The host shape.
        dtype: The element type.
        tile: What one fifo element holds, in the units a core reads. With
            one the buffer is its own stream; without one it is an argument
            of a hand-written `Operator.sequence`.
        per: The field (or fields, multiplied) the stream is replicated over.
        depth: The fifo depth.
        via: A pinned shim endpoint.
        replicate: Every `per=` lane gets the whole buffer, not a share.
        broadcast: One fifo every worker consumes.
        when: A bool `param()`; the operand and its stream exist only where
            it is true, and a call giving the operand by keyword sets it.
        finish: The cores apply the operator's `finish` to each tile of
            this output before releasing it (`Finish`), so a consumer folds
            into them. `True`, or the block of the output one core fills
            of a tile, in an order of its own (GEMM's C, joined from a
            column's cores): a step there must not depend on the order.
        prepare: The cores apply the operator's `prepare` to each tile of
            this input after acquiring it (`Prepare`), so the step that
            produced it folds into them. The operator's output must be
            linear in it, which its tolerance relies on. Without a tile, a
            hand-written sequence carries it, a line its innermost
            dimension, and the prologue's inputs ride the `feed=True` input.
        feed: The finish's inputs ride this input's stream rather than
            streams of their own: after the tiles a core reads for one
            output tile, the next tile of this stream holds that output
            tile's input of each (`Finish.apply`), so the finish takes no
            input channel of the core's and no shim channel. An untiled
            prepared input's prologue inputs ride it too, a tile each,
            where the operator's cores take them (`Prepare.apply`).
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
        finish: bool | tuple[_DimSpec, ...] = False,
        prepare: bool = False,
        feed: bool = False,
    ) -> None:
        if per is not None and broadcast:
            raise TypeError("a stream is either per=<dim> or broadcast, not both")
        if replicate and per is None:
            raise TypeError(
                "replicate=True needs per=<dim>: every slot receives the whole buffer"
            )
        # A step over a line sees a tile as a run of the output's elements.
        if finish and (
            isinstance(tile, (tuple, list))
            and len(tile) != 1
            or tile is None
            or not self.direction.drains
        ):
            raise TypeError(
                "finish=True names a streamed output of one-dimensional tiles, "
                "which a core finishes"
            )
        if prepare and (
            isinstance(tile, (tuple, list))
            and len(tile) != 1
            or self.direction is not Direction.IN
        ):
            raise TypeError(
                "prepare=True names an input of one-dimensional tiles, or of "
                "none, which a core prepares"
            )
        if feed and (tile is None or self.direction is not Direction.IN):
            raise TypeError("feed=True names a streamed input, which a finish rides")
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
        self.finish = bool(finish)
        self.finish_block = None if isinstance(finish, bool) else Shape(finish)
        self.prepare = prepare
        self.feed = feed

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.shape})"


class In(_Buffer):
    """A buffer the host fills and the array reads."""

    direction = Direction.IN


class Out(_Buffer):
    """A buffer the array writes and the host reads."""

    direction = Direction.OUT


class InOut(_Buffer):
    """A buffer the host fills and the array writes in place; what the
    stream does not drain stays as the host gave it.
    """

    direction = Direction.INOUT


def present(member: _Member, flags: Mapping[str, Any]) -> bool:
    """Whether an operand exists under ``flags``; a flag left out is its default."""
    when = member.when
    return when is None or bool(flags.get(when.name, when.default))


class ValueSpec:
    """``Scratchpad[np.int32]``: the annotation of a graph body's per-call parameter."""

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
    derive: Callable[[Any], Any] | None = None
    address: int | None = None
    lock: int | None = None
    optional: bool = False

    def __init__(self, dtype: Any = np.int32) -> None:
        self.dtype = dtype

    def __class_getitem__(cls, dtype) -> ValueSpec:
        return ValueSpec(cls.kind, dtype, cls.carried)

    if TYPE_CHECKING:
        # Integer arithmetic on a graph body's per-call parameter.
        def __add__(self, k: int) -> Any: ...
        def __sub__(self, k: int) -> Any: ...
        def __mul__(self, k: int) -> Any: ...
        def __radd__(self, k: int) -> Any: ...
        def __rmul__(self, k: int) -> Any: ...
        def __rsub__(self, k: int) -> Any: ...
        def __neg__(self) -> Any: ...
        def __floordiv__(self, d: Any) -> Any: ...
        def __bool__(self) -> NoReturn: ...

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
        super().__init__(type(self)[dtype].dtype)

    def __class_getitem__(cls, dtype) -> ValueSpec:
        if np.dtype(dtype).kind == "f":
            raise TypeError(
                "Scratchpad values cannot be floating point: the scratchpad "
                "encoding zeroes the top two bits of the value"
            )
        return super().__class_getitem__(dtype)


class Carried(Scratchpad):
    """A scratchpad value a graph computes for its own next call, returned
    last with ``iron.carry(name=...)``: an integer expression of its values
    (``position + 1``) or a one-element handle (a sampled token). The host
    writes it only to seed the first call.
    """

    carried = True


class DispatchTime(_Value):
    """A per-call value the instruction stream is regenerated around.

    Can change DMA sizes, strides and offsets; costs a stream regeneration
    and a buffer allocation per call; cannot be packaged as a full ELF.
    """

    kind = "dispatch"


class Extent(_Value):
    """A ``param()`` shape field a graph may bound per call.

    ``valid = Extent(size)`` reads as ``size`` until a graph bounds an
    operand the field sizes (``x[:n]``); then it, and every ``Value`` whose
    ``derive`` reads it, is per call. The image is built for the full value.
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
    """A value the array reads: per call when a graph binds it, else written
    once per build before the first DMA.

    Args:
        dtype: An integer type.
        derive: The once-per-build value, from the operator.
        address: Where a shipped image reads it.
        lock: The lock a shipped image waits on for it.
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
