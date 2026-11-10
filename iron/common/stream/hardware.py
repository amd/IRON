# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The device's compute tiles as stream-dse's core ids, read from mlir-aie's ``Device``.

No other module has to know what a stream-dse core id means.
"""

from __future__ import annotations

from dataclasses import dataclass

from aie.dialects._aie_enum_gen import AIETileType


@dataclass(frozen=True)
class ComputeArray:
    """The device's compute tiles, as stream-dse core ids grouped by column."""

    columns: tuple[tuple[int, ...], ...]

    @classmethod
    def from_device(cls, device) -> ComputeArray:
        """Return the compute grid of an mlir-aie ``Device``.

        stream-dse numbers tiles ``column * rows + row`` over the whole grid,
        so the stride is the device's row count, shim and memory rows
        included.
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
