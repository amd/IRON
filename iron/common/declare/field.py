# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The fields an operator declares and the references a class body writes.

A compile-time parameter is a dataclass field declared with ``Param``, a
tunable the library resolves one declared with ``Auto``; both are
``dataclasses.Field``s. Naming either in a shape expression yields a
``DimRef``, which class creation resolves against the class it lands on.
"""

from __future__ import annotations

import dataclasses
from dataclasses import MISSING
from typing import Any

from .domain import Domain


class Unresolvable(ValueError):
    """No legal resolution exists for this operator on this device."""


class Param(dataclasses.Field):
    """A compile-time parameter: given by the caller or inferred from the
    operands.

    A field named in an operand's ``tile=``/``per=``/``depth=``, or marked
    ``array=True``, configures the array; any other rebuilds only the
    instruction stream.

    Args:
        default: The value, or a callable of the operator computing it when
            neither the caller nor an operand gives it
            (``default=lambda op: op.rows * op.repeat``). Without one the
            field is a required constructor argument.
        array: The array reads the field though no tile names it.
        probe: The field reaches the device only as the words of `Value`s
            the cores read: no transfer, trip count, branch or core follows
            it, so every value of it costs the same. The tuner measures the
            operator at `probe` and takes that cost for every value. Pick
            the value that leaves the output most informative (the
            identity), since a setting judged exact there is taken as exact
            at every value. `None` is a probe like any other.

    Attributes:
        derive: The callable `default`, or None.
    """

    __slots__ = ("array", "derive", "probe")

    def __init__(
        self,
        *,
        default: Any = MISSING,
        array: bool = False,
        repr: bool = True,
        init: bool = True,
        probe: Any = MISSING,
    ) -> None:
        derive = default if callable(default) else None
        super().__init__(
            default=None if derive is not None else default,
            default_factory=MISSING,
            init=init,
            repr=repr,
            hash=None,
            compare=True,
            metadata=None,
            kw_only=MISSING,
        )
        self.array = array
        self.derive = derive
        self.probe = probe


class Auto(dataclasses.Field):
    """A tunable ``Operator.resolve`` fills for the device when the caller
    does not.

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

    __slots__ = ("array", "derived", "domain")

    def __init__(
        self,
        default: Any = None,
        /,
        *,
        array: bool = False,
        derived: bool = False,
        domain: Domain | None = None,
        repr: bool = True,
        init: bool = True,
    ) -> None:
        super().__init__(
            default=default,
            default_factory=MISSING,
            init=init,
            repr=repr,
            hash=None,
            compare=True,
            metadata=None,
            kw_only=MISSING,
        )
        self.array = array
        self.derived = derived
        self.domain = domain


class DimRef:
    """A field of a declared class: ``GEMV.K`` names the dimension, while
    ``op.K`` on an instance is the integer.
    """

    __slots__ = ("owner", "field")

    def __init__(self, owner: type, field: dataclasses.Field) -> None:
        self.owner = owner
        self.field = field

    @property
    def name(self) -> str:
        return self.field.name

    @property
    def default(self) -> Any:
        return self.field.default

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
