# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How an operator declares the shapes it is tested at on a device.

``iron/tests/operators/catalog.py`` runs every declaration against the
operator's ``reference()``. Nothing here imports pytest, so an operator
module stays importable without it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Iterable

from aie.iron.device import Device
from aie.utils.verify import Tolerance

__all__ = ["Case", "Sweep", "Testing"]


@dataclass(frozen=True)
class Case:
    """One construction of an operator.

    Attributes:
        kwargs: The constructor's keywords.
        extensive: Keeps the case out of the default suite.
        id: Its name in test output, else the arguments.
        bench: CI tracks it over time (``pytest.mark.bench``).
    """

    kwargs: dict = field(default_factory=dict)
    extensive: bool = False
    id: str | None = None
    bench: bool = False

    @property
    def label(self) -> str:
        return self.id or "-".join(f"{k}_{v}" for k, v in self.kwargs.items())


_Cases = Callable[[type, Device], Iterable[Case | dict]]


@dataclass(frozen=True)
class Testing:
    """How an operator is checked against its reference on a device.

    Attributes:
        cases: ``Case``s, keyword dicts, or callables of the class and the
            device returning them (a ``Sweep``).
        tolerance: The gate, else the kernel's contract. A data mover states
            ``Tolerance.exact``: any other accepts a wrong permutation.
        draw: Extra ``vectors`` arguments, or a callable of the operator
            returning them, for inputs with preconditions.
    """

    __test__ = False  # pytest: a declaration, not a test class

    cases: Iterable[Case | dict | _Cases] | _Cases
    tolerance: Tolerance | None = None
    draw: dict[str, Any] | Callable[[Any], dict[str, Any]] | None = None

    def resolve(self, cls: type, dev: Device) -> list[Case]:
        """The cases for ``cls`` on ``dev``, so an inherited sweep reads the
        subclass's caps.
        """
        out = []
        for c in [self.cases] if callable(self.cases) else self.cases:
            items = c(cls, dev) if callable(c) else [c]
            out += [i if isinstance(i, Case) else Case(dict(i)) for i in items]
        return out


LENGTHS = (1024, 2048, 4096, 8192)

# Takes the widest grid most of a millisecond, several times the dispatch cost.
BENCH_ELEMENTS = 1 << 23
BENCH_TILE = 4096


class Sweep:
    """The cases of an elementwise operator: every column count its shim
    budget allows by every channel count, at each length.

    Args:
        channels: None leaves the count to the operator (a binary one).
        tile_cap: Else the class's ``tile_cap``.
        regular: The one length in the default suite; None for all.
        rows: A length is that many elements in rows of ``tile_size``
            (a ``Rowwise`` operator).
        bench: The length of one CI-tracked case at the widest grid; None
            adds none.
        **extra: Given to every case.
    """

    def __init__(
        self,
        lengths: Iterable[int] = LENGTHS,
        *,
        channels: Iterable[int] | None = (1, 2),
        tile_cap: int | None = None,
        regular: int | None = 2048,
        rows: bool = False,
        bench: int | None = BENCH_ELEMENTS,
        **extra,
    ):
        self.lengths = tuple(lengths)
        self.bench = bench
        self.channels = None if channels is None else tuple(channels)
        self.tile_cap = tile_cap
        self.regular = regular
        self.rows = rows
        self.extra = extra

    def _kwargs(self, length: int, cols: int, chans: int, tile: int) -> dict:
        kwargs = dict(rows=length // tile) if self.rows else dict(size=length)
        kwargs["num_aie_columns"] = cols
        if self.channels is not None:
            kwargs["num_channels"] = chans
        kwargs.update(tile_size=tile, **self.extra)
        return kwargs

    def __call__(self, cls, dev: Device) -> list[Case]:
        cap = cls.tile_cap if self.tile_cap is None else self.tile_cap
        out = []
        for length in self.lengths:
            for chans in self.channels or (1,):
                for cols in range(1, cls.shim_columns(dev, chans, self.extra) + 1):
                    cores = cols * chans
                    tile = min(length // cores, cap)
                    if tile * cores != length:
                        continue
                    out.append(
                        Case(
                            self._kwargs(length, cols, chans, tile),
                            extensive=length != self.regular,
                        )
                    )
        if self.bench is not None:
            chans = max(self.channels or (1,))
            tile = min(BENCH_TILE, cap)
            cols = next(
                c
                for c in range(cls.shim_columns(dev, chans, self.extra), 0, -1)
                if self.bench % (c * chans * tile) == 0
            )
            out.append(
                Case(
                    self._kwargs(self.bench, cols, chans, tile),
                    bench=True,
                )
            )
        return out
