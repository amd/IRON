# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The values a tuner tries for a tunable, declared with ``auto(domain=)``.

Each kind is asked of the resolved operator, so its ladder runs through the
value the library would choose and the default is always among them. A
value the operator cannot resolve or build at is left out by the tuner, not
here.
"""

from __future__ import annotations

import dataclasses
import inspect
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Union

Bound = Union[int, Callable[..., int], None]


def evaluate(bound: Any, op: Any, dev: Any) -> Any:
    """``bound`` itself, or what it returns when it is a callable of the
    operator, or of the operator and the device.

    Args:
        bound: A value, `op -> value` or `(op, dev) -> value`.
        op: The resolved operator.
        dev: The device it is resolved against.
    """
    if not callable(bound):
        return bound
    if len(inspect.signature(bound).parameters) == 2:
        return bound(op, dev)
    return bound(op)


@dataclass(frozen=True)
class Domain(ABC):
    """The values a tunable is searched over.

    Attributes:
        when: A bool field of the operator; the tunable is searched only
            where it is true.
    """

    when: str | None = dataclasses.field(default=None, kw_only=True)

    @abstractmethod
    def values(self, op: Any, dev: Any, name: str) -> tuple[Any, ...]:
        """The values to try for `name`, its resolved value among them.

        Args:
            op: The resolved operator.
            dev: The device it is resolved against.
            name: The tunable's field name.
        """


@dataclass(frozen=True)
class Width(Domain):
    """A count of columns, channels or cores: the field's own value and
    every power of two up to the device's columns, widest first. A tunable
    a streamed ``per=`` names and that declares no domain is a width.
    """

    def values(self, op: Any, dev: Any, name: str) -> tuple[Any, ...]:
        powers = {1 << i for i in range(dev.cols.bit_length())}
        return tuple(sorted({getattr(op, name), *powers}, reverse=True))


@dataclass(frozen=True)
class Divisors(Domain):
    """The resolved value times a power of two, largest first, for every
    such value that divides `of`, is a multiple of `step` and is at most
    `cap`.

    Attributes:
        of: What the value must divide.
        step: What the value must be a multiple of.
        cap: The largest value, or None for no cap.
        span: The most octaves to go either side of the resolved value, or
            None for as far as the bounds allow.
    """

    of: Bound
    step: Bound = 1
    cap: Bound = None
    span: int | None = None

    def values(self, op: Any, dev: Any, name: str) -> tuple[Any, ...]:
        start = getattr(op, name)
        of, step = evaluate(self.of, op, dev), evaluate(self.step, op, dev)
        cap = evaluate(self.cap, op, dev)
        found = [start]
        value, octave = start * 2, 1
        while (
            of % value == 0
            and (cap is None or value <= cap)
            and (self.span is None or octave <= self.span)
        ):
            found.insert(0, value)
            value, octave = value * 2, octave + 1
        value, octave = start, 1
        while (
            value % 2 == 0
            and (value // 2) % step == 0
            and (self.span is None or octave <= self.span)
        ):
            value, octave = value // 2, octave + 1
            if of % value == 0 and (cap is None or value <= cap):
                found.append(value)
        return tuple(found)


@dataclass(frozen=True)
class Choices(Domain):
    """A fixed set of values, the resolved one first if it is not among
    them.

    Attributes:
        options: The values, or a callable of the operator (or of the
            operator and the device) returning them.
    """

    options: Any

    def values(self, op: Any, dev: Any, name: str) -> tuple[Any, ...]:
        options = tuple(evaluate(self.options, op, dev))
        start = getattr(op, name)
        return options if start in options else (start, *options)
