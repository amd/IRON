# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The shim DMA budget: how many columns an operator's streams may span."""

from __future__ import annotations

from aie.dialects.aie import (
    WireBundle,
    get_target_model,  # pyright: ignore[reportAttributeAccessIssue]  # not in _aie.pyi
)

from .field import Unresolvable
from .member import _Stream


def get_shim_dma_limit(dev) -> int:
    """Return the total number of ShimDMA output channels available on the device.

    Each shim tile exposes a fixed number of DMA source connections; summing
    across all shim tiles gives the device-wide ShimDMA budget.
    """
    tm = get_target_model(dev.resolve())
    return sum(
        tm.get_num_source_shim_mux_connections(col, row, WireBundle.DMA)
        for col in range(tm.columns())
        for row in range(tm.rows())
        if tm.is_shim_noc_or_pl_tile(col, row)
    )


def shim_columns(cls, dev, num_channels: int = 1) -> int:
    """How many of ``dev``'s columns a class's streams leave within the shim budget.

    One core per (column, channel) fills one fifo per input stream from the
    shim and drains one per output, so a column costs
    ``max(inputs, outputs) * num_channels`` channels in the busier
    direction. A ``replicate`` stream is shared by every column of a
    channel, so it is paid once per channel rather than per column.
    """
    streams = [m for m in cls._members if isinstance(m, _Stream)]
    shared = [m for m in streams if m.replicate]
    per_core = [m for m in streams if not m.replicate]
    directions = [m.direction for m in per_core]
    cost = max(directions.count("in"), directions.count("out")) * num_channels
    fixed = len(shared) * num_channels
    limit = get_shim_dma_limit(dev)
    if not cost:
        return dev.cols  # replicated streams alone: a column costs nothing more
    return max(1, min(dev.cols, (limit - fixed) // cost))


def check_shim_columns(obj, dev, cols: int, num_channels: int = 1) -> None:
    """Raise :class:`Unresolvable` if ``cols`` exceeds ``obj``'s shim budget."""
    allowed = shim_columns(type(obj), dev, num_channels)
    if cols > allowed:
        raise Unresolvable(
            f"{type(obj).__name__} with {cols} columns x {num_channels} "
            f"channels exceeds this device's shim DMA budget; "
            f"{allowed} columns fit"
        )
