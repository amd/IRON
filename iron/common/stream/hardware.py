# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Address an accelerator's compute tiles the way the array is laid out.

stream identifies a tile by an integer core id, which says nothing on its own:
which ids are compute tiles, and which column they sit in, is in the accelerator
description. This turns that description into columns of core ids, so a placement
is written in columns and no other IRON module has to know what an id means.

An operator that gives every layer the whole array (the layer-by-layer designs,
and a single layer sent to stream for a performance estimate) asks for
:attr:`ComputeArray.all_columns`. An operator that pipelines layers across the
array asks :meth:`ComputeArray.allocate` for a column budget per layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Iterable, Sequence

_COMPUTE_TYPE_SUFFIX = "compute"


@lru_cache(maxsize=None)
def _core_type(path: str) -> str:
    import yaml

    return yaml.safe_load(Path(path).read_text())["type"]


def _core_description(accelerator: Path, reference: str) -> Path:
    """Resolve a core reference, which is relative to the accelerator or to ``cores/``."""
    path = accelerator.parent / reference
    return (
        path if path.exists() else accelerator.parent / "cores" / Path(reference).name
    )


@dataclass(frozen=True)
class ComputeArray:
    """The accelerator's compute tiles, as core ids grouped by column."""

    columns: tuple[tuple[int, ...], ...]

    @classmethod
    def from_accelerator(cls, path) -> ComputeArray:
        import yaml

        path = Path(path)
        description = yaml.safe_load(path.read_text())
        coordinates = description.get("core_coordinates", {})
        by_column: dict[int, list[tuple[int, int]]] = {}
        for core_id, reference in description["cores"].items():
            if core_id not in coordinates:
                continue
            if not _core_type(str(_core_description(path, reference))).endswith(
                _COMPUTE_TYPE_SUFFIX
            ):
                continue
            column, row = coordinates[core_id]
            by_column.setdefault(column, []).append((row, core_id))
        return cls(
            tuple(
                tuple(core_id for _, core_id in sorted(rows))
                for _, rows in sorted(by_column.items())
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

    def cores(self, columns: Iterable[int]) -> tuple[int, ...]:
        """The core ids of ``columns``, column by column and row by row."""
        return tuple(core for column in columns for core in self.columns[column])

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
