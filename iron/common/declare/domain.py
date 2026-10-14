# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The values a tuner tries for a tunable, declared with ``Auto(domain=)``.

Each kind is asked of the resolved operator, so its ladder runs through the
value the library would choose and the default is always among them. A
value the operator cannot resolve or build at is left out by the tuner, not
here.

A domain need not be one of the classes below: a plain tuple is a fixed set
of values (the resolved one included, first if it is not already there),
and an ``Auto`` field annotated with an ``Enum`` and given no domain is
searched over that ``Enum``'s members, the resolved one first.
"""

from __future__ import annotations

import dataclasses
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable

# An integer, or what a callable of the resolved operator and its device returns.
Bound = int | Callable[[Any, Any], int] | None


@dataclass(frozen=True)
class Domain(ABC):
    """The values a tunable is searched over.

    Attributes:
        when: A callable of the resolved operator and its device; the
            tunable is searched only where it returns true.
    """

    when: Callable[[Any, Any], bool] | None = dataclasses.field(
        default=None, kw_only=True
    )

    @abstractmethod
    def values(self, op: Any, dev: Any, start: Any) -> tuple[Any, ...]:
        """The values to try for a tunable, `start` among them.

        Args:
            op: The resolved operator.
            dev: The device it is resolved against.
            start: The tunable's resolved value.
        """


@dataclass(frozen=True)
class Width(Domain):
    """A count of columns, channels or cores: the field's own value and
    every power of two up to the device's columns, widest first. A tunable
    a streamed ``per=`` names and that declares no domain is a width.
    """

    def values(self, op: Any, dev: Any, start: Any) -> tuple[Any, ...]:
        powers = {1 << i for i in range(dev.cols.bit_length())}
        return tuple(sorted({start, *powers}, reverse=True))


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

    def values(self, op: Any, dev: Any, start: Any) -> tuple[Any, ...]:
        of = self.of(op, dev) if callable(self.of) else self.of
        step = self.step(op, dev) if callable(self.step) else self.step
        cap = self.cap(op, dev) if callable(self.cap) else self.cap
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
