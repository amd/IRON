# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The device's compute tiles as columns of stream core ids, so a placement
is written in columns and rows.
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

        stream numbers tiles ``column * rows + row`` over the whole grid, shim
        and memory rows included.
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
        """The core ids of ``columns``, column by column; ``rows`` takes some rows."""
        selected = range(self.num_rows) if rows is None else rows
        return tuple(
            self.columns[column][row] for column in columns for row in selected
        )

    def allocate(self, budgets: Sequence[int]) -> tuple[tuple[int, ...], ...]:
        """Consecutive, disjoint column ranges, one per budget, so layers pipeline."""
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
