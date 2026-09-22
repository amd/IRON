# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How an operator declares the shapes it is tested at.

An operator knows its own valid shapes: which column counts divide its
size, how large a line its kernel holds, which layout flags change what is
built. So it declares them beside itself, as :class:`Testing` on the class,
and ``iron/operators/test.py`` runs every declaration against the
operator's ``reference()`` on a device. What that replaced was one test
module per operator, each a single call with the same body.

``iron/tests/common/cases.py`` is a different matrix and stays: one small
pinned case per shape decision, constructed device-free and lowered by the
toolchain gate. These cases are the device's, sized to stress it.

A declaration is data. Nothing here imports pytest or torch, so an
operator module stays importable without them; the runner turns the data
into parameters.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Iterable

import aie.utils as aie_utils

__all__ = [
    "Case",
    "Testing",
    "binary_elementwise_cases",
    "channeled_unary_cases",
    "device_columns",
]


def device_columns() -> int:
    """The bound device's width, for a declaration that sweeps it."""
    return aie_utils.get_current_device().cols


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

    ``cases`` is what to construct: :class:`Case` objects or plain keyword
    dicts, or a callable returning them, which is what an operator whose
    shapes follow the device's width declares. ``draw`` is extra
    :func:`iron.common.harness.vectors` arguments, or a callable of the
    operator returning them (an input that must satisfy the kernel's
    preconditions: a packed quantization, an angle table). The tolerances
    are the gate: an operator that only moves data sets both to zero, since
    any tolerance there also accepts a wrong permutation.
    """

    cases: Iterable[Case | dict] | Callable[[], Iterable[Case | dict]]
    rel_tol: float = 0.04
    abs_tol: float = 1e-6
    max_error_rate: float = 0.0
    draw: Any = None

    def resolve(self) -> list[Case]:
        """The cases, with the callable form called and dicts wrapped."""
        cases = self.cases() if callable(self.cases) else self.cases
        return [c if isinstance(c, Case) else Case(dict(c)) for c in cases]


def channeled_unary_cases(
    input_lengths, tile_cap, channels=(1, 2), regular=2048, **extra
):
    """Cases for a channeled unary operator, resolved against the device.

    Every column count the device has by every channel count, at each
    length, with the tile capped at what one core holds; only the
    ``regular`` length is in the default suite. ``channels=None`` leaves the
    channel count out, for an operator without one. Returned as a callable:
    the sweep needs the device, which is not bound when a class body runs.
    """

    def cases():
        out = []
        for length in input_lengths:
            for cols in range(1, device_columns() + 1):
                for chans in [1] if channels is None else channels:
                    cores = cols * chans
                    tile = min(length // cores, tile_cap)
                    if tile * cores != length:
                        continue
                    kwargs = dict(size=length, num_aie_columns=cols)
                    if channels is not None:
                        kwargs["num_channels"] = chans
                    kwargs.update(tile_size=tile, **extra)
                    out.append(Case(kwargs, extensive=length != regular))
        return out

    return cases


def binary_elementwise_cases(input_lengths, tile_cap=None, regular=2048, **extra):
    """Cases for a binary elementwise operator, as :func:`channeled_unary_cases`."""

    def cases():
        out = []
        for length in input_lengths:
            for cols in range(1, device_columns() + 1):
                tile = length // cols
                if tile_cap is not None:
                    tile = min(tile, tile_cap)
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
