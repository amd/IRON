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

import numpy as np

from .domain import Domain


class Unresolvable(ValueError):
    """No legal resolution exists for this operator on this device."""


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
    """A tunable the library resolves for the device.

    Attributes:
        derived: `resolve` always computes the field from the others, so no
            caller, profile or tuner sets it.
        domain: The values a tuner searches it over, or None for a width's
            inferred one or none.
    """

    derived: bool = False
    domain: Domain | None = None


def param(
    *, default: Any = MISSING, array: bool = False, repr: bool = True, init: bool = True
) -> Any:
    """Declare a compile-time parameter: given by the caller or inferred from
    the operands.

    A field named in an operand's ``tile=``/``per=``/``depth=``, or marked
    ``array=True``, configures the array; any other rebuilds only the
    instruction stream.

    Args:
        default: The value, or a callable of the operator computing it when
            neither the caller nor an operand gives it
            (``default=lambda op: op.rows * op.repeat``). Without one the
            field is a required constructor argument.
        array: The array reads the field though no tile names it.
    """
    if callable(default):
        spec, default = Param(array, default), None
    else:
        spec = Param(array)
    return dataclasses.field(
        default=default, repr=repr, init=init, metadata={Tier: spec}
    )


def auto(
    default: Any = None,
    /,
    *,
    array: bool = False,
    derived: bool = False,
    domain: Domain | None = None,
    repr: bool = True,
    init: bool = True,
) -> Any:
    """Declare a tunable ``Operator.resolve`` fills for the device when the
    caller does not.

    Annotate it with the resolved type. It may name a stream tile but never
    a host shape, since inference would cycle through resolution.
    ``init=False`` fixes a subclass's value of an inherited tunable.

    Args:
        default: The starting value; `None` means `resolve` must fill it.
        array: The array reads the field though no tile names it.
        derived: `resolve` computes the field from the device and the other
            fields whatever it was given, so it is not a tunable a caller,
            a profile or a tuner sets.
        domain: The values a tuner searches the field over (`Width`,
            `Divisors`, `Choices`). Left out, a tunable a streamed ``per=``
            names is searched as a `Width` and any other is not searched.
    """
    return dataclasses.field(
        default=default,
        repr=repr,
        init=init,
        metadata={Tier: Auto(array, derived, domain)},
    )


class DimRef:
    """A ``param()`` or ``auto()`` field of a declared class: ``GEMV.K`` names
    the dimension, while ``op.K`` on an instance is the integer.
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
        # An init=False field reads the class attribute, which is now this object.
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

    def of(self, op) -> Any:
        """This field's value on ``op``, an instance of its class or a subclass."""
        if not isinstance(op, self.owner):
            raise TypeError(
                f"{self!r} is not reachable from {type(op).__name__}: a shape may "
                f"reference the class's own fields"
            )
        return getattr(op, self.name)


@dataclass(frozen=True)
class OptionalDim:
    """A dimension present only when greater than one.

    ``In(OptionalDim(num_batches), M, K)`` is ``(M, K)`` for one batch and
    ``(num_batches, M, K)`` otherwise. Inference tells them apart by rank, so
    a shape has at most one.
    """

    ref: Any


@dataclass(frozen=True)
class Select:
    """A shape chosen by a flag the caller gives or defaults, never inferred:
    ``Select(b_col_maj, (N, K), (K, N))``.
    """

    flag: Any
    when_true: tuple
    when_false: tuple

    def branch(self, op) -> Shape:
        """The shape the flag picks on ``op``."""
        flag = self.flag
        if isinstance(flag, DimRef):
            flag = flag.of(op)
            if flag is None:
                raise ValueError(
                    f"{self.flag!r} is None; a Select() on it needs a resolved operator"
                )
        return Shape(tuple(self.when_true if flag else self.when_false))


_DimSpec = Any  # Field (own class, pre-processing) | DimRef | int | OptionalDim


