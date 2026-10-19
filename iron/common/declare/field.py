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

# The key of a field's ``ParamSpec`` in its metadata.
SPEC = "iron"


class Unresolvable(ValueError):
    """No legal resolution exists for this operator on this device."""


@dataclasses.dataclass(frozen=True, kw_only=True)
class ParamSpec:
    """What a ``field()`` field declares beyond its dataclass field.

    Attributes:
        derive: The function computing the field's default, or None.
        held: A value given for the field must be what `derive` computes.
        probe: The value the tuner measures the field at, or ``MISSING``.
        array: The operator's ``Array`` reads the field though no stream
            names it.
    """

    derive: Callable[[Any], Any] | None
    held: bool
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
            takes (``Auto(default=...)``), or None when ``resolve`` must
            fill the field.
        domain: The values a tuner searches the field over, or None.
    """

    default: Any
    domain: Any


def field(
    *,
    default: Any = MISSING,
    derive: Callable[[Any], Any] | None = None,
    held: bool = True,
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
        default: The value when neither the caller nor an operand gives
            one: ``field(default=64)``. Without `default` or `derive`, the field is
            a required constructor argument.
        derive: A function of the operator computing the field when
            neither the caller nor an operand gives it, called once the
            computed fields declared before it are set
            (``derive=lambda op: op.rows * op.repeat``). `default` and
            `derive` are exclusive.
        held: A value the caller or an operand gives for a `derive` field
            must be what it computes, or ``ValueError`` is raised; with
            ``held=False`` the given value overrides it.
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
        TypeError: Both `default` and `derive` are given, or `held=False`
            without `derive`.
    """
    if derive is not None and default is not MISSING:
        raise TypeError("field(default=, derive=): give one, not both")
    if not held and derive is None:
        raise TypeError("field(held=False): only a derive= field is held")
    return dataclasses.field(
        default=None if derive is not None else default,
        init=init,
        repr=repr,
        kw_only=True,
        metadata={
            SPEC: ParamSpec(
                derive=derive,
                held=held and derive is not None,
                probe=probe,
                array=array,
            )
        },
    )


def Auto(
    *,
    default: Any = None,
    domain: Any = None,
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
        domain: The values a tuner searches the field over: a tuple, an
            `Enum` class, or a function ``(op, dev, start) -> tuple`` such
            as mlir-aie's ``widths``. Left out, it is not searched.
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
                held=False,
                probe=MISSING,
                array=array,
                default=default,
                domain=domain,
            ),
        },
    )
