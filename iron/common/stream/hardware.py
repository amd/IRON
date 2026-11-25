# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The device as stream-dse describes it: its hardware description and its compute grid."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from aie.dialects._aie_enum_gen import AIETileType
from aie.utils.compile.jit.operator import Unresolvable

# The stream-dse hardware description of each device, by its name.
ACCELERATORS = {"npu2": "whole_array_strix.yaml"}


def accelerator(dev) -> str:
    """Return the path of stream-dse's hardware description of ``dev``.

    Raises:
        Unresolvable: stream-dse describes no such device.
    """
    import stream  # pyright: ignore[reportMissingImports]

    name = ACCELERATORS.get(dev.name)
    if name is None:
        raise Unresolvable(
            f"stream-dse has no hardware description of {dev.name}, only of "
            f"{sorted(ACCELERATORS)}"
        )
    return str(Path(stream.__file__).parent / "inputs" / "aie" / "hardware" / name)


@dataclass(frozen=True)
class ComputeArray:
    """The columns of the device and the compute tiles in each."""

    num_columns: int
    num_rows: int

    @classmethod
    def from_device(cls, device) -> ComputeArray:
        """Return the compute grid of an mlir-aie ``Device``."""
        rows = sum(
            device.get_tile_type(0, row) == AIETileType.CoreTile
            for row in range(device.rows)
        )
        return cls(device.cols, rows)
