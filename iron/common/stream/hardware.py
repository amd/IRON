# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Address the device's compute tiles the way the array is laid out.

stream identifies a tile by an integer core id, which says nothing on its own.
IRON already describes the device: mlir-aie's :class:`~aie.iron.device.Device`
knows the grid and the type of every tile in it. This turns that into columns of
core ids, so a placement is written in columns and rows and no other IRON module
has to know what a stream core id means.

An operator that gives every layer the whole array (the layer-by-layer designs,
and a single layer sent to stream for a performance estimate) asks for
:attr:`ComputeArray.all_columns`. An operator that pipelines layers across the
array asks :meth:`ComputeArray.allocate` for a column budget per layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from aie.iron.device.device import AIETileType


@dataclass(frozen=True)
class ComputeArray:
    """The device's compute tiles, as stream core ids grouped by column."""

    columns: tuple[tuple[int, ...], ...]

    @classmethod
    def from_device(cls, device) -> ComputeArray:
        """Read the compute grid from an mlir-aie ``Device``.

        stream numbers tiles ``column * rows + row`` across the device's whole
        grid, so the stride is the device's row count -- shim and memory rows
        included -- and not the number of compute rows.
        """
        return cls(
            tuple(
                tuple(
                    column * device.rows + row
                    for row in range(device.rows)
                    if device.get_tile_type(column, row) == AIETileType.CoreTile
                )
                for column in range(device.cols)
            )
        )

    @property
    def num_columns(self) -> int:
        return len(self.columns)

    @property
    def num_rows(self) -> int:
        return len(self.columns[0]) if self.columns else 0

    @property
    def all_columns(self) -> tuple[int, ...]:
        return tuple(range(self.num_columns))

    def cores(
        self, columns: Iterable[int], rows: Sequence[int] | None = None
    ) -> tuple[int, ...]:
        """The core ids of ``columns``, column by column and row by row.

        ``rows`` takes only some rows of each column, for a layer that wants the
        array's width but not its full depth -- an elementwise layer with one
        worker per column, as IRON's own channeled operators place it.
        """
        selected = range(self.num_rows) if rows is None else rows
        return tuple(
            self.columns[column][row] for column in columns for row in selected
        )

    def allocate(self, budgets: Sequence[int]) -> tuple[tuple[int, ...], ...]:
        """Consecutive, disjoint column ranges, one per budget.

        Layers placed on disjoint columns pipeline across steady-state
        iterations instead of taking turns on the same tiles.
        """
        if sum(budgets) > self.num_columns:
            raise ValueError(
                f"column budgets {list(budgets)} need {sum(budgets)} columns, "
                f"the array has {self.num_columns}"
            )
        ranges, first = [], 0
        for budget in budgets:
            ranges.append(tuple(range(first, first + budget)))
            first += budget
        return tuple(ranges)
