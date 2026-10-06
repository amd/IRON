# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Field specifiers and the dimension references a class body writes.

A compile-time parameter is a dataclass field declared with ``param``, a
tunable the library resolves one declared with ``auto``. Naming either in a
shape expression yields a ``DimRef``, which class creation resolves
against the class it lands on.
"""

from __future__ import annotations

import dataclasses
from dataclasses import MISSING, Field, dataclass
from typing import Any, Callable


class Unresolvable(ValueError):
    """No legal resolution exists for this operator on this device.

    An expected outcome, not a bug: raised by ``Operator.resolve`` so the
    caller learns at resolution rather than from a design that compiles and
    then hangs.
    """


@dataclass(frozen=True)
class Tier:
    """What a ``param()`` or ``auto()`` field declares, kept in its metadata
    under ``Tier``.

    Attributes:
        array: The array reads the field though no tile names it.
    """

    array: bool = False


@dataclass(frozen=True)
class Param(Tier):
    """A compile-time parameter.

    Attributes:
        derive: Computes the value from the operator when neither the caller
            nor an operand's shape gives it.
    """

    derive: Callable[[Any], Any] | None = None


@dataclass(frozen=True)
class Auto(Tier):
    """A tunable the library resolves for the device."""


def param(
    *, default: Any = MISSING, array: bool = False, repr: bool = True, init: bool = True
) -> Any:
    """Declare a compile-time parameter: given by the caller or inferred from
    the operands, and fixed from then on.

    A callable ``default`` is computed from the operator at construction,
    for a parameter its other fields determine when neither the caller nor
    an operand's shape gives it (``default=lambda op: op.rows * op.repeat``);
    ``Operator.check_derived`` checks that a value given as
    well agrees.

    A ``param()`` may appear in a shape. Its tier follows from use: a field
    named in an operand's ``tile=``/``per=``/``depth=`` configures the array,
    so changing it rebuilds the array; any other field rebuilds only the
    instruction stream, unless it is marked ``array=True`` because the array
    reads it though no tile names it (a kernel's epilogue). ``default`` is
    keyword-only so a type checker sees it; a ``param()`` without one is a
    required constructor argument.
    """
    if callable(default):
        spec, default = Param(array, default), None
    else:
        spec = Param(array)
    return dataclasses.field(
        default=default, repr=repr, init=init, metadata={Tier: spec}
    )


def auto(
    default: Any = None, /, *, array: bool = False, repr: bool = True, init: bool = True
) -> Any:
    """Declare a tunable the library resolves for the device when the caller
    does not: a compile-time value that starts at ``default`` (``None``:
    ``Operator.resolve`` must fill it) and that
    ``resolve`` may replace. Annotate it with the resolved type: the field
    is ``None`` only until resolution, and every hook after it sees the
    value.

    An ``auto()`` never appears in a host shape (inference would cycle
    through resolution); a stream tile may name one. ``init=False`` fixes a
    subclass's value of an inherited tunable (a kernel that only works with
    one channel per column).
    """
    return dataclasses.field(
        default=default, repr=repr, init=init, metadata={Tier: Auto(array)}
    )


# --------------------------------------------------------------------------
# Dimension references
# --------------------------------------------------------------------------


class DimRef:
    """A reference to a ``param()`` or ``auto()`` field of a declared class.

    As a class is created, each field is re-attached to the
    class as a ``DimRef``, so ``GEMV.K`` names the dimension from
    outside the class body while ``op.K`` on an instance is the integer. A
    non-data descriptor: instance attributes take precedence.
    """

    __slots__ = ("owner", "name", "tier", "default")

    def __init__(
        self, owner: type, name: str, tier: Tier | None, default=MISSING
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


@dataclass(frozen=True)
class OptionalDim:
    """A dimension that is present only when greater than one.

    ``In(OptionalDim(num_batches), M, K)`` declares ``(M, K)`` for a single
    batch and ``(num_batches, M, K)`` otherwise, the convention batched
    operators use for their host shapes; ``In(rows, OptionalDim(seq), cols)``
    takes a matrix or a stack of them. Inference reads the rank to tell the
    two apart, so a declaration has at most one.
    """

    ref: Any


@dataclass(frozen=True)
class Select:
    """A shape chosen by a flag: ``Select(b_col_maj, (N, K), (K, N))``.

    The flag is a field with a default or one the caller passes explicitly;
    it is never inferred. The only conditional shapes in the tree are GEMM's
    layout flags, which transpose a declared shape rather than resize it.
    """

    flag: Any
    when_true: tuple
    when_false: tuple


_DimSpec = Any  # Field (own class, pre-processing) | DimRef | int | OptionalDim


def _describe(spec) -> str:
    if isinstance(spec, Field):
        return spec.name if spec.name else "<field>"
    return repr(spec)
