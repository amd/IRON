# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an operator declares besides its fields: the ``Member`` base, and the
scalar values no operand carries.
"""

from __future__ import annotations

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

from .field import _DimSpec

if TYPE_CHECKING:
    from typing import Self

    # Named in the subclasses' base expressions as strings (bound imports member).
    from .bound import BoundValue


B = TypeVar("B")  # the bound form an instance serves


class Member(Generic[B]):
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
            if self.when is not None and not self.when.of(instance):
                raise AttributeError(
                    f"{type(instance).__name__}.{self.name} is declared when="
                    f"{self.when.name}, which is False on this instance"
                ) from None
            raise AttributeError(
                f"{type(instance).__name__}.{self.name} is not bound yet"
            ) from None

    def present(self, flags: Mapping[str, Any]) -> bool:
        """Whether this member exists under ``flags``; a flag left out is its default."""
        when = self.when
        return when is None or bool(flags.get(when.name, when.default))


class ValueSpec:
    """``Scratchpad[np.int32]``: the annotation of a graph body's per-call parameter."""

    __slots__ = ("kind", "dtype", "carried")

    def __init__(self, kind: str, dtype: Any, carried: bool = False) -> None:
        self.kind, self.dtype, self.carried = kind, dtype, carried

    def __repr__(self) -> str:
        text = f"{self.kind}[{np.dtype(self.dtype).name}]"
        return f"carried {text}" if self.carried else text


class _Value(Member["BoundValue"]):
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
