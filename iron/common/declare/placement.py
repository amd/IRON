# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Where an array's tiles go, as a tunable the tuner searches.

An operator names its placements and declares a field holding one name,
``placement: str = auto("memtiles", array=True, domain=PLACEMENT)``, with
``PLACEMENT = Placement({...})``. Each name is a `Pins`: how much of the
coordinates its ``array()`` writes it keeps for cores, memtiles and shims.
``array()`` asks ``PLACEMENT.pins(self.placement)`` for the tile of each
worker, link and shim end. The field is a plain string, so a profile entry
and the tuner's command line give it as they give any tunable, and it keys
the array and the design as any ``array=True`` field does. A placement the
placer or the router refuses is not measured (``narrowing.fitting``).
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from enum import Enum
from typing import Any

from aie.iron.device import Tile

from .domain import Domain


class Level(Enum):
    """How much of a tile's coordinates a placement keeps."""

    TILE = "tile"
    COLUMN = "column"
    FREE = "free"

    def tile(self, col: int, row: int) -> Tile | None:
        """The tile at (`col`, `row`) as this level keeps it: both
        coordinates, the column alone, or None, which aie.iron takes as the
        placer's choice of a tile of the kind it is passed for.
        """
        if self is Level.FREE:
            return None
        return Tile(col=col, row=row if self is Level.TILE else None)


@dataclass(frozen=True)
class Pins:
    """One placement of an array: the `Level` each kind of tile is held at.

    Attributes:
        cores: The workers' compute tiles.
        memtiles: The memtiles a split, join or forward runs on.
        shims: The shim tiles the operands' lanes stream through.
    """

    cores: Level = Level.TILE
    memtiles: Level = Level.TILE
    shims: Level = Level.TILE


@dataclass(frozen=True)
class Placement(Domain):
    """An operator's named placements, searched by name in declared order
    (the resolved one first).

    Attributes:
        named: The `Pins` of each placement, by name.
    """

    named: Mapping[str, Pins]

    def values(self, op: Any, dev: Any, name: str) -> tuple[Any, ...]:
        start = getattr(op, name)
        return (start, *(n for n in self.named if n != start))

    def pins(self, name: str) -> Pins:
        """The `Pins` placement `name` holds the array's tiles at.

        Raises:
            ValueError: `name` is not one of the placements.
        """
        if name not in self.named:
            raise ValueError(
                f"placement {name!r} is none of {', '.join(map(repr, self.named))}"
            )
        return self.named[name]
