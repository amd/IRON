# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How an operator declares the shapes it is tested at.

An operator knows its own valid shapes: which column counts divide its
size, how large a line its kernel holds, which layout flags change what is
built. So it declares them beside itself, as ``Testing`` on the class,
and ``iron/tests/operators/catalog.py`` runs every declaration against the
operator's ``reference()`` on a device.

``iron/tests/common/cases.py`` is a separate matrix: one small pinned case
per shape decision, constructed without a device and lowered by the
toolchain gate. The cases here run on the device and are sized to stress
it.

A declaration is data. Nothing here imports pytest or torch, so an
operator module stays importable without them; the runner turns the data
into parameters.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Iterable

from aie.iron.device import Device
from aie.utils.verify import Tolerance

__all__ = ["Case", "Sweep", "Testing"]


@dataclass(frozen=True)
class Case:
    """One construction of an operator, and whether the default suite runs it.

    ``kwargs`` are the constructor's; ``extensive`` keeps a case out of the
    default run (``-m "not extensive"``); ``bench`` marks it as a case CI
    tracks over time (``pytest.mark.bench``), which wants an input large
    enough that the dispatch cost does not dominate; ``id`` names it in test
    output, defaulting to the arguments.
    """

    kwargs: dict = field(default_factory=dict)
    extensive: bool = False
    id: str | None = None
    bench: bool = False

    @property
    def label(self) -> str:
        return self.id or "-".join(f"{k}_{v}" for k, v in self.kwargs.items())


# What a sweep is to Testing: the operator class and the device in, its cases out.
_Cases = Callable[[type, Device], Iterable[Case | dict]]


@dataclass(frozen=True)
class Testing:
    """How an operator is checked against its reference on a device.

    ``cases`` lists what to construct: ``Case`` objects, plain keyword
    dicts, and callables of the operator class and the device returning
    them (a ``Sweep``), for shapes that follow the device's width; or is
    one such callable. ``draw`` is extra
    ``iron.common.harness.vectors`` arguments, or a callable of the
    operator returning them (for an input that must satisfy the kernel's
    preconditions: a packed quantization, an angle table).

    ``tolerance`` is the gate. Left out, it is the contract of the kernel
    the operator runs (``Operator.tolerance``),
    and an operator whose kernel declares none must state one here. An
    operator that only moves data states ``Tolerance.exact``, since any
    other tolerance there also accepts a wrong permutation.
    """

    __test__ = False  # pytest: a declaration, not a test class

    cases: Iterable[Case | dict | _Cases] | _Cases
    tolerance: Tolerance | None = None
    draw: dict[str, Any] | Callable[[Any], dict[str, Any]] | None = None

    def resolve(self, cls: type, dev: Device) -> list[Case]:
        """The cases for ``cls`` on ``dev``: a callable is called with both,
        so a sweep inherited from a base reads the subclass's caps and shim
        budget; dicts are wrapped.
        """
        out = []
        for c in [self.cases] if callable(self.cases) else self.cases:
            items = c(cls, dev) if callable(c) else [c]
            out += [i if isinstance(i, Case) else Case(dict(i)) for i in items]
        return out


LENGTHS = (1024, 2048, 4096, 8192)

# The length of a sweep's bench case: 16 MiB of bf16 per operand, which takes
# the widest grid most of a millisecond, several times the dispatch cost.
BENCH_ELEMENTS = 1 << 23
# The line a bench case's cores each take, if the operator's cap allows.
BENCH_TILE = 4096


class Sweep:
    """The cases of an elementwise operator: every column count its shim
    budget allows by every channel count, at each length.

    Called with the operator class and the device, as ``Testing`` calls
    it, it reads the class's ``tile_cap`` (unless given one) and shim
    budget, so a sweep a base declares serves its subclasses; the device
    is given then, since none is bound when a class body runs. A case's
    tile is its length over its cores, at most the cap; only the
    ``regular`` length is in the
    default suite, every one when it is ``None``. ``channels=None`` leaves
    the channel count to the operator (a binary one, whose shim budget one
    channel fills). With ``rows``, a length is that many elements in rows
    of ``tile_size``, for a ``Rowwise``
    operator. ``extra`` is given to every case.

    ``bench`` adds one default-suite case of that many elements, marked for CI
    to track: the widest grid at the most channels, at a line of ``BENCH_TILE``
    or the cap. ``None`` adds none, for a sweep that only varies an argument
    another sweep of the same operator already benches.
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
            # The widest grid whose cores split the length evenly.
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
