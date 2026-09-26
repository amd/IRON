# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How an operator declares the shapes it is tested at.

An operator knows its own valid shapes: which column counts divide its
size, how large a line its kernel holds, which layout flags change what is
built. So it declares them beside itself, as :class:`Testing` on the class,
and ``iron/operators/test.py`` runs every declaration against the
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

from aie.utils.verify import Tolerance

from .device import bound_device

__all__ = [
    "Case",
    "Testing",
    "binary_elementwise_cases",
    "channeled_unary_cases",
    "device_columns",
]


def device_columns() -> int:
    """The bound device's width, for a declaration that sweeps it."""
    return bound_device().cols


@dataclass(frozen=True)
class Case:
    """One construction of an operator, and whether the default suite runs it.

    ``kwargs`` are the constructor's; ``extensive`` keeps a case out of the
    default run (``-m "not extensive"``); ``id`` names it in test output,
    defaulting to the arguments.
    """

    kwargs: dict = field(default_factory=dict)
    extensive: bool = False
    id: str | None = None

    @property
    def label(self) -> str:
        return self.id or "-".join(f"{k}_{v}" for k, v in self.kwargs.items())


@dataclass(frozen=True)
class Testing:
    """How an operator is checked against its reference on a device.

    ``cases`` lists what to construct: :class:`Case` objects or plain
    keyword dicts, or a callable of the operator class returning them, for
    an operator whose shapes follow the device's width. ``draw`` is extra
    :func:`iron.common.harness.vectors` arguments, or a callable of the
    operator returning them (for an input that must satisfy the kernel's
    preconditions: a packed quantization, an angle table).

    ``tolerance`` is the gate. Left out, it is the contract of the kernel
    the operator runs (:meth:`~iron.common.declare.Operator.reference_tolerance`),
    and an operator whose kernel declares none must state one here. An
    operator that only moves data states :meth:`Tolerance.exact`, since any
    other tolerance there also accepts a wrong permutation.
    """

    cases: Iterable[Case | dict] | Callable[[type], Iterable[Case | dict]]
    tolerance: Tolerance | None = None
    draw: dict[str, Any] | Callable[[Any], dict[str, Any]] | None = None

    def resolve(self, cls: type) -> list[Case]:
        """The cases for ``cls``: the callable form is called with the class,
        so a sweep inherited from a base reads the subclass's caps and shim
        budget; dicts are wrapped.
        """
        cases = self.cases(cls) if callable(self.cases) else self.cases
        return [c if isinstance(c, Case) else Case(dict(c)) for c in cases]


LENGTHS = (1024, 2048, 4096, 8192)


def channeled_unary_cases(
    input_lengths=LENGTHS,
    tile_cap=None,
    channels=(1, 2),
    regular: int | None = 2048,
    tile_floor=1,
    **extra,
):
    """Cases for a channeled unary operator, resolved against the device.

    Every column count the class's shim budget allows by every channel
    count, at each length, with the tile capped at what one core holds
    (the class's ``tile_cap`` unless given); only the ``regular`` length is
    in the default suite, every one when it is ``None``. ``tile_floor``
    drops the splits that leave a core a shorter line than its kernel
    takes. ``channels=None`` leaves the channel count out, for an operator
    without one. Returned as a callable of the class: the sweep needs the
    device, which is not bound when a class body runs.
    """

    def cases(cls):
        dev = bound_device()
        cap = cls.tile_cap if tile_cap is None else tile_cap
        out = []
        for length in input_lengths:
            for chans in [1] if channels is None else channels:
                for cols in range(1, cls.shim_columns(dev, chans) + 1):
                    cores = cols * chans
                    tile = min(length // cores, cap)
                    if tile * cores != length or tile < tile_floor:
                        continue
                    kwargs = dict(size=length, num_aie_columns=cols)
                    if channels is not None:
                        kwargs["num_channels"] = chans
                    kwargs.update(tile_size=tile, **extra)
                    out.append(Case(kwargs, extensive=length != regular))
        return out

    return cases


def binary_elementwise_cases(
    input_lengths=LENGTHS, tile_cap=None, regular: int | None = 2048, **extra
):
    """Cases for a binary elementwise operator, as :func:`channeled_unary_cases`."""

    def cases(cls):
        dev = bound_device()
        cap = cls.tile_cap if tile_cap is None else tile_cap
        out = []
        for length in input_lengths:
            for cols in range(1, cls.shim_columns(dev) + 1):
                tile = min(length // cols, cap)
                if tile * cols != length:
                    continue
                out.append(
                    Case(
                        dict(
                            size=length, num_aie_columns=cols, tile_size=tile, **extra
                        ),
                        extensive=length != regular,
                    )
                )
        return out

    return cases
