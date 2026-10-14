# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A declared shape: the dimensions an operand's host shape, tile or lanes name."""

from __future__ import annotations

from dataclasses import Field, dataclass
from typing import Any

import numpy as np

from .field import Auto, Param


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
        if isinstance(flag, Param):
            flag = getattr(op, flag.name)
            if flag is None:
                raise ValueError(
                    f"{self.flag!r} is None; a Select() on it needs a resolved operator"
                )
        return Shape(tuple(self.when_true if flag else self.when_false))


_DimSpec = Any  # Param | int | Select


@dataclass(frozen=True)
class Shape:
    """A declared shape: integers, ``Param`` fields and ``Select``s: a
    member's declared shape, or a stream's ``per=``.

    A ``Param`` field annotated ``T | None`` is a dimension present only
    where it resolves to something other than None (``In(num_batches, M, K)``
    is ``(M, K)`` when ``num_batches`` is None and ``(num_batches, M, K)``
    otherwise); inference tells the two ranks apart, so a shape has at most
    one such field.
    """

    dims: tuple

    def __str__(self) -> str:
        return ", ".join(repr(d) for d in self.dims)

    def check(self, cls: type, member: Any, what: str, *, allow_tunable: bool) -> None:
        """Check each dimension is a ``Param()`` field of ``cls`` or an
        integer, or with ``allow_tunable`` (a stream's tile) also an ``Auto()``.

        Raises:
            TypeError: A dimension breaks the rule.
        """
        for d in self.dims:
            if isinstance(d, Select):
                Shape(d.when_true + d.when_false).check(
                    cls, member, what, allow_tunable=allow_tunable
                )
            elif isinstance(d, bool):
                raise TypeError(f"{cls.__name__}.{member.name}: {d!r} is not a {what}")
            elif isinstance(d, Field):
                if not any(
                    vars(b).get("__dataclass_fields__", {}).get(d.name) is d
                    for b in cls.__mro__
                ):
                    raise TypeError(
                        f"{cls.__name__}: a shape references a field object that "
                        f"is not one of this class's fields"
                    )
                if not isinstance(d, Param) or (
                    isinstance(d, Auto) and not allow_tunable
                ):
                    why = (
                        "an Auto(); a host shape may not depend on tuning"
                        if isinstance(d, Auto)
                        else "not declared with Param()"
                    )
                    raise TypeError(
                        f"{cls.__name__}.{member.name}: {what} {d!r} is {why}. A "
                        f"shape dimension is a Param() field or an integer literal"
                    )
            elif not isinstance(d, (int, np.integer)):
                raise TypeError(
                    f"{cls.__name__}.{member.name}: {what} {d!r} is not a Param() "
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
        if isinstance(spec, Param):
            value = getattr(op, spec.name)
            if value is None:
                raise ValueError(
                    f"{spec!r} is None; it must be set before the shape can be resolved"
                )
            return int(value)
        raise TypeError(f"cannot resolve {spec!r} as a dimension")

    def resolve(self, op) -> tuple[int, ...]:
        """The shape on ``op``: a ``None``-valued ``Param`` dimension left
        out, each ``Select`` the branch its flag picks.
        """
        out: list[int] = []
        for d in self.dims:
            if isinstance(d, Param) and getattr(op, d.name) is None:
                continue
            if isinstance(d, Select):
                out.extend(d.branch(op).resolve(op))
            else:
                out.append(Shape.dim(d, op))
        return tuple(out)

    def axis_of(self, field: str, op) -> int | None:
        """The axis of the resolved shape that ``field`` sizes, or None."""
        axis = 0
        for d in self.dims:
            if isinstance(d, Param) and getattr(op, d.name) is None:
                continue
            if isinstance(d, Select):
                branch = d.branch(op)
                inner = branch.axis_of(field, op)
                if inner is not None:
                    return axis + inner
                axis += len(branch.resolve(op))
                continue
            if isinstance(d, Param) and d.name == field:
                return axis
            axis += 1
        return None

    def names(self) -> set[str]:
        """The fields this shape names, through ``Select``."""
        out: set[str] = set()
        for d in self.dims:
            if isinstance(d, Param):
                out.add(d.name)
            elif isinstance(d, Select):
                out |= Shape((d.flag, *d.when_true, *d.when_false)).names()
        return out