@dataclass(frozen=True)
class Shape:
    """A declared shape: integers, ``DimRef``s, at most one ``OptionalDim`` and
    ``Select``s: a member's declared shape, or a stream's ``per=``.
    """

    dims: tuple

    def __str__(self) -> str:
        return ", ".join(
            (d.name or "<field>") if isinstance(d, Field) else repr(d)
            for d in self.dims
        )

    def rewrite(self, cls: type) -> Shape:
        """This shape with each field the class body captured as ``cls``'s
        ``DimRef``.

        Raises:
            TypeError: A captured field is not one of ``cls``'s.
        """
        fields = {f.name: f for f in dataclasses.fields(cls)}
        out = []
        for d in self.dims:
            if isinstance(d, OptionalDim):
                d = OptionalDim(*Shape((d.ref,)).rewrite(cls).dims)
            elif isinstance(d, Select):
                d = Select(
                    *Shape((d.flag,)).rewrite(cls).dims,
                    Shape(d.when_true).rewrite(cls).dims,
                    Shape(d.when_false).rewrite(cls).dims,
                )
            elif isinstance(d, Field):
                if fields.get(d.name) is not d:
                    raise TypeError(
                        f"{cls.__name__}: a shape references a field object that "
                        f"is not one of this class's fields"
                    )
                d = getattr(cls, d.name)
            out.append(d)
        return Shape(tuple(out))

    def check(self, cls: type, member: Any, what: str, *, allow_tunable: bool) -> None:
        """Check each dimension is a ``param()`` field or an integer, or with
        ``allow_tunable`` (a stream's tile) also an ``auto()``.

        Raises:
            TypeError: A dimension breaks the rule.
        """
        for d in self.dims:
            if isinstance(d, OptionalDim):
                Shape((d.ref,)).check(cls, member, what, allow_tunable=allow_tunable)
            elif isinstance(d, Select):
                Shape(d.when_true + d.when_false).check(
                    cls, member, what, allow_tunable=allow_tunable
                )
            elif isinstance(d, bool):
                raise TypeError(f"{cls.__name__}.{member.name}: {d!r} is not a {what}")
            elif isinstance(d, DimRef):
                allowed = (Param, Auto) if allow_tunable else Param
                if not isinstance(d.tier, allowed):
                    why = (
                        "an auto(); a host shape may not depend on tuning"
                        if isinstance(d.tier, Auto)
                        else "not declared with param()"
                    )
                    raise TypeError(
                        f"{cls.__name__}.{member.name}: {what} {d!r} is {why}. A "
                        f"shape dimension is a param() field or an integer literal"
                    )
            elif not isinstance(d, (int, np.integer)):
                raise TypeError(
                    f"{cls.__name__}.{member.name}: {what} {d!r} is not a param() "
                    f"field or an integer. Expressions are not allowed in shapes; "
                    f"declare the result as a field"
                )

    @staticmethod
    def dim(spec, op) -> int:
        """One dimension's value on ``op``."""
        if isinstance(spec, bool):
            raise TypeError(f"{spec!r} is not a dimension")
        if isinstance(spec, (int, np.integer)):
            return int(spec)
        if isinstance(spec, DimRef):
            value = spec.of(op)
            if value is None:
                raise ValueError(
                    f"{spec!r} is None; it must be set before the shape can be resolved"
                )
            return int(value)
        raise TypeError(f"cannot resolve {spec!r} as a dimension")

    def resolve(self, op) -> tuple[int, ...]:
        """The shape on ``op``: an ``OptionalDim`` of one left out, each
        ``Select`` the branch its flag picks.
        """
        out: list[int] = []
        for d in self.dims:
            if isinstance(d, OptionalDim):
                if (n := Shape.dim(d.ref, op)) > 1:
                    out.append(n)
            elif isinstance(d, Select):
                out.extend(d.branch(op).resolve(op))
            else:
                out.append(Shape.dim(d, op))
        return tuple(out)

    def axis_of(self, field: str, op) -> int | None:
        """The axis of the resolved shape that ``field`` sizes, or None."""
        axis = 0
        for d in self.dims:
            if isinstance(d, OptionalDim):
                if Shape.dim(d.ref, op) <= 1:
                    continue
                d = d.ref
            if isinstance(d, Select):
                branch = d.branch(op)
                inner = branch.axis_of(field, op)
                if inner is not None:
                    return axis + inner
                axis += len(branch.resolve(op))
                continue
            if isinstance(d, DimRef) and d.name == field:
                return axis
            axis += 1
        return None

    def names(self) -> set[str]:
        """The fields this shape names, through ``OptionalDim`` and ``Select``."""
        out: set[str] = set()
        for d in self.dims:
            if isinstance(d, DimRef):
                out.add(d.name)
            elif isinstance(d, OptionalDim):
                out |= Shape((d.ref,)).names()
            elif isinstance(d, Select):
                out |= Shape((d.flag, *d.when_true, *d.when_false)).names()
        return out
