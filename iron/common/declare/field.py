# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The fields an operator declares.

Each is annotated ``CompileTime[T]`` (aie.iron's marker) and declared with
``field``, a compile-time parameter, or ``Auto``, a tunable the library
resolves. Each returns the `dataclasses.Field` itself, with its
``ParamSpec`` in the field's metadata, and each field is its own dimension
reference: ``GEMV.K`` in a shape names
the field, while ``op.K`` on an instance is the integer.
"""

from __future__ import annotations

import dataclasses
from dataclasses import MISSING
from typing import Any, Callable

from .domain import Domain

# The key of a field's ``ParamSpec`` in its metadata.
SPEC = "iron"


class Unresolvable(ValueError):
    """No legal resolution exists for this operator on this device."""


@dataclasses.dataclass(frozen=True, kw_only=True)
class ParamSpec:
    """What a ``field()`` field declares beyond its dataclass field.

    Attributes:
        derive: The field's computing default, or None.
        probe: The value the tuner measures the field at, or ``MISSING``.
        array: The operator's ``Array`` reads the field though no stream
            names it.
    """

    derive: Callable[[Any], Any] | None
    probe: Any
    array: bool

    @staticmethod
    def of(field: object) -> ParamSpec | None:
        """The spec ``field`` was declared with, or None where it is not a
        field declared with ``field()`` or ``Auto()``.
        """
        if not isinstance(field, dataclasses.Field):
            return None
        spec = field.metadata.get(SPEC)
        return spec if isinstance(spec, ParamSpec) else None


@dataclasses.dataclass(frozen=True, kw_only=True)
class AutoSpec(ParamSpec):
    """What an ``Auto()`` field declares beyond its dataclass field.

    Attributes:
        default: The starting value a construction or a profile leaves open
            takes (``Auto(default)``), or None when ``resolve`` must
            fill the field.
        domain: The values a tuner searches the field over, or None.
    """

    default: Any
    domain: Domain | tuple[Any, ...] | None


def field(
    default: Any = MISSING,
    /,
    *,
    derive: Callable[[Any], Any] | None = None,
    repr: bool = True,
    init: bool = True,
    probe: Any = MISSING,
    array: bool = False,
) -> Any:
    """A compile-time parameter: given by the caller or inferred from the
    operands.

    A field the operator's ``Array`` reads configures the array; any other
    rebuilds only the instruction stream.

    Args:
        default: The value. Without one, and without `derive`, the field is
            a required constructor argument.
        derive: A callable of the operator computing the field when neither
            the caller nor an operand gives it
            (``derive=lambda op: op.rows * op.repeat``). A value the caller
            gives overrides it, unless the operator's ``validate()`` holds
            the field to it with ``check_derived``. `default` and `derive`
            are exclusive.
        repr: The field is in the operator's repr.
        init: The field is a constructor argument.
        probe: The field reaches the device only as the words of `Value`s
            the cores read: no transfer, trip count, branch or core follows
            it, so every value of it costs the same. The tuner measures the
            operator at `probe` and takes that cost for every value. Pick
            the value that leaves the output most informative (the
            identity), since a setting judged exact there is taken as exact
            at every value. `None` is a probe like any other.
        array: The operator's ``Array`` reads the field (a scalar its
            kernel takes, a flag its build branches on), though no stream's
            tile, lanes, dtype or presence names it.

    Returns:
        The field.

    Raises:
        TypeError: Both `default` and `derive` are given.
    """
    if derive is not None and default is not MISSING:
        raise TypeError("field(default, derive=): give one, not both")
    return dataclasses.field(
        default=None if derive is not None else default,
        init=init,
        repr=repr,
        kw_only=True,
        metadata={SPEC: ParamSpec(derive=derive, probe=probe, array=array)},
    )


def Auto(
    default: Any = None,
    /,
    *,
    domain: Domain | tuple[Any, ...] | None = None,
    repr: bool = True,
    init: bool = True,
    array: bool = False,
) -> Any:
    """A tunable ``Operator.resolve`` fills for the device when the caller
    does not.

    Annotate it ``CompileTime[T]``, ``T`` the resolved type. It may name a
    stream tile but never a host shape, since inference would cycle through
    resolution.
    ``init=False`` makes it no tunable: a subclass's fixed value of an
    inherited one (its `default`), or one ``resolve`` computes from the device
    and the other fields, giving it to the copy it returns
    (``self.replace(x=...)``).

    Args:
        default: The starting value; `None` means `resolve` must fill it.
            Kept in the field's ``AutoSpec``, not the dataclass's own default
            (always ``None``, whatever is given): a caller leaving the
            tunable open must still read as "nothing given" in
            ``Operator.__post_init__``, before it fills this in.
        domain: The values a tuner searches the field over: a `Width`, a
            `Divisors`, a fixed tuple, or (left out, on an `Enum`-annotated
            field) that `Enum`'s members. Left out otherwise, a tunable a
            streamed ``per=`` names is searched as a `Width` and any other
            is not searched.
        repr: The field is in the operator's repr.
        init: The field is a constructor argument.
        array: As ``field``'s.

    Returns:
        The field.
    """
    return dataclasses.field(
        default=None,
        init=init,
        repr=repr,
        kw_only=True,
        metadata={
            SPEC: AutoSpec(
                derive=None,
                probe=MISSING,
                array=array,
                default=default,
                domain=domain,
            ),
        },
    )
