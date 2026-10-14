# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The fields an operator declares.

A compile-time parameter is a dataclass field declared with ``Param``, a
tunable the library resolves one declared with ``Auto(Param)``. Each is its
own dimension reference: ``GEMV.K`` in a shape names the field, while
``op.K`` on an instance is the integer.
"""

from __future__ import annotations

import dataclasses
from dataclasses import MISSING
from typing import Any, Callable

from .domain import Domain


class Unresolvable(ValueError):
    """No legal resolution exists for this operator on this device."""


class Param(dataclasses.Field):
    """A compile-time parameter: given by the caller or inferred from the
    operands.

    A field named in an operand's ``obj_type=``/``per=``/``depth=``, or marked
    ``array=True``, configures the array; any other rebuilds only the
    instruction stream.

    Args:
        default: The value. Without one, and without `derive`, the field is
            a required constructor argument.
        derive: A callable of the operator computing the field when neither
            the caller nor an operand gives it
            (``derive=lambda op: op.rows * op.repeat``); a value the caller
            gives must agree with it. `default` and `derive` are exclusive.
        array: The array reads the field though no obj_type= names it.
        probe: The field reaches the device only as the words of `Value`s
            the cores read: no transfer, trip count, branch or core follows
            it, so every value of it costs the same. The tuner measures the
            operator at `probe` and takes that cost for every value. Pick
            the value that leaves the output most informative (the
            identity), since a setting judged exact there is taken as exact
            at every value. `None` is a probe like any other.
    """

    __slots__ = ("array", "derive", "probe")

    def __init__(
        self,
        *,
        default: Any = MISSING,
        derive: Callable[[Any], Any] | None = None,
        array: bool = False,
        repr: bool = True,
        init: bool = True,
        probe: Any = MISSING,
    ) -> None:
        if derive is not None and default is not MISSING:
            raise TypeError("Param(default=, derive=): give one, not both")
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

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        # An init=False field is read through the class, where the field is.
        if self.default is not MISSING:
            return self.default
        raise AttributeError(self.name)

    def __repr__(self) -> str:
        return self.name or "<field>"


class Auto(Param):
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
        domain: The values a tuner searches the field over: a `Width`, a
            `Divisors`, a fixed tuple, or (left out, on an `Enum`-annotated
            field) that `Enum`'s members. Left out otherwise, a tunable a
            streamed ``per=`` names is searched as a `Width` and any other
            is not searched.
    """

    __slots__ = ("derived", "domain")

    def __init__(
        self,
        *,
        default: Any = None,
        array: bool = False,
        derived: bool = False,
        domain: Domain | tuple[Any, ...] | None = None,
        repr: bool = True,
        init: bool = True,
    ) -> None:
        super().__init__(array=array, repr=repr, init=init)
        # Always a value, never a derive: a tunable may default to a dtype.
        self.default = default
        self.derived = derived
        self.domain = domain
