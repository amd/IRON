# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The device's compute grid as columns of stream's integer core ids, derived from
mlir-aie's :class:`~aie.iron.device.Device`, so no other IRON module has to know what a
stream core id means."""

from __future__ import annotations

from dataclasses import dataclass
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


def array() -> ComputeArray:
    """The compute grid of the device being built for."""
    import aie.utils as aie_utils

    return ComputeArray.from_device(aie_utils.get_current_device())
